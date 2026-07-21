#!/usr/bin/env python3
"""Noncircular Lean ledger gate.

Consumes ``ncg-export-full`` JSON (stdin or ``--json PATH``). Rejects any
payload that came from the Python semantic seed / ``Spec.SeedData``.

This does **not** prove 179/179 constructibility. It proves that the Lean
exporter is the check surface, and reports specimen coverage against the
authored public ledger size when that ledger is available.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SPIKE = Path(__file__).resolve().parents[1]
STUBS = SPIKE.parent / "sage_category_tree_stubs"
AUTHORED_MANIFEST = (
    STUBS
    / "design"
    / "sage"
    / "authored"
    / "sage_normalized_category_mapping_manifest.json"
)
EXPECTED_PUBLIC = 179


def load_payload(path: Path | None) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8") if path else sys.stdin.read()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise SystemExit("export payload must be a JSON object")
    return data


def validate_lean_registry(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("source") != "lean-registry":
        errors.append(
            f"expected source=lean-registry (Lean exporter), got {data.get('source')!r}"
        )
    if "seed" in data:
        errors.append("Lean export must not embed a Python seed payload")
    if not data.get("schemaVersion"):
        errors.append("missing schemaVersion")
    cats = data.get("categories")
    if not isinstance(cats, list) or not cats:
        errors.append("categories must be a non-empty array from Lean")
        return errors
    ids: set[str] = set()
    names: set[str] = set()
    for i, cat in enumerate(cats):
        if not isinstance(cat, dict):
            errors.append(f"categories[{i}] is not an object")
            continue
        cid = cat.get("id")
        name = cat.get("canonicalName")
        decl = cat.get("declaration")
        if not isinstance(cid, str) or not cid.startswith("cat."):
            errors.append(f"categories[{i}].id must be a cat.* string, got {cid!r}")
        elif cid in ids:
            errors.append(f"duplicate category id {cid}")
        else:
            ids.add(cid)
        if not isinstance(name, str) or not name:
            errors.append(f"categories[{i}].canonicalName missing")
        elif name in names:
            errors.append(f"duplicate canonicalName {name}")
        else:
            names.add(name)
        if not isinstance(decl, str) or not decl:
            errors.append(f"categories[{i}] ({cid}) missing Lean declaration path")
    aliases = data.get("aliases") or []
    if isinstance(aliases, list):
        for a in aliases:
            if isinstance(a, dict) and a.get("spelling") in names:
                errors.append(
                    f"alias spelling collides with category node: {a.get('spelling')}"
                )
    return errors


def authored_public_count() -> int | None:
    if not AUTHORED_MANIFEST.is_file():
        return None
    manifest = json.loads(AUTHORED_MANIFEST.read_text(encoding="utf-8"))
    rows = manifest.get("rows") or manifest.get("public_rows") or manifest.get("categories")
    if isinstance(rows, list):
        return len(rows)
    total = manifest.get("public_count") or manifest.get("total")
    return int(total) if isinstance(total, int) else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        type=Path,
        default=None,
        help="Path to ncg-export-full JSON (default: stdin)",
    )
    parser.add_argument(
        "--require-full-179",
        action="store_true",
        help="Fail unless Lean export covers exactly 179 public categories",
    )
    args = parser.parse_args()

    data = load_payload(args.json)
    errors = validate_lean_registry(data)
    cats = data.get("categories") if isinstance(data.get("categories"), list) else []
    n = len(cats)
    authored = authored_public_count()
    target = authored if authored is not None else EXPECTED_PUBLIC

    print(
        json.dumps(
            {
                "source": data.get("source"),
                "lean_categories": n,
                "authored_public_target": target,
                "coverage": f"{n}/{target}",
                "complete": n == target,
            },
            sort_keys=True,
        )
    )

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    if args.require_full_179 and n != EXPECTED_PUBLIC:
        print(
            f"Lean export covers {n}/{EXPECTED_PUBLIC}; full 179 not yet authored in Lean",
            file=sys.stderr,
        )
        return 1

    if n == target:
        print(f"OK: {n}/{target} Lean registry categories (full coverage)")
    else:
        print(
            f"OK: Lean registry export valid ({n} categories); "
            f"full coverage {n}/{target} still incomplete"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
