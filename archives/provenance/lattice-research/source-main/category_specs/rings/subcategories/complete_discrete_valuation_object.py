r"""CompleteDiscreteValuationObjects ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _CompleteDiscreteValuationFields,
    _CompleteDiscreteValuationRings,
    _CompleteRings,
    _ValuedRings,
)

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        RingElement,
    )


class _CompleteDiscreteValuationObjects(Category_singleton):
    r"""Common element surface for complete discrete valuation rings and fields.

    Constructor target: complete discrete valuation ring and field families
    refine through this shared element-surface category.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complete discrete valuation rings and fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_CompleteRings(), _ValuedRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in _CompleteDiscreteValuationRings() or (
            R in _CompleteDiscreteValuationFields()
        )

    class ElementMethods:
        @abstractmethod
        def valuation(self) -> Cardinality: ...

        @abstractmethod
        def denominator(self) -> RingElement: ...

        @abstractmethod
        def numerator(self) -> RingElement: ...

        @abstractmethod
        def lift_to_precision(self, absprec: Integer | None = None) -> RingElement: ...

    class ParentMethods: ...
