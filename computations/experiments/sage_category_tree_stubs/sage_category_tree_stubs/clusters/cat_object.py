"""CatObject cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = "CatObject"
NODES = [
    "CatObject",
    "Cat_1",
    "Cat_2",
    "CatObject.Thin",
    "CatObject.Limits",
    "CatObject.Colimits",
    "Groupoids",
    "Bicategories",
    "TensorProducts = CatObject.Monoidal",
    "DualObjects",
    "Arr(−)",
    "(−)^op",
    "Comma",
    "Slices",
    "Coslices",
    "Subobjects",
    "Quotients",
    "Subquotients",
    "IsomorphicObjects",
    "DiagramCategories",
    "FunctorCategories",
    "HomCategories",
    "G-Objects(G)",
    "FibredCategories",
    "GroupoidObjects",
    "Torsors",
    "Sites",
    "Presheaves",
    "Sheaves",
    "Topoi",
    "RingedSites",
    "RingedTopoi",
    "Mod(O_X)",
    "Coh(X)",
    "QCoh(X)",
]
AXIOMS = [
    ("CatObject", "LocallySmall"),
    ("CatObject", "Finite"),
    ("CatObject", "Thin"),
    ("CatObject", "Limits"),
    ("CatObject", "Colimits"),
    ("CatObject.Limits", "Products"),
    ("CatObject.Colimits", "Coproducts"),
    ("CatObject", "Monoidal"),
]
NAMED_JOINS = [
    "TensorProducts = CatObject.Monoidal",
]


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
