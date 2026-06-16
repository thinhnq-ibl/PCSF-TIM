import pandas as pd
import numpy as np
from scipy import stats
import os

def main():
    # Load per-city metrics
    csv_path = "prepare_for_paper/results/loco_50fold_per_city_cpc.csv"
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path)
    
    # Target models for comparison
    models = {
        "DeepGravity": "DeepGravity_cpc",
        "TraditionalGravity": "TraditionalGravity_cpc",
        "Radiation": "Radiation_cpc"
    }
    
    pcf_cpc = df["PCF_CTF_cpc"].values
    
    rows = []
    print("=== Statistical Significance Tests (N = 50 cities) ===")
    print(f"{'Baseline Model':<22} | {'Mean Diff':<10} | {'t-stat':<8} | {'t-pval':<10} | {'W-stat':<8} | {'W-pval':<10} | {'95% CI Diff':<22} | {'Cohen d':<8}")
    print("-" * 115)
    
    for model_name, col_name in models.items():
        if col_name not in df.columns:
            # Handle possible missing column for comparison (e.g. TraditionalGravity if named differently)
            # We see TraditionalGravity_cpc, DeepGravity_cpc, Radiation_cpc in loco_50fold_per_city_cpc.csv
            continue
            
        base_cpc = df[col_name].values
        # Diff = PCF_CTF - Baseline (so positive means PCF is better)
        diff = pcf_cpc - base_cpc
        mean_diff = np.mean(diff)
        
        # Paired t-test
        t_stat, t_pval = stats.ttest_rel(pcf_cpc, base_cpc)
        
        # Wilcoxon signed-rank test
        w_stat, w_pval = stats.wilcoxon(pcf_cpc, base_cpc)
        
        # Confidence interval of the difference (95%)
        sem = stats.sem(diff)
        ci_half = sem * stats.t.ppf((1 + 0.95) / 2., len(diff) - 1)
        ci_str = f"[{mean_diff - ci_half:.4f}, {mean_diff + ci_half:.4f}]"
        
        # Effect size (Cohen's d for paired samples: mean_diff / std_diff)
        std_diff = np.std(diff, ddof=1)
        cohen_d = mean_diff / std_diff if std_diff > 1e-9 else 0.0
        
        print(f"{model_name:<22} | {mean_diff:<10.4f} | {t_stat:<8.4f} | {t_pval:<10.3e} | {w_stat:<8.1f} | {w_pval:<10.3e} | {ci_str:<22} | {cohen_d:<8.4f}")
        
        rows.append({
            "Baseline Model": model_name,
            "Mean Difference": round(float(mean_diff), 4),
            "Paired t-test (t)": round(float(t_stat), 4),
            "t-test p-value": float(t_pval),
            "Wilcoxon W": float(w_stat),
            "Wilcoxon p-value": float(w_pval),
            "95% CI Diff": ci_str,
            "Cohen d": round(float(cohen_d), 4)
        })

    # Save to markdown report
    output_md_path = "prepare_for_paper/results/loco_50fold_statistical_tests.md"
    with open(output_md_path, "w") as f:
        f.write("# Statistical Significance Tests (Zero-Shot LOCO 50 Folds)\n\n")
        f.write("Comparing the proposed **PCF-CTF (Zero-Shot Survey-Free)** against baseline models.\n\n")
        f.write("| Baseline Model | Mean Difference | Paired t-test ($t$) | $p$-value (t-test) | Wilcoxon $W$ | $p$-value (Wilcoxon) | 95% CI of Diff | Cohen's $d$ | Significant ($p < 0.05$)? |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
        for r in rows:
            sig = "**Yes**" if r["t-test p-value"] < 0.05 else "No"
            f.write(f"| **{r['Baseline Model']}** | {r['Mean Difference']:.4f} | {r['Paired t-test (t)']:.4f} | {r['t-test p-value']:.3e} | {r['Wilcoxon W']:.1f} | {r['Wilcoxon p-value']:.3e} | {r['95% CI Diff']} | {r['Cohen d']:.4f} | {sig} |\n")
            
    print(f"\nSaved report to {output_md_path}")

if __name__ == "__main__":
    main()
