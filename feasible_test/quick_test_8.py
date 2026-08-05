"""
Quick Test 8 — Entire Dissertation Feasibility: Gravity OD Reconstruction with Ground Truth (Oi, Aj, Beta)
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, predict_gravity_od, calculate_cpc

def run_test_8():
    print("=" * 60)
    print("Running Quick Test 8: Dissertation Gravity Decomposition CPC Evaluation")
    print("=" * 60)

    results = []

    for i, city in enumerate(ALL_50_CITIES, 1):
        nodes, df = process_city_data(city)
        actual_trips = df["trip_count"].values

        # Fit city beta
        beta = fit_beta_od_mle(df)

        # Reconstruct OD with ground truth O_i, A_j and beta
        T_hat = predict_gravity_od(df, beta)
        cpc_val = calculate_cpc(actual_trips, T_hat)

        results.append({
            "city": city,
            "n_nodes": len(nodes),
            "n_pairs": len(df),
            "beta": beta,
            "cpc": cpc_val
        })

    res_df = pd.DataFrame(results)

    mean_cpc = float(res_df["cpc"].mean())
    std_cpc = float(res_df["cpc"].std())
    min_cpc = float(res_df["cpc"].min())
    max_cpc = float(res_df["cpc"].max())

    print("\n" + "-" * 40)
    print("Quick Test 8 Dissertation Reconstruction Performance (50 Cities):")
    print(f"  Mean CPC  : {mean_cpc:.4f}")
    print(f"  Std Dev   : {std_cpc:.4f}")
    print(f"  Min CPC   : {min_cpc:.4f} ({res_df.loc[res_df['cpc'].idxmin(), 'city']})")
    print(f"  Max CPC   : {max_cpc:.4f} ({res_df.loc[res_df['cpc'].idxmax(), 'city']})")
    print("-" * 40)

    if mean_cpc > 0.70:
        print("  => DECISION: Mean CPC > 0.70 -> Gravity decomposition hypothesis is EXTREMELY SOLID!")
    elif mean_cpc > 0.50:
        print("  => DECISION: Mean CPC > 0.50 -> Good reconstruction baseline.")
    else:
        print("  => DECISION: Mean CPC < 0.50 -> Gravity decomposition requires adjustment.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt8_dissertation_gravity_cpc.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.hist(res_df["cpc"], bins=15, color="#2ca02c", edgecolor="black", alpha=0.75)
    plt.axvline(mean_cpc, color="red", linestyle="--", linewidth=2, label=f"Mean CPC = {mean_cpc:.3f}")

    plt.xlabel("Common Part of Commuters (CPC)", fontsize=12)
    plt.ylabel("Frequency (Number of Cities)", fontsize=12)
    plt.title("Quick Test 8: Dissertation Gravity Decomposition CPC Distribution", fontsize=13, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(fontsize=11)

    plt.text(0.05, 0.75, f"Mean CPC = {mean_cpc:.4f}\nStd Dev = {std_cpc:.4f}\nMin = {min_cpc:.4f}\nMax = {max_cpc:.4f}",
             transform=plt.gca().transAxes, fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9))

    plt.tight_layout()
    plt.savefig(figures_dir / "qt8_dissertation_gravity_cpc.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt8_dissertation_gravity_cpc.png'}")
    return res_df, mean_cpc

if __name__ == "__main__":
    run_test_8()
