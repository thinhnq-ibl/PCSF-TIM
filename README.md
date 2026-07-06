# Reproduction Package — "Calibrating Transferable Gravity Models from Aggregate Mobility Data"

This reproduction package contains the code, data, and scripts required to independently reproduce all key findings and figures in the paper.

---

## Workspace Folder Structure

```
PCSF-TIM/
├── README.md                          ➔ This guide
├── requirements.txt                   ➔ Python dependencies
├── paper/
│   ├── draft_paper_springer.tex       ➔ LaTeX paper source with 3 RQs
│   └── draft_paper_springer.pdf       ➔ Compiled PDF manuscript
├── code/                              ➔ Code scripts
│   ├── decomposed_gravity_model.py    ➔ Core gravity model implementation with Tanner decay
│   ├── decomposed_evaluation_workflow.py ➔ Evaluation workflow for aggregate decay recovery
│   ├── run_zero_shot_transfer_25to25.py ➔ Deterministic 25/25 stratified split definition
│   ├── run_aggregate_calibration_evaluation.py ➔ Evaluates aggregate-recovered decay performance
│   ├── run_deep_gravity_zeroshot.py   ➔ Zero-shot deep learning benchmark execution
│   ├── run_shap_feature_selection.py  ➔ SHAP importance analysis for outflow prediction
│   ├── run_shap_validation_sweep.py   ➔ Supporting sweep determining optimal feature counts
│   ├── plot_layer1_results.py         ➔ Generates decay parameter recovery scatter plots
│   ├── plot_layer2_results.py         ➔ Generates source-scale & noise sensitivity plots
│   ├── baselines.py                   ➔ Baseline models (Radiation, traditional Gravity)
│   ├── utils.py                       ➔ Data loading & normalization utilities
│   └── conference_benchmark.py        ➔ Benchmark helpers
├── results/                           ➔ Output folder for results
├── data/                              ➔ Built-environment features & OD matrices for 50 US cities
└── meta_prior/                        ➔ Meta Movement Distribution Maps data
```

---

## Setup & Prerequisites

### Python Environment
Requires Python 3.9 or higher. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Execution Guide

To reproduce the findings answering the research questions:

### 1. Decay Parameter Recovery (Answering RQ1)
Evaluate how well decay parameters can be recovered from aggregate trip-length histograms (correlations & downstream performance):
```bash
cd code
python run_aggregate_calibration_evaluation.py
```
* **Output CSV**: `results/us_50cities_meta_vs_gt_deepgravity.csv`
* **Plot Figure 4 (Decay scatters)**:
```bash
python plot_layer1_results.py
```
* **Saved Image**: `figures/layer1_scatter_plots.png`

### 2. Component Contribution & Shapley Value Ablation (Answering RQ2)
Run GBDT outflow model training, select transferable features, and compute Shapley values of components:
```bash
python run_shap_feature_selection.py
python run_shap_validation_sweep.py
```
* **Saved Image**: `figures/layer2_results.png` (Source-scale and noise sensitivity)

### 3. Zero-Shot Multi-Baseline & Urban Morphology Evaluation (Answering RQ3)
Evaluate zero-shot transfer CPC across held-out target cities and urban morphological classifications:
```bash
python run_deep_gravity_zeroshot.py
```

---

## Contact & Citation
If you utilize this package for replication, please cite:
> "Calibrating Transferable Gravity Models from Aggregate Mobility Data: An Empirical Investigation of Distance Decay Dominance", 2026.