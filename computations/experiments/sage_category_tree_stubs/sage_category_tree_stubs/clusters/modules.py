"""Modules cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = "Modules"
NODES = [
    "Modules(R)",
    "LeftModules(R)",
    "RightModules(R)",
    "Bimodules(R,S)",
    "Bimodules(R,R)",
    "VectorFieldModules",
    "TensorFieldModules",
    "DiffFormModules",
    "FreeModules = Modules.Free",
    "ProjectiveModules = Modules.Projective",
    "ModulesWithBasis = Modules.WithBasis",
    "ModulesWithGenerators = Modules.WithGenerators",
    "FiniteRankModules = Modules.FiniteRank",
    "FinitelyGeneratedModules = Modules.FinitelyGenerated",
    "FinitelyPresentedModules = Modules.FinitelyPresented",
    "VectorSpaces(K) = Modules.OverField",
    "VectorSpacesWithBasis = VectorSpaces.WithBasis",
]
AXIOMS = [
    ("Modules(R)", "Free"),
    ("Modules(R)", "Projective"),
    ("Modules(R)", "WithBasis"),
    ("Modules(R)", "WithGenerators"),
    ("Modules(R)", "FiniteRank"),
    ("Modules(R)", "FinitelyGenerated"),
    ("Modules(R)", "FinitelyPresented"),
    ("Modules(R)", "Torsion"),
    ("Modules(R)", "TorsionFree"),
    ("Modules(R)", "OverField"),
]
NAMED_JOINS = [
    "FreeModules = Modules.Free",
    "ProjectiveModules = Modules.Projective",
    "ModulesWithBasis = Modules.WithBasis",
    "ModulesWithGenerators = Modules.WithGenerators",
    "FiniteRankModules = Modules.FiniteRank",
    "FinitelyGeneratedModules = Modules.FinitelyGenerated",
    "FinitelyPresentedModules = Modules.FinitelyPresented",
    "VectorSpaces(K) = Modules.OverField",
    "VectorSpacesWithBasis = VectorSpaces.WithBasis",
]


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
