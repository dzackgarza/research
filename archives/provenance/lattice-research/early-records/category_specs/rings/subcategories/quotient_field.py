r"""QuotientFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.quotient_fields import QuotientFields as SageQuotientFields

from ...cat import Category, Category_singleton
from ._lazy_subcategories import _Fields

if TYPE_CHECKING:
    pass


class _QuotientFields(Category_singleton):
    r"""Quotient fields.

    Constructor target: field constructors whose objects are fraction fields,
    including ``QQ``, refine through this category.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "quotient fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageQuotientFields(), _Fields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageQuotientFields() or (R in _Fields() and R.is_quotient_field())

    class ParentMethods:
        @override
        @final
        def is_quotient_field(self) -> bool:
            return True

    class ElementMethods: ...
