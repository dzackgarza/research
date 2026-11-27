r"""Set category surface for the category spec redesign.

This module defines ``Sets()`` as a staged, non-destructive replacement for
Sage's ``Sets()``. It is the public API document for the set subtree: category
navigation, method surfaces, constructions, and constructor entry points live here.

Naming convention:
    Sets()      -- project category
    SageSets()  -- sage.categories.sets_cat.Sets()

Subcategory hierarchy::

    Sets()
    |-- Finite()
    |-- Infinite()
    |-- Countable()
    |   |-- Finite()
    |   `-- Infinite()
    |-- Uncountable()
    |-- Facade()
    |-- Topological()
    |   `-- Metric()
    |-- TotallyOrdered()
    |-- Graded()
    |-- Partitioned()
    |-- GSets(G)
    |-- CartesianProducts()
    |-- Subquotients()
    |-- Subobjects() / Subsets()
    |-- Quotients()
    |-- IsomorphicObjects()
    |-- WithRealizations()
    |-- Realizations()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()

One-object constructor refinements::

    FiniteEnumeratedSetObjects
    IntegerRangeSets
    NonNegativeIntegersSets
    PositiveIntegersSets
    PrimesSets
    RealSets
    RecursivelyEnumeratedSets
    DisjointUnionEnumeratedSets
    CartesianProductSets
    ImageSets
    TotallyOrderedFiniteSets
    FiniteSetMapsSets
    FamilySets
    EnumeratedSetsFromIterator

Constructor entry points live under ``Sets().Constructors()`` and call Sage's
canonical constructors before refining the result into this hierarchy.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.infinity import infinity

from ..cat import Cat, Category, Category_singleton
from ..utils import refine_category
from .homsets import SetAutCategory, SetEndCategory, SetHomCategory

if TYPE_CHECKING:
    from ..types import (
        Algebra,
        Cardinality,
        CountableSet,
        FiniteSet,
        Group,
        InfinityElement,
        Integer,
        IntegerPartition,
        RealInterval,
        RealNumber,
        RealOpenSet,
        RealSubset,
        Ring,
        RModule,
        Set,
        SetAut,
        SetElement,
        SetEnd,
        SetFamily,
        SetHom,
        SetMorphism,
        SetPartition,
        SetPartitionSet,
        Subset,
        SympySet,
    )


# ---------------------------------------------------------------------------
# Method surfaces for the root category
# ---------------------------------------------------------------------------


class _SetObjectMethods:
    r"""Methods on objects of the root category ``Sets()``."""

    @override
    @abstract_method
    def __contains__(self, x: Any) -> bool:
        r"""Return ``True`` if ``x`` is an element of ``self``."""
        ...

    @abstract_method
    def _element_constructor_(self, x: SetElement) -> SetElement: ...

    @abstract_method
    def is_parent_of(self, element: SetElement) -> bool:
        r"""Return whether this set is the parent of ``element``."""
        ...

    @abstract_method
    def an_element(self) -> SetElement:
        r"""Return a distinguished element of this set."""
        ...

    @abstract_method
    def some_elements(self) -> list[SetElement]:
        r"""Return sample elements of this set."""
        ...

    @abstract_method
    def cardinality(self) -> Cardinality:
        r"""Return the cardinality of this set."""
        ...

    @abstract_method
    def is_empty(self) -> bool:
        r"""Return whether this set has no elements."""
        ...

    @abstract_method
    def is_finite(self) -> bool:
        r"""Return whether this set has finite cardinality."""
        ...

    @abstract_method
    def construction(self):
        r"""Return Sage construction data for this set, when it has one."""
        ...

    @abstract_method
    def cartesian_product(
        self,
        factors: Sequence[Set],
        *,
        category: Category | None = None,
        extra_category: Category | None = None,
        flatten: bool = False,
    ) -> Set:
        r"""Return the Cartesian product of ``self`` with the parent sets in ``factors``."""
        ...

    @abstract_method
    def union(self, other: Set) -> Set:
        r"""Return the set-theoretic union of ``self`` and ``other``."""
        ...

    @final
    def __or__(self, other: Set) -> Set:
        return self.union(other)

    @final
    def __add__(self, other: Set) -> Set:
        return self.union(other)

    @abstract_method
    def is_subset(self, other: Set) -> bool:
        r"""Return whether ``self`` is a subset of ``other``."""
        ...

    @override
    @final
    def is_proper_subset(self, other: Set) -> bool:
        r"""Return whether ``self`` is a proper subset of ``other``."""
        return self.is_subset(other) and not other.is_subset(self)

    @override
    @final
    def is_superset(self, other: Set) -> bool:
        r"""Return whether ``self`` contains ``other`` as a subset."""
        return other.is_subset(self)

    @override
    @final
    def is_proper_superset(self, other: Set) -> bool:
        r"""Return whether ``self`` properly contains ``other``."""
        return other.is_proper_subset(self)

    @abstract_method
    def __richcmp__(self, other: Set, op: Integer) -> bool:
        r"""Compare sets using equality and subset/proper-subset relations."""
        ...

    @final
    def __le__(self, other: Set) -> bool:
        return self.is_subset(other)

    @final
    def __lt__(self, other: Set) -> bool:
        return self.is_proper_subset(other)

    @final
    def __ge__(self, other: Set) -> bool:
        return self.is_superset(other)

    @final
    def __gt__(self, other: Set) -> bool:
        return self.is_proper_superset(other)

    @abstract_method
    def subsets(self, size: Integer | None = None) -> Set:
        r"""Return the set of subsets, optionally with fixed cardinality ``size``."""
        ...

    @abstract_method
    def subsets_lattice(self) -> Set:
        r"""Return the lattice of subsets ordered by inclusion."""
        ...

    @final
    def free_module(self, base_ring: Ring) -> RModule:
        r"""Return the free ``base_ring``-module with basis indexed by this set."""
        from ..modules import Modules

        return Modules(base_ring).Constructors().CombinatorialFreeModule(basis_keys=self)

    @final
    def free_algebra(self, base_ring: Ring) -> Algebra:
        r"""Return the free ``base_ring``-algebra on this set of generators."""
        from ..algebras import Algebras

        return Algebras(base_ring).Constructors().free_algebra_from_set(self)

    @abstract_method
    def _sympy_(self) -> SympySet: ...


class _SetElementMethods:
    r"""Methods on elements of objects in ``Sets()``."""

    @abstract_method
    def __eq__(self, other: SetElement) -> bool: ...

    @abstract_method
    def __hash__(self) -> Integer: ...

    @abstract_method
    def cartesian_product(self, elements: Sequence[SetElement]) -> SetElement:
        r"""Return the Cartesian product element with these coordinates."""
        ...


# ---------------------------------------------------------------------------
# Sets -- the root category
# ---------------------------------------------------------------------------


class Sets(Category_singleton):
    r"""Replacement set category, staged below Sage's existing ``Sets()``.

    Canonical chain: ``Sets()``.

    Objects in ``Sets()`` are any Sage parents that lie in ``SageSets()``.
    The module docstring records the full public category hierarchy and constructor
    refinement map.
    """

    @override
    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageSets(),)

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return Sage's set category refined by this spec."""
        return [SageSets()]

    @override
    @final
    def additional_structure(self):
        r"""Return Sage's additional-structure marker for plain sets."""
        return None

    # ------------------------------------------------------------------
    # SubcategoryMethods -- available on every subcategory of Sets()
    # ------------------------------------------------------------------

    class SubcategoryMethods:
        @cached_method
        @final
        def Finite(self) -> Category:
            r"""Return the finite-set subcategory of this set category."""
            return self._with_axiom("Finite")

        @cached_method
        @final
        def Infinite(self) -> Category:
            r"""Return the infinite-set subcategory of this set category."""
            return self._with_axiom("Infinite")

        @cached_method
        @final
        def Countable(self) -> Category:
            r"""Return the countable-set subcategory of this set category."""
            return self._with_axiom("Countable")

        @cached_method
        @final
        def Uncountable(self) -> Category:
            r"""Return the uncountable-set subcategory of this set category."""
            return self._with_axiom("Uncountable")

        @cached_method
        @final
        def Facade(self) -> Category:
            r"""Return the facade-set subcategory of this set category."""
            return self._with_axiom("Facade")

        @cached_method
        @final
        def Topological(self) -> Category:
            r"""Return the topological-set subcategory of this set category."""
            return self._with_axiom("Topological")

        @cached_method
        @final
        def Metric(self) -> Category:
            r"""Return the metric-set subcategory of this set category."""
            return self._with_axiom("Metric")

        @cached_method
        @final
        def TotallyOrdered(self) -> Category:
            r"""Return the totally ordered set subcategory of this set category."""
            return self._with_axiom("TotallyOrdered")

        @cached_method
        @final
        def Graded(self) -> Category:
            r"""Return the graded-set subcategory of this set category."""
            return self._with_axiom("Graded")

        @cached_method
        @final
        def Partitioned(self) -> Category:
            r"""Return the partitioned-set subcategory of this set category."""
            return self._with_axiom("Partitioned")

        @cached_method
        @final
        def GSets(self, acting_group: Group) -> Category:
            r"""Return the category of sets with an action by ``acting_group``."""
            from .subcategories.group_actions import _GSets

            return _GSets(acting_group, self)

        @cached_method
        @final
        def IsomorphicObjects(self) -> Category:
            r"""Return the category of set objects presented by isomorphic models."""
            from .subcategories.constructions.isomorphic_objects import _IsomorphicObjects

            return _IsomorphicObjects.category_of(self)

        @cached_method
        @final
        def WithRealizations(self) -> Category:
            r"""Return the category of sets equipped with named realizations."""
            from .subcategories.constructions.with_realizations import SetsWithRealizations

            return SetsWithRealizations.category_of(self)

        @cached_method
        @final
        def Realizations(self) -> Category:
            r"""Return the category of realizations of objects in this set category."""
            from .subcategories.constructions.realizations import _Realizations

            return _Realizations.category_of(self)

    # ------------------------------------------------------------------
    # Constructors -- named Sage set entry points
    # ------------------------------------------------------------------

    class Constructors:
        r"""Named Sage set constructor entry points.

        Every method calls the canonical Sage constructor, then refines
        the resulting parent into ``Sets()`` and the most specific
        one-object subcategory.

        Usage::

            Sets().Constructors().Primes()
            Sets().Constructors().FiniteEnumeratedSet([1, 2, 3])
            Sets().Constructors().IntegerRange(2, 100, 5)
        """

        @final
        def __init__(self, category: Sets) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return "Sets constructors"

        @final
        def from_iterable(self, elements: Iterable[SetElement]) -> FiniteSet:
            r"""Return the finite enumerated set whose elements are read from ``elements``."""
            return self.FiniteEnumeratedSet(elements)

        @final
        def FiniteEnumeratedSet(self, elements: Iterable[SetElement]) -> FiniteSet:
            r"""Return ``FiniteEnumeratedSet(elements)``, refined into its subcategory."""
            from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as SageFES

            from .subcategories.finite_enumerated_set import _FiniteEnumeratedSetObjects

            return refine_category(SageFES(elements), [Sets(), _FiniteEnumeratedSetObjects()])

        @final
        def IntegerRange(
            self,
            begin: Integer | InfinityElement,
            end: Integer | InfinityElement | None = None,
            step: Integer = 1,
            middle_point: Integer | None = None,
        ) -> CountableSet:
            r"""Return the integer arithmetic progression determined by the bounds."""
            from sage.sets.integer_range import IntegerRange as SageIR

            from .subcategories.integer_range import _IntegerRangeSets

            return refine_category(SageIR(begin, end, step, middle_point), [Sets(), _IntegerRangeSets()])

        @final
        def NonNegativeIntegers(self) -> CountableSet:
            r"""Return ``NonNegativeIntegers()``, refined into its subcategory."""
            from sage.sets.non_negative_integers import NonNegativeIntegers as SageNN

            from .subcategories.non_negative_integers import _NonNegativeIntegersSets

            return refine_category(SageNN(), [Sets(), _NonNegativeIntegersSets()])

        @final
        def PositiveIntegers(self) -> CountableSet:
            r"""Return ``PositiveIntegers()``, refined into its subcategory."""
            from sage.sets.positive_integers import PositiveIntegers as SagePP

            from .subcategories.positive_integers import _PositiveIntegersSets

            return refine_category(SagePP(), [Sets(), _PositiveIntegersSets()])

        @final
        def Primes(self, proof: bool = True) -> CountableSet:
            r"""Return the full Sage set of prime integers."""
            from sage.sets.primes import Primes as SagePrimes

            from .subcategories.primes import _PrimesSets

            return refine_category(SagePrimes(proof), [Sets(), _PrimesSets()])

        @final
        def _real_subset_categories(self, real_set: RealSubset) -> list[Category]:
            r"""Return the project categories satisfied by a Sage real subset."""
            from sage.categories.topological_spaces import TopologicalSpaces as SageTopologicalSpaces

            from ..topological_spaces import TopologicalSpaces
            from .subcategories.real_set import _RealSets

            categories = [
                Sets(),
                Sets().Subobjects(),
                Sets().Topological(),
                _RealSets(),
                TopologicalSpaces().Subobjects(),
            ]
            if real_set.is_connected():
                categories.append(TopologicalSpaces().Connected())
            if real_set.category().is_subcategory(SageTopologicalSpaces().Compact()):
                categories.append(TopologicalSpaces().Compact())
            return categories

        @final
        def _refine_real_subset(self, real_set: RealSubset) -> RealSubset:
            r"""Refine a Sage real subset into the local set/topological hierarchy."""
            return refine_category(real_set, self._real_subset_categories(real_set))

        @final
        def RR(self) -> Set:
            r"""Return Sage ``RR`` refined as a topological set object."""
            from sage.rings.real_mpfr import RealField

            return refine_category(RealField(), [Sets(), Sets().Topological()])

        @final
        def RealSet(self, intervals: Sequence[RealInterval], *, normalized: bool = False) -> RealSubset:
            r"""Return a real subset represented as a finite union of real intervals."""
            from sage.sets.real_set import RealSet as SageRealSet

            return self._refine_real_subset(SageRealSet(*tuple(intervals), normalized=normalized))

        @final
        def RealSetInterval(
            self,
            lower: RealNumber | InfinityElement,
            upper: RealNumber | InfinityElement,
            *,
            lower_closed: bool,
            upper_closed: bool,
            normalized: bool = True,
        ) -> RealSubset:
            r"""Return ``RealSet.interval(lower, upper, ...)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            S = SageRealSet.interval(
                lower,
                upper,
                lower_closed=lower_closed,
                upper_closed=upper_closed,
                normalized=normalized,
            )
            return self._refine_real_subset(S)

        @final
        def OpenRealInterval(self, lower: RealNumber, upper: RealNumber, *, normalized: bool = True) -> RealOpenSet:
            r"""Return ``RealSet.open(lower, upper)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=False,
                upper_closed=False,
                normalized=normalized,
            )

        @final
        def ClosedRealInterval(self, lower: RealNumber, upper: RealNumber, *, normalized: bool = True) -> RealSubset:
            r"""Return ``RealSet.closed(lower, upper)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=True,
                upper_closed=True,
                normalized=normalized,
            )

        @final
        def RealPoint(self, point: RealNumber, *, normalized: bool = True) -> RealSubset:
            r"""Return ``RealSet.point(point)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                point,
                point,
                lower_closed=True,
                upper_closed=True,
                normalized=normalized,
            )

        @final
        def OpenClosedRealInterval(
            self,
            lower: RealNumber,
            upper: RealNumber,
            *,
            normalized: bool = True,
        ) -> RealSubset:
            r"""Return ``RealSet.open_closed(lower, upper)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=False,
                upper_closed=True,
                normalized=normalized,
            )

        @final
        def ClosedOpenRealInterval(
            self,
            lower: RealNumber,
            upper: RealNumber,
            *,
            normalized: bool = True,
        ) -> RealSubset:
            r"""Return ``RealSet.closed_open(lower, upper)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=True,
                upper_closed=False,
                normalized=normalized,
            )

        @final
        def UnboundedBelowClosedRealInterval(self, bound: RealNumber, *, normalized: bool = True) -> RealSubset:
            r"""Return ``RealSet.unbounded_below_closed(bound)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                -infinity,
                bound,
                lower_closed=False,
                upper_closed=True,
                normalized=normalized,
            )

        @final
        def UnboundedBelowOpenRealInterval(self, bound: RealNumber, *, normalized: bool = True) -> RealOpenSet:
            r"""Return ``RealSet.unbounded_below_open(bound)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                -infinity,
                bound,
                lower_closed=False,
                upper_closed=False,
                normalized=normalized,
            )

        @final
        def UnboundedAboveClosedRealInterval(self, bound: RealNumber, *, normalized: bool = True) -> RealSubset:
            r"""Return ``RealSet.unbounded_above_closed(bound)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                bound,
                infinity,
                lower_closed=True,
                upper_closed=False,
                normalized=normalized,
            )

        @final
        def UnboundedAboveOpenRealInterval(self, bound: RealNumber, *, normalized: bool = True) -> RealOpenSet:
            r"""Return ``RealSet.unbounded_above_open(bound)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                bound,
                infinity,
                lower_closed=False,
                upper_closed=False,
                normalized=normalized,
            )

        @final
        def RealLine(self, *, normalized: bool = True) -> RealSubset:
            r"""Return ``RealSet.real_line()``, refined into ``RealSets``."""
            return self.RealSetInterval(
                -infinity,
                infinity,
                lower_closed=False,
                upper_closed=False,
                normalized=normalized,
            )

        @final
        def RecursivelyEnumeratedSet(
            self,
            seeds: Iterable[SetElement],
            successors: Callable[[SetElement], Iterable[SetElement]],
            *,
            enumeration: str = "depth",
            max_depth: Integer | InfinityElement = infinity,
            post_process: Callable[[SetElement], SetElement] | None = None,
            facade: bool | None = None,
            category: Category | None = None,
        ) -> CountableSet:
            r"""Return a ``RecursivelyEnumeratedSet``, refined into its subcategory."""
            from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as SageRES

            from .subcategories.recursively_enumerated import _RecursivelyEnumeratedSets

            S = SageRES(
                seeds,
                successors,
                enumeration=enumeration,
                max_depth=max_depth,
                post_process=post_process,
                facade=facade,
                category=category,
            )
            return refine_category(S, [Sets(), _RecursivelyEnumeratedSets()])

        @final
        def DisjointUnionEnumeratedSets(
            self,
            family: SetFamily | Iterable[Set],
            *,
            facade: bool = True,
            keepkey: bool = False,
            category: Category | None = None,
        ) -> CountableSet:
            r"""Return a ``DisjointUnionEnumeratedSets``, refined into its subcategory."""
            from sage.sets.disjoint_union_enumerated_sets import (
                DisjointUnionEnumeratedSets as SageDUES,
            )

            from .subcategories.disjoint_union import _DisjointUnionEnumeratedSets

            S = SageDUES(family, facade=facade, keepkey=keepkey, category=category)
            return refine_category(S, [Sets(), _DisjointUnionEnumeratedSets()])

        @final
        def CartesianProduct(
            self,
            factors: Sequence[Set],
            *,
            category: Category | None = None,
            flatten: bool = False,
        ) -> Set:
            r"""Return the Cartesian product of a sequence of set parents."""
            from sage.sets.cartesian_product import CartesianProduct as SageCP

            from .subcategories.cartesian_product import _CartesianProductSets

            product_category = Sets().CartesianProducts() if category is None else category
            S = SageCP(tuple(factors), category=product_category, flatten=flatten)
            return refine_category(S, [Sets(), _CartesianProductSets()])

        @final
        def ImageSubobject(
            self,
            f: SetMorphism,
            domain_subset: Subset,
            *,
            category: Category | None = None,
            is_injective: bool | None = None,
            inverse: SetMorphism | None = None,
        ) -> Subset:
            r"""Return ``ImageSubobject(f, domain_subset)``, refined into its subcategory."""
            from sage.sets.image_set import ImageSubobject as SageIS

            from .subcategories.image import _ImageSets

            return refine_category(
                SageIS(f, domain_subset, category=category, is_injective=is_injective, inverse=inverse),
                [Sets(), _ImageSets()],
            )

        @final
        def TotallyOrderedFiniteSet(self, elements: Iterable[SetElement], *, facade: bool = True) -> FiniteSet:
            r"""Return a ``TotallyOrderedFiniteSet``, refined into its subcategory."""
            from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet as SageTOFS

            from .subcategories.totally_ordered_finite import _TotallyOrderedFiniteSets

            S = SageTOFS(elements, facade=facade)
            return refine_category(S, [Sets(), _TotallyOrderedFiniteSets()])

        @final
        def FiniteSetMaps(
            self,
            domain: FiniteSet | Integer,
            codomain: FiniteSet | Integer | None = None,
            *,
            action: str = "left",
            category: Category | None = None,
        ) -> FiniteSet:
            r"""Return the finite set of all functions ``domain -> codomain``.

            With only ``domain`` specified, Sage constructs the endomap set
            ``Map(domain, domain)``, whose elements form a finite monoid under
            composition.
            """
            from sage.sets.finite_set_maps import FiniteSetMaps as SageFSM

            from .subcategories.finite_set_maps import _FiniteSetMapsSets

            if codomain is None:
                S = SageFSM(domain, action=action, category=category)
            else:
                S = SageFSM(domain, codomain, action=action, category=category)
            return refine_category(S, [Sets(), _FiniteSetMapsSets()])

        @final
        def Family(
            self,
            indices: Iterable[SetElement] | Set,
            function: Callable[[SetElement], SetElement] | None = None,
            *,
            hidden_keys: Sequence[SetElement] = (),
            hidden_function: Callable[[SetElement], SetElement] | None = None,
            lazy: bool = False,
            name: str | None = None,
        ) -> SetFamily:
            r"""Return a ``Family``, refined into its subcategory."""
            from sage.sets.family import Family as SageFamily

            from .subcategories.family import _FamilySets

            S = SageFamily(
                indices,
                function,
                hidden_keys=list(hidden_keys),
                hidden_function=hidden_function,
                lazy=lazy,
                name=name,
            )
            return refine_category(S, [Sets(), _FamilySets()])

        @final
        def EnumeratedSetFromIterator(
            self,
            iterator_factory: Callable[[], Iterable[SetElement]],
            *,
            name: str | None = None,
            category: Category | None = None,
            cache: bool = False,
        ) -> CountableSet:
            r"""Return a callable-backed enumerated set from a nullary iterator factory."""
            from sage.sets.set_from_iterator import EnumeratedSetFromIterator as SageESFI

            from .subcategories.enumerated_from_iterator import _EnumeratedSetsFromIterator

            return refine_category(
                SageESFI(iterator_factory, name=name, category=category, cache=cache),
                [Sets(), _EnumeratedSetsFromIterator()],
            )

        @final
        def AllSetPartitions(self) -> CountableSet:
            r"""Return Sage's countable set of all finite set partitions."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return refine_category(SageSetPartitions(), [Sets(), Sets().Countable()])

        @final
        def SetPartitions(self, base_set: Set | Iterable[SetElement] | Integer) -> SetPartitionSet:
            r"""Return the set of all partitions of ``base_set``."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            from .subcategories.partitioned import PartitionedSetsCategory

            return refine_category(SageSetPartitions(base_set), [Sets(), PartitionedSetsCategory()])

        @final
        def SetPartitionsWithBlockCount(
            self,
            base_set: Set | Iterable[SetElement] | Integer,
            block_count: Integer,
        ) -> SetPartitionSet:
            r"""Return partitions of ``base_set`` into ``block_count`` blocks."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            from .subcategories.partitioned import PartitionedSetsCategory

            return refine_category(SageSetPartitions(base_set, block_count), [Sets(), PartitionedSetsCategory()])

        @final
        def SetPartitionsWithBlockSizes(
            self,
            base_set: Set | Iterable[SetElement] | Integer,
            block_sizes: IntegerPartition | Sequence[Integer],
        ) -> SetPartitionSet:
            r"""Return partitions of ``base_set`` with the given block-size partition."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            from .subcategories.partitioned import PartitionedSetsCategory

            return refine_category(SageSetPartitions(base_set, block_sizes), [Sets(), PartitionedSetsCategory()])

        @final
        def SetPartition(
            self,
            blocks: Iterable[Iterable[SetElement]],
            *,
            check: bool = True,
        ) -> SetPartition:
            r"""Return the partition whose blocks are ``blocks``."""
            from sage.combinat.set_partition import SetPartition as SageSetPartition

            return SageSetPartition(blocks, check=check)

        @final
        def SetPartitionFromRestrictedGrowthWordBlocks(self, word: Sequence[Integer]) -> SetPartition:
            r"""Return the set partition encoded by ``word`` using the block convention."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return SageSetPartitions().from_restricted_growth_word_blocks(word)

        @final
        def SetPartitionFromRestrictedGrowthWordIntertwining(self, word: Sequence[Integer]) -> SetPartition:
            r"""Return the set partition encoded by ``word`` using the intertwining convention."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return SageSetPartitions().from_restricted_growth_word_intertwining(word)

        @final
        def SetPartitionFromArcs(
            self,
            arcs: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartition:
            r"""Return the coarsest partition of ``{1, ..., n}`` containing ``arcs``."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return SageSetPartitions().from_arcs(arcs, base_set_cardinality)

        @final
        def SetPartitionFromRookPlacementArcs(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer | None = None,
        ) -> SetPartition:
            r"""Return the set partition encoded by a rook placement through arcs."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return SageSetPartitions().from_rook_placement(rooks, "arcs", base_set_cardinality)

        @final
        def SetPartitionFromRookPlacementGamma(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartition:
            r"""Return the set partition encoded by the Wachs-White gamma bijection."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return SageSetPartitions().from_rook_placement_gamma(rooks, base_set_cardinality)

        @final
        def SetPartitionFromRookPlacementRho(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartition:
            r"""Return the set partition encoded by the Wachs-White rho bijection."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return SageSetPartitions().from_rook_placement_rho(rooks, base_set_cardinality)

        @final
        def SetPartitionFromRookPlacementPsi(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartition:
            r"""Return the set partition encoded by Yip's psi bijection."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return SageSetPartitions().from_rook_placement_psi(rooks, base_set_cardinality)

        @final
        def cartesian_product(self, factors: Sequence[Set]) -> Set:
            r"""Return Sage's categorical Cartesian product of ``factors``."""
            from sage.categories.cartesian_product import cartesian_product

            from .subcategories.cartesian_product import _CartesianProductSets

            return refine_category(cartesian_product(list(factors)), [Sets(), _CartesianProductSets()])

    _Constructors = Constructors

    @cached_method
    @final
    def Constructors(self):
        r"""Return the named Sage set constructor collector."""
        return self.__class__._Constructors(self)

    HomCategory = SetHomCategory

    # ------------------------------------------------------------------
    # Axiomatic subcategories and construction categories
    # ------------------------------------------------------------------

    Finite = LazyImport("category_specs.sets.subcategories.finite", "_FiniteSets")
    Infinite = LazyImport("category_specs.sets.subcategories.infinite", "_InfiniteSets")
    Countable = LazyImport("category_specs.sets.subcategories.countable", "_CountableSets")
    Uncountable = LazyImport("category_specs.sets.subcategories.uncountable", "_UncountableSets")
    Facade = LazyImport("category_specs.sets.subcategories.facade", "_FacadeSets")
    Topological = LazyImport("category_specs.topological_spaces", "TopologicalSpaces")
    TotallyOrdered = LazyImport("category_specs.sets.subcategories.totally_ordered", "_TotallyOrdered")
    Graded = LazyImport("category_specs.sets.subcategories.graded", "GradedSetsCategory")
    Partitioned = LazyImport("category_specs.sets.subcategories.partitioned", "PartitionedSetsCategory")
    Metric = LazyImport("category_specs.topological_spaces", "MetricSpacesCategory")
    Subquotients = LazyImport("category_specs.sets.subcategories.constructions.subquotients", "_Subquotients")
    Subobjects = LazyImport("category_specs.sets.subcategories.constructions.subobjects", "Subsets")
    ObjectsOver = LazyImport("category_specs.sets.subcategories.constructions.objects_over", "_ObjectsOver")
    ObjectsUnder = LazyImport("category_specs.sets.subcategories.constructions.objects_under", "_ObjectsUnder")
    CartesianProducts = LazyImport("category_specs.sets.subcategories.constructions.cartesian_products", "_CartesianProducts")
    Subsets = Subobjects
    Quotients = LazyImport("category_specs.sets.subcategories.constructions.quotients", "_Quotients")
    IsomorphicObjects = LazyImport(
        "category_specs.sets.subcategories.constructions.isomorphic_objects",
        "_IsomorphicObjects",
    )
    WithRealizations = LazyImport(
        "category_specs.sets.subcategories.constructions.with_realizations",
        "SetsWithRealizations",
    )
    Realizations = LazyImport(
        "category_specs.sets.subcategories.constructions.realizations",
        "_Realizations",
    )

    ParentMethods = _SetObjectMethods
    ElementMethods = _SetElementMethods
    MorphismMethods = SetHomCategory.ElementMethods


SetsCategory = Sets
SetsObject = Sets.ParentMethods
SetsElement = Sets.ElementMethods
SetsMorphism = Sets.MorphismMethods
SetsHomCategory = SetHomCategory
SetsEndCategory = SetEndCategory
SetsAutCategory = SetAutCategory
SetsHom = SetHomCategory.ParentMethods
SetsEnd = SetEndCategory.ParentMethods
SetsAut = SetAutCategory.ParentMethods
SetsEndomorphism = SetEndCategory.ElementMethods
SetsAutomorphism = SetAutCategory.ElementMethods
