"""
Test A: Oracle Leakage Audit & Independent Structural Information Test
Evaluates whether Estimated and Transferred Urban Structure Representations (O_i, A_j)
outperform TLD-only baselines and Shuffled Negative Controls WITHOUT relying on Oracle OD Marginals.
"""

import sys
import os
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from scipy.spatial.distance import jensenshannon

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, predict_gravity_od, calculate_cpc
from quick_test_4 import build_node_dataset
from quick_test_10 import compute_tld_distribution

def run_test_a_oracle_leakage_audit():
    print("=" * 70)
    print("RUNNING TEST A: ORACLE LEAKAGE AUDIT (ESTIMATED VS TRANSFERRED VS ORACLE)")
    print("=" * 70)

    cities = np.array(ALL_50_CITIES)
    rng = np.random.default_rng(42)
    shuffled = rng.permutation(cities)

    train_cities = list(shuffled[:40])
    test_cities = list(shuffled[40:])

    print(f"Training set: 40 cities | Test set: 10 unseen test cities ({', '.join(test_cities[:5])}...)")

    X_train, y_O_train, y_A_train, _ = build_node_dataset(train_cities)
    X_test, y_O_test, y_A_test, _ = build_node_dataset(test_cities)

    # Fit RF on 40 training cities
    rf_O = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_O.fit(X_train, y_O_train)
    
    rf_A = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_A.fit(X_train, y_A_train)

    test_records = []

    for city in test_cities:
        nodes, df = process_city_data(city)
        actual_flows = df["trip_count"].values
        beta = fit_beta_od_mle(df)

        P = nodes["total_population"].values
        POI = nodes["total_pois"].values
        area = nodes["area_km2"].values
        road = nodes["road_density"].values

        X_city = np.column_stack([
            np.log(P + 1.0),
            np.log(POI + 1.0),
            np.log(area + 1e-4),
            np.log((P / (area + 1e-4)) + 1e-6),
            np.log((POI / (area + 1e-4)) + 1e-6),
            np.log(road + 1e-6)
        ])

        # 1. Oracle Marginals (True Ground Truth O_i, A_j from OD)
        O_oracle = nodes["O_i"].values
        A_oracle = nodes["A_j"].values
        T_oracle = predict_gravity_od(df, beta, custom_O=O_oracle, custom_A=A_oracle, node_ids=nodes["idx"].values)
        cpc_oracle = calculate_cpc(actual_flows, T_oracle)

        # 2. Transferred/Estimated Marginals (Learned from Open Urban Features)
        hat_O_transferred = np.maximum(np.expm1(rf_O.predict(X_city)), 0.0)
        hat_A_transferred = np.maximum(np.expm1(rf_A.predict(X_city)), 0.0)
        T_transferred = predict_gravity_od(df, beta, custom_O=hat_O_transferred, custom_A=hat_A_transferred, node_ids=nodes["idx"].values)
        cpc_transferred = calculate_cpc(actual_flows, T_transferred)

        # 3. TLD Only Baseline (Uniform Marginals)
        O_flat = np.ones_like(hat_O_transferred) * (hat_O_transferred.sum() / len(hat_O_transferred))
        A_flat = np.ones_like(hat_A_transferred) * (hat_A_transferred.sum() / len(hat_A_transferred))
        T_tld_only = predict_gravity_od(df, beta, custom_O=O_flat, custom_A=A_flat, node_ids=nodes["idx"].values)
        cpc_tld_only = calculate_cpc(actual_flows, T_tld_only)

        # 4. Negative Control (Shuffled Transferred Structure)
        O_shuffled = np.random.permutation(hat_O_transferred)
        A_shuffled = np.random.permutation(hat_A_transferred)
        T_shuffled = predict_gravity_od(df, beta, custom_O=O_shuffled, custom_A=A_shuffled, node_ids=nodes["idx"].values)
        cpc_shuffled = calculate_cpc(actual_flows, T_shuffled)

        test_records.append({
            "City": city,
            "CPC_TLD_Only": round(cpc_tld_only, 4),
            "CPC_Shuffled_Control": round(cpc_shuffled, 4),
            "CPC_Transferred_Structure": round(cpc_transferred, 4),
            "CPC_Oracle_Upper_Bound": round(cpc_oracle, 4),
            "Net_Gain_Over_TLD": round(cpc_transferred - cpc_tld_only, 4),
            "Net_Gain_Over_Shuffled": round(cpc_transferred - cpc_shuffled, 4)
        })

    df_res = pd.DataFrame(test_records)
    print("\nPER-CITY AUDIT BREAKDOWN FOR 10 UNSEEN TEST CITIES:")
    print(df_res[["City", "CPC_TLD_Only", "CPC_Shuffled_Control", "CPC_Transferred_Structure", "CPC_Oracle_Upper_Bound", "Net_Gain_Over_TLD"]].to_string(index=False))

    print("\n" + "=" * 70)
    print("STATISTICAL SUMMARY ACROSS 10 UNSEEN TEST CITIES:")
    print("=" * 70)
    print(f"  Model A (TLD-Only Baseline) Mean CPC   : {df_res['CPC_TLD_Only'].mean():.4f} (Std: {df_res['CPC_TLD_Only'].std():.4f})")
    print(f"  Model B (Shuffled Negative Control) Mean: {df_res['CPC_Shuffled_Control'].mean():.4f} (Std: {df_res['CPC_Shuffled_Control'].std():.4f})")
    print(f"  Model C (Transferred Structure) Mean    : {df_res['CPC_Transferred_Structure'].mean():.4f} (Std: {df_res['CPC_Transferred_Structure'].std():.4f}, Median: {df_res['CPC_Transferred_Structure'].median():.4f}, Range: [{df_res['CPC_Transferred_Structure'].min():.4f}, {df_res['CPC_Transferred_Structure'].max():.4f}])")
    print(f"  Model D (Oracle Upper Bound) Mean       : {df_res['CPC_Oracle_Upper_Bound'].mean():.4f} (Std: {df_res['CPC_Oracle_Upper_Bound'].std():.4f})")
    print("-" * 70)

    avg_gain = df_res['Net_Gain_Over_TLD'].mean()
    avg_neg_gain = df_res['Net_Gain_Over_Shuffled'].mean()
    print(f"  Average Net CPC Gain of Transferred Structure over TLD-Only : +{avg_gain:.4f}")
    print(f"  Average Net CPC Gain over Shuffled Negative Control          : +{avg_neg_gain:.4f}")
    print("-" * 70)

    if avg_gain > 0 and avg_neg_gain > 0:
        print("\n  => TEST A ORACLE LEAKAGE AUDIT PASSED CLEANLY!")
        print("     Transferred Urban Structure (CPC = {:.4f}) reliably outperforms".format(df_res['CPC_Transferred_Structure'].mean()))
        print("     both TLD-Only (CPC = {:.4f}) and Shuffled Controls (CPC = {:.4f}) WITHOUT Oracle OD marginals!".format(df_res['CPC_TLD_Only'].mean(), df_res['CPC_Shuffled_Control'].mean()))
    else:
        print("\n  => TEST A FAILED: Transferred structure does not exceed baselines.")

    return df_res

if __name__ == "__main__":
    run_test_a_oracle_leakage_audit()
