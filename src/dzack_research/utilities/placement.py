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

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Final, TypedDict

GRAPH: Final = Path(__file__).resolve().parents[3] / "docs" / "preamble-graph.json"
KINDS: Final = ("objects", "elements", "morphisms")


class Operation(TypedDict):
    name: str
    signature: str
    summary: str
    mark: str


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


def incomparable_introductions(poset: Poset) -> dict[tuple[str, str], set[str]]:
    r"""Operation names introduced on two or more pairwise incomparable categories."""
    sites: dict[tuple[str, str], set[str]] = defaultdict(set)
    for name, record in poset.items():
        for kind in KINDS:
            for operation in introduced(record, kind):
                sites[(kind, operation["name"])].add(name)
    return {
        key: names
        for key, names in sites.items()
        if len(names) > 1
        and all(
            left == right or (right not in up_set(poset, left) and left not in up_set(poset, right))
            for left in names
            for right in names
        )
    }


def worksheet(poset: Poset, name: str) -> list[str]:
    record = poset[name]
    above = up_set(poset, name)
    lines = [f"## {record['display']}", "", f"`{record['source']}` -- {record['summary']}", ""]
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
            again = [d for d in above if any(o["name"] == operation["name"] for o in introduced(poset[d], kind))]
            line = f"- `{operation['name']}{operation['signature']}` {operation['summary']}"
            if again:
                line += " **Finding:** also introduced on " + ", ".join(f"`{d}`" for d in again)
            lines.append(line)
    lines += ["", "### Up-set U_C", ""]
    lines += [f"- `{d}` -- {poset[d]['summary']}" for d in above] or ["- empty"]
    return [*lines, ""]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("categories", nargs="*", help="categories to print; all owned ones by default")
    parser.add_argument("--graph", type=Path, default=GRAPH)
    arguments = parser.parse_args()
    poset: Poset = json.loads(arguments.graph.read_text())["categories"]
    names = arguments.categories or sorted(
        name for name, record in poset.items() if record["owned"] and any(introduced(record, k) for k in KINDS)
    )
    lines = ["# Placement worksheet", ""]
    for name in names:
        lines += worksheet(poset, name)
    lines += ["# Operation names introduced on incomparable categories", ""]
    for (kind, operation), sites in sorted(incomparable_introductions(poset).items()):
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
