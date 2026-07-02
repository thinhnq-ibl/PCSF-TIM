"""Shared utilities: data loading, metrics, normalization."""
from __future__ import annotations
import os
import numpy as np
import pandas as pd
from typing import Optional

DATA_ROOT = os.path.join(os.path.dirname(__file__), "..", "data")


# ===================== DATA LOADING =====================

def load_city(city: str, use_network_distance: bool = False) -> dict:
    """Load all data for one city.

    Returns dict with:
        meta: DataFrame (idx, lon, lat, area_km2)
        od:   DataFrame (o_idx, d_idx, trip_count)
        dist: DataFrame (o_idx, d_idx, distance)  -- in km
        census: DataFrame (idx, total_population, ...)
        poi:    DataFrame (idx, total_pois, ...)
    """
    base = os.path.join(DATA_ROOT, city)
    meta = pd.read_csv(os.path.join(base, "meta.csv"))
    od = pd.read_csv(os.path.join(base, "pairs", "od.csv"))

    dist_file = "osm_path.csv" if use_network_distance else "distance.csv"
    dist = pd.read_csv(os.path.join(base, "pairs", dist_file))
    # Normalize column names; distance may be column 'distance' or other
    dist.columns = [c.lower() for c in dist.columns]
    if "distance" not in dist.columns:
        # find numeric column besides o_idx, d_idx
        num_cols = [c for c in dist.columns if c not in ("o_idx", "d_idx")]
        dist = dist.rename(columns={num_cols[0]: "distance"})
    # Ensure km
    if dist["distance"].max() > 1000:  # likely meters
        dist["distance"] = dist["distance"] / 1000.0

    census = pd.read_csv(os.path.join(base, "nodes", "census.csv"))
    poi = pd.read_csv(os.path.join(base, "nodes", "poi.csv"))
    return {"city": city, "meta": meta, "od": od, "dist": dist,
            "census": census, "poi": poi}


def build_pairs_dataframe(city_data: dict,
                          attr_mode: str = "poi_pop_avg",
                          min_distance: float = 0.1,
                          adaptive_self: bool = False) -> pd.DataFrame:
    """Build merged dataframe with all needed columns.

    Columns: o_idx, d_idx, trip_count, distance, d_clamped, A_j, O_i, P_i, P_j, POI_i, POI_j
    attr_mode: how to compute A_j
        - 'poi_pop_avg': average of normalized POI and Pop
        - 'poi': POI count normalized
        - 'pop': Population normalized
        - 'poi_categories': weighted POI categories (office, food, etc.)
    """
    od = city_data["od"].copy()
    dist = city_data["dist"][["o_idx", "d_idx", "distance"]].copy()
    meta = city_data["meta"]
    census = city_data["census"]
    poi = city_data["poi"]

    # Merge OD with distance (outer would lose info; inner is fine since od is sparse)
    df = od.merge(dist, on=["o_idx", "d_idx"], how="left")
    df["distance"] = df["distance"].fillna(0.0)

    # Compute O_i
    O = df.groupby("o_idx")["trip_count"].sum().rename("O_i")
    df = df.merge(O, left_on="o_idx", right_index=True)

    # Build node-level features
    nodes = meta[["idx", "area_km2"]].merge(
        census[["idx", "total_population"]], on="idx", how="left"
    ).merge(
        poi[["idx", "total_pois"]], on="idx", how="left"
    )
    nodes["total_population"] = nodes["total_population"].fillna(0)
    nodes["total_pois"] = nodes["total_pois"].fillna(0)

    # Compute attractiveness A_j
    pop = nodes["total_population"].values.astype(float)
    pois = nodes["total_pois"].values.astype(float)

    def minmax(x):
        rng = x.max() - x.min()
        if rng < 1e-9:
            return np.zeros_like(x)
        return (x - x.min()) / rng

    if attr_mode == "poi_pop_avg":
        A = (minmax(pop) + minmax(pois)) / 2.0
    elif attr_mode == "poi":
        A = minmax(pois)
    elif attr_mode == "pop":
        A = minmax(pop)
    elif attr_mode == "poi_categories":
        # weighted: jobs more important
        cols = []
        weights = {}
        for c, w in [("office", 3.0), ("commercial", 2.0), ("food_restaurant", 1.5),
                      ("education_higher", 2.0), ("shopping_supermarket", 1.0)]:
            if c in poi.columns:
                cols.append(c); weights[c] = w
        if not cols:
            A = minmax(pois)
        else:
            poi_subset = poi[["idx"] + cols].set_index("idx").reindex(nodes["idx"]).fillna(0)
            A = np.zeros(len(nodes))
            for c in cols:
                A = A + weights[c] * minmax(poi_subset[c].values)
            A = A / sum(weights.values())
    elif attr_mode == "jobs":
        # Only job-generating POIs (where people go to work/spend)
        cols = [c for c in ["office", "commercial", "industrial",
                             "education_higher", "healthcare_hospital",
                             "shopping_mall"] if c in poi.columns]
        sub = poi[["idx"] + cols].set_index("idx").reindex(nodes["idx"]).fillna(0)
        A = minmax(sub.sum(axis=1).values)
    elif attr_mode == "jobs_pop":
        # Avg of jobs and pop
        cols = [c for c in ["office", "commercial", "industrial",
                             "education_higher", "healthcare_hospital",
                             "shopping_mall"] if c in poi.columns]
        sub = poi[["idx"] + cols].set_index("idx").reindex(nodes["idx"]).fillna(0)
        A = (minmax(sub.sum(axis=1).values) + minmax(pop)) / 2.0
    elif attr_mode == "employment_pop":
        # employment_pop mode is disabled due to strict constraint: NEVER use employment_rate
        raise ValueError("employment_pop mode is disabled because employment_rate is forbidden.")
    elif attr_mode == "all_poi_sum":
        # Sum all individual POI category counts (avoid total_pois which may double count)
        skip = {"idx", "total_pois", "total_pois_density"}
        cols = [c for c in poi.columns
                if c not in skip and not c.endswith("_density")]
        sub = poi[["idx"] + cols].set_index("idx").reindex(nodes["idx"]).fillna(0)
        A = (minmax(sub.sum(axis=1).values) + minmax(pop)) / 2.0
    else:
        raise ValueError(f"Unknown attr_mode: {attr_mode}")

    nodes["A_j"] = A
    nodes["P"] = pop
    nodes["POI"] = pois

    # Merge A_j (using d_idx)
    df = df.merge(nodes[["idx", "A_j", "P", "POI", "area_km2"]].rename(
        columns={"idx": "d_idx", "A_j": "A_j", "P": "P_j", "POI": "POI_j",
                 "area_km2": "area_j"}
    ), on="d_idx", how="left")
    # Also merge P_i, POI_i for radiation
    df = df.merge(nodes[["idx", "P", "POI", "area_km2"]].rename(
        columns={"idx": "o_idx", "P": "P_i", "POI": "POI_i", "area_km2": "area_i"}
    ), on="o_idx", how="left")

    # Distance clamping
    if adaptive_self:
        # For self-flow (i==j), use zone radius √(area/π); else clamp to min
        zone_radius = np.sqrt(df["area_i"] / np.pi)
        is_self = df["o_idx"] == df["d_idx"]
        df["d_clamped"] = np.where(is_self, zone_radius,
                                    np.maximum(df["distance"], min_distance))
    else:
        df["d_clamped"] = np.maximum(df["distance"], min_distance)

    # Fill NaN
    for c in ["A_j", "P_i", "P_j", "POI_i", "POI_j"]:
        df[c] = df[c].fillna(0)

    return df.reset_index(drop=True)


# ===================== METRICS =====================

def cpc(pred: np.ndarray, actual: np.ndarray) -> float:
    """Common Part of Commuters (Sørensen-Dice)."""
    pred = np.asarray(pred, dtype=float)
    actual = np.asarray(actual, dtype=float)
    s = pred.sum() + actual.sum()
    if s < 1e-9:
        return 0.0
    return 2.0 * np.minimum(pred, actual).sum() / s


def rmse(pred: np.ndarray, actual: np.ndarray) -> float:
    return float(np.sqrt(np.mean((pred - actual) ** 2)))


def r2_log(pred: np.ndarray, actual: np.ndarray) -> float:
    lp = np.log1p(pred)
    la = np.log1p(actual)
    ss_res = np.sum((lp - la) ** 2)
    ss_tot = np.sum((la - la.mean()) ** 2)
    if ss_tot < 1e-9:
        return 0.0
    return float(1.0 - ss_res / ss_tot)


def evaluate(pred: np.ndarray, actual: np.ndarray) -> dict:
    return {
        "CPC": cpc(pred, actual),
        "RMSE": rmse(pred, actual),
        "R2_log": r2_log(pred, actual),
    }


# ===================== NORMALIZATION (Balancing K_i) =====================

def apply_origin_normalization(df: pd.DataFrame, T_pred: np.ndarray) -> np.ndarray:
    """Rescale predictions so Σ_j T_ij = O_i for each origin."""
    tmp = df[["o_idx", "O_i"]].copy()
    tmp["T_pred"] = T_pred
    sum_pred = tmp.groupby("o_idx")["T_pred"].transform("sum")
    scale = tmp["O_i"] / np.maximum(sum_pred, 1e-9)
    return T_pred * scale.values


# ===================== SCALE-INVARIANT FEATURE EXTRACTION =====================

def load_road_density(city: str) -> dict:
    p = os.path.join(DATA_ROOT, city, "nodes", "road.csv")
    if not os.path.exists(p):
        return {}
    rd = pd.read_csv(p)
    return dict(zip(rd["idx"].astype(int).values, rd["road_density"].values))


def build_city_features_improved(df: pd.DataFrame, road_map: dict, road_impute: float, feature_mode: str = "relative") -> tuple[np.ndarray, np.ndarray, list]:
    EPS = 1e-6
    df = df.copy() # Avoid modifying original in-place
    
    o = df[["o_idx", "P_i", "POI_i", "area_i"]].drop_duplicates("o_idx")
    o.columns = ["z", "P", "POI", "area"]
    d = df[["d_idx", "P_j", "POI_j", "area_j"]].drop_duplicates("d_idx")
    d.columns = ["z", "P", "POI", "area"]
    z = pd.concat([o, d]).drop_duplicates("z").set_index("z")
    
    P = np.nan_to_num(z["P"].values, nan=0.0).clip(EPS)
    POI = np.nan_to_num(z["POI"].values, nan=0.0).clip(0.0) + 1.0
    area = np.nan_to_num(z["area"].values, nan=0.01).clip(EPS)
    rd = np.array([road_map.get(int(zid), road_impute) for zid in z.index], float)
    rd = np.nan_to_num(rd, nan=road_impute).clip(0.0)
    
    base_feats = {
        int(zid): np.array([
            np.log(P[i] + EPS),
            np.log(POI[i] + EPS),
            np.log(area[i] + EPS),
            np.log(P[i] / area[i] + EPS),
            np.log(POI[i] / area[i] + EPS),
            np.log(rd[i] + 1e-9)
        ]) for i, zid in enumerate(z.index)
    }
    
    df_unique_dest = df[["d_idx", "P_j", "POI_j"]].drop_duplicates("d_idx").set_index("d_idx")
    dest_attr = (df_unique_dest["P_j"] + df_unique_dest["POI_j"]).to_dict()
    
    df["dest_attr"] = df["d_idx"].map(dest_attr).fillna(0.0)
    df["access_contrib"] = df["dest_attr"] / df["d_clamped"].clip(1e-3)
    access_map = df.groupby("o_idx")["access_contrib"].sum().to_dict()
    
    total_P = float(P.sum())
    total_POI = float(POI.sum())
    total_area = float(area.sum())
    total_rd = float(rd.sum())
    
    avg_P_density = total_P / (total_area + EPS)
    avg_POI_density = total_POI / (total_area + EPS)
    avg_rd = total_rd / (len(z) + EPS)
    
    poi_density = POI / area
    cbd_idx = z.index[np.argmax(poi_density)]
    cbd_df = df[df["d_idx"] == cbd_idx][["o_idx", "d_clamped"]].set_index("o_idx")
    cbd_dist_map = cbd_df["d_clamped"].to_dict()
    
    O = df.groupby("o_idx")["trip_count"].sum()
    orig_zones = sorted(O.index.tolist())
    
    # City-wide statistical parameters (mean and std) of base features
    all_base_feats = np.array(list(base_feats.values()))
    city_mean = all_base_feats.mean(axis=0)
    city_std = all_base_feats.std(axis=0) + EPS
    
    X_out, logO, kept = [], [], []
    for z_id in orig_zones:
        if z_id not in base_feats:
            continue
            
        base_vec = base_feats[z_id]
        
        # Apply city-wide statistical scaling instead of neighbor smoothing
        scaled_vec = (base_vec - city_mean) / city_std
        feats_12 = np.concatenate([base_vec, scaled_vec])
        
        P_val = z.loc[z_id, "P"]
        POI_val = z.loc[z_id, "POI"]
        area_val = z.loc[z_id, "area"]
        rd_val = road_map.get(int(z_id), road_impute)
        
        P_share = P_val / (total_P + EPS)
        POI_share = POI_val / (total_POI + EPS)
        area_share = area_val / (total_area + EPS)
        rd_share = rd_val / (total_rd + EPS)
        
        P_density = P_val / (area_val + EPS)
        POI_density = POI_val / (area_val + EPS)
        
        P_density_ratio = P_density / (avg_P_density + EPS)
        POI_density_ratio = POI_density / (avg_POI_density + EPS)
        rd_ratio = rd_val / (avg_rd + EPS)
        
        access_val = access_map.get(z_id, 0.0)
        cbd_dist_val = cbd_dist_map.get(z_id, 10.0)
        
        if feature_mode == "relative":
            extra_feats = [
                np.log(P_share + 1e-12),
                np.log(POI_share + 1e-12),
                np.log(area_share + 1e-12),
                np.log(rd_share + 1e-12),
                np.log(access_val + 1e-12),
                np.log(cbd_dist_val + 1e-6),
                np.log(P_density_ratio + EPS),
                np.log(POI_density_ratio + EPS),
                np.log(rd_ratio + EPS)
            ]
        else: # super_rich
            extra_feats = [
                np.log(P_share + 1e-12),
                np.log(POI_share + 1e-12),
                np.log(area_share + 1e-12),
                np.log(rd_share + 1e-12),
                np.log(access_val + 1e-12),
                np.log(cbd_dist_val + 1e-6),
                np.log(total_P),
                np.log(total_POI),
                np.log(total_area),
                np.log(P_density_ratio + EPS),
                np.log(POI_density_ratio + EPS),
                np.log(rd_ratio + EPS)
            ]
            
        full_feats = np.concatenate([feats_12, extra_feats])
        X_out.append(full_feats)
        logO.append(np.log(max(float(O[z_id]), 1.0)))
        kept.append(z_id)
        
    return np.array(X_out), np.array(logO), kept

