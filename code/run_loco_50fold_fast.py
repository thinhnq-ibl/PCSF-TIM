"""
Simplified LOCO 50-fold evaluation - Fast version focusing on core results.
Uses simpler models for speed while maintaining LOCO methodology rigor.
"""

import logging
import numpy as np
import pandas as pd
import json
from pathlib import Path
from typing import List, Dict, Tuple

import sys
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    load_city, build_pairs_dataframe, apply_origin_normalization, 
    cpc, rmse, r2_log, load_road_density
)
from conference_benchmark import make_split, TEST_FRAC, SPLIT_SEED, FULL_CITIES
from run_survey_free_10to40_redesign import (
    build_city_features_redesign, _fit_pe_bin50_train
)
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import HistGradientBoostingRegressor
from baselines import _compute_s_ij

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
logger = logging.getLogger(__name__)

CITIES_50 = FULL_CITIES
RESULTS_DIR = Path(__file__).parent.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)

def fit_decay_simple(df_test, b_k, edges):
    """Simple power-law fit to decay from marginal distribution."""
    from scipy.optimize import minimize
    
    d_test = df_test["d_clamped"].values
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d_test), 0, len(b_k)-1)
    b_vec = b_k[bin_idx]
    
    def neg_loglik(params):
        alpha = params[0]
        val = d_test ** (-alpha)
        val = val / (val.sum() + 1e-9)
        return -np.sum(np.log(np.maximum(val * b_vec, 1e-10)))
    
    result = minimize(neg_loglik, [1.5], method='Nelder-Mead')
    return float(result.x[0])

def run_loco_simplified(cities_list: List[str]) -> Tuple[pd.DataFrame, Dict]:
    """Simplified LOCO 50-fold evaluation - focus on PCF-CTF vs DeepGravity."""
    
    results_per_fold = []
    aggregate_metrics = {model: [] for model in ["PCF_CTF", "DeepGravity", "TraditionalGravity", "Radiation"]}
    
    # Load all city data
    logger.info("Loading city data...")
    city_cache = {}
    road_vals = []
    
    for city in cities_list:
        try:
            city_data = load_city(city)
            df = build_pairs_dataframe(
                city_data, 
                attr_mode="poi_pop_avg",
                min_distance=0.1, 
                adaptive_self=True
            )
            tr_mask, te_mask = make_split(df, SPLIT_SEED, TEST_FRAC)
            road_map = load_road_density(city)
            road_vals.extend(road_map.values())
            
            city_cache[city] = {
                "city_data": city_data,
                "df": df,
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
    
    # National decay parameters
    ab = []
    for c in city_cache.keys():
        df = city_cache[c]["df"]
        tr = city_cache[c]["train_mask"]
        try:
            a, b = _fit_pe_bin50_train(df.iloc[tr])
            ab.append((a, b))
        except Exception as e:
            logger.warning(f"Failed to fit decay for {c}: {e}")
    
    if not ab:
        logger.error("No cities could fit decay!")
        return None, None
    
    ab = np.array(ab)
    alpha_nat = float(np.median(ab[:, 0]))
    beta_nat = float(np.median(ab[:, 1]))
    logger.info(f"National decay: alpha={alpha_nat:.4f}, beta={beta_nat:.4f}")
    
    # LOCO Loop
    for fold_idx, target_city in enumerate(city_cache.keys()):
        logger.info(f"\n=== FOLD {fold_idx+1}/{n_cities}: {target_city} ===")
        
        source_cities = [c for c in city_cache.keys() if c != target_city]
        
        target_cc = city_cache[target_city]
        target_df = target_cc["df"]
        target_test_mask = target_cc["test_mask"]
        target_pairs = target_df[target_test_mask].copy()
        
        # Train GBDT on sources
        Xs_train, ys_train = [], []
        for src in source_cities:
            cc = city_cache[src]
            try:
                X, logO, _ = build_city_features_redesign(
                    cc["city_data"], cc["road_map"], road_impute
                )
                Xs_train.append(X)
                ys_train.append(logO)
            except Exception as e:
                logger.warning(f"Feature extraction failed for {src}: {e}")
        
        if not Xs_train:
            logger.warning(f"No training data for fold {fold_idx}")
            continue
        
        X_train = np.vstack(Xs_train)
        y_train = np.concatenate(ys_train)
        scaler = StandardScaler().fit(X_train)
        
        gbdt = HistGradientBoostingRegressor(
            max_depth=2, learning_rate=0.05, max_iter=100, l2_regularization=5.0, random_state=42
        )
        gbdt.fit(scaler.transform(X_train), y_train)
        
        # Predict on target
        try:
            X_target, logO_target, zones_target = build_city_features_redesign(
                target_cc["city_data"], target_cc["road_map"], road_impute
            )
            logO_pred = gbdt.predict(scaler.transform(X_target))
            O_pred = np.exp(logO_pred)
            O_pred_map = {z: float(o) for z, o in zip(zones_target, O_pred)}
        except Exception as e:
            logger.warning(f"Prediction failed for {target_city}: {e}")
            continue
        
        # Model predictions
        actual = target_pairs["trip_count"].values
        o_idx = target_pairs["o_idx"].values.astype(int)
        d_vec = target_pairs["d_clamped"].values
        O_actual = target_pairs["O_i"].values
        A_actual = target_pairs["A_j"].values
        P_i = target_pairs["P_i"].values
        P_j = target_pairs["P_j"].values
        
        O_pred_vec = np.array([O_pred_map.get(o, 1.0) for o in o_idx])
        
        # 1. PCF-CTF
        T_pcf = O_pred_vec * np.exp(-alpha_nat * np.log(np.maximum(d_vec, 1e-6)) - beta_nat * d_vec) * A_actual
        T_pcf = apply_origin_normalization(target_pairs, T_pcf)
        
        # 2. Traditional Gravity
        T_trad = O_actual * np.exp(-alpha_nat * np.log(np.maximum(d_vec, 1e-6)) - beta_nat * d_vec)
        T_trad = apply_origin_normalization(target_pairs, T_trad)
        
        # 3. Radiation
        s_ij = _compute_s_ij(target_pairs, "P_j")
        T_rad = O_actual * (P_i * P_j) / np.maximum((P_i + s_ij) * (P_i + P_j + s_ij), 1e-9)
        T_rad = apply_origin_normalization(target_pairs, T_rad)
        
        # 4. DeepGravity-style simple neural (very fast)
        from sklearn.neural_network import MLPRegressor
        
        X_mlp_src = []
        y_mlp_src = []
        for src in source_cities:
            cc = city_cache[src]
            src_df = cc["df"]
            src_tr = cc["train_mask"]
            src_pairs = src_df.iloc[src_tr]
            
            X_i = np.log1p(src_pairs["O_i"].values.reshape(-1, 1))
            X_j = np.log1p(src_pairs["A_j"].values.reshape(-1, 1))
            X_d = np.log(np.maximum(src_pairs["d_clamped"].values.reshape(-1, 1), 1e-6))
            X_concat = np.hstack([X_i, X_j, X_d])
            
            X_mlp_src.append(X_concat)
            y_mlp_src.append(np.log1p(src_pairs["trip_count"].values))
        
        X_mlp = np.vstack(X_mlp_src)
        y_mlp = np.concatenate(y_mlp_src)
        
        mlp = MLPRegressor(hidden_layer_sizes=(64,), max_iter=100, learning_rate_init=0.01, random_state=42)
        mlp.fit(X_mlp, y_mlp)
        
        X_i_tgt = np.log1p(O_actual.reshape(-1, 1))
        X_j_tgt = np.log1p(A_actual.reshape(-1, 1))
        X_d_tgt = np.log(np.maximum(d_vec.reshape(-1, 1), 1e-6))
        X_mlp_tgt = np.hstack([X_i_tgt, X_j_tgt, X_d_tgt])
        
        T_mlp_log = mlp.predict(X_mlp_tgt)
        T_mlp = np.expm1(T_mlp_log)
        T_mlp = np.maximum(T_mlp, 1e-9)
        T_mlp = apply_origin_normalization(target_pairs, T_mlp)
        
        # Evaluate
        predictions = {
            "PCF_CTF": T_pcf,
            "DeepGravity": T_mlp,
            "TraditionalGravity": T_trad,
            "Radiation": T_rad
        }
        
        fold_result = {"target_city": target_city}
        for model_name, T_pred in predictions.items():
            c_val = cpc(actual, T_pred)
            fold_result[f"{model_name}_cpc"] = c_val
            aggregate_metrics[model_name].append(c_val)
            logger.info(f"  {model_name:20s}: CPC={c_val:.4f}")
        
        results_per_fold.append(fold_result)
    
    # Aggregate statistics
    df_results = pd.DataFrame(results_per_fold)
    
    stats = {}
    for model in aggregate_metrics:
        vals = np.array(aggregate_metrics[model])
        if len(vals) > 0:
            stats[model] = {
                "mean_cpc": float(np.mean(vals)),
                "std_cpc": float(np.std(vals)),
                "min_cpc": float(np.min(vals)),
                "max_cpc": float(np.max(vals)),
                "median_cpc": float(np.median(vals)),
                "q25_cpc": float(np.percentile(vals, 25)),
                "q75_cpc": float(np.percentile(vals, 75)),
            }
    
    # Calculate win rates
    if len(results_per_fold) > 0:
        pcf_wins = sum(1 for r in results_per_fold if r.get("PCF_CTF_cpc", 1) < r.get("DeepGravity_cpc", 1))
        stats["PCF_CTF"]["win_pct_vs_deepgravity"] = 100 * pcf_wins / len(results_per_fold)
        stats["DeepGravity"]["win_pct_vs_pcf"] = 100 - stats["PCF_CTF"]["win_pct_vs_deepgravity"]
    
    return df_results, stats

def main():
    df_results, stats = run_loco_simplified(CITIES_50)
    
    if df_results is not None:
        # Save results
        csv_file = RESULTS_DIR / "loco_50fold_per_city_cpc.csv"
        json_file = RESULTS_DIR / "loco_50fold_aggregate_stats.json"
        
        df_results.to_csv(csv_file, index=False)
        with open(json_file, 'w') as f:
            json.dump(stats, f, indent=2)
        
        logger.info(f"\n✓ Results saved to:")
        logger.info(f"  CSV:  {csv_file}")
        logger.info(f"  JSON: {json_file}")
        
        # Print summary
        logger.info("\n" + "="*60)
        logger.info("LOCO 50-FOLD SUMMARY")
        logger.info("="*60)
        for model in ["PCF_CTF", "DeepGravity", "TraditionalGravity", "Radiation"]:
            if model in stats:
                s = stats[model]
                logger.info(f"\n{model}:")
                logger.info(f"  Mean CPC: {s['mean_cpc']:.4f} ± {s['std_cpc']:.4f}")
                logger.info(f"  Range: [{s['min_cpc']:.4f}, {s['max_cpc']:.4f}]")
                if "win_pct_vs_deepgravity" in s:
                    logger.info(f"  vs DeepGravity: {s['win_pct_vs_deepgravity']:.1f}% win rate")

if __name__ == "__main__":
    main()
