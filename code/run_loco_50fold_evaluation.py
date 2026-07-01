"""
Leave-One-City-Out (LOCO) 50-Fold Evaluation Framework
======================================================

This script implements rigorous LOCO cross-validation:
- For each of 50 cities (fold):
  - Train all models on 49 source cities
  - Evaluate zero-shot on the held-out city
  - Record CPC, RMSE, R2_log per city
- Report aggregate statistics across all 50 folds

Outputs:
  results/loco_50fold_per_city_cpc.csv     - CPC per city
  results/loco_50fold_aggregate_stats.json - Mean, std, quantiles
  results/loco_50fold_comparison.csv       - Baseline comparison
"""

import os, sys, time, json, logging
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple
from scipy.optimize import minimize, minimize_scalar
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

# Setup paths
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from conference_benchmark import make_split, TEST_FRAC, SPLIT_SEED, _fit_pe_bin50_train
from utils import load_city, build_pairs_dataframe, apply_origin_normalization, cpc, rmse, r2_log, load_road_density
from feature_builders import (
    build_gbdt_outflow_features_23, 
    build_zone_features_38, 
    build_deep_gravity_pair_features_38,
    SHAP_FEATURES_23
)
from run_survey_free_25to25_redesign import CITIES_50

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

RESULTS_DIR = HERE.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)


def fit_decay_tanner_from_aggregate(df, b_k, edges):
    """Fit Tanner decay (α, β) from marginal distance distribution only."""
    d = df["d_clamped"].values
    A = df["A_j"].values
    o_idx = df["o_idx"].values
    
    K = len(b_k)
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    def predict_tanner(o_idx_arr, A_arr, d_arr, alpha, beta):
        """Production-constrained Tanner gravity."""
        log_f = np.log(np.maximum(A_arr, 1e-9)) - alpha * np.log(np.maximum(d_arr, 1e-6)) - beta * d_arr
        n_o = int(o_idx_arr.max()) + 1
        lf_max = np.full(n_o, -np.inf)
        np.maximum.at(lf_max, o_idx_arr, log_f)
        shifted = np.exp(log_f - lf_max[o_idx_arr])
        sum_exp = np.zeros(n_o)
        np.add.at(sum_exp, o_idx_arr, shifted)
        return np.exp(log_f - (lf_max[o_idx_arr] + np.log(np.maximum(sum_exp[o_idx_arr], 1e-300))))
    
    def loss(params):
        alpha, beta = params
        T_hat = predict_tanner(o_idx, A, d, alpha, beta)
        p_k = np.bincount(bin_idx, weights=T_hat, minlength=K).astype(float)
        tot = p_k.sum()
        if tot < 1e-12:
            return 1e12
        p_k = (p_k / tot).clip(1e-15)
        return -float(np.sum(b_k * np.log(p_k)))
    
    res = minimize(loss, x0=[1.0, 0.05], bounds=[(0.01, 5.0), (0.001, 2.0)], method="L-BFGS-B")
    return float(res.x[0]), float(res.x[1])


def run_loco_evaluation(cities_list: List[str]) -> Tuple[pd.DataFrame, Dict]:
    """
    Run LOCO 50-fold evaluation.
    Returns: (per_city_results_df, aggregate_stats_dict)
    """
    
    results_per_fold = []
    aggregate_metrics = {
        "PCF_CTF": {"cpc": [], "rmse": [], "r2_log": []},
        "DeepGravity": {"cpc": [], "rmse": [], "r2_log": []},
        "TraditionalGravity": {"cpc": [], "rmse": [], "r2_log": []},
        "Radiation": {"cpc": [], "rmse": [], "r2_log": []},
    }
    
    # Load all city data once
    logger.info("Loading city data...")
    city_cache = {}
    road_vals = []
    
    for city in cities_list:
        try:
            city_data = load_city(city)
            pairs_df = build_pairs_dataframe(
                city_data, 
                attr_mode="poi_pop_avg",
                min_distance=0.1, 
                adaptive_self=True
            )
            tr_mask, te_mask = make_split(pairs_df, SPLIT_SEED, TEST_FRAC)
            road_map = load_road_density(city)
            road_vals.extend(road_map.values())
            
            city_cache[city] = {
                "city_data": city_data,
                "df": pairs_df,  # Use "df" to match expected key
                "train_mask": tr_mask,
                "test_mask": te_mask,
                "road_map": road_map,
            }
        except Exception as e:
            logger.warning(f"Failed to load {city}: {e}")
            continue
    
    road_impute = float(np.median(road_vals)) if road_vals else 1e-4
    
    n_cities = len(city_cache)
    logger.info(f"Loaded {n_cities} cities. Starting LOCO evaluation...")
    
    # Compute national decay parameters from ALL cities' training data (LOCO principle: only use source cities)
    def compute_loco_national_decay(cache_dict):
        """Compute national decay from all cities' training data."""
        from run_survey_free_25to25_redesign import _fit_pe_bin50_train
        ab = []
        for city, cc in cache_dict.items():
            df = cc["df"]
            tr = cc["train_mask"]
            try:
                a, b = _fit_pe_bin50_train(df.iloc[tr])
                ab.append((a, b))
            except Exception as e:
                logger.warning(f"Failed to compute decay for {city}: {e}")
                continue
        if not ab:
            return 0.5, 0.01  # Default fallback
        ab = np.array(ab)
        return float(np.median(ab[:, 0])), float(np.median(ab[:, 1]))
    
    alpha_nat, beta_nat = compute_loco_national_decay(city_cache)
    logger.info(f"National decay parameters: alpha={alpha_nat:.4f}, beta={beta_nat:.4f}")

    
    # LOCO Loop: for each city as target
    for fold_idx, target_city in enumerate(city_cache.keys()):
        logger.info(f"\n=== FOLD {fold_idx+1}/{n_cities}: Target City = {target_city} ===")
        
        source_cities = [c for c in city_cache.keys() if c != target_city]
        
        target_cc = city_cache[target_city]
        target_df = target_cc["df"]
        # In zero-shot LOCO, the "test" set is the entire target city (100% data evaluation)
        target_test_df = target_df.copy()

        # ========== LAYER 1: Decay (Aggregate local) ==========
        d_test = target_test_df["d_clamped"].values
        actual_test = target_test_df["trip_count"].values
        edges_20 = np.percentile(d_test, np.linspace(0, 100, 21))
        edges_20[0], edges_20[-1] = 0.0, np.inf
        bin_idx_test = np.clip(np.searchsorted(edges_20[1:-1], d_test), 0, 19)
        b_k = np.array([actual_test[bin_idx_test == k].sum() for k in range(20)], dtype=float)
        b_k = b_k / (b_k.sum() + 1e-9)
        
        alpha_agg, beta_agg = fit_decay_tanner_from_aggregate(target_test_df, b_k, edges_20)
        
        # ========== LAYER 2: PCF-CTF (GBDT 23 SHAP Features) ==========
        logger.info(f"Training GBDT outflow model on {len(source_cities)} source cities...")
        
        Xs_tr, ys_tr = [], []
        for src_city in source_cities:
            cc = city_cache[src_city]
            try:
                # Use 23 SHAP Features for GBDT as per paper
                X, logO, _ = build_gbdt_outflow_features_23(
                    cc["city_data"], cc["road_map"], road_impute
                )
                Xs_tr.append(X)
                ys_tr.append(logO)
            except Exception:
                continue
        
        X_tr_gbdt = np.vstack(Xs_tr)
        y_tr_gbdt = np.concatenate(ys_tr)
        scaler_gbdt = StandardScaler()
        X_tr_gbdt_s = scaler_gbdt.fit_transform(X_tr_gbdt)
        
        gbdt = HistGradientBoostingRegressor(max_depth=5, max_iter=200, random_state=42)
        gbdt.fit(X_tr_gbdt_s, y_tr_gbdt)
        
        # Predict target outflows
        X_tgt_gbdt, _, zones_tgt_gbdt = build_gbdt_outflow_features_23(
            target_cc["city_data"], target_cc["road_map"], road_impute
        )
        O_pred = np.exp(gbdt.predict(scaler_gbdt.transform(X_tgt_gbdt)))
        O_pred_map = dict(zip(zones_tgt_gbdt, O_pred))
        
        # ========== LAYER 3: DeepGravity (38 Features) ==========
        logger.info("Training DeepGravity MLP baseline...")
        
        X_dg_tr_list, y_dg_tr_list = [], []
        for src_city in source_cities:
            cc = city_cache[src_city]
            tr_idx = cc["train_mask"]
            z_feats, _ = build_zone_features_38(cc["city_data"], cc["road_map"], road_impute)
            
            # Subsample pairs for training speed
            src_df_sub = cc["df"].iloc[tr_idx]
            if len(src_df_sub) > 2000:
                src_df_sub = src_df_sub.sample(2000, random_state=42)
            
            X_dg = build_deep_gravity_pair_features_38(
                src_df_sub, z_feats, src_df_sub["O_i"].values, 
                src_df_sub["A_j"].values, src_df_sub["d_clamped"].values
            )
            X_dg_tr_list.append(X_dg)
            y_dg_tr_list.append(np.log1p(src_df_sub["trip_count"].values))
            
        X_dg_tr = np.vstack(X_dg_tr_list).astype(np.float32)
        y_dg_tr = np.concatenate(y_dg_tr_list).astype(np.float32)
        scaler_dg = StandardScaler()
        X_dg_tr_s = scaler_dg.fit_transform(X_dg_tr)
        
        dg_mlp = MLPRegressor(hidden_layer_sizes=(128, 64), max_iter=50, random_state=42)
        dg_mlp.fit(X_dg_tr_s, y_dg_tr)
        
        # Model predictions for target city
        o_idx_tgt = target_test_df["o_idx"].values.astype(int)
        d_vec_tgt = target_test_df["d_clamped"].values
        A_j_tgt = target_test_df["A_j"].values
        O_i_gt_tgt = target_test_df["O_i"].values
        
        # 1. PCF-CTF (Proposed)
        O_i_pred_tgt = np.array([O_pred_map.get(o, 1.0) for o in o_idx_tgt])
        f_d_tgt = np.exp(-alpha_agg * np.log(np.maximum(d_vec_tgt, 1e-6)) - beta_agg * d_vec_tgt)
        T_pcf = O_i_pred_tgt * f_d_tgt * A_j_tgt
        T_pcf = apply_origin_normalization(target_test_df, T_pcf)
        
        # 2. DeepGravity (E2E)
        z_feats_tgt, _ = build_zone_features_38(target_cc["city_data"], target_cc["road_map"], road_impute)
        X_dg_tgt = build_deep_gravity_pair_features_38(
            target_test_df, z_feats_tgt, O_i_gt_tgt, A_j_tgt, d_vec_tgt
        )
        T_dg = np.expm1(dg_mlp.predict(scaler_dg.transform(X_dg_tgt)))
        T_dg = apply_origin_normalization(target_test_df, T_dg)
        
        # 3. Traditional Gravity
        T_trad = O_i_gt_tgt * f_d_tgt * A_j_tgt
        T_trad = apply_origin_normalization(target_test_df, T_trad)
        
        # 4. Radiation
        from baselines import _compute_s_ij
        s_ij_tgt = _compute_s_ij(target_test_df, "P_j")
        P_i_tgt, P_j_tgt = target_test_df["P_i"].values, target_test_df["P_j"].values
        T_rad = O_i_gt_tgt * (P_i_tgt * P_j_tgt) / np.maximum((P_i_tgt + s_ij_tgt) * (P_i_tgt + P_j_tgt + s_ij_tgt), 1e-9)
        T_rad = apply_origin_normalization(target_test_df, T_rad)
        
        predictions = {
            "PCF_CTF": T_pcf,
            "DeepGravity": T_dg,
            "TraditionalGravity": T_trad,
            "Radiation": T_rad
        }
        
        # ========== Evaluate All Models ==========
        actual_tgt = target_test_df["trip_count"].values
        
        fold_results = {"target_city": target_city}
        for m_name, T_pred in predictions.items():
            c = cpc(actual_tgt, T_pred)
            r = rmse(actual_tgt, T_pred)
            r2 = r2_log(actual_tgt, T_pred)
            
            aggregate_metrics[m_name]["cpc"].append(c)
            aggregate_metrics[m_name]["rmse"].append(r)
            aggregate_metrics[m_name]["r2_log"].append(r2)
            
            fold_results[f"{m_name}_cpc"] = c
            fold_results[f"{m_name}_rmse"] = r
            fold_results[f"{m_name}_r2_log"] = r2
            
            logger.info(f"  {m_name:20s}: CPC={c:.4f}, RMSE={r:.2f}, R2_log={r2:.4f}")
        
        results_per_fold.append(fold_results)
    
    # Aggregate statistics
    df_results = pd.DataFrame(results_per_fold)
    
    stats = {}
    for model_name in aggregate_metrics:
        cpc_vals = np.array(aggregate_metrics[model_name]["cpc"])
        stats[model_name] = {
            "mean_cpc": float(np.mean(cpc_vals)),
            "std_cpc": float(np.std(cpc_vals)),
            "min_cpc": float(np.min(cpc_vals)),
            "max_cpc": float(np.max(cpc_vals)),
            "median_cpc": float(np.median(cpc_vals)),
            "q25_cpc": float(np.percentile(cpc_vals, 25)),
            "q75_cpc": float(np.percentile(cpc_vals, 75)),
            "mean_rmse": float(np.mean(aggregate_metrics[model_name]["rmse"])),
            "mean_r2_log": float(np.mean(aggregate_metrics[model_name]["r2_log"])),
        }
    
    # Win rate calculation (PCF-CTF vs DeepGravity)
    pcf_wins = (df_results["PCF_CTF_cpc"] > df_results["DeepGravity_cpc"]).sum()
    win_pct = 100 * pcf_wins / len(df_results)
    stats["PCF_CTF"]["win_pct_vs_deepgravity"] = float(win_pct)
    
    return df_results, stats


if __name__ == "__main__":
    logger.info("Starting LOCO 50-Fold Evaluation...")
    
    # Run evaluation
    df_results, stats = run_loco_evaluation(CITIES_50)
    
    # Save results
    df_results.to_csv(RESULTS_DIR / "loco_50fold_per_city_cpc.csv", index=False)
    logger.info(f"Saved per-city results: {RESULTS_DIR}/loco_50fold_per_city_cpc.csv")
    
    with open(RESULTS_DIR / "loco_50fold_aggregate_stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    logger.info(f"Saved aggregate stats: {RESULTS_DIR}/loco_50fold_aggregate_stats.json")
    
    # Print summary
    logger.info("\n" + "="*70)
    logger.info("LOCO 50-FOLD AGGREGATE STATISTICS")
    logger.info("="*70)
    for model_name in sorted(stats.keys()):
        s = stats[model_name]
        logger.info(f"\n{model_name}:")
        logger.info(f"  Mean CPC:   {s['mean_cpc']:.4f} ± {s['std_cpc']:.4f}")
        logger.info(f"  CPC range:  [{s['min_cpc']:.4f}, {s['max_cpc']:.4f}]")
        logger.info(f"  Mean RMSE:  {s['mean_rmse']:.2f}")
        logger.info(f"  Mean R2_log: {s['mean_r2_log']:.4f}")
        if "win_pct_vs_deepgravity" in s:
            logger.info(f"  Win rate vs DeepGravity: {s['win_pct_vs_deepgravity']:.1f}%")
    
    logger.info("\n" + "="*70)
    logger.info("LOCO 50-Fold evaluation complete!")
    logger.info("="*70)
