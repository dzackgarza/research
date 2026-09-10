#!/usr/bin/env python3
"""Check DAG.md for the ways a dependency graph can look complete and not be.

Four failure modes, all the same kind: a place where the graph presents a
finished edge or a finished node and there is nothing behind it.

1. A dependency cell names a node id that no row defines.  The edge is then
   fabricated: it points at nothing, and nobody reading the graph can tell.
2. A dependency cell names neither a node nor a substrate.  The graph then
   understates the work by an unknown amount, which is the defect the stratum
   decompositions exist to remove.
3. A dependency cell is empty, presenting the node as a root of the graph.  A
   real root rests on nothing at all, which is rare; an empty cell is usually a
   node whose dependencies were never worked out, and it reads as the opposite.
   Roots are declared in ROOTS below, and anything else empty is a finding.

4. A node carries no terminality verdict.  "Terminal" in this file is a claim
   about a node's supplier -- available in the pinned Mathlib, or in a corpus the
   registry knows -- and "greenfield" is the claim that no supplier exists.  A
   node in neither classification has no answer to the question the file exists
   to answer, and nothing else here notices: 24 nodes lost their verdict this way
   while the first three checks stayed green, because strata added after the
   classification was written were never swept.  The two superseded nodes in
   SUPERSEDED are exempt; a node replaced by other nodes has no supplier.

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

# `F5.3-F5.7`, `A0-A7`, `Ni1-Ni10`: one stratum prefix, an en dash or hyphen, and
# a second endpoint that may repeat the prefix.
NODE_RANGE = re.compile(
    r"\b([A-Z][A-Za-z]{0,2})(\d+(?:\.\d+)?)[\u2013-]+(?:[A-Z][A-Za-z]{0,2})?(\d+(?:\.\d+)?)\b"
)

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


# The last column of a dependency table is headed by one of these.  Tables headed
# otherwise -- the construction floor, the route tables, the terminality tables,
# the S-row index -- also have node ids in their first column and must not be
# read as dependencies.  Keying on the header rather than on the row shape is
# also what keeps S1-S7 out of the node count: DAG.md says they are subjects and
# not nodes, and their table is headed "Mathlib substrate".
DEPENDENCY_HEADERS = {"depends on", "next dependency"}

# The three terminality-verdict tables are the only ones headed "Nodes" (plural)
# in the first column: the two terminal tables and the greenfield table.  Every
# other table here -- routes, the ATLAS sweep, the construction floor, the
# dependency tables -- is headed "Node" or "Stratum".  Only the first column is
# read: the later columns name substrate and near misses, and reading those would
# count a node as verdicted because some other row's explanation mentions it.
VERDICT_HEADER = "nodes"

# Nodes whose content was decomposed into other nodes.  A superseded node has no
# supplier to name, so it carries no verdict; its dependency cell points at the
# nodes that replaced it, and check 1 keeps that edge honest.
SUPERSEDED: frozenset[str] = frozenset({"C1", "Nk2"})


def verdicted(text: str, defined: set[str]) -> set[str]:
    """Every node named in the first column of a terminality-verdict table."""
    out: set[str] = set()
    in_verdict_table = False
    for line in text.splitlines():
        if not line.startswith("| "):
            in_verdict_table = False
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 2:
            continue
        if not in_verdict_table:
            in_verdict_table = cells[0].lower() == VERDICT_HEADER
            continue
        if set(cells[0]) <= set("- :"):
            continue
        out |= expand_ranges(cells[0], defined)
    return out


def expand_ranges(cell: str, defined: set[str]) -> set[str]:
    """The nodes a subject cell names, with `F5.3-F5.7` and `A0-A7` expanded."""
    got = set(NODE_ID.findall(cell))
    for m in NODE_RANGE.finditer(cell):
        prefix, lo, hi = m.group(1), m.group(2), m.group(3)
        if "." in lo and "." in hi:
            stem, a = lo.split(".")
            stem_hi, b = hi.split(".")
            if stem != stem_hi:
                continue
            got |= {f"{prefix}{stem}.{k}" for k in range(int(a), int(b) + 1)}
        elif "." not in lo and "." not in hi:
            got |= {f"{prefix}{k}" for k in range(int(lo), int(hi) + 1)}
    return got & defined


def rows(text: str) -> list[tuple[int, str, str]]:
    """Every dependency-table row keyed by a node id, as (line, id, dependency)."""
    out = []
    in_dependency_table = False
    for i, line in enumerate(text.splitlines(), 1):
        if not line.startswith("| "):
            in_dependency_table = False
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 2:
            continue
        if not in_dependency_table:
            # A header row declares what the table is; only dependency tables count.
            in_dependency_table = cells[-1].lower() in DEPENDENCY_HEADERS
            continue
        if set(cells[-1]) <= set("- :"):
            continue  # the |---|---| separator
        head = cells[0]
        if not NODE_ID.fullmatch(head):
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

    unverdicted = sorted(defined - verdicted(text, defined) - SUPERSEDED)
    if unverdicted:
        print(f"\n{len(unverdicted)} node(s) in no terminality-verdict table:")
        for node in unverdicted:
            print(f"  {node}")

    if not dangling and not undecomposed and not rootless and not unverdicted:
        print("\nevery node has a dependency naming a defined node or a substrate,")
        print("and a terminality verdict saying who supplies it")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "DAG.md")))
