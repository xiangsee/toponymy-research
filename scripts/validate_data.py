#!/usr/bin/env python3
"""Lightweight source-data validation, using Python standard library only.

This checks syntax and bookkeeping, not whether historical claims are true.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows_from(relative: str):
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def validate():
    cases = rows_from("data/seed_cases.csv")
    sources = rows_from("data/source_registry.csv")
    if not cases:
        raise ValueError("Case register cannot be empty")
    if not sources:
        raise ValueError("Source register cannot be empty")

    seen = set()
    allowed = {"QUESTION_ONLY", "IN_RESEARCH", "NEEDS_REVIEW", "CHECKED", "DISPUTED"}
    for idx, case in enumerate(cases, 2):
        cid = case.get("case_id", "").strip()
        if not cid or cid in seen:
            raise ValueError(f"Duplicate/missing case id at line {idx}: {cid!r}")
        if not case.get("name_zh", "").strip():
            raise ValueError(f"Missing name at line {idx}")
        if case.get("claim_status") not in allowed:
            raise ValueError(f"Unexpected case status at line {idx}")
        seen.add(cid)

    source_ids = set()
    for idx, src in enumerate(sources, 2):
        sid = src.get("source_id", "").strip()
        if not sid or sid in source_ids:
            raise ValueError(f"Duplicate/missing source id at line {idx}: {sid!r}")
        if src.get("url") and not src["url"].startswith("https://"):
            raise ValueError(f"Untrusted URL format at line {idx}")
        source_ids.add(sid)

    with (ROOT / "data/toponym_case.schema.json").open(encoding="utf-8") as handle:
        schema = json.load(handle)
    if schema.get("type") != "object":
        raise ValueError("Expected object schema")
    print(f"OK: {len(cases)} initial research questions, {len(sources)} source records, schema JSON syntax valid")
    print("Note: this script does not check historical correctness or source interpretation.")


if __name__ == "__main__":
    validate()
