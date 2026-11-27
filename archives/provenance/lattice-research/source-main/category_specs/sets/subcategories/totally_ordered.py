r"""Totally ordered set subcategory."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

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
        @final
        def is_totally_ordered(self) -> bool:
            return True

        @abstractmethod
        def rank(self, x: SetElement) -> Integer:
            r"""Return the order rank of ``x`` in this totally ordered set."""
            ...

        @abstractmethod
        def min(self) -> SetElement:
            r"""Return the least element of this totally ordered set."""
            ...

        @abstractmethod
        def max(self) -> SetElement:
            r"""Return the greatest element of this totally ordered set."""
            ...

    class ElementMethods:
        @abstractmethod
        def __lt__(self, other: _TotallyOrdered.ElementMethods) -> bool: ...

        @abstractmethod
        def __le__(self, other: _TotallyOrdered.ElementMethods) -> bool: ...

        @final
        def __gt__(self, other: _TotallyOrdered.ElementMethods) -> bool:
            return other.__lt__(self)

        @final
        def __ge__(self, other: _TotallyOrdered.ElementMethods) -> bool:
            return other.__le__(self)
