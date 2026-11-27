r"""One-object subcategory for Sage ``NonNegativeIntegers()``."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import SetElement, SympySet


from ...cat import Category
from .. import Sets


class _NonNegativeIntegersSets(Category_singleton):
    r"""The countably infinite facade set ``{0, 1, 2, ...}`` inside ``ZZ``.

    Constructor target:
    ``Sets().Constructors().NonNegativeIntegers()`` refines Sage's named
    parent here.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Infinite().Facade()]

    class ParentMethods:
        @override
        @final
        def is_finite(self) -> bool:
            return False

        @override
        @abstract_method
        def __contains__(self, elt: Any) -> bool: ...

        @override
        @abstract_method
        def _element_constructor_(self, i: SetElement) -> SetElement: ...

        @override
        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstract_method
        def an_element(self) -> SetElement: ...

        @override
        @abstract_method
        def some_elements(self) -> list[SetElement]: ...

        @override
        @abstract_method
        def _sympy_(self) -> SympySet: ...

    class ElementMethods: ...
    class MorphismMethods: ...
