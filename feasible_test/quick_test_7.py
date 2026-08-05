"""
Quick Test 7 — Cross-City Transferability: Can Urban Feature models generalize to unseen cities (45 train / 5 test)?
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data
from quick_test_4 import build_node_dataset

def run_test_7():
    print("=" * 60)
    print("Running Quick Test 7: Zero-Shot Cross-City Generalization (45 Train / 5 Test)")
    print("=" * 60)

    # 10-fold City-level Cross Validation (5 cities held out per fold)
    cities = np.array(ALL_50_CITIES)
    rng = np.random.default_rng(42)
    shuffled_cities = rng.permutation(cities)

    n_folds = 10
    cities_per_fold = len(cities) // n_folds

    fold_results = []

    for fold in range(n_folds):
        test_cities = shuffled_cities[fold * cities_per_fold : (fold + 1) * cities_per_fold]
        train_cities = [c for c in cities if c not in test_cities]

        X_train, y_O_train, y_A_train, _ = build_node_dataset(train_cities)
        X_test, y_O_test, y_A_test, test_indices = build_node_dataset(test_cities)

        # Fit model on 45 training cities
        rf_O = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
        rf_O.fit(X_train, y_O_train)
        pred_O_test = rf_O.predict(X_test)

        rf_A = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
        rf_A.fit(X_train, y_A_train)
        pred_A_test = rf_A.predict(X_test)

        r2_O = r2_score(y_O_test, pred_O_test)
        r2_A = r2_score(y_A_test, pred_A_test)

        fold_results.append({
            "fold": fold + 1,
            "test_cities": ", ".join(test_cities),
            "r2_Oi": r2_O,
            "r2_Aj": r2_A
        })

    res_df = pd.DataFrame(fold_results)

    avg_r2_O = res_df["r2_Oi"].mean()
    avg_r2_A = res_df["r2_Aj"].mean()

    print("\n" + "-" * 50)
    print("Quick Test 7 Zero-Shot Cross-City Transferability Results:")
    print(res_df[["fold", "r2_Oi", "r2_Aj"]].to_string(index=False))
    print("-" * 50)
    print(f"  Mean Test R^2 for O_i across unseen cities : {avg_r2_O:.4f}")
    print(f"  Mean Test R^2 for A_j across unseen cities : {avg_r2_A:.4f}")
    print("-" * 50)

    if avg_r2_O > 0.80 and avg_r2_A > 0.70:
        print("  => DECISION: Strong zero-shot transferability! Urban features generalize across cities.")
    else:
        print("  => DECISION: Transferability is moderate; city-specific calibration recommended.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt7_cross_city_transfer.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    x = np.arange(n_folds) + 1
    width = 0.35

    plt.bar(x - width/2, res_df["r2_Oi"], width, label=r"Test $R^2$ ($O_i$ Generation)", color="#1f77b4", alpha=0.85, edgecolor="black")
    plt.bar(x + width/2, res_df["r2_Aj"], width, label=r"Test $R^2$ ($A_j$ Attraction)", color="#ff7f0e", alpha=0.85, edgecolor="black")

    plt.axhline(avg_r2_O, color="#1f77b4", linestyle="--", linewidth=1.5, label=f"Mean $O_i$ $R^2 = {avg_r2_O:.3f}$")
    plt.axhline(avg_r2_A, color="#ff7f0e", linestyle="--", linewidth=1.5, label=f"Mean $A_j$ $R^2 = {avg_r2_A:.3f}$")

    plt.ylabel("Out-of-City Test $R^2$ Score", fontsize=12)
    plt.xlabel("Validation Fold (5 Unseen Cities per Fold)", fontsize=12)
    plt.title("Quick Test 7: Zero-Shot Cross-City Generalization", fontsize=13, fontweight="bold")
    plt.xticks(x)
    plt.ylim(0, 1.05)
    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.legend(fontsize=10, loc="lower right")

    plt.tight_layout()
    plt.savefig(figures_dir / "qt7_cross_city_transfer.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt7_cross_city_transfer.png'}")
    return res_df, avg_r2_O, avg_r2_A

if __name__ == "__main__":
    run_test_7()
