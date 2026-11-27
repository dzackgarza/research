r"""CompleteDiscreteValuationFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.complete_discrete_valuation import (
    CompleteDiscreteValuationFields as SageCompleteDiscreteValuationFields,
)

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _CompleteDiscreteValuationObjects,
    _DiscreteValuationFields,
)

if TYPE_CHECKING:
    pass


class _CompleteDiscreteValuationFields(Category_singleton):
    r"""Complete discrete valuation fields.

    Constructor target: complete valued field families such as
    ``Rings().Constructors().Qp(...)`` refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complete discrete valuation fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            SageCompleteDiscreteValuationFields(),
            _CompleteDiscreteValuationObjects(),
            _DiscreteValuationFields(),
        ]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageCompleteDiscreteValuationFields() or (
            R in _DiscreteValuationFields() and R.is_complete_discrete_valuation_field()
        )

    class ParentMethods:
        @override
        @final
        def is_complete_discrete_valuation_field(self) -> bool:
            return True

    class ElementMethods: ...
