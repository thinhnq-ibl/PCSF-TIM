"""
Dallas Anomaly Fix: Bounded Multi-start Solver
==============================================
Tests if a robust multi-start solver for fit_beta_tld_mle
recovers the global minimum of the likelihood function for Dallas
and other cities, eliminating the optimization failure.
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize_scalar

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import process_city_data, fit_beta_od_mle, ALL_50_CITIES

def fit_beta_tld_mle_robust(df: pd.DataFrame, K: int = 3, grid_size: int = 15):
    """Fit beta parameter robustly using a grid-start bounded minimizer."""
    d = df["d_clamped"].values
    A = df["A_j_clamped"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values

    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)

    d_max = d.max()
    edges = np.linspace(0, d_max, K + 1)
    edges[-1] = np.inf
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)

    y_k = np.bincount(bin_idx, weights=trips, minlength=K).astype(float)
    tot_trips = y_k.sum()
    if tot_trips == 0:
        return 0.1

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

    # 1. Grid search to find a good starting neighborhood
    grid = np.linspace(0.001, 3.0, grid_size)
    grid_likes = [neg_tld_log_like(b) for b in grid]
    best_idx = np.argmin(grid_likes)
    best_b = grid[best_idx]
    
    # 2. Define sub-bounds around the best grid point
    # We bracket the optimizer to the neighboring grid points to avoid flat regions
    low_b = grid[max(0, best_idx - 1)]
    high_b = grid[min(grid_size - 1, best_idx + 1)]
    
    res = minimize_scalar(neg_tld_log_like, bounds=(low_b, high_b), method="bounded")
    return float(res.x)

def run_test():
    test_cities = ['Dallas', 'Los_Angeles', 'Jacksonville', 'Wichita', 'Las_Vegas', 'Chicago', 'San_Jose', 'Fort_Worth', 'Minneapolis', 'Sacramento']
    print("=" * 80)
    print("TESTING ROBUST MULTI-START TLD-MLE SOLVER ON TEST CITIES")
    print("=" * 80)
    
    for c in test_cities:
        nodes, df = process_city_data(c)
        beta_od = fit_beta_od_mle(df)
        
        # Original solver
        from utils_test import fit_beta_tld_mle
        beta_orig = fit_beta_tld_mle(df, K=3)
        err_orig = abs(beta_orig - beta_od) / beta_od * 100.0
        
        # Robust solver
        beta_robust = fit_beta_tld_mle_robust(df, K=3)
        err_robust = abs(beta_robust - beta_od) / beta_od * 100.0
        
        print(f"  {c:20s} | beta_od={beta_od:.4f} | beta_orig={beta_orig:.4f} ({err_orig:6.2f}%) | beta_robust={beta_robust:.4f} ({err_robust:6.2f}%)")

if __name__ == "__main__":
    run_test()
