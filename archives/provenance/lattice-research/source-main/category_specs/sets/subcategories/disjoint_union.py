r"""One-object subcategory for Sage disjoint unions of enumerated sets."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton

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
        @abstractmethod
        def _is_a(self, x: SetElement) -> bool: ...

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool: ...

        @override
        @abstractmethod
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstractmethod
        def an_element(self) -> SetElement: ...

        @override
        @abstractmethod
        def cardinality(self) -> Cardinality: ...

        @abstractmethod
        def _element_constructor_default(self, el: SetElement) -> SetElement: ...

        @abstractmethod
        def _element_constructor_facade(self, el: SetElement) -> SetElement: ...

    class ElementMethods: ...
