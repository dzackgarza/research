r"""DivisionRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.division_rings import DivisionRings as SageDivisionRings

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings

if TYPE_CHECKING:
    pass


class _DivisionRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Division()``."""

    _base_category_class_and_axiom = (Rings, "Division")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "division rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageDivisionRings(), Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageDivisionRings() or (
            R in self.base_category() and R.is_division_ring()
        )

    class ParentMethods:
        @override
        @final
        def is_division_ring(self) -> bool:
            return True

    class ElementMethods: ...
