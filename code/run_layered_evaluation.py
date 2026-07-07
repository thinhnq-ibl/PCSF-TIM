import os
import sys
import time
import logging
import numpy as np
import pandas as pd
from scipy.optimize import minimize, minimize_scalar
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List, Dict

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path)
sys.path.insert(0, os.path.dirname(dir_path))
sys.path.insert(0, os.path.dirname(os.path.dirname(dir_path)))

from conference_benchmark import make_split, TEST_FRAC, SPLIT_SEED, cpc, _fit_pe_bin50_train
from utils import load_city, build_pairs_dataframe, apply_origin_normalization, rmse, r2_log
from run_survey_free_25to25_redesign import (
    CITIES_50, SOURCE_CITIES, HELDOUT_CITIES,
    load_road_density, build_city_features_redesign,
    proposed_predict, national_decay
)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

EPS = 1e-6

# Morphology taxonomy for Layer 5
MORPHOLOGY_GROUPS = {
    "Dense / Transit": ["New_York", "Chicago", "Philadelphia", "Boston", "San_Francisco", "Washington_DC", "Baltimore", "Minneapolis", "Oakland", "Long_Beach"],
    "Sprawling / Grid": ["Los_Angeles", "Houston", "Phoenix", "San_Antonio", "Dallas", "Atlanta", "Denver", "Indianapolis", "Columbus", "Las_Vegas", "Jacksonville", "Kansas_City", "Omaha", "Oklahoma_City", "Tulsa", "Wichita", "El_Paso", "Mesa", "Arlington", "Fort_Worth", "Tucson"],
    "Polycentric": ["San_Jose", "Austin", "Charlotte", "Louisville", "Memphis", "Milwaukee", "Nashville", "Raleigh", "Detroit", "Sacramento", "Fresno", "Albuquerque", "Colorado_Springs"],
    "Coastal": ["San_Diego", "Seattle", "Portland", "Miami", "Tampa", "Virginia_Beach"]
}

def predict_tanner_singly(o_idx, A, d, gamma, beta):
    """Production-constrained Tanner gravity with constant/variable outflows."""
    log_f = np.log(A.clip(1e-9)) - gamma * np.log(d.clip(1e-6)) - beta * d
    n_o = int(o_idx.max()) + 1
    lf_max = np.full(n_o, -np.inf)
    np.maximum.at(lf_max, o_idx, log_f)
    shifted = np.exp(log_f - lf_max[o_idx])
    sum_exp = np.zeros(n_o)
    np.add.at(sum_exp, o_idx, shifted)
    log_B = lf_max + np.log(sum_exp.clip(1e-300))
    return np.exp(log_f - log_B[o_idx])

def fit_decay_from_bins_only(df, b_k, edges):
    """Fits decay parameters using ONLY the distance bin distribution (no OD, no Oi variance)."""
    d = df["d_clamped"].values
    A = df["A_j"].values
    o_idx = df["o_idx"].values
    
    K = len(b_k)
    bin_idx = np.clip(np.searchsorted(edges[1:-1], d), 0, K - 1)
    
    # Calculate midpoints of bins for moment estimation
    midpoints = []
    for i in range(K):
        left = edges[i]
        right = edges[i+1]
        if np.isinf(right):
            # Fallback for last bin: use 1.5 * left boundary
            midpoints.append(1.5 * left)
        else:
            midpoints.append(0.5 * (left + right))
    midpoints = np.array(midpoints)
    d_obs = float(np.sum(b_k * midpoints))
    
    # Scientific initialization
    beta_init = np.clip(1.0 / np.maximum(d_obs, 1e-3), 0.001, 2.0)
    gamma_init = 1.0
    
    best_loss = np.inf
    best_params = [gamma_init, beta_init]
    
    # Reparameterized optimization with restarts to avoid local minima
    # optimization variables: theta = [log_gamma, log_beta]
    def loss_reparam(theta):
        g = np.exp(theta[0])
        b = np.exp(theta[1])
        T_hat = predict_tanner_singly(o_idx, A, d, g, b)
        p_k = np.bincount(bin_idx, weights=T_hat, minlength=K).astype(float)
        tot = p_k.sum()
        if tot < 1e-12:
            return 1e12
        p_k = (p_k / tot).clip(1e-15)
        return -float(np.sum(b_k * np.log(p_k)))
        
    rng = np.random.default_rng(42)
    for run in range(10):
        if run == 0:
            theta_start = [np.log(gamma_init), np.log(beta_init)]
        else:
            theta_start = [
                rng.normal(np.log(gamma_init), 0.25),
                rng.normal(np.log(beta_init), 0.25)
            ]
        
        # Optimize in unconstrained log space
        res = minimize(loss_reparam, x0=theta_start, method="L-BFGS-B", 
                       bounds=[(np.log(0.01), np.log(5.0)), (np.log(0.0001), np.log(2.0))])
        
        if res.success and res.fun < best_loss:
            best_loss = res.fun
            best_params = [np.exp(res.x[0]), np.exp(res.x[1])]
            
    return float(best_params[0]), float(best_params[1])

def fit_decay_mle_od(df):
    """Fits decay parameters using individual OD pairs (MLE Ground Truth)."""
    d = df["d_clamped"].values
    A = df["A_j"].values
    o_idx = df["o_idx"].values
    trips = df["trip_count"].values
    
    unique_o, o_idx_mapped = np.unique(o_idx, return_inverse=True)
    n_o = len(unique_o)
    
    # Calculate empirical mean trip distance from ground truth trips
    total_trips = trips.sum()
    if total_trips > 0:
        d_obs = float(np.sum(trips * d) / total_trips)
    else:
        d_obs = 10.0
        
    # Scientific initialization
    beta_init = np.clip(1.0 / np.maximum(d_obs, 1e-3), 0.001, 2.0)
    gamma_init = 1.0
    
    best_loss = np.inf
    best_params = [gamma_init, beta_init]
    
    # Reparameterized loss function: theta = [log_gamma, log_beta]
    def loss_reparam(theta):
        g = np.exp(theta[0])
        b = np.exp(theta[1])
        log_f = np.log(np.maximum(A, 1e-9)) - g * np.log(np.maximum(d, 1e-6)) - b * d
        lf_max = np.full(n_o, -np.inf)
        np.maximum.at(lf_max, o_idx_mapped, log_f)
        shifted = np.exp(log_f - lf_max[o_idx_mapped])
        sum_exp = np.zeros(n_o)
        np.add.at(sum_exp, o_idx_mapped, shifted)
        log_denom = lf_max + np.log(np.maximum(sum_exp, 1e-300))
        
        log_p = log_f - log_denom[o_idx_mapped]
        return -float(np.sum(trips * log_p))

    rng = np.random.default_rng(42)
    for run in range(10):
        if run == 0:
            theta_start = [np.log(gamma_init), np.log(beta_init)]
        else:
            theta_start = [
                rng.normal(np.log(gamma_init), 0.25),
                rng.normal(np.log(beta_init), 0.25)
            ]
            
        res = minimize(loss_reparam, x0=theta_start, method="L-BFGS-B",
                       bounds=[(np.log(0.01), np.log(5.0)), (np.log(0.0001), np.log(2.0))])
                       
        if res.success and res.fun < best_loss:
            best_loss = res.fun
            best_params = [np.exp(res.x[0]), np.exp(res.x[1])]
            
    return float(best_params[0]), float(best_params[1])


def run_layer1(city_cache, source_cities, heldout_cities):
    logging.info("=== LAYER 1: DECAY IDENTIFICATION TEST ===")
    results_t11 = []
    results_t12 = []
    results_t13 = []
    results_t14 = []
    results_t15 = []
    
    for c in heldout_cities:
        cc = city_cache[c]
        df = cc["df"]
        tr = cc["train_mask"]
        
        # T1.1: Pure Decay Recovery (K=20)
        d_tr = df["d_clamped"].values[tr]
        actual_tr = df["trip_count"].values[tr]
        edges_20 = np.linspace(0, d_tr.max(), 21)
        edges_20[-1] = np.inf
        bin_idx_tr = np.clip(np.searchsorted(edges_20[1:-1], d_tr), 0, 19)
        b_k = np.array([actual_tr[bin_idx_tr == k].sum() for k in range(20)], float)
        b_k /= b_k.sum()
        
        # Fit with no OD data, constant Oi (Oi=1.0)
        g_recovered, b_recovered = fit_decay_from_bins_only(df, b_k, edges_20)
        # Fit with actual OD data (ground truth Tanner direct)
        g_gt, b_gt = fit_decay_mle_od(df.iloc[tr])
        
        # Calculate downstream CPC using oracle outflow
        o_sum = df.groupby("o_idx")["trip_count"].sum()
        O_true_map = o_sum.to_dict()
        pred_gt = proposed_predict(df, O_true_map, g_gt, b_gt)
        pred_rec = proposed_predict(df, O_true_map, g_recovered, b_recovered)
        
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        cpc_gt = cpc(pred_gt[test_idx], actual[test_idx])
        cpc_rec = cpc(pred_rec[test_idx], actual[test_idx])
        
        results_t11.append({
            "city": c,
            "gamma_recovered": g_recovered,
            "beta_recovered": b_recovered,
            "gamma_gt": g_gt,
            "beta_gt": b_gt,
            "cpc_gt": float(cpc_gt),
            "cpc_recovered": float(cpc_rec)
        })
        
        # T1.2: Bin Robustness sweep K in {3, 5, 10, 20}
        params_k = {}
        o_sum = df.groupby("o_idx")["trip_count"].sum()
        O_true_map = o_sum.to_dict()
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        d_max = d_tr.max()
        for K in [3, 5, 10, 20]:
            edges_K = np.linspace(0, d_max, K + 1)
            edges_K[-1] = np.inf
            bin_idx_tr_K = np.clip(np.searchsorted(edges_K[1:-1], d_tr), 0, K - 1)
            b_k_K = np.array([actual_tr[bin_idx_tr_K == k].sum() for k in range(K)], float)
            b_k_K /= b_k_K.sum()
            
            gk, bk = fit_decay_from_bins_only(df, b_k_K, edges_K)
            params_k[f"gamma_{K}"] = gk
            params_k[f"beta_{K}"] = bk
            
            # Downstream CPC prediction
            pred_k = proposed_predict(df, O_true_map, gk, bk)
            cpc_val = cpc(pred_k[test_idx], actual[test_idx])
            params_k[f"cpc_{K}"] = float(cpc_val)
            
        gammas = [params_k[f"gamma_{K}"] for K in [3, 5, 10, 20]]
        betas = [params_k[f"beta_{K}"] for K in [3, 5, 10, 20]]
        results_t12.append({
            "city": c,
            "gamma_std": np.std(gammas),
            "beta_std": np.std(betas),
            **params_k
        })
 
        # T1.3: Attractiveness Perturbation Test (noise: 10%, 20%, 50%)
        rng = np.random.default_rng(SPLIT_SEED)
        for noise in [0.1, 0.2, 0.5]:
            df_pert = df.copy()
            noise_factor = rng.normal(0, noise, len(df_pert))
            df_pert["A_j"] = np.clip(df_pert["A_j"] * (1.0 + noise_factor), 0.0, None)
            
            g_pert, b_pert = fit_decay_from_bins_only(df_pert, b_k, edges_20)
            results_t13.append({
                "city": c,
                "noise": noise,
                "gamma_pert": g_pert,
                "beta_pert": b_pert,
                "gamma_gt": g_gt,
                "beta_gt": b_gt
            })
 
        # T1.4: Missing Attractiveness Information Test (masking: 10%, 20%, 50%)
        unique_zones = df["d_idx"].unique()
        n_zones = len(unique_zones)
        zone_attractions = df.groupby("d_idx")["A_j"].mean()
        mean_attraction = float(zone_attractions.mean())
        
        for mask_pct in [0.1, 0.2, 0.5]:
            df_mask = df.copy()
            rng_mask = np.random.default_rng(SPLIT_SEED)
            mask_size = int(n_zones * mask_pct)
            masked_zones = rng_mask.choice(unique_zones, size=mask_size, replace=False)
            
            is_masked = df_mask["d_idx"].isin(masked_zones)
            df_mask.loc[is_masked, "A_j"] = mean_attraction
            
            g_mask, b_mask = fit_decay_from_bins_only(df_mask, b_k, edges_20)
            results_t14.append({
                "city": c,
                "mask_pct": mask_pct,
                "gamma_mask": g_mask,
                "beta_mask": b_mask,
                "gamma_gt": g_gt,
                "beta_gt": b_gt
            })
 
        # T1.5: CBD Collapse Test (top 10% zones with highest attractiveness A_j)
        zone_attractions_full = df.groupby("d_idx")["A_j"].mean()
        n_top = max(1, int(len(zone_attractions_full) * 0.1))
        top_cbd_zones = zone_attractions_full.nlargest(n_top).index.values
        
        # Scenario T1.5a: Replace top 10% zones with mean attraction
        df_cbd_mean = df.copy()
        df_cbd_mean.loc[df_cbd_mean["d_idx"].isin(top_cbd_zones), "A_j"] = mean_attraction
        g_cbd_mean, b_cbd_mean = fit_decay_from_bins_only(df_cbd_mean, b_k, edges_20)
        
        # Scenario T1.5b: Scale down top 10% zones by 0.2 (80% reduction)
        df_cbd_reduce = df.copy()
        df_cbd_reduce.loc[df_cbd_reduce["d_idx"].isin(top_cbd_zones), "A_j"] *= 0.2
        g_cbd_red, b_cbd_red = fit_decay_from_bins_only(df_cbd_reduce, b_k, edges_20)
        
        results_t15.append({
            "city": c,
            "gamma_cbd_mean": g_cbd_mean,
            "beta_cbd_mean": b_cbd_mean,
            "gamma_cbd_reduce": g_cbd_red,
            "beta_cbd_reduce": b_cbd_red,
            "gamma_gt": g_gt,
            "beta_gt": b_gt
        })
        
    df_t11 = pd.DataFrame(results_t11)
    df_t12 = pd.DataFrame(results_t12)
    df_t13 = pd.DataFrame(results_t13)
    df_t14 = pd.DataFrame(results_t14)
    df_t15 = pd.DataFrame(results_t15)
    
    # Calculate recovery errors and CPC
    gamma_err = np.abs(df_t11["gamma_recovered"] - df_t11["gamma_gt"]).mean()
    beta_err = np.abs(df_t11["beta_recovered"] - df_t11["beta_gt"]).mean()
    cpc_gt_mean = df_t11["cpc_gt"].mean()
    cpc_rec_mean = df_t11["cpc_recovered"].mean()
    
    logging.info(f"T1.1 Pure Decay Recovery MAE vs Ground Truth: gamma_MAE={gamma_err:.4f}, beta_MAE={beta_err:.4f}")
    logging.info(f"T1.1 Downstream CPC under Oracle Outflow: CPC_gt={cpc_gt_mean:.4f}, CPC_rec={cpc_rec_mean:.4f} (Gap={cpc_gt_mean - cpc_rec_mean:.4f})")
    logging.info(f"T1.2 Bin Robustness Parameter Standard Deviation: gamma_std_mean={df_t12['gamma_std'].mean():.4f}, beta_std_mean={df_t12['beta_std'].mean():.4f}")
    logging.info(f"T1.2 Downstream CPC by Bin Count: CPC_3={df_t12['cpc_3'].mean():.4f}, CPC_5={df_t12['cpc_5'].mean():.4f}, CPC_10={df_t12['cpc_10'].mean():.4f}, CPC_20={df_t12['cpc_20'].mean():.4f}")
    
    logging.info("T1.3 Attractiveness Perturbation Test MAE vs Ground Truth:")
    for noise in [0.1, 0.2, 0.5]:
        sub = df_t13[df_t13["noise"] == noise]
        g_err = np.abs(sub["gamma_pert"] - sub["gamma_gt"]).mean()
        b_err = np.abs(sub["beta_pert"] - sub["beta_gt"]).mean()
        logging.info(f"   Noise {int(noise*100)}%: gamma_MAE={g_err:.4f}, beta_MAE={b_err:.4f}")
 
    logging.info("T1.4 Missing Attractiveness Information Test MAE vs Ground Truth:")
    for mask_pct in [0.1, 0.2, 0.5]:
        sub = df_t14[df_t14["mask_pct"] == mask_pct]
        g_err = np.abs(sub["gamma_mask"] - sub["gamma_gt"]).mean()
        b_err = np.abs(sub["beta_mask"] - sub["beta_gt"]).mean()
        logging.info(f"   Mask {int(mask_pct*100)}%: gamma_MAE={g_err:.4f}, beta_MAE={b_err:.4f}")

    logging.info("T1.5 CBD Collapse Test MAE vs Ground Truth:")
    g_err_mean = np.abs(df_t15["gamma_cbd_mean"] - df_t15["gamma_gt"]).mean()
    b_err_mean = np.abs(df_t15["beta_cbd_mean"] - df_t15["beta_gt"]).mean()
    g_err_red = np.abs(df_t15["gamma_cbd_reduce"] - df_t15["gamma_gt"]).mean()
    b_err_red = np.abs(df_t15["beta_cbd_reduce"] - df_t15["beta_gt"]).mean()
    logging.info(f"   T1.5a (Mean Replacement): gamma_MAE={g_err_mean:.4f}, beta_MAE={b_err_mean:.4f}")
    logging.info(f"   T1.5b (80% Reduction):    gamma_MAE={g_err_red:.4f}, beta_MAE={b_err_red:.4f}")

    return df_t11, df_t12, df_t13, df_t14, df_t15

def run_layer2(city_cache, source_cities, heldout_cities, road_impute, decay_params_map):
    logging.info("=== LAYER 2: OUTFLOW (Oi) ESTIMATION TEST ===")
    
    # Train outflow GBDT on source cities
    Xs, ys = [], []
    for c in source_cities:
        cc = city_cache[c]
        X, logO, _ = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        Xs.append(X)
        ys.append(logO)
    Xs = np.vstack(Xs)
    ys = np.concatenate(ys)
    scaler = StandardScaler().fit(Xs)
    
    clf = HistGradientBoostingRegressor(
        max_depth=2, learning_rate=0.05, max_iter=200, l2_regularization=5.0, random_state=42
    )
    clf.fit(scaler.transform(Xs), ys)
    
    results_t2 = []
    oi_logs = []
    
    for c in heldout_cities:
        cc = city_cache[c]
        df = cc["df"]
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        # Outflow prediction
        X, logO_true, zones = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = clf.predict(scaler.transform(X))
        O_hat_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        oi_logs.append((logO_true, logO_pred))
        
        # Get city-specific recovered decay parameters
        g_val, b_val = decay_params_map[c]
        
        # T2.1 Oracle Upper Bound vs Survey Free
        pred_sf = proposed_predict(df, O_hat_map, g_val, b_val)
        O_true_map = dict(zip(zones, np.exp(logO_true)))
        pred_oracle = proposed_predict(df, O_true_map, g_val, b_val)
        
        cpc_sf = cpc(pred_sf[test_idx], actual[test_idx])
        cpc_oracle = cpc(pred_oracle[test_idx], actual[test_idx])
        
        # T2.2 Noise Sensitivity — inject noise into GBDT-predicted logO_pred
        # Baseline (noise=0%) uses cpc_sf (clean GBDT), to measure degradation
        # on top of the model's own prediction, not the oracle.
        noise_results = {}
        for noise_pct in [0.0, 0.1, 0.2, 0.4]:
            if noise_pct == 0.0:
                noise_results[f"cpc_noise_{int(noise_pct*100)}"] = cpc_sf
            else:
                rng = np.random.default_rng(SPLIT_SEED)
                noise = rng.normal(0, noise_pct, len(logO_pred))
                O_noise_map = {z: float(np.maximum(1.0, np.exp(lp + n))) for z, lp, n in zip(zones, logO_pred, noise)}
                pred_noise = proposed_predict(df, O_noise_map, g_val, b_val)
                noise_results[f"cpc_noise_{int(noise_pct*100)}"] = cpc(pred_noise[test_idx], actual[test_idx])
                
        results_t2.append({
            "city": c,
            "cpc_sf": cpc_sf,
            "cpc_oracle": cpc_oracle,
            "cpc_gain": cpc_oracle - cpc_sf,
            **noise_results
        })
        
    df_t2 = pd.DataFrame(results_t2)
    
    # T2.3 Cross-City Transfer Outflow R2
    lt = np.concatenate([a for a, _ in oi_logs])
    lp = np.concatenate([b for _, b in oi_logs])
    r2_oi = r2_log(np.exp(lp), np.exp(lt))
    
    # T2.4 Source-Scale Robustness — learning curve: 5→25 source cities
    logging.info("T2.4 Source-Scale Robustness (learning curve)...")
    scale_steps = [5, 10, 15, 20, 25]
    n_seeds = 3
    lc_rows = []
    for n_src in scale_steps:
        seed_cpcs = []
        for seed_offset in range(n_seeds):
            rng_lc = np.random.default_rng(SPLIT_SEED + seed_offset * 97)
            chosen = list(rng_lc.choice(len(source_cities), size=n_src, replace=False))
            src_subset = [source_cities[i] for i in chosen]
            # Train GBDT on subset
            Xs_sub, ys_sub = [], []
            for c in src_subset:
                cc = city_cache[c]
                X_s, logO_s, _ = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
                Xs_sub.append(X_s)
                ys_sub.append(logO_s)
            Xs_sub = np.vstack(Xs_sub)
            ys_sub = np.concatenate(ys_sub)
            sc_sub = StandardScaler().fit(Xs_sub)
            clf_sub = HistGradientBoostingRegressor(
                max_depth=2, learning_rate=0.05, max_iter=200,
                l2_regularization=5.0, random_state=42
            )
            clf_sub.fit(sc_sub.transform(Xs_sub), ys_sub)
            # Evaluate on ALL 25 heldout cities
            cpcs_h = []
            for c in heldout_cities:
                cc = city_cache[c]
                df_h = cc["df"]
                te_h = cc["test_mask"]
                actual_h = df_h["trip_count"].values
                test_idx_h = np.where(te_h)[0]
                X_h, _, zones_h = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
                logO_pred_h = clf_sub.predict(sc_sub.transform(X_h))
                O_hat_h = {z: float(np.exp(lp)) for z, lp in zip(zones_h, logO_pred_h)}
                g_val, b_val = decay_params_map[c]
                pred_h = proposed_predict(df_h, O_hat_h, g_val, b_val)
                cpcs_h.append(cpc(pred_h[test_idx_h], actual_h[test_idx_h]))
            seed_cpcs.append(float(np.mean(cpcs_h)))
        lc_rows.append({
            "n_source": n_src,
            "cpc_mean": float(np.mean(seed_cpcs)),
            "cpc_std":  float(np.std(seed_cpcs)),
            "cpc_min":  float(np.min(seed_cpcs)),
            "cpc_max":  float(np.max(seed_cpcs)),
        })
        logging.info(f"   T2.4 n_source={n_src:2d}: CPC={np.mean(seed_cpcs):.4f} ± {np.std(seed_cpcs):.4f}")
    df_t24 = pd.DataFrame(lc_rows)
    
    logging.info(f"T2.1 Oracle CPC Mean: {df_t2['cpc_oracle'].mean():.4f} vs Survey-Free CPC Mean: {df_t2['cpc_sf'].mean():.4f} (CPC Gain: {df_t2['cpc_gain'].mean():.4f})")
    logging.info(f"T2.2 Noise Sensitivity CPC Degradation:")
    for noise_pct in [0, 10, 20, 40]:
        logging.info(f"   Noise {noise_pct}%: CPC Mean = {df_t2[f'cpc_noise_{noise_pct}'].mean():.4f}")
    logging.info(f"T2.3 Cross-City Transfer Outflow R2_log: {r2_oi:.6f}")
    return df_t2, r2_oi, df_t24

def run_layer3(city_cache, heldout_cities, decay_params_map, GBDT_model, scaler, road_impute):
    logging.info("=== LAYER 3: ATTRACTION MODEL (Aj) ABLATION ===")
    results_t3 = []
    
    for c in heldout_cities:
        cc = city_cache[c]
        df = cc["df"].copy()
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        # Obtain outflow predicted map
        X, logO_true, zones = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = GBDT_model.predict(scaler.transform(X))
        O_hat_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        
        g_val, b_val = decay_params_map[c]
        
        # Helper to run prediction with specific Attraction vector
        def run_ablation_pred(A_vec):
            df_temp = df.copy()
            df_temp["A_j"] = A_vec
            pred = proposed_predict(df_temp, O_hat_map, g_val, b_val)
            return cpc(pred[test_idx], actual[test_idx])
            
        # T3.1 Feature Knockout
        # Attraction model forms:
        # Full: df["A_j"]
        # POI only: minmax(POI_j)
        # Pop only: minmax(P_j)
        # Road only: minmax(rd_j)
        # Area only: minmax(area_j)
        def minmax(x):
            rng = x.max() - x.min()
            return (x - x.min()) / rng if rng > 1e-9 else np.zeros_like(x)
            
        cpc_full = run_ablation_pred(df["A_j"].values)
        cpc_poi = run_ablation_pred(minmax(df["POI_j"].values))
        cpc_pop = run_ablation_pred(minmax(df["P_j"].values))
        cpc_road = run_ablation_pred(minmax(df["POI_j"].values * 0.0 + df["d_idx"].map(cc["road_map"]).fillna(road_impute).values))
        cpc_area = run_ablation_pred(minmax(df["area_j"].values))
        
        # T3.2 Normalization Study
        # Raw features: raw POI + population
        cpc_raw = run_ablation_pred((df["POI_j"].values + df["P_j"].values) / 2.0)
        
        # Z-score normalization attraction
        def zscore_attraction(vals):
            mean_v = vals.mean()
            std_v = vals.std() + EPS
            z = (vals - mean_v) / std_v
            # Clip to be positive to act as attraction
            return np.clip(z - z.min(), 0, None)
            
        cpc_zscore = run_ablation_pred((zscore_attraction(df["POI_j"].values) + zscore_attraction(df["P_j"].values)) / 2.0)
        
        results_t3.append({
            "city": c,
            "cpc_full": cpc_full,
            "cpc_poi_only": cpc_poi,
            "cpc_pop_only": cpc_pop,
            "cpc_road_only": cpc_road,
            "cpc_area_only": cpc_area,
            "cpc_raw": cpc_raw,
            "cpc_zscore": cpc_zscore
        })
        
    df_t3 = pd.DataFrame(results_t3)
    logging.info("T3.1 Feature Knockout Mean CPC:")
    logging.info(f"   Full Attraction: {df_t3['cpc_full'].mean():.4f}")
    logging.info(f"   POI Only:        {df_t3['cpc_poi_only'].mean():.4f}")
    logging.info(f"   Pop Only:        {df_t3['cpc_pop_only'].mean():.4f}")
    logging.info(f"   Road Only:       {df_t3['cpc_road_only'].mean():.4f}")
    logging.info(f"   Area Only:       {df_t3['cpc_area_only'].mean():.4f}")
    logging.info("T3.2 Normalization Study Mean CPC:")
    logging.info(f"   Min-Max (Full):  {df_t3['cpc_full'].mean():.4f}")
    logging.info(f"   Raw Features:    {df_t3['cpc_raw'].mean():.4f}")
    logging.info(f"   Z-Score:         {df_t3['cpc_zscore'].mean():.4f}")
    return df_t3

def run_layer4(city_cache, heldout_cities, decay_params_map, GBDT_model, scaler, road_impute):
    logging.info("=== LAYER 4: FULL SYSTEM DECOMPOSITION TEST ===")
    results_t4 = []
    
    for c in heldout_cities:
        cc = city_cache[c]
        df = cc["df"].copy()
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        X, logO_true, zones = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = GBDT_model.predict(scaler.transform(X))
        O_hat_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        O_flat_map = {z: float(np.mean(np.exp(logO_true))) for z in zones}
        
        g_val, b_val = decay_params_map[c]
        
        # 1. Full model (Decay, Oi predicted, Aj OSM): v(O, d, A)
        pred_full = proposed_predict(df, O_hat_map, g_val, b_val)
        v_O_d_A = cpc(pred_full[test_idx], actual[test_idx])
        
        # 2. No attraction (Aj = 1.0 constant): v(O, d)
        df_no_A = df.copy()
        df_no_A["A_j"] = 1.0
        pred_no_A = proposed_predict(df_no_A, O_hat_map, g_val, b_val)
        v_O_d = cpc(pred_no_A[test_idx], actual[test_idx])
        
        # 3. No production (Oi = constant): v(d, A)
        pred_no_O = proposed_predict(df, O_flat_map, g_val, b_val)
        v_d_A = cpc(pred_no_O[test_idx], actual[test_idx])
        
        # 4. No decay (gamma=0, beta=0): v(O, A)
        pred_no_decay = proposed_predict(df, O_hat_map, 0.0, 0.0)
        v_O_A = cpc(pred_no_decay[test_idx], actual[test_idx])

        # 5. Only O (decay=0, A=1.0 constant): v(O)
        pred_only_O = proposed_predict(df_no_A, O_hat_map, 0.0, 0.0)
        v_O = cpc(pred_only_O[test_idx], actual[test_idx])

        # 6. Only decay (Oi=constant, A=1.0 constant): v(d)
        pred_only_d = proposed_predict(df_no_A, O_flat_map, g_val, b_val)
        v_d = cpc(pred_only_d[test_idx], actual[test_idx])

        # 7. Only attraction (Oi=constant, decay=0): v(A)
        pred_only_A = proposed_predict(df, O_flat_map, 0.0, 0.0)
        v_A = cpc(pred_only_A[test_idx], actual[test_idx])

        # 8. Empty coalition (Oi=constant, decay=0, A=1.0 constant): v(empty)
        pred_uniform = proposed_predict(df_no_A, O_flat_map, 0.0, 0.0)
        v_empty = cpc(pred_uniform[test_idx], actual[test_idx])

        # Compute Shapley Values for this city
        # O contribution
        phi_O = (1.0/3.0) * (v_O_d_A - v_d_A) + (1.0/6.0) * (v_O_d - v_d + v_O_A - v_A) + (1.0/3.0) * (v_O - v_empty)
        # Decay (d) contribution
        phi_d = (1.0/3.0) * (v_O_d_A - v_O_A) + (1.0/6.0) * (v_O_d - v_O + v_d_A - v_A) + (1.0/3.0) * (v_d - v_empty)
        # Attraction (A) contribution
        phi_A = (1.0/3.0) * (v_O_d_A - v_O_d) + (1.0/6.0) * (v_O_A - v_O + v_d_A - v_d) + (1.0/3.0) * (v_A - v_empty)

        results_t4.append({
            "city": c,
            "cpc_full": v_O_d_A,
            "cpc_no_attraction": v_O_d,
            "cpc_no_production": v_d_A,
            "cpc_no_decay": v_O_A,
            "cpc_only_O": v_O,
            "cpc_only_d": v_d,
            "cpc_only_A": v_A,
            "cpc_uniform": v_empty,
            "shapley_Oi": phi_O,
            "shapley_fd": phi_d,
            "shapley_Aj": phi_A
        })
        
    df_t4 = pd.DataFrame(results_t4)
    
    # Compute marginal gains
    df_t4["delta_decay"] = df_t4["cpc_full"] - df_t4["cpc_no_decay"]
    df_t4["delta_Oi"] = df_t4["cpc_full"] - df_t4["cpc_no_production"]
    df_t4["delta_Aj"] = df_t4["cpc_full"] - df_t4["cpc_no_attraction"]
    
    logging.info("T4.1 Full Factorial Ablation Table CPC Mean:")
    logging.info(f"   Full Model:         {df_t4['cpc_full'].mean():.4f}")
    logging.info(f"   No Attraction (Aj): {df_t4['cpc_no_attraction'].mean():.4f}")
    logging.info(f"   No Production (Oi): {df_t4['cpc_no_production'].mean():.4f}")
    logging.info(f"   No Decay (f(d)):    {df_t4['cpc_no_decay'].mean():.4f}")
    logging.info(f"   Uniform Baseline:   {df_t4['cpc_uniform'].mean():.4f}")
    
    logging.info("T4.2 Marginal Contributions Mean CPC Gain:")
    logging.info(f"   Delta Decay:      {df_t4['delta_decay'].mean():+.4f}")
    logging.info(f"   Delta Production: {df_t4['delta_Oi'].mean():+.4f}")
    logging.info(f"   Delta Attraction: {df_t4['delta_Aj'].mean():+.4f}")

    logging.info("T4.3 Shapley Values Mean Contribution:")
    logging.info(f"   Shapley Outflow (Oi):    {df_t4['shapley_Oi'].mean():.4f}")
    logging.info(f"   Shapley Decay (f(d)):    {df_t4['shapley_fd'].mean():.4f}")
    logging.info(f"   Shapley Attraction (Aj): {df_t4['shapley_Aj'].mean():.4f}")
    return df_t4

def run_layer5(city_cache, heldout_cities, decay_params_map, GBDT_model, scaler, road_impute):
    logging.info("=== LAYER 5: ZERO-SHOT GENERALIZATION TEST ===")
    
    results_t5 = []
    
    for c in heldout_cities:
        cc = city_cache[c]
        df = cc["df"]
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        # Identify morphology group
        group = "Unknown"
        for gname, gcities in MORPHOLOGY_GROUPS.items():
            if c in gcities:
                group = gname
                break
                
        # Base predicted outflow
        X, logO_true, zones = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = GBDT_model.predict(scaler.transform(X))
        O_hat_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        
        g_val, b_val = decay_params_map[c]
        
        # Standard survey-free CPC
        pred_sf = proposed_predict(df, O_hat_map, g_val, b_val)
        cpc_sf = cpc(pred_sf[test_idx], actual[test_idx])
        
        # T5.3 Feature Perturbation Stress Test
        # Perturb POI ±10%, population ±20%, road density ±15%
        # Apply uniform multiplicative noise to the inputs of the GBDT
        rng = np.random.default_rng(SPLIT_SEED)
        
        meta = cc["city_data"]["meta"]
        census = cc["city_data"]["census"].copy()
        poi = cc["city_data"]["poi"].copy()
        
        # Perturb population and POI
        census["total_population"] = census["total_population"] * rng.uniform(0.8, 1.2, len(census))
        poi["total_pois"] = poi["total_pois"] * rng.uniform(0.9, 1.1, len(poi))
        
        # Perturb road map
        perturbed_road_map = {k: v * rng.uniform(0.85, 1.15) for k, v in cc["road_map"].items()}
        
        perturbed_city_data = {
            "meta": meta,
            "census": census,
            "poi": poi,
            "dist": cc["city_data"]["dist"],
            "od": cc["city_data"]["od"]
        }
        
        X_pert, _, zones_pert = build_city_features_redesign(perturbed_city_data, perturbed_road_map, road_impute)
        logO_pert = GBDT_model.predict(scaler.transform(X_pert))
        O_pert_map = {z: float(np.exp(lp)) for z, lp in zip(zones_pert, logO_pert)}
        
        pred_pert = proposed_predict(df, O_pert_map, g_val, b_val)
        cpc_pert = cpc(pred_pert[test_idx], actual[test_idx])
        
        results_t5.append({
            "city": c,
            "morphology": group,
            "cpc_sf": cpc_sf,
            "cpc_perturbed": cpc_pert,
            "cpc_drop": cpc_sf - cpc_pert
        })
        
    df_t5 = pd.DataFrame(results_t5)
    
    # T5.1 Morphology-Based Split CPC Means
    logging.info("T5.1 Morphology-Based CPC Performance:")
    for group in MORPHOLOGY_GROUPS.keys():
        sub = df_t5[df_t5["morphology"] == group]
        logging.info(f"   {group:<18s} CPC Mean = {sub['cpc_sf'].mean():.4f} (count={len(sub)})")
        
    # T5.2 Extreme Transfer Experiments
    logging.info("T5.2 Extreme Transfer Mismatched Models:")
    
    # Train specific model on NYC only -> test on sprawling cities
    nyc_cc = city_cache["New_York"]
    X_nyc, logO_nyc, _ = build_city_features_redesign(nyc_cc["city_data"], nyc_cc["road_map"], road_impute)
    scaler_nyc = StandardScaler().fit(X_nyc)
    clf_nyc = HistGradientBoostingRegressor(max_depth=2, learning_rate=0.05, max_iter=200, l2_regularization=5.0, random_state=42)
    clf_nyc.fit(scaler_nyc.transform(X_nyc), logO_nyc)
    
    # Train specific model on LA only -> test on Sprawling/Grid cities
    la_cc = city_cache["Los_Angeles"]
    X_la, logO_la, _ = build_city_features_redesign(la_cc["city_data"], la_cc["road_map"], road_impute)
    scaler_la = StandardScaler().fit(X_la)
    clf_la = HistGradientBoostingRegressor(max_depth=2, learning_rate=0.05, max_iter=200, l2_regularization=5.0, random_state=42)
    clf_la.fit(scaler_la.transform(X_la), logO_la)
    
    # Train specific model on Houston only -> test on Dense cities
    houston_cc = city_cache["Houston"]
    X_hou, logO_hou, _ = build_city_features_redesign(houston_cc["city_data"], houston_cc["road_map"], road_impute)
    scaler_hou = StandardScaler().fit(X_hou)
    clf_hou = HistGradientBoostingRegressor(max_depth=2, learning_rate=0.05, max_iter=200, l2_regularization=5.0, random_state=42)
    clf_hou.fit(scaler_hou.transform(X_hou), logO_hou)
    
    # Evaluate NYC -> Rural/Sprawling
    sprawling_cities = MORPHOLOGY_GROUPS["Sprawling / Grid"]
    cpc_nyc_to_sprawl = []
    for c in sprawling_cities:
        cc = city_cache[c]
        df = cc["df"]
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        X, logO_true, zones = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = clf_nyc.predict(scaler_nyc.transform(X))
        O_pred_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        g_val, b_val = decay_params_map[c]
        pred = proposed_predict(df, O_pred_map, g_val, b_val)
        cpc_nyc_to_sprawl.append(cpc(pred[test_idx], actual[test_idx]))
        
    # Evaluate LA -> Sprawling/Grid
    cpc_la_to_grid = []
    for c in sprawling_cities:
        cc = city_cache[c]
        df = cc["df"]
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        X, logO_true, zones = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = clf_la.predict(scaler_la.transform(X))
        O_pred_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        g_val, b_val = decay_params_map[c]
        pred = proposed_predict(df, O_pred_map, g_val, b_val)
        cpc_la_to_grid.append(cpc(pred[test_idx], actual[test_idx]))
        
    # Evaluate Houston -> Dense
    dense_cities = MORPHOLOGY_GROUPS["Dense / Transit"]
    cpc_houston_to_dense = []
    for c in dense_cities:
        cc = city_cache[c]
        df = cc["df"]
        te = cc["test_mask"]
        actual = df["trip_count"].values
        test_idx = np.where(te)[0]
        
        X, logO_true, zones = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        logO_pred = clf_hou.predict(scaler_hou.transform(X))
        O_pred_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
        g_val, b_val = decay_params_map[c]
        pred = proposed_predict(df, O_pred_map, g_val, b_val)
        cpc_houston_to_dense.append(cpc(pred[test_idx], actual[test_idx]))
        
    logging.info(f"   NYC model -> Sprawling Cities CPC Mean:     {np.mean(cpc_nyc_to_sprawl):.4f}")
    logging.info(f"   LA model -> Sprawling/Grid Cities CPC Mean:  {np.mean(cpc_la_to_grid):.4f}")
    logging.info(f"   Houston model -> Dense Cities CPC Mean:      {np.mean(cpc_houston_to_dense):.4f}")
    
    # T5.3 Feature Perturbation Stress Test CPC Mean drop
    logging.info(f"T5.3 Feature Perturbation Stress Test CPC Drop Mean: {df_t5['cpc_drop'].mean():.4f}")
    
    ext_transfer = {
        "nyc_to_sprawl": float(np.mean(cpc_nyc_to_sprawl)),
        "la_to_grid": float(np.mean(cpc_la_to_grid)),
        "houston_to_dense": float(np.mean(cpc_houston_to_dense))
    }
    return df_t5, ext_transfer

def main():
    t0 = time.time()
    logging.info("Loading 50 cities ...")
    road_vals = []
    city_cache = {}
    for c in CITIES_50:
        city_data = load_city(c)
        df = build_pairs_dataframe(city_data, attr_mode="poi_pop_avg",
                                   min_distance=0.1, adaptive_self=True)
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
    logging.info(f"Data loading complete in {time.time() - t0:.1f}s.")
    
    # Get national decay parameters (median of source city fits)
    gamma_nat, beta_nat = national_decay(city_cache)
    
    # Pre-compute aggregate-recovered decay parameters for all cities (to be used in downstream Zero-Shot layers)
    logging.info("Pre-computing aggregate-recovered decay parameters for all 50 cities...")
    decay_params_map = {}
    for c in CITIES_50:
        cc = city_cache[c]
        df = cc["df"]
        tr = cc["train_mask"]
        d_tr = df["d_clamped"].values[tr]
        actual_tr = df["trip_count"].values[tr]
        edges_20 = np.linspace(0, d_tr.max(), 21)
        edges_20[-1] = np.inf
        bin_idx_tr = np.clip(np.searchsorted(edges_20[1:-1], d_tr), 0, 19)
        b_k = np.array([actual_tr[bin_idx_tr == k].sum() for k in range(20)], float)
        b_k /= b_k.sum()
        g_rec, b_rec = fit_decay_from_bins_only(df, b_k, edges_20)
        decay_params_map[c] = (g_rec, b_rec)
        
    # Train GBDT outflow model on source cities for downstream tests
    Xs, ys = [], []
    for c in SOURCE_CITIES:
        cc = city_cache[c]
        X, logO, _ = build_city_features_redesign(cc["city_data"], cc["road_map"], road_impute)
        Xs.append(X)
        ys.append(logO)
    Xs = np.vstack(Xs)
    ys = np.concatenate(ys)
    scaler = StandardScaler().fit(Xs)
    
    clf = HistGradientBoostingRegressor(
        max_depth=2, learning_rate=0.05, max_iter=200, l2_regularization=5.0, random_state=42
    )
    clf.fit(scaler.transform(Xs), ys)
    
    # Run the layers
    df_t11, df_t12, df_t13, df_t14, df_t15 = run_layer1(city_cache, SOURCE_CITIES, HELDOUT_CITIES)
    df_t2, r2_oi, df_t24 = run_layer2(city_cache, SOURCE_CITIES, HELDOUT_CITIES, road_impute, decay_params_map)
    df_t3 = run_layer3(city_cache, HELDOUT_CITIES, decay_params_map, clf, scaler, road_impute)
    df_t4 = run_layer4(city_cache, HELDOUT_CITIES, decay_params_map, clf, scaler, road_impute)
    df_t5, ext_transfer = run_layer5(city_cache, HELDOUT_CITIES, decay_params_map, clf, scaler, road_impute)
    
    # Save results to prepare_for_paper/results
    results_dir = os.path.join(os.path.dirname(dir_path), "results")
    os.makedirs(results_dir, exist_ok=True)
    
    df_t11.to_csv(os.path.join(results_dir, "layered_t1_recovery.csv"), index=False)
    df_t12.to_csv(os.path.join(results_dir, "layered_t1_robustness.csv"), index=False)
    df_t13.to_csv(os.path.join(results_dir, "layered_t1_attraction_perturbation.csv"), index=False)
    df_t14.to_csv(os.path.join(results_dir, "layered_t1_attraction_masking.csv"), index=False)
    df_t15.to_csv(os.path.join(results_dir, "layered_t1_cbd_collapse.csv"), index=False)
    df_t2.to_csv(os.path.join(results_dir, "layered_t2_outflow.csv"), index=False)
    df_t24.to_csv(os.path.join(results_dir, "layered_t2_learning_curve.csv"), index=False)
    df_t3.to_csv(os.path.join(results_dir, "layered_t3_attraction.csv"), index=False)
    df_t4.to_csv(os.path.join(results_dir, "layered_t4_decomposition.csv"), index=False)
    df_t5.to_csv(os.path.join(results_dir, "layered_t5_generalization.csv"), index=False)
    
    # Write a markdown summary file in results
    with open(os.path.join(results_dir, "layered_evaluation_summary.md"), "w") as f:
        f.write("# Redesigned Experimental Evaluation Protocol Results Summary\n\n")
        f.write(f"Generated at: 2026-06-06\n\n")
        
        f.write("## 1. Decay Identification (Layer 1)\n")
        f.write(f"- T1.1 Pure Decay Recovery MAE vs Ground Truth: gamma_MAE={np.abs(df_t11['gamma_recovered'] - df_t11['gamma_gt']).mean():.4f}, beta_MAE={np.abs(df_t11['beta_recovered'] - df_t11['beta_gt']).mean():.4f}\n")
        f.write(f"- T1.1 Downstream CPC under Oracle Outflow: CPC_gt={df_t11['cpc_gt'].mean():.4f}, CPC_rec={df_t11['cpc_recovered'].mean():.4f} (Gap={df_t11['cpc_gt'].mean() - df_t11['cpc_recovered'].mean():.4f})\n")
        f.write(f"- T1.2 Bin Robustness Parameter Std Mean: gamma_std_mean={df_t12['gamma_std'].mean():.4f}, beta_std_mean={df_t12['beta_std'].mean():.4f}\n")
        f.write(f"- T1.2 Downstream CPC by Bin Count: CPC_3={df_t12['cpc_3'].mean():.4f}, CPC_5={df_t12['cpc_5'].mean():.4f}, CPC_10={df_t12['cpc_10'].mean():.4f}, CPC_20={df_t12['cpc_20'].mean():.4f}\n")
        f.write("- T1.3 Attractiveness Perturbation Test MAE vs Ground Truth:\n")
        for noise in [0.1, 0.2, 0.5]:
            sub = df_t13[df_t13["noise"] == noise]
            g_err = np.abs(sub["gamma_pert"] - sub["gamma_gt"]).mean()
            b_err = np.abs(sub["beta_pert"] - sub["beta_gt"]).mean()
            f.write(f"  - Noise {int(noise*100)}%: gamma_MAE={g_err:.4f}, beta_MAE={b_err:.4f}\n")
        f.write("- T1.4 Missing Attractiveness Information Test MAE vs Ground Truth:\n")
        for mask_pct in [0.1, 0.2, 0.5]:
            sub = df_t14[df_t14["mask_pct"] == mask_pct]
            g_err = np.abs(sub["gamma_mask"] - sub["gamma_gt"]).mean()
            b_err = np.abs(sub["beta_mask"] - sub["beta_gt"]).mean()
            f.write(f"  - Mask {int(mask_pct*100)}%: gamma_MAE={g_err:.4f}, beta_MAE={b_err:.4f}\n")
        f.write("- T1.5 CBD Collapse Test MAE vs Ground Truth:\n")
        g_err_mean = np.abs(df_t15["gamma_cbd_mean"] - df_t15["gamma_gt"]).mean()
        b_err_mean = np.abs(df_t15["beta_cbd_mean"] - df_t15["beta_gt"]).mean()
        g_err_red = np.abs(df_t15["gamma_cbd_reduce"] - df_t15["gamma_gt"]).mean()
        b_err_red = np.abs(df_t15["beta_cbd_reduce"] - df_t15["beta_gt"]).mean()
        f.write(f"  - T1.5a (Mean Replacement): gamma_MAE={g_err_mean:.4f}, beta_MAE={b_err_mean:.4f}\n")
        f.write(f"  - T1.5b (80% Reduction):    gamma_MAE={g_err_red:.4f}, beta_MAE={b_err_red:.4f}\n")
        f.write("\n")
        
        f.write("## 2. Outflow (Oi) Estimation (Layer 2)\n")
        f.write(f"- T2.1 Oracle CPC Mean: {df_t2['cpc_oracle'].mean():.4f} vs Survey-Free CPC Mean: {df_t2['cpc_sf'].mean():.4f} (CPC Gain: {df_t2['cpc_gain'].mean():.4f})\n")
        f.write(f"- T2.2 Noise Sensitivity CPC:\n")
        for noise_pct in [0, 10, 20, 40]:
            f.write(f"  - Noise {noise_pct}%: CPC Mean = {df_t2[f'cpc_noise_{noise_pct}'].mean():.4f}\n")
        f.write(f"- T2.3 Cross-City Transfer Outflow R2_log: {r2_oi:.6f}\n")
        f.write(f"- T2.4 Source-Scale Learning Curve (CPC mean ± std):\n")
        for _, row in df_t24.iterrows():
            f.write(f"  - n_source={int(row['n_source']):2d}: CPC={row['cpc_mean']:.4f} ± {row['cpc_std']:.4f}\n")
        f.write("\n")
        
        f.write("## 3. Attraction Model (Aj) Ablation (Layer 3)\n")
        f.write("- T3.1 Feature Knockout Mean CPC:\n")
        f.write(f"  - Full Attraction: {df_t3['cpc_full'].mean():.4f}\n")
        f.write(f"  - POI Only:        {df_t3['cpc_poi_only'].mean():.4f}\n")
        f.write(f"  - Pop Only:        {df_t3['cpc_pop_only'].mean():.4f}\n")
        f.write(f"  - Road Only:       {df_t3['cpc_road_only'].mean():.4f}\n")
        f.write(f"  - Area Only:       {df_t3['cpc_area_only'].mean():.4f}\n")
        f.write("- T3.2 Normalization Study Mean CPC:\n")
        f.write(f"  - Min-Max (Full):  {df_t3['cpc_full'].mean():.4f}\n")
        f.write(f"  - Raw Features:    {df_t3['cpc_raw'].mean():.4f}\n")
        f.write(f"  - Z-Score:         {df_t3['cpc_zscore'].mean():.4f}\n\n")
        
        f.write("## 4. Full System Decomposition (Layer 4)\n")
        f.write("- T4.1 Full Factorial Ablation Table CPC Mean:\n")
        f.write(f"  - Full Model:         {df_t4['cpc_full'].mean():.4f}\n")
        f.write(f"  - No Attraction (Aj): {df_t4['cpc_no_attraction'].mean():.4f}\n")
        f.write(f"  - No Production (Oi): {df_t4['cpc_no_production'].mean():.4f}\n")
        f.write(f"  - No Decay (f(d)):    {df_t4['cpc_no_decay'].mean():.4f}\n")
        f.write("- T4.2 Marginal Contributions Mean CPC Gain:\n")
        f.write(f"  - Delta Decay:      {df_t4['delta_decay'].mean():+.4f}\n")
        f.write(f"  - Delta Production: {df_t4['delta_Oi'].mean():+.4f}\n")
        f.write(f"  - Delta Attraction: {df_t4['delta_Aj'].mean():+.4f}\n")
        f.write("- T4.3 Shapley Values Mean Contribution:\n")
        f.write(f"  - Shapley Outflow (Oi):    {df_t4['shapley_Oi'].mean():.4f}\n")
        f.write(f"  - Shapley Decay (f(d)):    {df_t4['shapley_fd'].mean():.4f}\n")
        f.write(f"  - Shapley Attraction (Aj): {df_t4['shapley_Aj'].mean():.4f}\n\n")
        
        f.write("## 5. Zero-Shot Generalization (Layer 5)\n")
        f.write("- T5.1 Morphology-Based CPC Performance:\n")
        for group in MORPHOLOGY_GROUPS.keys():
            sub = df_t5[df_t5["morphology"] == group]
            f.write(f"  - {group:<18s} CPC Mean = {sub['cpc_sf'].mean():.4f}\n")
        f.write("- T5.2 Extreme Transfer Mismatched Models:\n")
        f.write(f"  - NYC model -> Sprawling Cities CPC Mean:     {ext_transfer['nyc_to_sprawl']:.4f}\n")
        f.write(f"  - LA model -> Sprawling/Grid Cities CPC Mean:  {ext_transfer['la_to_grid']:.4f}\n")
        f.write(f"  - Houston model -> Dense Cities CPC Mean:      {ext_transfer['houston_to_dense']:.4f}\n")
        f.write(f"- T5.3 Feature Perturbation Stress Test CPC Drop Mean: {df_t5['cpc_drop'].mean():.4f}\n")
        
    logging.info(f"Layered evaluation complete! Results saved to {results_dir}")

if __name__ == "__main__":
    main()
