#!/usr/bin/env python3
"""Download and audit a bounded set of third-party household-flexibility data.

Only public, attributed source URLs. No imputation, joins, or reclassification.
Standard-library only: Python >=3.9.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import time
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "data"

DATASETS = [
    {
        "source": "norway_ev_2024_v2",
        "filename": "Dataset1_charging_reports.csv",
        "url": "https://zenodo.org/records/13896176/files/Dataset1_charging_reports.csv?download=1",
        "md5": "8bb7463d760cc846271b1ed9bdf808fd",
        "data_kind": "measured charging-session events and energy",
    },
    {
        "source": "norway_ev_2024_v2",
        "filename": "Dataset2_user_predictions.csv",
        "url": "https://zenodo.org/records/13896176/files/Dataset2_user_predictions.csv?download=1",
        "md5": "ed0a2c2a2600ca5b5e08f98d7d7d6d10",
        "data_kind": "inferred per-user EV charging power and capacity",
    },
    {
        "source": "norway_ev_2024_v2",
        "filename": "Dataset3_session_predictions.csv",
        "url": "https://zenodo.org/records/13896176/files/Dataset3_session_predictions.csv?download=1",
        "md5": "df82be864494c37f727e19215c62c235",
        "data_kind": "inferred charging-session parameters",
    },
    {
        "source": "opsd_cossmic_2020_04_15",
        "filename": "household_data_60min_singleindex.csv",
        "url": "https://data.open-power-system-data.org/household_data/2020-04-15/household_data_60min_singleindex.csv",
        "md5": None,
        "data_kind": "meter-based hourly consumption/generation; gaps may be interpolated",
    },
]

def fetch(entry: dict, timeout: int = 90) -> dict:
    path = OUTPUT / entry["source"] / entry["filename"]
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".part")
    last_error = None
    for attempt in range(1, 4):
        try:
            request = Request(entry["url"], headers={"User-Agent": "AcademicDataReproduction/1.0"})
            sha256 = hashlib.sha256()
            md5 = hashlib.md5()
            count = 0
            with urlopen(request, timeout=timeout) as response, tmp.open("wb") as out:
                while True:
                    block = response.read(1024 * 1024)
                    if not block:
                        break
                    out.write(block)
                    sha256.update(block)
                    md5.update(block)
                    count += len(block)
                    if count > 65 * 1024 * 1024:
                        raise ValueError("unexpected size: exceeds 65 MiB guard")
            if not count:
                raise ValueError("empty response")
            if entry["md5"] and md5.hexdigest() != entry["md5"]:
                raise ValueError(f"published MD5 mismatch (got {md5.hexdigest()})")
            os.replace(tmp, path)
            return {
                "source": entry["source"], "file": str(path.relative_to(ROOT)),
                "data_kind": entry["data_kind"], "url": entry["url"],
                "status": "downloaded", "size_bytes": count,
                "sha256": sha256.hexdigest(), "md5": md5.hexdigest(),
                "published_md5": entry["md5"],
            }
        except Exception as exc:
            tmp.unlink(missing_ok=True)
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < 3:
                time.sleep(attempt * 2)
    return {
        "source": entry["source"], "file": str(path.relative_to(ROOT)),
        "url": entry["url"], "status": "failed", "reason": last_error,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=["all", "norway", "opsd"], default="all")
    args = parser.parse_args()
    selected = [
        item for item in DATASETS
        if args.only == "all" or
        (args.only == "norway" and item["source"].startswith("norway")) or
        (args.only == "opsd" and item["source"].startswith("opsd"))
    ]
    records = []
    for entry in selected:
        print(f"Fetching: {entry['source']}/{entry['filename']}", flush=True)
        result = fetch(entry)
        records.append(result)
        print(result["status"], result.get("size_bytes", result.get("reason", "")), flush=True)
    manifest = {
        "note": "Measured vs model-derived fields are distinguished in the README.",
        "records": records,
    }
    (ROOT / "download_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    success = sum(r["status"] == "downloaded" for r in records)
    print(f"Verified downloads: {success}/{len(records)}")
    return 0 if success else 1

if __name__ == "__main__":
    raise SystemExit(main())
