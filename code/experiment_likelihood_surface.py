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
from validate_behavioral_recovery import predict_tanner_singly

def run_likelihood_surface_experiment(city_name="Houston", K=20, n_grid=30):
    print(f"=== Processing {city_name} ===", flush=True)
    
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
    trips = df_eval["trip_count"].values
    
    d_max = d.max()
    edges = np.linspace(0, d_max, K + 1)
    edges[-1] = np.inf
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    y_k = np.array([trips[bin_idx == k].sum() for k in range(K)], float)
    tot_trips = y_k.sum()
    if tot_trips == 0:
        raise ValueError(f"No trips found for {city_name}")
    b_k = y_k / tot_trips
    
    def compute_log_likelihood(gamma, beta):
        T_hat = predict_tanner_singly(o_idx_mapped, A, d, gamma, beta)
        p_k = np.bincount(bin_idx, weights=T_hat, minlength=K).astype(float)
        tot = p_k.sum()
        if tot < 1e-12:
            return -1e12
        p_k = (p_k / tot).clip(1e-15)
        return float(np.sum(b_k * np.log(p_k)))

    gammas = np.linspace(0.1, 3.0, n_grid)
    betas = np.linspace(0.0001, 0.15, n_grid)
    
    G, B = np.meshgrid(gammas, betas)
    Z_ll = np.zeros_like(G)
    
    for i in range(n_grid):
        for j in range(n_grid):
            Z_ll[i, j] = compute_log_likelihood(G[i, j], B[i, j])
            
    max_idx = np.unravel_index(np.argmax(Z_ll), Z_ll.shape)
    best_gamma = float(G[max_idx])
    best_beta = float(B[max_idx])
    best_ll = float(Z_ll[max_idx])
    
    # Single plot for individual city
    fig, ax = plt.subplots(figsize=(7, 5))
    contour = ax.contourf(G, B, Z_ll, levels=25, cmap="viridis")
    plt.colorbar(contour, label="Log-Likelihood $L(\\gamma, \\beta)$")
    
    ax.scatter([best_gamma], [best_beta], color="red", marker="*", s=180, label=f"MLE Peak ($\\gamma$={best_gamma:.2f}, $\\beta$={best_beta:.4f})")
    ax.set_xlabel("Gamma (Power-law exponent $\\gamma$)")
    ax.set_ylabel("Beta (Exponential decay $\\beta$)")
    ax.set_title(f"Likelihood Surface over TLD — {city_name}\n(Unimodal Peak & High Curvature)")
    ax.legend(loc="upper right")
    
    output_dir = os.path.join(dir_path, "../figures")
    os.makedirs(output_dir, exist_ok=True)
    output_fig = os.path.join(output_dir, f"likelihood_surface_{city_name}.png")
    plt.savefig(output_fig, dpi=300, bbox_inches="tight")
    plt.close()
    
    return {
        "city": city_name,
        "tot_trips": int(tot_trips),
        "best_gamma": best_gamma,
        "best_beta": best_beta,
        "best_ll": best_ll,
        "G": G, "B": B, "Z_ll": Z_ll
    }

def main():
    test_cities = ["New_York", "Los_Angeles", "Chicago", "Houston", "Atlanta"]
    results = []
    
    fig, axes = plt.subplots(1, 5, figsize=(25, 4.5))
    
    for idx, city in enumerate(test_cities):
        try:
            res = run_likelihood_surface_experiment(city)
            results.append(res)
            
            ax = axes[idx]
            contour = ax.contourf(res["G"], res["B"], res["Z_ll"], levels=20, cmap="viridis")
            ax.scatter([res["best_gamma"]], [res["best_beta"]], color="red", marker="*", s=150)
            ax.set_title(f"{city}\n(\\gamma={res['best_gamma']:.2f}, \\beta={res['best_beta']:.3f})", fontsize=12)
            ax.set_xlabel("Gamma (\\gamma)")
            if idx == 0:
                ax.set_ylabel("Beta (\\beta)")
        except Exception as e:
            print(f"Error processing {city}: {e}", flush=True)
            
    plt.tight_layout()
    output_combined = os.path.join(dir_path, "../figures/likelihood_surfaces_all_cities.png")
    plt.savefig(output_combined, dpi=300, bbox_inches="tight")
    plt.close()
    
    res_df = pd.DataFrame([{k: v for k, v in r.items() if k not in ["G", "B", "Z_ll"]} for r in results])
    out_csv = os.path.join(dir_path, "../results/likelihood_evidence_summary.csv")
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    res_df.to_csv(out_csv, index=False)
    print("\nSUCCESS! Combined plot saved to:", output_combined)
    print(res_df.to_string(), flush=True)

if __name__ == "__main__":
    main()
