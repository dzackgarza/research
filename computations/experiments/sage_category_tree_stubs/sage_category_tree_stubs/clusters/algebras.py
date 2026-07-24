"""Algebras cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = "Algebras"
NODES = [
    "Algebras(R)",
    "Algebras(R).Graded",
    "LieAlgebras(R)",
    "CliffordAlgebras(R)",
    "SymmetricAlgebras(R)",
    "ExteriorAlgebras(R)",
    "TensorAlgebras(R)",
    "HopfAlgebras(R)",
    "Coalgebras(R)",
    "Bialgebras(R)",
    "C∞Algebras(R)",
    "ChainComplexes(C)",
    "CochainComplexes(C)",
    "DeRhamComplexes",
    "Homology",
    "AssociativeAlgebras = Algebras.Associative",
    "UnitalAlgebras = Algebras.Associative.Unital",
    "CommAlgebras = UnitalAlgebras.Commutative",
    "NonUnitalDGAs = Algebras.Differential",
    "DGAs = UnitalAlgebras.Differential",
    "AlgebrasOverField = Algebras.OverField",
]
AXIOMS = [
    ("Algebras(R)", "Differential"),
    ("Algebras(R)", "OverField"),
    ("Algebras(R)", "Graded"),
]
NAMED_JOINS = [
    "AssociativeAlgebras = Algebras.Associative",
    "UnitalAlgebras = Algebras.Associative.Unital",
    "CommAlgebras = UnitalAlgebras.Commutative",
    "NonUnitalDGAs = Algebras.Differential",
    "DGAs = UnitalAlgebras.Differential",
    "AlgebrasOverField = Algebras.OverField",
]


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
