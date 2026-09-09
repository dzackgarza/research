#!/usr/bin/env python3
"""Check DAG.md for the ways a dependency graph can look complete and not be.

Three failure modes, all the same kind: a place where the graph presents a
finished edge and there is none behind it.

1. A dependency cell names a node id that no row defines.  The edge is then
   fabricated: it points at nothing, and nobody reading the graph can tell.
2. A dependency cell names neither a node nor a substrate.  The graph then
   understates the work by an unknown amount, which is the defect the stratum
   decompositions exist to remove.
3. A dependency cell is empty, presenting the node as a root of the graph.  A
   real root rests on nothing at all, which is rare; an empty cell is usually a
   node whose dependencies were never worked out, and it reads as the opposite.
   Roots are declared in ROOTS below, and anything else empty is a finding.

A cell counts as naming a substrate when it says where the thing lives or that
it is absent -- Mathlib, a registry corpus, or an explicit absence.

Run: python3 check_dag.py [DAG.md]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# A node id: a stratum prefix of letters, then digits, optionally dotted (F1.10)
# or suffixed (A1a, V11b, F5.7).
NODE_ID = re.compile(r"\b([A-Z][A-Za-z]{0,2}\d+(?:\.\d+)?[a-z]?)\b")

# Phrases that make a dependency cell a substrate verdict rather than a subject.
SUBSTRATE_MARKERS = (
    "mathlib", "absent", "nothing", "lean-categories", "corpus",
    "sphere-packing", "gq2-lean", "hasseprinciple", "registry",
    "`", "see there", "see below",
)


# Nodes that genuinely rest on nothing in this graph: pure definitions over the
# ambient conventions, with no earlier node and no Mathlib dependency worth
# naming.  Every other empty dependency cell is a finding.
ROOTS: frozenset[str] = frozenset()


def rows(text: str) -> list[tuple[int, str, str]]:
    """Every table row whose first cell is a node id, as (line, id, last cell)."""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 3:
            continue
        head = cells[0]
        m = NODE_ID.fullmatch(head)
        if not m:
            continue
        out.append((i, head, cells[-1]))
    return out


def main(path: Path) -> int:
    text = path.read_text()
    table = rows(text)
    defined = {node for _, node, _ in table}
    if not defined:
        print("no node rows found -- the row pattern no longer matches", file=sys.stderr)
        return 2

    dangling: list[tuple[int, str, str]] = []
    undecomposed: list[tuple[int, str, str]] = []

    rootless: list[tuple[int, str]] = []

    for line, node, dep in table:
        if not dep or dep in {"—", "-", ""}:
            if node not in ROOTS:
                rootless.append((line, node))
            continue
        referenced = set(NODE_ID.findall(dep))
        unknown = {r for r in referenced if r not in defined}
        for u in sorted(unknown):
            dangling.append((line, node, u))
        if not (referenced - unknown):
            if not any(m in dep.lower() for m in SUBSTRATE_MARKERS):
                undecomposed.append((line, node, dep))

    print(f"{len(defined)} nodes defined, {len(table)} rows read")

    if dangling:
        print(f"\n{len(dangling)} dangling reference(s) -- an edge pointing at no node:")
        for line, node, target in dangling:
            print(f"  DAG.md:{line}  {node} -> {target}")
    if undecomposed:
        print(f"\n{len(undecomposed)} dependency cell(s) naming neither a node nor a substrate:")
        for line, node, dep in undecomposed:
            print(f"  DAG.md:{line}  {node} -> {dep}")
    if rootless:
        print(f"\n{len(rootless)} node(s) with an empty dependency cell, presented as roots:")
        for line, node in rootless:
            print(f"  DAG.md:{line}  {node}")

    if not dangling and not undecomposed and not rootless:
        print("\nevery node has a dependency, naming a defined node or a substrate verdict")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "DAG.md")))
