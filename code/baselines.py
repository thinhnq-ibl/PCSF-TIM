"""Baseline transportation models.

All models take a pre-built `df` from utils.build_pairs_dataframe and return
predicted flow vector (length = len(df)) aligned with df.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar, minimize
from utils import apply_origin_normalization


# ===================== HELPER =====================

def _fit_param(loss_fn, x0, bounds, method="Nelder-Mead"):
    """Optimize a single parameter via scalar minimize."""
    res = minimize_scalar(loss_fn, bounds=bounds, method="bounded",
                          options={"xatol": 1e-4})
    return res.x


def _log_mse(pred, actual):
    return np.sum((np.log1p(pred) - np.log1p(actual)) ** 2)


def gravity_power_unconstrained(df: pd.DataFrame) -> tuple[np.ndarray, dict]:
    """T_ij = k * O_i^alpha * A_j^beta * d_ij^(-gamma), k normalized, alpha, beta, gamma free."""
    O_i = df["O_i"].values
    A_j = df["A_j"].values
    d = df["d_clamped"].values
    actual = df["trip_count"].values
    total_actual = np.sum(actual)

    def loss(params):
        alpha, beta, gamma = params
        O_pow = np.power(np.maximum(O_i, 1e-9), alpha)
        A_pow = np.power(np.maximum(A_j, 1e-9), beta)
        d_pow = np.power(np.maximum(d, 1e-9), -gamma)
        T_raw = O_pow * A_pow * d_pow
        sum_raw = np.sum(T_raw)
        if sum_raw == 0:
            return 1e18
        T = T_raw * (total_actual / sum_raw)
        return float(np.sum((np.log1p(T) - np.log1p(actual)) ** 2))

    res = minimize(loss, x0=[1.0, 1.0, 1.5], bounds=[(0.01, 3.0), (0.01, 3.0), (0.01, 5.0)], method="L-BFGS-B")
    alpha, beta, gamma = res.x
    O_pow = np.power(O_i, alpha)
    A_pow = np.power(A_j, beta)
    d_pow = np.power(d, -gamma)
    T_raw = O_pow * A_pow * d_pow
    pred = T_raw * (total_actual / np.sum(T_raw))
    return pred, {"model": "Gravity_Power_Unconstrained", "alpha": float(alpha), "beta": float(beta), "gamma": float(gamma)}


def gravity_exp_unconstrained(df: pd.DataFrame) -> tuple[np.ndarray, dict]:
    """T_ij = k * O_i^alpha * A_j^beta * exp(-beta_dist * d_ij), k normalized, alpha, beta, beta_dist free."""
    O_i = df["O_i"].values
    A_j = df["A_j"].values
    d = df["d_clamped"].values
    actual = df["trip_count"].values
    total_actual = np.sum(actual)

    def loss(params):
        alpha, beta, beta_dist = params
        O_pow = np.power(np.maximum(O_i, 1e-9), alpha)
        A_pow = np.power(np.maximum(A_j, 1e-9), beta)
        exp_dist = np.exp(-np.clip(beta_dist * d, 0, 700))
        T_raw = O_pow * A_pow * exp_dist
        sum_raw = np.sum(T_raw)
        if sum_raw == 0:
            return 1e18
        T = T_raw * (total_actual / sum_raw)
        return float(np.sum((np.log1p(T) - np.log1p(actual)) ** 2))

    res = minimize(loss, x0=[1.0, 1.0, 0.1], bounds=[(0.01, 3.0), (0.01, 3.0), (0.001, 5.0)], method="L-BFGS-B")
    alpha, beta, beta_dist = res.x
    O_pow = np.power(O_i, alpha)
    A_pow = np.power(A_j, beta)
    exp_dist = np.exp(-beta_dist * d)
    T_raw = O_pow * A_pow * exp_dist
    pred = T_raw * (total_actual / np.sum(T_raw))
    return pred, {"model": "Gravity_Exp_Unconstrained", "alpha": float(alpha), "beta": float(beta), "beta_dist": float(beta_dist)}



# ===================== CONSTRAINED GRAVITY =====================

def gravity_power_constrained(df: pd.DataFrame) -> tuple[np.ndarray, dict]:
    """Production-constrained: T_ij = K_i * O_i * A_j * d^(-α), Σ_j T_ij = O_i."""
    A_j = df["A_j"].values
    d = df["d_clamped"].values
    actual = df["trip_count"].values

    def predict(alpha):
        T = df["O_i"].values * A_j * d ** (-alpha)
        return apply_origin_normalization(df, T)

    def loss(alpha):
        return _log_mse(predict(alpha), actual)

    alpha = _fit_param(loss, 0.5, (0.01, 3.0))
    return predict(alpha), {"model": "Gravity_Power_Constrained", "alpha": float(alpha)}


def gravity_exp_constrained(df: pd.DataFrame) -> tuple[np.ndarray, dict]:
    """Production-constrained exp gravity."""
    A_j = df["A_j"].values
    d = df["d_clamped"].values
    actual = df["trip_count"].values

    def predict(beta):
        T = df["O_i"].values * A_j * np.exp(-beta * d)
        return apply_origin_normalization(df, T)

    def loss(beta):
        return _log_mse(predict(beta), actual)

    beta = _fit_param(loss, 0.1, (0.001, 2.0))
    return predict(beta), {"model": "Gravity_Exp_Constrained", "beta": float(beta)}


# ===================== RADIATION =====================

def _compute_s_ij(df: pd.DataFrame, mass_col: str) -> np.ndarray:
    """For each (i,j) pair, compute s_ij = sum of mass in circle of radius d_ij
    centered at i, EXCLUDING i and j.

    Implementation: for each pair, find all nodes k with d_ik <= d_ij, k != i, k != j.
    Approach: build per-origin distance vector once.
    """
    # Build mass dict (idx -> mass)
    o_meta = df[["o_idx", "P_i", "POI_i"]].drop_duplicates("o_idx").set_index("o_idx")
    d_meta = df[["d_idx", "P_j", "POI_j"]].drop_duplicates("d_idx").set_index("d_idx")
    # Combine into single node mass
    all_nodes = sorted(set(df["o_idx"]).union(set(df["d_idx"])))
    masses = {}
    for idx in all_nodes:
        if idx in o_meta.index:
            masses[idx] = o_meta.loc[idx, mass_col.replace("_j", "_i")]
        elif idx in d_meta.index:
            masses[idx] = d_meta.loc[idx, mass_col]
        else:
            masses[idx] = 0.0

    # For each origin, get all (d_idx, distance) pairs sorted by distance, with cumulative mass
    s_ij = np.zeros(len(df))
    df_idx = df.index.values
    o_arr = df["o_idx"].values
    j_arr = df["d_idx"].values
    d_arr = df["d_clamped"].values

    # Group by origin: sorted distance and cumulative mass
    from collections import defaultdict
    by_origin: dict = defaultdict(list)
    for k in range(len(df)):
        by_origin[o_arr[k]].append((d_arr[k], j_arr[k], k))

    for o, items in by_origin.items():
        items.sort(key=lambda x: x[0])
        ds = np.array([it[0] for it in items])
        js = np.array([it[1] for it in items])
        ks = np.array([it[2] for it in items])
        mass_o = masses.get(o, 0.0)
        ms = np.array([masses.get(jj, 0.0) for jj in js])
        # cumulative mass up to and including this index
        cum = np.cumsum(ms)
        # For each item, s_ij = cum_mass(d <= d_ij) - mass_o - mass_j
        # cum already includes mass_j at this position; exclude j
        # also exclude origin (mass_o)
        # Note: cum includes positions with same d (ties); approximate
        s_vals = cum - mass_o - ms
        s_vals = np.maximum(s_vals, 0.0)
        for kk, sv in zip(ks, s_vals):
            s_ij[kk] = sv

    return s_ij


def radiation_population(df: pd.DataFrame) -> tuple[np.ndarray, dict]:
    """T_ij = O_i * (P_i * P_j) / ((P_i + s_ij)(P_i + P_j + s_ij))"""
    P_i = df["P_i"].values
    P_j = df["P_j"].values
    O_i = df["O_i"].values
    s_ij = _compute_s_ij(df, "P_j")
    denom = (P_i + s_ij) * (P_i + P_j + s_ij)
    denom = np.maximum(denom, 1e-9)
    pred = O_i * (P_i * P_j) / denom
    # Radiation is naturally production-constrained-ish; normalize for fair compare
    pred = apply_origin_normalization(df, pred)
    return pred, {"model": "Radiation_Population"}


def radiation_poi(df: pd.DataFrame) -> tuple[np.ndarray, dict]:
    """Radiation with POI mass instead of population."""
    M_i = df["POI_i"].values
    M_j = df["POI_j"].values
    O_i = df["O_i"].values
    s_ij = _compute_s_ij(df, "POI_j")
    denom = (M_i + s_ij) * (M_i + M_j + s_ij)
    denom = np.maximum(denom, 1e-9)
    pred = O_i * (M_i * M_j) / denom
    pred = apply_origin_normalization(df, pred)
    return pred, {"model": "Radiation_POI"}


BASELINE_MODELS = [
    gravity_power_unconstrained,
    gravity_exp_unconstrained,
    gravity_power_constrained,
    gravity_exp_constrained,
    radiation_population,
    radiation_poi,
]
