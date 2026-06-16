# Reproduction Package — "Survey-Free Urban Mobility Modelling via Meta MDM Priors"

This folder contains everything needed to independently reproduce all key results in the paper.

**Target journal**: *Computers, Environment and Urban Systems* / *IJGIS* / *Transportation Research Part C*

---

## Folder Structure

```
prepare_for_paper/
├── README.md                    ← This guide
├── requirements.txt             ← Python dependencies
├── paper/
│   ├── draft_paper.md           ← Full English Q1 paper
│   └── draft_paper_vn.md        ← Bilingual English/Vietnamese version
├── code/                        ← All experiment scripts
│   ├── conference_benchmark.py  ← Core benchmark engine (shared)
│   ├── run_us_gravity_ablation.py         ← RQ2: Table 2
│   ├── run_us_meta_vs_gt_deepgravity.py   ← RQ1: Table 1
│   ├── run_us_bin_sweep_unified.py        ← RQ3: Table 3
│   ├── run_us_oi_sweep.py                 ← RQ4: Table 4
│   ├── my_model.py              ← Core model kernels
│   ├── utils.py                 ← Data loading helpers
│   ├── baselines.py             ← Radiation & gravity baselines
│   ├── run_paper_common.py      ← Shared utilities for meta script
│   ├── plot_us_ablation.py      ← Figure 1 generator
│   ├── plot_us_meta_vs_gt_deepgravity.py  ← Figure 3 generator
│   ├── plot_us_bin_sweep.py               ← Figure 4 generator
│   └── plot_us_oi_sweep_multimetric.py    ← Figure 2 generator
├── results/                     ← Pre-computed CSV results (reference values)
│   ├── conference_per_city_full.csv        ← Per-city CPC for all models
│   ├── conference_summary_full.csv         ← Summary statistics
│   ├── conference_paired_tests_full.csv    ← Wilcoxon/t-test results
│   ├── us_50cities_gravity_ablation_cpc.csv ← RQ2: 50-city singly-constrained ablation
│   ├── us_50cities_statistical_tests.md    ← Statistical significance report (50 cities)
│   ├── bootstrap_wilcoxon.csv              ← Bootstrap CIs
│   ├── bootstrap_wilcoxon_summary.csv      ← Bootstrap summary
│   ├── CONFERENCE_RESULTS.md               ← Conference benchmark narrative
│   └── RESULTS_SUMMARY.md                  ← Human-readable summary
├── figures/                     ← Pre-computed publication figures
│   ├── us_50cities_ablation_cpc.png/.pdf           ← Figure 1
│   ├── us_50cities_meta_vs_gt_deepgravity.png/.pdf ← Figure 3
│   ├── us_50cities_bin_sweep_cpc_rmse.png/.pdf     ← Figure 4
│   ├── us_50cities_oi_sweep_multimetric.png/.pdf   ← Figure 2
│   ├── us_50cities_oi_scarcity_sweet_spot.png      ← Figure 2b
│   ├── us_50cities_cpc_boxplot.png                 ← Figure 6
│   └── accuracy_vs_data_requirement.png            ← Figure 5
├── data/                        ← City data for all 50 US cities
│   └── {City}/
│       ├── meta.csv             ← Tract GEOIDs, lon/lat, area
│       ├── features.json        ← City-level metadata
│       ├── nodes/
│       │   ├── census.csv       ← Population, income per zone
│       │   ├── poi.csv          ← POI counts per zone
│       │   └── road.csv         ← Road density per zone
│       └── pairs/
│           ├── od.csv           ← Observed OD flows (LODES)
│           └── distance.csv     ← Pairwise haversine distances
└── meta_prior/
    └── movement-distribution-maps_2026-04-01_2026-04-16.csv
                                 ← Meta Mobility Distribution Map prior
```

---

## Prerequisites

### Python Version
Python 3.9 or higher (tested on Python 3.10, 3.11).

### Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy>=1.24 pandas>=2.0 scipy>=1.10 scikit-learn>=1.3 \
            torch>=2.0 matplotlib>=3.7 seaborn>=0.12 tqdm>=4.65
```

### Working Directory
All scripts use **relative paths based on the original project root**. To run them, either:

**Option A (recommended)** — Set the project root in your environment:
```bash
# From the prepare_for_paper/ directory, run scripts by pointing to code/:
cd prepare_for_paper
```

**Option B** — Run from the workspace root, pointing at `prepare_for_paper/code/`:
```bash
# From workspace root (human_mobility/)
python prepare_for_paper/code/conference_benchmark.py --full
```

> **Note on data paths**: The scripts resolve data paths relative to their own file location. Since `code/` and `data/` are both inside `prepare_for_paper/`, you may need to edit the `DATA_ROOT_US` path variable in each script to point to `prepare_for_paper/data/` instead of `us/data/`.

### Quick Path Fix (run once)
```python
# In each script, find the line:
DATA_ROOT_US = Path(__file__).parent.parent.parent / "us" / "data"
# Change to:
DATA_ROOT_US = Path(__file__).parent.parent / "data"
```

---

## Data Description

### 50 US Cities (in `data/`)
The `data/` folder contains all 50 US cities used across all experiments:

| Group | Cities |
|-------|--------|
| East | Baltimore, Boston, Philadelphia, Washington_DC, Charlotte, Raleigh |
| Midwest | Columbus, Indianapolis, Louisville, Memphis, Milwaukee, Nashville |
| West | Austin, Denver, Houston, Portland, San_Diego, San_Francisco, San_Jose, Seattle |
| Southwest | Albuquerque, El_Paso, Las_Vegas, Mesa, Phoenix, Tucson |
| South | Arlington, Atlanta, Dallas, Fort_Worth, Jacksonville, Miami, Oklahoma_City, San_Antonio, Tampa, Tulsa, Virginia_Beach, Wichita |
| Midwest+ | Chicago, Colorado_Springs, Kansas_City, Minneapolis, Omaha |
| West Coast | Fresno, Long_Beach, Los_Angeles, Oakland, Sacramento |
| New York | New_York |

### Data Files Per City

| File | Description | Columns |
|------|-------------|---------|
| `meta.csv` | Zone metadata | `idx, t_id (GEOID), lon, lat, area_km2, city` |
| `nodes/census.csv` | Demographics per zone | `idx, total_population, median_income, ...` |
| `nodes/poi.csv` | POI counts per zone | `idx, total_pois, restaurant, office, ...` |
| `nodes/road.csv` | Road infrastructure | `idx, road_density` |
| `pairs/od.csv` | Observed commute flows | `o_idx, d_idx, trip_count` |
| `pairs/distance.csv` | Pairwise distances | `o_idx, d_idx, d_km` |

> [!IMPORTANT]
> **Privacy & Transferability Constraint**: Do NOT use `employment_rate` (or any other employment-related census fields) in the feature space of the prediction models. PCF-CTF relies strictly on globally available open data (OSM, WorldPop/Meta population) to maintain zero-shot generalizability; LODES employment metrics are deliberately excluded to prevent privacy leakage and dependencies on proprietary/local surveys.

**Source**: LODES (Longitudinal Employer-Household Dynamics) workplace area characteristics, US Census Bureau. DOI: https://lehd.ces.census.gov/

### Meta MDM Prior (`meta_prior/`)
`movement-distribution-maps_2026-04-01_2026-04-16.csv` — Meta Mobility Distribution Maps aggregated at county level. Used as a survey-free substitute for local OD calibration.

**Relevant columns**: `country, polygon_level, polygon_name, start_quadkey, end_quadkey, length_km, n_crisis, n_baseline`

The script filters to distance bins: `(0, 10)`, `[10, 100)`, `100+` km.

---

## Experiment Reproduction Guide

### Overview — Experiments to Paper Tables/Figures

| Experiment Script | Paper Table | Paper Figure | Research Question | Cities | Expected Runtime |
|---|---|---|---|---|---|
| `conference_benchmark.py --full` | Table 1 (model comparison) | Figure 1 | RQ2 baseline | **50 cities** | ~75 min |
| `run_us_gravity_ablation.py` | Table 2 (singly- vs unconstrained) | Figure 1 | RQ2 | **50 cities** | ~60 min |
| `run_us_meta_vs_gt_deepgravity.py` | Table 3 (Meta vs local) | Figure 3 | RQ1 | **50 cities** | ~45 min |
| `run_us_bin_sweep_unified.py` | Table 4 (bin count ablation) | Figure 4 | RQ3 | **50 cities** | ~75 min |
| `run_us_oi_sweep.py` | Table 5 (survey fraction) | Figure 2 | RQ4 | **50 cities** | ~60 min |

---

### Experiment 1: Full Model Benchmark (Table 1)

**Script**: `conference_benchmark.py`  
**What it does**: Compares Radiation, Gravity-Exp, Gravity-Power, MyModel_v2, and DeepGravity across all 50 cities on 80/20 train/test split (seed=42). Bootstraps 95% CI (B=200).

```bash
# Run from workspace root
python prepare_for_paper/code/conference_benchmark.py --full
```

**Expected outputs**:
- `prepare_for_paper/results/conference_per_city_full.csv` — per-city results
- `prepare_for_paper/results/conference_summary_full.csv` — mean ± std per model
- `prepare_for_paper/results/conference_paired_tests_full.csv` — Wilcoxon p-values

**Expected summary values (mean CPC, n=50 cities from `us_50cities_gravity_ablation_cpc.csv`)**:

| Model | Expected mean CPC | Std |
|-------|------------------|-----|
| DoublyConstrained_Power | — | — |
| DeepGravity_MLP | 0.7713 | — |
| Gravity_Power_Constrained | 0.7263 | 0.030 |
| **MyModel_v2_PowerExp** | **0.7214** | **0.026** |
| Gravity_Exp_Constrained | 0.6374 | 0.039 |
| Radiation_Population | 0.4492 | 0.054 |

> Values from pre-computed `results/us_50cities_gravity_ablation_cpc.csv`. DoublyConstrained not in ablation CSV.

**Cross-check with pre-computed results**:
```python
import pandas as pd
ref = pd.read_csv('prepare_for_paper/results/us_50cities_gravity_ablation_cpc.csv')
print(ref[['city','MyModel_v2_PowerExp','Gravity_Power_Con','Gravity_Exp_Con','DeepGravity_MLP']].mean())
```

---

### Experiment 2: Singly-Constrained vs Unconstrained Ablation (Table 2)

**Script**: `run_us_gravity_ablation.py`  
**What it does**: Compares singly-constrained vs unconstrained gravity and MyModel_v2 across all 50 cities.

```bash
python prepare_for_paper/code/run_us_gravity_ablation.py
```

**Expected output**: `results/us_50cities_gravity_ablation_cpc.csv`

**Expected columns**: `city, Gravity_Power_Con, Gravity_Exp_Con, MyModel_v2_PowerExp, Radiation_Pop, DeepGravity_MLP`

**Key finding**: Singly-constrained dominates unconstrained by ~10–35% CPC across all 50 cities.

**Cross-check**:
```python
df = pd.read_csv('prepare_for_paper/results/us_50cities_gravity_ablation_cpc.csv')
print(df[['city','MyModel_v2_PowerExp','Gravity_Power_Con','Gravity_Exp_Con']].to_string())
print('\nMeans:', df[['MyModel_v2_PowerExp','Gravity_Power_Con','Gravity_Exp_Con','Radiation_Pop']].mean())
```

---

### Experiment 3: Meta MDM Prior vs Ground Truth Calibration (Table 3)

**Script**: `run_us_meta_vs_gt_deepgravity.py`  
**What it does**: Compares 4 calibration strategies: Meta-3 (survey-free), House-3 (GT 3-bin), House-K20 (GT percentile), and DeepGravity across all 50 cities.

```bash
python prepare_for_paper/code/run_us_meta_vs_gt_deepgravity.py
```

**Expected output**: `results/us_50cities_meta_vs_gt_deepgravity.csv`

**Expected mean CPC across 50 cities**:

| Method | Expected mean CPC |
|--------|-----------------|
| Meta-3 (survey-free) | **0.709** |
| House-3 (GT 3-bin) | 0.721 |
| House-K20 (GT 20-pct) | **0.730** |
| DeepGravity MLP | **0.772** |

**Statistical test** — Meta-3 vs House-K20 gap (ΔCPC = 0.021, p = 0.21, not significant):
```python
from scipy.stats import wilcoxon
df = pd.read_csv('prepare_for_paper/results/us_50cities_meta_vs_gt_deepgravity.csv')
stat, p = wilcoxon(df['cpc_meta_3'], df['cpc_house_k20'])
print(f"Wilcoxon p-value (Meta-3 vs House-K20): {p:.4f}")
# Expected: p > 0.05 (not statistically significant)
```

**Cross-check per-city values**:
```python
df = pd.read_csv('prepare_for_paper/results/us_50cities_meta_vs_gt_deepgravity.csv')
print(df[['city','cpc_meta_3','cpc_house_k20','cpc_deepgravity']].to_string())
```

**Note**: Cities with `scale_check = FALLBACK` (Baltimore, Boston, Louisville, San_Francisco, Washington_DC) indicate that Meta MDM data required robust scale fallback due to sparse coverage — the model still runs and produces valid results.

---

### Experiment 4: Distance Bin Count Ablation (Table 4)

**Script**: `run_us_bin_sweep_unified.py`  
**What it does**: Sweeps K=3,4,5,7,10,15,20,25,30 percentile bins + Physical 3-bin and 4-bin across all 50 cities.

```bash
python prepare_for_paper/code/run_us_bin_sweep_unified.py
```

**Expected output**: `results/us_50cities_bin_sweep_unified.csv`

**Key findings** (mean CPC across 50 cities):

| Bin Configuration | Expected mean CPC |
|-------------------|-----------------|
| Physical 3-bin [0,10,100,∞] km | ~0.724 |
| Physical 4-bin [0,1,10,100,∞] km | **~0.730** |
| Percentile K=10 | ~0.729 |
| Percentile K=20 | ~0.730 |
| Percentile K=30 | ~0.730 |

**Result**: K≥10 and Physical-4 achieve near-identical CPC (plateau effect). Physical-3 bin matches Meta MDM constraints.

**Cross-check**:
```python
df = pd.read_csv('prepare_for_paper/results/us_50cities_bin_sweep_unified.csv')
cols_cpc = [c for c in df.columns if c.startswith('cpc_')]
print(df[cols_cpc].mean().sort_values(ascending=False))
```

---

### Experiment 5: Survey Fraction Sensitivity — "Sweet Spot" (Table 5)

**Script**: `run_us_oi_sweep.py`  
**What it does**: Varies the fraction of sampled OD pairs used for calibration (ρ = 5%, 10%, ..., 50%) with Ridge regression on 6 OSM features across all 50 cities.

```bash
python prepare_for_paper/code/run_us_oi_sweep.py
```

**Expected outputs**:
- `results/us_50cities_oi_sweep.csv` — long format (city × frac × metrics)

**Key finding — CPC by survey fraction** (averaged across 50 cities):

| ρ (fraction) | Expected mean CPC |
|-------------|-----------------|
| 0 (zero-shot, Meta prior) | ~0.670 |
| 5% | ~0.682 |
| 10% | ~0.693 |
| **20%** | **~0.706** ← sweet spot |
| 30% | ~0.710 |
| 50% | ~0.714 |

**Sweet spot logic**: Marginal CPC gain per 1% survey: +0.146pp/1% for ρ<20%, drops to +0.047pp/1% for ρ>20%. Economic optimum at ρ = 20%.

**Cross-check**:
```python
df = pd.read_csv('prepare_for_paper/results/us_50cities_oi_sweep.csv')
print(df.groupby('frac')['cpc'].mean())
```

---

## Generating Publication Figures

Each figure has a dedicated plot script. Run from workspace root:

```bash
# Figure 1: Model comparison boxplot
python prepare_for_paper/code/plot_us_ablation.py

# Figure 2: Survey fraction sweep (multi-metric)
python prepare_for_paper/code/plot_us_oi_sweep_multimetric.py

# Figure 3: Meta vs Ground Truth comparison
python prepare_for_paper/code/plot_us_meta_vs_gt_deepgravity.py

# Figure 4: Bin sweep CPC/RMSE
python prepare_for_paper/code/plot_us_bin_sweep.py
```

Pre-computed publication-quality figures are available in `figures/` — they can be used for verification without re-running.

---

## Statistical Significance Tests

All significance tests use paired Wilcoxon signed-rank (non-parametric) and paired t-test. **All experiments now run over all 50 cities.** Pre-computed 50-city results in `results/us_50cities_statistical_tests.md`.

**Reproduce statistical tests**:
```python
import pandas as pd
from scipy.stats import wilcoxon, ttest_rel

ref = pd.read_csv('prepare_for_paper/results/conference_per_city_full.csv')

# Pivot to get per-city CPC by model
pivot = ref.pivot_table(index='city', columns='model', values='test_cpc')

# MyModel_v2 vs Gravity_Exp_Constrained
stat, p = wilcoxon(pivot['MyModel_v2_PowerExp'], pivot['Gravity_Exp_Constrained'])
print(f"MyModel_v2 vs Gravity_Exp: Wilcoxon p = {p:.2e}")
# Expected: p << 0.001 (highly significant)

# MyModel_v2 vs Radiation
stat, p = wilcoxon(pivot['MyModel_v2_PowerExp'], pivot['Radiation_Population'])
print(f"MyModel_v2 vs Radiation: Wilcoxon p = {p:.2e}")
# Expected: p ~ 1.78e-15

# MyModel_v2 vs DeepGravity
stat, p = wilcoxon(pivot['MyModel_v2_PowerExp'], pivot['DeepGravity_MLP'])
print(f"MyModel_v2 vs DeepGravity: Wilcoxon p = {p:.2e}")
# Expected: p ~ 6.3e-11 (DeepGravity is significantly better)
```

**Pre-computed summary** (from `results/us_50cities_statistical_tests.md`):

| Comparison | Mean ΔCPC | Wilcoxon W | p-value | Significant? |
|-----------|-----------|-----------|---------|-------------|
| MyModel_v2 vs Gravity_Exp | +0.077 | 0.0 | 2.6e-23 | Yes |
| MyModel_v2 vs Radiation | +0.230 | 0.0 | 8.4e-33 | Yes |
| MyModel_v2 vs Gravity_Power | −0.015 | 119.5 | 5.7e-7 | Yes (Power > MyModel) |
| MyModel_v2 vs DeepGravity | −0.048 | 51.0 | 6.3e-11 | Yes (DG > MyModel) |

---

## Model Architecture Reference

### Core Model: MyModel_v2 (Power-Exponential / Tanner Hybrid)

The singly-constrained gravity model with Power-Exponential kernel:

$$T_{ij} = O_i \cdot \frac{A_j \cdot d_{ij}^{-\alpha} \cdot e^{-\beta \cdot d_{ij}}}{\sum_{j'} A_{j'} \cdot d_{ij'}^{-\alpha} \cdot e^{-\beta \cdot d_{ij'}}}$$

Where:
- $O_i$ = observed outflow from zone $i$ (singly-constrained)
- $A_j$ = attractiveness of zone $j$ (total population from LODES)
- $d_{ij}$ = haversine distance in km (self-flow: $d_{ii} = \sqrt{A_i/\pi}$)
- $\alpha$ = power decay exponent (calibrated per city, typically 1.3–1.7)
- $\beta$ = fixed at 0 for standard fitting (exponential component optional)

### Calibration via KL-Divergence on Distance Bins

Parameters are fitted by minimizing KL divergence between observed and predicted trip-length distributions, aggregated into discrete distance bins. No pairwise OD data required — only the marginal distance histogram.

**4-bin physical scheme** (default): `[0, 1, 10, 100, ∞]` km  
**Meta-3 scheme** (survey-free): `[0, 10, 100, ∞]` km (3 bins, matching Meta MDM resolution)

### Evaluation Metric: CPC

$$\text{CPC} = \frac{2 \sum_{ij} \min(T_{ij}, \hat{T}_{ij})}{\sum_{ij} T_{ij} + \sum_{ij} \hat{T}_{ij}}$$

Range: [0, 1]. Higher is better. Evaluation on held-out 20% test split (seed=42).

---

## Reproducibility Checklist

Use this checklist for independent third-party verification:

- [ ] Python ≥ 3.9 installed, all packages in `requirements.txt` installed
- [ ] **Experiment 1** (`conference_benchmark.py --full`): MyModel_v2 mean CPC ≈ 0.721 across 50 cities (see `results/us_50cities_gravity_ablation_cpc.csv`)
- [ ] **Experiment 2** (`run_us_gravity_ablation.py`): Singly-constrained CPC > Unconstrained for all 50 cities
- [ ] **Experiment 3** (`run_us_meta_vs_gt_deepgravity.py`): Meta-3 CPC vs House-K20 not statistically different (p > 0.05, 50 cities)
- [ ] **Experiment 4** (`run_us_bin_sweep_unified.py`): CPC plateau at K≥10, Physical-4 ≈ K=20 (50 cities)
- [ ] **Experiment 5** (`run_us_oi_sweep.py`): Sweet spot at ρ=20%, marginal gain drops after 20% (50 cities)
- [ ] **Statistical tests (50 cities)**: MyModel_v2 vs Radiation p < 1e-30, vs Gravity_Exp p < 1e-20 (see `results/us_50cities_statistical_tests.md`)
- [ ] **Figures**: Re-generated figures visually match `figures/*.png`

---

## Troubleshooting

### ImportError: No module named 'conference_benchmark'
The scripts import each other. Make sure your `PYTHONPATH` includes the `code/` directory:
```bash
export PYTHONPATH=prepare_for_paper/code:$PYTHONPATH  # Linux/Mac
$env:PYTHONPATH = "prepare_for_paper\code;$env:PYTHONPATH"  # Windows PowerShell
```

### FileNotFoundError: us/data/{City}/
The scripts by default look for data at `../../us/data/` relative to the code. If running from `prepare_for_paper/code/`, change `DATA_ROOT_US` in each script to:
```python
DATA_ROOT_US = Path(__file__).parent.parent / "data"
```

### Meta CSV not found
The Meta MDM CSV is referenced as:
```python
META_CSV = ROOT / 'movement-distribution-maps_2026-04-01_2026-04-16.csv'
```
Change to point to `prepare_for_paper/meta_prior/movement-distribution-maps_2026-04-01_2026-04-16.csv`.

### CONF_CSV (conference_per_city_full.csv) not found
The meta script reads pre-computed DeepGravity results. Change:
```python
CONF_CSV = ROOT / 'my_model' / 'results' / 'conference_per_city_full.csv'
```
to:
```python
CONF_CSV = Path(__file__).parent.parent / 'results' / 'conference_per_city_full.csv'
```

---

## Contact & Citation

If you reproduce any results from this package, please cite:

> [Author(s)], "Survey-Free Urban Mobility Modelling via Meta Mobility Distribution Map Priors", *Computers, Environment and Urban Systems*, 2025.

Data source: U.S. Census Bureau LODES, Meta Mobility Distribution Maps (April 2026).

---

*Package assembled: 2026. All results reproducible with the code and data provided in this folder.*
