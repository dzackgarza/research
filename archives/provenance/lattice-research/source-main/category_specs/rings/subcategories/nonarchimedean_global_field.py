r"""NonArchimedeanGlobalFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .global_field import _GlobalFields as _GlobalFields

if TYPE_CHECKING:
    pass


class _NonArchimedeanGlobalFields(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().Field().GlobalFields().NonArchimedean()``.
    """

    _base_category_class_and_axiom = (_GlobalFields, "NonArchimedean")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "nonarchimedean global fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_GlobalFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_nonarchimedean_global_field()

    class ParentMethods:
        @override
        @final
        def is_nonarchimedean_global_field(self) -> bool:
            return True

    class ElementMethods: ...
