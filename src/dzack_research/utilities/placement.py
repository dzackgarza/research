r"""The placement worksheet: each introduced operation against its up-set.

``CAT-05`` states placement as a poset problem.  ``P`` is the declared category
poset, ``U_C = {D in P | D > C}`` the up-set of ``C``, and for an operation
``f`` introduced on ``C`` the set ``W_f = {D in U_C | f is well-defined on D}``
is closed downward in ``U_C``.  The home of ``f`` is ``max W_f``, or ``C``
when ``W_f`` is empty.  Deciding which ``D`` belong to ``W_f`` is mathematics;
everything else is read here from the live survey that ``just preamble-megadoc``
writes to ``docs/preamble-graph.json``.

For each category the worksheet prints its introduced object, element and
arrow operations, then every ``D`` in ``U_C`` with its definition, so the
reader decides ``W_f`` from the definitions on one screen.  Three facts need
no judgement and are printed as findings:

* an operation name introduced on ``C`` and again on some ``D`` in ``U_C``;
* the lowest categories of ``U_C`` whose arrow type the arrow type of ``C``
  does not inherit, although every arrow of ``C`` is an arrow there, and a Mor
  class that declares no arrow type at all;
* an operation name introduced on several pairwise incomparable categories,
  with the minimal common upper bounds of those categories in ``P``.  When
  ``f`` means the same thing on each, its home is at or below one of those
  bounds, and a missing bound is a missing category.

Run ``python -m dzack_research.utilities.placement [CATEGORY ...]``, or
``just placement``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fnmatch import fnmatchcase
from itertools import combinations
from pathlib import Path
from typing import Final, NotRequired, TypedDict

from dzack_research.utilities.source_inventory import source_fingerprint

GRAPH: Final = Path(__file__).resolve().parents[3] / "docs" / "preamble-graph.json"
KINDS: Final = ("objects", "elements", "morphisms")


class Operation(TypedDict):
    name: str
    signature: str
    summary: str
    mark: str
    source: NotRequired[str]


class CategoryRecord(TypedDict):
    display: str
    source: str
    summary: str
    owned: bool
    supers: list[str]
    ancestry: list[str]
    operations: dict[str, list[Operation]]
    arrow_mor_class: str
    arrow_type: str
    arrow_type_source: str
    arrow_unthreaded: list[str]
    problem: NotRequired[str]
    probed_as: NotRequired[str]


type Poset = dict[str, CategoryRecord]


def up_set(poset: Poset, name: str) -> list[str]:
    r"""``U_C``, in the survey's linearization order, restricted to ``P``."""
    return [above for above in poset[name]["ancestry"] if above in poset]


def introduced(record: CategoryRecord, kind: str) -> list[Operation]:
    return record["operations"][kind]


def minimal_common_upper_bounds(poset: Poset, names: set[str]) -> list[str]:
    r"""The minimal elements of the intersection of the up-sets of ``names``."""
    common = set.intersection(*(set(up_set(poset, name)) | {name} for name in names))
    return sorted(
        bound
        for bound in common
        if not any(bound in up_set(poset, other) for other in common if other != bound)
    )


def incomparable_introductions(poset: Poset) -> list[tuple[str, str, set[str]]]:
    r"""All incomparable pairs, including pairs within a mixed comparable family."""
    sites: dict[tuple[str, str], set[str]] = defaultdict(set)
    for name, record in poset.items():
        for kind in KINDS:
            for operation in introduced(record, kind):
                sites[(kind, operation["name"])].add(name)
    return [
        (*key, {left, right})
        for key, names in sites.items()
        for left, right in combinations(sorted(names), 2)
        if right not in up_set(poset, left) and left not in up_set(poset, right)
    ]


def worksheet(poset: Poset, name: str, methods: list[str]) -> list[str]:
    record = poset[name]
    above = up_set(poset, name)
    lines = [f"## {record['display']}", "", f"`{record['source']}` -- {record['summary']}", ""]
    if record.get("probed_as"):
        lines.append(f"Sampled as: {record['probed_as']}")
    if record.get("problem"):
        lines.append(f"Survey problem: {record['problem']}")
    if record["arrow_type"]:
        lines.append(f"Arrow type: `{record['arrow_type']}` {record['arrow_type_source']}")
    elif record["arrow_mor_class"]:
        lines.append(
            f"**Finding:** `{record['arrow_mor_class']}` declares no arrow type; its element "
            "constructor builds arrows of whatever class its code names, so their operations "
            "cannot be read from the graph"
        )
    if record["arrow_unthreaded"]:
        lines.append(
            "**Finding:** the arrow type does not inherit the arrow type of "
            + ", ".join(f"`{d}`" for d in record["arrow_unthreaded"])
        )
    for kind in KINDS:
        operations = introduced(record, kind)
        if not operations:
            continue
        lines += ["", f"### Introduced on {kind}", ""]
        for operation in operations:
            if methods and not any(fnmatchcase(operation["name"], pattern) for pattern in methods):
                continue
            again = [d for d in above if any(o["name"] == operation["name"] for o in introduced(poset[d], kind))]
            line = f"- `{operation['name']}{operation['signature']}` {operation['summary']}"
            if operation.get("source"):
                line += f" ({operation['source']})"
            if again:
                line += " **Finding:** also introduced on " + ", ".join(f"`{d}`" for d in again)
            lines.append(line)
    lines += ["", "### Up-set U_C", ""]
    lines += [f"- `{d}` -- {poset[d]['summary']}" for d in above] or ["- empty"]
    return [*lines, ""]


def selected_categories(poset: Poset, patterns: list[str], direction: str, between: list[str]) -> list[str]:
    unmatched = [p for p in patterns if not any(fnmatchcase(name, p) for name in poset)]
    assert not unmatched, f"No snapshot category matches {unmatched!r}"
    seeds = {name for name in poset if any(fnmatchcase(name, p) for p in patterns)}
    assert not patterns or seeds, f"No snapshot category matches {patterns!r}"
    names = seeds.copy() if patterns else {name for name, record in poset.items() if record["owned"]}
    if direction in {"up", "both"}:
        names.update(above for name in seeds for above in up_set(poset, name))
    if direction in {"down", "both"}:
        names.update(name for name in poset if set(up_set(poset, name)) & seeds)
    if between:
        lower, upper = between
        assert lower in poset and upper in poset, f"Unknown interval endpoints: {between!r}"
        assert lower == upper or upper in up_set(poset, lower), f"Unordered interval: {between!r}"
        names &= (set(up_set(poset, lower)) | {lower}) & {n for n in poset if n == upper or upper in up_set(poset, n)}
    return sorted(names)


def snapshot_relations(poset: Poset) -> set[tuple[str, ...]]:
    """Relations whose changes remain reviewable independently of rendering."""
    relations = {(name, "category") for name in poset}
    for name, record in poset.items():
        relations.update((name, "super", parent) for parent in record["supers"])
        for kind in KINDS:
            relations.update((name, kind, op["name"], op["signature"]) for op in introduced(record, kind))
        relations.add((name, "arrow", record["arrow_type"]))
        relations.update((name, "unthreaded", parent) for parent in record["arrow_unthreaded"])
    return relations


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("categories", nargs="*", help="categories to print; all owned ones by default")
    parser.add_argument("--graph", type=Path, default=GRAPH)
    parser.add_argument("--direction", choices=("self", "up", "down", "both"), default="self")
    parser.add_argument("--between", nargs=2, default=[], metavar=("LOWER", "UPPER"))
    parser.add_argument("--method", action="append", default=[], help="operation glob; repeatable")
    parser.add_argument("--format", choices=("markdown", "json", "dot"), default="markdown")
    parser.add_argument("--compare", type=Path, help="earlier graph snapshot; report added and removed relations")
    parser.add_argument("--source-root", type=Path, default=GRAPH.parents[1] / "src/dzack_research/preamble")
    arguments = parser.parse_args()
    if arguments.compare and (arguments.categories or arguments.method or arguments.between or arguments.direction != "self" or arguments.format != "markdown"):
        parser.error("--compare compares whole snapshots and emits JSON; omit slice and format options")
    content = arguments.graph.read_bytes()
    snapshot = json.loads(content)
    poset: Poset = snapshot["categories"]
    names = selected_categories(poset, arguments.categories, arguments.direction, arguments.between)
    metadata = snapshot.get("source", {})
    freshness = "unrecorded: this snapshot has no source fingerprint"
    if "fingerprint" in metadata:
        assert arguments.source_root.is_dir(), f"Source tree not found: {arguments.source_root}"
        freshness = "matches source" if metadata["fingerprint"] == source_fingerprint(arguments.source_root) else "stale: source differs from snapshot"
    evidence = {
        "snapshot": str(arguments.graph), "snapshot_sha256": hashlib.sha256(content).hexdigest(),
        "freshness": freshness, "source": metadata,
        "boundary": "Sampled runtime categories, not all parameter regimes. Candidate owners require mathematical review.",
    }
    if arguments.compare:
        before: Poset = json.loads(arguments.compare.read_text())["categories"]
        old, new = snapshot_relations(before), snapshot_relations(poset)
        print(json.dumps({**evidence, "previous": str(arguments.compare), "added": sorted(new - old), "removed": sorted(old - new)}, indent=2))
        return
    if arguments.format == "json":
        selected = {
            name: {**poset[name], "operations": {
                kind: [op for op in introduced(poset[name], kind) if not arguments.method or any(fnmatchcase(op["name"], p) for p in arguments.method)]
                for kind in KINDS
            }} for name in names
        }
        print(json.dumps({**evidence, "categories": selected}, indent=2))
        return
    if arguments.format == "dot":
        lines = ["// " + json.dumps(evidence), "digraph category_slice {", "  rankdir=BT;"]
        lines.extend(f"  {json.dumps(name)};" for name in names)
        lines.extend(f"  {json.dumps(name)} -> {json.dumps(parent)};" for name in names for parent in poset[name]["supers"] if parent in names)
        print("\n".join([*lines, "}"]))
        return
    lines = ["# Placement worksheet", "", f"Snapshot: {arguments.graph}; {freshness}", evidence["boundary"], ""]
    for name in names:
        lines += worksheet(poset, name, arguments.method)
    lines += ["# Operation names introduced on incomparable categories", ""]
    for kind, operation, sites in incomparable_introductions(poset):
        if arguments.method and not any(fnmatchcase(operation, p) for p in arguments.method):
            continue
        if not sites.isdisjoint(names):
            bounds = minimal_common_upper_bounds(poset, sites) or ["none in P"]
            lines.append(
                f"- {kind} `{operation}` on "
                + ", ".join(f"`{s}`" for s in sorted(sites))
                + " -- minimal common upper bounds: "
                + ", ".join(f"`{b}`" for b in bounds)
            )
    print("\n".join(lines))


if __name__ == "__main__":
    main()
