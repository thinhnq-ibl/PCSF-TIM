"""
Validation of Statistical Interpretation of Behavioral Recovery
================================================================
Task 1: Implement 3 recovery methods (Poisson MLE, Multinomial MLE, Cross-Entropy)
Task 2: Compare performance across benchmark cities
Task 3: Validate Scale Invariance across count magnitudes
Task 4: Analytical report and manuscript recommendations
"""

import os
import sys
import time
import numpy as np
import pandas as pd
from scipy.optimize import minimize

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from utils import load_city, build_pairs_dataframe
from conference_benchmark import FULL_CITIES, cpc

# Single-origin or multi-origin Tanner gravity prediction
def predict_tanner_singly(o_idx, A, d, gamma, beta):
    """Production-constrained Tanner gravity probability matrix p_ij(gamma, beta)."""
    log_f = np.log(np.maximum(A, 1e-9)) - gamma * np.log(np.maximum(d, 1e-6)) - beta * d
    n_o = int(o_idx.max()) + 1
    lf_max = np.full(n_o, -np.inf)
    np.maximum.at(lf_max, o_idx, log_f)
    shifted = np.exp(log_f - lf_max[o_idx])
    sum_exp = np.zeros(n_o)
    np.add.at(sum_exp, o_idx, shifted)
    log_B = lf_max + np.log(np.maximum(sum_exp, 1e-300))
    return np.exp(log_f - log_B[o_idx])

# Method A — Poisson MLE (Reference on full OD matrix)
def method_a_poisson_mle(df, gamma_init=1.0, beta_init=0.1):
    d = df["d_clamped"].values
    A = df["A_j"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values
    
    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)
    
    t0 = time.time()
    
    def loss(theta):
        g = np.exp(theta[0])
        b = np.exp(theta[1])
        log_f = np.log(np.maximum(A, 1e-9)) - g * np.log(np.maximum(d, 1e-6)) - b * d
        lf_max = np.full(n_o, -np.inf)
        np.maximum.at(lf_max, o_idx_mapped, log_f)
        shifted = np.exp(log_f - lf_max[o_idx_mapped])
        sum_exp = np.zeros(n_o)
        np.add.at(sum_exp, o_idx_mapped, shifted)
        log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
        
        log_p = log_f - log_denom[o_idx_mapped]
        # Poisson / Multinomial log-likelihood over OD pairs
        return -float(np.sum(trips * log_p))

    best_loss = np.inf
    best_params = (gamma_init, beta_init)
    rng = np.random.default_rng(42)
    
    for run in range(5):
        if run == 0:
            theta_start = [np.log(gamma_init), np.log(beta_init)]
        else:
            theta_start = [rng.normal(np.log(gamma_init), 0.3), rng.normal(np.log(beta_init), 0.3)]
        
        res = minimize(loss, x0=theta_start, method="L-BFGS-B",
                       bounds=[(np.log(0.01), np.log(5.0)), (np.log(0.0001), np.log(2.0))])
        if res.success and res.fun < best_loss:
            best_loss = res.fun
            best_params = (float(np.exp(res.x[0])), float(np.exp(res.x[1])))

    runtime = time.time() - t0
    return best_params[0], best_params[1], best_loss, runtime

# Method B — Multinomial MLE (on raw histogram counts y_k)
def method_b_multinomial_mle(df, y_k, edges, gamma_init=1.0, beta_init=0.1):
    d = df["d_clamped"].values
    A = df["A_j"].values
    o_idx = df["o_idx"].values
    K = len(y_k)
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    t0 = time.time()
    
    def loss(theta):
        g = np.exp(theta[0])
        b = np.exp(theta[1])
        T_hat = predict_tanner_singly(o_idx, A, d, g, b)
        p_k = np.bincount(bin_idx, weights=T_hat, minlength=K).astype(float)
        tot = p_k.sum()
        if tot < 1e-12:
            return 1e12
        p_k = (p_k / tot).clip(1e-15)
        # Multinomial log-likelihood: sum y_k log p_k
        return -float(np.sum(y_k * np.log(p_k)))

    best_loss = np.inf
    best_params = (gamma_init, beta_init)
    rng = np.random.default_rng(42)
    
    for run in range(5):
        if run == 0:
            theta_start = [np.log(gamma_init), np.log(beta_init)]
        else:
            theta_start = [rng.normal(np.log(gamma_init), 0.3), rng.normal(np.log(beta_init), 0.3)]
        
        res = minimize(loss, x0=theta_start, method="L-BFGS-B",
                       bounds=[(np.log(0.01), np.log(5.0)), (np.log(0.0001), np.log(2.0))])
        if res.success and res.fun < best_loss:
            best_loss = res.fun
            best_params = (float(np.exp(res.x[0])), float(np.exp(res.x[1])))

    runtime = time.time() - t0
    return best_params[0], best_params[1], best_loss, runtime

# Method C — Cross-Entropy (on normalized histogram b_k)
def method_c_cross_entropy(df, b_k, edges, gamma_init=1.0, beta_init=0.1):
    d = df["d_clamped"].values
    A = df["A_j"].values
    o_idx = df["o_idx"].values
    K = len(b_k)
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    t0 = time.time()
    
    def loss(theta):
        g = np.exp(theta[0])
        b = np.exp(theta[1])
        T_hat = predict_tanner_singly(o_idx, A, d, g, b)
        p_k = np.bincount(bin_idx, weights=T_hat, minlength=K).astype(float)
        tot = p_k.sum()
        if tot < 1e-12:
            return 1e12
        p_k = (p_k / tot).clip(1e-15)
        # Cross entropy: sum b_k log p_k
        return -float(np.sum(b_k * np.log(p_k)))

    best_loss = np.inf
    best_params = (gamma_init, beta_init)
    rng = np.random.default_rng(42)
    
    for run in range(5):
        if run == 0:
            theta_start = [np.log(gamma_init), np.log(beta_init)]
        else:
            theta_start = [rng.normal(np.log(gamma_init), 0.3), rng.normal(np.log(beta_init), 0.3)]
        
        res = minimize(loss, x0=theta_start, method="L-BFGS-B",
                       bounds=[(np.log(0.01), np.log(5.0)), (np.log(0.0001), np.log(2.0))])
        if res.success and res.fun < best_loss:
            best_loss = res.fun
            best_params = (float(np.exp(res.x[0])), float(np.exp(res.x[1])))

    runtime = time.time() - t0
    return best_params[0], best_params[1], best_loss, runtime


def run_task2_benchmark_comparison(cities, K=20):
    print(f"\n--- Running Task 2: Benchmark Comparison on {len(cities)} cities (K={K}) ---")
    results = []
    
    for city in cities:
        try:
            city_data = load_city(city)
            df = build_pairs_dataframe(city_data)
            df["A_j"] = df["area_j"].values.clip(1e-4) # default attraction
            
            d = df["d_clamped"].values
            trips = df["trip_count"].values
            
            # Distance binning
            d_max = d.max()
            edges = np.linspace(0, d_max, K + 1)
            edges[-1] = np.inf
            bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
            
            # Raw histogram counts y_k and normalized b_k
            y_k = np.array([trips[bin_idx == k].sum() for k in range(K)], float)
            tot_trips = y_k.sum()
            if tot_trips == 0:
                continue
            b_k = y_k / tot_trips
            
            # Method A
            g_a, b_a, loss_a, time_a = method_a_poisson_mle(df)
            # Method B
            g_b, b_b, loss_b, time_b = method_b_multinomial_mle(df, y_k, edges)
            # Method C
            g_c, b_c, loss_c, time_c = method_c_cross_entropy(df, b_k, edges)
            
            # Pairwise differences
            d_alpha_ab = abs(g_a - g_b)
            d_beta_ab = abs(b_a - b_b)
            
            d_alpha_bc = abs(g_b - g_c)
            d_beta_bc = abs(b_b - b_c)
            
            d_alpha_ac = abs(g_a - g_c)
            d_beta_ac = abs(b_a - b_c)
            
            rmse_theta_bc = np.sqrt(((g_b - g_c)**2 + (b_b - b_c)**2) / 2.0)
            rmse_theta_ac = np.sqrt(((g_a - g_c)**2 + (b_a - b_c)**2) / 2.0)
            
            results.append({
                "city": city,
                "tot_trips": tot_trips,
                "g_A": g_a, "b_A": b_a, "time_A": time_a,
                "g_B": g_b, "b_B": b_b, "time_B": time_b,
                "g_C": g_c, "b_C": b_c, "time_C": time_c,
                "d_alpha_AB": d_alpha_ab, "d_beta_AB": d_beta_ab,
                "d_alpha_BC": d_alpha_bc, "d_beta_BC": d_beta_bc,
                "d_alpha_AC": d_alpha_ac, "d_beta_AC": d_beta_ac,
                "rmse_BC": rmse_theta_bc,
                "rmse_AC": rmse_theta_ac
            })
            print(f"[{city}] Method A: ({g_a:.4f}, {b_a:.4f}) | Method B: ({g_b:.4f}, {b_b:.4f}) | Method C: ({g_c:.4f}, {b_c:.4f}) | Δ(B,C): ({d_alpha_bc:.2e}, {d_beta_bc:.2e})")
        except Exception as e:
            print(f"Error processing {city}: {e}")
            
    res_df = pd.DataFrame(results)
    return res_df


def run_task3_scale_invariance(city="New_York", K=20):
    print(f"\n--- Running Task 3: Scale Invariance Experiment on {city} ---")
    city_data = load_city(city)
    df = build_pairs_dataframe(city_data)
    df["A_j"] = df["area_j"].values.clip(1e-4)
    
    d = df["d_clamped"].values
    trips = df["trip_count"].values
    
    edges = np.linspace(0, d.max(), K + 1)
    edges[-1] = np.inf
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    y_k_orig = np.array([trips[bin_idx == k].sum() for k in range(K)], float)
    b_k = y_k_orig / y_k_orig.sum()
    
    # Method C baseline on normalized b_k
    g_c, b_c, loss_c, time_c = method_c_cross_entropy(df, b_k, edges)
    
    scales = [1, 10, 100, 1000, 10000, 100000, 1000000]
    scale_results = []
    
    # Also test specific synthetic prompt vector (0.35, 0.45, 0.20)
    print("\n--- Synthetic Toy Example Verification ---")
    b_toy = np.array([0.35, 0.45, 0.20])
    edges_toy = np.linspace(0, d.max(), 4)
    edges_toy[-1] = np.inf
    
    g_toy_c, b_toy_c, _, _ = method_c_cross_entropy(df, b_toy, edges_toy)
    
    toy_scales = [100, 1000, 10000, 100000]
    for scale in toy_scales:
        y_toy = b_toy * scale
        g_b, b_b, loss_b, t_b = method_b_multinomial_mle(df, y_toy, edges_toy)
        diff_g = abs(g_b - g_toy_c)
        diff_b = abs(b_b - b_toy_c)
        print(f"Toy Scale N={scale:7d} | Y=({y_toy[0]:.0f},{y_toy[1]:.0f},{y_toy[2]:.0f}) | α={g_b:.6f}, β={b_b:.6f} | Δα={diff_g:.2e}, Δβ={diff_b:.2e}")

    print(f"\n--- Full City Scale Sweep ({city}) ---")
    for scale in scales:
        y_k_scale = b_k * scale
        g_b, b_b, loss_b, t_b = method_b_multinomial_mle(df, y_k_scale, edges)
        diff_alpha = abs(g_b - g_c)
        diff_beta = abs(b_b - b_c)
        rmse_diff = np.sqrt((diff_alpha**2 + diff_beta**2)/2.0)
        
        scale_results.append({
            "Scale": scale,
            "Total_Count_N": y_k_scale.sum(),
            "alpha_b": g_b,
            "beta_b": b_b,
            "alpha_c_ref": g_c,
            "beta_c_ref": b_c,
            "delta_alpha": diff_alpha,
            "delta_beta": diff_beta,
            "RMSE_Diff": rmse_diff,
            "Runtime_sec": t_b
        })
        print(f"Scale factor={scale:7d} | N={y_k_scale.sum():12.1f} | α={g_b:.6f}, β={b_b:.6f} | Δα={diff_alpha:.2e}, Δβ={diff_beta:.2e}")
        
    return pd.DataFrame(scale_results)


if __name__ == "__main__":
    # Test on a representative subset of benchmark cities (10 cities across morphology types)
    test_cities = [
        'New_York', 'Los_Angeles', 'Chicago', 'Houston', 'Philadelphia',
        'Phoenix', 'San_Antonio', 'Dallas', 'San_Diego', 'San_Jose'
    ]
    
    print("==========================================================")
    print("STARTING BEHAVIORAL RECOVERY STATISTICAL VALIDATION")
    print("==========================================================")
    
    df_benchmark = run_task2_benchmark_comparison(test_cities)
    df_scale = run_task3_scale_invariance('New_York')
    
    import os
    results_dir = r"d:\research\PCSF-TIM\results"
    os.makedirs(results_dir, exist_ok=True)
    scratch_dir = r"C:\Users\Thinh Nguyen\.gemini\antigravity\brain\14f1c30f-1f49-4f15-ac9d-35d27b41da9a\scratch"
    os.makedirs(scratch_dir, exist_ok=True)
    
    p2 = os.path.join(results_dir, "task2_method_comparison.csv")
    p3 = os.path.join(results_dir, "task3_scale_invariance.csv")
    s2 = os.path.join(scratch_dir, "task2_method_comparison.csv")
    s3 = os.path.join(scratch_dir, "task3_scale_invariance.csv")
    
    df_benchmark.to_csv(p2, index=False)
    df_scale.to_csv(p3, index=False)
    df_benchmark.to_csv(s2, index=False)
    df_scale.to_csv(s3, index=False)
    
    print(f"File 1 exists: {os.path.exists(s2)}, File 2 exists: {os.path.exists(s3)}")
