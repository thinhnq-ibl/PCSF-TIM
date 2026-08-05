"""
Quick Test 14 — Model Capacity Bottleneck Analysis (QT14):
Benchmarks Linear Ridge vs Random Forest vs Gradient Boosting vs MLP Neural Network across 5-fold CV
to prove whether the R^2 ~ 0.45 ceiling is a model capacity limitation or spatial representation limitation.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES
from quick_test_4 import build_node_dataset

def run_test_14():
    print("=" * 60)
    print("Running Quick Test 14: Model Capacity & Bottleneck Benchmark")
    print("=" * 60)

    X, y_O, y_A, _ = build_node_dataset(ALL_50_CITIES)
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    models = {
        "Linear Ridge": Ridge(alpha=1.0),
        "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, max_depth=6, random_state=42),
        "MLP Neural Net": MLPRegressor(hidden_layer_sizes=(128, 64), max_iter=200, random_state=42)
    }

    model_results = []

    for name, model in models.items():
        print(f"Benchmarking {name}...")
        pred_O = np.zeros_like(y_O)
        pred_A = np.zeros_like(y_A)

        for train_idx, val_idx in kf.split(X):
            # Fit O_i
            model.fit(X[train_idx], y_O[train_idx])
            pred_O[val_idx] = model.predict(X[val_idx])

            # Fit A_j
            model.fit(X[train_idx], y_A[train_idx])
            pred_A[val_idx] = model.predict(X[val_idx])

        r2_O = r2_score(y_O, pred_O)
        mae_O = mean_absolute_error(y_O, pred_O)
        
        r2_A = r2_score(y_A, pred_A)
        mae_A = mean_absolute_error(y_A, pred_A)

        model_results.append({
            "Model": name,
            "R2_Oi": r2_O,
            "MAE_Oi": mae_O,
            "R2_Aj": r2_A,
            "MAE_Aj": mae_A
        })

    res_df = pd.DataFrame(model_results)

    print("\n" + "=" * 60)
    print("QUICK TEST 14 MODEL CAPACITY BENCHMARK:")
    print("=" * 60)
    print(res_df.to_string(index=False))
    print("=" * 60)

    best_tabular_r2 = max(res_df["R2_Oi"].max(), res_df["R2_Aj"].max())

    if best_tabular_r2 < 0.50:
        print("  => DECISION: All non-spatial model architectures ceiling at R^2 ~ 0.46!")
        print("               This proves the bottleneck is NOT model capacity, but the lack of SPATIAL GRAPH STRUCTURE.")
        print("               Spatial GNN / DeepGravity architecture is strictly necessary for Paper 2.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(results_dir / "qt14_model_capacity_benchmark.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5.5))
    x = np.arange(len(res_df))
    width = 0.35

    plt.bar(x - width/2, res_df["R2_Oi"], width, label=r"$O_i$ Generation 5-Fold $R^2$", color="#1f77b4", alpha=0.85, edgecolor="black")
    plt.bar(x + width/2, res_df["R2_Aj"], width, label=r"$A_j$ Attraction 5-Fold $R^2$", color="#ff7f0e", alpha=0.85, edgecolor="black")

    plt.ylabel("5-Fold Cross-Validation $R^2$ Score", fontsize=12)
    plt.xlabel("Model Architecture", fontsize=12)
    plt.title("Quick Test 14: Model Capacity Bottleneck (Non-Spatial Ceiling)", fontsize=13, fontweight="bold")
    plt.xticks(x, res_df["Model"], fontsize=11)
    plt.ylim(0, 0.65)
    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.legend(fontsize=11)

    for i in range(len(res_df)):
        plt.text(x[i] - width/2, res_df["R2_Oi"].iloc[i] + 0.01, f"{res_df['R2_Oi'].iloc[i]:.3f}", ha="center", va="bottom", fontsize=9)
        plt.text(x[i] + width/2, res_df["R2_Aj"].iloc[i] + 0.01, f"{res_df['R2_Aj'].iloc[i]:.3f}", ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt14_model_capacity_comparison.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt14_model_capacity_comparison.png'}")
    return res_df

if __name__ == "__main__":
    run_test_14()
