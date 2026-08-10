"""
Inspect all cities in data/ and extract FIPS county codes for all 50 cities.
Check overlap with Meta MDM dataset (meta_prior/movement-distribution-maps_2026-04-01_2026-04-16.csv).
"""

import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
META_CSV_PATH = ROOT_DIR / "meta_prior" / "movement-distribution-maps_2026-04-01_2026-04-16.csv"

def inspect_all_cities():
    cities = sorted([d.name for d in DATA_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")])
    print(f"Total city directories in data/: {len(cities)}")
    
    # Load raw Meta MDM to check available US counties
    meta_raw = pd.read_csv(META_CSV_PATH)
    us_meta = meta_raw[meta_raw["country"] == "USA"].copy()
    us_meta["gadm_id"] = us_meta["gadm_id"].astype(str)
    
    print(f"Total US Meta MDM rows: {len(us_meta)}, unique GADM Level 2 regions: {us_meta['gadm_id'].nunique()}")
    
    city_county_map = {}
    fips_to_city = {}
    
    for city in cities:
        meta_file = DATA_DIR / city / "meta.csv"
        if meta_file.exists():
            df_meta = pd.read_csv(meta_file)
            if "county_fips" in df_meta.columns:
                unique_fips = df_meta["county_fips"].dropna().astype(int).unique()
                city_county_map[city] = unique_fips.tolist()
                for f in unique_fips:
                    if f not in fips_to_city:
                        fips_to_city[f] = []
                    fips_to_city[f].append(city)
            else:
                print(f"City {city}: meta.csv has no 'county_fips' column.")
        else:
            print(f"City {city}: meta.csv missing.")
            
    print(f"\nExtracted FIPS codes across all {len(cities)} cities:")
    print(f"Total unique FIPS codes found: {len(fips_to_city)}")
    
    # Match with US Meta MDM
    # Meta MDM gadm_id for US is formatted like 'USA.36.31_1' or FIPS codes
    print("\nSample GADM IDs in US Meta MDM:")
    print(us_meta[["gadm_id", "gadm_name"]].drop_duplicates().head(20))
    
    return city_county_map, us_meta

if __name__ == "__main__":
    inspect_all_cities()
