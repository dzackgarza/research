r"""Infinite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality

from .. import Sets


class _InfiniteSets(CategoryWithAxiom):
    r"""Canonical chain: ``Sets().Infinite()``."""

    _base_category_class_and_axiom = (Sets, "Infinite")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "infinite sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageSets().Infinite(), Sets()]

    @override
    @final
    def __contains__(self, S: Any) -> bool:
        return S in SageSets().Infinite() or (
            S in self.base_category() and not S.is_finite()
        )

    class ParentMethods:
        @override
        @final
        def is_finite(self) -> bool:
            return False

        @override
        @final
        def cardinality(self) -> Cardinality:
            from sage.rings.infinity import infinity

            return infinity

        @override
        @final
        def is_empty(self) -> bool:
            return False

    class ElementMethods: ...
