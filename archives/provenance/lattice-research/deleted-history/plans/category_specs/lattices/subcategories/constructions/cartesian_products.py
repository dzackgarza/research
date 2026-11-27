r"""Cartesian-product construction category for lattices."""

from __future__ import annotations

from typing import final

from ....cat import CartesianProductsCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products of lattices with the product bilinear form.

    Canonical chain: ``Lattices(R).CartesianProducts()``.
    """

    @final
    def extra_super_categories(self):
        return [self.base_category()]

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
