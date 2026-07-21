#!/usr/bin/env python3
"""Stage 9: recompute authored 179 ledger rows from the Lean seed manifest.

Does not trust mapping.yaml status strings. Rebuilds the constructibility sketch
from ``Spec/seed_manifest.json``'s embedded seed payload and evaluates every
public authored row.
"""

from __future__ import annotations

import importlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SPIKE = Path(__file__).resolve().parents[1]
STUBS = SPIKE.parent / "sage_category_tree_stubs"
MANIFEST = SPIKE / "NormalizedCategoryGraph/Spec/seed_manifest.json"

sys.path.insert(0, str(STUBS))

_authored_mapping = importlib.import_module("sage_category_tree_stubs.authored_mapping")
_constructibility = importlib.import_module("sage_category_tree_stubs.constructibility")
_semantic_seed = importlib.import_module("sage_category_tree_stubs.semantic_seed")

evaluate_all_public = _authored_mapping.evaluate_all_public
build_sketch = _constructibility.build_sketch
SemanticSeed = _semantic_seed.SemanticSeed


def sketch_from_lean_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    seed_blob = manifest["seed"]
    seed = SemanticSeed(
        entities=tuple(seed_blob["entities"]),
        classifiers=tuple(seed_blob["classifiers"]),
        arrows=tuple(seed_blob["arrows"]),
    )
    return build_sketch(seed)


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "seed" not in manifest:
        print("Lean manifest missing seed payload", file=sys.stderr)
        return 1
    sketch = sketch_from_lean_manifest(manifest)
    rows = evaluate_all_public(sketch=sketch)
    statuses: Counter[str] = Counter()
    bad: list[tuple[object, str]] = []
    for req, result in rows:
        name = getattr(result.status, "name", None) or str(result.status)
        statuses[name] += 1
        if name not in {"CONSTRUCTIBLE", "EXACT_BASE"}:
            bad.append((getattr(req, "source_sage_name", req), name))
    print(dict(statuses))
    print(f"total={len(rows)} bad={len(bad)}")
    for item in bad[:30]:
        print(" ", item)
    if len(rows) != 179:
        print(f"expected 179 public rows, got {len(rows)}", file=sys.stderr)
        return 1
    if bad:
        return 1
    if statuses.get("MISSING_SEED", 0):
        return 1
    print("OK: 179/179 EXACT_BASE|CONSTRUCTIBLE from Lean seed manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
