"""
Paper 2 Phase 2 Feasibility Gate: Structural Transferability Suite
Tests 1-4:
- Test 1: Full 10x10 Pairwise Source -> Target OD Transfer Matrix (C_st)
- Test 2: Oracle Best-Source Selection Gain (ΔCPC_oracle_source)
- Test 3: Structural Similarity vs. Transfer Performance Correlation (corr(Sim_st, C_st))
- Test 4: Nearest Structural Source (s*) vs. Global/Random Baseline Performance
"""

import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import spearmanr, pearsonr
from scipy.spatial.distance import cdist
from scipy.optimize import minimize_scalar

# Setup paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Selected 10 representative cities
TEST_CITIES = sorted([
    "Atlanta", "Austin", "Boston", "Chicago", "Dallas",
    "Denver", "Los_Angeles", "Miami", "Seattle", "Washington_DC"
])

def compute_cpc(T_pred, T_true):
    """Compute Common Part of Commuters (CPC)."""
    sum_pred = np.sum(T_pred)
    sum_true = np.sum(T_true)
    if sum_pred <= 0 or sum_true <= 0:
        return 0.0
    return float(2.0 * np.sum(np.minimum(T_pred, T_true)) / (sum_pred + sum_true))

def load_and_calibrate_city(city: str):
    """Load city data, extract structural feature vector R_S, and fit local beta."""
    base = DATA_DIR / city
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
    road_density_mean = 1e-4
    if road_file.exists():
        road = pd.read_csv(road_file)
        if "road_density" in road.columns:
            road_density_mean = float(road["road_density"].mean())

    nodes = meta[["idx", "area_km2"]].merge(
        census[["idx", "total_population"]], on="idx", how="left"
    ).merge(
        poi[["idx", "total_pois"]], on="idx", how="left"
    ).fillna(0.0)

    n_nodes = len(nodes)
    
    T_true = np.zeros((n_nodes, n_nodes))
    for _, row in od.iterrows():
        i, j, c = int(row["o_idx"]), int(row["d_idx"]), float(row["trip_count"])
        if i < n_nodes and j < n_nodes:
            T_true[i, j] = c
            
    D = np.zeros((n_nodes, n_nodes))
    for _, row in dist.iterrows():
        i, j, d = int(row["o_idx"]), int(row["d_idx"]), float(row["distance"])
        if i < n_nodes and j < n_nodes:
            D[i, j] = max(d, 0.01)

    O_i = T_true.sum(axis=1)
    pop = nodes["total_population"].values.astype(float)
    pois = nodes["total_pois"].values.astype(float)
    pop_norm = pop / (pop.max() + 1e-6)
    poi_norm = pois / (pois.max() + 1e-6)
    A_j = 0.5 * (pop_norm + poi_norm) + 1e-4

    # Fit local beta parameter
    def neg_log_like(beta_val):
        beta = float(beta_val)
        log_f = np.log(A_j[None, :]) - beta * D
        lf_max = log_f.max(axis=1, keepdims=True)
        exp_f = np.exp(log_f - lf_max)
        denom = exp_f.sum(axis=1, keepdims=True)
        P_ij = exp_f / denom
        log_p = np.log(np.maximum(P_ij, 1e-300))
        return -float(np.sum(T_true * log_p))

    res = minimize_scalar(neg_log_like, bounds=(0.0001, 3.0), method="bounded")
    beta_local = float(res.x)

    # Urban Structure Feature Vector R_S
    total_pop = float(pop.sum())
    total_pois = float(pois.sum())
    total_area = float(nodes["area_km2"].sum())
    pop_density = total_pop / max(total_area, 1e-4)
    poi_density = total_pois / max(total_area, 1e-4)
    mean_dist = float(D[D > 0].mean())
    median_tract_area = float(nodes["area_km2"].median())
    
    r_s_vec = np.array([
        np.log1p(total_pop),
        np.log1p(total_pois),
        np.log1p(total_area),
        np.log1p(pop_density),
        np.log1p(poi_density),
        mean_dist,
        median_tract_area,
        road_density_mean
    ])

    return {
        "city": city,
        "n_nodes": n_nodes,
        "T_true": T_true,
        "D": D,
        "O_i": O_i,
        "A_j": A_j,
        "beta_local": beta_local,
        "r_s_vec": r_s_vec
    }

def run_structural_transfer_gate():
    print("=" * 70)
    print("PAPER 2 PHASE 2 FEASIBILITY GATE: STRUCTURAL TRANSFERABILITY")
    print("=" * 70)

    city_data = {}
    for city in TEST_CITIES:
        print(f"Loading & calibrating {city}...")
        city_data[city] = load_and_calibrate_city(city)

    N = len(TEST_CITIES)
    C_matrix = np.zeros((N, N)) # C_st: source s -> target t

    # 1. Compute Pairwise Cross-City Transfer Matrix C_st
    for i, s_city in enumerate(TEST_CITIES):
        s_beta = city_data[s_city]["beta_local"]
        for j, t_city in enumerate(TEST_CITIES):
            t_data = city_data[t_city]
            T_true = t_data["T_true"]
            O_i = t_data["O_i"]
            A_j = t_data["A_j"]
            D = t_data["D"]

            # Predict target flow using source beta
            log_f = np.log(A_j[None, :]) - s_beta * D
            lf_max = log_f.max(axis=1, keepdims=True)
            exp_f = np.exp(log_f - lf_max)
            P_pred = exp_f / exp_f.sum(axis=1, keepdims=True)
            T_pred = O_i[:, None] * P_pred

            C_matrix[i, j] = compute_cpc(T_pred, T_true)

    # 2. Compute Structural Similarity Matrix S_st
    R_S_matrix = np.array([city_data[c]["r_s_vec"] for c in TEST_CITIES])
    # Standardize features (z-score)
    R_S_norm = (R_S_matrix - R_S_matrix.mean(axis=0)) / (R_S_matrix.std(axis=0) + 1e-6)
    
    # Cosine Similarity Matrix
    dot_prod = R_S_norm @ R_S_norm.T
    norms = np.linalg.norm(R_S_norm, axis=1, keepdims=True)
    S_matrix = dot_prod / (norms @ norms.T + 1e-12)

    # 3. Compute Global Leave-One-Out Baseline per Target
    cpc_global = np.zeros(N)
    for j, t_city in enumerate(TEST_CITIES):
        # Average beta of 9 source cities
        sources = [i for i in range(N) if i != j]
        avg_beta = np.mean([city_data[TEST_CITIES[i]]["beta_local"] for i in sources])
        
        t_data = city_data[t_city]
        log_f = np.log(t_data["A_j"][None, :]) - avg_beta * t_data["D"]
        lf_max = log_f.max(axis=1, keepdims=True)
        exp_f = np.exp(log_f - lf_max)
        P_pred = exp_f / exp_f.sum(axis=1, keepdims=True)
        T_pred = t_data["O_i"][:, None] * P_pred
        cpc_global[j] = compute_cpc(T_pred, t_data["T_true"])

    # Extract off-diagonal pairs for statistical testing
    pairs_sim = []
    pairs_cpc = []
    for i in range(N):
        for j in range(N):
            if i != j:
                pairs_sim.append(S_matrix[i, j])
                pairs_cpc.append(C_matrix[i, j])

    pairs_sim = np.array(pairs_sim)
    pairs_cpc = np.array(pairs_cpc)

    corr_spearman, p_spearman = spearmanr(pairs_sim, pairs_cpc)
    corr_pearson, p_pearson = pearsonr(pairs_sim, pairs_cpc)

    # 4. Nearest Structural Source Evaluation
    cpc_nearest = np.zeros(N)
    cpc_random = np.zeros(N)
    cpc_oracle = np.zeros(N)

    for j in range(N):
        sources = [i for i in range(N) if i != j]
        # Nearest structural source s*
        s_star = max(sources, key=lambda i: S_matrix[i, j])
        cpc_nearest[j] = C_matrix[s_star, j]
        
        # Oracle best source
        cpc_oracle[j] = max([C_matrix[i, j] for i in sources])
        
        # Mean across random sources
        cpc_random[j] = np.mean([C_matrix[i, j] for i in sources])

    # Compute Summary Performance Metrics
    mean_self = np.mean([C_matrix[i, i] for i in range(N)])
    mean_oracle_best = np.mean(cpc_oracle)
    mean_nearest = np.mean(cpc_nearest)
    mean_global = np.mean(cpc_global)
    mean_random = np.mean(cpc_random)

    win_rate_over_global = np.mean(cpc_nearest >= cpc_global) * 100.0
    win_rate_over_random = np.mean(cpc_nearest >= cpc_random) * 100.0

    print("\n" + "=" * 70)
    print("RESULTS: STRUCTURAL TRANSFERABILITY FEASIBILITY GATE")
    print("=" * 70)
    print(f"  1. Structural Similarity vs. Transfer Performance Correlation:")
    print(f"     - Spearman rho = {corr_spearman:+.4f} (p = {p_spearman:.4e})")
    print(f"     - Pearson r    = {corr_pearson:+.4f} (p = {p_pearson:.4e})")
    print("-" * 70)
    print(f"  2. OD Transfer Performance Ladder across 10 Cities:")
    print(f"     - Local Self-Calibration (Upper Bound) : {mean_self:.4f}")
    print(f"     - Oracle Best-Source Selection         : {mean_oracle_best:.4f} (Δ vs Global: {mean_oracle_best - mean_global:+.4f})")
    print(f"     - Nearest Structural Source (s*)      : {mean_nearest:.4f} (Δ vs Global: {mean_nearest - mean_global:+.4f})")
    print(f"     - Pooled Global Baseline               : {mean_global:.4f}")
    print(f"     - Random Source Selection              : {mean_random:.4f}")
    print("-" * 70)
    print(f"  3. Win-Rate of Nearest Structural Source:")
    print(f"     - Outperforms Pooled Global Model : {win_rate_over_global:.1f}% of cities")
    print(f"     - Outperforms Random Source       : {win_rate_over_random:.1f}% of cities")
    print("=" * 70)

    # Save detailed matrix results
    df_c_matrix = pd.DataFrame(C_matrix, index=TEST_CITIES, columns=TEST_CITIES)
    df_c_matrix.to_csv(OUTPUT_DIR / "paper2_cross_city_transfer_matrix.csv")

    df_s_matrix = pd.DataFrame(S_matrix, index=TEST_CITIES, columns=TEST_CITIES)
    df_s_matrix.to_csv(OUTPUT_DIR / "paper2_structural_similarity_matrix.csv")

    df_summary = pd.DataFrame({
        "target_city": TEST_CITIES,
        "self_cpc": [C_matrix[i, i] for i in range(N)],
        "oracle_best_cpc": cpc_oracle,
        "nearest_source_cpc": cpc_nearest,
        "global_baseline_cpc": cpc_global,
        "random_source_cpc": cpc_random
    })
    df_summary.to_csv(OUTPUT_DIR / "paper2_structural_transfer_summary.csv", index=False)

    print("\nDECISION GATE VERDICT FOR PAPER 2 (STRUCTURAL TRANSFERABILITY):")
    if corr_spearman > 0.40 and p_spearman < 0.01 and mean_nearest > mean_global:
        print("  🟢 VERDICT: EXCELLENT STRONG GO!")
        print("     Urban Structural Similarity strongly predicts OD transferability!")
        print("     Paper 2 foundation is rock solid for Structural Transferability (R_S).")
    elif corr_spearman > 0.20 and mean_nearest >= mean_global:
        print("  🟡 VERDICT: MODERATE GO. Structural similarity predicts transfer, but multi-dimensional representation refinement needed.")
    else:
        print("  🔴 VERDICT: NOVELTY WARNING. Structural similarity does not predict OD transferability.")
    print("=" * 70)

if __name__ == "__main__":
    run_structural_transfer_gate()
