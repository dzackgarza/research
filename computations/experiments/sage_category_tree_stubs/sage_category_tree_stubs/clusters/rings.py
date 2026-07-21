"""Rings cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = "Rings"
NODES = [
    "Rngs",
    "Rings",
    "Fields",
    "CohomologyRings",
    "DeRhamCohomologyRings",
    "CommRings = Rings.Commutative",
    "Domains = Rings.Domain",
    "IntegralDomains = Domains.Commutative",
    "GCDDomains = Rings.Commutative.GCDDomain",
    "UFDs = Rings.Commutative.UFD",
    "PIDs = Rings.Commutative.PID",
    "EuclideanDomains = Rings.Commutative.Euclidean",
    "NoetherianCommRings = Rings.Commutative.Noetherian",
    "FiniteRings = Rings.Finite",
    "FiniteFields = Fields.Finite",
    "DivisionRings = Magmas.Inverse",
]
AXIOMS = [
    ("Rings", "Domain"),
    ("Domains = Rings.Domain", "IntegralDomain"),
    ("IntegralDomains = Domains.Commutative", "GCDDomain"),
    ("IntegralDomains = Domains.Commutative", "UFD"),
    ("IntegralDomains = Domains.Commutative", "PID"),
    ("IntegralDomains = Domains.Commutative", "Euclidean"),
    ("CommRings = Rings.Commutative", "Noetherian"),
]
NAMED_JOINS = [
    "CommRings = Rings.Commutative",
    "Domains = Rings.Domain",
    "IntegralDomains = Domains.Commutative",
    "GCDDomains = Rings.Commutative.GCDDomain",
    "UFDs = Rings.Commutative.UFD",
    "PIDs = Rings.Commutative.PID",
    "EuclideanDomains = Rings.Commutative.Euclidean",
    "NoetherianCommRings = Rings.Commutative.Noetherian",
    "FiniteRings = Rings.Finite",
    "FiniteFields = Fields.Finite",
    "DivisionRings = Magmas.Inverse",
]


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
