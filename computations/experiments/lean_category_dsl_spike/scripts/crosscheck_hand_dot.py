#!/usr/bin/env python3
"""Stage 7: typed crosscheck of hand DOT against Lean seed manifest.

Compares stable IDs (via sidecar), not DOT layout text.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

SPIKE = Path(__file__).resolve().parents[1]
LEAN = SPIKE / "NormalizedCategoryGraph"
MANIFEST = LEAN / "Spec/seed_manifest.json"
SIDECAR = LEAN / "Presentation/dot_graph_id_sidecar.json"


def canonicalize_alias(aliases: dict[str, str], cid: str) -> str:
    seen: set[str] = set()
    while cid in aliases and cid not in seen:
        seen.add(cid)
        cid = aliases[cid]
    return cid


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sidecar = json.loads(SIDECAR.read_text(encoding="utf-8"))
    id_map: dict[str, str] = sidecar["map"]
    edges = sidecar.get("hand_edges") or []

    by_id = {c["id"]: c for c in manifest["categories"]}
    alias_of: dict[str, str] = {}
    for a in manifest["aliases"]:
        alias_of[a["id"]] = a["aliasOf"]
        alias_of[a["spelling"]] = a["aliasOf"]
        # authored spelling ids like cat.commutativerings
        if a["declaration"]:
            alias_of[a["declaration"]] = a["aliasOf"]

    adj: dict[str, set[str]] = defaultdict(set)
    for p in manifest["structuralPorts"]:
        adj[p["source"]].add(p["target"])
    for o in manifest["opaqueCategories"]:
        for p in o.get("ports") or []:
            adj[p["source"]].add(p["target"])

    def reachable(src: str, tgt: str) -> bool:
        src = canonicalize_alias(alias_of, src)
        tgt = canonicalize_alias(alias_of, tgt)
        if src == tgt:
            return True
        seen = {src}
        stack = [src]
        while stack:
            u = stack.pop()
            for v in adj.get(u, ()):
                v = canonicalize_alias(alias_of, v)
                if v == tgt:
                    return True
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return False

    findings: list[str] = []

    for a in manifest["aliases"]:
        tgt = canonicalize_alias(alias_of, a["aliasOf"])
        if tgt not in by_id:
            findings.append(f"alias_dangling:{a['id']}->{a['aliasOf']}")
        if a["spelling"] in {c["canonicalName"] for c in manifest["categories"]}:
            findings.append(f"alias_creates_node_name:{a['spelling']}")

    for e in edges:
        if e["kind"] != "solid":
            continue
        sid = id_map.get(e["src"])
        tid = id_map.get(e["tgt"])
        if not sid or not tid:
            continue
        cs, ct = canonicalize_alias(alias_of, sid), canonicalize_alias(alias_of, tid)
        if cs == ct:
            # Alias spelling drawn as a solid parent of its canonical target
            # (e.g. LeftModules(R) → Modules(R)); both map to one seed id.
            continue

    hand_vertices = {e["src"] for e in edges} | {e["tgt"] for e in edges}
    for v in sorted(hand_vertices):
        if v.startswith("ax."):
            continue
        gid = id_map.get(v)
        if not gid:
            continue
        gid = canonicalize_alias(alias_of, gid)
        if gid not in by_id:
            findings.append(f"hand_id_missing_in_lean:{v}->{gid}")

    # Presentation-visible Lean nodes with a DOT vertex must appear in hand
    hand_ids = {
        canonicalize_alias(alias_of, id_map[v]) for v in hand_vertices if v in id_map
    }
    for c in manifest["categories"]:
        if c.get("visibility") != "present":
            continue
        if c.get("kind") in {"classifier_domain", "category_constructor", "alias"}:
            continue
        if c.get("origin") == "constructorValue":
            continue
        dv = c.get("dotVertex")
        if not dv:
            continue
        cid = canonicalize_alias(alias_of, c["id"])
        if cid not in hand_ids and dv not in hand_vertices and dv.split("=", 1)[0].strip() not in hand_vertices:
            findings.append(f"lean_present_absent_from_hand:{c['id']}")

    # Solid parent edges: require structural reachability when both ends are
    # ordinary categories (not constructors / construction values).
    for e in edges:
        if e["kind"] != "solid":
            continue
        sid, tid = id_map.get(e["src"]), id_map.get(e["tgt"])
        if not sid or not tid:
            findings.append(f"solid_edge_unmapped:{e['src']}->{e['tgt']}")
            continue
        sid, tid = canonicalize_alias(alias_of, sid), canonicalize_alias(alias_of, tid)
        src_e, tgt_e = by_id.get(sid), by_id.get(tid)
        if not src_e or not tgt_e:
            findings.append(f"solid_edge_endpoint_missing:{e['src']}->{e['tgt']}")
            continue
        if src_e.get("kind") == "category_constructor" or tgt_e.get("kind") == "category_constructor":
            continue
        if src_e.get("origin") == "constructorValue" or tgt_e.get("origin") == "constructorValue":
            # Construction-value parents are realized iff a construction/forgetful port exists.
            if reachable(sid, tid):
                continue
            findings.append(f"solid_edge_unrealized:{e['src']}->{e['tgt']} ({sid}->{tid})")
            continue
        if not reachable(sid, tid):
            # Classifier-domain Hasse edges with no seed arrow are presentation-only.
            if src_e.get("kind") == "classifier_domain" or tgt_e.get("kind") == "classifier_domain":
                findings.append(
                    f"presentation_only_classifier_edge:{e['src']}->{e['tgt']} ({sid}->{tid})"
                )
            else:
                findings.append(f"solid_edge_unrealized:{e['src']}->{e['tgt']} ({sid}->{tid})")

    print(f"crosscheck findings: {len(findings)}")
    for f in findings[:60]:
        print(f"  {f}")
    if len(findings) > 60:
        print(f"  ... +{len(findings) - 60} more")

    hard = [
        f
        for f in findings
        if f.startswith("alias_creates_node_name:")
        or f.startswith("hand_id_missing_in_lean:")
        or f.startswith("alias_dangling:")
        or f.startswith("solid_edge_unrealized:")
        or f.startswith("solid_edge_unmapped:")
        or f.startswith("solid_edge_endpoint_missing:")
        or f.startswith("presentation_only_classifier_edge:")
        or f.startswith("lean_present_absent_from_hand:")
    ]
    soft = [f for f in findings if f not in hard]
    print(f"hard={len(hard)} soft={len(soft)}")
    if findings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
