import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score
from scipy.stats import pearsonr

# Set plot style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 13, 'axes.titlesize': 14})

# Path setups
CODE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(os.path.dirname(CODE_DIR), "results")
FIGURES_DIR = os.path.join(os.path.dirname(CODE_DIR), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

def plot_scatters():
    # Load recovery data
    df_rec = pd.read_csv(os.path.join(RESULTS_DIR, "layered_t1_recovery.csv"))
    
    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='silver')
    
    # --- Alpha (Gamma) Plot ---
    x_alpha = df_rec["alpha_gt"].values
    y_alpha = df_rec["alpha_recovered"].values
    corr_alpha, _ = pearsonr(x_alpha, y_alpha)
    r2_alpha = corr_alpha ** 2  # Explained variance (Pearson r^2)
    mae_alpha = np.mean(np.abs(x_alpha - y_alpha))
    rmse_alpha = np.sqrt(np.mean((x_alpha - y_alpha)**2))
    
    sns.scatterplot(x=x_alpha, y=y_alpha, ax=axes[0], s=80, color="#1f77b4", edgecolor="w", alpha=0.8)
    lims = [min(x_alpha.min(), y_alpha.min()) - 0.1, max(x_alpha.max(), y_alpha.max()) + 0.1]
    axes[0].plot(lims, lims, "k--", alpha=0.7, zorder=0, label="Perfect Recovery ($y=x$)")
    axes[0].set_xlim(lims)
    axes[0].set_ylim(lims)
    axes[0].set_xlabel("Ground Truth $\\gamma$ (Full OD)")
    axes[0].set_ylabel("Recovered $\\gamma$ (Distance Bins)")
    axes[0].set_title("Power-law Decay $\\gamma$ Recovery")
    axes[0].legend(loc="upper left")
    
    text_alpha = f"Pearson $r^2 = {r2_alpha:.3f}$\nPearson $r = {corr_alpha:.3f}$\nMAE = {mae_alpha:.4f}\nRMSE = {rmse_alpha:.4f}"
    axes[0].text(0.58, 0.06, text_alpha, transform=axes[0].transAxes, fontsize=11,
                 verticalalignment='bottom', bbox=props)
    
    # --- Beta Plot ---
    x_beta = df_rec["beta_gt"].values
    y_beta = df_rec["beta_recovered"].values
    corr_beta, _ = pearsonr(x_beta, y_beta)
    r2_beta = corr_beta ** 2  # Explained variance (Pearson r^2)
    mae_beta = np.mean(np.abs(x_beta - y_beta))
    rmse_beta = np.sqrt(np.mean((x_beta - y_beta)**2))
    
    sns.scatterplot(x=x_beta, y=y_beta, ax=axes[1], s=80, color="#d62728", edgecolor="w", alpha=0.8)
    lims_beta = [min(x_beta.min(), y_beta.min()) - 0.01, max(x_beta.max(), y_beta.max()) + 0.01]
    axes[1].plot(lims_beta, lims_beta, "k--", alpha=0.7, zorder=0, label="Perfect Recovery ($y=x$)")
    axes[1].set_xlim(lims_beta)
    axes[1].set_ylim(lims_beta)
    axes[1].set_xlabel("Ground Truth $\\beta$ (Full OD)")
    axes[1].set_ylabel("Recovered $\\beta$ (Distance Bins)")
    axes[1].set_title("Exponential Decay $\\beta$ Recovery")
    axes[1].legend(loc="upper left")
    
    text_beta = f"Pearson $r^2 = {r2_beta:.3f}$\nPearson $r = {corr_beta:.3f}$\nMAE = {mae_beta:.4f}\nRMSE = {rmse_beta:.4f}"
    axes[1].text(0.58, 0.06, text_beta, transform=axes[1].transAxes, fontsize=11,
                 verticalalignment='bottom', bbox=props)
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "layer1_scatter_plots.png"), dpi=300)
    plt.close()
    print("Saved -> figures/layer1_scatter_plots.png")

def plot_heatmap():
    # Load all data
    df_t11 = pd.read_csv(os.path.join(RESULTS_DIR, "layered_t1_recovery.csv"))
    df_t13 = pd.read_csv(os.path.join(RESULTS_DIR, "layered_t1_attraction_perturbation.csv"))
    df_t14 = pd.read_csv(os.path.join(RESULTS_DIR, "layered_t1_attraction_masking.csv"))
    df_t15 = pd.read_csv(os.path.join(RESULTS_DIR, "layered_t1_cbd_collapse.csv"))
    
    # Build list of scenarios
    scenarios = []
    
    # 1. Baseline
    scenarios.append({
        "Scenario": "T1.1 Baseline (0% Noise)",
        "alpha_MAE": np.abs(df_t11["alpha_recovered"] - df_t11["alpha_gt"]).mean(),
        "beta_MAE": np.abs(df_t11["beta_recovered"] - df_t11["beta_gt"]).mean()
    })
    
    # 2. Perturbation noise
    for noise in [0.1, 0.2, 0.5]:
        sub = df_t13[df_t13["noise"] == noise]
        scenarios.append({
            "Scenario": f"T1.3 Perturbation {int(noise*100)}% Noise",
            "alpha_MAE": np.abs(sub["alpha_pert"] - sub["alpha_gt"]).mean(),
            "beta_MAE": np.abs(sub["beta_pert"] - sub["beta_gt"]).mean()
        })
        
    # 3. Masking
    for mask in [0.1, 0.2, 0.5]:
        sub = df_t14[df_t14["mask_pct"] == mask]
        scenarios.append({
            "Scenario": f"T1.4 Masking {int(mask*100)}% Zones",
            "alpha_MAE": np.abs(sub["alpha_mask"] - sub["alpha_gt"]).mean(),
            "beta_MAE": np.abs(sub["beta_mask"] - sub["beta_gt"]).mean()
        })
        
    # 4. CBD collapse
    scenarios.append({
        "Scenario": "T1.5a CBD Collapse (Mean)",
        "alpha_MAE": np.abs(df_t15["alpha_cbd_mean"] - df_t15["alpha_gt"]).mean(),
        "beta_MAE": np.abs(df_t15["beta_cbd_mean"] - df_t15["beta_gt"]).mean()
    })
    scenarios.append({
        "Scenario": "T1.5b CBD Collapse (80% Drop)",
        "alpha_MAE": np.abs(df_t15["alpha_cbd_reduce"] - df_t15["alpha_gt"]).mean(),
        "beta_MAE": np.abs(df_t15["beta_cbd_reduce"] - df_t15["beta_gt"]).mean()
    })
    
    df_heat = pd.DataFrame(scenarios).set_index("Scenario")
    
    # Plot heatmap
    plt.figure(figsize=(10, 8))
    
    # We will use two heatmaps next to each other or a combined heatmap with formatted annotations
    sns.heatmap(df_heat, annot=True, fmt=".4f", cmap="YlOrRd", cbar=True,
                linewidths=0.5, annot_kws={"size": 11})
    
    plt.title("Layer 1 Decay Identifiability Robustness Heatmap (MAE)")
    plt.ylabel("")
    plt.xlabel("Parameter Error Metric")
    plt.tight_layout()
    
    plt.savefig(os.path.join(FIGURES_DIR, "layer1_robustness_heatmap.png"), dpi=300)
    plt.close()
    print("Saved -> figures/layer1_robustness_heatmap.png")

if __name__ == "__main__":
    plot_scatters()
    plot_heatmap()
