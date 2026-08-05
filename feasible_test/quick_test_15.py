"""
Quick Test 15 — Structure Perturbation Analysis (QT15):
Evaluates how noise/perturbations in spatial mass vectors (Oi, Aj) impact OD flow CPC, JSD, and Trip Distance.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.spatial.distance import jensenshannon

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, predict_gravity_od, calculate_cpc
from quick_test_10 import compute_tld_distribution

def run_test_15():
    print("=" * 60)
    print("Running Quick Test 15: Structure Perturbation Analysis")
    print("=" * 60)

    noise_levels = [0.0, 0.10, 0.25, 0.50]
    rng = np.random.default_rng(42)

    results = []

    for noise in noise_levels:
        cpc_list = []
        jsd_list = []
        dist_err_list = []

        for city in ALL_50_CITIES[:20]: # 20 cities benchmark
            nodes, df = process_city_data(city)
            actual = df["trip_count"].values
            d = df["d_clamped"].values
            beta = fit_beta_od_mle(df)

            obs_avg_d = float(np.sum(actual * d) / (np.sum(actual) + 1e-9))
            obs_tld = compute_tld_distribution(df, actual)

            # Perturb O_i and A_j
            O_orig = nodes["O_i"].values.copy()
            A_orig = nodes["A_j"].values.copy()

            if noise > 0:
                O_pert = np.maximum(O_orig * (1.0 + rng.normal(0, noise, size=len(O_orig))), 0.0)
                A_pert = np.maximum(A_orig * (1.0 + rng.normal(0, noise, size=len(A_orig))), 0.0)
            else:
                O_pert = O_orig
                A_pert = A_orig

            T_hat = predict_gravity_od(df, beta, custom_O=O_pert, custom_A=A_pert, node_ids=nodes["idx"].values)

            # Metrics
            cpc_val = calculate_cpc(actual, T_hat)
            pred_tld = compute_tld_distribution(df, T_hat)
            jsd_val = float(jensenshannon(obs_tld, pred_tld) ** 2)
            pred_avg_d = float(np.sum(T_hat * d) / (np.sum(T_hat) + 1e-9))
            d_err = abs(pred_avg_d - obs_avg_d)

            cpc_list.append(cpc_val)
            jsd_list.append(jsd_val)
            dist_err_list.append(d_err)

        results.append({
            "noise_level": noise,
            "mean_cpc": float(np.mean(cpc_list)),
            "mean_jsd": float(np.mean(jsd_list)),
            "mean_dist_err_km": float(np.mean(dist_err_list))
        })

    res_df = pd.DataFrame(results)

    print("\n" + "=" * 50)
    print("QUICK TEST 15 STRUCTURE PERTURBATION RESULTS:")
    print("=" * 50)
    print(res_df.to_string(index=False))
    print("=" * 50)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt15_structure_perturbation.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    fig, ax1 = plt.subplots(figsize=(7.5, 5))
    x_labels = [f"{int(n*100)}%" for n in noise_levels]

    color = "#1f77b4"
    ax1.set_xlabel("Structure Perturbation Noise Level", fontsize=11)
    ax1.set_ylabel("Mean Common Part of Commuters (CPC)", color=color, fontsize=11)
    ax1.plot(x_labels, res_df["mean_cpc"], "o-", color=color, linewidth=2, markersize=8, label="CPC")
    ax1.tick_params(axis="y", labelcolor=color)
    ax1.grid(True, linestyle=":", alpha=0.6)

    ax2 = ax1.twinx()
    color = "#d62728"
    ax2.set_ylabel("JSD TLD Divergence", color=color, fontsize=11)
    ax2.plot(x_labels, res_df["mean_jsd"], "s--", color=color, linewidth=2, markersize=8, label="JSD")
    ax2.tick_params(axis="y", labelcolor=color)

    plt.title("Quick Test 15: Structure Perturbation Impact on OD Flow & TLD", fontsize=12, fontweight="bold")
    plt.tight_layout()
    plt.savefig(figures_dir / "qt15_structure_perturbation.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt15_structure_perturbation.png'}")
    return res_df

if __name__ == "__main__":
    run_test_15()
