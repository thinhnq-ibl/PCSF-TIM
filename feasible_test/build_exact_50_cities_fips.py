"""
Inspect all 56 FIPS codes across all 50 cities in data/
Build exact FIPS-to-State/County mapping for 100% precise GADM Level 2 matching.
"""

import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
META_CSV_PATH = ROOT_DIR / "meta_prior" / "movement-distribution-maps_2026-04-01_2026-04-16.csv"

def inspect_fips_details():
    cities = sorted([d.name for d in DATA_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")])
    
    records = []
    for city in cities:
        meta_file = DATA_DIR / city / "meta.csv"
        if meta_file.exists():
            meta_df = pd.read_csv(meta_file)
            if "county_fips" in meta_df.columns:
                fips_list = meta_df["county_fips"].dropna().astype(int).unique()
                for f in fips_list:
                    records.append({"city": city, "fips": f})
                    
    df_fips = pd.DataFrame(records)
    print(f"Total city-fips records: {len(df_fips)}")
    print(f"Unique FIPS codes: {df_fips['fips'].nunique()}")
    
    # Load US Meta MDM
    meta_raw = pd.read_csv(META_CSV_PATH)
    us_meta = meta_raw[meta_raw["country"] == "USA"].copy()
    
    # Display sample gadm_id and gadm_name
    unique_gadm = us_meta[["gadm_id", "gadm_name"]].drop_duplicates()
    print(f"Total GADM Level 2 regions in US Meta MDM: {len(unique_gadm)}")
    
    print("\nAll FIPS found in 50 cities:")
    for city, grp in df_fips.groupby("city"):
        f_str = ", ".join([str(x) for x in grp["fips"].tolist()])
        print(f"City: {city:<20} FIPS: {f_str}")

if __name__ == "__main__":
    inspect_fips_details()
