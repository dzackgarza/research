r"""Cartesian-product construction category for lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from ....cat import CartesianProductsCategory

if TYPE_CHECKING:
    from ... import LatticesCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products of lattices with the product bilinear form.

    Canonical chain: ``Lattices(R).CartesianProducts()``.
    """

    @final
    def extra_super_categories(self) -> list[LatticesCategory]:
        return [self.base_category()]

    class ParentMethods: ...

    class ElementMethods: ...
