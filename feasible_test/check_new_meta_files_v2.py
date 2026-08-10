"""
Scan workspace and meta_prior/ for newly added Meta MDM files and date ranges (v2).
"""

import os
import sys
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
META_PRIOR_DIR = ROOT_DIR / "meta_prior"

def check_new_meta_v2():
    print("="*75)
    print("       CHECKING FOR NEW META MDM FILES & DATES IN WORKSPACE (V2)")
    print("="*75)
    
    meta_files = list(ROOT_DIR.glob("**/*movement*.csv")) + list(ROOT_DIR.glob("**/meta_prior/*.csv")) + list(ROOT_DIR.glob("**/*june*.csv")) + list(ROOT_DIR.glob("**/*july*.csv"))
    unique_files = sorted(list(set(meta_files)))
    
    print(f"Total potential Meta files found: {len(unique_files)}\n")
    
    all_dates = set()
    file_info = []
    
    for f in unique_files:
        rel_path = f.relative_to(ROOT_DIR)
        size_mb = f.stat().st_size / (1024 * 1024)
        
        try:
            df = pd.read_csv(f, nrows=100)
            date_col = None
            if "ds" in df.columns:
                date_col = "ds"
            elif "date" in df.columns:
                date_col = "date"
                
            if date_col:
                full_df = pd.read_csv(f)
                dates = sorted(full_df[date_col].astype(str).unique().tolist())
                all_dates.update(dates)
                
                file_info.append({
                    "path": str(rel_path),
                    "size_mb": size_mb,
                    "n_rows": len(full_df),
                    "n_dates": len(dates),
                    "min_date": min(dates),
                    "max_date": max(dates)
                })
        except Exception as e:
            pass
            
    df_files = pd.DataFrame(file_info)
    print(df_files.to_string(index=False))
    
    sorted_all_dates = sorted(list(all_dates))
    print("\n" + "="*75)
    print(f"TOTAL UNIQUE META DATES ACROSS ALL FILES: {len(sorted_all_dates)}")
    print(f"Date Range: from {min(sorted_all_dates)} to {max(sorted_all_dates)}")
    print("="*75 + "\n")

if __name__ == "__main__":
    check_new_meta_v2()
