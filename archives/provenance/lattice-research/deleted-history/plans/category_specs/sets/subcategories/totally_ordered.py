r"""Totally ordered set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Integer, SetElement

from .. import Sets


class _TotallyOrdered(CategoryWithAxiom):
    r"""Canonical chain: ``Sets().TotallyOrdered()``."""
    _base_category_class_and_axiom = (Sets, "TotallyOrdered")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "totally ordered sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets()]

    class ParentMethods:
        @override
        @final
        def is_totally_ordered(self) -> bool:
            return True

        @abstract_method
        def rank(self, x: SetElement) -> Integer:
            r"""Return the order rank of ``x`` in this totally ordered set."""
            ...

        @abstract_method
        def min(self) -> SetElement:
            r"""Return the least element of this totally ordered set."""
            ...

        @abstract_method
        def max(self) -> SetElement:
            r"""Return the greatest element of this totally ordered set."""
            ...

    class ElementMethods:
        @abstract_method
        def __lt__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __le__(self, other: SetElement) -> bool: ...

        @override
        @final
        def __gt__(self, other: SetElement) -> bool:
            return other.__lt__(self)

        @override
        @final
        def __ge__(self, other: SetElement) -> bool:
            return other.__le__(self)

    class MorphismMethods: ...
