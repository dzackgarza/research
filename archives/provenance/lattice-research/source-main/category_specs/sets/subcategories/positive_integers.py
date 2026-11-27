r"""One-object subcategory for Sage ``PositiveIntegers()``."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.category_singleton import Category_singleton

if TYPE_CHECKING:
    from ...types import SetElement, SympySet

from ...cat import Category
from .. import Sets
from .integer_range import _IntegerRangeSets


class _PositiveIntegersSets(Category_singleton):
    r"""The countably infinite facade set ``{1, 2, 3, ...}`` inside ``ZZ``.

    Constructor target:
    ``Sets().Constructors().PositiveIntegers()`` refines Sage's named parent
    here and inherits the integer-range surface.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_IntegerRangeSets(), Sets().Countable().Infinite().Facade()]

    class ParentMethods:
        @override
        @abstractmethod
        def an_element(self) -> SetElement: ...

        @override
        @abstractmethod
        def _sympy_(self) -> SympySet: ...

    class ElementMethods: ...
