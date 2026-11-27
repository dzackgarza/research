r"""Cartesian products of modules."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category

from ....cat import CartesianProductsCategory

if TYPE_CHECKING:
    from ....types import RingElement, RModuleElement
    from ... import _RModElements, _RModObjects


class _CartesianProducts(CartesianProductsCategory):
    r"""Canonical chain: ``Modules(R).CartesianProducts()``."""

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Declare that M x N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        _sets: Sequence[_RModObjects]

        @abstractmethod
        def _cartesian_product_of_elements(
            self, elements: Iterable[RModuleElement]
        ) -> RModuleElement: ...

        @override
        @final
        def __init_extra__(self) -> None:
            factors = self._sets
            assert len(factors) > 0, f"No factors found in {self}: {factors}"
            R = factors[0].base_ring()
            assert all(Mi.base_ring() is R for Mi in factors)
            self._base = R

    class ElementMethods:
        @abstractmethod
        def parent(self) -> _CartesianProducts.ParentMethods: ...

        @abstractmethod
        def cartesian_factors(self) -> Sequence[_RModElements]: ...

        @override
        @final
        def _lmul_(self, x: RingElement) -> RModuleElement:
            return self.parent()._cartesian_product_of_elements(
                y._lmul_(x) for y in self.cartesian_factors()
            )
