r"""CompleteDiscreteValuationRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.complete_discrete_valuation import (
    CompleteDiscreteValuationRings as SageCompleteDiscreteValuationRings,
)

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _CompleteDiscreteValuationObjects,
    _DiscreteValuationRings,
)

if TYPE_CHECKING:
    pass


class _CompleteDiscreteValuationRings(Category_singleton):
    r"""Complete discrete valuation rings.

    Constructor target: complete valued ring families such as
    ``Rings().Constructors().Zp(...)`` refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complete discrete valuation rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            SageCompleteDiscreteValuationRings(),
            _CompleteDiscreteValuationObjects(),
            _DiscreteValuationRings(),
        ]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageCompleteDiscreteValuationRings() or (
            R in _DiscreteValuationRings() and R.is_complete_discrete_valuation_ring()
        )

    class ParentMethods:
        @override
        @final
        def is_complete_discrete_valuation_ring(self) -> bool:
            return True

    class ElementMethods: ...
