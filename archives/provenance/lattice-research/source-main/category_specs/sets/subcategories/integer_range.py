r"""One-object subcategory for Sage ``IntegerRange`` parents."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, cast, final, override

from sage.categories.category_singleton import Category_singleton
from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.sets.integer_range import (
    IntegerRangeEmpty as SageIntegerRangeEmpty,
)
from sage.sets.integer_range import (
    IntegerRangeFinite as SageIntegerRangeFinite,
)
from sage.sets.integer_range import (
    IntegerRangeFromMiddle as SageIntegerRangeFromMiddle,
)
from sage.sets.integer_range import (
    IntegerRangeInfinite as SageIntegerRangeInfinite,
)

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement


from ...cat import Category
from .. import Sets


class _IntegerRangeSets(Category_singleton):
    r"""Arithmetic progressions of integers, finite or infinite by bounds.

    Constructor target:
    ``Sets().Constructors().IntegerRange(...)`` refines Sage integer ranges
    here as countable facade sets.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Facade()]

    class ParentMethods:
        @override
        @final
        def _element_constructor_(self, el: SetElement) -> SetElement:
            if el in self:
                from sage.rings.integer import Integer

                if not isinstance(el, Integer):
                    return cast("SetElement", Integer(el))
                return cast("SetElement", el)
            raise ValueError(f"{el} not in {self}")

        @override
        @final
        def __contains__(self, elt: Any) -> bool:
            from sage.rings.integer import Integer

            try:
                elt = Integer(elt)
            except (TypeError, ValueError):
                return False

            if isinstance(self, SageIntegerRangeEmpty):
                return False
            if isinstance(self, SageIntegerRangeFromMiddle):
                return cast(bool, SageIntegerRangeFromMiddle.__contains__(self, elt))
            if isinstance(self, SageIntegerRangeFinite):
                return cast(bool, SageIntegerRangeFinite.__contains__(self, elt))
            if isinstance(self, SageIntegerRangeInfinite):
                return cast(bool, SageIntegerRangeInfinite.__contains__(self, elt))
            raise TypeError(
                f"unsupported Sage integer range wrapper: {type(self).__name__}"
            )

        @override
        @final
        def cardinality(self) -> Cardinality:
            if self.is_finite():
                from sage.categories.finite_enumerated_sets import (
                    FiniteEnumeratedSets as SageFiniteEnumeratedSets,
                )

                return SageFiniteEnumeratedSets.ParentMethods.cardinality(self)

            from sage.rings.infinity import infinity

            return infinity

        @override
        @final
        def rank(self, x: SetElement) -> Integer:
            return SageEnumeratedSets.ParentMethods.rank(self, x)

        @override
        @final
        def __getitem__(self, i: Integer) -> SetElement:
            return cast(
                "SetElement", SageEnumeratedSets.ParentMethods.__getitem__(self, i)
            )

        @override
        @final
        def __iter__(self) -> Iterator[SetElement]:
            return cast(
                "Iterator[SetElement]", SageEnumeratedSets.ParentMethods.__iter__(self)
            )

        @override
        @final
        def _an_element_(self) -> SetElement:
            return cast(
                "SetElement", SageEnumeratedSets.ParentMethods._an_element_(self)
            )

    class ElementMethods: ...
