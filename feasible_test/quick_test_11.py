"""
Quick Test 11 — City Heterogeneity & Behaviour Sensitivity Analysis:
Determining which cities are highly sensitive to Behaviour parameter beta vs structure-dominated cities,
and correlating sensitivity with urban spatial indicators.
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

def run_test_11():
    print("=" * 60)
    print("Running Quick Test 11: City Heterogeneity & Sensitivity Breakdown")
    print("=" * 60)

    qt9_path = FEASIBLE_DIR / "results" / "qt9_cross_matrix_cpc.csv"
    if qt9_path.exists():
        cpc_df = pd.read_csv(qt9_path, index_col=0)
        cpc_mat = cpc_df.values
    else:
        from quick_test_9 import run_test_9
        cpc_mat, _, _ = run_test_9()

    cities = ALL_50_CITIES
    n_cities = len(cities)

    city_stats = []

    for j, city in enumerate(cities):
        nodes, df = process_city_data(city)
        col_cpc = cpc_mat[:, j]
        
        own_cpc = col_cpc[j]
        mean_foreign_cpc = np.mean(np.delete(col_cpc, j))
        min_foreign_cpc = np.min(col_cpc)
        max_foreign_cpc = np.max(col_cpc)
        
        # Sensitivity metrics
        cpc_delta_mean = own_cpc - mean_foreign_cpc
        cpc_delta_range = max_foreign_cpc - min_foreign_cpc
        cpc_std = np.std(col_cpc)

        # Urban spatial features
        n_zones = len(nodes)
        tot_pop = nodes["total_population"].sum()
        tot_area = nodes["area_km2"].sum()
        pop_density = tot_pop / (tot_area + 1e-4)
        max_dist = df["distance"].max()
        avg_dist = (df["trip_count"] * df["distance"]).sum() / (df["trip_count"].sum() + 1e-9)
        fitted_beta = fit_beta_od_mle(df)

        city_stats.append({
            "city": city,
            "fitted_beta": fitted_beta,
            "own_cpc": own_cpc,
            "mean_foreign_cpc": mean_foreign_cpc,
            "cpc_delta_mean": cpc_delta_mean,
            "cpc_delta_range": cpc_delta_range,
            "cpc_std": cpc_std,
            "n_zones": n_zones,
            "tot_area": tot_area,
            "pop_density": pop_density,
            "max_dist": max_dist,
            "avg_dist": avg_dist
        })

    res_df = pd.DataFrame(city_stats)

    # Sort cities by beta-sensitivity (cpc_delta_range or cpc_std)
    res_df = res_df.sort_values(by="cpc_delta_range", ascending=False)

    top_5_sensitive = res_df.head(5)[["city", "fitted_beta", "own_cpc", "cpc_delta_range", "avg_dist"]]
    top_5_insensitive = res_df.tail(5)[["city", "fitted_beta", "own_cpc", "cpc_delta_range", "avg_dist"]]

    print("\n" + "-" * 50)
    print("TOP 5 MOST BEHAVIOUR-SENSITIVE CITIES (Highest Beta Sensitivity):")
    print(top_5_sensitive.to_string(index=False))
    print("-" * 50)
    print("TOP 5 STRUCTURE-DOMINATED CITIES (Lowest Beta Sensitivity):")
    print(top_5_insensitive.to_string(index=False))
    print("-" * 50)

    # Correlations between sensitivity and spatial indicators
    corr_beta = np.corrcoef(res_df["cpc_delta_range"], res_df["fitted_beta"])[0, 1]
    corr_avg_d = np.corrcoef(res_df["cpc_delta_range"], res_df["avg_dist"])[0, 1]
    corr_max_d = np.corrcoef(res_df["cpc_delta_range"], res_df["max_dist"])[0, 1]
    corr_density = np.corrcoef(res_df["cpc_delta_range"], res_df["pop_density"])[0, 1]

    print("\nCorrelations with Beta Sensitivity (CPC Range):")
    print(f"  Corr with Fitted Beta   : {corr_beta:.4f}")
    print(f"  Corr with Avg Distance : {corr_avg_d:.4f}")
    print(f"  Corr with Max Distance : {corr_max_d:.4f}")
    print(f"  Corr with Pop Density  : {corr_density:.4f}")
    print("-" * 50)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt11_city_heterogeneity.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Bar plot of top/bottom cities
    top_bottom_df = pd.concat([res_df.head(10), res_df.tail(10)])
    colors = ["#d62728" if i < 10 else "#1f77b4" for i in range(20)]
    
    axes[0].barh(top_bottom_df["city"], top_bottom_df["cpc_delta_range"], color=colors, alpha=0.85, edgecolor="black")
    axes[0].set_xlabel("CPC Range (Max Foreign Beta - Min Foreign Beta)", fontsize=11)
    axes[0].set_title("Quick Test 11: Top & Bottom 10 Cities by Beta Sensitivity", fontsize=12, fontweight="bold")
    axes[0].invert_yaxis()
    axes[0].grid(axis="x", linestyle=":", alpha=0.6)

    # Scatter plot: Fitted Beta vs Sensitivity
    sns.scatterplot(data=res_df, x="fitted_beta", y="cpc_delta_range", hue="avg_dist", palette="viridis", size="tot_area", sizes=(40, 200), ax=axes[1])
    axes[1].set_xlabel(r"Fitted Beta Parameter $\beta$", fontsize=11)
    axes[1].set_ylabel("CPC Sensitivity Range", fontsize=11)
    axes[1].set_title(f"Beta Sensitivity vs Fitted Beta Parameter\nPearson r = {corr_beta:.4f}", fontsize=12, fontweight="bold")
    axes[1].grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt11_city_heterogeneity.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt11_city_heterogeneity.png'}")
    return res_df, top_5_sensitive, top_5_insensitive

if __name__ == "__main__":
    run_test_11()
