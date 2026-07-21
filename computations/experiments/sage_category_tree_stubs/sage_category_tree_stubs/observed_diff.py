"""Structural diff of two observed Sage manifests (version-bump step 3–4)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .design_sources import load_json
from .observed_build import OBSERVED_PATH


def _cat_index(observed: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for cat in observed.get("categories", []):
        key = cat.get("inventory_category_id") or cat["id"]
        out[key] = cat
    return out


def _edge_set(cat: dict[str, Any]) -> set[tuple[str | None, str | None]]:
    edges: set[tuple[str | None, str | None]] = set()
    for e in cat.get("immediate_supercategories") or []:
        edges.add((e.get("target"), e.get("sage_name")))
    return edges


def diff_observed(
    old: dict[str, Any],
    new: dict[str, Any],
) -> dict[str, Any]:
    old_cats = _cat_index(old)
    new_cats = _cat_index(new)
    old_keys = set(old_cats)
    new_keys = set(new_cats)

    added = sorted(new_keys - old_keys)
    removed = sorted(old_keys - new_keys)

    parent_changes: list[dict[str, Any]] = []
    axiom_changes: list[dict[str, Any]] = []
    for key in sorted(old_keys & new_keys):
        a, b = old_cats[key], new_cats[key]
        ea, eb = _edge_set(a), _edge_set(b)
        if ea != eb:
            parent_changes.append(
                {
                    "category": key,
                    "qualname": b.get("qualname"),
                    "removed_edges": sorted(ea - eb),
                    "added_edges": sorted(eb - ea),
                }
            )
        ax_a = set(a.get("defined_axioms") or [])
        ax_b = set(b.get("defined_axioms") or [])
        if ax_a != ax_b:
            axiom_changes.append(
                {
                    "category": key,
                    "added": sorted(ax_b - ax_a),
                    "removed": sorted(ax_a - ax_b),
                }
            )

    old_axioms = {a["name"] for a in old.get("axioms", [])}
    new_axioms = {a["name"] for a in new.get("axioms", [])}
    old_cons = {c["name"] for c in old.get("constructions", [])}
    new_cons = {c["name"] for c in new.get("constructions", [])}

    old_aliases = {(a["alias"], a["canonical"]) for a in old.get("aliases", [])}
    new_aliases = {(a["alias"], a["canonical"]) for a in new.get("aliases", [])}

    return {
        "old_sage_version": (old.get("manifest") or {}).get("sage_version"),
        "new_sage_version": (new.get("manifest") or {}).get("sage_version"),
        "categories_added": added,
        "categories_removed": removed,
        "immediate_supercategory_changes": parent_changes,
        "defined_axiom_changes": axiom_changes,
        "axioms_added": sorted(new_axioms - old_axioms),
        "axioms_removed": sorted(old_axioms - new_axioms),
        "constructions_added": sorted(new_cons - old_cons),
        "constructions_removed": sorted(old_cons - new_cons),
        "aliases_added": sorted(new_aliases - old_aliases),
        "aliases_removed": sorted(old_aliases - new_aliases),
    }


def format_diff_report(diff: dict[str, Any]) -> str:
    lines = [
        "Observed Sage structural diff",
        f"  {diff.get('old_sage_version')} → {diff.get('new_sage_version')}",
        f"  categories added:   {len(diff['categories_added'])}",
        f"  categories removed: {len(diff['categories_removed'])}",
        f"  parent edge changes:{len(diff['immediate_supercategory_changes'])}",
        f"  axiom def changes:  {len(diff['defined_axiom_changes'])}",
        f"  axioms added:       {len(diff['axioms_added'])}",
        f"  constructions +/-:  "
        f"{len(diff['constructions_added'])}/{len(diff['constructions_removed'])}",
    ]
    for key in (
        "categories_added",
        "categories_removed",
        "axioms_added",
        "axioms_removed",
        "constructions_added",
        "constructions_removed",
    ):
        items = diff.get(key) or []
        if not items:
            continue
        lines.append(f"{key}:")
        for item in items[:30]:
            lines.append(f"  - {item}")
        if len(items) > 30:
            lines.append(f"  … ({len(items) - 30} more)")
    for row in (diff.get("immediate_supercategory_changes") or [])[:20]:
        lines.append(
            f"  parentΔ {row['qualname']}: "
            f"+{len(row['added_edges'])} -{len(row['removed_edges'])}"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "old",
        type=Path,
        help="Previous observed.json",
    )
    parser.add_argument(
        "new",
        type=Path,
        nargs="?",
        default=OBSERVED_PATH,
        help="New observed.json (default: design/sage/observed.json)",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args(argv)
    old = load_json(args.old)
    new = load_json(args.new)
    diff = diff_observed(old, new)
    if args.json:
        print(json.dumps(diff, indent=2))
    else:
        print(format_diff_report(diff))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
