"""
Shared utility functions for Feasibility Test Suite across 50 US Cities.
"""
import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize_scalar

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"

# List of 50 US cities in data directory
ALL_50_CITIES = sorted([
    d.name for d in DATA_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")
])

def load_city_raw(city_name: str):
    """Load raw city csv files."""
    base = DATA_DIR / city_name
    meta = pd.read_csv(base / "meta.csv")
    od = pd.read_csv(base / "pairs" / "od.csv")
    
    dist_file = base / "pairs" / "distance.csv"
    if not dist_file.exists():
        dist_file = base / "pairs" / "osm_path.csv"
    dist = pd.read_csv(dist_file)
    dist.columns = [c.lower() for c in dist.columns]
    if "distance" not in dist.columns:
        num_cols = [c for c in dist.columns if c not in ("o_idx", "d_idx")]
        dist = dist.rename(columns={num_cols[0]: "distance"})
    if dist["distance"].max() > 1000:
        dist["distance"] = dist["distance"] / 1000.0

    census = pd.read_csv(base / "nodes" / "census.csv")
    poi = pd.read_csv(base / "nodes" / "poi.csv")
    
    road_file = base / "nodes" / "road.csv"
    if road_file.exists():
        road = pd.read_csv(road_file)
    else:
        road = pd.DataFrame({"idx": meta["idx"], "road_density": 1e-4})
        
    return {
        "city": city_name,
        "meta": meta,
        "od": od,
        "dist": dist,
        "census": census,
        "poi": poi,
        "road": road
    }

def process_city_data(city_name: str):
    """Process a city into node features dataframe and pair trip dataframe."""
    raw = load_city_raw(city_name)
    meta = raw["meta"].copy()
    census = raw["census"].copy()
    poi = raw["poi"].copy()
    road = raw["road"].copy()
    od = raw["od"].copy()
    dist = raw["dist"].copy()

    # Merge node features
    nodes = meta[["idx", "area_km2"]].merge(
        census[["idx", "total_population"]], on="idx", how="left"
    ).merge(
        poi[["idx", "total_pois"]], on="idx", how="left"
    ).merge(
        road[["idx", "road_density"]], on="idx", how="left"
    ).fillna(0.0)
    
    nodes["total_population"] = nodes["total_population"].clip(lower=0.0)
    nodes["total_pois"] = nodes["total_pois"].clip(lower=0.0)
    nodes["area_km2"] = nodes["area_km2"].clip(lower=1e-4)
    nodes["road_density"] = nodes["road_density"].clip(lower=0.0)

    # Compute observed O_i (outflow) and A_j (inflow) from OD
    O_i_series = od.groupby("o_idx")["trip_count"].sum().rename("O_i")
    A_j_series = od.groupby("d_idx")["trip_count"].sum().rename("A_j")

    nodes = nodes.merge(O_i_series, left_on="idx", right_index=True, how="left").fillna({"O_i": 0.0})
    nodes = nodes.merge(A_j_series, left_on="idx", right_index=True, how="left").fillna({"A_j": 0.0})

    # Merge OD with distance
    df = od.merge(dist[["o_idx", "d_idx", "distance"]], on=["o_idx", "d_idx"], how="inner")
    df["d_clamped"] = df["distance"].clip(lower=0.01)
    
    # Merge node A_j into pairs
    df = df.merge(nodes[["idx", "A_j"]], left_on="d_idx", right_on="idx", how="left")
    df["A_j_clamped"] = df["A_j"].clip(lower=1e-4)

    return nodes, df

def fit_beta_od_mle(df: pd.DataFrame):
    """Fit beta parameter directly on full OD matrix using Poisson/Multinomial MLE."""
    d = df["d_clamped"].values
    A = df["A_j_clamped"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values

    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)

    def neg_log_like(beta_val):
        beta = float(beta_val)
        log_f = np.log(A) - beta * d
        lf_max = np.full(n_o, -np.inf)
        np.maximum.at(lf_max, o_idx_mapped, log_f)
        shifted = np.exp(log_f - lf_max[o_idx_mapped])
        sum_exp = np.zeros(n_o)
        np.add.at(sum_exp, o_idx_mapped, shifted)
        log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
        log_p = log_f - log_denom[o_idx_mapped]
        return -float(np.sum(trips * log_p))

    res = minimize_scalar(neg_log_like, bounds=(0.0001, 3.0), method="bounded")
    return float(res.x)

def fit_beta_tld_mle(df: pd.DataFrame, K: int = 20):
    """Fit beta parameter purely from aggregate Travel-Length Distribution (TLD)."""
    d = df["d_clamped"].values
    A = df["A_j_clamped"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values

    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)

    d_max = d.max()
    edges = np.linspace(0, d_max, K + 1)
    edges[-1] = np.inf
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)

    # Aggregate trip count per distance bin (TLD)
    y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
    tot_trips = y_k.sum()
    if tot_trips == 0:
        return 0.1

    def neg_tld_log_like(beta_val):
        beta = float(beta_val)
        log_f = np.log(A) - beta * d
        lf_max = np.full(n_o, -np.inf)
        np.maximum.at(lf_max, o_idx_mapped, log_f)
        shifted = np.exp(log_f - lf_max[o_idx_mapped])
        sum_exp = np.zeros(n_o)
        np.add.at(sum_exp, o_idx_mapped, shifted)
        log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
        log_p = log_f - log_denom[o_idx_mapped]
        
        # Expected trips per pair
        p_ij = np.exp(log_p)
        # Binned expected trip probability
        p_k = np.bincount(bin_idx, weights=p_ij, minlength=K).astype(float)
        p_k_tot = p_k.sum()
        if p_k_tot < 1e-12:
            return 1e12
        p_k = (p_k / p_k_tot).clip(1e-15)
        return -float(np.sum(y_k * np.log(p_k)))

    res = minimize_scalar(neg_tld_log_like, bounds=(0.0001, 3.0), method="bounded")
    return float(res.x)

def calculate_cpc(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Calculate Common Part of Commuters (CPC)."""
    denom = np.sum(actual) + np.sum(predicted)
    if denom < 1e-12:
        return 0.0
    numer = 2.0 * np.sum(np.minimum(actual, predicted))
    return float(numer / denom)

def predict_gravity_od(df: pd.DataFrame, beta: float, custom_O: np.ndarray = None, custom_A: np.ndarray = None, node_ids: np.ndarray = None):
    """Predict OD trip matrix given beta and optional custom O_i / A_j arrays."""
    d = df["d_clamped"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values

    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)

    if custom_A is not None and node_ids is not None:
        idx_to_pos = {int(nid): pos for pos, nid in enumerate(node_ids)}
        d_idx = df["d_idx"].values
        d_pos = np.array([idx_to_pos.get(int(idx), 0) for idx in d_idx])
        A = custom_A[d_pos].clip(lower=1e-4)
    else:
        A = df["A_j_clamped"].values

    log_f = np.log(A) - beta * d
    lf_max = np.full(n_o, -np.inf)
    np.maximum.at(lf_max, o_idx_mapped, log_f)
    shifted = np.exp(log_f - lf_max[o_idx_mapped])
    sum_exp = np.zeros(n_o)
    np.add.at(sum_exp, o_idx_mapped, shifted)
    log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
    p_ij = np.exp(log_f - log_denom[o_idx_mapped])

    if custom_O is not None and node_ids is not None:
        idx_to_pos = {int(nid): pos for pos, nid in enumerate(node_ids)}
        o_pos = np.array([idx_to_pos.get(int(idx), 0) for idx in unique_o])
        O_i_vals = custom_O[o_pos]
        T_hat = O_i_vals[o_idx_mapped] * p_ij
    else:
        O_i_orig = np.zeros(n_o)
        np.add.at(O_i_orig, o_idx_mapped, trips)
        T_hat = O_i_orig[o_idx_mapped] * p_ij

    return T_hat
