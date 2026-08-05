"""
Quick Test 12 — Evidence for Parameter Identification & Solution Stability (QT12):
Evaluates solution stability across 20 random multi-start initializations and synthetic parameter recovery
to build empirical statistical evidence supporting parameter identification.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.optimize import minimize

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, fit_beta_tld_mle, predict_gravity_od

def run_test_12():
    print("=" * 60)
    print("Running Quick Test 12: Parameter Identification Evidence & Stability")
    print("=" * 60)

    cities = ALL_50_CITIES[:15] # 15 benchmark cities for intensive multi-start test
    n_restarts = 20

    multi_start_results = []
    rng = np.random.default_rng(42)

    for city in cities:
        nodes, df = process_city_data(city)
        trips = df["trip_count"].values
        d = df["d_clamped"].values
        A = df["A_j_clamped"].values
        o_idx = df["o_idx"].values
        unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
        n_o = len(unique_o)

        recovered_betas = []

        for r in range(n_restarts):
            # random starting point in [0.01, 2.0]
            init_beta = rng.uniform(0.01, 2.0)

            def loss(log_b):
                b = np.exp(log_b[0])
                log_f = np.log(A) - b * d
                lf_max = np.full(n_o, -np.inf)
                np.maximum.at(lf_max, o_idx_mapped, log_f)
                shifted = np.exp(log_f - lf_max[o_idx_mapped])
                sum_exp = np.zeros(n_o)
                np.add.at(sum_exp, o_idx_mapped, shifted)
                log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
                log_p = log_f - log_denom[o_idx_mapped]
                return -float(np.sum(trips * log_p))

            res = minimize(loss, x0=[np.log(init_beta)], method="L-BFGS-B")
            if res.success:
                recovered_betas.append(float(np.exp(res.x[0])))

        rec_betas = np.array(recovered_betas)
        std_beta = float(np.std(rec_betas))
        cv_beta = float(std_beta / (np.mean(rec_betas) + 1e-9))

        multi_start_results.append({
            "city": city,
            "mean_beta": float(np.mean(rec_betas)),
            "std_beta": std_beta,
            "cv_beta": cv_beta,
            "min_beta": float(np.min(rec_betas)),
            "max_beta": float(np.max(rec_betas))
        })

    ms_df = pd.DataFrame(multi_start_results)

    # 2. Synthetic Parameter Recovery Test
    synthetic_results = []
    test_betas = [0.10, 0.25, 0.40, 0.55, 0.70]
    sample_city = "Austin"
    nodes, df_austin = process_city_data(sample_city)

    for beta_true in test_betas:
        # Generate synthetic OD trips from known beta_true
        T_synth = predict_gravity_od(df_austin, beta_true)
        df_synth = df_austin.copy()
        df_synth["trip_count"] = T_synth

        # Recover beta from synthetic TLD
        beta_recovered = fit_beta_tld_mle(df_synth)
        rel_err = abs(beta_recovered - beta_true) / beta_true

        synthetic_results.append({
            "beta_true": beta_true,
            "beta_recovered": beta_recovered,
            "rel_error": rel_err
        })

    synth_df = pd.DataFrame(synthetic_results)
    avg_rel_err = float(synth_df["rel_error"].mean())
    avg_cv = float(ms_df["cv_beta"].mean())

    print("\n" + "-" * 50)
    print("QUICK TEST 12 STABILITY & RECOVERY EVIDENCE:")
    print("-" * 50)
    print(f"  Average Multi-Start CV across cities : {avg_cv*100:.4f}%")
    print(f"  Synthetic Recovery Relative Error    : {avg_rel_err*100:.4f}%")
    print("-" * 50)

    if avg_cv < 0.001 and avg_rel_err < 0.01:
        print("  => DECISION: Strong empirical statistical evidence supports parameter identification!")
        print("               Likelihood surface exhibits sharp, stable, unique global optimum.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    ms_df.to_csv(results_dir / "qt12_multi_start_stability.csv", index=False)
    synth_df.to_csv(results_dir / "qt12_synthetic_recovery.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Subplot 1: Multi-start CV across cities
    axes[0].bar(ms_df["city"], ms_df["cv_beta"] * 100, color="#2ca02c", alpha=0.85, edgecolor="black")
    axes[0].set_ylabel("Coefficient of Variation (%)", fontsize=11)
    axes[0].set_title(f"Multi-Start Recovery Variance (20 Initializations)\nMean CV = {avg_cv*100:.4f}%", fontsize=12, fontweight="bold")
    axes[0].tick_params(axis="x", rotation=45)
    axes[0].grid(axis="y", linestyle=":", alpha=0.6)

    # Subplot 2: Synthetic Recovery True vs Recovered
    axes[1].plot(synth_df["beta_true"], synth_df["beta_recovered"], "o-", color="#1f77b4", linewidth=2, markersize=8, label="Recovered $\\hat{\\beta}$")
    axes[1].plot(synth_df["beta_true"], synth_df["beta_true"], "r--", linewidth=2, label="True Ground-Truth $\\beta^*$")
    axes[1].set_xlabel(r"Synthetic True Parameter $\beta^*$", fontsize=11)
    axes[1].set_ylabel(r"Recovered Parameter $\hat{\beta}_{TLD}$", fontsize=11)
    axes[1].set_title(f"Synthetic Parameter Recovery\nMean Rel Error = {avg_rel_err*100:.2f}%", fontsize=12, fontweight="bold")
    axes[1].grid(True, linestyle=":", alpha=0.6)
    axes[1].legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt12_identifiability_stability.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt12_identifiability_stability.png'}")
    return ms_df, synth_df, avg_cv, avg_rel_err

if __name__ == "__main__":
    run_test_12()
