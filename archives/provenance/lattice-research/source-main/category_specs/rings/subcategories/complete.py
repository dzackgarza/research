r"""CompleteRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .topological import _TopologicalRings as _TopologicalRings

if TYPE_CHECKING:
    pass


class _CompleteRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Topological().Complete()``."""

    _base_category_class_and_axiom = (_TopologicalRings, "Complete")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complete rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_TopologicalRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_complete_ring()

    class ParentMethods:
        @override
        @final
        def is_complete_ring(self) -> bool:
            return True

    class ElementMethods: ...
