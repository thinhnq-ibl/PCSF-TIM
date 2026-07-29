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
from conference_benchmark import cpc, FULL_CITIES
from validate_behavioral_recovery import predict_tanner_singly, method_a_poisson_mle, method_c_cross_entropy

HELDOUT_25_CITIES = [
    "Boston", "Long_Beach", "New_York", "Philadelphia", "Washington_DC",
    "Atlanta", "Dallas", "El_Paso", "Houston", "Jacksonville",
    "Las_Vegas", "Mesa", "Omaha", "San_Antonio", "Tulsa",
    "Albuquerque", "Charlotte", "Detroit", "Louisville", "Milwaukee",
    "Raleigh", "San_Jose", "Portland", "Seattle", "Virginia_Beach"
]

def run_downstream_validation(K=20):
    print(f"=== Running Downstream Validation (OD Reconstruction) across 25 Cities ===", flush=True)
    
    results = []
    
    for city in HELDOUT_25_CITIES:
        try:
            city_data = load_city(city)
            df = build_pairs_dataframe(city_data)
            df["A_j"] = df["area_j"].values.clip(1e-4)
            
            d = df["d_clamped"].values
            A = df["A_j"].values
            o_idx = df["o_idx"].values
            trips_gt = df["trip_count"].values
            
            unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
            df_mapped = df.copy()
            df_mapped["o_idx"] = o_idx_mapped
            
            # --- 1. Oracle OD Calibration (Method A: Full OD Matrix MLE) ---
            g_oracle, b_oracle, _, _ = method_a_poisson_mle(df_mapped)
            prob_oracle = predict_tanner_singly(o_idx_mapped, A, d, g_oracle, b_oracle)
            
            # Scale by origin production O_i to get OD flows
            n_o = len(unique_o)
            O_i = np.bincount(o_idx_mapped, weights=trips_gt, minlength=n_o)
            T_hat_oracle = prob_oracle * O_i[o_idx_mapped]
            cpc_oracle = cpc(T_hat_oracle, trips_gt)
            
            # --- 2. Inferred θ from Aggregate TLD (Method C: Cross-Entropy on TLD) ---
            d_max = d.max()
            edges = np.linspace(0, d_max, K + 1)
            edges[-1] = np.inf
            bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
            
            y_k = np.array([trips_gt[bin_idx == k].sum() for k in range(K)], float)
            b_k = y_k / y_k.sum()
            
            g_tld, b_tld, _, _ = method_c_cross_entropy(df_mapped, b_k, edges)
            prob_tld = predict_tanner_singly(o_idx_mapped, A, d, g_tld, b_tld)
            T_hat_tld = prob_tld * O_i[o_idx_mapped]
            cpc_tld = cpc(T_hat_tld, trips_gt)
            
            # --- 3. Baseline OD (Distance-blind Random / Uniform Gravity) ---
            prob_base = predict_tanner_singly(o_idx_mapped, A, d, gamma=0.0, beta=0.0)
            T_hat_base = prob_base * O_i[o_idx_mapped]
            cpc_base = cpc(T_hat_base, trips_gt)
            
            # Metrics gap
            cpc_gap = cpc_oracle - cpc_tld
            retention_pct = (cpc_tld / cpc_oracle) * 100.0 if cpc_oracle > 0 else 0.0
            
            results.append({
                "city": city,
                "gamma_oracle": g_oracle,
                "beta_oracle": b_oracle,
                "cpc_oracle": cpc_oracle,
                "gamma_tld": g_tld,
                "beta_tld": b_tld,
                "cpc_tld": cpc_tld,
                "cpc_baseline": cpc_base,
                "cpc_gap": cpc_gap,
                "retention_pct": retention_pct
            })
            
            print(f"[{city:15s}] Baseline CPC: {cpc_base:.4f} | TLD-Inferred CPC: {cpc_tld:.4f} | Oracle CPC: {cpc_oracle:.4f} | Retention: {retention_pct:.2f}%", flush=True)
            
        except Exception as e:
            print(f"Error processing {city}: {e}", flush=True)
            
    res_df = pd.DataFrame(results)
    
    # Save CSV
    out_csv = os.path.join(dir_path, "../results/downstream_od_validation_summary.csv")
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    res_df.to_csv(out_csv, index=False)
    
    mean_cpc_base = res_df["cpc_baseline"].mean()
    mean_cpc_tld = res_df["cpc_tld"].mean()
    mean_cpc_oracle = res_df["cpc_oracle"].mean()
    mean_retention = res_df["retention_pct"].mean()
    
    print("\n" + "="*60)
    print("      DOWNSTREAM OD RECONSTRUCTION VALIDATION SUMMARY")
    print("="*60)
    print(f"Mean Baseline CPC (No Decay):         {mean_cpc_base:.4f}")
    print(f"Mean TLD-Inferred CPC (Our Method):  {mean_cpc_tld:.4f}")
    print(f"Mean Full-OD Oracle CPC:            {mean_cpc_oracle:.4f}")
    print(f"Mean Information Retention (% Oracle): {mean_retention:.2f}%")
    print("="*60 + "\n")
    
    # --- Visualization Plot ---
    output_dir = os.path.join(dir_path, "../figures")
    os.makedirs(output_dir, exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(13, 5.5))
    x = np.arange(len(res_df))
    width = 0.28
    
    rects1 = ax.bar(x - width, res_df["cpc_baseline"], width, label="Distance-Blind Baseline", color="lightgray", edgecolor="k")
    rects2 = ax.bar(x, res_df["cpc_tld"], width, label="TLD-Inferred OD (Proposed)", color="navy", edgecolor="k")
    rects3 = ax.bar(x + width, res_df["cpc_oracle"], width, label="Full-OD Oracle", color="darkgreen", edgecolor="k")
    
    ax.set_xticks(x)
    ax.set_xticklabels(res_df["city"], rotation=60, ha="right", fontsize=9)
    ax.set_ylabel("Common Part of Commuters (CPC)")
    ax.set_title("Downstream Validation: OD Matrix Reconstruction Accuracy (25 Cities)")
    ax.set_ylim(0, 1.0)
    ax.legend(loc="upper right", framealpha=0.9)
    ax.grid(True, linestyle=":", alpha=0.5)
    
    plt.tight_layout()
    fig_path = os.path.join(output_dir, "downstream_od_reconstruction.png")
    plt.savefig(fig_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"Saved Downstream OD Plot to: {fig_path}")
    print(f"Saved Summary CSV to: {out_csv}")

if __name__ == "__main__":
    run_downstream_validation()
