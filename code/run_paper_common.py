"""
Shared constants, city list, and helper functions for all run_paper_e*.py scripts.
12-city evaluation set: 10 large US + Seoul + Singapore.
"""
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize_scalar
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).parent))
# my_model/code contains utils.py and conference_benchmark.py
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'my_model' / 'code'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from conference_benchmark import _load_seoul_df, _load_sgp_df, FULL_CITIES
from utils import load_city, build_pairs_dataframe, cpc

# ── 12-city evaluation set ────────────────────────────────────────────────────
CITY_LIST_US = [
    'New_York', 'Los_Angeles', 'Chicago', 'Houston', 'Philadelphia',
    'Phoenix', 'San_Antonio', 'Dallas', 'San_Diego', 'San_Jose',
]
CITY_LIST_EXT = [('Seoul', _load_seoul_df), ('Singapore', _load_sgp_df)]
CITY_LIST_12  = [(c, None) for c in CITY_LIST_US] + CITY_LIST_EXT

# Display names (short) for plots
CITY_SHORT = {
    'New_York': 'New York', 'Los_Angeles': 'LA', 'Chicago': 'Chicago',
    'Houston': 'Houston', 'Philadelphia': 'Phila.', 'Phoenix': 'Phoenix',
    'San_Antonio': 'San Antonio', 'Dallas': 'Dallas', 'San_Diego': 'San Diego',
    'San_Jose': 'San Jose', 'Seoul': 'Seoul', 'Singapore': 'Singapore',
}
CITY_REGION = {c: 'US' for c in CITY_LIST_US}
CITY_REGION['Seoul'] = 'Asia'
CITY_REGION['Singapore'] = 'Asia'

# ── Global constants ──────────────────────────────────────────────────────────
K          = 20
SPLIT_SEED = 42
TEST_FRAC  = 0.20
BETA_US    = 16.2
ZONE_SEED  = 99
OI_FRAC    = 0.20
FRACS      = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]
MIN_KNOWN  = 12        # min zones needed for Ridge fit
N_FEATURES = 6
LOG_LO, LOG_HI = -10.0, 15.0
EPS = 1e-6

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT         = Path(__file__).parent.parent.parent
DATA_ROOT_US = Path(__file__).parent.parent / 'data'
ROAD_EXT = {
    'Seoul':     ROOT / 'seoul' / 'data' / 'road.csv',
    'Singapore': ROOT / 'sgp'   / 'data' / 'road.csv',
}
RESULTS_PAPER = Path(__file__).parent.parent / 'results'
RESULTS_PAPER.mkdir(parents=True, exist_ok=True)


# ── Road density ──────────────────────────────────────────────────────────────
def load_road_density(city_name):
    """Return {zone_idx: road_density} from road.csv, or None."""
    p = ROAD_EXT.get(city_name, DATA_ROOT_US / city_name / 'nodes' / 'road.csv')
    if not p.exists():
        return None
    rd = pd.read_csv(p)[['idx', 'road_density']]
    return dict(zip(rd['idx'].values, rd['road_density'].values))


def compute_road_impute():
    """US-wide median road density (for imputing missing zones)."""
    vals = []
    for c in FULL_CITIES:
        rm = load_road_density(c)
        if rm:
            vals.extend(rm.values())
    return float(np.median(vals)) if vals else 1e-4


# ── Feature engineering ───────────────────────────────────────────────────────
def make_features(grp, road_density_map=None, road_impute=1e-4):
    """6-dim log-feature matrix for a grouped zone dataframe.
    Returns (X [n_zones x 6], log_O [n_zones], zone_ids).
    """
    P    = np.nan_to_num(grp['P_i'].values,   nan=0.0).clip(EPS)
    POI  = np.nan_to_num(grp['POI_i'].values, nan=0.0).clip(0.0) + 1.0
    area = np.nan_to_num(grp['area_i'].values, nan=0.01).clip(EPS)
    O    = np.nan_to_num(grp['O_i'].values,   nan=1.0).clip(1.0)
    zone_ids = grp.index.values

    if road_density_map is not None:
        rd = np.array([road_density_map.get(int(z), road_impute) for z in zone_ids], float)
    else:
        rd = np.full(len(zone_ids), road_impute, float)
    rd = np.nan_to_num(rd, nan=road_impute).clip(0.0)

    X = np.column_stack([
        np.log(P + EPS).clip(LOG_LO, LOG_HI),
        np.log(POI + EPS).clip(LOG_LO, LOG_HI),
        np.log(area + EPS).clip(LOG_LO, LOG_HI),
        np.log(P / area + EPS).clip(LOG_LO, LOG_HI),
        np.log(POI / area + EPS).clip(LOG_LO, LOG_HI),
        np.log(rd + 1e-9).clip(LOG_LO, LOG_HI),
    ])
    return X, np.log(O).clip(LOG_LO, LOG_HI), zone_ids


# ── Data loading ──────────────────────────────────────────────────────────────
def load_city_df(city_name, loader=None):
    """Load pairs dataframe for US or external city."""
    if loader is not None:
        return loader()
    return build_pairs_dataframe(
        load_city(city_name),
        attr_mode='poi_pop_avg', min_distance=0.1, adaptive_self=True
    )


# ── Setup (train/test split + bins) ──────────────────────────────────────────
def setup_splits(df, b_k_override=None):
    """Deterministic 80/20 split; compute b_k on training pairs.

    b_k_override: if provided, use this K-bin array instead of computing from data.
    Returns dict with all tensors needed for fitting/eval.
    """
    n = len(df)
    rng = np.random.default_rng(SPLIT_SEED)
    perm = rng.permutation(n)
    n_test = int(n * TEST_FRAC)
    test_mask = np.zeros(n, bool)
    test_mask[perm[:n_test]] = True

    o_idx  = df['o_idx'].values
    A_j    = df['A_j'].values
    d_all  = df['d_clamped'].values.clip(1e-6)
    actual = df['trip_count'].values

    train_idx = perm[n_test:]
    d_tr  = d_all[train_idx]
    T_tr  = actual[train_idx]

    # Bin edges from training distances (equal-width over physical distance)
    edges = np.linspace(0, d_tr.max(), K + 1)
    edges[-1] = np.inf
    bin_idx_all = np.clip(np.searchsorted(edges[1:-1], d_all), 0, K - 1)
    bin_idx_tr  = np.clip(np.searchsorted(edges[1:-1], d_tr),  0, K - 1)

    if b_k_override is not None:
        b_k = np.asarray(b_k_override, float)
        b_k = (b_k / b_k.sum()).clip(1e-12)
    else:
        b_k = np.array([T_tr[bin_idx_tr == k].sum() for k in range(K)], float)
        b_k = (b_k / b_k.sum()).clip(1e-12)

    _, inv = np.unique(o_idx, return_inverse=True)
    return dict(
        o_idx=o_idx, A_j=A_j, d_all=d_all, actual=actual,
        test_mask=test_mask, b_k=b_k, bin_idx_all=bin_idx_all,
        n_total=float(T_tr.sum()), inv=inv, edges=edges,
        d_tr=d_tr, T_tr=T_tr, bin_idx_tr=bin_idx_tr,
    )


# ── Core model ────────────────────────────────────────────────────────────────
def predict_raw(o_idx, A_j, d, O_i_vec, alpha):
    """Vectorised log-sum-exp stable production-constrained gravity."""
    log_f = np.log(A_j.clip(1e-9)) - alpha * np.log(d.clip(1e-6))
    n_o = int(o_idx.max()) + 1
    lf_max = np.full(n_o, -np.inf)
    np.maximum.at(lf_max, o_idx, log_f)
    shifted = np.exp(log_f - lf_max[o_idx])
    sum_exp = np.zeros(n_o)
    np.add.at(sum_exp, o_idx, shifted)
    log_B = lf_max + np.log(sum_exp.clip(1e-300))
    return np.exp(np.log(O_i_vec.clip(1e-9)) + log_f - log_B[o_idx])


def fit_alpha_bins(s, O_pair):
    """Fit alpha by minimising KL(b_k || p_k) using bin histogram."""
    def obj(a):
        T_hat = predict_raw(s['o_idx'], s['A_j'], s['d_all'], O_pair, float(a))
        p_k = np.bincount(s['bin_idx_all'], weights=T_hat, minlength=K).astype(float)
        tot = p_k.sum()
        if tot < 1e-12:
            return 1e12
        return -s['n_total'] * float(np.sum(s['b_k'] * np.log((p_k / tot).clip(1e-15))))
    return float(minimize_scalar(obj, bounds=(0.1, 20.0), method='bounded').x)


def fit_alpha_pairs(s, O_pair):
    """Fit alpha by Poisson log-likelihood on individual training pairs (non-private baseline)."""
    o_tr = s['o_idx'][~s['test_mask']]
    A_tr = s['A_j'][~s['test_mask']]
    d_tr = s['d_all'][~s['test_mask']]
    T_tr = s['actual'][~s['test_mask']]
    O_tr = O_pair[~s['test_mask']]
    # Use pair-level pseudo-LLH: minimize -sum T_ij * log(hat_T_ij)
    def obj(a):
        T_hat = predict_raw(o_tr, A_tr, d_tr, O_tr, float(a))
        return -float(np.sum(T_tr * np.log(T_hat.clip(1e-15))))
    return float(minimize_scalar(obj, bounds=(0.1, 20.0), method='bounded').x)


def eval_cpc(s, T_pred):
    return float(cpc(T_pred[s['test_mask']], s['actual'][s['test_mask']]))


def full_pipeline(s, O_per_o, inv, fit_fn=None):
    """Run full pipeline with given O_i proxy. Returns (cpc, alpha)."""
    if fit_fn is None:
        fit_fn = fit_alpha_bins
    O_pair = O_per_o[inv]
    alpha = fit_fn(s, O_pair)
    T_pred = predict_raw(s['o_idx'], s['A_j'], s['d_all'], O_pair, alpha)
    return eval_cpc(s, T_pred), alpha


# ── O_i imputation methods ────────────────────────────────────────────────────
def impute_m0(P_per_o):
    return np.maximum(P_per_o * BETA_US, 1.0)


def impute_m1(O_per_o, P_per_o, known_idx):
    O_k = O_per_o[known_idx]; P_k = P_per_o[known_idx]
    valid = P_k > 100
    beta = float(np.median(O_k[valid] / P_k[valid])) if valid.sum() >= 3 \
        else float(np.median(O_k / P_k.clip(1)))
    return np.maximum(P_per_o * beta, 1.0), beta


def impute_m2_ridge(O_per_o, X, logO, known_idx, unknown_idx):
    """Ridge regression in log space. Returns O_hat array (true for known zones)."""
    scaler = StandardScaler()
    X_tr = scaler.fit_transform(X[known_idx])
    ridge = Ridge(alpha=1.0)
    ridge.fit(X_tr, logO[known_idx])
    O_hat = O_per_o.copy()
    O_hat[unknown_idx] = np.maximum(np.exp(ridge.predict(scaler.transform(X[unknown_idx]))), 1.0)
    return O_hat


def oi_r2(O_true, O_pred):
    log_t = np.log(np.maximum(O_true, 1))
    log_p = np.log(np.maximum(O_pred, 1))
    ss_res = np.sum((log_t - log_p) ** 2)
    ss_tot = np.sum((log_t - log_t.mean()) ** 2)
    return float(1 - ss_res / ss_tot) if ss_tot > 1e-9 else 0.0


def recovery(cpc_method, cpc_m0, cpc_true):
    gap = cpc_true - cpc_m0
    return float((cpc_method - cpc_m0) / gap) if gap > 1e-6 else 0.0
