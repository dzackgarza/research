r"""One-object subcategory for Sage ``TotallyOrderedFiniteSet`` parents."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, cast, final, override

from sage.categories.category_singleton import Category_singleton
from sage.categories.sets_cat import EmptySetError

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement


from ...cat import Category
from .. import Sets


class _TotallyOrderedFiniteSets(Category_singleton):
    r"""Finite sets equipped with a user-specified total order.

    Constructor target:
    ``Sets().Constructors().TotallyOrderedFiniteSet(elements)`` refines here
    as both finite countable and totally ordered.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Finite(), Sets().TotallyOrdered()]

    class ParentMethods:
        @override
        @abstractmethod
        def _element_constructor_(self, data: SetElement) -> SetElement: ...

        @abstractmethod
        def le(self, x: SetElement, y: SetElement) -> bool:
            r"""Return whether ``x`` is at most ``y`` in the finite total order."""
            ...

        @override
        @abstractmethod
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstractmethod
        def cardinality(self) -> Cardinality: ...

        @override
        @abstractmethod
        def rank(self, x: SetElement) -> Integer: ...

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool: ...

        @override
        @final
        def min(self) -> SetElement:
            try:
                return next(iter(self))
            except StopIteration:
                raise EmptySetError

        @override
        @final
        def max(self) -> SetElement:
            missing = object()
            last = missing
            for last in self:
                pass
            if last is missing:
                raise EmptySetError
            return cast("SetElement", last)

    class ElementMethods:
        @override
        @abstractmethod
        def __eq__(self, other: object) -> bool: ...

        @abstractmethod
        def __ne__(self, other: object) -> bool: ...

        @override
        @abstractmethod
        def __lt__(self, other: SetElement) -> bool: ...

        @override
        @abstractmethod
        def __le__(self, other: SetElement) -> bool: ...

        @override
        @abstractmethod
        def __gt__(self, other: SetElement) -> bool: ...

        @override
        @abstractmethod
        def __ge__(self, other: SetElement) -> bool: ...
