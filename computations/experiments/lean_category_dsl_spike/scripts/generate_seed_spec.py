#!/usr/bin/env python3
"""Regenerate NormalizedCategoryGraph Spec from the Python semantic seed.

Source of truth: sage_category_tree_stubs/design/normalized_category_graph/semantic_seed/
Outputs:
  NormalizedCategoryGraph/Spec/seed_manifest.json
  NormalizedCategoryGraph/Presentation/dot_graph_id_sidecar.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SPIKE = Path(__file__).resolve().parents[1]
STUBS = SPIKE.parent / "sage_category_tree_stubs"
SEED = STUBS / "design/normalized_category_graph/semantic_seed"
LEAN = SPIKE / "NormalizedCategoryGraph"
HAND = STUBS / "design/normalized_category_graph/category_parent_graph.hand.dot"



def _leg_functor_id(leg: str | None, leg_by_classifier: dict[str, str]) -> str:
    """The FunctorId naming a pullback leg.

    A leg given as a classifier id is the classifier's forgetful leg; a leg with no
    known arrow is an error rather than a category reference, because silently
    emitting one produces an expression no evaluator can resolve.
    """
    if not leg:
        raise ValueError("pullback leg is missing")
    if leg.startswith("fun."):
        return leg
    if leg.startswith("clf."):
        arrow = leg_by_classifier.get(leg)
        if not arrow:
            raise ValueError(f"classifier leg {leg} has no classifier_leg arrow in the seed")
        return arrow
    raise ValueError(f"pullback leg {leg} is neither a functor nor a classifier")


def expr_of(e: dict, leg_by_classifier: dict[str, str] | None = None) -> dict:
    leg_by_classifier = leg_by_classifier or {}
    d = e.get("definition") or {}
    # Spelling aliases only. A construction value is an alias by `kind` but its
    # `of` names the construction's functor, so routing it here emitted a category
    # reference to a `fun.*` id; it falls through to the construction_value branch.
    if d.get("operation") == "same_as":
        target = d.get("same_as") or d.get("target")
        return {"tag": "reference", "id": target or e["id"]}
    if d.get("opaque"):
        return {"tag": "opaque", "id": e["id"]}
    op = d.get("operation")
    if op == "classifier_application":
        host = d.get("host") or d.get("base")
        return {
            "tag": "refine",
            "base": {"tag": "reference", "id": host},
            "classifier": d.get("classifier"),
            "route": None,
        }
    if op == "classifier_tower":
        base: dict = {"tag": "reference", "id": d.get("base") or d.get("host")}
        for clf in d.get("classifiers") or []:
            base = {"tag": "refine", "base": base, "classifier": clf, "route": None}
        return base
    if op == "pullback":
        # CategoryExpr.pullback takes two FunctorIds and a CategoryExpr. Emitting the
        # legs as category references made a typed importer look for categories named
        # `fun.*` and `clf.*`, which do not exist. A classifier leg is named by the
        # arrow that carries it, so resolve the classifier to that arrow.
        return {
            "tag": "pullback",
            "left": _leg_functor_id(d.get("left"), leg_by_classifier),
            "right": _leg_functor_id(d.get("right"), leg_by_classifier),
            "over": {"tag": "reference", "id": d.get("over")},
        }
    if op == "parameter_substitution":
        return {
            "tag": "familyApp",
            "family": d.get("of") or e["id"],
            "args": [str(d.get("substitute"))],
        }
    if op == "construction_value":
        return {"tag": "constructor", "constructor": "construction_value", "args": []}
    if e["kind"] == "classifier_domain":
        return {
            "tag": "classifierTotal",
            "classifier": d.get("classifier_id") or e["id"].replace(".domain", ""),
        }
    return {"tag": "atom", "id": e["id"]}


def origin_of(e: dict) -> str:
    d = e.get("definition") or {}
    if e["kind"] == "alias" or d.get("operation") == "same_as":
        return "alias"
    if d.get("opaque"):
        return "opaqueCategory"
    if e["kind"] == "category_family" and not d:
        return "root"
    if e["kind"] == "classifier_domain":
        return "atomicClassifierTotal"
    if e["kind"] == "category_constructor" or d.get("operation") == "construction_value":
        return "constructorValue"
    return "derivedNamed"


def visibility_of(e: dict) -> str:
    d = e.get("definition") or {}
    return "semanticOnly" if d.get("opaque") else "present"


def _split_graphviz_node_list(raw: str) -> list[str]:
    """Split an unquoted Graphviz multi-node declaration (`A; B`).

    Quoted names (`\"A; B\"`) are kept intact. Trailing empty pieces from a
    final semicolon are dropped.
    """
    raw = raw.strip()
    if not raw:
        return []
    if raw.startswith('"') and raw.endswith('"') and raw.count('"') == 2:
        return [raw.strip('"')]
    return [p.strip().strip('"') for p in raw.split(";") if p.strip()]


def collect_hand_nodes(text: str) -> set[str]:
    nodes: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if (
            not line
            or line.startswith("//")
            or line.startswith("graph")
            or line.startswith("digraph")
            or line.startswith("node")
            or line.startswith("edge")
            or line.startswith("{")
            or line.startswith("}")
            or line.startswith("subgraph")
            or line.startswith("rank")
            or line.startswith("label")
            or line.startswith("labelloc")
            or line.startswith("fontsize")
            or line.startswith("fontname")
            or line.startswith("nodesep")
            or line.startswith("ranksep")
            or line.startswith("splines")
            or line.startswith("color")
            or line.startswith("fillcolor")
            or line.startswith("style")
            or line.startswith("shape")
            or line.startswith("penwidth")
            or line.startswith("constraint")
        ):
            continue
        if "->" not in line and "[" in line:
            name = line.split("[", 1)[0].strip()
            for part in _split_graphviz_node_list(name):
                nodes.add(part)
        if "->" in line:
            left, right = line.split("->", 1)
            src = left.strip().split("[")[0].strip().strip('"')
            tgt = right.strip().split("[")[0].strip().rstrip(";").strip().strip('"')
            nodes.add(src)
            nodes.add(tgt)
    return nodes


def parse_hand_edges(text: str) -> list[tuple[str, str, str]]:
    """Return (src, tgt, kind) where kind is solid|dotted|other."""
    out: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if "->" not in line or line.startswith("//"):
            continue
        left, right = line.split("->", 1)
        src = left.strip().split("[")[0].strip().strip('"')
        rest = right.strip()
        tgt = rest.split("[")[0].strip().rstrip(";").strip().strip('"')
        kind = "solid"
        if "style=dotted" in rest or 'style="dotted"' in rest:
            kind = "dotted"
        elif "style=dashed" in rest or 'style="dashed"' in rest:
            kind = "dashed"
        out.append((src, tgt, kind))
    return out


def main() -> int:
    ents = json.loads((SEED / "entities.json").read_text())["entities"]
    clfs_raw = json.loads((SEED / "classifiers.json").read_text())
    clfs = clfs_raw["classifiers"] if isinstance(clfs_raw, dict) else clfs_raw
    arrows_raw = json.loads((SEED / "arrows.json").read_text())
    arrows = arrows_raw["arrows"] if isinstance(arrows_raw, dict) else arrows_raw
    # A classifier's forgetful leg is named by its classifier_leg arrow; pullback
    # expressions cite that FunctorId rather than the classifier id.
    leg_by_classifier = {
        str(a["source"]).removesuffix(".domain"): str(a["id"])
        for a in arrows
        if a.get("kind") == "classifier_leg"
    }

    sidecar: dict[str, str] = {}
    # Prefer canonical (non-alias) entities when several share a DOT vertex.
    ranked = sorted(
        ents,
        key=lambda e: (
            0
            if e["kind"] != "alias" and (e.get("definition") or {}).get("operation") != "same_as"
            else 1,
            e["id"],
        ),
    )
    for e in ranked:
        v = e.get("dot_vertex")
        if not v:
            continue
        d = e.get("definition") or {}
        target = e["id"]
        if d.get("operation") == "same_as":
            target = d.get("same_as") or d.get("of") or d.get("target") or e["id"]
        if v not in sidecar:
            sidecar[v] = target
        if v.strip('"') not in sidecar:
            sidecar[v.strip('"')] = target
        if "=" in v:
            short = v.split("=", 1)[0].strip().strip('"')
            sidecar.setdefault(short, target)

    hand_text = HAND.read_text(encoding="utf-8")
    hand_nodes = collect_hand_nodes(hand_text)
    missing_hand = sorted(
        n for n in hand_nodes if n not in sidecar and not n.startswith("ax.")
    )
    sidecar_out = {
        "schemaVersion": "0.1.0",
        "description": "Hand DOT vertex label → stable graph id",
        "map": {k: sidecar[k] for k in sorted(sidecar)},
        "hand_vertices_without_seed": missing_hand,
        "hand_vertices_without_seed_count": len(missing_hand),
        "hand_edges": [
            {"src": s, "tgt": t, "kind": k} for s, t, k in parse_hand_edges(hand_text)
        ],
    }
    (LEAN / "Presentation/dot_graph_id_sidecar.json").write_text(
        json.dumps(sidecar_out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    categories = []
    aliases = []
    opaques = []
    for e in sorted(ents, key=lambda x: x["id"]):
        d = e.get("definition") or {}
        # Spelling aliases only (same_as). construction_value keeps a named node.
        if e["kind"] == "alias" and d.get("operation") == "same_as":
            aliases.append(
                {
                    "id": f"alias.{e['id'].removeprefix('cat.').removeprefix('alias.')}",
                    "spelling": e.get("canonical_name") or e["id"],
                    "aliasOf": d.get("same_as") or d.get("of") or d.get("target") or e["id"],
                    "declaration": e["id"],
                }
            )
            continue
        categories.append(
            {
                "id": e["id"],
                "canonicalName": e.get("canonical_name") or e["id"],
                "declaration": e["id"],
                "expression": expr_of(e, leg_by_classifier),
                "origin": origin_of(e),
                "visibility": visibility_of(e),
                "kind": e["kind"],
                "dotVertex": e.get("dot_vertex"),
            }
        )
        if d.get("opaque"):
            ports = []
            for a in arrows:
                if a.get("source") == e["id"] and a.get("preferred", True) and a.get(
                    "kind"
                ) in {
                    "forgetful",
                    "full_inclusion",
                    "pullback_projection",
                    "theorem_inclusion",
                }:
                    ports.append(
                        {
                            "id": f"oport.{e['id']}.{a['target']}",
                            "source": e["id"],
                            "target": a["target"],
                            "role": a.get("role") or "structural",
                            "declaration": a.get("id", ""),
                            "provenance": a.get("kind", ""),
                        }
                    )
            opaques.append(
                {
                    "id": e["id"],
                    "declaration": e["id"],
                    "ports": ports,
                    "reason": d.get("notes") or "opaque host",
                    "visibility": "semanticOnly",
                }
            )

    classifiers = [
        {
            "id": c["id"],
            "canonicalName": c.get("name") or c["id"],
            "declaration": c["id"],
            "hostId": c.get("host_id") or c.get("host"),
            "visibility": "present",
            "domainId": c.get("domain_id"),
            "legArrowId": c.get("leg_arrow_id"),
        }
        for c in sorted(clfs, key=lambda x: x["id"])
    ]

    # Alias rows are keyed `alias.*`; arrows cite the underlying `cat.*` declaration.
    alias_only_ids = {a["declaration"] for a in aliases}
    structural = []
    for a in sorted(arrows, key=lambda x: x["id"]):
        if not a.get("preferred", True):
            continue
        if a.get("kind") not in {
            "forgetful",
            "full_inclusion",
            "pullback_projection",
            "theorem_inclusion",
            "classifier_leg",
            # Hand DOT draws many construction/param edges as solid parents.
            "construction",
            "parameter_dependency",
            "equivalence",
        }:
            continue
        # Alias-only entities are recorded in `aliases`, not `categories`, so a
        # structural port touching one has an endpoint absent from the manifest.
        # Exporting it anyway gives consumers dangling structural maps.
        if a["source"] in alias_only_ids or a["target"] in alias_only_ids:
            continue
        structural.append(
            {
                "id": a["id"],
                "source": a["source"],
                "target": a["target"],
                "kind": a["kind"],
                "role": a.get("role"),
            }
        )

    manifest = {
        "schemaVersion": "0.2.0-seed",
        "universes": {},
        "categories": categories,
        "classifiers": classifiers,
        "aliases": aliases,
        "opaqueCategories": opaques,
        "structuralPorts": structural,
        "theoremInclusions": [],
        "coherences": [],
        "presentationDispositions": [],
        "categoryFamilies": [],
        "namedExpressions": [],
        "seed": {"entities": ents, "classifiers": clfs, "arrows": arrows},
    }
    (LEAN / "Spec/seed_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(
        f"wrote Spec/seed_manifest.json ({len(categories)} cats, {len(classifiers)} clfs); "
        f"sidecar map={len(sidecar)}; hand unmapped={len(missing_hand)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
