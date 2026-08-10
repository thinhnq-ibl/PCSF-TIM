"""
Search the workspace for all Meta MDM datasets and check date ranges.
"""

import os
import sys
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

def find_all_meta_csvs():
    print("="*75)
    print("      SEARCHING FOR ALL META MDM DATASETS IN WORKSPACE")
    print("="*75)
    
    meta_files = list(ROOT_DIR.glob("**/*movement*distribution*.csv")) + list(ROOT_DIR.glob("**/meta_prior/*.csv")) + list(ROOT_DIR.glob("**/*meta*.csv"))
    
    unique_files = sorted(list(set(meta_files)))
    print(f"Found {len(unique_files)} potential Meta files:\n")
    
    for f in unique_files:
        rel_path = f.relative_to(ROOT_DIR)
        size_mb = f.stat().st_size / (1024 * 1024)
        print(f"- {rel_path} ({size_mb:.2f} MB)")
        
        # Check if it looks like Meta MDM dataset
        try:
            df = pd.read_csv(f, nrows=100)
            if "ds" in df.columns or "date" in df.columns or "home_to_ping_distance_category" in df.columns:
                full_df = pd.read_csv(f)
                date_col = "ds" if "ds" in full_df.columns else "date"
                if date_col in full_df.columns:
                    unique_dates = full_df[date_col].unique()
                    print(f"  --> Contains {len(unique_dates)} unique dates: from {min(unique_dates)} to {max(unique_dates)}")
                    print(f"  --> Total rows: {len(full_df)}")
        except Exception as e:
            pass
            
    print("="*75 + "\n")

if __name__ == "__main__":
    find_all_meta_csvs()
