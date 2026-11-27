r"""Cartesian-product construction for sets."""

from __future__ import annotations

from ....cat import CartesianProductsCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products of sets.

    Canonical chain: ``Sets().CartesianProducts()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
