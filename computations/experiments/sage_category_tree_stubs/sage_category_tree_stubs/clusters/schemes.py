"""Schemes cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = "Schemes"
NODES = [
    "Schemes(S)",
    "Varieties(K) = Schemes.Integral.Separated.FiniteType",
    "Curves(K) = Schemes.RelativeDimension(1)",
    "Surfaces(K) = Schemes.RelativeDimension(2)",
    "Hypersurfaces(K)",
    "CompleteIntersections(K)",
    "ToricVarieties(K)",
    "AlgebraicSpaces",
]
AXIOMS = [
    ("Schemes(S)", "Affine"),
    ("Schemes(S)", "Separated"),
    ("Schemes(S)", "Proper"),
    ("Schemes(S)", "Smooth"),
    ("Schemes(S)", "Unramified"),
    ("Schemes(S)", "Étale"),
    ("Schemes(S)", "Flat"),
    ("Schemes(S)", "Finite"),
    ("Schemes(S)", "Projective"),
    ("Schemes(S)", "LocallyFinitePresentation"),
    ("Schemes(S)", "Integral"),
    ("Schemes(S)", "FiniteType"),
    ("Schemes(S)", "RelativeDimension"),
    ("Schemes(S)", "RelativeDimension_1"),
    ("Schemes(S)", "RelativeDimension_2"),
]
NAMED_JOINS = [
    "Varieties(K) = Schemes.Integral.Separated.FiniteType",
    "Curves(K) = Schemes.RelativeDimension(1)",
    "Surfaces(K) = Schemes.RelativeDimension(2)",
]


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
