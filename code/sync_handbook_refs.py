#!/usr/bin/env python3
"""
sync_handbook_refs.py
---------------------
Automatically syncs the References section in Handbook.md directly from handbook_references.bib.
Usage:
    python3 code/sync_handbook_refs.py
"""

import os
import re

HANDBOOK_PATH = "Handbook.md"
BIB_PATH = "handbook_references.bib"

def parse_bib_file(bib_path):
    if not os.path.exists(bib_path):
        raise FileNotFoundError(f"Bib file not found: {bib_path}")
    
    with open(bib_path, "r", encoding="utf-8") as f:
        content = f.read()

    entries = {}
    blocks = content.split("@")
    for b in blocks:
        if not b.strip():
            continue
        header = b.strip().split("\n")[0]
        if "{" in header:
            key = header.split("{")[1].split(",")[0].strip()
            # Extract fields
            author_m = re.search(r"author\s*=\s*[\"\{](.*?)[\"\}]\s*[,}]", b, re.DOTALL | re.IGNORECASE)
            title_m = re.search(r"title\s*=\s*[\"\{](.*?)[\"\}]\s*[,}]", b, re.DOTALL | re.IGNORECASE)
            year_m = re.search(r"year\s*=\s*[\"\{](.*?)[\"\}]\s*[,}]", b, re.DOTALL | re.IGNORECASE)
            journal_m = re.search(r"(journal|booktitle|institution|publisher)\s*=\s*[\"\{](.*?)[\"\}]\s*[,}]", b, re.DOTALL | re.IGNORECASE)
            
            author = author_m.group(1).replace("\n", " ").replace("{", "").replace("}", "").strip() if author_m else "Unknown"
            title = title_m.group(1).replace("\n", " ").replace("{", "").replace("}", "").strip() if title_m else "Untitled"
            year = year_m.group(1).strip() if year_m else "n.d."
            journal = journal_m.group(2).replace("\n", " ").replace("{", "").replace("}", "").strip() if journal_m else ""
            
            entries[key] = {
                "author": author,
                "title": title,
                "year": year,
                "journal": journal,
                "raw_bib": "@" + b.strip()
            }
    return entries

def update_handbook_refs():
    bib_entries = parse_bib_file(BIB_PATH)
    
    with open(HANDBOOK_PATH, "r", encoding="utf-8") as f:
        hb_content = f.read()

    # Generate Markdown Summary Table
    table_lines = [
        "## References Summary / Danh mục Tài liệu Tham khảo (Auto-synced from `handbook_references.bib`)\n",
        "> **Note:** This section is linked to [`handbook_references.bib`](file:///Users/nguyenquocthinh/Documents/PCSF-TIM/handbook_references.bib). Run `python3 code/sync_handbook_refs.py` to refresh.\n",
        "| Ref ID | Reference | Year | BibTeX key |",
        "| :--- | :--- | :--- | :--- |"
    ]

    for idx, (key, entry) in enumerate(sorted(bib_entries.items()), 1):
        ref_desc = f"{entry['author']} *{entry['title']}*, {entry['journal']}".strip(", ")
        table_lines.append(f"| R{idx} | {ref_desc} | {entry['year']} | `{key}` |")

    new_ref_section = "\n".join(table_lines) + "\n"

    # Replace existing References section if present
    ref_marker = "## References Summary"
    if ref_marker in hb_content:
        base_content = hb_content.split(ref_marker)[0].strip()
        updated_content = base_content + "\n\n---\n\n" + new_ref_section
    else:
        updated_content = hb_content.strip() + "\n\n---\n\n" + new_ref_section

    with open(HANDBOOK_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Successfully synced {len(bib_entries)} references from {BIB_PATH} into {HANDBOOK_PATH}.")

if __name__ == "__main__":
    update_handbook_refs()
