#!/usr/bin/env python3
"""Validate project category graphs through Sage category identities."""

from __future__ import annotations

import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@dataclass(frozen=True)
class GraphCheck:
    label: str
    category: Any


@dataclass(frozen=True)
class GraphFailure:
    label: str
    category_repr: str
    check: str
    error_type: str
    message: str
    traceback_text: str


def project_category_checks() -> tuple[GraphCheck, ...]:
    from category_specs.algebras import Algebras
    from category_specs.cat import Cat
    from category_specs.forms import FormedModules
    from category_specs.lattices import Lattices
    from category_specs.modules import Modules
    from category_specs.posets import Posets
    from category_specs.rings import Rings
    from category_specs.sets import Sets
    from category_specs.topological_spaces import TopologicalSpaces
    from sage.all import GF, QQ, ZZ, IntegerModRing, PolynomialRing

    polynomial_ring = PolynomialRing(ZZ, name="x")

    return (
        GraphCheck("Cat()", Cat()),
        GraphCheck("Sets()", Sets()),
        GraphCheck("Posets()", Posets()),
        GraphCheck("TopologicalSpaces()", TopologicalSpaces()),
        GraphCheck("Rings()", Rings()),
        GraphCheck("Modules(ZZ)", Modules(ZZ)),
        GraphCheck("Modules(QQ)", Modules(QQ)),
        GraphCheck("Modules(IntegerModRing(6))", Modules(IntegerModRing(6))),
        GraphCheck("Modules(ZZ['x'])", Modules(polynomial_ring)),
        GraphCheck("Modules(GF(5))", Modules(GF(5))),
        GraphCheck("Algebras(QQ)", Algebras(QQ)),
        GraphCheck("FormedModules(ZZ)", FormedModules(ZZ)),
        GraphCheck("Lattices(ZZ)", Lattices(ZZ)),
    )


def _format_exception(exc: BaseException) -> tuple[str, str, str]:
    return (
        type(exc).__name__,
        str(exc),
        "".join(traceback.format_exception(type(exc), exc, exc.__traceback__)),
    )


def _category_origin(category: Any) -> str:
    r"""Return the source namespace for a category graph vertex."""
    saw_sage = False
    for cls in type(category).mro():
        module = cls.__module__
        if module.startswith("category_specs."):
            return "Spec"
        if module.startswith("sage."):
            saw_sage = True
    if saw_sage:
        return "Sage"
    return type(category).__module__


def _base_category_label(category: Any) -> str:
    r"""Return a human-readable identity-preserving graph label."""
    return f"{_category_origin(category)} {category._repr_object_names()}"


def _category_graph_nodes(category: Any) -> tuple[Any, ...]:
    r"""Return all category objects needed for the identity graph."""
    nodes: list[Any] = []
    seen: set[int] = set()

    def add_node(node: Any) -> None:
        node_id = id(node)
        if node_id not in seen:
            seen.add(node_id)
            nodes.append(node)

    for node in category._all_super_categories:
        add_node(node)
        for target in node._super_categories:
            add_node(target)
    return tuple(nodes)


def _category_graph_edges(nodes: tuple[Any, ...]) -> tuple[tuple[Any, Any], ...]:
    r"""Return immediate supercategory edges between category objects."""
    node_ids = {id(node) for node in nodes}
    edges: list[tuple[Any, Any]] = []
    for source in nodes:
        for target in source._super_categories:
            if id(target) in node_ids:
                edges.append((source, target))
    return tuple(edges)


def _category_graph_labels(nodes: tuple[Any, ...]) -> dict[int, str]:
    r"""Return labels that distinguish project and Sage categories."""
    base_labels = {id(node): _base_category_label(node) for node in nodes}
    counts: dict[str, int] = {}
    for label in base_labels.values():
        counts[label] = counts.get(label, 0) + 1

    labels: dict[int, str] = {}
    for node in nodes:
        label = base_labels[id(node)]
        if counts[label] > 1:
            cls = type(node)
            label = f"{label} [{cls.__module__}.{cls.__qualname__}]"
        labels[id(node)] = label
    return labels


def _identity_graph_is_directed_acyclic(
    nodes: tuple[Any, ...], edges: tuple[tuple[Any, Any], ...]
) -> bool:
    r"""Return whether the immediate-supercategory graph is acyclic."""
    adjacency: dict[int, list[int]] = {id(node): [] for node in nodes}
    for source, target in edges:
        adjacency[id(source)].append(id(target))

    active: set[int] = set()
    finished: set[int] = set()

    def visit(node_id: int) -> bool:
        if node_id in active:
            return False
        if node_id in finished:
            return True
        active.add(node_id)
        for target_id in adjacency[node_id]:
            if not visit(target_id):
                return False
        active.remove(node_id)
        finished.add(node_id)
        return True

    return all(visit(id(node)) for node in nodes)


def _print_identity_category_graph(label: str, category: Any) -> bool:
    r"""Print the category graph without collapsing equal display names."""
    nodes = _category_graph_nodes(category)
    edges = _category_graph_edges(nodes)
    labels = _category_graph_labels(nodes)
    directed_acyclic = _identity_graph_is_directed_acyclic(nodes, edges)

    print(f"=== {label}: identity category graph ===")
    print(f"category: {category!r}")
    print(f"vertices: {len(nodes)}")
    print(f"edges: {len(edges)}")
    print(f"directed acyclic: {directed_acyclic}")
    for source, target in sorted(
        edges, key=lambda edge: (labels[id(edge[0])], labels[id(edge[1])])
    ):
        print(f"  {labels[id(source)]} -> {labels[id(target)]}")
    return directed_acyclic


def _check_category_graph(label: str, category: Any) -> list[GraphFailure]:
    failures: list[GraphFailure] = []
    category_repr = repr(category)

    if not _print_identity_category_graph(label, category):
        failures.append(
            GraphFailure(
                label,
                category_repr,
                "identity category graph",
                "AssertionError",
                "category graph is not a directed acyclic graph",
                "",
            )
        )

    try:
        category._test_category_graph()
    except Exception as exc:
        error_type, message, traceback_text = _format_exception(exc)
        failures.append(
            GraphFailure(
                label,
                category_repr,
                "category._test_category_graph()",
                error_type,
                message,
                traceback_text,
            )
        )

    return failures


def main() -> int:
    checks = project_category_checks()
    failures: list[GraphFailure] = []

    for check in checks:
        failures.extend(_check_category_graph(check.label, check.category))

    if not failures:
        print("Sage category graph validation passed.")
        return 0

    print("Sage category graph validation failed.")
    for failure in failures:
        print()
        print(f"=== FAILURE: {failure.label} ===")
        print(f"category: {failure.category_repr}")
        print(f"check: {failure.check}")
        print(f"error: {failure.error_type}: {failure.message}")
        if failure.traceback_text:
            print(failure.traceback_text.rstrip())
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
