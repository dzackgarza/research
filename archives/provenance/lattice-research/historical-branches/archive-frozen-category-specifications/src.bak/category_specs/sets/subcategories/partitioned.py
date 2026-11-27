r"""Axiomatic subcategory for partitioned sets and set partitions."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, cast, final, override, TypeAlias

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Sets
from ..homsets import (
    SetAutCategory,
    SetEndCategory,
    SetHomCategory,
)

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        FiniteSet,
        Set,
        SetElement,
        SetPartition,
        Subset,
    )


# ---------------------------------------------------------------------------
# Partitioned axiom --- sets carrying partition data
# ---------------------------------------------------------------------------


class PartitionedSetsCategory(CategoryWithAxiom):
    r"""Sets whose elements are partitioned.

    Canonical chain: ``Sets().Partitioned()``.

    A partitioned set *X* carries a partition of itself, accessible
    via ``partition()``.  The partition object itself lives in the
    :class:`PartitionsCategory` and owns methods such as
    ``crossings()``, ``is_noncrossing()``, and ``refines()``.

    This is an axiom on ``Sets()``, so it composes with other set
    axioms: ``Sets().Finite().TotallyOrdered().Partitioned()``
    describes a finite, totally ordered set that carries a partition.
    """

    _base_category_class_and_axiom = (Sets, "Partitioned")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "partitioned sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return []

    class ParentMethods:
        @final
        def partition(self) -> SetPartition:
            r"""Return the partition of this set."""
            return self.an_element()

    class ElementMethods: ...


# ---------------------------------------------------------------------------
# Partitions subcategory --- sets whose *elements* are partitions
# ---------------------------------------------------------------------------


class PartitionsCategory(Category):
    r"""Sets whose elements are partitions of a fixed base set.

    Canonical construction: ``PartitionsCategory()``.

    This is *not* an axiom --- it is a subcategory of ``Sets()``.
    Objects in this category are the set-of-partitions parents
    such as ``SetPartitions(3)``; their *elements* are individual
    partition objects carrying methods like ``crossings()``,
    ``arcs()``, ``refines()``, and ``ordered_coarsening_closure()``.

    Because the elements are partitions, the parent always knows its
    ``base_set()`` --- the underlying set being partitioned --- which
    may carry its own axioms such as ``TotallyOrdered``.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "sets of partitions of a fixed set"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable(), Sets().Subobjects()]

    class ParentMethods:
        @abstractmethod
        def base_set(self) -> Set:
            r"""Return the base set whose partitions are elements of ``self``."""
            ...

        @abstractmethod
        def base_set_cardinality(self) -> Cardinality:
            r"""Return the cardinality of ``base_set()``."""
            ...

        @abstractmethod
        def is_less_than(self, x: SetPartition, y: SetPartition) -> bool:
            r"""Return whether ``x`` is strictly finer than ``y``."""
            ...

        @override
        @final
        def ambient(self) -> Set:
            r"""Return the powerset-of-powerset ambient set containing ``self``."""
            return self.base_set().subsets().subsets()

        @override
        @abstractmethod
        def _element_constructor_(
            self,
            blocks: Sequence[Sequence[SetElement]],
            check: bool = True,
        ) -> SetPartition:
            r"""Construct the partition with the given blocks."""
            ...

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool:
            r"""Return whether ``x`` is a partition of ``base_set()``."""
            ...

        @override
        @abstractmethod
        def cardinality(self) -> Cardinality:
            r"""Return the number of partitions in ``self``."""
            ...

        @override
        @abstractmethod
        def random_element(self) -> SetPartition:
            r"""Return a random partition in ``self``."""
            ...

        @final
        def has_finite_totally_ordered_base_set(self) -> bool:
            r"""Return whether the base set is finite and totally ordered.

            Returns ``True`` for partitions over a finite totally ordered base
            (integer, iteration, or algebraic set with canonical enumeration).
            """
            return True

    class ElementMethods:
        @abstractmethod
        def __iter__(self) -> Iterator[SetElement]:
            r"""Iterate over the blocks of this partition."""
            ...

        @abstractmethod
        def parent(self) -> PartitionsCategory.ParentMethods:
            r"""Return the fixed-base partition parent of this partition."""
            ...

        @abstractmethod
        def base_set(self) -> Set:
            r"""Return the base set covered by the blocks of this partition."""
            ...

        @abstractmethod
        def base_set_cardinality(self) -> Cardinality:
            r"""Return the cardinality of ``base_set()``."""
            ...

        @final
        def blocks(self) -> Subset:
            r"""Return this partition as a subset of ``P(base_set())``."""
            from sage.sets.set import Set as SageSet

            return cast("Subset", SageSet([SageSet(block) for block in self]))

        @final
        def as_subset_of_powerset(self) -> Subset:
            r"""Return this partition as a subset of ``P(base_set())``."""
            return self.blocks()

        @final
        def meet(self, other: SetPartition) -> SetPartition:
            r"""Return the infimum in the refinement lattice."""
            return self * other

        @final
        def join(self, other: SetPartition) -> SetPartition:
            r"""Return the supremum in the refinement lattice."""
            return self.sup(other)

        @abstractmethod
        def sup(self, other: SetPartition) -> SetPartition:
            r"""Return Sage's supremum operation for set partitions."""
            ...

        @final
        def refines(self, other: SetPartition) -> bool:
            r"""Return whether ``self`` refines ``other``."""
            return cast(bool, self == other or self.parent().is_less_than(self, other))

        @final
        def strictly_refines(self, other: SetPartition) -> bool:
            r"""Return whether ``self`` is strictly finer than ``other``."""
            return self.parent().is_less_than(self, other)

        @final
        def refinement_set(self) -> FiniteSet:
            r"""Return the finite set of partition refinements, including ``self``."""
            return Sets().Constructors().Set(elements=self.refinements())

        @final
        def coarsening_set(self) -> FiniteSet:
            r"""Return the finite set of partition coarsenings, including ``self``."""
            return Sets().Constructors().Set(elements=self.coarsenings())

        @abstractmethod
        def refinements(self) -> list[SetPartition]:
            r"""Return Sage's list of refinements, including ``self``."""
            ...

        @abstractmethod
        def coarsenings(self) -> list[SetPartition]:
            r"""Return Sage's list of coarsenings, including ``self``."""
            ...

        @abstractmethod
        def standard_form(self) -> list[list[SetElement]]:
            r"""Return the blocks as sorted lists when the base set is ordered."""
            ...

        @abstractmethod
        def arcs(self) -> list[tuple[SetElement, SetElement]]:
            r"""Return the arcs between consecutive elements in each ordered block."""
            ...

        @abstractmethod
        def crossings(
            self,
        ) -> list[
            tuple[
                tuple[SetElement, SetElement],
                tuple[SetElement, SetElement],
            ]
        ]:
            r"""Return crossing arc pairs.

            The base set is assumed finite and totally ordered.
            """
            ...

        @abstractmethod
        def nestings(
            self,
        ) -> list[
            tuple[
                tuple[SetElement, SetElement],
                tuple[SetElement, SetElement],
            ]
        ]:
            r"""Return nesting arc pairs when the finite base set is totally ordered."""
            ...

        @abstractmethod
        def is_noncrossing(self) -> bool:
            r"""Return whether the ordered finite partition has no crossing arcs."""
            ...

        @abstractmethod
        def is_nonnesting(self) -> bool:
            r"""Return whether the ordered finite partition has no nesting arcs."""
            ...

        @abstractmethod
        def is_atomic(self) -> bool:
            r"""Return whether the partition is pipe-indecomposable.

            The partition is assumed nonempty, ordered, and finite.
            """
            ...

        @final
        def ordered_coarsening_closure(self) -> FiniteSet:
            r"""Return Sage's ordered coarsening closure, including ``self``."""
            return Sets().Constructors().Set(elements=self.strict_coarsenings())

        @abstractmethod
        def strict_coarsenings(self) -> list[SetPartition]:
            r"""Return Sage's ordered coarsening closure list, including ``self``."""
            ...


# ---------------------------------------------------------------------------
# TotallyOrdered axiom
# ---------------------------------------------------------------------------


class TotallyOrderedSetsCategory(CategoryWithAxiom):
    r"""Sets whose elements are finite and totally ordered.

    Canonical chain: ``Sets().Finite().TotallyOrdered()``.
    """

    _base_category_class_and_axiom = (Sets, "TotallyOrdered")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "totally ordered sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return []

    class ParentMethods: ...

    class ElementMethods: ...


# ---------------------------------------------------------------------------
# Type aliases
# ---------------------------------------------------------------------------

PartitionedSetsObject : TypeAlias = PartitionedSetsCategory.ParentMethods
PartitionedSetsElement : TypeAlias = PartitionedSetsCategory.ElementMethods
PartitionedSetsMorphism : TypeAlias = SetHomCategory.ElementMethods
PartitionedSetsHomCategory : TypeAlias = SetHomCategory
PartitionedSetsEndCategory : TypeAlias = SetEndCategory
PartitionedSetsAutCategory : TypeAlias = SetAutCategory
PartitionedSetsHom : TypeAlias = SetHomCategory.ParentMethods
PartitionedSetsEnd : TypeAlias = SetEndCategory.ParentMethods
PartitionedSetsAut : TypeAlias = SetAutCategory.ParentMethods
PartitionedSetsEndomorphism : TypeAlias = SetEndCategory.ElementMethods
PartitionedSetsAutomorphism : TypeAlias = SetAutCategory.ElementMethods

PartitionsObject : TypeAlias = PartitionsCategory.ParentMethods
PartitionsElement : TypeAlias = PartitionsCategory.ElementMethods
PartitionsMorphism : TypeAlias = SetHomCategory.ElementMethods
