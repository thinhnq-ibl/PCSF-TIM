import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path)

from utils import load_city, build_pairs_dataframe
from validate_behavioral_recovery import predict_tanner_singly, method_c_cross_entropy

def run_synthetic_recovery_experiment(city_name="Houston", K=20, n_samples=25):
    print(f"=== Running Synthetic Recovery Experiment on {city_name} ===", flush=True)
    
    # 1. Load spatial layout
    city_data = load_city(city_name)
    df = build_pairs_dataframe(city_data)
    df["A_j"] = df["area_j"].values.clip(1e-4)
    
    if len(df) > 50000:
        df_eval = df.sample(n=50000, random_state=42).copy()
    else:
        df_eval = df.copy()
        
    d = df_eval["d_clamped"].values
    A = df_eval["A_j"].values
    unique_o, o_idx_mapped = np.unique(df_eval["o_idx"].values, return_inverse=True)
    
    d_max = d.max()
    edges = np.linspace(0, d_max, K + 1)
    edges[-1] = np.inf
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    # Create evaluation df_eval with mapped origin index
    df_eval["o_idx"] = o_idx_mapped
    
    # 2. Sample True Parameter Pairs (gamma_true, beta_true)
    rng = np.random.default_rng(42)
    gammas_true = rng.uniform(0.3, 2.5, n_samples)
    betas_true = rng.uniform(0.005, 0.12, n_samples)
    
    recovery_results = []
    
    for i in range(n_samples):
        g_true = float(gammas_true[i])
        b_true = float(betas_true[i])
        
        # Step A: Generate Synthetic TLD from Known Parameters
        T_synth = predict_tanner_singly(o_idx_mapped, A, d, g_true, b_true)
        p_k_synth = np.bincount(bin_idx, weights=T_synth, minlength=K).astype(float)
        b_k_synth = p_k_synth / p_k_synth.sum()
        
        # Step B: Recover Parameters from Synthetic TLD
        g_rec, b_rec, loss_val, _ = method_c_cross_entropy(df_eval, b_k_synth, edges, gamma_init=1.0, beta_init=0.05)
        
        # Absolute & Relative Errors
        err_g = abs(g_rec - g_true)
        err_b = abs(b_rec - b_true)
        rel_err_g = (err_g / g_true) * 100.0
        rel_err_b = (err_b / b_true) * 100.0
        
        recovery_results.append({
            "sample_id": i + 1,
            "gamma_true": g_true,
            "beta_true": b_true,
            "gamma_recovered": g_rec,
            "beta_recovered": b_rec,
            "err_gamma": err_g,
            "err_beta": err_b,
            "rel_err_gamma_pct": rel_err_g,
            "rel_err_beta_pct": rel_err_b
        })
        
        print(f"Sample {i+1:02d} | True: ({g_true:.3f}, {b_true:.4f}) | Recovered: ({g_rec:.3f}, {b_rec:.4f}) | Error: Δγ={err_g:.2e} ({rel_err_g:.2f}%), Δβ={err_b:.2e} ({rel_err_b:.2f}%)", flush=True)

    res_df = pd.DataFrame(recovery_results)
    
    # Metrics
    mean_rel_g = res_df["rel_err_gamma_pct"].mean()
    mean_rel_b = res_df["rel_err_beta_pct"].mean()
    r2_g = np.corrcoef(res_df["gamma_true"], res_df["gamma_recovered"])[0, 1]**2
    r2_b = np.corrcoef(res_df["beta_true"], res_df["beta_recovered"])[0, 1]**2
    
    print("\n" + "="*60)
    print("       SYNTHETIC PARAMETER RECOVERY METRICS")
    print("="*60)
    print(f"Mean Relative Error (Gamma γ): {mean_rel_g:.4f}%")
    print(f"Mean Relative Error (Beta β):  {mean_rel_b:.4f}%")
    print(f"R² Score (Gamma γ):            {r2_g:.6f}")
    print(f"R² Score (Beta β):             {r2_b:.6f}")
    print("="*60 + "\n")
    
    # 3. Parity Plots (True vs Recovered)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gamma Parity
    ax1 = axes[0]
    ax1.scatter(res_df["gamma_true"], res_df["gamma_recovered"], color="navy", alpha=0.8, s=60, edgecolors="k")
    g_min, g_max = min(res_df["gamma_true"].min(), res_df["gamma_recovered"].min()) * 0.9, max(res_df["gamma_true"].max(), res_df["gamma_recovered"].max()) * 1.1
    ax1.plot([g_min, g_max], [g_min, g_max], "r--", linewidth=2, label="Perfect Recovery (1:1)")
    ax1.set_xlabel("True Gamma ($\\gamma^*$)")
    ax1.set_ylabel("Recovered Gamma ($\\hat{\\gamma}$)")
    ax1.set_title(f"Gamma Recovery (R² = {r2_g:.4f}, Mean Err = {mean_rel_g:.2f}%)")
    ax1.legend(loc="upper left")
    ax1.grid(True, linestyle=":", alpha=0.6)
    
    # Beta Parity
    ax2 = axes[1]
    ax2.scatter(res_df["beta_true"], res_df["beta_recovered"], color="darkgreen", alpha=0.8, s=60, edgecolors="k")
    b_min, b_max = min(res_df["beta_true"].min(), res_df["beta_recovered"].min()) * 0.9, max(res_df["beta_true"].max(), res_df["beta_recovered"].max()) * 1.1
    ax2.plot([b_min, b_max], [b_min, b_max], "r--", linewidth=2, label="Perfect Recovery (1:1)")
    ax2.set_xlabel("True Beta ($\\beta^*$)")
    ax2.set_ylabel("Recovered Beta ($\\hat{\\beta}$)")
    ax2.set_title(f"Beta Recovery (R² = {r2_b:.4f}, Mean Err = {mean_rel_b:.2f}%)")
    ax2.legend(loc="upper left")
    ax2.grid(True, linestyle=":", alpha=0.6)
    
    plt.tight_layout()
    output_dir = os.path.join(dir_path, "../figures")
    os.makedirs(output_dir, exist_ok=True)
    fig_path = os.path.join(output_dir, "synthetic_recovery_parity.png")
    plt.savefig(fig_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    # Save CSV
    out_csv = os.path.join(dir_path, "../results/synthetic_recovery_summary.csv")
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    res_df.to_csv(out_csv, index=False)
    print(f"Parity Plot saved to: {fig_path}")
    print(f"Results CSV saved to: {out_csv}")

if __name__ == "__main__":
    run_synthetic_recovery_experiment()
