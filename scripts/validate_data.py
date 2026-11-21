#!/usr/bin/env python3
"""Validate reference integrity, IDs and syntax of public research registers.

This checks bookkeeping only: it CANNOT determine if historical claims are true.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows_from(relative: str):
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def required_unique(rows, id_col: str, label: str):
    seen = set()
    for line, item in enumerate(rows, 2):
        value = (item.get(id_col) or "").strip()
        if not value or value in seen:
            raise ValueError(f"{label} at line {line}: duplicate/missing {id_col}: {value!r}")
        seen.add(value)
    return seen


def source_refs(refs: str, known: set[str], label: str, line: int):
    for ref in (refs or "").split("|"):
        if ref.strip() and ref.strip() not in known:
            raise ValueError(f"{label} line {line}: unknown source {ref!r}")


def validate():
    cases = rows_from("data/seed_cases.csv")
    sources = rows_from("data/source_registry.csv")
    claims = rows_from("data/p1a_claim_register.csv")
    witnesses = rows_from("data/p1a_inscription_register.csv")
    if not all((cases, sources, claims, witnesses)):
        raise ValueError("Research registers cannot be empty")

    case_ids = required_unique(cases, "case_id", "case")
    source_ids = required_unique(sources, "source_id", "source")
    claim_ids = required_unique(claims, "claim_id", "claim")
    witness_ids = required_unique(witnesses, "object_id", "inscription witness")
    for line, case in enumerate(cases, 2):
        if not (case.get("name_zh") or "").strip():
            raise ValueError(f"Missing name at line {line}")
        if case.get("claim_status") not in {
            "QUESTION_ONLY", "IN_RESEARCH", "NEEDS_REVIEW", "CHECKED", "DISPUTED"
        }:
            raise ValueError(f"Unexpected case status at line {line}")
    for line, source in enumerate(sources, 2):
        url = source.get("url") or ""
        if url and not url.startswith("https://"):
            raise ValueError(f"Untrusted URL format at line {line}")

    for line, claim in enumerate(claims, 2):
        source_refs(claim.get("source_ids", ""), source_ids, "claim", line)
        if not (claim.get("not_established") or "").strip():
            raise ValueError(f"Missing claim limitations at line {line}")
    for line, witness in enumerate(witnesses, 2):
        source_refs(witness.get("source_ids", ""), source_ids, "witness", line)
        if not (witness.get("verification_next") or "").strip():
            raise ValueError(f"Missing witness verification_next at line {line}")

    with (ROOT / "data/toponym_case.schema.json").open(encoding="utf-8") as handle:
        schema = json.load(handle)
    if schema.get("type") != "object":
        raise ValueError("Expected object schema")

    print(f"OK: {len(case_ids)} cases, {len(source_ids)} sources, "
          f"{len(claim_ids)} claims, {len(witness_ids)} inscription witnesses")
    print("Reference IDs, CSV and JSON syntax checked.")
    print("This does NOT validate historical facts, epigraphic readings or geographic identification.")


if __name__ == "__main__":
    validate()
