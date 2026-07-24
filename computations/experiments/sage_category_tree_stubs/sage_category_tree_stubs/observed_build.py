"""Build ``design/sage/observed.json`` from inventory + optional runtime probe.

Empirical only: no mathematical corrections, no property/structure labels.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from .composed_identity import (
    composed_sage_id,
    is_composed_cls_key,
    make_composed_category_record,
)
from .design_sources import DESIGN_ROOT, SAGE_INVENTORY_DIR, load_json

EXTRACTOR_VERSION = "1.2.0"
OBSERVED_PATH = DESIGN_ROOT / "sage" / "observed.json"
RUNTIME_PROBE_PATH = DESIGN_ROOT / "sage" / "runtime_probe.json"

_ROLE_KIND = {
    "public named category class": "category_class",
    "public category wrapper constructor": "named_wrapper",
    "framework/helper category class": "framework_helper",
    "test-only category class": "test_only",
    "example-only category class": "example_only",
}


def _slug(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    return text.strip("_").lower() or "anon"


def _sage_category_id(category_id: str) -> str:
    return f"sage.category.{_slug(category_id)}"


def _sage_axiom_id(name: str) -> str:
    return f"sage.axiom.{_slug(name)}"


def _sage_construction_id(name: str) -> str:
    return f"sage.construction.{_slug(name)}"


def _parse_source(source: str) -> dict[str, Any]:
    path, _, line = source.partition(":")
    try:
        line_n = int(line) if line else None
    except ValueError:
        line_n = None
    return {
        "path": path or None,
        "line_start": line_n,
        "content_hash": None,
    }


def _parse_declared_parents(defining_relation: str | None) -> list[str]:
    """Best-effort source-axis parents from inventory ``defining_relation`` text."""
    if not defining_relation:
        return []
    dr = defining_relation.strip()
    m = re.match(r"(?i)supercategory\s+(\w+)\s*\(\s*\)", dr)
    if m:
        return [m.group(1)]
    m = re.match(r"^(\w+)\s*\+\s*axiom\b", dr, re.I)
    if m:
        return [m.group(1)]
    return []


def _edge(
    target_id: str | None,
    *,
    origin: str,
    probe: str,
    sage_name: str | None = None,
    cls_key: str | None = None,
    repr_text: str | None = None,
) -> dict[str, Any]:
    return {
        "target": target_id,
        "origin": origin,
        "probe": probe,
        "sage_name": sage_name,
        "cls_key": cls_key,
        "repr": repr_text,
    }


def build_observed_from_inventory(
    inventory_path: Path | None = None,
    *,
    runtime_probe_path: Path | None = None,
) -> dict[str, Any]:
    inv_path = inventory_path or (SAGE_INVENTORY_DIR / "sagemath-10.9-category-inventory.json")
    raw = inv_path.read_bytes()
    inventory = json.loads(raw.decode("utf-8"))
    meta = inventory["metadata"]

    probe_path = runtime_probe_path or RUNTIME_PROBE_PATH
    probe: dict[str, Any] | None = None
    if probe_path.is_file():
        probe = load_json(probe_path)

    # This snapshot is a deterministic reading of the pinned inventory and probe, so
    # it dates the observation it derives from rather than the moment of derivation.
    # Stamping the clock here made every rebuild a diff and put the artifact
    # permanently out of reach of a "regeneration leaves the tree clean" gate.
    observed_at = (probe or {}).get("probe", {}).get("generated_at") or meta.get("generated_at")
    assert observed_at, f"neither {probe_path.name} nor the inventory metadata dates the observation; refusing to stamp the current time into a derived artifact"

    categories: list[dict[str, Any]] = []
    for row in inventory["categories"]:
        kind = _ROLE_KIND.get(row.get("role", ""), "category_class")
        cid = _sage_category_id(row["category_id"])
        declared_names = _parse_declared_parents(row.get("defining_relation"))
        categories.append(
            {
                "id": cid,
                "kind": kind,
                "symbol": (f"sage.categories.{row['module'].replace('/', '.')}.{row['constructor']}"),
                "module": row["module"],
                "qualname": row["constructor"],
                "inventory_category_id": row["category_id"],
                "parameters": [],
                "representative": {
                    "expression": f"{row['constructor']}()",
                    "repr": None,
                    "note": "filled from runtime probe when matched",
                },
                "source": {
                    **_parse_source(row.get("source") or ""),
                    "url": row.get("source_url"),
                },
                "immediate_supercategories": [],
                "declared_supercategories": [
                    _edge(
                        None,
                        origin="source",
                        probe="defining_relation",
                        sage_name=name,
                    )
                    for name in declared_names
                ],
                "observed_supercategories": [],
                "defined_axioms": [],
                "available_axioms": [],
                "satisfied_axioms": [],
                "defined_constructions": [],
                "available_constructions": [],
                "aliases": [],
                "deprecated_aliases": [],
                "defining_relation": row.get("defining_relation") or None,
                "notes": row.get("notes") or None,
            }
        )

    by_qual: dict[str, dict[str, Any]] = {c["qualname"]: c for c in categories}
    by_inv: dict[str, dict[str, Any]] = {c["inventory_category_id"]: c for c in categories}
    by_id: dict[str, dict[str, Any]] = {c["id"]: c for c in categories}

    def ensure_composed(cls_key: str, *, repr_text: str | None = None) -> str:
        """Mint / reuse an observed id for a dotted Sage parent."""
        if cls_key in by_qual:
            cid_existing = by_qual[cls_key]["id"]
            assert isinstance(cid_existing, str)
            return cid_existing
        cid = composed_sage_id(cls_key)
        if cid in by_id:
            return cid
        rec = make_composed_category_record(cls_key, repr_text=repr_text)
        categories.append(rec)
        by_qual[cls_key] = rec
        by_id[cid] = rec
        return cid

    def resolve_name(name: str, *, repr_text: str | None = None) -> str | None:
        if not name:
            return None
        if name in by_qual:
            found = by_qual[name]["id"]
            assert isinstance(found, str)
            return found
        bare = re.sub(r"\(.*\)$", "", name).strip()
        if bare in by_qual:
            found = by_qual[bare]["id"]
            assert isinstance(found, str)
            return found
        if is_composed_cls_key(name):
            return ensure_composed(name, repr_text=repr_text)
        return None

    # Resolve declared targets now that the index exists
    for cat in categories:
        for edge in cat["declared_supercategories"]:
            edge["target"] = resolve_name(edge["sage_name"] or "")

    for feat in inventory.get("feature_declarations", []):
        cat_feat = by_inv.get(feat.get("category_id"))
        if cat_feat is None:
            continue
        cat = cat_feat
        if feat.get("feature_type") == "axiom":
            name = feat.get("feature_name")
            if name and name not in cat["defined_axioms"]:
                cat["defined_axioms"].append(name)
        elif feat.get("feature_type") in {"functorial construction", "functorial_construction"}:
            name = feat.get("feature_name")
            if name and name not in cat["defined_constructions"]:
                cat["defined_constructions"].append(name)

    axioms: list[dict[str, Any]] = []
    axiom_by_name: dict[str, dict[str, Any]] = {}
    for row in inventory["axioms"]:
        name = row["axiom"]
        defining = []
        for entry in (row.get("defining_named_categories") or "").split(";"):
            entry = entry.strip()
            if not entry:
                continue
            short = entry.rsplit(".", 1)[-1]
            if short in by_qual:
                defining.append(by_qual[short]["id"])
            else:
                defining.append(f"sage.category.{_slug(entry)}")
        rec = {
            "id": _sage_axiom_id(name),
            "name": name,
            "status": row.get("status"),
            "defining_categories": defining,
            "generated_categories": [],
            "implementation_symbols": [],
            "source": _parse_source(row.get("registry_source") or ""),
            "notes": ("Character (property/structure/stuff) is NOT asserted here; compute from the normalized classifier leg."),
        }
        axioms.append(rec)
        axiom_by_name[name] = rec

    # generated axiom categories from feature_declarations
    for feat in inventory.get("feature_declarations", []):
        if feat.get("feature_type") != "axiom":
            continue
        ax = axiom_by_name.get(feat.get("feature_name") or "")
        if ax is None:
            continue
        base = by_inv.get(feat.get("category_id") or "")
        target_mod = feat.get("target_or_expansion") or ""
        result_short = target_mod.rsplit(".", 1)[-1] if target_mod else ""
        result_id = resolve_name(result_short) or (f"sage.category.{_slug(result_short)}" if result_short else None)
        if base is None or result_id is None:
            continue
        ax["generated_categories"].append(
            {
                "base": base["id"],
                "result": result_id,
                "origin": "feature_declaration",
            }
        )

    constructions: list[dict[str, Any]] = []
    for row in inventory["functorial_constructions"]:
        name = row["construction"]
        construction_defining: list[str] = []
        for part in (row.get("interface_declarations") or "").split(";"):
            part = part.strip()
            if not part or ":" not in part:
                continue
            owner = part.split(":", 1)[0].rsplit(".", 1)[-1]
            rid = resolve_name(owner)
            if rid:
                construction_defining.append(rid)
        constructions.append(
            {
                "id": _sage_construction_id(name),
                "name": name,
                "implementation_symbol": row.get("category_implementation_class"),
                "arity": "variadic",
                "sage_variance": row.get("flavor"),
                "sage_regressive": False,
                "defining_categories": sorted(set(construction_defining)),
                "generated_categories": [],
                "source": _parse_source(row.get("implementation_source") or ""),
                "named_result_categories": [p.strip() for p in (row.get("named_result_categories") or "").split(";") if p.strip()],
            }
        )

    aliases: list[dict[str, Any]] = []
    for row in inventory.get("aliases", []):
        aliases.append(
            {
                "alias": row["alias"],
                "canonical": row["canonical"],
                "module": row.get("module"),
                "status": row.get("status"),
                "source": _parse_source(row.get("source") or ""),
            }
        )

    # Merge runtime probe onto matching inventory categories
    runtime_only: list[dict[str, Any]] = []
    runtime_edge_count = 0
    if probe is not None:
        matched_keys: set[str] = set()
        for inst in probe.get("instances", []):
            key = inst.get("cls_key") or ""
            matched = by_qual.get(key)
            observed_edges: list[dict[str, Any]] = []
            for sup in inst.get("supers", []):
                sk = sup.get("cls_key") or ""
                tid = resolve_name(sk, repr_text=sup.get("repr"))
                observed_edges.append(
                    _edge(
                        tid,
                        origin="runtime",
                        probe="super_categories",
                        sage_name=sk,
                        cls_key=sk,
                        repr_text=sup.get("repr"),
                    )
                )
            runtime_edge_count += len(observed_edges)
            if matched is not None:
                matched_keys.add(key)
                matched["observed_supercategories"] = observed_edges
                matched["immediate_supercategories"] = list(observed_edges)
                matched["satisfied_axioms"] = list(inst.get("axioms") or [])
                matched["representative"] = {
                    "expression": f"{key}()",
                    "repr": inst.get("repr"),
                    "bindings": {},
                    "note": "extraction probe instance from category_sample()",
                }
            elif is_composed_cls_key(key):
                cid = ensure_composed(key, repr_text=inst.get("repr"))
                rec = by_id[cid]
                rec["observed_supercategories"] = observed_edges
                rec["immediate_supercategories"] = list(observed_edges)
                rec["satisfied_axioms"] = list(inst.get("axioms") or [])
                rec["representative"] = {
                    "expression": rec["representative"]["expression"],
                    "repr": inst.get("repr"),
                    "bindings": {},
                    "note": "category_sample() composed instance",
                }
                if inst.get("module"):
                    rec["module"] = inst["module"].replace(".", "/")
            else:
                rid = f"sage.category.runtime.{_slug(key or inst.get('repr') or 'anon')}"
                runtime_only.append(
                    {
                        "id": rid,
                        "kind": inst.get("kind") or "category_instance",
                        "symbol": f"{inst.get('module')}.{inst.get('cls')}",
                        "module": (inst.get("module") or "").replace(".", "/"),
                        "qualname": key or inst.get("cls"),
                        "inventory_category_id": None,
                        "parameters": [],
                        "representative": {
                            "expression": None,
                            "repr": inst.get("repr"),
                            "note": "runtime-only; no inventory class match",
                        },
                        "source": {
                            "path": None,
                            "line_start": None,
                            "content_hash": None,
                        },
                        "immediate_supercategories": observed_edges,
                        "declared_supercategories": [],
                        "observed_supercategories": observed_edges,
                        "defined_axioms": [],
                        "available_axioms": [],
                        "satisfied_axioms": list(inst.get("axioms") or []),
                        "defined_constructions": [],
                        "available_constructions": [],
                        "aliases": [],
                        "deprecated_aliases": [],
                        "defining_relation": None,
                        "notes": "Present in category_sample() but not inventory census",
                    }
                )
        categories.extend(runtime_only)

        # Fallback immediate = declared when no runtime match
        for cat in categories:
            if not cat["immediate_supercategories"] and cat["declared_supercategories"]:
                cat["immediate_supercategories"] = [
                    {**e, "origin": "source", "probe": "defining_relation"} for e in cat["declared_supercategories"] if e.get("target") or e.get("sage_name")
                ]

    sage_version = meta.get("sage_version")
    sage_commit = meta.get("sage_git_commit") or meta.get("sage_commit")
    python_version = None
    if probe is not None:
        sage_version = probe.get("probe", {}).get("sage_version") or sage_version
        python_version = probe.get("probe", {}).get("python_version")

    return {
        "manifest": {
            "schema_version": 1,
            "sage_version": sage_version,
            "sage_git_commit": sage_commit,
            "extractor_version": EXTRACTOR_VERSION,
            "generated_at": observed_at,
            "python_version": python_version or sys.version.split()[0],
            "inventory_sha256": hashlib.sha256(raw).hexdigest(),
            "runtime_probe": str(probe_path.relative_to(DESIGN_ROOT)) if probe is not None else None,
            "runtime_edge_count": runtime_edge_count if probe is not None else 0,
            "runtime_only_categories": len(runtime_only),
            "scope": meta.get("scope"),
            "note": ("Empirical snapshot. Runtime parents from super_categories() when probe present; declared parents from defining_relation. Does not correct Sage defects."),
        },
        "categories": categories,
        "axioms": axioms,
        "constructions": constructions,
        "aliases": aliases,
    }


def write_observed(path: Path | None = None) -> Path:
    dest = path or OBSERVED_PATH
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = build_observed_from_inventory()
    dest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return dest


def main() -> int:
    path = write_observed()
    data = load_json(path)
    m = data["manifest"]
    n_imm = sum(len(c.get("immediate_supercategories") or []) for c in data["categories"])
    print(
        f"wrote {path} "
        f"(categories={len(data['categories'])} "
        f"immediate_edges={n_imm} "
        f"axioms={len(data['axioms'])} "
        f"constructions={len(data['constructions'])} "
        f"sage={m['sage_version']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
