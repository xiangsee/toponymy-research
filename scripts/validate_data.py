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
    attestations = rows_from("data/p1a_name_attestations.csv")
    catalog_queries = rows_from("data/p1a_catalog_queries.csv")
    relations = rows_from("data/p1a_historical_name_relations.csv")
    if not all((cases, sources, claims, witnesses, attestations,
                catalog_queries, relations)):
        raise ValueError("Research registers cannot be empty")

    case_ids = required_unique(cases, "case_id", "case")
    source_ids = required_unique(sources, "source_id", "source")
    claim_ids = required_unique(claims, "claim_id", "claim")
    witness_ids = required_unique(witnesses, "object_id", "inscription witness")
    attestation_ids = required_unique(attestations, "attestation_id", "name attestation")
    query_ids = required_unique(catalog_queries, "query_id", "catalog query")
    relation_ids = required_unique(relations, "relation_id", "name relation")
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

    for line, attestation in enumerate(attestations, 2):
        case_id = (attestation.get("case_id") or "").strip()
        if case_id not in case_ids:
            raise ValueError(f"attestation line {line}: unknown case {case_id!r}")
        source_refs(attestation.get("source_ids", ""), source_ids, "attestation", line)
        for field in ("catalog_identifier", "role_hypothesis", "source_review_level",
                      "not_established", "verification_next"):
            if not (attestation.get(field) or "").strip():
                raise ValueError(f"attestation line {line}: missing {field}")

    for line, query in enumerate(catalog_queries, 2):
        if query.get("case_id") not in case_ids:
            raise ValueError(f"catalog query line {line}: unknown case {query.get('case_id')!r}")
        source_refs(query.get("source_ids", ""), source_ids, "catalog query", line)
        if not (query.get("normalized_search_number") or "").strip():
            raise ValueError(f"catalog query line {line}: missing search number")
        if query.get("lookup_status") == "QUERY_PLANNED" and (
            query.get("object_identity_status") not in ("SAME_OBJECT_UNKNOWN", "UNVERIFIED")
        ):
            raise ValueError(f"catalog query line {line}: cannot confirm object identity before lookup")
    for line, relation in enumerate(relations, 2):
        for field in ("from_attestation_id", "to_attestation_id"):
            if relation.get(field) not in attestation_ids:
                raise ValueError(f"name relation line {line}: unknown {field}={relation.get(field)!r}")
        source_refs(relation.get("source_ids", ""), source_ids, "name relation", line)
        for field in ("epistemic_status", "evidence_gap", "invalid_inference", "verification_next"):
            if not (relation.get(field) or "").strip():
                raise ValueError(f"name relation line {line}: missing {field}")

    with (ROOT / "data/toponym_case.schema.json").open(encoding="utf-8") as handle:
        schema = json.load(handle)
    if schema.get("type") != "object":
        raise ValueError("Expected object schema")

    print(f"OK: {len(case_ids)} cases, {len(source_ids)} sources, "
          f"{len(claim_ids)} claims, {len(witness_ids)} inscription witnesses, "
          f"{len(attestation_ids)} name attestations, "
          f"{len(query_ids)} catalog queries, {len(relation_ids)} proposed name relations")
    print("Reference IDs, CSV and JSON syntax checked.")
    print("This does NOT validate historical facts, epigraphic readings or geographic identification.")


if __name__ == "__main__":
    validate()
