r"""Cartesian products of categories."""

from __future__ import annotations

from ... import CartesianProductsCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Product categories.

    Canonical chain: ``Cat().CartesianProducts()``.
    """

    class ParentMethods: ...

    class ElementMethods: ...
