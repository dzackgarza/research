r"""Cartesian-product construction for rings."""

from __future__ import annotations

from ....cat import CartesianProductsCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products of rings.

    Canonical chain: ``Rings().CartesianProducts()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
