r"""One-object subcategory for Sage disjoint unions of enumerated sets."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement


from ...cat import Category
from .. import Sets


class _DisjointUnionEnumeratedSets(Category_singleton):
    r"""Countable coproduct of an indexed family of enumerated sets.

    Constructor target:
    ``Sets().Constructors().DisjointUnionEnumeratedSets(family)`` refines
    Sage's disjoint-union parent here.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def _is_a(self, x: SetElement) -> bool: ...

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
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def _element_constructor_default(self, el: SetElement) -> SetElement: ...

        @abstract_method
        def _element_constructor_facade(self, el: SetElement) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
