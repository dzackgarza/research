r"""One-object subcategory for Sage ``RealSet`` parents."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.category_singleton import Category_singleton
from sage.rings.infinity import infinity, minus_infinity

if TYPE_CHECKING:
    from ...types import FiniteSet, RealInterval, RealNumber, RealSubset


from ...cat import Category
from ...utils import refine_category
from .. import Sets


class _RealSets(Category_singleton):
    r"""Sage real subsets represented as finite unions of real intervals.

    Constructor target:
    named real-subset constructors under ``Sets().Constructors()`` refine here
    and then into the applicable topological subobject categories.

    A RealSet ``X`` carries a canonical basis expression as a finite set of
    disjoint intervals ``{X₁, …, Xₙ}`` with ``X = ∪ᵢ Xᵢ``, exposed via
    ``interval_components()``.  Topological predicates, closure, interior, and
    boundary are subspace operations owned by
    ``TopologicalSpaces().Subobjects()``.  Set operations such as ``union()``
    and ``intersection()`` are owned by ``Sets().Subobjects()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        from ...topological_spaces import TopologicalSpaces

        return [
            Sets().Topological(),
            Sets().Subobjects(),
            TopologicalSpaces().Subobjects(),
        ]

    class ParentMethods:
        @final
        def _as_real_set(self) -> RealSubset:
            from sage.sets.real_set import RealSet as SageRealSet

            assert isinstance(self, SageRealSet), f"expected Sage RealSet, got {self}"
            return self

        @final
        def _is_real_line(self) -> bool:
            X = self._as_real_set()
            if X.n_components() != 1:
                return False
            interval = X.get_interval(0)
            return interval.lower() is minus_infinity and interval.upper() is infinity

        @override
        @final
        def ambient(self) -> RealSubset:
            r"""Return the ambient real line for this real subset."""
            if self._is_real_line():
                return self
            return Sets().Constructors().real_line()

        @final
        def ambient_real_line(self) -> RealSubset:
            r"""Return the ambient real line for this real subset."""
            if self._is_real_line():
                return self
            return Sets().Constructors().real_line()

        @override
        @final
        def is_open(self, U: RealSubset | None = None) -> bool:
            r"""Return whether this real subset, or ``U`` inside it, is open."""
            from sage.sets.real_set import RealSet as SageRealSet

            if U is None:
                return SageRealSet.is_open(self)
            return U.is_subset(self) and SageRealSet.is_open(U)

        @override
        @final
        def is_closed(self, U: RealSubset | None = None) -> bool:
            r"""Return whether this real subset, or ``U`` inside it, is closed."""
            from sage.sets.real_set import RealSet as SageRealSet

            if U is None:
                return SageRealSet.is_closed(self)
            return U.is_subset(self) and SageRealSet.is_closed(U)

        @override
        @final
        def closure(self, U: RealSubset | None = None) -> RealSubset:
            r"""Return closure in the ambient real-line topology."""
            from sage.sets.real_set import RealSet as SageRealSet

            if U is None:
                return refine_category(SageRealSet.closure(self), _RealSets())
            if not U.is_subset(self):
                raise ValueError("closure subset must lie in its ambient real set")
            return refine_category(SageRealSet.closure(U), _RealSets())

        @override
        @final
        def interior(self, U: RealSubset | None = None) -> RealSubset:
            r"""Return interior in the ambient real-line topology."""
            from sage.sets.real_set import RealSet as SageRealSet

            if U is None:
                return refine_category(SageRealSet.interior(self), _RealSets())
            if not U.is_subset(self):
                raise ValueError("interior subset must lie in its ambient real set")
            return refine_category(SageRealSet.interior(U), _RealSets())

        @override
        @final
        def boundary(self, U: RealSubset | None = None) -> RealSubset:
            r"""Return boundary in the ambient real-line topology."""
            from sage.sets.real_set import RealSet as SageRealSet

            if U is None:
                return refine_category(SageRealSet.boundary(self), _RealSets())
            if not U.is_subset(self):
                raise ValueError("boundary subset must lie in its ambient real set")
            return refine_category(SageRealSet.boundary(U), _RealSets())

        @final
        def is_open_subset(self, U: RealSubset) -> bool:
            r"""Return whether ``U`` is open as a subspace of this real subset."""
            return U.is_subset(self) and U.is_open()

        @final
        def is_closed_subset(self, U: RealSubset) -> bool:
            r"""Return whether ``U`` is closed as a subspace of this real subset."""
            return U.is_subset(self) and U.is_closed()

        @final
        def closure_subset(self, U: RealSubset) -> RealSubset:
            r"""Return the closure of ``U`` inside this real subset."""
            from sage.sets.real_set import RealSet as SageRealSet

            if not U.is_subset(self):
                raise ValueError("closure subset must lie in its ambient real set")
            return refine_category(SageRealSet.closure(U), _RealSets())

        @final
        def interior_subset(self, U: RealSubset) -> RealSubset:
            r"""Return the interior of ``U`` inside this real subset."""
            from sage.sets.real_set import RealSet as SageRealSet

            if not U.is_subset(self):
                raise ValueError("interior subset must lie in its ambient real set")
            return refine_category(SageRealSet.interior(U), _RealSets())

        @final
        def boundary_subset(self, U: RealSubset) -> RealSubset:
            r"""Return the boundary of ``U`` inside this real subset."""
            from sage.sets.real_set import RealSet as SageRealSet

            if not U.is_subset(self):
                raise ValueError("boundary subset must lie in its ambient real set")
            return refine_category(SageRealSet.boundary(U), _RealSets())

        @abstractmethod
        def interval_components(self) -> FiniteSet[RealInterval]:
            r"""Return the finite set of disjoint intervals whose union is ``self``."""
            ...

        @abstractmethod
        def inf(self) -> RealNumber:
            r"""Return the infimum of this subset of the real line."""
            ...

        @abstractmethod
        def sup(self) -> RealNumber:
            r"""Return the supremum of this subset of the real line."""
            ...

        @override
        @final
        def is_compact(self) -> bool:
            r"""Return whether this real subset is compact in the real line."""
            return self.is_empty() or (
                self.is_closed()
                and self.inf() is not minus_infinity
                and self.sup() is not infinity
            )

    class ElementMethods: ...
