"""Cluster subtrees of the category parent graph.

Each module names the solid categories, axioms introduced on the cluster's
hosts, and named axiomatic joins owned by that cluster. Categories themselves
are materialized by :mod:`sage_category_tree_stubs.factory`.
"""

from . import (
    algebras,
    cat_object,
    convex,
    forms,
    graphs,
    magmas,
    modules,
    rings,
    schemes,
    semirings,
    sets,
    spaces,
    stacks,
)

CLUSTERS = (
    cat_object,
    sets,
    spaces,
    convex,
    graphs,
    magmas,
    semirings,
    rings,
    modules,
    algebras,
    forms,
    schemes,
    stacks,
)

__all__ = ["CLUSTERS"]
