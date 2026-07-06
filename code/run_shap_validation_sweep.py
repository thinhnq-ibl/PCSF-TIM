import os
import sys
import time
import logging
import numpy as np
import pandas as pd
import shap
from scipy.optimize import minimize
from sklearn.ensemble import GradientBoostingRegressor, HistGradientBoostingRegressor
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List, Dict

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path)
sys.path.insert(0, os.path.dirname(dir_path))

from conference_benchmark import make_split, TEST_FRAC, SPLIT_SEED, cpc
from utils import load_city, build_pairs_dataframe, apply_origin_normalization, rmse, r2_log
from run_survey_free_25to25_redesign import (
    CITIES_50, SOURCE_CITIES, HELDOUT_CITIES,
    load_road_density, proposed_predict, national_decay
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

EPS = 1e-6

def build_city_features_30(city_data: dict, road_map: dict, road_impute: float) -> Tuple[np.ndarray, np.ndarray, List[int], List[str]]:
    """
    Build 30-dimensional spatial features for each zone.
    
    1. 20 Absolute features (area_km2, road_density, pop, total_pois, 16 POIs counts)
    2. 3 Spatial Density features (pop_density, road_density_alt, total_pois_density)
    3. 7 Z-score city-wide context features (z_area, z_road, z_pop, z_total_pois, z_road_alt, z_pop_density, z_total_pois_density)
    """
    df = build_pairs_dataframe(city_data, attr_mode="poi_pop_avg", min_distance=0.1, adaptive_self=True)
    meta = city_data["meta"]
    census = city_data["census"]
    poi = city_data["poi"]
    
    nodes = (
        meta[["idx", "area_km2"]]
        .merge(census[["idx", "total_population"]], on="idx", how="left")
        .merge(poi, on="idx", how="left")
    )
    assert "employment_rate" not in nodes.columns, "employment_rate is non-transferable and must not be used."
    nodes["total_population"] = nodes["total_population"].fillna(0.0)
    nodes["area_km2"] = nodes["area_km2"].fillna(0.01).clip(EPS)
    
    # Road density
    rd = np.array([road_map.get(int(zid), road_impute) for zid in nodes["idx"]], float)
    nodes["road_density"] = np.nan_to_num(rd, nan=road_impute).clip(0.0)
    
    # Base raw values (Absolute Scale - 4 values)
    feat_area = nodes["area_km2"].values
    feat_road = nodes["road_density"].values
    feat_pop = nodes["total_population"].values
    feat_total_pois = nodes["total_pois"].fillna(0.0).values
    
    # 16 raw category POIs (counts)
    poi_cols_raw = [
        "office", "industrial", "commercial", "education_primary", "education_higher",
        "healthcare_hospital", "healthcare_doctor", "shopping_mall", "shopping_supermarket",
        "food_restaurant", "food_cafe", "food_fast", "entertainment_culture",
        "entertainment_sports", "transport_rail", "transport_bus"
    ]
    raw_pois = []
    for col in poi_cols_raw:
        vals = nodes[col].fillna(0.0).values if col in nodes.columns else np.zeros(len(nodes))
        raw_pois.append(vals)
        
    # Absolute list (20 features total)
    absolute_list = [feat_area, feat_road, feat_pop, feat_total_pois] + raw_pois
    absolute_names = ["area_km2", "road_density", "total_population", "total_pois"] + [f"poi_{c}" for c in poi_cols_raw]
    
    # ── Mật độ không gian (Spatial Density - 3 features) ──
    pop_density = feat_pop / feat_area
    total_pois_density = feat_total_pois / feat_area
    
    density_list = [pop_density, feat_road, total_pois_density]
    density_names = ["pop_density", "road_density_alt", "total_pois_density"]
    
    # ── Bối cảnh chuẩn hóa Z-score (Z-Score Context - 7 features) ──
    # Formula: (x - mean_city) / (std_city + EPS)
    def to_zscore(vals):
        mean_v = np.mean(vals)
        std_v = np.std(vals) + EPS
        return (vals - mean_v) / std_v
        
    z_area = to_zscore(feat_area)
    z_road = to_zscore(feat_road)
    z_pop = to_zscore(feat_pop)
    z_total_pois = to_zscore(feat_total_pois)
    z_road_alt = to_zscore(feat_road)
    z_pop_density = to_zscore(pop_density)
    z_total_pois_density = to_zscore(total_pois_density)
    
    zscore_list = [z_area, z_road, z_pop, z_total_pois, z_road_alt, z_pop_density, z_total_pois_density]
    zscore_names = ["z_area_km2", "z_road_density", "z_pop", "z_total_pois", "z_road_density_alt", "z_pop_density", "z_total_pois_density"]
    
    # Stack absolute and density features and log-transform
    abs_stacked = np.column_stack(absolute_list + density_list).astype(np.float32)
    abs_log = np.log1p(np.maximum(0.0, abs_stacked))
    
    # Stack Z-scores (no log-transform)
    z_stacked = np.column_stack(zscore_list).astype(np.float32)
    
    # Final 30 feature matrix
    X_30 = np.concatenate([abs_log, z_stacked], axis=1).astype(np.float32)
    feat_names_30 = absolute_names + density_names + zscore_names
    
    node_feat_dict = dict(zip(nodes["idx"].astype(int), X_30))
    
    # Target outflows to predict
    O = df.groupby("o_idx")["trip_count"].sum()
    orig_zones = sorted(O.index.tolist())
    
    X_out = []
    logO = []
    kept = []
    for z_id in orig_zones:
        if z_id not in node_feat_dict:
            continue
        X_out.append(node_feat_dict[z_id])
        logO.append(np.log(max(float(O[z_id]), 1.0)))
        kept.append(z_id)
        
    return np.array(X_out), np.array(logO), kept, feat_names_30

def main():
    logging.info("STEP 1: Loading city data for 30-feature SHAP selection...")
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
    # Pre-compute aggregate-recovered decay parameters for all 50 cities
    from run_layered_evaluation import fit_decay_from_bins_only
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
    
    # Train base GBDT outflow on all 30 features
    logging.info("STEP 2: Training base GBDT outflow model on 30 features...")
    Xs, ys = [], []
    for c in SOURCE_CITIES:
        cc = city_cache[c]
        X, logO, _, feat_names_30 = build_city_features_30(cc["city_data"], cc["road_map"], road_impute)
        Xs.append(X)
        ys.append(logO)
    Xs = np.vstack(Xs)
    ys = np.concatenate(ys)
    
    scaler = StandardScaler().fit(Xs)
    Xs_scaled = scaler.transform(Xs)
    
    base_model = GradientBoostingRegressor(n_estimators=100, max_depth=4, learning_rate=0.08, random_state=42)
    base_model.fit(Xs_scaled, ys)
    
    # Compute SHAP
    logging.info("STEP 3: Computing SHAP values per city...")
    explainer = shap.TreeExplainer(base_model)
    city_shap_importances = {}
    for c in SOURCE_CITIES:
        cc = city_cache[c]
        X_c, _, _, _ = build_city_features_30(cc["city_data"], cc["road_map"], road_impute)
        X_c_scaled = scaler.transform(X_c)
        shap_values = explainer.shap_values(X_c_scaled)
        city_shap_importances[c] = np.mean(np.abs(shap_values), axis=0)
        
    shap_matrix = np.array([city_shap_importances[c] for c in SOURCE_CITIES])
    mean_shap = np.mean(shap_matrix, axis=0)
    std_shap = np.std(shap_matrix, axis=0)
    stability_index = mean_shap / (std_shap + EPS)
    
    df_stats = pd.DataFrame({
        "idx": range(len(feat_names_30)),
        "feature": feat_names_30,
        "mean_importance": mean_shap,
        "std_importance": std_shap,
        "stability_index": stability_index
    })
    
    # ── STEP 4: SHAP Stability Selection ──────────────────────────────────────
    filtered_indices = df_stats[
        (df_stats["mean_importance"] >= 0.005) & 
        (df_stats["stability_index"] >= 1.0)
    ]["idx"].tolist()
    
    # Correlation pruning (redundancy check > 0.9)
    corr = np.corrcoef(Xs_scaled, rowvar=False)
    active_set = set(filtered_indices)
    for p in sorted(list(active_set)):
        if p not in active_set:
            continue
        for q in sorted(list(active_set)):
            if p == q or q not in active_set:
                continue
            if abs(corr[p, q]) > 0.9:
                mu_p = df_stats.loc[p, "mean_importance"]
                mu_q = df_stats.loc[q, "mean_importance"]
                if mu_p >= mu_q:
                    active_set.discard(q)
                else:
                    active_set.discard(p)
                    break
                    
    selected_indices = sorted(list(active_set))
    selected_features = [feat_names_30[idx] for idx in selected_indices]
    logging.info(f"SHAP Stability Selection found {len(selected_features)} stable features: {selected_features}")
    
    # ── STEP 5: Validation Sweep ──────────────────────────────────────────────
    ranked_features = df_stats.sort_values(by="mean_importance", ascending=False)["feature"].tolist()
    feature_to_idx = {name: idx for idx, name in enumerate(feat_names_30)}
    
    k_values = [5, 6, 7, 10, 15, 20, 25, len(feat_names_30)]
    results = []
    
    print("\n" + "="*80)
    print("SHAP FEATURE SWEEP PERFORMANCE ON 25 HELD-OUT CITIES (30 CANDIDATES)")
    print("="*80)
    print(f"{'K Features':12s} | {'Mean CPC':10s} | {'CPC Std':10s} | {'Outflow R2_log':15s}")
    print("-" * 60)
    
    for k in k_values:
        sub_feats = ranked_features[:k]
        feature_idxs = [feature_to_idx[name] for name in sub_feats if name in feature_to_idx]
        
        # Scale train features
        Xs_sub = Xs[:, feature_idxs]
        scaler_sub = StandardScaler().fit(Xs_sub)
        Xs_sub_scaled = scaler_sub.transform(Xs_sub)
        
        clf = HistGradientBoostingRegressor(max_depth=2, learning_rate=0.05, max_iter=200, l2_regularization=5.0, random_state=42)
        clf.fit(Xs_sub_scaled, ys)
        
        cpc_scores = []
        r2_scores = []
        for c in HELDOUT_CITIES:
            cc = city_cache[c]
            df = cc["df"]
            te = cc["test_mask"]
            actual = df["trip_count"].values
            test_idx = np.where(te)[0]
            
            X_c, logO_true, zones, _ = build_city_features_30(cc["city_data"], cc["road_map"], road_impute)
            X_c_sub = X_c[:, feature_idxs]
            logO_pred = clf.predict(scaler_sub.transform(X_c_sub))
            
            O_hat_map = {z: float(np.exp(lp)) for z, lp in zip(zones, logO_pred)}
            g_val, b_val = decay_params_map[c]
            pred = proposed_predict(df, O_hat_map, g_val, b_val)
            
            cpc_scores.append(cpc(pred[test_idx], actual[test_idx]))
            r2_scores.append(r2_log(np.exp(logO_pred), np.exp(logO_true)))
            
        mean_cpc = np.mean(cpc_scores)
        std_cpc = np.std(cpc_scores)
        mean_r2 = np.mean(r2_scores)
        print(f"{k:<12d} | {mean_cpc:<10.4f} | {std_cpc:<10.4f} | {mean_r2:<15.4f}")
        results.append({"K": k, "Mean_CPC": mean_cpc, "Std_CPC": std_cpc, "Outflow_R2": mean_r2})
        
    print("="*80)
    
    # Save statistics and sweep comparison
    results_dir = "prepare_for_paper/results"
    os.makedirs(results_dir, exist_ok=True)
    df_stats.to_csv(os.path.join(results_dir, "layered_t6_shap_stats_30.csv"), index=False)
    
    # Write a new markdown summary
    output_md_path = os.path.join(results_dir, "shap_evaluation_summary_30.md")
    with open(output_md_path, "w") as f:
        f.write("# SHAP Feature Selection & Sweep Report (30 Candidates)\n\n")
        f.write("## 1. Feature Ranking Table\n\n")
        f.write("| Rank | Feature Name | Mean Absolute SHAP (\\mu_p) | Stability (S_p) | Selected |\n")
        f.write("| --- | --- | ---: | ---: | :---: |\n")
        df_stats_sorted = df_stats.sort_values(by="mean_importance", ascending=False)
        for rank, (_, row) in enumerate(df_stats_sorted.iterrows(), 1):
            is_sel = "Yes" if row["idx"] in selected_indices else "No"
            f.write(f"| {rank} | {row['feature']} | {row['mean_importance']:.6f} | {row['stability_index']:.4f} | {is_sel} |\n")
            
        f.write("\n## 2. K-Feature Sweep Evaluation\n\n")
        f.write("| K Features | Mean CPC | CPC Std Dev | Outflow R²_log |\n")
        f.write("| --- | ---: | ---: | ---: |\n")
        for res in results:
            f.write(f"| {res['K']} | {res['Mean_CPC']:.4f} | {res['Std_CPC']:.4f} | {res['Outflow_R2']:.4f} |\n")
            
    logging.info(f"SHAP validation complete! Report saved to {output_md_path}")

if __name__ == "__main__":
    main()
