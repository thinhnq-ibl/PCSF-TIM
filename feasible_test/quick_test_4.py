"""
Quick Test 4 — Paper 2 Feasibility: Can Random Forest predict Origin Generation O_i from Urban Features?
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score, mean_absolute_error

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data

def build_node_dataset(cities):
    """Aggregate node features and targets across specified cities."""
    all_X = []
    all_y_O = []
    all_y_A = []
    city_indices = []

    for city in cities:
        nodes, _ = process_city_data(city)
        P = nodes["total_population"].values
        POI = nodes["total_pois"].values
        area = nodes["area_km2"].values
        road = nodes["road_density"].values
        
        O = nodes["O_i"].values
        A = nodes["A_j"].values

        # Log transform features
        X = np.column_stack([
            np.log(P + 1.0),
            np.log(POI + 1.0),
            np.log(area + 1e-4),
            np.log((P / (area + 1e-4)) + 1e-6),
            np.log((POI / (area + 1e-4)) + 1e-6),
            np.log(road + 1e-6)
        ])
        
        y_O = np.log(O + 1.0)
        y_A = np.log(A + 1.0)

        all_X.append(X)
        all_y_O.append(y_O)
        all_y_A.append(y_A)
        city_indices.extend([city] * len(nodes))

    return np.vstack(all_X), np.concatenate(all_y_O), np.concatenate(all_y_A), city_indices

def run_test_4():
    print("=" * 60)
    print("Running Quick Test 4: Predicting Origin Generation O_i with Random Forest")
    print("=" * 60)

    X, y_O, _, city_indices = build_node_dataset(ALL_50_CITIES)
    print(f"Total dataset size: {len(y_O)} zones across 50 cities")

    rf = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    
    # 5-Fold Cross-Validation
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    y_pred_cv = np.zeros_like(y_O)
    
    for fold, (train_idx, val_idx) in enumerate(kf.split(X), 1):
        rf.fit(X[train_idx], y_O[train_idx])
        y_pred_cv[val_idx] = rf.predict(X[val_idx])

    r2_cv = r2_score(y_O, y_pred_cv)
    mae_cv = mean_absolute_error(y_O, y_pred_cv)

    # In-sample fit
    rf.fit(X, y_O)
    y_pred_in = rf.predict(X)
    r2_in = r2_score(y_O, y_pred_in)

    print("\n" + "-" * 40)
    print("Quick Test 4 O_i Prediction Performance:")
    print(f"  5-Fold CV R^2 Score : {r2_cv:.4f}")
    print(f"  5-Fold CV MAE       : {mae_cv:.4f}")
    print(f"  In-Sample R^2 Score : {r2_in:.4f}")
    print("-" * 40)

    if r2_cv > 0.90:
        print("  => DECISION: R^2 > 0.90 -> Paper 2 is EXTREMELY FEASIBLE for O_i prediction!")
    elif r2_cv > 0.70:
        print("  => DECISION: R^2 > 0.70 -> Good baseline performance; NN can optimize further.")
    else:
        print("  => DECISION: R^2 < 0.40 -> Feature set needs revision.")

    # Save results
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    res_df = pd.DataFrame({"city": city_indices, "y_true_O": y_O, "y_pred_O": y_pred_cv})
    res_df.to_csv(results_dir / "qt4_predict_Oi_results.csv", index=False)

    # Plot
    figures_dir = FEASIBLE_DIR / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7, 6))
    plt.scatter(y_O, y_pred_cv, alpha=0.3, color="#1f77b4", s=15)
    lim_min = min(y_O.min(), y_pred_cv.min())
    lim_max = max(y_O.max(), y_pred_cv.max())
    plt.plot([lim_min, lim_max], [lim_min, lim_max], "r--", linewidth=2, label="Identity Line ($y=x$)")

    plt.xlabel(r"Observed Origin Generation $\log(O_i + 1)$", fontsize=12)
    plt.ylabel(r"RF Predicted $\log(\hat{O}_i + 1)$ (5-Fold CV)", fontsize=12)
    plt.title(f"Quick Test 4: Paper 2 Feasibility — $O_i$ Prediction\n5-Fold CV $R^2 = {r2_cv:.4f}$", fontsize=13, fontweight="bold")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(fontsize=11)

    plt.text(0.05, 0.85, f"CV R² = {r2_cv:.4f}\nCV MAE = {mae_cv:.4f}\nN = {len(y_O)} zones",
             transform=plt.gca().transAxes, fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9))

    plt.tight_layout()
    plt.savefig(figures_dir / "qt4_predict_Oi.png", dpi=300)
    plt.close()

    print(f"Saved plot to {figures_dir / 'qt4_predict_Oi.png'}")
    return r2_cv

if __name__ == "__main__":
    run_test_4()
