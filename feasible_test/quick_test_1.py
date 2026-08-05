"""
Quick Test 1 — Is Paper 1 feasible? (Can TLD recover Behaviour parameter beta?)
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, fit_beta_tld_mle

def run_test_1():
    print("=" * 60)
    print("Running Quick Test 1: Beta_OD vs Beta_TLD (Paper 1 Feasibility)")
    print("=" * 60)

    results = []
    
    for i, city in enumerate(ALL_50_CITIES, 1):
        print(f"[{i:02d}/50] Processing {city}...")
        try:
            nodes, df = process_city_data(city)
            beta_od = fit_beta_od_mle(df)
            beta_tld = fit_beta_tld_mle(df)
            
            results.append({
                "city": city,
                "n_nodes": len(nodes),
                "n_pairs": len(df),
                "beta_OD": beta_od,
                "beta_TLD": beta_tld,
                "diff": beta_tld - beta_od,
                "rel_abs_err": abs(beta_tld - beta_od) / (beta_od + 1e-6)
            })
        except Exception as e:
            print(f"  Error processing {city}: {e}")

    res_df = pd.DataFrame(results)
    
    # Calculate R^2 and statistics
    y_true = res_df["beta_OD"].values
    y_pred = res_df["beta_TLD"].values
    
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1.0 - (ss_res / ss_tot)
    
    mae = np.mean(np.abs(y_true - y_pred))
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    corr = np.corrcoef(y_true, y_pred)[0, 1]

    print("\n" + "-" * 40)
    print(f"Quick Test 1 Results across {len(res_df)} Cities:")
    print(f"  R^2 Score       : {r2:.4f}")
    print(f"  Correlation (r) : {corr:.4f}")
    print(f"  MAE             : {mae:.4f}")
    print(f"  RMSE            : {rmse:.4f}")
    print("-" * 40)

    if r2 > 0.95:
        print("  => DECISION: R^2 > 0.95 -> Paper 1 is EXTREMELY FEASIBLE!")
    elif r2 > 0.80:
        print("  => DECISION: R^2 > 0.80 -> Paper 1 is strong, minor calibration needed.")
    else:
        print("  => DECISION: R^2 < 0.50 -> Caution / Reconsider.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt1_beta_od_vs_tld.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7, 6))
    plt.scatter(res_df["beta_OD"], res_df["beta_TLD"], color="#2b5c8f", alpha=0.8, edgecolors="k", s=60, label="50 US Cities")
    
    lim_min = min(y_true.min(), y_pred.min()) * 0.9
    lim_max = max(y_true.max(), y_pred.max()) * 1.1
    plt.plot([lim_min, lim_max], [lim_min, lim_max], "r--", linewidth=2, label="Identity Line ($y=x$)")

    plt.xlabel(r"$\beta_{OD}$ (Direct fit on OD pairs)", fontsize=12)
    plt.ylabel(r"$\beta_{TLD}$ (Estimated from aggregate TLD)", fontsize=12)
    plt.title(f"Quick Test 1: Paper 1 Feasibility\n$R^2 = {r2:.4f}$, Pearson $r = {corr:.4f}$", fontsize=13, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(fontsize=11)

    # Annotate key stats on chart
    plt.text(0.05, 0.85, f"R² = {r2:.4f}\nMAE = {mae:.4f}\nN = {len(res_df)} cities", 
             transform=plt.gca().transAxes, fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9))

    plt.tight_layout()
    plt.savefig(figures_dir / "qt1_beta_od_vs_tld.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt1_beta_od_vs_tld.png'}")
    return res_df, r2

if __name__ == "__main__":
    run_test_1()
