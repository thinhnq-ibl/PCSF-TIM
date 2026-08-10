"""
Paper 2 Phase 2C Forensic Audit: Fast Precomputed Nested SWET & Feature Family Ablation
Checks:
1. Nested Leave-One-Target-Out tuning of tau (Strict leakage-free OOF CPC)
2. Downstream SWET Ablation across feature families (Pop-only vs Density vs R1-R4 Full RS)
3. Target-level paired CPC distribution, bootstrap 95% CIs, and win-rates
"""

import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import spearmanr, pearsonr, wilcoxon
from scipy.optimize import minimize_scalar

# Setup paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Selected 10 representative cities for forensic audit
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

def load_city_features_and_calibration(city: str):
    """Load city data, build feature families, and calibrate local beta."""
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

    total_pop = float(pop.sum())
    total_pois = float(pois.sum())
    total_area = float(nodes["area_km2"].sum())
    pop_density = total_pop / max(total_area, 1e-4)
    poi_density = total_pois / max(total_area, 1e-4)
    mean_dist = float(D[D > 0].mean())
    median_tract_area = float(nodes["area_km2"].median())
    
    f_r1_size = np.array([np.log1p(total_pop), np.log1p(total_area)])
    f_r2_opp = np.array([np.log1p(total_pop), np.log1p(total_area), np.log1p(total_pois)])
    f_r3_density = np.array([
        np.log1p(total_pop), np.log1p(total_area), np.log1p(total_pois),
        np.log1p(pop_density), np.log1p(poi_density), road_density_mean
    ])
    f_r4_full = np.array([
        np.log1p(total_pop), np.log1p(total_area), np.log1p(total_pois),
        np.log1p(pop_density), np.log1p(poi_density), road_density_mean,
        mean_dist, median_tract_area
    ])

    return {
        "city": city,
        "n_nodes": n_nodes,
        "T_true": T_true,
        "D": D,
        "O_i": O_i,
        "A_j": A_j,
        "beta_local": beta_local,
        "f_r1": f_r1_size,
        "f_r2": f_r2_opp,
        "f_r3": f_r3_density,
        "f_r4": f_r4_full,
        "pop_only": np.array([np.log1p(total_pop)]),
        "density_only": np.array([np.log1p(pop_density)])
    }

def compute_similarity_matrix(feature_vectors):
    """Compute normalized cosine similarity matrix."""
    matrix = np.array(feature_vectors)
    if matrix.shape[1] == 1:
        diffs = np.abs(matrix - matrix.T)
        sim = 1.0 / (1.0 + diffs)
        return sim
    norm_matrix = (matrix - matrix.mean(axis=0)) / (matrix.std(axis=0) + 1e-6)
    dot_prod = norm_matrix @ norm_matrix.T
    norms = np.linalg.norm(norm_matrix, axis=1, keepdims=True)
    sim = dot_prod / (norms @ norms.T + 1e-12)
    return sim

def run_nested_swet_oof_eval(city_data, S_matrix, T_pred_dict):
    """
    Fast Nested Leave-One-Target-Out SWET Evaluation using pre-computed T_pred matrices.
    """
    N = len(TEST_CITIES)
    cpc_oof_list = []
    best_tau_list = []

    for t_idx, t_city in enumerate(TEST_CITIES):
        train_indices = [i for i in range(N) if i != t_idx]
        
        # Inner LOO validation to tune tau_(-t)
        def inner_swet_loss(tau_val):
            tau = float(tau_val)
            inner_cpcs = []
            for u_idx in train_indices:
                inner_sources = [s for s in train_indices if s != u_idx]
                sims = np.array([S_matrix[s, u_idx] for s in inner_sources])
                weights = np.exp(tau * sims) / np.sum(np.exp(tau * sims))
                
                u_data = city_data[TEST_CITIES[u_idx]]
                T_swet = np.zeros_like(u_data["T_true"])
                for s_sub, s_idx in enumerate(inner_sources):
                    T_swet += weights[s_sub] * T_pred_dict[(s_idx, u_idx)]
                inner_cpcs.append(compute_cpc(T_swet, u_data["T_true"]))
            return -np.mean(inner_cpcs)

        res_tau = minimize_scalar(inner_swet_loss, bounds=(0.0, 20.0), method="bounded")
        tau_star = float(res_tau.x)
        best_tau_list.append(tau_star)

        # Apply tau_star to target t
        sims_t = np.array([S_matrix[s, t_idx] for s in train_indices])
        weights_t = np.exp(tau_star * sims_t) / np.sum(np.exp(tau_star * sims_t))
        
        t_data = city_data[t_city]
        T_swet_t = np.zeros_like(t_data["T_true"])
        for s_sub, s_idx in enumerate(train_indices):
            T_swet_t += weights_t[s_sub] * T_pred_dict[(s_idx, t_idx)]

        cpc_oof_list.append(compute_cpc(T_swet_t, t_data["T_true"]))

    return np.array(cpc_oof_list), np.array(best_tau_list)

def run_phase2c_audit():
    print("=" * 75)
    print("PAPER 2 PHASE 2C FORENSIC AUDIT: FAST NESTED SWET & DOWNSTREAM ABLATION")
    print("=" * 75)

    city_data = {}
    for city in TEST_CITIES:
        city_data[city] = load_city_features_and_calibration(city)

    N = len(TEST_CITIES)
    C_matrix = np.zeros((N, N))
    T_pred_dict = {}

    print("Precomputing all 90 pairwise prediction matrices...")
    for i, s_city in enumerate(TEST_CITIES):
        s_beta = city_data[s_city]["beta_local"]
        for j, t_city in enumerate(TEST_CITIES):
            t_data = city_data[t_city]
            log_f = np.log(t_data["A_j"][None, :]) - s_beta * t_data["D"]
            lf_max = log_f.max(axis=1, keepdims=True)
            exp_f = np.exp(log_f - lf_max)
            P_pred = exp_f / exp_f.sum(axis=1, keepdims=True)
            T_pred = t_data["O_i"][:, None] * P_pred
            
            T_pred_dict[(i, j)] = T_pred
            C_matrix[i, j] = compute_cpc(T_pred, t_data["T_true"])

    cpc_global = np.zeros(N)
    for j, t_city in enumerate(TEST_CITIES):
        sources = [i for i in range(N) if i != j]
        avg_beta = np.mean([city_data[TEST_CITIES[i]]["beta_local"] for i in sources])
        t_data = city_data[t_city]
        log_f = np.log(t_data["A_j"][None, :]) - avg_beta * t_data["D"]
        lf_max = log_f.max(axis=1, keepdims=True)
        exp_f = np.exp(log_f - lf_max)
        P_pred = exp_f / exp_f.sum(axis=1, keepdims=True)
        T_pred = t_data["O_i"][:, None] * P_pred
        cpc_global[j] = compute_cpc(T_pred, t_data["T_true"])

    cpc_oracle_source = np.array([max([C_matrix[i, j] for i in range(N) if i != j]) for j in range(N)])

    # Build similarity matrices
    sim_matrices = {
        "Pop_Only": compute_similarity_matrix([city_data[c]["pop_only"] for c in TEST_CITIES]),
        "Density_Only": compute_similarity_matrix([city_data[c]["density_only"] for c in TEST_CITIES]),
        "R1_Size": compute_similarity_matrix([city_data[c]["f_r1"] for c in TEST_CITIES]),
        "R2_Opportunities": compute_similarity_matrix([city_data[c]["f_r2"] for c in TEST_CITIES]),
        "R3_Network": compute_similarity_matrix([city_data[c]["f_r3"] for c in TEST_CITIES]),
        "R4_Full_RS": compute_similarity_matrix([city_data[c]["f_r4"] for c in TEST_CITIES])
    }

    # Run Nested Out-of-Fold SWET Evaluation across feature families
    ablation_results = {}
    print("\nRunning Leakage-Free Nested Leave-One-Target-Out SWET Evaluation...")
    
    for name, S_mat in sim_matrices.items():
        cpc_oof, tau_list = run_nested_swet_oof_eval(city_data, S_mat, T_pred_dict)
        mean_cpc = np.mean(cpc_oof)
        median_cpc = np.median(cpc_oof)
        deltas = cpc_oof - cpc_global
        win_rate = np.mean(deltas > 0) * 100.0
        
        mean_oracle = np.mean(cpc_oracle_source)
        mean_global = np.mean(cpc_global)
        gap_recovered = ((mean_cpc - mean_global) / (mean_oracle - mean_global)) * 100.0
        
        ablation_results[name] = {
            "cpc_oof": cpc_oof,
            "mean_cpc": mean_cpc,
            "median_cpc": median_cpc,
            "mean_delta": np.mean(deltas),
            "win_rate_pct": win_rate,
            "gap_recovered_pct": gap_recovered,
            "mean_tau": np.mean(tau_list)
        }

    print("\n" + "=" * 75)
    print("NESTED LEAKAGE-FREE SWET FEATURE ABLATION RESULTS:")
    print("=" * 75)
    print(f"  Pooled Global Baseline CPC : {np.mean(cpc_global):.4f}")
    print(f"  Oracle Source Benchmark CPC: {np.mean(cpc_oracle_source):.4f}")
    print("-" * 75)
    print(f"  {'Feature Family':<20} | {'Mean OOF CPC':<12} | {'Δ vs Global':<12} | {'Win Rate':<10} | {'Gap Recovered':<12}")
    print("-" * 75)
    
    for name, res in ablation_results.items():
        print(f"  {name:<20} | {res['mean_cpc']:<12.4f} | {res['mean_delta']:<+12.4f} | {res['win_rate_pct']:<9.1f}% | {res['gap_recovered_pct']:<11.1f}%")

    print("=" * 75)

    # 95% Bootstrap CI for Full R4 RS Model
    full_cpc = ablation_results["R4_Full_RS"]["cpc_oof"]
    full_deltas = full_cpc - cpc_global
    
    np.random.seed(42)
    boot_means = [np.mean(np.random.choice(full_deltas, size=N, replace=True)) for _ in range(10000)]
    ci_lower, ci_upper = np.percentile(boot_means, [2.5, 97.5])
    w_stat, p_wilcox = wilcoxon(full_deltas) if not np.all(full_deltas == 0) else (0, 1.0)

    print("\nSTATISTICAL SUMMARY FOR NESTED FULL R4_Full_RS SWET MODEL:")
    print(f"  - Out-of-Fold Mean CPC     : {np.mean(full_cpc):.4f}")
    print(f"  - Mean Δ vs Global         : {np.mean(full_deltas):+.4f}")
    print(f"  - 95% Bootstrap CI (Targets): [{ci_lower:+.4f}, {ci_upper:+.4f}]")
    print(f"  - Target Win-Rate          : {ablation_results['R4_Full_RS']['win_rate_pct']:.1f}%")
    print(f"  - Paired Wilcoxon p-value  : {p_wilcox:.4f}")
    print("=" * 75)

    # Save summary dataframe
    df_rows = []
    for name, res in ablation_results.items():
        df_rows.append({
            "feature_family": name,
            "mean_oof_cpc": res["mean_cpc"],
            "median_oof_cpc": res["median_cpc"],
            "mean_delta_global": res["mean_delta"],
            "win_rate_pct": res["win_rate_pct"],
            "gap_recovered_pct": res["gap_recovered_pct"],
            "mean_tau": res["mean_tau"]
        })
    df_out = pd.DataFrame(df_rows)
    df_out.to_csv(OUTPUT_DIR / "paper2_phase2c_nested_swet_ablation.csv", index=False)

if __name__ == "__main__":
    run_phase2c_audit()
