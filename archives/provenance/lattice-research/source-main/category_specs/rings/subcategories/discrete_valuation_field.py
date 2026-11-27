r"""DiscreteValuationFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.discrete_valuation import (
    DiscreteValuationFields as SageDiscreteValuationFields,
)

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _DiscreteValuationRings,
    _Fields,
)

if TYPE_CHECKING:
    pass


class _DiscreteValuationFields(Category_singleton):
    r"""Discrete valuation fields.

    Constructor target: valued field constructors such as
    ``Rings().Constructors().Qp(...)`` refine through this category.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "discrete valuation fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageDiscreteValuationFields(), _Fields(), _DiscreteValuationRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageDiscreteValuationFields() or (
            R in _Fields() and R.is_discrete_valuation_field()
        )

    class ParentMethods:
        @override
        @final
        def is_discrete_valuation_field(self) -> bool:
            return True

    class ElementMethods: ...
