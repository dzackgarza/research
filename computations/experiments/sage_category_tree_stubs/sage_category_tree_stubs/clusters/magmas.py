"""Magmas cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = "Magmas"
NODES = [
    "Magmas",
    "Magmas.Additive",
    "Magmas.Multiplicative",
    "CoxeterGroups",
    "WeylGroups",
    "ReflectionGroups",
    "OrthogonalGroups",
    "IsometryGroups",
    "Pic",
    "Div",
    "NS",
    "Cycles",
    "ChowGroups",
    "HodgeStructures",
    "Semigroups = Magmas.Associative",
    "Monoids = Magmas.Associative.Unital",
    "Groups = Magmas.Associative.Unital.Inverse",
    "AbelianGroups = Groups.Commutative",
    "FinitelyGeneratedGroups = Magmas.Associative.Unital.Inverse.FinitelyGenerated",
    "AdditiveSemigroups = Magmas.Additive.Associative",
    "AdditiveMonoids = Magmas.Additive.Associative.Unital",
    "AdditiveGroups = Magmas.Additive.Associative.Unital.Inverse",
    "AdditiveAbelianGroups = AdditiveGroups.Commutative",
]
AXIOMS = [
    ("Magmas", "Associative"),
    ("Magmas", "Commutative"),
    ("Magmas", "Unital"),
    ("Magmas", "Inverse"),
    ("Magmas", "Additive"),  # Magmas.Additive = AdditiveMagmas (one-tower)
    ("Magmas", "Multiplicative"),
    ("Magmas", "FinitelyGenerated"),
    ("Magmas.Additive", "Associative"),
    ("Magmas.Additive", "Unital"),
    ("Magmas.Additive", "Inverse"),
    ("Magmas.Additive", "Commutative"),
]
NAMED_JOINS = [
    "Semigroups = Magmas.Associative",
    "Monoids = Magmas.Associative.Unital",
    "Groups = Magmas.Associative.Unital.Inverse",
    "AbelianGroups = Groups.Commutative",
    "FinitelyGeneratedGroups = Magmas.Associative.Unital.Inverse.FinitelyGenerated",
    "AdditiveSemigroups = Magmas.Additive.Associative",
    "AdditiveMonoids = Magmas.Additive.Associative.Unital",
    "AdditiveGroups = Magmas.Additive.Associative.Unital.Inverse",
    "AdditiveAbelianGroups = AdditiveGroups.Commutative",
]


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
