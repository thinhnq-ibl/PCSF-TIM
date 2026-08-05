"""
Quick Test 17 — Cross-Domain Transferability (QT17):
Strict 40-train / 10-test city split evaluating zero-shot transfer performance across unseen metropolitan domains.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from scipy.spatial.distance import jensenshannon

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, predict_gravity_od, calculate_cpc
from quick_test_4 import build_node_dataset
from quick_test_10 import compute_tld_distribution

def run_test_17():
    print("=" * 60)
    print("Running Quick Test 17: Cross-Domain Transferability (40 Train / 10 Test)")
    print("=" * 60)

    cities = np.array(ALL_50_CITIES)
    rng = np.random.default_rng(42)
    shuffled = rng.permutation(cities)

    train_cities = list(shuffled[:40])
    test_cities = list(shuffled[40:])

    print(f"Training set: 40 cities | Test set: 10 unseen cities ({', '.join(test_cities[:5])}...)")

    X_train, y_O_train, y_A_train, _ = build_node_dataset(train_cities)
    X_test, y_O_test, y_A_test, test_city_tags = build_node_dataset(test_cities)

    # Fit RF on 40 cities
    rf_O = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_O.fit(X_train, y_O_train)
    pred_O_test = rf_O.predict(X_test)

    rf_A = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_A.fit(X_train, y_A_train)
    pred_A_test = rf_A.predict(X_test)

    r2_O = r2_score(y_O_test, pred_O_test)
    r2_A = r2_score(y_A_test, pred_A_test)

    # Downstream OD reconstruction on 10 unseen test cities
    test_city_results = []

    for city in test_cities:
        nodes, df = process_city_data(city)
        actual = df["trip_count"].values
        beta = fit_beta_od_mle(df)

        # Build test features for this city
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

        # Predicted log O_i and log A_j -> transform to original scale
        hat_O = np.maximum(np.expm1(rf_O.predict(X_city)), 0.0)
        hat_A = np.maximum(np.expm1(rf_A.predict(X_city)), 0.0)

        # Reconstruct OD with predicted O_i, A_j and fitted beta
        T_hat = predict_gravity_od(df, beta, custom_O=hat_O, custom_A=hat_A, node_ids=nodes["idx"].values)
        cpc_val = calculate_cpc(actual, T_hat)

        obs_tld = compute_tld_distribution(df, actual)
        pred_tld = compute_tld_distribution(df, T_hat)
        jsd_val = float(jensenshannon(obs_tld, pred_tld) ** 2)

        test_city_results.append({
            "city": city,
            "cpc": cpc_val,
            "jsd": jsd_val
        })

    res_df = pd.DataFrame(test_city_results)
    mean_test_cpc = float(res_df["cpc"].mean())
    mean_test_jsd = float(res_df["jsd"].mean())

    print("\n" + "=" * 60)
    print("QUICK TEST 17 CROSS-DOMAIN TRANSFER RESULTS (10 UNSEEN CITIES):")
    print("=" * 60)
    print(f"  Unseen Test Node R^2 for O_i  : {r2_O:.4f}")
    print(f"  Unseen Test Node R^2 for A_j  : {r2_A:.4f}")
    print(f"  Mean Downstream CPC on Test  : {mean_test_cpc:.4f}")
    print(f"  Mean Downstream JSD on Test  : {mean_test_jsd:.4f}")
    print("=" * 60)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt17_cross_domain_transfer.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.bar(res_df["city"], res_df["cpc"], color="#1f77b4", alpha=0.85, edgecolor="black")
    plt.axhline(mean_test_cpc, color="red", linestyle="--", linewidth=2, label=f"Mean Test CPC = {mean_test_cpc:.3f}")

    plt.ylabel("Common Part of Commuters (CPC)", fontsize=11)
    plt.xlabel("10 Unseen Test Cities (40 Train / 10 Test Split)", fontsize=11)
    plt.title("Quick Test 17: Zero-Shot Cross-Domain Transfer Performance", fontsize=12, fontweight="bold")
    plt.xticks(rotation=30, fontsize=10)
    plt.ylim(0, 0.9)
    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt17_cross_domain_transfer.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt17_cross_domain_transfer.png'}")
    return res_df, r2_O, r2_A, mean_test_cpc

if __name__ == "__main__":
    run_test_17()
