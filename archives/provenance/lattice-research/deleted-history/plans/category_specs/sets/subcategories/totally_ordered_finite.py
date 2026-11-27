r"""One-object subcategory for Sage ``TotallyOrderedFiniteSet`` parents."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

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
        @abstract_method
        def _element_constructor_(self, data: SetElement) -> SetElement: ...

        @abstract_method
        def le(self, x: SetElement, y: SetElement) -> bool:
            r"""Return whether ``x`` is at most ``y`` in the finite total order."""
            ...

        @override
        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @override
        @abstract_method
        def rank(self, x: SetElement) -> Integer: ...

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @override
        @abstract_method
        def min(self) -> SetElement: ...

        @override
        @abstract_method
        def max(self) -> SetElement: ...

    class ElementMethods:
        @override
        @abstract_method
        def __eq__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __ne__(self, other: SetElement) -> bool: ...

        @override
        @abstract_method
        def __lt__(self, other: SetElement) -> bool: ...

        @override
        @abstract_method
        def __le__(self, other: SetElement) -> bool: ...

        @override
        @abstract_method
        def __gt__(self, other: SetElement) -> bool: ...

        @override
        @abstract_method
        def __ge__(self, other: SetElement) -> bool: ...

    class MorphismMethods: ...
