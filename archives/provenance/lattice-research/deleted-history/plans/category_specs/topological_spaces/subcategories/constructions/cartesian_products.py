r"""Cartesian-product construction category for topological spaces."""

from __future__ import annotations

from ....cat import CartesianProductsCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products equipped with the product topology.

    Canonical chain: ``TopologicalSpaces().CartesianProducts()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
