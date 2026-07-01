"""
Zero-Shot DeepGravity City Transfer (38-Feature Version)
=========================================================

Trains a single DeepGravity MLP on the pooled OD pairs of 10 source cities using
the FULL 38-feature set (6 base + 16 POI counts + 16 POI densities), and transfers
it zero-shot to 40 held-out cities under:

1. Oracle Outflow: using true O_i as feature
2. Survey-Free E2E: using GBDT-predicted O_hat (23 SHAP features) as feature

**Design Rationale**:
- DeepGravity uses 38 features: Neural networks benefit from full feature space
  to learn complex non-linear interactions between urban characteristics
- GBDT uses 23 SHAP features: Tree-based models prefer stable, transferable
  features that reduce overfitting to city-specific artifacts

Author: PSF-CTF Team
Date: 2026-06-06
"""

import os
import sys
import time
import logging
import numpy as np
import pandas as pd
import torch
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List, Dict

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path)
sys.path.insert(0, os.path.dirname(dir_path))

from conference_benchmark import make_split, TEST_FRAC, SPLIT_SEED, cpc, apply_origin_normalization
from utils import load_city, build_pairs_dataframe
from run_survey_free_25to25_redesign import (
    CITIES_50, SOURCE_CITIES, HELDOUT_CITIES,
    load_road_density, proposed_predict, national_decay
)
from feature_builders import (
    build_zone_features_37,
    build_deep_gravity_pair_features_37,
    build_gbdt_outflow_features_23,
    SHAP_FEATURES_23
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

EPS = 1e-6

def fit_mlp_global(X_train: np.ndarray, y_train: np.ndarray, hidden: int = 128, epochs: int = 150, lr: float = 1e-3, seed: int = 0) -> torch.nn.Module:
    """Train DeepGravity MLP on global pooled training data."""
    torch.manual_seed(seed)
    np.random.seed(seed)
    
    X_train_t = torch.from_numpy(X_train).float()
    y_train_t = torch.from_numpy(y_train).float()
    
    in_dim = X_train.shape[1]
    model = torch.nn.Sequential(
        torch.nn.Linear(in_dim, hidden), torch.nn.ReLU(),
        torch.nn.Linear(hidden, hidden), torch.nn.ReLU(),
        torch.nn.Linear(hidden, 1)
    )
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    
    n_tr = len(X_train)
    batch = min(8192, n_tr)
    
    for ep in range(epochs):
        perm = torch.randperm(n_tr)
        for start in range(0, n_tr, batch):
            ix = perm[start:start + batch]
            pred = model(X_train_t[ix]).squeeze(-1)
            loss = ((pred - y_train_t[ix]) ** 2).mean()
            opt.zero_grad()
            loss.backward()
            opt.step()
            
    model.eval()
    return model

def main():
    t0 = time.time()
    logging.info("Loading 50 cities...")
    road_vals = []
    city_cache = {}
    for c in CITIES_50:
        city_data = load_city(c)
        df = build_pairs_dataframe(city_data, attr_mode="poi_pop_avg", min_distance=0.1, adaptive_self=True)
        tr, te = make_split(df, SPLIT_SEED, TEST_FRAC)
        rm = load_road_density(c)
        road_vals.extend(rm.values())
        city_cache[c] = {
            "city_data": city_data,
            "df": df,
            "train_mask": tr,
            "test_mask": te,
            "road_map": rm
        }
    road_impute = float(np.median(road_vals)) if road_vals else 1e-4
    logging.info(f"Loaded 50 cities in {time.time() - t0:.1f}s.")
    
    # Get national decay parameters
    alpha_nat, beta_nat = national_decay(city_cache)
    
    # ── Train GBDT Outflow on Source Cities (23 SHAP Features) ───────────────
    logging.info("Training GBDT outflow model on source cities (23 SHAP features)...")
    Xs_gbdt, ys_gbdt = [], []
    for c in SOURCE_CITIES:
        cc = city_cache[c]
        X, logO, _ = build_gbdt_outflow_features_23(cc["city_data"], cc["road_map"], road_impute)
        Xs_gbdt.append(X)
        ys_gbdt.append(logO)
    Xs_gbdt = np.vstack(Xs_gbdt)
    ys_gbdt = np.concatenate(ys_gbdt)
    scaler_gbdt = StandardScaler().fit(Xs_gbdt)
    
    gbdt_model = HistGradientBoostingRegressor(
        max_depth=2, learning_rate=0.05, max_iter=200, l2_regularization=5.0, random_state=42
    )
    gbdt_model.fit(scaler_gbdt.transform(Xs_gbdt), ys_gbdt)
    logging.info(f"GBDT trained: Input shape {Xs_gbdt.shape} (23 SHAP features)")
    
    # ── Prepare Pooled DeepGravity Training Data (Source Cities, 38 Features) ──
    logging.info("Building pooled DeepGravity training data (38 features)...")
    X_dg_tr_list = []
    y_dg_tr_list = []
    
    for c in SOURCE_CITIES:
        cc = city_cache[c]
        df = cc["df"]
        tr = cc["train_mask"]
        
        # Build 37-feature zone features
        nodes_37, feat_names = build_zone_features_37(cc["city_data"], cc["road_map"], road_impute)
        
        # Extract OD pair features using true O_i
        O_true = df["O_i"].values
        A_j = df["A_j"].values
        d = df["d_clamped"].values
        
        feat_dg = build_deep_gravity_pair_features_37(df, nodes_37, O_true, A_j, d)
        
        # Filter train mask
        X_dg_tr_list.append(feat_dg[tr])
        y_dg_tr_list.append(np.log1p(df["trip_count"].values[tr]))
        
    X_dg_train = np.vstack(X_dg_tr_list)
    y_dg_train = np.concatenate(y_dg_tr_list)
    
    logging.info(f"DeepGravity training data: {X_dg_train.shape}")
    
    # Downsample to 150,000 samples for fast training
    if len(X_dg_train) > 150000:
        logging.info(f"Downsampling from {len(X_dg_train)} to 150,000 samples...")
        np.random.seed(42)
        idx = np.random.choice(len(X_dg_train), 150000, replace=False)
        X_dg_train = X_dg_train[idx]
        y_dg_train = y_dg_train[idx]
    
    scaler_dg = StandardScaler().fit(X_dg_train)
    X_dg_train_scaled = scaler_dg.transform(X_dg_train)
    
    logging.info(f"Training DeepGravity MLP. Shape: {X_dg_train_scaled.shape}")
    dg_model = fit_mlp_global(X_dg_train_scaled, y_dg_train, hidden=256, epochs=50, lr=1e-3, seed=0)
    
    # ── Evaluate Zero-Shot DeepGravity on 25 Held-out Cities ──────────────────
    logging.info("Evaluating Zero-Shot DeepGravity on 25 held-out cities...")
    results = []
    
    for c in HELDOUT_CITIES:
        cc = city_cache[c]
        df = cc["df"]
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        # 1. Predict GBDT Outflow (11 SHAP features)
        X_gbdt, logO_true, zones = build_gbdt_outflow_features_23(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = gbdt_model.predict(scaler_gbdt.transform(X_gbdt))
        O_hat_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        O_pred_vec = df["o_idx"].map(O_hat_map).fillna(1.0).values
        
        # 2. Get 37-feature zone features
        nodes_37, _ = build_zone_features_37(cc["city_data"], cc["road_map"], road_impute)
        
        # 3. Predict DeepGravity (Oracle O_i)
        O_true = df["O_i"].values
        A_j = df["A_j"].values
        d = df["d_clamped"].values
        feat_dg_oracle = build_deep_gravity_pair_features_37(df, nodes_37, O_true, A_j, d)
        feat_dg_oracle_scaled = scaler_dg.transform(feat_dg_oracle)
        with torch.no_grad():
            pred_oracle_t = dg_model(torch.from_numpy(feat_dg_oracle_scaled).float()).numpy().squeeze(-1)
        pred_oracle = np.expm1(np.clip(pred_oracle_t, 0, 20))
        pred_oracle = apply_origin_normalization(df, pred_oracle)
        
        # 4. Predict DeepGravity (Survey-Free E2E: GBDT O_hat)
        feat_dg_e2e = build_deep_gravity_pair_features_37(df, nodes_37, O_pred_vec, A_j, d)
        feat_dg_e2e_scaled = scaler_dg.transform(feat_dg_e2e)
        with torch.no_grad():
            pred_e2e_t = dg_model(torch.from_numpy(feat_dg_e2e_scaled).float()).numpy().squeeze(-1)
        pred_e2e = np.expm1(np.clip(pred_e2e_t, 0, 20))
        pred_e2e = apply_origin_normalization(df, pred_e2e)
        
        # Evaluate
        cpc_oracle = cpc(pred_oracle[test_idx], actual[test_idx])
        cpc_e2e = cpc(pred_e2e[test_idx], actual[test_idx])
        
        # Compare with baselines
        O_true_map = dict(zip(zones, np.exp(logO_true)))
        pred_tanner = proposed_predict(df, O_true_map, alpha_nat, beta_nat)
        cpc_tanner = cpc(pred_tanner[test_idx], actual[test_idx])
        
        results.append({
            "city": c,
            "CPC_DeepGravity_Oracle": round(cpc_oracle, 4),
            "CPC_DeepGravity_E2E": round(cpc_e2e, 4),
            "CPC_Tanner_Oracle": round(cpc_tanner, 4),
        })
        
        logging.info(f"{c}: DG_Oracle={cpc_oracle:.4f}, DG_E2E={cpc_e2e:.4f}, Tanner={cpc_tanner:.4f}")
    
    # Save results
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    df_res = pd.DataFrame(results)
    df_res.to_csv(os.path.join(results_dir, "us_25heldout_deepgravity_37features.csv"), index=False)
    
    logging.info(f"✓ Results saved to results/us_25heldout_deepgravity_37features.csv")
    logging.info(f"Total time: {time.time() - t0:.1f}s")
    
    # Summary statistics
    mean_oracle = df_res["CPC_DeepGravity_Oracle"].mean()
    mean_e2e = df_res["CPC_DeepGravity_E2E"].mean()
    mean_tanner = df_res["CPC_Tanner_Oracle"].mean()
    
    print("\n" + "="*70)
    print("DEEPGRAVITY 37-FEATURE ZERO-SHOT EVALUATION SUMMARY")
    print("="*70)
    print(f"Mean CPC (DeepGravity Oracle):     {mean_oracle:.4f}")
    print(f"Mean CPC (DeepGravity E2E):       {mean_e2e:.4f}")
    print(f"Mean CPC (Tanner Oracle Baseline): {mean_tanner:.4f}")
    print("="*70)

if __name__ == "__main__":
    main()
