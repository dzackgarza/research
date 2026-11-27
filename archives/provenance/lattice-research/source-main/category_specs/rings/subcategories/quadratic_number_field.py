r"""QuadraticNumberFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.rings.number_field.number_field import (
    NumberField_quadratic,
)

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .number_field import _NumberFields as _NumberFields

if TYPE_CHECKING:
    pass


class _QuadraticNumberFields(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().Field().NumberFields().QuadraticNumberField()``.
    """

    _base_category_class_and_axiom = (_NumberFields, "QuadraticNumberField")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "quadratic number fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_NumberFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        if isinstance(R, NumberField_quadratic):
            return True
        if R in SageNumberFields():
            return bool(R.degree() == 2)
        if R not in self.base_category():
            return False
        return bool(R.is_quadratic_number_field())

    class ParentMethods:
        @final
        def is_quadratic(self) -> bool:
            return True

        @override
        @final
        def is_quadratic_number_field(self) -> bool:
            return True

    class ElementMethods: ...
