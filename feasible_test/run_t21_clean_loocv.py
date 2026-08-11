"""
T21: 50-City Clean LOOCV End-to-End Stress Test
===============================================
Runs Leave-One-City-Out Cross-Validation on all 50 metropolitan areas
under the completely zero-target-OD pipeline:
  - RF capacity prediction trained on 49 cities.
  - Robust grid-start 3-bin TLD beta MLE inference on the target city (zero leak).
  - Single-constrained gravity flow reconstruction.
  - Downing CPC calculation.
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_tld_mle, predict_gravity_od, calculate_cpc
from quick_test_4 import build_node_dataset

def run_loocv():
    print("=" * 80)
    print("RUNNING T21: 50-CITY CLEAN LOOCV END-TO-END STRESS TEST")
    print("=" * 80)
    
    cities = ALL_50_CITIES
    cpc_results = []
    
    # We will loop over all 50 cities
    for idx, target_city in enumerate(cities):
        # 1. Split training and target
        train_cities = [c for c in cities if c != target_city]
        
        # 2. Build training dataset
        X_train, y_O_train, y_A_train, _ = build_node_dataset(train_cities)
        
        # 3. Train RF models (fast settings to complete in reasonable time)
        rf_O = RandomForestRegressor(n_estimators=30, max_depth=10, random_state=42, n_jobs=-1)
        rf_O.fit(X_train, y_O_train)
        rf_A = RandomForestRegressor(n_estimators=30, max_depth=10, random_state=42, n_jobs=-1)
        rf_A.fit(X_train, y_A_train)
        
        # 4. Predict on target city
        nodes, df = process_city_data(target_city)
        actual = df["trip_count"].values.astype(float)
        N = len(nodes)
        node_ids = nodes["idx"].values
        
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
        
        # 5. Fit beta purely from 3-bin TLD (no leak!)
        beta_est = fit_beta_tld_mle(df, K=3)
        
        # 6. Predict flows and compute CPC
        T_hat = predict_gravity_od(df, beta_est, custom_O=hat_O, custom_A=hat_A, node_ids=node_ids).astype(float)
        if T_hat.sum() > 0:
            T_hat *= (actual.sum() / T_hat.sum())
        cpc_val = calculate_cpc(actual, T_hat)
        cpc_results.append(cpc_val)
        
        print(f"  [{idx+1:02d}/50] {target_city:22s} : CPC = {cpc_val:.4f} (beta = {beta_est:.4f})")

    # Statistical compilation
    cpc_array = np.array(cpc_results)
    mean_cpc = cpc_array.mean()
    median_cpc = np.median(cpc_array)
    p25 = np.percentile(cpc_array, 2.5)
    p975 = np.percentile(cpc_array, 97.5)
    
    # 95% Bootstrap CI of the Mean (N=50)
    n_boot = 1000
    boot_means = [np.mean(np.random.choice(cpc_array, size=len(cpc_array), replace=True)) for _ in range(n_boot)]
    ci_low, ci_high = np.percentile(boot_means, [2.5, 97.5])
    
    print("\n" + "=" * 80)
    print("50-CITY LOOCV OVERALL METRICS (Clean 3-bin beta)")
    print("=" * 80)
    print(f"  Mean CPC                             : {mean_cpc:.4f}")
    print(f"  Median CPC                           : {median_cpc:.4f}")
    print(f"  95% Bootstrap Confidence Interval    : [{ci_low:.4f}, {ci_high:.4f}]")
    print(f"  Marginal Spread (2.5% to 97.5%)      : [{p25:.4f}, {p975:.4f}]")
    
    # Classify failure and success cases
    df_cities = pd.DataFrame({"City": cities, "CPC": cpc_results}).sort_values(by="CPC")
    
    failures = df_cities[df_cities["CPC"] < 0.50]
    successes = df_cities[df_cities["CPC"] > 0.65]
    
    print(f"\nFailure Cases (CPC < 0.50) [N={len(failures)}]:")
    print(failures.to_string(index=False))
    
    print(f"\nSuccess Cases (CPC > 0.65) [N={len(successes)}]:")
    print(successes.to_string(index=False))

    print("\n" + "=" * 80)
    print("LOOCV RUN COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    run_loocv()
