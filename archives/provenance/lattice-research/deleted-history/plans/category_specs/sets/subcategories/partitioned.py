r"""Axiomatic subcategory for finite set partitions."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Sets
from ..homsets import SetAutCategory, SetEndCategory, SetHomCategory

if TYPE_CHECKING:
    from ...types import Cardinality, Set, SetElement, SetPartition, Subset


class PartitionedSetsCategory(CategoryWithAxiom):
    r"""Sets whose elements are partitions of a fixed base set.

    Canonical chain: ``Sets().Partitioned()``.

    A partition of ``X`` is a subset of the powerset ``P(X)`` whose blocks are
    nonempty, pairwise disjoint, and cover ``X``.  Sage represents the parent of
    such partitions as ``SetPartitions(X)`` and each partition as a
    ``SetPartition`` element.
    """

    _base_category_class_and_axiom = (Sets, "Partitioned")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "sets of partitions of a fixed set"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable(), Sets().Subobjects()]

    class ParentMethods:
        @abstract_method
        def base_set(self) -> Set:
            r"""Return the base set whose partitions are elements of ``self``."""
            ...

        @abstract_method
        def base_set_cardinality(self) -> Cardinality:
            r"""Return the cardinality of ``base_set()``."""
            ...

        @override
        @final
        def ambient(self) -> Set:
            r"""Return the powerset-of-powerset ambient set containing ``self``."""
            return self.base_set().subsets().subsets()

        @override
        @abstract_method
        def _element_constructor_(
            self,
            blocks: Sequence[Sequence[SetElement]],
            check: bool = True,
        ) -> SetPartition:
            r"""Construct the partition with the given blocks."""
            ...

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool:
            r"""Return whether ``x`` is a partition of ``base_set()``."""
            ...

        @override
        @abstract_method
        def cardinality(self) -> Cardinality:
            r"""Return the number of partitions in ``self``."""
            ...

        @override
        @abstract_method
        def random_element(self) -> SetPartition:
            r"""Return a random partition in ``self``."""
            ...

    class ElementMethods:
        @abstract_method
        def base_set(self) -> Set:
            r"""Return the base set covered by the blocks of this partition."""
            ...

        @abstract_method
        def base_set_cardinality(self) -> Cardinality:
            r"""Return the cardinality of ``base_set()``."""
            ...

        @final
        def blocks(self) -> Subset:
            r"""Return this partition as a subset of ``P(base_set())``."""
            from sage.sets.set import Set as SageSet

            return SageSet(self)

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

        @final
        def refines(self, other: SetPartition) -> bool:
            r"""Return whether ``self`` refines ``other``."""
            return self == other or self.parent().is_less_than(self, other)

        @final
        def strictly_refines(self, other: SetPartition) -> bool:
            r"""Return whether ``self`` is strictly finer than ``other``."""
            return self.parent().is_less_than(self, other)

        @abstract_method
        def standard_form(self) -> list[list[SetElement]]:
            r"""Return the blocks as sorted lists when the base set is ordered."""
            ...

        @abstract_method
        def arcs(self) -> list[tuple[SetElement, SetElement]]:
            r"""Return the arcs between consecutive elements in each ordered block."""
            ...

    class MorphismMethods: ...


PartitionedSetsObject = PartitionedSetsCategory.ParentMethods
PartitionedSetsElement = PartitionedSetsCategory.ElementMethods
PartitionedSetsMorphism = PartitionedSetsCategory.MorphismMethods
PartitionedSetsHomCategory = SetHomCategory
PartitionedSetsEndCategory = SetEndCategory
PartitionedSetsAutCategory = SetAutCategory
PartitionedSetsHom = SetHomCategory.ParentMethods
PartitionedSetsEnd = SetEndCategory.ParentMethods
PartitionedSetsAut = SetAutCategory.ParentMethods
PartitionedSetsEndomorphism = SetEndCategory.ElementMethods
PartitionedSetsAutomorphism = SetAutCategory.ElementMethods
