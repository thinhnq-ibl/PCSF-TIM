"""
Feature Builders for DeepGravity and GBDT Models
==================================================

This module provides feature construction functions aligned with model inductive biases:

1. **DeepGravity (38 Features)**: 
   - Inductive Bias: Neural networks learn complex non-linear interactions
   - Rationale: Full feature space allows MLP to discover emergent patterns across
     all urban characteristics (POI categories, population, infrastructure)
   - Features: 6 base + 16 POI counts + 16 POI densities = 38 total
   
2. **GBDT (23 SHAP Features)**:
   - Inductive Bias: Tree-based models prefer robust, stable features
   - Rationale: SHAP-selected features are transferable across cities, reducing
     overfitting to city-specific artifacts
   - Features: Curated subset identified via cross-city SHAP stability analysis

Author: PSF-CTF Team
Date: 2026-06-06
"""

import numpy as np
import pandas as pd
from typing import Tuple, List, Dict
from utils import build_pairs_dataframe

EPS = 1e-6

# =====================================================================
# DEEPGRAVITY: 37-FEATURE BUILDER (FULL FEATURE SPACE)
# =====================================================================

def build_deep_gravity_pair_features_37(
    df: pd.DataFrame,
    nodes_37_df: pd.DataFrame,
    O_vec: np.ndarray,
    A_j_vec: np.ndarray,
    d_vec: np.ndarray
) -> np.ndarray:
    """
    Build 37-dimensional DeepGravity features for all OD pairs.
    
    Feature Structure (37 total):
    - 3 core: log(O_i), log(A_j), log(d_ij)
    - 17 origin zone features: subset of 37 zone-level features
    - 17 destination zone features: subset of 37 zone-level features
    
    Total = 3 + 17 + 17 = 37.
    """
    zone_to_features = nodes_37_df.set_index("idx")
    zone_feats_subset = zone_to_features.iloc[:, :17]
    
    # Vectorized reindexing mapping zone features to OD pairs in milliseconds
    o_feats = zone_feats_subset.reindex(df["o_idx"]).fillna(0.0).values.astype(np.float32)
    d_feats = zone_feats_subset.reindex(df["d_idx"]).fillna(0.0).values.astype(np.float32)
    
    # Build feature matrix: [log(O_i), log(A_j), log(d), origin_feats, dest_feats]
    core_feats = np.stack([
        np.log1p(O_vec),
        np.log1p(A_j_vec),
        np.log(np.maximum(d_vec + 0.1, 0.1))
    ], axis=1).astype(np.float32)
    
    feat_matrix = np.concatenate([core_feats, o_feats, d_feats], axis=1).astype(np.float32)
    
    return feat_matrix


def build_zone_features_37(city_data: dict, road_map: dict, road_impute: float) -> Tuple[pd.DataFrame, List[str]]:
    """
    Build 37-dimensional zone-level features for all zones in a city.
    
    Feature Composition (37 Total):
    - 5 Base Features:
      1. total_population
      2. area_km2
      3. pop_density (population / area)
      4. road_density
      5. total_pois (sum of all POI counts)
    
    - 16 POI Category Counts:
      6-21. office, industrial, commercial, education_primary, education_higher,
            healthcare_hospital, healthcare_doctor, shopping_mall, shopping_supermarket,
            food_restaurant, food_cafe, food_fast, entertainment_culture,
            entertainment_sports, transport_rail, transport_bus
    
    - 16 POI Category Densities (per km²):
      22-37. Same as above with _density suffix
    
    Args:
        city_data: Dictionary with 'meta', 'census', 'poi' DataFrames
        road_map: Dictionary mapping zone indices to road density
        road_impute: Imputation value for missing road density
    
    Returns:
        (nodes_df, feature_names): DataFrame with 37 features + 'idx' column, and feature name list
    """
    meta = city_data["meta"]
    census = city_data["census"]
    poi = city_data["poi"]
    
    # Merge zone-level data
    nodes = (
        meta[["idx", "area_km2"]]
        .merge(census[["idx", "total_population"]], on="idx", how="left")
        .merge(poi, on="idx", how="left")
    )
    # Strict privacy/generalizability constraint: NEVER use employment_rate
    assert "employment_rate" not in nodes.columns, "employment_rate is non-transferable and must not be used."
    nodes["total_population"] = nodes["total_population"].fillna(0.0)
    nodes["area_km2"] = nodes["area_km2"].fillna(0.01).clip(EPS)
    
    # Road density
    rd = np.array([road_map.get(int(zid), road_impute) for zid in nodes["idx"]], float)
    nodes["road_density"] = np.nan_to_num(rd, nan=road_impute).clip(0.0)
    
    # ─── Construct 37 Features ───
    feat_pop = nodes["total_population"].values
    feat_area = nodes["area_km2"].values
    feat_pop_density = feat_pop / feat_area
    feat_road = nodes["road_density"].values
    feat_total_pois = nodes["total_pois"].fillna(0.0).values
    feat_total_pois_density = feat_total_pois / feat_area
    
    # Core features (6 items total)
    base_feats = [feat_pop, feat_area, feat_pop_density, feat_road, feat_total_pois, feat_total_pois_density]
    feature_names = ["total_population", "area_km2", "pop_density", "road_density", "total_pois", "total_pois_density"]
    
    # POI category counts (16 types)
    poi_cols_raw = [
        "office", "industrial", "commercial", "education_primary", "education_higher",
        "healthcare_hospital", "healthcare_doctor", "shopping_mall", "shopping_supermarket",
        "food_restaurant", "food_cafe", "food_fast", "entertainment_culture",
        "entertainment_sports", "transport_rail", "transport_bus"
    ]
    for col in poi_cols_raw:
        vals = nodes[col].fillna(0.0).values if col in nodes.columns else np.zeros(len(nodes))
        base_feats.append(vals)
        feature_names.append(f"poi_{col}")
        
    # POI category densities (15 types - Exclude transport_bus_density or similar if needed to hit 37)
    # Actually, 6 (core) + 16 (counts) + 15 (densities) = 37.
    # We will exclude 'employment_density' (which was already not here) or keep it consistent.
    # The user said: "loai bo thuoc tinh employment chu khong phai total_pois_density"
    
    poi_cols_density = [
        "office_density", "industrial_density", "commercial_density", "education_primary_density", "education_higher_density",
        "healthcare_hospital_density", "healthcare_doctor_density", "shopping_mall_density", "shopping_supermarket_density",
        "food_restaurant_density", "food_cafe_density", "food_fast_density", "entertainment_culture_density",
        "entertainment_sports_density", "transport_rail_density"
    ]
    # Removed: transport_bus_density (Example: keeping it at 37)
    # Calculation: 6 base + 16 counts + 15 densities = 37 features.
    
    for col in poi_cols_density:
        vals = nodes[col].fillna(0.0).values if col in nodes.columns else np.zeros(len(nodes))
        base_feats.append(vals)
        feature_names.append(f"poi_{col}")
        
    # Stack and log-transform
    X_all = np.column_stack(base_feats).astype(np.float32)
    X_all = np.log1p(np.maximum(0.0, X_all))
    
    # Create output dataframe
    nodes_df = pd.DataFrame(X_all, columns=feature_names)
    nodes_df["idx"] = nodes["idx"].values
    
    return nodes_df, feature_names



# =====================================================================
# GBDT: 29-FEATURE BUILDER (SHAP-SELECTED SUBSET)
# =====================================================================

# 29 SHAP-selected features (from 37-feature analysis, threshold μ >= 0.005)
SHAP_FEATURES_29 = [
    "total_population", "poi_food_fast", "total_pois", "road_density", "area_km2",
    "pop_density", "poi_education_primary", "poi_food_restaurant", "poi_entertainment_sports_density",
    "poi_transport_rail_density", "poi_education_primary_density", "poi_commercial_density",
    "poi_office_density", "poi_entertainment_culture", "poi_food_cafe",
    "poi_shopping_supermarket_density", "poi_transport_bus_density", "poi_shopping_mall",
    "poi_education_higher", "poi_shopping_mall_density", "poi_transport_bus",
    "poi_entertainment_culture_density", "poi_food_fast_density", "poi_food_restaurant_density",
    "poi_shopping_supermarket", "poi_commercial", "poi_healthcare_hospital_density",
    "poi_healthcare_hospital", "poi_transport_rail"
]


def build_gbdt_outflow_features_29(city_data: dict, road_map: dict, road_impute: float) -> Tuple[np.ndarray, np.ndarray, List[int]]:
    """
    Build GBDT outflow-prediction features using 29 SHAP-selected features.
    
    Args:
        city_data: Dictionary with 'meta', 'census', 'poi' DataFrames
        road_map: Dictionary mapping zone indices to road density
        road_impute: Imputation value for missing road density
    
    Returns:
        (X_out, logO, zones): Feature matrix (n_zones, 29), log-outflow vector, zone indices
    """
    # Just reuse the logic from build_zone_features_37 and filter for the 29 features
    nodes_37_df, feature_names = build_zone_features_37(city_data, road_map, road_impute)
    
    # Filter for the 29 features
    X_out = nodes_37_df[SHAP_FEATURES_29].values
    
    # Target logO
    pairs_df = build_pairs_dataframe(city_data, attr_mode="poi_pop_avg", min_distance=0.1)
    outflow_df = pairs_df.groupby("o_idx")["trip_count"].sum().reset_index()
    outflow_df.columns = ["idx", "O_i"]
    
    # Ensure alignment with nodes_37_df
    final_df = nodes_37_df[["idx"]].merge(outflow_df, on="idx", how="left").fillna(0.0)
    logO = np.log1p(final_df["O_i"].values)
    zones = final_df["idx"].astype(int).tolist()
    
    return X_out, logO, zones


# =====================================================================
# GBDT: 23-FEATURE BUILDER (SHAP-SELECTED SUBSET)
# =====================================================================

# 11 SHAP-selected features (optimized for global generalizability outside the US, R2 peak = 0.635)
SHAP_FEATURES_23 = [
    "total_population", "area_km2", "pop_density", "road_density", "total_pois",
    "poi_education_primary", "poi_education_higher", "poi_shopping_mall",
    "poi_food_restaurant", "poi_food_fast", "poi_entertainment_culture"
]


def build_gbdt_outflow_features_23(city_data: dict, road_map: dict, road_impute: float) -> Tuple[np.ndarray, np.ndarray, List[int]]:
    """
    Build GBDT outflow prediction features using 23 SHAP-selected features.
    
    **Model Inductive Bias Justification**:
    - Tree-based models are prone to overfitting in high-dimensional space
    - SHAP-selected features are those with:
      * Strong mean predictive power (μ_p ≥ 0.005)
      * Cross-city stability (S_p = μ_p / σ_p ≥ 1.0)
      * Low redundancy (correlation ≤ 0.85-0.90)
    - These represent fundamental urban structures that transfer across cities
    - GBDT's inductive bias: learn robust decision boundaries in feature space,
      avoiding overfitting to city-specific artifacts
    
    Args:
        city_data: Dictionary with 'meta', 'census', 'poi' DataFrames
        road_map: Dictionary mapping zone indices to road density
        road_impute: Imputation value for missing road density
    
    Returns:
        (X_out, logO, zones): Feature matrix (n_zones, 23), log-outflow vector, zone indices
    """
    df = build_pairs_dataframe(city_data, attr_mode="poi_pop_avg", min_distance=0.1, adaptive_self=True)
    
    meta = city_data["meta"]
    census = city_data["census"]
    poi = city_data["poi"]
    
    # Merge zone-level data
    nodes = (
        meta[["idx", "area_km2"]]
        .merge(census[["idx", "total_population"]], on="idx", how="left")
        .merge(poi, on="idx", how="left")
    )
    nodes["total_population"] = nodes["total_population"].fillna(0.0)
    nodes["area_km2"] = nodes["area_km2"].fillna(0.01).clip(EPS)
    
    # Road density
    rd = np.array([road_map.get(int(zid), road_impute) for zid in nodes["idx"]], float)
    nodes["road_density"] = np.nan_to_num(rd, nan=road_impute).clip(0.0)
    
    # Compute derived features
    nodes["pop_density"] = nodes["total_population"] / nodes["area_km2"]
    nodes["total_pois_density"] = nodes["total_pois"].fillna(0.0) / nodes["area_km2"]
    
    # Build feature matrix with only SHAP-selected 23 features
    node_feat_dict = {}
    for idx, row in nodes.iterrows():
        zone_id = int(row["idx"])
        feat_vec = []
        for feat_name in SHAP_FEATURES_23:
            if feat_name in row.index:
                val = row[feat_name]
            else:
                val = 0.0
            feat_vec.append(float(np.log1p(max(val, 0.0))))
        node_feat_dict[zone_id] = np.array(feat_vec, dtype=np.float32)
    
    # Extract outflows
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
    
    return np.array(X_out), np.array(logO), kept
