r"""CyclotomicFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.rings.number_field.number_field import (
    NumberField_cyclotomic,
)

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .number_field import _NumberFields as _NumberFields

if TYPE_CHECKING:
    pass


class _CyclotomicFields(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().Field().NumberFields().Cyclotomic()``.
    """

    _base_category_class_and_axiom = (_NumberFields, "Cyclotomic")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "cyclotomic fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_NumberFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        if isinstance(R, NumberField_cyclotomic):
            return True
        if R in SageNumberFields():
            return False
        return R in self.base_category() and R.is_cyclotomic_field()

    class ParentMethods:
        @final
        def is_cyclotomic(self) -> bool:
            return True

        @override
        @final
        def is_cyclotomic_field(self) -> bool:
            return True

    class ElementMethods: ...
