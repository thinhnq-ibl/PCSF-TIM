"""
plot_layer2_results.py
======================
Visualise Layer 2 (Outflow Bottleneck Analysis) results.

Figures generated
-----------------
figures/layer2_learning_curve.png  — T2.4: CPC vs #source cities
figures/layer2_noise_sensitivity.png — T2.2: CPC under noise on GBDT O_i

Usage
-----
    python prepare_for_paper/code/plot_layer2_results.py
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS    = os.path.join(BASE_DIR, "results")
FIGURES    = os.path.join(BASE_DIR, "figures")
os.makedirs(FIGURES, exist_ok=True)

# ── Style ──────────────────────────────────────────────────────────────────────
BLUE    = "#4C72B0"
ORANGE  = "#DD8452"
GREEN   = "#55A868"
GREY    = "#8A8A8A"
RED     = "#C44E52"

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "font.size":        12,
    "axes.titlesize":   13,
    "axes.labelsize":   12,
    "xtick.labelsize":  11,
    "ytick.labelsize":  11,
    "legend.fontsize":  11,
    "axes.spines.top":  False,
    "axes.spines.right": False,
    "figure.dpi":       150,
})


# ══════════════════════════════════════════════════════════════════════════════
# Figure 1 — T2.4  Learning Curve
# ══════════════════════════════════════════════════════════════════════════════
def plot_learning_curve(ax, df_lc, df_t2):
    """CPC mean ± 1σ as #source cities grows from 5 → 25."""
    x      = df_lc["n_source"].values
    y_mean = df_lc["cpc_mean"].values
    y_std  = df_lc["cpc_std"].values

    # Shaded ±1σ band
    ax.fill_between(x, y_mean - y_std, y_mean + y_std,
                    color=BLUE, alpha=0.18, label=r"$\pm 1\sigma$ (3 seeds)")

    # Learning curve line
    ax.plot(x, y_mean, "o-", color=BLUE, linewidth=2.2,
            markersize=8, markerfacecolor="white", markeredgewidth=2.2,
            label="GBDT CPC (survey-free)")

    # Reference lines
    oracle_cpc = df_t2["cpc_oracle"].mean()

    ax.axhline(oracle_cpc, color=GREEN, linewidth=1.6, linestyle="--",
               label=f"Oracle $O_i$ (N=25): {oracle_cpc:.3f}")

    # Annotate each point
    for xi, yi, si in zip(x, y_mean, y_std):
        ax.annotate(f"{yi:.3f}", xy=(xi, yi),
                    xytext=(0, 10), textcoords="offset points",
                    ha="center", fontsize=9.5, color=BLUE)

    ax.set_xlabel("Number of source cities used to train GBDT")
    ax.set_ylabel("Mean CPC (25 held-out cities)")
    ax.set_title("T2.4  Source-Scale Robustness — Outflow GBDT Learning Curve")
    ax.set_xticks(x)
    ax.set_xticklabels([str(int(v)) for v in x])
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f"))
    ax.legend(loc="upper left", framealpha=0.9)
    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.5)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 2 — T2.2  Noise Sensitivity
# ══════════════════════════════════════════════════════════════════════════════
def plot_noise_sensitivity(ax, df_t2):
    """Bar chart: mean CPC at noise levels 0, 10, 20, 40 % applied to logO_pred."""
    noise_levels = [0, 10, 20, 40]
    means = [df_t2[f"cpc_noise_{n}"].mean() for n in noise_levels]
    stds  = [df_t2[f"cpc_noise_{n}"].std()  for n in noise_levels]

    xpos  = np.arange(len(noise_levels))
    bars  = ax.bar(xpos, means, width=0.55, color=BLUE, alpha=0.82,
                   yerr=stds, capsize=5, error_kw={"ecolor": GREY, "linewidth": 1.5},
                   label="GBDT + noise")

    # Oracle reference
    oracle_cpc = df_t2["cpc_oracle"].mean()
    ax.axhline(oracle_cpc, color=GREEN, linewidth=1.6, linestyle="--",
               label=f"Oracle $O_i$: {oracle_cpc:.3f}")

    # Annotate bars
    for bar, mean_val in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height() + 0.002,
                f"{mean_val:.3f}", ha="center", va="bottom",
                fontsize=9.5, color=BLUE)

    ax.set_xticks(xpos)
    ax.set_xticklabels([f"{n}%" for n in noise_levels])
    ax.set_xlabel(r"Gaussian noise $\sigma$ on $\log\hat{O}_i$ (GBDT prediction)")
    ax.set_ylabel("Mean CPC (25 held-out cities)")
    ax.set_title(r"T2.2  Noise Sensitivity — CPC under perturbed $\hat{O}_i$")
    ax.legend(loc="lower left", framealpha=0.9)
    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.5)


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════
def main():
    # Load data
    lc_path = os.path.join(RESULTS, "layered_t2_learning_curve.csv")
    t2_path = os.path.join(RESULTS, "layered_t2_outflow.csv")

    if not os.path.exists(lc_path):
        print(f"[ERROR] Learning curve data not found: {lc_path}")
        print("  Run run_layered_evaluation.py first to generate results.")
        return
    if not os.path.exists(t2_path):
        print(f"[ERROR] Outflow results not found: {t2_path}")
        return

    df_lc = pd.read_csv(lc_path)
    df_t2 = pd.read_csv(t2_path)

    # ── Combined figure (2 panels) ─────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.2))
    fig.suptitle("Layer 2: Outflow ($O_i$) Estimation — Bottleneck Analysis",
                 fontsize=14, fontweight="bold", y=1.01)

    plot_learning_curve(axes[0], df_lc, df_t2)
    plot_noise_sensitivity(axes[1], df_t2)

    plt.tight_layout()
    out_combined = os.path.join(FIGURES, "layer2_results.png")
    plt.savefig(out_combined, bbox_inches="tight", dpi=200)
    plt.close()
    print(f"[OK] Saved combined figure: {out_combined}")

    # ── Stand-alone learning curve (for paper) ─────────────────────────────
    fig2, ax2 = plt.subplots(figsize=(7, 4.5))
    plot_learning_curve(ax2, df_lc, df_t2)
    plt.tight_layout()
    out_lc = os.path.join(FIGURES, "layer2_learning_curve.png")
    plt.savefig(out_lc, bbox_inches="tight", dpi=200)
    plt.close()
    print(f"[OK] Saved learning curve : {out_lc}")

    # ── Stand-alone noise chart (for paper) ────────────────────────────────
    fig3, ax3 = plt.subplots(figsize=(6.5, 4.5))
    plot_noise_sensitivity(ax3, df_t2)
    plt.tight_layout()
    out_ns = os.path.join(FIGURES, "layer2_noise_sensitivity.png")
    plt.savefig(out_ns, bbox_inches="tight", dpi=200)
    plt.close()
    print(f"[OK] Saved noise sensitivity: {out_ns}")


if __name__ == "__main__":
    main()
