"""
Quick Test 9 — Behaviour-Structure Cross Matrix (50 x 50 = 2500 Reconstructions)
Evaluating Scenario A vs Scenario B vs Scenario C for Structure-Behaviour Separation.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, predict_gravity_od, calculate_cpc

def run_test_9():
    print("=" * 60)
    print("Running Quick Test 9: Behaviour-Structure Cross Matrix (50 x 50)")
    print("=" * 60)

    cities = ALL_50_CITIES
    n_cities = len(cities)

    # 1. Load data and fit beta for all 50 cities
    print(f"Pre-loading data and fitting beta for {n_cities} cities...")
    betas = []
    city_data_cache = {}

    for i, city in enumerate(cities, 1):
        nodes, df = process_city_data(city)
        b = fit_beta_od_mle(df)
        betas.append(b)
        city_data_cache[city] = {
            "df": df,
            "actual": df["trip_count"].values
        }

    betas = np.array(betas)
    cpc_matrix = np.zeros((n_cities, n_cities))

    print(f"Executing {n_cities} x {n_cities} = {n_cities*n_cities} OD reconstructions...")

    for j, col_city in enumerate(cities):
        df_j = city_data_cache[col_city]["df"]
        actual_j = city_data_cache[col_city]["actual"]

        for i, row_city in enumerate(cities):
            beta_i = betas[i]
            T_hat_ij = predict_gravity_od(df_j, beta_i)
            cpc_ij = calculate_cpc(actual_j, T_hat_ij)
            cpc_matrix[i, j] = cpc_ij

    # Save 50x50 CPC matrix as CSV
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    cpc_df = pd.DataFrame(cpc_matrix, index=[f"Beta_{c}" for c in cities], columns=[f"Struct_{c}" for c in cities])
    cpc_df.to_csv(results_dir / "qt9_cross_matrix_cpc.csv")

    # Statistical Evaluation of Scenarios A, B, C
    diag_cpc = np.diag(cpc_matrix)
    off_diag_mask = ~np.eye(n_cities, dtype=bool)
    off_diag_cpc = cpc_matrix[off_diag_mask]

    col_stds = np.std(cpc_matrix, axis=0) # Variation down columns (holding structure fixed, changing beta)
    mean_col_std = float(np.mean(col_stds))
    total_matrix_std = float(np.std(cpc_matrix))

    diag_rank_counts = 0
    for j in range(n_cities):
        # Is diagonal element highest or top-2 in column j?
        col_vals = cpc_matrix[:, j]
        best_in_col = np.argmax(col_vals)
        if best_in_col == j:
            diag_rank_counts += 1

    pct_diag_is_best = (diag_rank_counts / n_cities) * 100.0
    mean_diag_cpc = float(np.mean(diag_cpc))
    mean_off_diag_cpc = float(np.mean(off_diag_cpc))
    diag_advantage = mean_diag_cpc - mean_off_diag_cpc

    print("\n" + "=" * 60)
    print("QUICK TEST 9 CROSS MATRIX DIAGNOSIS:")
    print("=" * 60)
    print(f"  Mean Diagonal CPC (Matched Beta_i & Struct_i) : {mean_diag_cpc:.4f}")
    print(f"  Mean Off-Diagonal CPC (Cross Beta_i & Struct_j): {mean_off_diag_cpc:.4f}")
    print(f"  Diagonal Advantage (Delta CPC)                 : +{diag_advantage:.4f}")
    print(f"  % Cities where own Beta_i is BEST for Struct_i : {pct_diag_is_best:.1f}% ({diag_rank_counts}/{n_cities})")
    print(f"  Mean Column Std Dev (Beta Sensitivity)         : {mean_col_std:.4f}")
    print(f"  Total Matrix Std Dev                           : {total_matrix_std:.4f}")
    print("-" * 60)

    scenario = "Unknown"
    if diag_advantage > 0.02 and mean_col_std > 0.02:
        scenario = "SCENARIO A (Ideal: High Structure-Behaviour Specificity)"
        explanation = (
            "The diagonal (matched city beta & structure) achieves superior CPC compared to cross-city combinations. "
            "Structure and Behaviour both carry distinct, essential city-specific information. "
            "The central hypothesis of the PhD dissertation is STRONGLY VALIDATED."
        )
    elif mean_col_std < 0.01:
        scenario = "SCENARIO B (Structure Universal / Low Beta Sensitivity)"
        explanation = (
            "Column values are nearly uniform despite changing beta. Structure dominates and beta has minimal impact. "
            "Paper 2 architecture requires adjustment to focus more on spatial structure representations."
        )
    else:
        scenario = "SCENARIO C (Weak Structure-Behaviour Separation)"
        explanation = "Matrix values show weak differentiation across both structure and behavior."

    print(f"  >>> RESULT: {scenario}")
    print(f"  >>> Summary: {explanation}")
    print("=" * 60)

    # Plot Heatmap
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        cpc_matrix,
        cmap="viridis",
        xticklabels=False,
        yticklabels=False,
        cbar_kws={"label": "Common Part of Commuters (CPC)"}
    )
    plt.title(f"Quick Test 9: Behaviour-Structure Cross Matrix (50 x 50 = 2500 Reconstructions)\nDiagnosis: {scenario[:10]} (Diag CPC = {mean_diag_cpc:.3f} vs Cross = {mean_off_diag_cpc:.3f})", 
              fontsize=12, fontweight="bold", pad=15)
    plt.xlabel("Spatial Structure (50 Cities j = 1 ... 50)", fontsize=11)
    plt.ylabel(r"Behaviour Parameter $\beta_i$ (50 Cities i = 1 ... 50)", fontsize=11)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt9_cross_matrix_heatmap.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt9_cross_matrix_heatmap.png'}")
    return cpc_matrix, scenario, diag_advantage

if __name__ == "__main__":
    run_test_9()
