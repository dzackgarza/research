r"""Uncountable set subcategory."""

from __future__ import annotations

from typing import final, override

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Sets


class _UncountableSets(CategoryWithAxiom):
    r"""Canonical chain: ``Sets().Uncountable()``."""
    _base_category_class_and_axiom = (Sets, "Uncountable")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "uncountable sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Infinite()]

    class ParentMethods:
        @override
        @final
        def is_countable(self) -> bool:
            return False

        @override
        @final
        def is_uncountable(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
