"""
Dallas Anomaly Audit: Likelihood Profiling for beta
===================================================
Investigates if the 720% beta estimation error in Dallas under 3-bin TLD
is due to optimization instability (local minima) or genuine non-identifiability.
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize_scalar

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import process_city_data, fit_beta_od_mle, fit_beta_tld_mle

def get_likelihood_profile():
    city = "Dallas"
    print("=" * 80)
    print(f"DALLAS ANOMALY AUDIT: LIKELIHOOD PROFILE FOR BETA")
    print("=" * 80)
    
    nodes, df = process_city_data(city)
    
    # Extract data for MLE
    d = df["d_clamped"].values
    A = df["A_j_clamped"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values
    
    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)
    
    # 1. OD-MLE Likelihood Function
    def neg_log_like(beta_val):
        beta = float(beta_val)
        log_f = np.log(A) - beta * d
        lf_max = np.full(n_o, -np.inf)
        np.maximum.at(lf_max, o_idx_mapped, log_f)
        shifted = np.exp(log_f - lf_max[o_idx_mapped])
        sum_exp = np.zeros(n_o)
        np.add.at(sum_exp, o_idx_mapped, shifted)
        log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
        log_p = log_f - log_denom[o_idx_mapped]
        return -float(np.sum(trips * log_p))
    
    # 2. TLD-MLE Likelihood Function
    def get_neg_tld_log_like(K):
        d_max = d.max()
        edges = np.linspace(0, d_max, K + 1)
        edges[-1] = np.inf
        bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
        y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
        tot_trips = y_k.sum()
        
        def neg_tld_log_like(beta_val):
            beta = float(beta_val)
            log_f = np.log(A) - beta * d
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
        
        return neg_tld_log_like, y_k

    # True OD-MLE fit
    beta_od = fit_beta_od_mle(df)
    nll_od_true = neg_log_like(beta_od)
    print(f"True OD-MLE beta: {beta_od:.4f} (NegLogLike: {nll_od_true:.4f})")
    
    # Multi-start fit for 3-bin TLD
    tld3_fun, y_k3 = get_likelihood_profile_for_k(3, df, neg_log_like) # Wait, let's just define the profile locally.
    
def get_likelihood_profile_for_k(K, df, d, A, o_idx, trips, unique_o, o_idx_mapped, n_o):
    d_max = d.max()
    edges = np.linspace(0, d_max, K + 1)
    edges[-1] = np.inf
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
    
    def neg_tld_log_like(beta_val):
        beta = float(beta_val)
        log_f = np.log(A) - beta * d
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
        
    return neg_tld_log_like, y_k

def run_audit():
    city = "Dallas"
    print("=" * 80)
    print(f"DALLAS ANOMALY AUDIT: PROFILE LIKELIHOOD ANALYSIS")
    print("=" * 80)
    
    nodes, df = process_city_data(city)
    
    d = df["d_clamped"].values
    A = df["A_j_clamped"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values
    
    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)
    
    # True OD-MLE fit
    beta_od = fit_beta_od_mle(df)
    print(f"True OD-MLE beta : {beta_od:.4f}")
    
    # 20-bin TLD MLE fit
    beta_tld20 = fit_beta_tld_mle(df, K=20)
    print(f"20-bin TLD beta  : {beta_tld20:.4f}")
    
    # 3-bin TLD MLE fit using default bounded solver
    beta_tld3_default = fit_beta_tld_mle(df, K=3)
    print(f"3-bin TLD beta (default bounded): {beta_tld3_default:.4f}")
    
    # Let's inspect the likelihood function for 3-bin and 20-bin and OD-MLE
    f_od = lambda b: np.sum(trips * (np.log(A) - b * d)) # simplified or full
    
    # We will compute full multinomial negative log-likelihood for OD-MLE
    def neg_log_like_od(beta_val):
        beta = float(beta_val)
        log_f = np.log(A) - beta * d
        lf_max = np.full(n_o, -np.inf)
        np.maximum.at(lf_max, o_idx_mapped, log_f)
        shifted = np.exp(log_f - lf_max[o_idx_mapped])
        sum_exp = np.zeros(n_o)
        np.add.at(sum_exp, o_idx_mapped, shifted)
        log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
        log_p = log_f - log_denom[o_idx_mapped]
        return -float(np.sum(trips * log_p))

    neg_tld3, y_k3 = get_likelihood_profile_for_k(3, df, d, A, o_idx, trips, unique_o, o_idx_mapped, n_o)
    neg_tld20, y_k20 = get_likelihood_profile_for_k(20, df, d, A, o_idx, trips, unique_o, o_idx_mapped, n_o)
    
    print("\nDistance trip count histogram (3-bins):")
    print(f"  Bin trip counts: {y_k3}")
    
    print("\n--- Likelihood Profile Scan ---")
    betas_to_scan = np.linspace(0.01, 3.0, 60)
    print(f"{'beta':>8s} | {'NegLogLike_OD':>15s} | {'NegLogLike_TLD_20':>18s} | {'NegLogLike_TLD_3':>18s}")
    print("-" * 65)
    for b in betas_to_scan:
        nll_od = neg_log_like_od(b)
        nll_t20 = neg_tld20(b)
        nll_t3 = neg_tld3(b)
        marker = " <--" if abs(b - beta_od) < 0.03 or abs(b - beta_tld3_default) < 0.03 else ""
        print(f"{b:8.4f} | {nll_od:15.2f} | {nll_t20:18.2f} | {nll_t3:18.2f}{marker}")

    # Test multiple initialization points with scipy minimize
    print("\n--- Testing Multi-start Bounded Optimization for 3-bin TLD ---")
    starts = [0.01, 0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 2.5]
    for start in starts:
        # Bounded scalar minimization in interval [0.0001, 3.0]
        # Bounded method doesn't take 'x0', it just searches the bracket.
        # But we can try Brent method with different bracket starts or grid searches.
        # Let's try Brent with bracket
        try:
            res_brent = minimize_scalar(neg_tld3, bracket=(start - 0.05, start, start + 0.05), method="brent")
            val_brent = float(res_brent.x)
            nll_brent = neg_tld3(val_brent)
            print(f"  Brent start around {start:.2f}: converged to beta = {val_brent:.4f} (NLL: {nll_brent:.4f})")
        except Exception as e:
            print(f"  Brent start around {start:.2f} failed: {e}")

    # Let's also check if there is a flat likelihood boundary hit
    print("\n--- Detailed Scan Around OD-MLE beta (0.2259) vs TLD3 beta (1.8541) ---")
    for b in [0.20, 0.2259, 0.25, 0.50, 1.00, 1.50, 1.8541, 1.90, 2.00]:
        print(f"  beta = {b:.4f}: NegLogLike_OD = {neg_log_like_od(b):.2f}, NegLogLike_TLD3 = {neg_tld3(b):.2f}")

if __name__ == "__main__":
    run_audit()
