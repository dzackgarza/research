r"""Cartesian-product construction category for posets."""

from __future__ import annotations

from ....cat import CartesianProductsCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products equipped with the product order.

    Canonical chain: ``Posets().CartesianProducts()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
