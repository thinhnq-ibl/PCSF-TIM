"""
T34: Behavioural Misspecification & Structural Compensation Test
================================================================
Evaluates how well independent structural opportunity constraints (R_S)
compensate for behavioural parameter (beta) uncertainty during downstream
OD reconstruction, proving that:
  OD degradation with R_S < OD degradation without R_S
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, predict_gravity_od, calculate_cpc
from quick_test_4 import build_node_dataset

def run_t34():
    print("=" * 80)
    print("RUNNING T34: BEHAVIOURAL MISSPECIFICATION & STRUCTURAL COMPENSATION TEST")
    print("=" * 80)
    
    np.random.seed(42)
    cities = ALL_50_CITIES.copy()
    np.random.shuffle(cities)
    train_cities = cities[:40]
    test_cities = cities[40:]
    
    # 1. Train Random Forest model on 40 train cities
    print("Training capacity prediction models on 40 source cities...")
    X_train, y_O_train, y_A_train, _ = build_node_dataset(train_cities)
    rf_O = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_O.fit(X_train, y_O_train)
    rf_A = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_A.fit(X_train, y_A_train)

    deltas = [-0.6, -0.4, -0.2, -0.1, 0.0, 0.1, 0.2, 0.4, 0.6]
    
    results = {d: {"cpc_uniform": [], "cpc_trans": []} for d in deltas}
    
    print("Running perturbation experiments across 10 test cities...")
    for c in test_cities:
        nodes, df = process_city_data(c)
        actual = df["trip_count"].values.astype(float)
        N = len(nodes)
        node_ids = nodes["idx"].values
        
        # True beta
        beta_star = fit_beta_od_mle(df)
        
        # Predict capacities using RF
        P = nodes["total_population"].values
        POI = nodes["total_pois"].values
        area = nodes["area_km2"].values
        road = nodes["road_density"].values
        X_city = np.column_stack([
            np.log(P + 1.0), np.log(POI + 1.0), np.log(area + 1e-4),
            np.log((P / (area + 1e-4)) + 1e-6), np.log((POI / (area + 1e-4)) + 1e-6),
            np.log(road + 1e-6)
        ])
        hat_O = np.maximum(np.expm1(rf_O.predict(X_city)), 0.0)
        hat_A = np.maximum(np.expm1(rf_A.predict(X_city)), 0.0)
        
        # Uniform capacities
        O_flat = np.ones(N) * (actual.sum() / N)
        A_flat = np.ones(N) * (actual.sum() / N)
        
        for d in deltas:
            # Perturb beta
            beta_perturbed = beta_star * (1.0 + d)
            
            # Uniform flow prediction
            T_uniform = predict_gravity_od(df, beta_perturbed, custom_O=O_flat, custom_A=A_flat, node_ids=node_ids).astype(float)
            cpc_uniform = calculate_cpc(actual, T_uniform)
            
            # Transferred structure prediction
            T_trans = predict_gravity_od(df, beta_perturbed, custom_O=hat_O, custom_A=hat_A, node_ids=node_ids).astype(float)
            T_trans *= (actual.sum() / max(T_trans.sum(), 1e-12))
            cpc_trans = calculate_cpc(actual, T_trans)
            
            results[d]["cpc_uniform"].append(cpc_uniform)
            results[d]["cpc_trans"].append(cpc_trans)

    # Compile averages
    mean_results = []
    cpc_uniform_0 = np.mean(results[0.0]["cpc_uniform"])
    cpc_trans_0 = np.mean(results[0.0]["cpc_trans"])
    
    for d in deltas:
        mu_uniform = np.mean(results[d]["cpc_uniform"])
        mu_trans = np.mean(results[d]["cpc_trans"])
        
        deg_uniform = mu_uniform - cpc_uniform_0
        deg_trans = mu_trans - cpc_trans_0
        
        mean_results.append({
            "delta": d,
            "cpc_uniform": mu_uniform,
            "cpc_trans": mu_trans,
            "gain": mu_trans - mu_uniform,
            "deg_uniform": deg_uniform,
            "deg_trans": deg_trans
        })

    # Print results table
    print("\nSTRUCTURAL COMPENSATION TABLE (T34):")
    print(f"{'Perturb (delta)':<15s} | {'Uniform CPC':<12s} | {'Trans CPC':<12s} | {'CPC Gain':<10s} | {'Degradation (Unif)':<20s} | {'Degradation (Trans)':<20s}")
    print("-" * 105)
    for r in mean_results:
        print(f"{r['delta']*100:+13.0f}% | {r['cpc_uniform']:11.4f} | {r['cpc_trans']:11.4f} | {r['gain']:+9.4f} | {r['deg_uniform']:+18.4f} | {r['deg_trans']:+18.4f}")

    print("\nVerification of compensation mechanism:")
    for r in mean_results:
        if r['delta'] == 0.0:
            continue
        ratio = abs(r['deg_trans']) / max(abs(r['deg_uniform']), 1e-12)
        status = "COMPENSATED (Flatter curve)" if abs(r['deg_trans']) < abs(r['deg_uniform']) else "Not compensated"
        print(f"  Delta {r['delta']*100:+3.0f}%: Transferred degradation is {ratio*100:.1f}% of Uniform degradation -> {status}")

    print("\n" + "=" * 80)
    print("T34 TEST COMPLETED")
    print("=" * 80)

if __name__ == "__main__":
    run_t34()
