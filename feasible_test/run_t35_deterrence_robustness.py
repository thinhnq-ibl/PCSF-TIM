"""
T35: Deterrence Function Robustness & Complexity Test
======================================================
Evaluates parameter recoverability across the compression grid
(Full OD -> 20 -> 10 -> 5 -> 3 bins) for Chicago under:
  1. Exponential decay: e^{-beta * d}
  2. Power-law decay: d^{-alpha}
  3. Tanner decay: d^{-alpha} * e^{-beta * d}

Provides empirical evidence for the 3-Tier decay probe architecture.
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize_scalar, minimize

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import process_city_data

# Generic likelihood helper functions
def neg_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips):
    lf_max = np.full(n_o, -np.inf)
    np.maximum.at(lf_max, o_idx_mapped, log_f)
    shifted = np.exp(log_f - lf_max[o_idx_mapped])
    sum_exp = np.zeros(n_o)
    np.add.at(sum_exp, o_idx_mapped, shifted)
    log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
    log_p = log_f - log_denom[o_idx_mapped]
    return -float(np.sum(trips * log_p))

def neg_tld_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips, bin_idx, y_k, K):
    lf_max = np.full(n_o, -np.inf)
    np.maximum.at(lf_max, o_idx_mapped, log_f)
    shifted = np.exp(log_f - lf_max[o_idx_mapped])
    sum_exp = np.zeros(n_o)
    np.add.at(sum_exp, o_idx_mapped, shifted)
    log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
    log_p = log_f - log_denom[o_idx_mapped]
    
    p_ij = np.exp(log_p)
    p_k = np.bincount(bin_idx, weights=p_ij, minlength=K).astype(float)
    p_k_tot = p_k.sum()
    if p_k_tot < 1e-12:
        return 1e12
    p_k = (p_k / p_k_tot).clip(1e-15)
    return -float(np.sum(y_k * np.log(p_k)))

def run_t35_stress():
    print("=" * 80)
    print("RUNNING T35: DETERRENCE FUNCTION ROBUSTNESS & COMPLEXITY TEST (CHICAGO)")
    print("=" * 80)
    
    nodes, df = process_city_data("Chicago")
    d = df["d_clamped"].values
    log_d = np.log(d)
    A = df["A_j_clamped"].values
    log_A = np.log(A)
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values
    
    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)
    
    d_max = d.max()
    
    # Define solvers for each functional form
    
    # ----------------------------------------------------
    # 1. EXPONENTIAL
    # ----------------------------------------------------
    def fit_exp_od():
        def obj(beta):
            log_f = log_A - beta * d
            return neg_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips)
        res = minimize_scalar(obj, bounds=(0.0001, 3.0), method="bounded")
        return float(res.x)
        
    def fit_exp_tld(K):
        edges = np.linspace(0, d_max, K + 1)
        edges[-1] = np.inf
        bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
        y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
        
        def obj(beta):
            log_f = log_A - beta * d
            return neg_tld_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips, bin_idx, y_k, K)
            
        # Grid start
        grid = np.linspace(0.001, 3.0, 15)
        likes = [obj(b) for b in grid]
        best_b = grid[np.argmin(likes)]
        res = minimize_scalar(obj, bounds=(max(0.0001, best_b - 0.25), min(3.0, best_b + 0.25)), method="bounded")
        return float(res.x)

    # ----------------------------------------------------
    # 2. POWER-LAW
    # ----------------------------------------------------
    def fit_power_od():
        def obj(alpha):
            log_f = log_A - alpha * log_d
            return neg_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips)
        res = minimize_scalar(obj, bounds=(0.0001, 5.0), method="bounded")
        return float(res.x)
        
    def fit_power_tld(K):
        edges = np.linspace(0, d_max, K + 1)
        edges[-1] = np.inf
        bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
        y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
        
        def obj(alpha):
            log_f = log_A - alpha * log_d
            return neg_tld_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips, bin_idx, y_k, K)
            
        # Grid start
        grid = np.linspace(0.001, 5.0, 15)
        likes = [obj(a) for a in grid]
        best_a = grid[np.argmin(likes)]
        res = minimize_scalar(obj, bounds=(max(0.0001, best_a - 0.4), min(5.0, best_a + 0.4)), method="bounded")
        return float(res.x)

    # ----------------------------------------------------
    # 3. TANNER (2 Parameters)
    # ----------------------------------------------------
    def fit_tanner_od():
        def obj(params):
            alpha, beta = params
            log_f = log_A - alpha * log_d - beta * d
            return neg_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips)
            
        # 2D Grid search to get a robust start point
        grid_alpha = np.linspace(0.0, 4.0, 8)
        grid_beta = np.linspace(0.0, 2.0, 8)
        best_like = np.inf
        best_start = (1.0, 0.1)
        for a in grid_alpha:
            for b in grid_beta:
                like = obj((a, b))
                if like < best_like:
                    best_like = like
                    best_start = (a, b)
                    
        res = minimize(obj, x0=best_start, bounds=[(0.0, 5.0), (0.0, 3.0)], method="L-BFGS-B")
        return res.x[0], res.x[1]
        
    def fit_tanner_tld(K):
        edges = np.linspace(0, d_max, K + 1)
        edges[-1] = np.inf
        bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
        y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
        
        def obj(params):
            alpha, beta = params
            log_f = log_A - alpha * log_d - beta * d
            return neg_tld_log_like_generic(log_f, unique_o, o_idx_mapped, n_o, trips, bin_idx, y_k, K)
            
        # 2D Grid search
        grid_alpha = np.linspace(0.0, 4.0, 8)
        grid_beta = np.linspace(0.0, 2.0, 8)
        best_like = np.inf
        best_start = (1.0, 0.1)
        for a in grid_alpha:
            for b in grid_beta:
                like = obj((a, b))
                if like < best_like:
                    best_like = like
                    best_start = (a, b)
                    
        res = minimize(obj, x0=best_start, bounds=[(0.0, 5.0), (0.0, 3.0)], method="L-BFGS-B")
        return res.x[0], res.x[1]

    # Calculate Oracle references
    print("Fitting Oracle parameters on full OD matrix...")
    beta_oracle_exp = fit_exp_od()
    alpha_oracle_pow = fit_power_od()
    alpha_oracle_tan, beta_oracle_tan = fit_tanner_od()
    
    print(f"  Oracle Exponential beta* = {beta_oracle_exp:.4f}")
    print(f"  Oracle Power-law   alpha* = {alpha_oracle_pow:.4f}")
    print(f"  Oracle Tanner      alpha* = {alpha_oracle_tan:.4f}, beta* = {beta_oracle_tan:.4f}")
    
    bins_grid = [20, 10, 5, 3]
    results = []
    
    for K in bins_grid:
        print(f"\nProcessing {K}-bin TLD compression...")
        
        # Fit Exp
        beta_est = fit_exp_tld(K)
        err_exp = abs(beta_est - beta_oracle_exp) / beta_oracle_exp * 100
        
        # Fit Power
        alpha_est = fit_power_tld(K)
        err_pow = abs(alpha_est - alpha_oracle_pow) / alpha_oracle_pow * 100
        
        # Fit Tanner
        alpha_tan, beta_tan = fit_tanner_tld(K)
        err_tan_a = abs(alpha_tan - alpha_oracle_tan) / max(alpha_oracle_tan, 1e-4) * 100
        err_tan_b = abs(beta_tan - beta_oracle_tan) / max(beta_oracle_tan, 1e-4) * 100
        err_tan = (err_tan_a + err_tan_b) / 2.0
        
        print(f"  [K={K:02d}] Exponential: beta = {beta_est:.4f} (Error = {err_exp:.2f}%)")
        print(f"  [K={K:02d}] Power-law  : alpha = {alpha_est:.4f} (Error = {err_pow:.2f}%)")
        print(f"  [K={K:02d}] Tanner     : alpha = {alpha_tan:.4f}, beta = {beta_tan:.4f} (Avg Error = {err_tan:.2f}%)")
        
        results.append({
            "K": K,
            "Exp_Beta": beta_est, "Exp_Err": err_exp,
            "Pow_Alpha": alpha_est, "Pow_Err": err_pow,
            "Tan_Alpha": alpha_tan, "Tan_Beta": beta_tan,
            "Tan_Err_A": err_tan_a, "Tan_Err_B": err_tan_b, "Tan_Err_Avg": err_tan
        })
        
    print("\n" + "=" * 80)
    print("T35 RESULTS COMPILATION")
    print("=" * 80)
    print("Bins | Exp Error | Pow Error | Tanner Avg Error (alpha err / beta err)")
    print("-" * 80)
    for r in results:
        print(f" {r['K']:2d}  |   {r['Exp_Err']:5.2f}%  |   {r['Pow_Err']:5.2f}%  |   {r['Tan_Err_Avg']:5.2f}% ({r['Tan_Err_A']:.1f}% / {r['Tan_Err_B']:.1f}%)")
    print("=" * 80)

if __name__ == "__main__":
    run_t35_stress()
