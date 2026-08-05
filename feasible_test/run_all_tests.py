"""
Master Execution Script for Full Feasibility Test Suite (Quick Tests 1 - 19)
"""
import os
import sys
import time
import json
import pandas as pd
from pathlib import Path

FEASIBLE_DIR = Path(__file__).parent
sys.path.insert(0, str(FEASIBLE_DIR))

from quick_test_1 import run_test_1
from quick_test_2 import run_test_2
from quick_test_3 import run_test_3
from quick_test_4 import run_test_4
from quick_test_5 import run_test_5
from quick_test_6 import run_test_6
from quick_test_7 import run_test_7
from quick_test_8 import run_test_8
from quick_test_9 import run_test_9
from quick_test_10 import run_test_10
from quick_test_11 import run_test_11
from quick_test_12 import run_test_12
from quick_test_13 import run_test_13
from quick_test_14 import run_test_14
from quick_test_15 import run_test_15
from quick_test_16 import run_test_16
from quick_test_17 import run_test_17
from quick_test_18 import run_test_18
from quick_test_19 import run_test_19

def main():
    print("#" * 70)
    print("STARTING FULL EXTENDED FEASIBILITY TEST SUITE (TESTS 1 - 19)")
    print("#" * 70)

    start_time = time.time()
    summary = {}

    # Core Tests 1 - 11
    t0 = time.time()
    _, r2_qt1 = run_test_1()
    summary["Quick_Test_1"] = {"R2_beta_OD_vs_TLD": float(r2_qt1), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    _, cv_qt2 = run_test_2()
    summary["Quick_Test_2"] = {"CV_beta": float(cv_qt2), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    _, avg_own_3, avg_wrong_3 = run_test_3()
    summary["Quick_Test_3"] = {"CPC_own": float(avg_own_3), "CPC_wrong": float(avg_wrong_3), "CPC_drop": float(avg_own_3 - avg_wrong_3), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    r2_qt4 = run_test_4()
    summary["Quick_Test_4"] = {"R2_5fold_CV_Oi": float(r2_qt4), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    r2_qt5 = run_test_5()
    summary["Quick_Test_5"] = {"R2_5fold_CV_Aj": float(r2_qt5), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    imp_df = run_test_6()
    summary["Quick_Test_6"] = {"Top_Feature_Oi": imp_df.iloc[0]["feature"], "Top_Feature_Aj": imp_df.sort_values(by="importance_Aj", ascending=False).iloc[0]["feature"], "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    _, r2_O_7, r2_A_7 = run_test_7()
    summary["Quick_Test_7"] = {"ZeroShot_Test_R2_Oi": float(r2_O_7), "ZeroShot_Test_R2_Aj": float(r2_A_7), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    _, cpc_qt8 = run_test_8()
    summary["Quick_Test_8"] = {"Dissertation_Mean_CPC": float(cpc_qt8), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    cpc_mat, scenario, diag_adv = run_test_9()
    summary["Quick_Test_9"] = {"Scenario": scenario, "Diagonal_Advantage_Delta_CPC": float(diag_adv), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    summary_10 = run_test_10()
    summary["Quick_Test_10"] = {
        "JSD_Improvement_pct": float(summary_10.loc[summary_10['Metric']=='JSD (TLD Divergence)', 'Pct_Improvement'].values[0]),
        "AvgDist_Error_Improvement_pct": float(summary_10.loc[summary_10['Metric']=='Delta Avg Distance (km)', 'Pct_Improvement'].values[0]),
        "runtime_s": round(time.time() - t0, 2)
    }

    t0 = time.time()
    _, top_sens, top_insens = run_test_11()
    summary["Quick_Test_11"] = {
        "Most_Sensitive_City": top_sens.iloc[0]["city"],
        "Least_Sensitive_City": top_insens.iloc[0]["city"],
        "runtime_s": round(time.time() - t0, 2)
    }

    # Decisive Science Tests 12 - 19
    t0 = time.time()
    _, _, cv_12, synth_err_12 = run_test_12()
    summary["Quick_Test_12"] = {"Multi_Start_CV_pct": float(cv_12 * 100), "Synthetic_Recovery_Error_pct": float(synth_err_12 * 100), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    df_13 = run_test_13()
    summary["Quick_Test_13"] = {"Expanded_Delta_R2_Oi": float(df_13["delta_r2_Oi"].values[0]), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    df_14 = run_test_14()
    summary["Quick_Test_14"] = {"Best_NonSpatial_R2": float(df_14["R2_Oi"].max()), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    df_15 = run_test_15()
    summary["Quick_Test_15"] = {"CPC_Noise_50pct": float(df_15.loc[df_15["noise_level"]==0.5, "mean_cpc"].values[0]), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    df_16 = run_test_16()
    summary["Quick_Test_16"] = {"Eta2_Structure_pct": float(df_16["Eta2_Structure_pct"].values[0]), "Eta2_Behaviour_pct": float(df_16["Eta2_Behaviour_pct"].values[0]), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    _, r2_O_17, r2_A_17, test_cpc_17 = run_test_17()
    summary["Quick_Test_17"] = {"Test_R2_Oi": float(r2_O_17), "Test_Downstream_CPC": float(test_cpc_17), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    df_18 = run_test_18()
    summary["Quick_Test_18"] = {"Beta_Error_Noise_20pct": float(df_18.loc[df_18["noise_level"]==0.2, "mean_beta_error_pct"].values[0]), "runtime_s": round(time.time() - t0, 2)}

    t0 = time.time()
    df_19 = run_test_19()
    summary["Quick_Test_19"] = {"R2_40_train_cities": float(df_19.loc[df_19["n_train_cities"]==40, "r2_Oi"].values[0]), "runtime_s": round(time.time() - t0, 2)}

    total_time = round(time.time() - start_time, 2)
    summary["Total_Execution_Time_s"] = total_time

    # Save summary json
    results_dir = FEASIBLE_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    with open(results_dir / "summary_results.json", "w") as f:
        json.dump(summary, f, indent=4)

    print("\n" + "#" * 70)
    print("ALL 19 QUICK TESTS COMPLETED SUCCESSFULLY!")
    print(f"Total Execution Time: {total_time} seconds")
    print(f"Summary JSON saved to {results_dir / 'summary_results.json'}")
    print("#" * 70)

if __name__ == "__main__":
    main()
