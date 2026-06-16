"""My Model: Power × Exponential distance decay with multiple ablation options.

T_ij = O_i * A_j * f(d_ij)

where f(d) can be one of:
  - power_exp: d^(-α) * exp(-β·d)         (D2, default)
  - offset_power: (d + d0)^(-α) * exp(-β·d)  (D3)
  - stretched: d^(-α) * exp(-β·d^η)       (D5)

Options handled:
  A. normalize (origin balancing)
  E. fitting method: bin50_linear, bin50_log, direct, poisson_glm
  F. self-flow: clamp / adaptive (already in df), separate
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from scipy.optimize import minimize, minimize_scalar
from utils import apply_origin_normalization


def _decay(d: np.ndarray, params: dict, decay_form: str) -> np.ndarray:
    if decay_form == "power_exp":
        a, b = params["alpha"], params["beta"]
        return d ** (-a) * np.exp(-b * d)
    elif decay_form == "offset_power":
        a, b, d0 = params["alpha"], params["beta"], params["d0"]
        return (d + d0) ** (-a) * np.exp(-b * d)
    elif decay_form == "stretched":
        a, b, eta = params["alpha"], params["beta"], params["eta"]
        return d ** (-a) * np.exp(-b * d ** eta)
    elif decay_form == "gep":
        # Generalized Exponential Power: exp(-β · d^η)
        b, eta = params["beta"], params["eta"]
        return np.exp(-b * d ** eta)
    elif decay_form == "weighted_sum":
        # Linear combination: w · d^(-α) + (1-w) · exp(-β·d)
        w, a, b = params["w"], params["alpha"], params["beta"]
        w = min(max(w, 0.0), 1.0)
        return w * d ** (-a) + (1.0 - w) * np.exp(-b * d)
    raise ValueError(decay_form)


def _bin_stats(df: pd.DataFrame, n_bins: int = 50, log_spaced: bool = False):
    d = df["d_clamped"].values
    flow = df["trip_count"].values
    d_max = d.max()
    d_min = max(d.min(), 0.01)
    if log_spaced:
        edges = np.logspace(np.log10(d_min), np.log10(d_max), n_bins + 1)
    else:
        edges = np.linspace(0, d_max, n_bins + 1)
    bin_idx = np.digitize(d, edges) - 1
    bin_idx = np.clip(bin_idx, 0, n_bins - 1)
    out = pd.DataFrame({"bin": bin_idx, "d": d, "flow": flow})
    g = out.groupby("bin").agg(
        d_mid=("d", "mean"), flow_sum=("flow", "sum"), n=("flow", "size")
    ).reset_index()
    g = g[g["n"] > 0]
    return g


def _fit_bin(df: pd.DataFrame, decay_form: str, log_spaced: bool):
    g = _bin_stats(df, 50, log_spaced)
    d_mid = g["d_mid"].values
    flow_sum = g["flow_sum"].values
    n_bin = g["n"].values

    def predict_bin(params):
        f = _decay(d_mid, params, decay_form)
        return n_bin * f  # aggregate predicted flow magnitude

    def loss_for(arr):
        if decay_form == "power_exp":
            p = {"alpha": arr[0], "beta": arr[1]}
        elif decay_form == "offset_power":
            p = {"alpha": arr[0], "beta": arr[1], "d0": arr[2]}
        elif decay_form == "stretched":
            p = {"alpha": arr[0], "beta": arr[1], "eta": arr[2]}
        elif decay_form == "gep":
            p = {"beta": arr[0], "eta": arr[1]}
        elif decay_form == "weighted_sum":
            p = {"w": arr[0], "alpha": arr[1], "beta": arr[2]}
        pred = predict_bin(p)
        # log-MSE
        return np.sum((np.log1p(pred * (flow_sum.sum() / max(pred.sum(), 1e-9))) - np.log1p(flow_sum)) ** 2)

    if decay_form == "power_exp":
        x0 = [0.5, 0.1]; bnds = [(0.01, 3.0), (0.001, 2.0)]
    elif decay_form == "offset_power":
        x0 = [0.5, 0.1, 0.1]; bnds = [(0.01, 3.0), (0.0, 2.0), (0.01, 1.0)]
    elif decay_form == "stretched":
        x0 = [0.5, 0.1, 1.0]; bnds = [(0.01, 3.0), (0.001, 2.0), (0.3, 2.0)]
    elif decay_form == "gep":
        x0 = [0.5, 0.7]; bnds = [(0.001, 5.0), (0.1, 2.0)]
    elif decay_form == "weighted_sum":
        x0 = [0.5, 1.0, 0.1]; bnds = [(0.0, 1.0), (0.01, 3.0), (0.001, 2.0)]
    res = minimize(loss_for, x0, method="Nelder-Mead",
                   options={"xatol": 1e-4, "fatol": 1e-4, "maxiter": 500})
    arr = res.x
    if decay_form == "power_exp":
        return {"alpha": float(arr[0]), "beta": float(arr[1])}
    if decay_form == "offset_power":
        return {"alpha": float(arr[0]), "beta": float(arr[1]), "d0": float(arr[2])}
    if decay_form == "gep":
        return {"beta": float(arr[0]), "eta": float(arr[1])}
    if decay_form == "weighted_sum":
        return {"w": float(min(max(arr[0], 0.0), 1.0)), "alpha": float(arr[1]), "beta": float(arr[2])}
    return {"alpha": float(arr[0]), "beta": float(arr[1]), "eta": float(arr[2])}


def _fit_direct(df: pd.DataFrame, decay_form: str):
    d = df["d_clamped"].values
    O = df["O_i"].values
    A = df["A_j"].values
    actual = df["trip_count"].values

    def predict(arr):
        if decay_form == "power_exp":
            p = {"alpha": arr[0], "beta": arr[1]}
        elif decay_form == "offset_power":
            p = {"alpha": arr[0], "beta": arr[1], "d0": arr[2]}
        elif decay_form == "stretched":
            p = {"alpha": arr[0], "beta": arr[1], "eta": arr[2]}
        elif decay_form == "gep":
            p = {"beta": arr[0], "eta": arr[1]}
        elif decay_form == "weighted_sum":
            p = {"w": arr[0], "alpha": arr[1], "beta": arr[2]}
        return O * A * _decay(d, p, decay_form)

    def loss(arr):
        pred = predict(arr)
        return np.sum((np.log1p(pred) - np.log1p(actual)) ** 2)

    if decay_form == "power_exp":
        x0 = [0.5, 0.1]
    elif decay_form == "offset_power":
        x0 = [0.5, 0.1, 0.1]
    elif decay_form == "gep":
        x0 = [0.5, 0.7]
    elif decay_form == "weighted_sum":
        x0 = [0.5, 1.0, 0.1]
    else:
        x0 = [0.5, 0.1, 1.0]
    res = minimize(loss, x0, method="Nelder-Mead",
                   options={"xatol": 1e-4, "fatol": 1e-4, "maxiter": 300})
    arr = res.x
    if decay_form == "power_exp":
        return {"alpha": float(arr[0]), "beta": float(arr[1])}
    if decay_form == "offset_power":
        return {"alpha": float(arr[0]), "beta": float(arr[1]), "d0": float(arr[2])}
    if decay_form == "gep":
        return {"beta": float(arr[0]), "eta": float(arr[1])}
    if decay_form == "weighted_sum":
        return {"w": float(min(max(arr[0], 0.0), 1.0)), "alpha": float(arr[1]), "beta": float(arr[2])}
    return {"alpha": float(arr[0]), "beta": float(arr[1]), "eta": float(arr[2])}


def my_model(df: pd.DataFrame,
             normalize: bool = True,
             decay_form: str = "power_exp",
             fit_method: str = "bin50_linear") -> tuple[np.ndarray, dict]:
    """Run my model with configurable options.

    Args:
        normalize: apply K_i origin normalization
        decay_form: 'power_exp' | 'offset_power' | 'stretched'
        fit_method: 'bin50_linear' | 'bin50_log' | 'direct'
    """
    if fit_method == "bin50_linear":
        params = _fit_bin(df, decay_form, log_spaced=False)
    elif fit_method == "bin50_log":
        params = _fit_bin(df, decay_form, log_spaced=True)
    elif fit_method == "direct":
        params = _fit_direct(df, decay_form)
    else:
        raise ValueError(fit_method)

    d = df["d_clamped"].values
    O = df["O_i"].values
    A = df["A_j"].values
    pred = O * A * _decay(d, params, decay_form)

    if normalize:
        pred = apply_origin_normalization(df, pred)

    info = {"model": f"MyModel[{decay_form}/{fit_method}/norm={normalize}]"}
    info.update(params)
    return pred, info


# Ablation configurations: progressive enrichment
ABLATION_CONFIGS = [
    # (name, my_model kwargs, build_pairs_dataframe overrides)
    ("MyModel_v0_baseline",       {"normalize": False, "decay_form": "power_exp",    "fit_method": "bin50_linear"}, {"attr_mode": "poi_pop_avg", "adaptive_self": False, "min_distance": 0.1}),
    ("MyModel_v1_normalize",      {"normalize": True,  "decay_form": "power_exp",    "fit_method": "bin50_linear"}, {"attr_mode": "poi_pop_avg", "adaptive_self": False, "min_distance": 0.1}),
    ("MyModel_v2_adaptiveclamp",  {"normalize": True,  "decay_form": "power_exp",    "fit_method": "bin50_linear"}, {"attr_mode": "poi_pop_avg", "adaptive_self": True,  "min_distance": 0.1}),
    ("MyModel_v3_categoryA",      {"normalize": True,  "decay_form": "power_exp",    "fit_method": "bin50_linear"}, {"attr_mode": "poi_categories", "adaptive_self": True, "min_distance": 0.1}),
    ("MyModel_v4_offsetpower",    {"normalize": True,  "decay_form": "offset_power", "fit_method": "bin50_linear"}, {"attr_mode": "poi_categories", "adaptive_self": True, "min_distance": 0.1}),
    ("MyModel_v5_logbins",        {"normalize": True,  "decay_form": "offset_power", "fit_method": "bin50_log"},    {"attr_mode": "poi_categories", "adaptive_self": True, "min_distance": 0.1}),
    ("MyModel_v6_direct",         {"normalize": True,  "decay_form": "offset_power", "fit_method": "direct"},        {"attr_mode": "poi_categories", "adaptive_self": True, "min_distance": 0.1}),
    ("MyModel_v7_network",        {"normalize": True,  "decay_form": "offset_power", "fit_method": "direct"},        {"attr_mode": "poi_categories", "adaptive_self": True, "min_distance": 0.1, "use_network": True}),
]
