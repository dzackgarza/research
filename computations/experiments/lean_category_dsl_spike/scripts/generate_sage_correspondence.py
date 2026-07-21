#!/usr/bin/env python3
"""Regenerate Realization/Sage/Correspondence.lean from correspondence.json."""

from __future__ import annotations

import json
from pathlib import Path

SPIKE = Path(__file__).resolve().parents[1]
STUBS = SPIKE.parent / "sage_category_tree_stubs"
SRC = STUBS / "design/sage_to_normalized_map/correspondence.json"
OUT = SPIKE / "NormalizedCategoryGraph/Realization/Sage"


def main() -> int:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    payload = {
        "schemaVersion": "0.1.0",
        "sage_to_graph": data["sage_to_graph"],
        "graph_to_sage": data["graph_to_sage"],
        "axiom_sage_to_graph": data.get("axiom_sage_to_graph") or {},
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "correspondence.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    raw = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    esc = raw.replace("\\", "\\\\").replace('"', '\\"')
    lean = f"""/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Ids

/-!
# Sage realization — name ↔ stable-id correspondence

Generated from `sage_category_tree_stubs/design/sage_to_normalized_map/correspondence.json`.
Do not edit by hand; regenerate with `scripts/generate_sage_correspondence.py`.
-/

namespace NormalizedCategoryGraph.Realization.Sage

open NormalizedCategoryGraph

/-- Full Sage ↔ graph correspondence as deterministic JSON. -/
def correspondenceJson : String :=
  "{esc}"

theorem sage_magmas_id : CategoryId.magmas.raw = "cat.magmas" := rfl
theorem sage_sets_id : CategoryId.sets.raw = "cat.sets" := rfl
theorem sage_comm_rings_id : CategoryId.commutativeRings.raw = "cat.commutative_rings" := rfl

theorem correspondence_mentions_magmas :
    correspondenceJson.contains "cat.magmas" = true := by
  native_decide

end NormalizedCategoryGraph.Realization.Sage
"""
    (OUT / "Correspondence.lean").write_text(lean, encoding="utf-8")
    print(f"wrote Realization/Sage ({len(payload['sage_to_graph'])} sage names)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
