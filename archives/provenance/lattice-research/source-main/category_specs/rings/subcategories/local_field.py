r"""LocalFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ._lazy_subcategories import _TopologicalRings
from .field import _Fields as _Fields

if TYPE_CHECKING:
    pass


class _LocalFields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field().LocalFields()``."""

    _base_category_class_and_axiom = (_Fields, "LocalFields")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "local fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_Fields(), _TopologicalRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_local_field()

    class ParentMethods:
        @override
        @final
        def is_local_field(self) -> bool:
            return True

    class ElementMethods: ...
