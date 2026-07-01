"""
Conference Benchmark Helper
===========================
Implements make_split, cpc, apply_origin_normalization, and cities lists.
"""

import numpy as np
import pandas as pd
from typing import Tuple, List

TEST_FRAC = 0.20
SPLIT_SEED = 42

FULL_CITIES = [
    "Albuquerque", "Arlington", "Atlanta", "Austin", "Baltimore", "Boston",
    "Charlotte", "Chicago", "Colorado_Springs", "Columbus", "Dallas", "Denver",
    "Detroit", "El_Paso", "Fort_Worth", "Fresno", "Houston", "Indianapolis",
    "Jacksonville", "Kansas_City", "Las_Vegas", "Long_Beach", "Los_Angeles",
    "Louisville", "Memphis", "Mesa", "Miami", "Milwaukee", "Minneapolis",
    "Nashville", "New_York", "Oakland", "Oklahoma_City", "Omaha", "Philadelphia",
    "Phoenix", "Portland", "Raleigh", "Sacramento", "San_Antonio", "San_Diego",
    "San_Francisco", "San_Jose", "Seattle", "Tampa", "Tucson", "Tulsa",
    "Virginia_Beach", "Washington_DC", "Wichita"
]

def make_split(df: pd.DataFrame, seed: int = 42, test_frac: float = 0.2) -> Tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    n = len(df)
    shuffled_idx = rng.permutation(n)
    test_size = int(n * test_frac)
    test_idx = shuffled_idx[:test_size]
    
    train_mask = np.ones(n, dtype=bool)
    train_mask[test_idx] = False
    test_mask = np.zeros(n, dtype=bool)
    test_mask[test_idx] = True
    return train_mask, test_mask

def cpc(pred: np.ndarray, actual: np.ndarray) -> float:
    pred = np.asarray(pred, dtype=float)
    actual = np.asarray(actual, dtype=float)
    s = pred.sum() + actual.sum()
    if s < 1e-9:
        return 0.0
    return float(2.0 * np.minimum(pred, actual).sum() / s)

def apply_origin_normalization(df: pd.DataFrame, T_pred: np.ndarray) -> np.ndarray:
    tmp = df[["o_idx", "O_i"]].copy()
    tmp["T_pred"] = T_pred
    sum_pred = tmp.groupby("o_idx")["T_pred"].transform("sum")
    scale = tmp["O_i"] / np.maximum(sum_pred, 1e-9)
    return T_pred * scale.values

def _fit_pe_bin50_train(df):
    # Dummy placeholder for _fit_pe_bin50_train if needed
    return 1.0, 0.05
