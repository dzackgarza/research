r"""Cartesian products of algebras."""

from __future__ import annotations

from typing import final, override

from ....cat import CartesianProductsCategory, Category


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products in a category of algebras.

    Canonical chain: ``Algebras(R).CartesianProducts()``.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return the algebra category inherited by Cartesian products."""
        return [self.base_category()]

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
