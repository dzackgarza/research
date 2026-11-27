r"""One-object subcategory for Sage ``RealSet`` parents."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, final, overload, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        Integer,
        RealInterval,
        RealNumber,
        RealSubset,
        SetElement,
        SympySet,
    )


from ...cat import Category
from .. import Sets


class _RealSets(Category_singleton):
    r"""Sage real subsets represented as finite unions of real intervals.

    Constructor target:
    named real-subset constructors under ``Sets().Constructors()`` refine here
    and then into the applicable topological subobject categories.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        from ...topological_spaces import TopologicalSpaces

        return [Sets().Topological(), Sets().Subobjects(), TopologicalSpaces().Subobjects()]

    class ParentMethods:
        @override
        @abstract_method
        def __iter__(self) -> Iterator[RealInterval]: ...

        @abstract_method
        def n_components(self) -> Integer:
            r"""Return the number of interval components of this real subset."""
            ...

        @override
        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @override
        @abstract_method
        def is_empty(self) -> bool: ...

        @abstract_method
        def is_universe(self) -> bool:
            r"""Return whether this real subset is the whole real line."""
            ...

        @abstract_method
        def get_interval(self, i: Integer) -> RealInterval:
            r"""Return the ``i``-th interval component of this real subset."""
            ...

        @overload
        def union(self, other: RealSubset) -> RealSubset: ...

        @overload
        def union(self, real_set_collection: Sequence[RealSubset]) -> RealSubset: ...

        @override
        @abstract_method
        def union(
            self,
            other: RealSubset | Sequence[RealSubset],
        ) -> RealSubset:
            r"""Return the finite-interval-normalized union."""
            ...

        @overload
        def intersection(self, other: RealSubset) -> RealSubset: ...

        @overload
        def intersection(self, real_set_collection: Sequence[RealSubset]) -> RealSubset: ...

        @override
        @abstract_method
        def intersection(
            self,
            other: RealSubset | Sequence[RealSubset],
        ) -> RealSubset:
            r"""Return the finite-interval-normalized intersection."""
            ...

        @abstract_method
        def inf(self) -> RealNumber:
            r"""Return the infimum of this subset of the real line."""
            ...

        @abstract_method
        def sup(self) -> RealNumber:
            r"""Return the supremum of this subset of the real line."""
            ...

        @override
        @abstract_method
        def complement(self) -> RealSubset:
            r"""Return the finite-interval-normalized complement in the real line."""
            ...

        @override
        @abstract_method
        def difference(self, other: RealSubset) -> RealSubset:
            r"""Return the finite-interval-normalized set difference."""
            ...

        @override
        @abstract_method
        def symmetric_difference(self, other: RealSubset) -> RealSubset:
            r"""Return the finite-interval-normalized symmetric difference."""
            ...

        @abstract_method
        def contains(self, x: SetElement) -> bool:
            r"""Return whether the real point ``x`` lies in this real subset."""
            ...

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @staticmethod
        @abstract_method
        def convex_hull(real_set_collection: Sequence[RealSubset]) -> RealSubset:
            r"""Return the least real interval containing the given real subsets."""
            ...

        @abstract_method
        def is_disjoint(self, other: RealSubset) -> bool:
            r"""Return whether this real subset is disjoint from ``other``."""
            ...

        @staticmethod
        @abstract_method
        def are_pairwise_disjoint(real_set_collection: Sequence[RealSubset]) -> bool:
            r"""Return whether the real subsets are pairwise disjoint."""
            ...

        @override
        @abstract_method
        def _an_element_(self) -> SetElement: ...

        @override
        @abstract_method
        def _sympy_(self) -> SympySet: ...

    class ElementMethods: ...
    class MorphismMethods: ...
