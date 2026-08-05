"""
Quick Test 2 — Is Behaviour city-specific? (Distribution & Variation of Beta across 50 Cities)
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle

def run_test_2():
    print("=" * 60)
    print("Running Quick Test 2: Distribution & City-Specificity of Beta")
    print("=" * 60)

    qt1_path = FEASIBLE_DIR / "results" / "qt1_beta_od_vs_tld.csv"
    if qt1_path.exists():
        df = pd.read_csv(qt1_path)
    else:
        results = []
        for i, city in enumerate(ALL_50_CITIES, 1):
            nodes, city_df = process_city_data(city)
            beta_od = fit_beta_od_mle(city_df)
            results.append({"city": city, "beta_OD": beta_od})
        df = pd.DataFrame(results)

    betas = df["beta_OD"].values
    mean_beta = float(np.mean(betas))
    std_beta = float(np.std(betas))
    cv_beta = float(std_beta / mean_beta)
    min_beta = float(np.min(betas))
    max_beta = float(np.max(betas))

    print("\n" + "-" * 40)
    print("Quick Test 2 Beta Variation Statistics (50 Cities):")
    print(f"  Mean Beta              : {mean_beta:.4f}")
    print(f"  Std Deviation          : {std_beta:.4f}")
    print(f"  Coefficient of Var (CV): {cv_beta:.4f} ({cv_beta*100:.1f}%)")
    print(f"  Min Beta               : {min_beta:.4f} ({df.loc[df['beta_OD'].idxmin(), 'city']})")
    print(f"  Max Beta               : {max_beta:.4f} ({df.loc[df['beta_OD'].idxmax(), 'city']})")
    print("-" * 40)

    if cv_beta > 0.15:
        print("  => DECISION: High city-specificity detected (CV > 15%). Behaviour is distinctly city-dependent!")
    else:
        print("  => DECISION: Low variation across cities. Behaviour may be homogeneous.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    df[["city", "beta_OD"]].to_csv(results_dir / "qt2_beta_distribution.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    n, bins, patches = plt.hist(betas, bins=15, color="#1f77b4", edgecolor="black", alpha=0.75)
    plt.axvline(mean_beta, color="red", linestyle="--", linewidth=2, label=f"Mean = {mean_beta:.3f}")
    plt.axvline(mean_beta - std_beta, color="orange", linestyle=":", linewidth=1.5, label=f"±1 Std Dev ({std_beta:.3f})")
    plt.axvline(mean_beta + std_beta, color="orange", linestyle=":", linewidth=1.5)

    plt.xlabel(r"Distance Decay Parameter $\beta$", fontsize=12)
    plt.ylabel("Frequency (Number of Cities)", fontsize=12)
    plt.title("Quick Test 2: Distribution of Behaviour Parameter Across 50 Cities", fontsize=13, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(fontsize=11)

    plt.text(0.68, 0.75, f"Mean = {mean_beta:.4f}\nStd = {std_beta:.4f}\nCV = {cv_beta*100:.1f}%\nRange = [{min_beta:.3f}, {max_beta:.3f}]",
             transform=plt.gca().transAxes, fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9))

    plt.tight_layout()
    plt.savefig(figures_dir / "qt2_beta_distribution.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt2_beta_distribution.png'}")
    return df, cv_beta

if __name__ == "__main__":
    run_test_2()
