"""Sets cluster stubs."""

from __future__ import annotations

from sage.categories.category import Category

from ._base import axiom, cat

CLUSTER = 'Sets'
NODES = [
    "Sets",
    "Homsets",
    "Sets.Finite",
    "Sets.Infinite",
    "Sets.Countable",
    "Sets.Graded",
    "CountableInfiniteSets = Sets.Countable.Infinite",
]
AXIOMS = [('Sets', 'Finite'), ('Sets', 'Infinite'), ('Sets', 'Countable'), ('Sets', 'Uncountable'), ('Sets', 'Graded')]
NAMED_JOINS = ['CountableInfiniteSets = Sets.Countable.Infinite']


def categories() -> dict[str, Category]:
    return {node: cat(node) for node in NODES}


def axiom_categories() -> dict[tuple[str, str], Category]:
    return {(host, name): axiom(host, name) for host, name in AXIOMS}
