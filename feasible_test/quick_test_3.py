"""
Quick Test 3 — Structure vs Behaviour Sensitivity: Does changing Beta impact OD reconstruction (CPC)?
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

def run_test_3():
    print("=" * 60)
    print("Running Quick Test 3: Sensitivity of OD Reconstruction to Beta Perturbation")
    print("=" * 60)

    qt1_path = FEASIBLE_DIR / "results" / "qt1_beta_od_vs_tld.csv"
    if qt1_path.exists():
        beta_df = pd.read_csv(qt1_path)
    else:
        results = []
        for city in ALL_50_CITIES:
            _, c_df = process_city_data(city)
            b = fit_beta_od_mle(c_df)
            results.append({"city": city, "beta_OD": b})
        beta_df = pd.DataFrame(results)

    betas_dict = dict(zip(beta_df["city"], beta_df["beta_OD"]))
    mean_beta = float(np.mean(list(betas_dict.values())))

    results = []
    rng = np.random.default_rng(42)
    cities = list(betas_dict.keys())

    for i, city in enumerate(cities, 1):
        nodes, df = process_city_data(city)
        actual_trips = df["trip_count"].values

        beta_own = betas_dict[city]
        
        # 1. Own optimal beta
        T_own = predict_gravity_od(df, beta_own)
        cpc_own = calculate_cpc(actual_trips, T_own)

        # 2. National mean beta
        T_mean = predict_gravity_od(df, mean_beta)
        cpc_mean = calculate_cpc(actual_trips, T_mean)

        # 3. Random wrong city beta
        other_cities = [c for c in cities if c != city]
        rand_city = rng.choice(other_cities)
        beta_wrong = betas_dict[rand_city]
        T_wrong = predict_gravity_od(df, beta_wrong)
        cpc_wrong = calculate_cpc(actual_trips, T_wrong)

        results.append({
            "city": city,
            "beta_own": beta_own,
            "beta_wrong": beta_wrong,
            "cpc_own": cpc_own,
            "cpc_mean": cpc_mean,
            "cpc_wrong": cpc_wrong,
            "cpc_drop_mean": cpc_own - cpc_mean,
            "cpc_drop_wrong": cpc_own - cpc_wrong
        })

    res_df = pd.DataFrame(results)

    avg_own = float(res_df["cpc_own"].mean())
    avg_mean = float(res_df["cpc_mean"].mean())
    avg_wrong = float(res_df["cpc_wrong"].mean())

    print("\n" + "-" * 40)
    print("Quick Test 3 Sensitivity Results (50 Cities):")
    print(f"  Average CPC (Own Optimal Beta) : {avg_own:.4f}")
    print(f"  Average CPC (National Mean Beta): {avg_mean:.4f} (Drop: {avg_own - avg_mean:.4f})")
    print(f"  Average CPC (Random City Beta) : {avg_wrong:.4f} (Drop: {avg_own - avg_wrong:.4f})")
    print("-" * 40)

    if (avg_own - avg_wrong) > 0.05:
        print("  => DECISION: Beta strongly impacts OD reconstruction accuracy! Behaviour is crucial.")
    else:
        print("  => DECISION: Beta impact is minimal; spatial structure dominates.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt3_beta_sensitivity.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7, 5))
    categories = ["Own Optimal $\\beta_i$", "National Mean $\\bar{\\beta}$", "Random Foreign $\\beta_j$"]
    means = [avg_own, avg_mean, avg_wrong]
    colors = ["#2ca02c", "#ff7f0e", "#d62728"]

    bars = plt.bar(categories, means, color=colors, alpha=0.85, edgecolor="black", width=0.55)
    plt.ylabel("Mean Common Part of Commuters (CPC)", fontsize=12)
    plt.title("Quick Test 3: Sensitivity of OD Reconstruction to Beta", fontsize=13, fontweight="bold")
    plt.ylim(0, max(means) * 1.25)
    plt.grid(axis="y", linestyle=":", alpha=0.6)

    for bar, val in zip(bars, means):
        plt.text(bar.get_x() + bar.get_width()/2.0, val + 0.015, f"{val:.4f}", ha="center", va="bottom", fontsize=11, fontweight="bold")

    plt.tight_layout()
    plt.savefig(figures_dir / "qt3_beta_sensitivity.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt3_beta_sensitivity.png'}")
    return res_df, avg_own, avg_wrong

if __name__ == "__main__":
    run_test_3()
