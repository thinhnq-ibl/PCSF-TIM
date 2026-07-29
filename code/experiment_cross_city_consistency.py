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

HELDOUT_25_CITIES = [
    "Boston", "Long_Beach", "New_York", "Philadelphia", "Washington_DC",
    "Atlanta", "Dallas", "El_Paso", "Houston", "Jacksonville",
    "Las_Vegas", "Mesa", "Omaha", "San_Antonio", "Tulsa",
    "Albuquerque", "Charlotte", "Detroit", "Louisville", "Milwaukee",
    "Raleigh", "San_Jose", "Portland", "Seattle", "Virginia_Beach"
]

def run_cross_city_consistency(K=20):
    print(f"=== Running Cross-City Consistency Experiment across {len(HELDOUT_25_CITIES)} Cities ===", flush=True)
    
    # Target synthetic ground truth parameters to recover across all cities
    gamma_target = 1.35
    beta_target = 0.035
    
    results = []
    
    for city in HELDOUT_25_CITIES:
        try:
            city_data = load_city(city)
            df = build_pairs_dataframe(city_data)
            df["A_j"] = df["area_j"].values.clip(1e-4)
            
            if len(df) > 50000:
                df_eval = df.sample(n=50000, random_state=42).copy()
            else:
                df_eval = df.copy()
                
            d = df_eval["d_clamped"].values
            A = df_eval["A_j"].values
            unique_o, o_idx_mapped = np.unique(df_eval["o_idx"].values, return_inverse=True)
            trips_real = df_eval["trip_count"].values
            
            d_max = d.max()
            edges = np.linspace(0, d_max, K + 1)
            edges[-1] = np.inf
            bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
            
            df_eval["o_idx"] = o_idx_mapped
            
            # --- Part 1: Synthetic Recovery on City Spatial Layout ---
            T_synth = predict_tanner_singly(o_idx_mapped, A, d, gamma_target, beta_target)
            p_k_synth = np.bincount(bin_idx, weights=T_synth, minlength=K).astype(float)
            b_k_synth = p_k_synth / p_k_synth.sum()
            
            g_rec_synth, b_rec_synth, _, _ = method_c_cross_entropy(df_eval, b_k_synth, edges, gamma_init=1.0, beta_init=0.05)
            
            err_g_synth = abs(g_rec_synth - gamma_target)
            err_b_synth = abs(b_rec_synth - beta_target)
            rel_err_g_synth = (err_g_synth / gamma_target) * 100.0
            rel_err_b_synth = (err_b_synth / beta_target) * 100.0
            
            # --- Part 2: Real-Data Parameter Estimation ---
            y_k_real = np.array([trips_real[bin_idx == k].sum() for k in range(K)], float)
            b_k_real = y_k_real / y_k_real.sum()
            g_real, b_real, _, _ = method_c_cross_entropy(df_eval, b_k_real, edges, gamma_init=1.0, beta_init=0.05)
            
            results.append({
                "city": city,
                "gamma_true": gamma_target,
                "beta_true": beta_target,
                "gamma_synth_rec": g_rec_synth,
                "beta_synth_rec": b_rec_synth,
                "err_gamma_synth": err_g_synth,
                "err_beta_synth": err_b_synth,
                "rel_err_gamma_pct": rel_err_g_synth,
                "rel_err_beta_pct": rel_err_b_synth,
                "gamma_real": g_real,
                "beta_real": b_real
            })
            print(f"[{city:15s}] Synth Rec: γ={g_rec_synth:.4f} (Err={rel_err_g_synth:.3f}%), β={b_rec_synth:.5f} (Err={rel_err_b_synth:.3f}%) | Real: γ={g_real:.3f}, β={b_real:.4f}", flush=True)
            
        except Exception as e:
            print(f"Error processing {city}: {e}", flush=True)
            
    res_df = pd.DataFrame(results)
    
    # Save CSV
    out_csv = os.path.join(dir_path, "../results/cross_city_consistency_summary.csv")
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    res_df.to_csv(out_csv, index=False)
    
    print("\n" + "="*60)
    print("      CROSS-CITY CONSISTENCY SUMMARY (25 CITIES)")
    print("="*60)
    print(f"Synthetic Recovery - Max Gamma Rel Error: {res_df['rel_err_gamma_pct'].max():.4f}%")
    print(f"Synthetic Recovery - Max Beta Rel Error:  {res_df['rel_err_beta_pct'].max():.4f}%")
    print(f"Synthetic Recovery - Mean Gamma Rel Err:  {res_df['rel_err_gamma_pct'].mean():.4f}%")
    print(f"Synthetic Recovery - Mean Beta Rel Err:   {res_df['rel_err_beta_pct'].mean():.4f}%")
    print(f"Real Data Parameter Range - Gamma γ:      [{res_df['gamma_real'].min():.3f}, {res_df['gamma_real'].max():.3f}] (Mean={res_df['gamma_real'].mean():.3f}, Std={res_df['gamma_real'].std():.3f})")
    print(f"Real Data Parameter Range - Beta β:       [{res_df['beta_real'].min():.4f}, {res_df['beta_real'].max():.4f}] (Mean={res_df['beta_real'].mean():.4f}, Std={res_df['beta_real'].std():.4f})")
    print("="*60 + "\n")
    
    # --- Visualizations ---
    output_dir = os.path.join(dir_path, "../figures")
    os.makedirs(output_dir, exist_ok=True)
    
    # Figure 1: Synthetic Recovery Errors Across 25 Cities
    fig, ax = plt.subplots(figsize=(12, 5))
    x_indices = np.arange(len(res_df))
    width = 0.35
    
    ax.bar(x_indices - width/2, res_df["rel_err_gamma_pct"], width, label="Gamma Rel Error (%)", color="navy")
    ax.bar(x_indices + width/2, res_df["rel_err_beta_pct"], width, label="Beta Rel Error (%)", color="darkred")
    
    ax.set_xticks(x_indices)
    ax.set_xticklabels(res_df["city"], rotation=60, ha="right", fontsize=9)
    ax.set_ylabel("Relative Recovery Error (%)")
    ax.set_title("Cross-City Synthetic Parameter Recovery Errors (25 Cities)")
    ax.set_ylim(0, max(0.05, res_df["rel_err_beta_pct"].max() * 1.2))
    ax.legend(loc="upper right")
    ax.grid(True, linestyle=":", alpha=0.5)
    
    plt.tight_layout()
    fig1_path = os.path.join(output_dir, "cross_city_synthetic_recovery_errors.png")
    plt.savefig(fig1_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    # Figure 2: Real-Data Estimated Parameters Across 25 Cities
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.scatter(res_df["gamma_real"], res_df["beta_real"], color="teal", s=80, edgecolors="k", zorder=3)
    
    for i, txt in enumerate(res_df["city"]):
        ax.annotate(txt, (res_df["gamma_real"].iloc[i], res_df["beta_real"].iloc[i]), fontsize=8, xytext=(4, 2), textcoords="offset points")
        
    ax.set_xlabel("Estimated Power-law Exponent (\\gamma)")
    ax.set_ylabel("Estimated Exponential Decay (\\beta)")
    ax.set_title("Real-World Estimated Travel-Decay Parameters across 25 Cities")
    ax.grid(True, linestyle=":", alpha=0.6)
    
    plt.tight_layout()
    fig2_path = os.path.join(output_dir, "cross_city_real_parameters.png")
    plt.savefig(fig2_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"Figure 1 saved: {fig1_path}")
    print(f"Figure 2 saved: {fig2_path}")

if __name__ == "__main__":
    run_cross_city_consistency()
