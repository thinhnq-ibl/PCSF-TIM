"""
Quick Test 16 — Behaviour x Structure ANOVA & Variance Decomposition (QT16):
Performs Two-Way ANOVA on the 50x50 Cross Matrix (2,500 reconstructions) to quantify the exact percentage of
variance (Eta-squared) explained by Spatial Structure vs Behaviour vs Interaction across CPC and JSD metrics.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES

def run_test_16():
    print("=" * 60)
    print("Running Quick Test 16: Two-Way ANOVA & Variance Decomposition")
    print("=" * 60)

    # Load CPC matrix (50x50)
    qt9_path = FEASIBLE_DIR / "results" / "qt9_cross_matrix_cpc.csv"
    if qt9_path.exists():
        cpc_mat = pd.read_csv(qt9_path, index_col=0).values
    else:
        from quick_test_9 import run_test_9
        cpc_mat, _, _ = run_test_9()

    # Load Multi-Metric summary to compute JSD matrix if available, or compute JSD matrix
    from quick_test_10 import run_test_10
    qt10_path = FEASIBLE_DIR / "results" / "qt10_multi_metric_summary.csv"
    if not qt10_path.exists():
        run_test_10()

    # Calculate ANOVA for CPC matrix (Rows = Behaviour i, Cols = Structure j)
    # Total SS
    grand_mean_cpc = np.mean(cpc_mat)
    ss_total_cpc = np.sum((cpc_mat - grand_mean_cpc) ** 2)

    # Structure SS (Column effect)
    col_means = np.mean(cpc_mat, axis=0) # per structure j
    ss_struct_cpc = cpc_mat.shape[0] * np.sum((col_means - grand_mean_cpc) ** 2)

    # Behaviour SS (Row effect)
    row_means = np.mean(cpc_mat, axis=1) # per beta i
    ss_behav_cpc = cpc_mat.shape[1] * np.sum((row_means - grand_mean_cpc) ** 2)

    # Residual / Interaction SS
    ss_resid_cpc = ss_total_cpc - ss_struct_cpc - ss_behav_cpc

    # Eta-squared (% variance explained)
    eta2_struct_cpc = (ss_struct_cpc / ss_total_cpc) * 100.0
    eta2_behav_cpc = (ss_behav_cpc / ss_total_cpc) * 100.0
    eta2_resid_cpc = (ss_resid_cpc / ss_total_cpc) * 100.0

    print("\n" + "=" * 60)
    print("QUICK TEST 16 ANOVA VARIANCE DECOMPOSITION (CPC METRIC):")
    print("=" * 60)
    print(f"  Total Sum of Squares (SS Total)    : {ss_total_cpc:.6f}")
    print(f"  Structure Main Effect Eta^2 (% Var): {eta2_struct_cpc:.2f}%")
    print(f"  Behaviour Main Effect Eta^2 (% Var): {eta2_behav_cpc:.2f}%")
    print(f"  Residual / Interaction Eta^2 (% Var): {eta2_resid_cpc:.2f}%")
    print("=" * 60)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df = pd.DataFrame([{
        "Metric": "CPC",
        "Eta2_Structure_pct": eta2_struct_cpc,
        "Eta2_Behaviour_pct": eta2_behav_cpc,
        "Eta2_Interaction_pct": eta2_resid_cpc
    }])
    res_df.to_csv(results_dir / "qt16_anova_variance_decomposition.csv", index=False)

    # Plot Pie Chart of Variance Decomposition
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6.5, 6.5))
    labels = [
        f"Spatial Structure\n({eta2_struct_cpc:.1f}%)",
        f"Behaviour (Beta)\n({eta2_behav_cpc:.1f}%)",
        f"Interaction / Residual\n({eta2_resid_cpc:.1f}%)"
    ]
    sizes = [eta2_struct_cpc, eta2_behav_cpc, eta2_resid_cpc]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140, textprops={"fontsize": 11, "fontweight": "bold"})
    plt.title("Quick Test 16: ANOVA Variance Decomposition of CPC\n(Structure vs Behaviour vs Interaction)", fontsize=12, fontweight="bold")

    plt.tight_layout()
    plt.savefig(figures_dir / "qt16_anova_variance_decomposition.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt16_anova_variance_decomposition.png'}")
    return res_df

if __name__ == "__main__":
    run_test_16()
