"""
Quick Test 10 — Metric Dependence & Distance Sensitivity Test:
Multi-Metric 50x50 Cross Matrix (CPC, RMSE, JSD, Mean Distance Error, Log-Likelihood)
and TLD Histogram Shift Analysis when swapping Beta.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy.spatial.distance import jensenshannon

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, predict_gravity_od, calculate_cpc

def compute_tld_distribution(df, trips, K=20):
    """Compute normalized Travel-Length Distribution (TLD) histogram."""
    d = df["d_clamped"].values
    d_max = d.max()
    edges = np.linspace(0, d_max, K + 1)
    edges[-1] = np.inf
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
    tot = y_k.sum()
    if tot < 1e-12:
        return np.ones(K) / K
    return y_k / tot

def run_test_10():
    print("=" * 60)
    print("Running Quick Test 10: Multi-Metric Cross Matrix & Distance Shift Analysis")
    print("=" * 60)

    cities = ALL_50_CITIES
    n_cities = len(cities)

    print(f"Pre-loading data and fitting beta for {n_cities} cities...")
    betas = []
    city_cache = {}

    for city in cities:
        nodes, df = process_city_data(city)
        b = fit_beta_od_mle(df)
        betas.append(b)
        actual = df["trip_count"].values
        d_vals = df["d_clamped"].values
        obs_avg_d = float(np.sum(actual * d_vals) / (np.sum(actual) + 1e-9))
        obs_tld = compute_tld_distribution(df, actual)

        city_cache[city] = {
            "df": df,
            "actual": actual,
            "d_vals": d_vals,
            "obs_avg_d": obs_avg_d,
            "obs_tld": obs_tld
        }

    betas = np.array(betas)

    # Matrices for 5 metrics across 50x50 combinations
    mat_cpc = np.zeros((n_cities, n_cities))
    mat_rmse = np.zeros((n_cities, n_cities))
    mat_jsd = np.zeros((n_cities, n_cities))
    mat_delta_d = np.zeros((n_cities, n_cities))
    mat_loglike = np.zeros((n_cities, n_cities))

    print("Computing 50 x 50 cross-matrix for 5 evaluation metrics...")

    for j, col_city in enumerate(cities):
        df_j = city_cache[col_city]["df"]
        actual_j = city_cache[col_city]["actual"]
        d_j = city_cache[col_city]["d_vals"]
        obs_avg_d_j = city_cache[col_city]["obs_avg_d"]
        obs_tld_j = city_cache[col_city]["obs_tld"]
        tot_trips_j = actual_j.sum()

        for i, row_city in enumerate(cities):
            beta_i = betas[i]
            T_hat_ij = predict_gravity_od(df_j, beta_i)

            # 1. CPC
            mat_cpc[i, j] = calculate_cpc(actual_j, T_hat_ij)

            # 2. RMSE
            mat_rmse[i, j] = np.sqrt(np.mean((actual_j - T_hat_ij) ** 2))

            # 3. JSD on TLD
            pred_tld_ij = compute_tld_distribution(df_j, T_hat_ij)
            mat_jsd[i, j] = jensenshannon(obs_tld_j, pred_tld_ij) ** 2 # JSD score in [0, 1]

            # 4. Delta Average Trip Distance (km)
            pred_avg_d_ij = float(np.sum(T_hat_ij * d_j) / (np.sum(T_hat_ij) + 1e-9))
            mat_delta_d[i, j] = abs(pred_avg_d_ij - obs_avg_d_j)

            # 5. Log-Likelihood
            p_ij = (T_hat_ij / (tot_trips_j + 1e-9)).clip(1e-15)
            mat_loglike[i, j] = np.sum(actual_j * np.log(p_ij))

    # Evaluate Sensitivity per metric (Diagonal vs Off-Diagonal)
    metrics_summary = []

    def analyze_mat(mat, name, is_higher_better=True):
        diag = np.diag(mat)
        off_mask = ~np.eye(n_cities, dtype=bool)
        off_diag = mat[off_mask]
        
        mean_diag = float(np.mean(diag))
        mean_off = float(np.mean(off_diag))
        
        if is_higher_better:
            adv = mean_diag - mean_off
            pct_change = (adv / (abs(mean_off) + 1e-9)) * 100.0
        else:
            adv = mean_off - mean_diag # positive if diag is lower (better)
            pct_change = (adv / (abs(mean_off) + 1e-9)) * 100.0

        col_stds = np.std(mat, axis=0)
        mean_col_std = float(np.mean(col_stds))

        metrics_summary.append({
            "Metric": name,
            "Mean_Diagonal": mean_diag,
            "Mean_OffDiagonal": mean_off,
            "Diagonal_Advantage": adv,
            "Pct_Improvement": pct_change,
            "Mean_Column_Std": mean_col_std
        })

    analyze_mat(mat_cpc, "CPC", is_higher_better=True)
    analyze_mat(mat_rmse, "RMSE", is_higher_better=False)
    analyze_mat(mat_jsd, "JSD (TLD Divergence)", is_higher_better=False)
    analyze_mat(mat_delta_d, "Delta Avg Distance (km)", is_higher_better=False)
    analyze_mat(mat_loglike, "Log-Likelihood", is_higher_better=True)

    summary_df = pd.DataFrame(metrics_summary)

    print("\n" + "=" * 65)
    print("QUICK TEST 10 MULTI-METRIC MATRIX COMPARISON:")
    print("=" * 65)
    print(summary_df.to_string(index=False))
    print("=" * 65)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(results_dir / "qt10_multi_metric_summary.csv", index=False)

    # Plot Multi-Metric Heatmaps
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # Subplot 1: JSD
    sns.heatmap(mat_jsd, cmap="magma_r", ax=axes[0, 0], xticklabels=False, yticklabels=False, cbar_kws={"label": "JSD (Lower = Better)"})
    axes[0, 0].set_title(f"JSD of TLD (Diag = {summary_df.loc[2, 'Mean_Diagonal']:.4f} vs Off = {summary_df.loc[2, 'Mean_OffDiagonal']:.4f})\nShift Sensitivity = +{summary_df.loc[2, 'Pct_Improvement']:.1f}%", fontsize=11, fontweight="bold")
    axes[0, 0].set_ylabel(r"Beta Parameter $\beta_i$", fontsize=10)

    # Subplot 2: Delta Avg Distance
    sns.heatmap(mat_delta_d, cmap="viridis_r", ax=axes[0, 1], xticklabels=False, yticklabels=False, cbar_kws={"label": "Error in Mean Distance (km)"})
    axes[0, 1].set_title(f"Avg Trip Distance Error (km) (Diag = {summary_df.loc[3, 'Mean_Diagonal']:.2f}km vs Off = {summary_df.loc[3, 'Mean_OffDiagonal']:.2f}km)\nShift Sensitivity = +{summary_df.loc[3, 'Pct_Improvement']:.1f}%", fontsize=11, fontweight="bold")

    # Subplot 3: RMSE
    sns.heatmap(mat_rmse, cmap="plasma_r", ax=axes[1, 0], xticklabels=False, yticklabels=False, cbar_kws={"label": "RMSE (Flows)"})
    axes[1, 0].set_title(f"OD Flow RMSE (Diag = {summary_df.loc[1, 'Mean_Diagonal']:.2f} vs Off = {summary_df.loc[1, 'Mean_OffDiagonal']:.2f})\nShift Sensitivity = +{summary_df.loc[1, 'Pct_Improvement']:.1f}%", fontsize=11, fontweight="bold")
    axes[1, 0].set_xlabel("Spatial Structure (Cities j)", fontsize=10)
    axes[1, 0].set_ylabel(r"Beta Parameter $\beta_i$", fontsize=10)

    # Subplot 4: CPC
    sns.heatmap(mat_cpc, cmap="viridis", ax=axes[1, 1], xticklabels=False, yticklabels=False, cbar_kws={"label": "CPC (Higher = Better)"})
    axes[1, 1].set_title(f"CPC (Diag = {summary_df.loc[0, 'Mean_Diagonal']:.4f} vs Off = {summary_df.loc[0, 'Mean_OffDiagonal']:.4f})\nShift Sensitivity = +{summary_df.loc[0, 'Pct_Improvement']:.1f}%", fontsize=11, fontweight="bold")
    axes[1, 1].set_xlabel("Spatial Structure (Cities j)", fontsize=10)

    plt.suptitle("Quick Test 10: Multi-Metric Sensitivity & Distance Decay Shift Analysis", fontsize=14, fontweight="bold", y=0.98)
    plt.tight_layout()
    plt.savefig(figures_dir / "qt10_multi_metric_heatmaps.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt10_multi_metric_heatmaps.png'}")
    return summary_df

if __name__ == "__main__":
    run_test_10()
