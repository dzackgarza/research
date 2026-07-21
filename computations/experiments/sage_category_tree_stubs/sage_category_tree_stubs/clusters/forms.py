"""Forms cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = 'Forms'
NODES = [
    "∫Hom_R(−,W)",
    "∫Bil_R(W)",
    "∫Quad_R(W)",
    "∫Herm_R(W)",
    "Genera",
    "LatticeHomsets",
    "RootLattices",
    "Lat_R = ∫Bil_R(R).Symmetric.Nondegenerate",
    "Lat.Definite",
    "Lat.Indefinite",
    "DiscBil = ∫Bil.Symmetric.Nondegenerate.Finite",
    "DiscQuad = ∫Quad.Nondegenerate",
    "∫Bil.SkewSymmetric",
]
AXIOMS = [
    ("∫Hom_R(−,W)", "Nondegenerate"),
    ("∫Hom_R(−,W)", "Even"),
    ("∫Hom_R(−,W)", "Odd"),
    ("∫Hom_R(−,W)", "Unimodular"),
    ("∫Bil_R(W)", "Symmetric"),
    ("∫Bil_R(W)", "SkewSymmetric"),
    ("∫Bil.SkewSymmetric", "Alternating"),
    ("Lat_R = ∫Bil_R(R).Symmetric.Nondegenerate", "Definite"),
    ("Lat_R = ∫Bil_R(R).Symmetric.Nondegenerate", "PositiveDefinite"),
    ("Lat_R = ∫Bil_R(R).Symmetric.Nondegenerate", "NegativeDefinite"),
    ("Lat_R = ∫Bil_R(R).Symmetric.Nondegenerate", "Indefinite"),
    ("Lat_R = ∫Bil_R(R).Symmetric.Nondegenerate", "Hyperbolic"),
]
NAMED_JOINS = ['Lat_R = ∫Bil_R(R).Symmetric.Nondegenerate', 'DiscBil = ∫Bil.Symmetric.Nondegenerate.Finite', 'DiscQuad = ∫Quad.Nondegenerate']


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
