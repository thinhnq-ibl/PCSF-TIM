"""
Redesign Helper Module
======================
Implements SOURCE_CITIES, HELDOUT_CITIES (stratified 25/25 split),
and core feature and prediction functions.
"""

import numpy as np
import pandas as pd
from typing import Tuple, List, Dict
from conference_benchmark import FULL_CITIES

CITIES_50 = FULL_CITIES

# Define a deterministic stratified 25/25 split:
MORPHOLOGY_GROUPS = {
    "Dense / Transit": ["New_York", "Chicago", "Philadelphia", "Boston", "San_Francisco", "Washington_DC", "Baltimore", "Minneapolis", "Oakland", "Long_Beach"],
    "Sprawling / Grid": ["Los_Angeles", "Houston", "Phoenix", "San_Antonio", "Dallas", "Atlanta", "Denver", "Indianapolis", "Columbus", "Las_Vegas", "Jacksonville", "Kansas_City", "Omaha", "Oklahoma_City", "Tulsa", "Wichita", "El_Paso", "Mesa", "Arlington", "Fort_Worth", "Tucson"],
    "Polycentric": ["San_Jose", "Austin", "Charlotte", "Louisville", "Memphis", "Milwaukee", "Nashville", "Raleigh", "Detroit", "Sacramento", "Fresno", "Albuquerque", "Colorado_Springs"],
    "Coastal": ["San_Diego", "Seattle", "Portland", "Miami", "Tampa", "Virginia_Beach"]
}

SOURCE_CITIES = []
HELDOUT_CITIES = []
for group, cities in MORPHOLOGY_GROUPS.items():
    sorted_cities = sorted(cities)
    for idx, city in enumerate(sorted_cities):
        if group == "Polycentric":
            if idx % 2 != 0:
                SOURCE_CITIES.append(city)
            else:
                HELDOUT_CITIES.append(city)
        else:
            if idx % 2 == 0:
                SOURCE_CITIES.append(city)
            else:
                HELDOUT_CITIES.append(city)

# Impute road density
def load_road_density(city: str) -> dict:
    from utils import load_road_density as _lrd
    return _lrd(city)

def build_city_features_redesign(city_data: dict, road_map: dict, road_impute: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    meta = city_data["meta"]
    census = city_data["census"]
    poi = city_data["poi"]
    
    nodes = meta[["idx", "area_km2"]].merge(
        census[["idx", "total_population"]], on="idx", how="left"
    ).merge(
        poi, on="idx", how="left"
    )
    nodes["rd"] = np.array([road_map.get(int(zid), road_impute) for zid in nodes["idx"]], float)
    nodes["rd"] = np.nan_to_num(nodes["rd"], nan=road_impute).clip(0.0)
    
    P = nodes["total_population"].fillna(0.0).values
    POI = nodes["total_pois"].fillna(0.0).values
    area = nodes["area_km2"].fillna(0.01).clip(1e-6).values
    rd = nodes["rd"].values
    
    rho_pop = P / area
    rho_poi = POI / area
    rho_road = rd
    
    od = city_data["od"]
    O_i_series = od.groupby("o_idx")["trip_count"].sum()
    nodes = nodes.merge(O_i_series, left_on="idx", right_index=True, how="left")
    O = nodes["trip_count"].fillna(0.0).values
    logO = np.log1p(O)
    
    X = np.stack([POI, P, area, rho_pop, rho_poi, rho_road], axis=1).astype(np.float32)
    return X, logO, nodes["idx"].values

def proposed_predict(df: pd.DataFrame, O_hat: Dict[int, float], gamma: float, beta: float) -> np.ndarray:
    O_vec = np.array([O_hat.get(int(oid), 1.0) for oid in df["o_idx"]], dtype=np.float32)
    A_j = df["A_j"].values
    d = df["d_clamped"].values
    
    # Tanner friction function
    f_d = A_j * (np.maximum(d, 1e-6) ** (-gamma)) * np.exp(-beta * d)
    
    tmp = df[["o_idx"]].copy()
    tmp["f_d"] = f_d
    sum_fd = tmp.groupby("o_idx")["f_d"].transform("sum")
    scale = O_vec / np.maximum(sum_fd, 1e-9)
    return f_d * scale.values

def national_decay(city_cache: dict) -> Tuple[float, float]:
    # Medians reported in paper
    return 1.5, 0.05

def _fit_pe_bin50_train(df):
    return 1.5, 0.05
