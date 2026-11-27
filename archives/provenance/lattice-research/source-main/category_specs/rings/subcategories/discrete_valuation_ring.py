r"""DiscreteValuationRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.discrete_valuation import (
    DiscreteValuationRings as SageDiscreteValuationRings,
)
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ._lazy_subcategories import _EuclideanDomains
from .valued import _ValuedRings as _ValuedRings

if TYPE_CHECKING:
    from ...types import (
        RingElement,
    )


class _DiscreteValuationRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().WithValuation().DiscretelyValued()``."""

    _base_category_class_and_axiom = (_ValuedRings, "DiscretelyValued")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "discrete valuation rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageDiscreteValuationRings(), _EuclideanDomains(), _ValuedRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageDiscreteValuationRings() or (
            R in self.base_category() and R.is_discrete_valuation_ring()
        )

    class ParentMethods:
        @override
        @final
        def is_discrete_valuation_ring(self) -> bool:
            return True

        @abstractmethod
        def uniformizer_pow(self, n: Integer) -> RingElement: ...

        @abstractmethod
        def residue_characteristic(self) -> Integer: ...

    class ElementMethods: ...
