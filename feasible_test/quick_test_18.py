"""
Quick Test 18 — Noise Robustness Analysis (QT18):
Evaluates model degradation under 5%, 10%, and 20% additive Gaussian noise on TLD and Urban Features.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_tld_mle

def run_test_18():
    print("=" * 60)
    print("Running Quick Test 18: Noise Robustness Analysis")
    print("=" * 60)

    noise_levels = [0.0, 0.05, 0.10, 0.20]
    rng = np.random.default_rng(42)

    results = []

    for noise in noise_levels:
        rel_errors = []

        for city in ALL_50_CITIES[:20]: # 20 cities benchmark
            nodes, df = process_city_data(city)
            beta_true = fit_beta_tld_mle(df)

            # Corrupt trip counts with noise
            trips_noisy = np.maximum(df["trip_count"].values * (1.0 + rng.normal(0, noise, size=len(df))), 0.0)
            df_noisy = df.copy()
            df_noisy["trip_count"] = trips_noisy

            beta_recovered = fit_beta_tld_mle(df_noisy)
            rel_err = abs(beta_recovered - beta_true) / (beta_true + 1e-6)
            rel_errors.append(rel_err)

        results.append({
            "noise_level": noise,
            "mean_beta_error_pct": float(np.mean(rel_errors) * 100.0)
        })

    res_df = pd.DataFrame(results)

    print("\n" + "=" * 50)
    print("QUICK TEST 18 NOISE ROBUSTNESS RESULTS:")
    print("=" * 50)
    print(res_df.to_string(index=False))
    print("=" * 50)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt18_noise_robustness.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7, 5))
    x_labels = [f"{int(n*100)}%" for n in noise_levels]
    plt.plot(x_labels, res_df["mean_beta_error_pct"], "o-", color="#2ca02c", linewidth=2, markersize=8)

    plt.ylabel(r"Relative Error in Estimated $\hat{\beta}$ (%)", fontsize=11)
    plt.xlabel("Additive Noise Level on Data", fontsize=11)
    plt.title(r"Quick Test 18: Parameter $\beta$ Recovery Robustness under Data Noise", fontsize=12, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt18_noise_robustness.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt18_noise_robustness.png'}")
    return res_df

if __name__ == "__main__":
    run_test_18()
