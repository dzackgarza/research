r"""Cartesian-product construction category for topological spaces."""

from __future__ import annotations

from typing import final, override

from ....cat import CartesianProductsCategory, Category


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products equipped with the product topology.

    Canonical chain: ``TopologicalSpaces().CartesianProducts()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return project product categories without Sage axiom reapplication."""
        from ....sets import Sets

        return [self.base_category(), Sets().CartesianProducts()]

    class ParentMethods: ...

    class ElementMethods: ...
