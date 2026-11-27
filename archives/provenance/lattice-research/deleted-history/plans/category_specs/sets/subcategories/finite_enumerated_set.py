r"""One-object subcategory for Sage ``FiniteEnumeratedSet`` parents."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement


from ...cat import Category
from .. import Sets


class _FiniteEnumeratedSetObjects(Category_singleton):
    r"""Tuple-backed finite facade sets from ``sage.sets.finite_enumerated_set``.

    Constructor target:
    ``Sets().Constructors().FiniteEnumeratedSet(elements)`` refines here as a
    finite countable facade set.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Finite().Facade()]

    class ParentMethods:
        @abstract_method
        def __bool__(self) -> bool: ...

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @override
        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstract_method
        def an_element(self) -> SetElement: ...

        @override
        @abstract_method
        def random_element(self) -> SetElement: ...

        @override
        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @override
        @abstract_method
        def rank(self, x: SetElement) -> Integer: ...

        @abstract_method
        def __call__(self, el: SetElement) -> SetElement:
            r"""Return the finite enumerated element represented by ``el``."""
            ...

        @override
        @abstract_method
        def _element_constructor_(self, el: SetElement) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
