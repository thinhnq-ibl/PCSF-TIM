"""
Quick Test 6 — Feature Importance: Which Urban Features drive Origin (Oi) and Attraction (Aj)?
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES
from quick_test_4 import build_node_dataset

FEATURE_NAMES = [
    "Population",
    "POI Count",
    "Area (km²)",
    "Pop Density",
    "POI Density",
    "Road Density"
]

def run_test_6():
    print("=" * 60)
    print("Running Quick Test 6: Urban Feature Importance Analysis")
    print("=" * 60)

    X, y_O, y_A, _ = build_node_dataset(ALL_50_CITIES)

    rf_O = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_O.fit(X, y_O)
    imp_O = rf_O.feature_importances_

    rf_A = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_A.fit(X, y_A)
    imp_A = rf_A.feature_importances_

    imp_df = pd.DataFrame({
        "feature": FEATURE_NAMES,
        "importance_Oi": imp_O,
        "importance_Aj": imp_A
    }).sort_values(by="importance_Oi", ascending=False)

    print("\n" + "-" * 50)
    print("Quick Test 6 Feature Importances (Random Forest MDI):")
    print(imp_df.to_string(index=False))
    print("-" * 50)

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    imp_df.to_csv(results_dir / "qt6_feature_importance.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    x = np.arange(len(FEATURE_NAMES))
    width = 0.35

    plt.figure(figsize=(9, 5.5))
    plt.bar(x - width/2, imp_df["importance_Oi"], width, label=r"Origin Generation $O_i$", color="#1f77b4", alpha=0.85, edgecolor="black")
    plt.bar(x + width/2, imp_df["importance_Aj"], width, label=r"Destination Attraction $A_j$", color="#ff7f0e", alpha=0.85, edgecolor="black")

    plt.ylabel("Relative Feature Importance (MDI)", fontsize=12)
    plt.xlabel("Urban Feature", fontsize=12)
    plt.title("Quick Test 6: Urban Feature Importance for $O_i$ and $A_j$", fontsize=13, fontweight="bold")
    plt.xticks(x, imp_df["feature"], rotation=15, fontsize=10)
    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.legend(fontsize=11)

    for i in range(len(FEATURE_NAMES)):
        plt.text(x[i] - width/2, imp_df["importance_Oi"].iloc[i] + 0.01, f"{imp_df['importance_Oi'].iloc[i]*100:.1f}%", ha="center", va="bottom", fontsize=8)
        plt.text(x[i] + width/2, imp_df["importance_Aj"].iloc[i] + 0.01, f"{imp_df['importance_Aj'].iloc[i]*100:.1f}%", ha="center", va="bottom", fontsize=8)

    plt.tight_layout()
    plt.savefig(figures_dir / "qt6_feature_importance.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt6_feature_importance.png'}")
    return imp_df

if __name__ == "__main__":
    run_test_6()
