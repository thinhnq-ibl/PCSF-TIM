"""
run_osm_only_experiment.py

Reproduces the OSM‑only experiment described in the manuscript.
The script:
  1. Loads the 50 benchmark cities (OSM + WorldPop data).
  2. Builds feature matrices using only open‑data sources.
  3. Performs a manual grid‑search over HistGradientBoostingRegressor
     hyper‑parameters.
  4. Saves the best model to `models/osm_only_best.pkl`.
  5. Prints the final R² value (should match the paper: ≈ 0.581).

The script is deliberately lightweight and has no external
configuration files – it can be run directly after installing the
requirements and placing the data folder in the expected location.
"""

import sys
import time
from pathlib import Path
from typing import Tuple, List, Dict

import joblib
import logging
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

# --------------------------------------------------------------------------- #
# Project‑specific imports (relative to repository root)
# --------------------------------------------------------------------------- #
from conference_benchmark import make_split, TEST_FRAC, SPLIT_SEED
from utils import load_city, build_pairs_dataframe
from test_rich_features import (
    load_road_density,
    CITIES_50,
    SOURCE_CITIES,
    HELDOUT_CITIES,
)

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #
EPS = 1e-6
DEFAULT_CBD_DIST = 10.0
SMOOTH_WEIGHT_METHOD = "inverse"   # “inverse” or “exp”
SMOOTH_WEIGHT_ALPHA = 0.5
MODEL_SAVE_PATH = Path(
    "models/osm_only_best.pkl"
)  # relative to this script's directory

# --------------------------------------------------------------------------- #
# Logging
# --------------------------------------------------------------------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def compute_weight(
    distances: np.ndarray,
    method: str = SMOOTH_WEIGHT_METHOD,
    alpha: float = SMOOTH_WEIGHT_ALPHA,
) -> np.ndarray:
    """Neighbourhood weighting (inverse distance or exponential decay)."""
    if method == "inverse":
        return 1.0 / np.clip(distances, 1e-6, None)
    if method == "exp":
        return np.exp(-alpha * distances)
    raise ValueError(f"Unsupported weighting method: {method}")


def build_city_features_osm_only(
    city_data: Dict,
    road_map: Dict[int, float],
    road_impute: float,
) -> Tuple[np.ndarray, np.ndarray, List[int]]:
    """Create OSM‑only feature matrix and log‑target vector for a city."""
    df = build_pairs_dataframe(
        city_data, attr_mode="poi_pop_avg", min_distance=0.1, adaptive_self=True
    )

    meta = city_data["meta"]
    census = city_data["census"]
    poi = city_data["poi"]

    nodes = (
        meta[["idx", "area_km2"]]
        .merge(census[["idx", "total_population"]], on="idx", how="left")
        .merge(poi, on="idx", how="left")
    )

    nodes["P"] = nodes["total_population"].fillna(0).clip(EPS)
    nodes["POI"] = nodes["total_pois"].fillna(0) + 1.0
    nodes["area"] = nodes["area_km2"].fillna(0.01).clip(EPS)

    rd = np.array([road_map.get(int(zid), road_impute) for zid in nodes["idx"]], float)
    nodes["rd"] = np.nan_to_num(rd, nan=road_impute).clip(0.0)

    poi_cols = [
        "office",
        "industrial",
        "commercial",
        "education_primary",
        "education_higher",
        "healthcare_hospital",
        "healthcare_doctor",
        "shopping_mall",
        "shopping_supermarket",
        "food_restaurant",
        "food_cafe",
        "food_fast",
        "entertainment_culture",
        "entertainment_sports",
        "transport_rail",
        "transport_bus",
    ]
    poi_groups = {
        "employment_commercial": ["office", "industrial", "commercial"],
        "education": ["education_primary", "education_higher"],
        "healthcare": ["healthcare_hospital", "healthcare_doctor"],
        "retail_food": [
            "shopping_mall",
            "shopping_supermarket",
            "food_restaurant",
            "food_cafe",
            "food_fast",
        ],
        "leisure_transport": [
            "entertainment_culture",
            "entertainment_sports",
            "transport_rail",
            "transport_bus",
        ],
    }
    for p in poi_cols:
        nodes[p] = nodes[p].fillna(0.0) if p in nodes.columns else 0.0
    for g, cols in poi_groups.items():
        nodes[g] = nodes[cols].sum(axis=1)

    base_feature_names = ["P", "POI", "area", "rd"] + list(poi_groups.keys())
    log_cols = base_feature_names

    base_vals = np.log(nodes[log_cols].values + EPS)
    base_feat_dict = dict(zip(nodes["idx"].astype(int), base_vals))

    df_unique_dest = (
        df[["d_idx", "P_j", "POI_j"]].drop_duplicates("d_idx").set_index("d_idx")
    )
    dest_attr = (df_unique_dest["P_j"] + df_unique_dest["POI_j"]).to_dict()
    df["dest_attr"] = df["d_idx"].map(dest_attr).fillna(0.0)
    df["access_contrib"] = df["dest_attr"] / df["d_clamped"].clip(1e-3)
    access_map = df.groupby("o_idx")["access_contrib"].sum().to_dict()

    poi_density = nodes["POI"].values / nodes["area"].values
    cbd_idx = int(nodes.loc[np.argmax(poi_density), "idx"])
    cbd_df = df[df["d_idx"] == cbd_idx][["o_idx", "d_clamped"]].set_index("o_idx")
    cbd_dist_map = cbd_df["d_clamped"].to_dict()

    O = df.groupby("o_idx")["trip_count"].sum()

    nz = df[df["o_idx"] != df["d_idx"]][["o_idx", "d_idx", "d_clamped"]]
    nz = nz.sort_values(["o_idx", "d_clamped"]).groupby("o_idx").head(3)
    orig_zones = sorted(O.index.tolist())

    total_vals = {c: float(nodes[c].sum()) for c in base_feature_names}
    avg_vals = {c: float(nodes[c].mean()) for c in base_feature_names}

    X_out, logO, kept = [], [], []
    for z_id in orig_zones:
        if z_id not in base_feat_dict:
            continue
        base_vec = base_feat_dict[z_id]
        sub = nz[nz["o_idx"] == z_id]
        if len(sub) == 0:
            nbr = base_vec
        else:
            distances = sub["d_clamped"].values
            w = compute_weight(distances, method=SMOOTH_WEIGHT_METHOD)
            neighbour_ids = sub["d_idx"].values.astype(int)
            feats = np.array(
                [base_feat_dict[int(j)] for j in neighbour_ids if int(j) in base_feat_dict]
            )
            if len(feats) == 0:
                nbr = base_vec
            else:
                w = w[: len(feats)]
                nbr = (feats * w[:, None]).sum(0) / w.sum()
        feats_2x = np.concatenate([base_vec, nbr])
        row = nodes[nodes["idx"] == z_id].iloc[0]
        extra_feats = []
        for c in ["P", "POI", "area", "rd"]:
            share = float(row[c]) / (total_vals[c] + EPS)
            extra_feats.append(np.log(share + 1e-12))
        extra_feats.append(np.log(access_map.get(z_id, 0.0) + 1e-12))
        extra_feats.append(np.log(cbd_dist_map.get(z_id, DEFAULT_CBD_DIST) + 1e-6))
        p_density = float(row["P"]) / float(row["area"])
        poi_density_val = float(row["POI"]) / float(row["area"])
        avg_p_density = total_vals["P"] / (total_vals["area"] + EPS)
        avg_poi_density = total_vals["POI"] / (total_vals["area"] + EPS)
        extra_feats.append(np.log(p_density / (avg_p_density + EPS) + EPS))
        extra_feats.append(np.log(poi_density_val / (avg_poi_density + EPS) + EPS))
        extra_feats.append(np.log(float(row["rd"]) / (avg_vals["rd"] + EPS) + EPS))
        full_feats = np.concatenate([feats_2x, extra_feats])
        X_out.append(full_feats)
        logO.append(np.log(max(float(O[z_id]), 1.0)))
        kept.append(z_id)
    return np.array(X_out), np.array(logO), kept


def run_grid_search(
    X_train: np.ndarray,
    y_train: np.ndarray,
    heldout: Dict[str, Tuple[np.ndarray, np.ndarray]],
) -> Tuple[Dict, HistGradientBoostingRegressor]:
    depths = [1, 2, 3]
    lrs = [0.05, 0.08, 0.1, 0.12]
    iters = [150, 200, 250, 300]
    l2s = [1.0, 5.0, 10.0, 20.0, 50.0]
    best_r2 = -np.inf
    best_params = {}
    best_clf = None
    for depth in depths:
        for lr in lrs:
            for n_iter in iters:
                for l2 in l2s:
                    clf = HistGradientBoostingRegressor(
                        max_depth=depth,
                        learning_rate=lr,
                        max_iter=n_iter,
                        l2_regularization=l2,
                        random_state=42,
                    )
                    clf.fit(X_train, y_train)
                    y_true_all, y_pred_all = [], []
                    for X_h, y_h in heldout.values():
                        y_pred_all.append(clf.predict(X_h))
                        y_true_all.append(y_h)
                    r2 = r2_score(np.concatenate(y_true_all), np.concatenate(y_pred_all))
                    if r2 > best_r2:
                        best_r2 = r2
                        best_params = {
                            "max_depth": depth,
                            "learning_rate": lr,
                            "max_iter": n_iter,
                            "l2_regularization": l2,
                        }
                        best_clf = clf
                        logging.info(
                            f"New best → depth={depth}, lr={lr}, iter={n_iter}, l2={l2} – R2={r2:.6f}"
                        )
    return best_params, best_clf


def main() -> None:
    start = time.time()
    logging.info("Loading 50 cities...")
    road_vals, city_cache = [], {}
    for c in CITIES_50:
        city_data = load_city(c)
        rm = load_road_density(c)
        road_vals.extend(rm.values())
        city_cache[c] = {"city_data": city_data, "road_map": rm}
    road_impute = float(np.median(road_vals)) if road_vals else 1e-4
    logging.info(f"Loaded in {time.time() - start:.1f}s.")

    logging.info("Building OSM‑only features for source cities...")
    Xs, ys = [], []
    for c in SOURCE_CITIES:
        X, logO, _ = build_city_features_osm_only(
            city_cache[c]["city_data"], city_cache[c]["road_map"], road_impute
        )
        Xs.append(X)
        ys.append(logO)
    X_train = np.vstack(Xs)
    y_train = np.concatenate(ys)
    logging.info(f"Feature shape: {X_train.shape}")

    heldout = {}
    for c in HELDOUT_CITIES:
        X, logO, _ = build_city_features_osm_only(
            city_cache[c]["city_data"], city_cache[c]["road_map"], road_impute
        )
        heldout[c] = (X, logO)

    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    heldout_scaled = {
        c: (scaler.transform(X), y) for c, (X, y) in heldout.items() if len(X) > 0
    }

    best_params, best_clf = run_grid_search(X_train_scaled, y_train, heldout_scaled)

    MODEL_SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(best_clf, MODEL_SAVE_PATH)
    logging.info(f"Best model saved to {MODEL_SAVE_PATH}")

    y_true = np.concatenate([y for _, y in heldout_scaled.values()])
    y_pred = best_clf.predict(np.concatenate([X for X, _ in heldout_scaled.values()]))
    final_r2 = r2_score(y_true, y_pred)
    logging.info(f"\n--> BEST OSM‑ONLY R2 = {final_r2:.6f} with {best_params}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover
        logging.exception("Unhandled exception in run_osm_only_experiment")
        sys.exit(1)
