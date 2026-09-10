#!/usr/bin/env python3
"""Check DAG.md for the ways a dependency graph can look complete and not be.

WHAT THIS SCRIPT CANNOT DO.  Every check here is bookkeeping: it reads the tables
and asks whether a cell or a row is *present*.  It never asks whether the row is
*true*.  Whether a terminality verdict is correct -- whether the declaration it
names exists in the pinned Mathlib, whether it says what the node says, whether a
corpus claim survives reading the corpus -- is a question about a large body of
Lean that this script does not read and could not check.  Those verdicts are
established by hand, and the tables record what was read so a later reader can
re-check them; four of them were false when this check was written and green.

So a green run means only this: no cell is empty, no edge points at nothing, and
no node or stratum is missing its row.  It is a guard against a table that has
gone stale or been extended without its verdicts, not a proof that the graph
bottoms out.

Five failure modes, all the same kind: a place where the graph presents a
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
   classification was written were never swept.  This finds the *missing* row; it
   says nothing about whether a present row is right.  The two superseded nodes in
   SUPERSEDED are exempt; a node replaced by other nodes has no supplier.

5. A greenfield stratum has no row in the construction floor.  Greenfield says
   no supplier exists, which is a claim about who has already done the work and
   not about whether the node can be written; without a floor row the stratum
   reads as blocked on missing foundations, which for every stratum here is
   false.  Strata A-D in PAPER_STRATA are exempt: their nodes are the paper's
   own results, and what they rest on is the other strata, which the dependency
   tables already give node by node.

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

# The construction-floor tables are headed "Node" in the first column and "What
# must be authored" in the last, which is what tells them from the dependency and
# route tables.
FLOOR_HEADER = "what must be authored"

# Strata that are the paper's own results rather than foundations, and so need no
# construction floor of their own.
PAPER_STRATA: frozenset[str] = frozenset({"A", "B", "C", "D"})


def stratum(node: str) -> str:
    """The stratum prefix of a node id: the letters before the first digit."""
    return node[: len(node) - len(node.lstrip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))] or "".join(
        ch for ch in node if ch.isalpha() and not ch.isdigit()
    )


def first_column(text: str, header: str, defined: set[str]) -> set[str]:
    """Every node named in the first column of each table with this last header."""
    out: set[str] = set()
    in_table = False
    for line in text.splitlines():
        if not line.startswith("| "):
            in_table = False
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 2:
            continue
        if not in_table:
            in_table = cells[-1].lower() == header
            continue
        if set(cells[0]) <= set("- :"):
            continue
        out |= expand_ranges(cells[0], defined)
    return out


def greenfield(text: str, defined: set[str]) -> set[str]:
    """Every node named in the first column of the greenfield table."""
    return first_column(text, "nearest thing that exists", defined)


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

    floored = {s for n in first_column(text, FLOOR_HEADER, defined) for s in [stratum(n)]}
    unfloored = sorted(
        {stratum(n) for n in greenfield(text, defined)} - floored - PAPER_STRATA
    )
    if unfloored:
        print(f"\n{len(unfloored)} greenfield stratum/strata with no construction-floor row:")
        for s in unfloored:
            print(f"  {s}")

    if not dangling and not undecomposed and not rootless and not unverdicted and not unfloored:
        print("\nevery node has a dependency naming a defined node or a substrate,")
        print("a row in a terminality table, and for every greenfield stratum a row in")
        print("the construction floor.  Whether those rows are TRUE is not checked here")
        print("and cannot be: it is a question about the pinned Mathlib and the corpora,")
        print("read by hand and recorded in the rows themselves.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "DAG.md")))
