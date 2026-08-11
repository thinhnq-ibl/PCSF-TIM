"""
CRITICAL AUDIT FIX: beta Leakage Remediation
==========================================
Re-runs T20 (Leakage Audit) and T32 (Structural Ablation) using fit_beta_tld_mle(df, K=3)
instead of fit_beta_od_mle(df), to ensure zero target-OD information leaks into beta.

Also renames "TLD-Only" baseline to "Uniform Spatial Baseline" for accuracy.

Compares results side-by-side with original oracle-beta results.
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, fit_beta_tld_mle, predict_gravity_od, calculate_cpc
from quick_test_4 import build_node_dataset
from sklearn.ensemble import RandomForestRegressor

np.random.seed(42)
cities = ALL_50_CITIES.copy()
np.random.shuffle(cities)
train_cities = cities[:40]
test_cities = cities[40:]

print("=" * 80)
print("CRITICAL AUDIT FIX: BETA LEAKAGE REMEDIATION")
print("=" * 80)
print(f"Train Cities: {len(train_cities)}, Test Cities: {len(test_cities)}")
print(f"Test Cities: {test_cities}")
print()

# =============================================================================
# PART 1: Compare beta_od vs beta_tld for each test city
# =============================================================================
print("-" * 80)
print("PART 1: beta COMPARISON (OD-MLE vs TLD-MLE K=3) FOR TEST CITIES")
print("-" * 80)

beta_comparisons = []
for c in test_cities:
    nodes, df = process_city_data(c)
    beta_od = fit_beta_od_mle(df)
    beta_tld_3 = fit_beta_tld_mle(df, K=3)
    beta_tld_20 = fit_beta_tld_mle(df, K=20)
    pct_err_3 = abs(beta_tld_3 - beta_od) / beta_od * 100.0
    pct_err_20 = abs(beta_tld_20 - beta_od) / beta_od * 100.0
    beta_comparisons.append({
        "city": c, "beta_od": beta_od,
        "beta_tld_3": beta_tld_3, "pct_err_3": pct_err_3,
        "beta_tld_20": beta_tld_20, "pct_err_20": pct_err_20
    })
    print(f"  {c:30s}  beta_od={beta_od:.4f}  beta_tld3={beta_tld_3:.4f} ({pct_err_3:6.2f}%)  beta_tld20={beta_tld_20:.4f} ({pct_err_20:6.2f}%)")

mean_err_3 = np.mean([b["pct_err_3"] for b in beta_comparisons])
mean_err_20 = np.mean([b["pct_err_20"] for b in beta_comparisons])
print(f"\n  Mean beta Error (3-bin TLD vs OD): {mean_err_3:.2f}%")
print(f"  Mean beta Error (20-bin TLD vs OD): {mean_err_20:.2f}%")

# =============================================================================
# PART 2: T20 LEAKAGE AUDIT with TLD-derived beta (K=3 and K=20)
# =============================================================================
print("\n" + "=" * 80)
print("PART 2: T20 RE-RUN WITH TLD-DERIVED beta (Zero Target-OD Leakage)")
print("=" * 80)

# Train RF models for structural prediction
X_train, y_O_train, y_A_train, _ = build_node_dataset(train_cities)
rf_O = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
rf_O.fit(X_train, y_O_train)
rf_A = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
rf_A.fit(X_train, y_A_train)

results_oracle_beta = []
results_tld3_beta = []
results_tld20_beta = []

for c in test_cities:
    nodes, df = process_city_data(c)
    actual = df["trip_count"].values.astype(float)
    N = len(nodes)
    node_ids = nodes["idx"].values

    beta_od = fit_beta_od_mle(df)
    beta_tld3 = fit_beta_tld_mle(df, K=3)
    beta_tld20 = fit_beta_tld_mle(df, K=20)

    # Build features for structural prediction
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

    # Uniform baseline
    O_flat = np.ones(N) * (actual.sum() / N)
    A_flat = np.ones(N) * (actual.sum() / N)

    for beta_val, beta_label, result_list in [
        (beta_od, "oracle_beta", results_oracle_beta),
        (beta_tld3, "tld3_beta", results_tld3_beta),
        (beta_tld20, "tld20_beta", results_tld20_beta),
    ]:
        # Uniform Spatial Baseline
        T_uniform = predict_gravity_od(df, beta_val, custom_O=O_flat, custom_A=A_flat, node_ids=node_ids).astype(float)
        cpc_uniform = calculate_cpc(actual, T_uniform)

        # Transferred Structure
        T_trans = predict_gravity_od(df, beta_val, custom_O=hat_O, custom_A=hat_A, node_ids=node_ids).astype(float)
        T_trans *= (actual.sum() / max(T_trans.sum(), 1e-12))
        cpc_trans = calculate_cpc(actual, T_trans)

        # Oracle Ceiling
        T_oracle = predict_gravity_od(df, beta_val, node_ids=node_ids).astype(float)
        cpc_oracle = calculate_cpc(actual, T_oracle)

        result_list.append({
            "city": c, "cpc_uniform": cpc_uniform, "cpc_trans": cpc_trans, "cpc_oracle": cpc_oracle,
            "gain_trans_vs_uniform": cpc_trans - cpc_uniform
        })

# Print comparison table
print(f"\n{'':30s} | {'ORACLE beta (leaked)':>20s} | {'TLD 3-bin beta (clean)':>20s} | {'TLD 20-bin beta (clean)':>20s}")
print(f"{'':30s} | {'Uniform->Trans->Oracle':>20s} | {'Uniform->Trans->Oracle':>20s} | {'Uniform->Trans->Oracle':>20s}")
print("-" * 120)
for i, c in enumerate(test_cities):
    ro = results_oracle_beta[i]
    r3 = results_tld3_beta[i]
    r20 = results_tld20_beta[i]
    print(f"  {c:28s} | {ro['cpc_uniform']:.4f}->{ro['cpc_trans']:.4f}->{ro['cpc_oracle']:.4f} | "
          f"{r3['cpc_uniform']:.4f}->{r3['cpc_trans']:.4f}->{r3['cpc_oracle']:.4f} | "
          f"{r20['cpc_uniform']:.4f}->{r20['cpc_trans']:.4f}->{r20['cpc_oracle']:.4f}")

# Summary statistics
for label, rlist in [("ORACLE beta (leaked)", results_oracle_beta), ("TLD 3-bin beta (clean)", results_tld3_beta), ("TLD 20-bin beta (clean)", results_tld20_beta)]:
    mean_uniform = np.mean([r["cpc_uniform"] for r in rlist])
    mean_trans = np.mean([r["cpc_trans"] for r in rlist])
    mean_oracle = np.mean([r["cpc_oracle"] for r in rlist])
    mean_gain = np.mean([r["gain_trans_vs_uniform"] for r in rlist])
    print(f"\n  {label:25s}: Uniform={mean_uniform:.4f}  Transferred={mean_trans:.4f}  Oracle={mean_oracle:.4f}  Gain={mean_gain:+.4f}")

# =============================================================================
# PART 3: T32 STRUCTURAL ABLATION with TLD-derived beta (K=3)
# =============================================================================
print("\n" + "=" * 80)
print("PART 3: T32 STRUCTURAL ABLATION RE-RUN WITH TLD 3-BIN beta")
print("=" * 80)

feature_configs = [
    ("TLD Only (Uniform)", None),
    ("TLD + Pop", ["pop"]),
    ("TLD + POI", ["poi"]),
    ("TLD + Pop+POI", ["pop", "poi"]),
    ("TLD + Full Structure", ["pop", "poi", "area", "road"]),
]

def build_ablation_features(nodes, feature_set):
    P = nodes["total_population"].values
    POI = nodes["total_pois"].values
    area = nodes["area_km2"].values
    road = nodes["road_density"].values
    
    features = []
    if feature_set is None:
        return None
    if "pop" in feature_set:
        features.extend([np.log(P + 1.0), np.log((P / (area + 1e-4)) + 1e-6)])
    if "poi" in feature_set:
        features.extend([np.log(POI + 1.0), np.log((POI / (area + 1e-4)) + 1e-6)])
    if "area" in feature_set:
        features.append(np.log(area + 1e-4))
    if "road" in feature_set:
        features.append(np.log(road + 1e-6))
    return np.column_stack(features) if features else None

for config_name, feat_set in feature_configs:
    if feat_set is None:
        # Uniform baseline
        cpc_list_oracle = []
        cpc_list_tld3 = []
        for c in test_cities:
            nodes, df = process_city_data(c)
            actual = df["trip_count"].values.astype(float)
            N = len(nodes)
            O_flat = np.ones(N) * (actual.sum() / N)
            A_flat = np.ones(N) * (actual.sum() / N)
            
            beta_od = fit_beta_od_mle(df)
            beta_tld3 = fit_beta_tld_mle(df, K=3)
            
            T_o = predict_gravity_od(df, beta_od, custom_O=O_flat, custom_A=A_flat, node_ids=nodes["idx"].values).astype(float)
            T_t = predict_gravity_od(df, beta_tld3, custom_O=O_flat, custom_A=A_flat, node_ids=nodes["idx"].values).astype(float)
            cpc_list_oracle.append(calculate_cpc(actual, T_o))
            cpc_list_tld3.append(calculate_cpc(actual, T_t))
        
        print(f"  {config_name:30s}  oracle_beta CPC={np.mean(cpc_list_oracle):.4f}  tld3_beta CPC={np.mean(cpc_list_tld3):.4f}")
    else:
        # Train ablation RF models
        X_abl_train_all = []
        y_O_abl_train = []
        y_A_abl_train = []
        for c in train_cities:
            nodes, df = process_city_data(c)
            X_abl = build_ablation_features(nodes, feat_set)
            if X_abl is not None:
                X_abl_train_all.append(X_abl)
                y_O_abl_train.append(np.log1p(nodes["O_i"].values))
                y_A_abl_train.append(np.log1p(nodes["A_j"].values))
        
        X_abl_train_all = np.vstack(X_abl_train_all)
        y_O_abl_train = np.concatenate(y_O_abl_train)
        y_A_abl_train = np.concatenate(y_A_abl_train)
        
        rf_O_abl = RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
        rf_O_abl.fit(X_abl_train_all, y_O_abl_train)
        rf_A_abl = RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
        rf_A_abl.fit(X_abl_train_all, y_A_abl_train)
        
        cpc_list_oracle = []
        cpc_list_tld3 = []
        for c in test_cities:
            nodes, df = process_city_data(c)
            actual = df["trip_count"].values.astype(float)
            X_abl_city = build_ablation_features(nodes, feat_set)
            hat_O = np.maximum(np.expm1(rf_O_abl.predict(X_abl_city)), 0.0)
            hat_A = np.maximum(np.expm1(rf_A_abl.predict(X_abl_city)), 0.0)
            
            beta_od = fit_beta_od_mle(df)
            beta_tld3 = fit_beta_tld_mle(df, K=3)
            
            T_o = predict_gravity_od(df, beta_od, custom_O=hat_O, custom_A=hat_A, node_ids=nodes["idx"].values).astype(float)
            T_o *= (actual.sum() / max(T_o.sum(), 1e-12))
            T_t = predict_gravity_od(df, beta_tld3, custom_O=hat_O, custom_A=hat_A, node_ids=nodes["idx"].values).astype(float)
            T_t *= (actual.sum() / max(T_t.sum(), 1e-12))
            
            cpc_list_oracle.append(calculate_cpc(actual, T_o))
            cpc_list_tld3.append(calculate_cpc(actual, T_t))
        
        print(f"  {config_name:30s}  oracle_beta CPC={np.mean(cpc_list_oracle):.4f}  tld3_beta CPC={np.mean(cpc_list_tld3):.4f}")

print("\n" + "=" * 80)
print("beta LEAKAGE REMEDIATION COMPLETE")
print("=" * 80)
