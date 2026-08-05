"""
Quick Test 19 — Data Requirement Scaling Curve (QT19):
Evaluates performance scaling curve (5, 10, 20, 30, 40 training cities) to determine minimum dataset requirements.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES
from quick_test_4 import build_node_dataset

def run_test_19():
    print("=" * 60)
    print("Running Quick Test 19: Data Requirement Scaling Curve")
    print("=" * 60)

    cities = np.array(ALL_50_CITIES)
    rng = np.random.default_rng(42)
    shuffled = rng.permutation(cities)

    test_cities = list(shuffled[40:]) # Fixed 10 test cities
    train_pool = list(shuffled[:40])

    X_test, y_O_test, y_A_test, _ = build_node_dataset(test_cities)

    train_sizes = [5, 10, 20, 30, 40]
    results = []

    for n_train in train_sizes:
        curr_train_cities = train_pool[:n_train]
        X_tr, y_O_tr, y_A_tr, _ = build_node_dataset(curr_train_cities)

        rf_O = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
        rf_O.fit(X_tr, y_O_tr)
        pred_O = rf_O.predict(X_test)
        r2_O = r2_score(y_O_test, pred_O)

        rf_A = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
        rf_A.fit(X_tr, y_A_tr)
        pred_A = rf_A.predict(X_test)
        r2_A = r2_score(y_A_test, pred_A)

        results.append({
            "n_train_cities": n_train,
            "r2_Oi": r2_O,
            "r2_Aj": r2_A
        })

    res_df = pd.DataFrame(results)

    print("\n" + "=" * 50)
    print("QUICK TEST 19 DATA SCALING RESULTS:")
    print("=" * 50)
    print(res_df.to_string(index=False))
    print("=" * 50)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt19_data_scaling_curve.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7.5, 5))
    plt.plot(res_df["n_train_cities"], res_df["r2_Oi"], "o-", color="#1f77b4", linewidth=2, markersize=8, label=r"$O_i$ Test $R^2$")
    plt.plot(res_df["n_train_cities"], res_df["r2_Aj"], "s--", color="#ff7f0e", linewidth=2, markersize=8, label=r"$A_j$ Test $R^2$")

    plt.ylabel("Test $R^2$ Score (10 Unseen Cities)", fontsize=11)
    plt.xlabel("Number of Training Cities", fontsize=11)
    plt.title("Quick Test 19: Data Scaling Curve vs Number of Training Cities", fontsize=12, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.ylim(0, 0.6)
    plt.legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt19_data_requirement_scaling.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt19_data_requirement_scaling.png'}")
    return res_df

if __name__ == "__main__":
    run_test_19()
