"""Normalized category graph 𝒢 with Sage as a versioned backend correspondence.

Architectural decoupling (not a Sage rewrite)::

    DSL mathematics → 𝒢 → Sage-version correspondence → Sage implementations

See :mod:`sage_category_tree_stubs.architecture` and
:mod:`sage_category_tree_stubs.sage_correspondence`.

Cluster subtrees live in :mod:`sage_category_tree_stubs.clusters`. Categories
are materialized by :mod:`sage_category_tree_stubs.factory` from
``category_parent_graph.dot``.
"""

from .registry import CATEGORY_FACTORIES, get_category, instantiate_all

__all__ = [
    "CATEGORY_FACTORIES",
    "get_category",
    "instantiate_all",
]
