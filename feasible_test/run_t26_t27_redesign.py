"""
T26 & T27 Redesign: Model-Based Cross-City Transfer Test
=========================================================
Redesigns the transferability test by performing proper cross-city
Random Forest model transfer instead of the invalid np.resize.

Evaluates 105 pairs (15 cities) under both:
  - Oracle beta (OD-MLE)
  - Clean 3-bin beta (TLD-MLE K=3)
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
import scipy.stats as stats
from sklearn.ensemble import RandomForestRegressor

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from utils_test import ALL_50_CITIES, process_city_data, fit_beta_od_mle, fit_beta_tld_mle, predict_gravity_od, calculate_cpc

def run_redesign():
    print("=" * 80)
    print("RUNNING T26 & T27 REDESIGN: MODEL-BASED CROSS-CITY TRANSFER (105 PAIRS)")
    print("=" * 80)
    
    cities = ALL_50_CITIES[:15]  # 15 cities -> 105 pairs
    
    city_vecs = {}
    city_coords = {}
    city_pops = {}
    city_nodes = {}
    city_dfs = {}
    
    # Coordinate dictionary for centroids
    coords_dict = {
        "Albuquerque": (35.0844, -106.6504), "Arlington": (32.7357, -97.1081),
        "Atlanta": (33.7490, -84.3880), "Austin": (30.2672, -97.7431),
        "Baltimore": (39.2904, -76.6122), "Boston": (42.3601, -71.0589),
        "Charlotte": (35.2271, -80.8431), "Chicago": (41.8781, -87.6298),
        "Colorado_Springs": (38.8339, -104.8214), "Columbus": (39.9612, -82.9988),
        "Dallas": (32.7767, -96.7970), "Denver": (39.7392, -104.9903),
        "Detroit": (42.3314, -83.0458), "El_Paso": (31.7619, -106.4850),
        "Fort_Worth": (32.7555, -97.3308)
    }
    
    print("Processing city data and features...")
    for c in cities:
        nodes, df = process_city_data(c)
        P = nodes["total_population"].values
        POI = nodes["total_pois"].values
        area = nodes["area_km2"].values
        road = nodes["road_density"].values
        
        # Macro structural vector for similarity
        vec = np.array([
            np.log(P.sum() + 1.0), np.log(POI.sum() + 1.0), np.log(area.sum() + 1e-4),
            np.log((P.sum() / area.sum()) + 1e-6), np.log((POI.sum() / area.sum()) + 1e-6),
            np.log(road.mean() + 1e-6)
        ])
        city_vecs[c] = vec
        city_coords[c] = coords_dict.get(c, (35.0, -95.0))
        city_pops[c] = P.sum()
        city_nodes[c] = nodes
        city_dfs[c] = df

    records_oracle_beta = []
    records_clean_beta = []
    
    print("Running cross-city transfers...")
    for i, ca in enumerate(cities):
        nodes_a = city_nodes[ca]
        
        # Build training dataset for City A
        P_a = nodes_a["total_population"].values
        POI_a = nodes_a["total_pois"].values
        area_a = nodes_a["area_km2"].values
        road_a = nodes_a["road_density"].values
        X_a = np.column_stack([
            np.log(P_a + 1.0), np.log(POI_a + 1.0), np.log(area_a + 1e-4),
            np.log((P_a / (area_a + 1e-4)) + 1e-6), np.log((POI_a / (area_a + 1e-4)) + 1e-6),
            np.log(road_a + 1e-6)
        ])
        y_O_a = np.log1p(nodes_a["O_i"].values)
        y_A_a = np.log1p(nodes_a["A_j"].values)
        
        # Train RF models on City A
        rf_O = RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
        rf_O.fit(X_a, y_O_a)
        rf_A = RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
        rf_A.fit(X_a, y_A_a)
        
        for j, cb in enumerate(cities):
            if i == j:
                continue
                
            nodes_b = city_nodes[cb]
            df_b = city_dfs[cb]
            actual_b = df_b["trip_count"].values.astype(float)
            
            # Predict capacities on City B using City A's trained model
            P_b = nodes_b["total_population"].values
            POI_b = nodes_b["total_pois"].values
            area_b = nodes_b["area_km2"].values
            road_b = nodes_b["road_density"].values
            X_b = np.column_stack([
                np.log(P_b + 1.0), np.log(POI_b + 1.0), np.log(area_b + 1e-4),
                np.log((P_b / (area_b + 1e-4)) + 1e-6), np.log((POI_b / (area_b + 1e-4)) + 1e-6),
                np.log(road_b + 1e-6)
            ])
            hat_O_b = np.maximum(np.expm1(rf_O.predict(X_b)), 0.0)
            hat_A_b = np.maximum(np.expm1(rf_A.predict(X_b)), 0.0)
            
            # Normalize to B total trips
            tot_trips_b = actual_b.sum()
            
            # Macro features for structural similarity
            va, vb = city_vecs[ca], city_vecs[cb]
            sim_struct = float(np.dot(va, vb) / (np.linalg.norm(va) * np.linalg.norm(vb)))
            
            # Geographic distance between centroids
            lat1, lon1 = city_coords[ca]
            lat2, lon2 = city_coords[cb]
            geo_dist = np.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2) * 111.0
            
            # Population difference
            pop_diff = abs(np.log(city_pops[ca] + 1.0) - np.log(city_pops[cb] + 1.0))
            
            # Run transfers for both oracle beta and clean beta
            for beta_func, records_list in [
                (lambda df: fit_beta_od_mle(df), records_oracle_beta),
                (lambda df: fit_beta_tld_mle(df, K=3), records_clean_beta)
            ]:
                beta_b = beta_func(df_b)
                T_ab = predict_gravity_od(df_b, beta_b, custom_O=hat_O_b, custom_A=hat_A_b, node_ids=nodes_b["idx"].values).astype(float)
                if T_ab.sum() > 0:
                    T_ab *= (tot_trips_b / T_ab.sum())
                cpc_ab = float(calculate_cpc(actual_b, T_ab))
                
                records_list.append({
                    "Source": ca, "Target": cb, "Structural_Sim": sim_struct,
                    "Geo_Dist_km": geo_dist, "Pop_Diff": pop_diff, "Transfer_CPC": cpc_ab
                })

    # Statistical Evaluation
    for label, rlist in [("ORACLE beta (leaked control)", records_oracle_beta), ("CLEAN 3-bin beta (survey-free)", records_clean_beta)]:
        df_pairs = pd.DataFrame(rlist)
        corr_s, p_s = stats.spearmanr(df_pairs["Structural_Sim"], df_pairs["Transfer_CPC"])
        corr_geo, p_geo = stats.spearmanr(df_pairs["Geo_Dist_km"], df_pairs["Transfer_CPC"])
        corr_pop, p_pop = stats.spearmanr(df_pairs["Pop_Diff"], df_pairs["Transfer_CPC"])
        
        # Run OLS Regression
        X = np.column_stack([np.ones(len(df_pairs)), df_pairs["Structural_Sim"], df_pairs["Geo_Dist_km"], df_pairs["Pop_Diff"]])
        y = df_pairs["Transfer_CPC"].values
        beta_ols, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
        
        print("\n" + "-" * 80)
        print(f"RESULTS FOR: {label}")
        print("-" * 80)
        print(f"  Mean Transfer CPC                            : {df_pairs['Transfer_CPC'].mean():.4f}")
        print(f"  Spearman rho(Structural_Sim, Transfer_CPC)   : {corr_s:.4f} (p-val: {p_s:.4e})")
        print(f"  Spearman rho(Geo_Dist_km, Transfer_CPC)      : {corr_geo:.4f} (p-val: {p_geo:.4e})")
        print(f"  Spearman rho(Pop_Diff, Transfer_CPC)          : {corr_pop:.4f} (p-val: {p_pop:.4e})")
        print("\nMULTIVARIABLE OLS COEFFICIENTS (CPC ~ Intercept + StructSim + GeoDist + PopDiff):")
        print(f"  Intercept            : {beta_ols[0]:.4f}")
        print(f"  Structural Similarity: {beta_ols[1]:.4f}")
        print(f"  Geographic Distance  : {beta_ols[2]:.6f}")
        print(f"  Population Diff      : {beta_ols[3]:.4f}")
        
    print("\n" + "=" * 80)
    print("T26 & T27 REDESIGN COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    run_redesign()
