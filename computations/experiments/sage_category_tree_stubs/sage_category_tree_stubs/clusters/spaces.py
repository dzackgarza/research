"""Spaces cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = "Spaces"
NODES = [
    "TopologicalSpaces",
    "MetricSpaces",
    "Manifolds",
    "Manifolds.Smooth",
    "Manifolds.PL",
    "RingedSpaces",
    "LocallyRingedSpaces",
    "StratifiedSpaces",
]
AXIOMS = [
    ("Manifolds", "Smooth"),
    ("Manifolds", "PL"),
]
NAMED_JOINS: list[str] = []


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
