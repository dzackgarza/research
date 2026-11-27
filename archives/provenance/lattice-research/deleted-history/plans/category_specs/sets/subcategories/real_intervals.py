r"""One-object subcategory for ``RealSet`` -- subsets of R as finite unions of intervals.

``RealSet`` inherits ``Set_base``, ``Set_boolean_operators``, ``Set_add_sub_operators``.
Its Sage category is ``TopologicalSpaces()``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import RealNumber, Set, SetElement, SympySet


def _Sets():
    from .. import Sets as _S
    return _S()


class _RealSets(Category_singleton):
    r"""Category for ``RealSet`` -- finite unions of real intervals."""

    def super_categories(self) -> list:
        return [_Sets().Topological(), _Sets().WithBooleanOps()]

    class ParentMethods:
        @abstract_method
        def union(self, X: Set) -> Set: ...

        @abstract_method
        def intersection(self, X: Set) -> Set: ...

        @abstract_method
        def difference(self, X: Set) -> Set: ...

        @abstract_method
        def symmetric_difference(self, X: Set) -> Set: ...

        @abstract_method
        def complement(self) -> Set:
            r"""Return the complement of ``self`` in R."""
            ...

        @abstract_method
        def is_empty(self) -> bool: ...

        @abstract_method
        def is_finite(self) -> bool: ...

        @abstract_method
        def is_connected(self) -> bool: ...

        @abstract_method
        def inf(self) -> RealNumber:
            r"""Return the infimum of ``self`` in R u {+-oo}."""
            ...

        @abstract_method
        def sup(self) -> RealNumber:
            r"""Return the supremum of ``self`` in R u {+-oo}."""
            ...

        @abstract_method
        def measure(self) -> RealNumber:
            r"""Return the Lebesgue measure of ``self``."""
            ...

        @abstract_method
        def closure(self) -> Set: ...

        @abstract_method
        def interior(self) -> Set: ...

        @abstract_method
        def boundary(self) -> Set: ...

        @abstract_method
        def contains(self, x: SetElement) -> bool:
            r"""Return whether ``x`` is in ``self`` (alias for ``__contains__``)."""
            ...

        @abstract_method
        def __contains__(self, x: SetElement) -> bool: ...

        @abstract_method
        def __iter__(self):
            r"""Iterate over the ``InternalRealInterval`` components of ``self``."""
            ...

        @abstract_method
        def n_components(self) -> int:
            r"""Return the number of connected components (intervals)."""
            ...

        @abstract_method
        def is_open(self) -> bool: ...

        @abstract_method
        def is_closed(self) -> bool: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...
