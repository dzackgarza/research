r"""Concrete Sage-backed set subcategories.

This file records named Sage set constructors and the method surfaces of their
concrete categories.  ``_NamedSets`` is only a constructor collector: its
constructor helpers call Sage first, then refine the resulting parent into
``Sets()`` and the most specific concrete subcategory known from Sage's dispatch.

Named Sage sets exposed here (from ``sage.sets.all``):

    Set                      -- generic set wrapper (Set_object / Set_object_enumerated)
    FiniteEnumeratedSet      -- explicit finite set backed by a tuple
    IntegerRange             -- arithmetic progression of integers
    NonNegativeIntegers      -- {0, 1, 2, ...}
    PositiveIntegers         -- {1, 2, 3, ...}
    Primes                   -- set of prime numbers (or congruence-filtered subsets)
    RealSet                  -- finite union of real intervals
    RecursivelyEnumeratedSet -- set defined by seeds + successor function
    DisjointUnionEnumeratedSets -- concatenation of enumerated families
    CartesianProduct         -- product of sets (via cartesian_product)
    ConditionSet             -- subset defined by predicates
    ImageSubobject           -- image {f(x) | x ∈ X} of a set under a map
    TotallyOrderedFiniteSet  -- finite set with user-specified total order
    FiniteSetMaps            -- all maps between two finite sets
    Family                   -- indexed family (f_i)_{i ∈ I}
    EnumeratedSetFromIterator -- enumerated set built from a callable iterator

Note: ``DisjointSet`` (union-find) is NOT a ``Parent`` and is not included.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import (
        Cardinality,
        SetElement,
    )


def Sets():
    from . import Sets as _Sets

    return _Sets()


def _refine_named_set(S: Any, *categories: Any):
    return refine_category(S, [Sets(), *categories])


def _joined_super_categories(*categories: Any) -> list[Any]:
    return Category.join(categories, as_list=True)


# ---------------------------------------------------------------------------
# Set(X) wrapper objects
# ---------------------------------------------------------------------------


class _SetObjects(Category_singleton):
    r"""Category of ``Set(X)`` wrapper objects (``Set_object`` and subclasses).

    The ``Set`` factory wraps an almost arbitrary object as a Sage parent.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets())

    class ParentMethods:
        @abstract_method
        def object(self):
            r"""Return the underlying wrapped object."""
            ...

        @abstract_method
        def union(self, X) -> SageSet: ...

        @abstract_method
        def intersection(self, X) -> SageSet: ...

        @abstract_method
        def difference(self, X) -> SageSet: ...

        @abstract_method
        def symmetric_difference(self, X) -> SageSet: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def is_empty(self) -> bool: ...

        @abstract_method
        def is_finite(self) -> bool: ...

        @abstract_method
        def subsets(self, size=None) -> SageSet:
            r"""Return the :class:`Subsets` object for ``self``."""
            ...

        @abstract_method
        def subsets_lattice(self):
            r"""Return the lattice of subsets ordered by containment (finite only)."""
            ...

        @abstract_method
        def _sympy_(self):
            r"""Return an equivalent SymPy set."""
            ...


class _SetObjectsEnumerated(Category_singleton):
    r"""Category for ``Set_object_enumerated`` — finite frozenset-backed ``Set(X)`` objects."""

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(
            _SetObjects(),
            Sets().Countable().Finite()
,
        )

    class ParentMethods:
        @abstract_method
        def list(self) -> list: ...

        @abstract_method
        def set(self) -> set:
            r"""Return the underlying Python ``set``."""
            ...

        @abstract_method
        def frozenset(self) -> frozenset:
            r"""Return an immutable Python ``frozenset``."""
            ...

        @abstract_method
        def random_element(self) -> SetElement: ...


# ---------------------------------------------------------------------------
# FiniteEnumeratedSet  (explicit finite set backed by a tuple)
# ---------------------------------------------------------------------------


class _FiniteEnumeratedSetObjects(Category_singleton):
    r"""Category for ``FiniteEnumeratedSet([...])`` objects.

    These are tuple-backed, facade, uniquely-represented finite enumerated sets.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated().Finite().Facade())

    class ParentMethods:
        @abstract_method
        def list(self) -> list: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x) -> bool: ...

        @abstract_method
        def rank(self, x: SetElement) -> int: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...


# ---------------------------------------------------------------------------
# IntegerRange  (arithmetic progression of integers)
# ---------------------------------------------------------------------------


class _IntegerRangeSets(Category_singleton):
    r"""Category for ``IntegerRange`` objects (finite or infinite arithmetic progressions).

    Finite:  both endpoints finite  → ``FiniteEnumeratedSets().Facade()``
    Infinite: one endpoint infinite → ``InfiniteEnumeratedSets().Facade()``
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated().Facade())

    class ParentMethods:
        @abstract_method
        def rank(self, x: SetElement) -> int: ...

        @abstract_method
        def unrank(self, n: int) -> Cardinality: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def next(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x) -> bool: ...

        @abstract_method
        def __len__(self) -> int: ...


# ---------------------------------------------------------------------------
# NonNegativeIntegers / PositiveIntegers  (infinite facade enumerated sets)
# ---------------------------------------------------------------------------


class _NonNegativeIntegersSets(Category_singleton):
    r"""Category for the set ``ℕ₀ = {0, 1, 2, ...}`` (``NonNegativeIntegers``).

    Elements are plain Sage ``Integer`` objects with parent ``ZZ``; this is a
    facade set.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated().Infinite().Facade())

    class ParentMethods:
        def is_finite(self) -> bool:
            return False

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def next(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __contains__(self, x) -> bool: ...

        @abstract_method
        def an_element(self) -> SetElement: ...


class _PositiveIntegersSets(Category_singleton):
    r"""Category for the set ``ℕ₊ = {1, 2, 3, ...}`` (``PositiveIntegers``).

    Subclass of :class:`_NonNegativeIntegersSets` with ``first()`` = 1 and
    ``an_element()`` = 42.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(_NonNegativeIntegersSets())

    class ParentMethods:
        @abstract_method
        def _sympy_(self):
            r"""Return SymPy ``Naturals``."""
            ...


# ---------------------------------------------------------------------------
# Primes
# ---------------------------------------------------------------------------


class _PrimesSets(Category_singleton):
    r"""Category for ``Primes()`` — the set of all prime numbers.

    With congruence conditions (``modulus``, ``classes``), the set is finite
    and falls in ``FiniteEnumeratedSets().Facade()``; otherwise it is infinite.

    Key methods: ``__contains__``, ``__iter__``, ``cardinality``, ``first``,
    ``next``, ``an_element``, ``unrank``.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated().Facade())

    class ParentMethods:
        @abstract_method
        def __contains__(self, x) -> bool:
            r"""Return ``True`` iff ``x`` is prime (and satisfies congruence conditions)."""
            ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def next(self, p: SetElement) -> SetElement: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...


# ---------------------------------------------------------------------------
# RealSet  (finite union of real intervals, Topological)
# ---------------------------------------------------------------------------


class _RealSets(Category_singleton):
    r"""Category for ``RealSet`` — subsets of ℝ as finite unions of intervals.

    ``RealSet`` inherits ``Set_base``, ``Set_boolean_operators``, and
    ``Set_add_sub_operators``, so it supports boolean operations.
    Its Sage category is ``TopologicalSpaces()``.

    Construction class methods:
        ``open(a, b)``, ``closed(a, b)``, ``open_closed(a, b)``,
        ``closed_open(a, b)``, ``point(a)``,
        ``unbounded_below_open(b)``, ``unbounded_below_closed(b)``,
        ``unbounded_above_open(a)``, ``unbounded_above_closed(a)``,
        ``interval(a, b, lower_closed, upper_closed)``
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(
            Sets().Topological(),
            Sets().WithBooleanOps(),
        )

    class ParentMethods:
        @abstract_method
        def union(self, X) -> SageSet: ...

        @abstract_method
        def intersection(self, X) -> SageSet: ...

        @abstract_method
        def difference(self, X) -> SageSet: ...

        @abstract_method
        def symmetric_difference(self, X) -> SageSet: ...

        @abstract_method
        def complement(self) -> SageSet:
            r"""Return the complement of ``self`` in ℝ."""
            ...

        @abstract_method
        def is_empty(self) -> bool: ...

        @abstract_method
        def is_finite(self) -> bool: ...

        @abstract_method
        def is_connected(self) -> bool: ...

        @abstract_method
        def inf(self):
            r"""Return the infimum of ``self`` in ℝ ∪ {±∞}."""
            ...

        @abstract_method
        def sup(self):
            r"""Return the supremum of ``self`` in ℝ ∪ {±∞}."""
            ...

        @abstract_method
        def measure(self):
            r"""Return the Lebesgue measure of ``self``."""
            ...

        @abstract_method
        def closure(self) -> SageSet: ...

        @abstract_method
        def interior(self) -> SageSet: ...

        @abstract_method
        def boundary(self) -> SageSet: ...

        @abstract_method
        def contains(self, x) -> bool:
            r"""Return whether ``x`` is in ``self`` (alias for ``__contains__``)."""
            ...

        @abstract_method
        def __contains__(self, x) -> bool: ...

        @abstract_method
        def __iter__(self):
            r"""Iterate over the ``InternalRealInterval`` components of ``self``."""
            ...

        @abstract_method
        def _sympy_(self): ...


# ---------------------------------------------------------------------------
# RecursivelyEnumeratedSet
# ---------------------------------------------------------------------------


class _RecursivelyEnumeratedSets(Category_singleton):
    r"""Category for ``RecursivelyEnumeratedSet`` — sets defined by seeds + successor function.

    Supports four structure types (dispatch in constructor):
        None / generic   → ``RecursivelyEnumeratedSet_generic``
        ``'symmetric'``  → ``RecursivelyEnumeratedSet_symmetric``
        ``'graded'``     → ``RecursivelyEnumeratedSet_graded``
        ``'forest'``     → ``RecursivelyEnumeratedSet_forest``
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated())

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def breadth_first_search_iterator(self):
            r"""Return a breadth-first search iterator over ``self``."""
            ...

        @abstract_method
        def depth_first_search_iterator(self):
            r"""Return a depth-first search iterator over ``self``."""
            ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        # Graded / symmetric structure only:

        def graded_component(self, depth: int) -> list:
            r"""Return elements at the given BFS depth (graded/symmetric structures)."""
            raise NotImplementedError("graded_component requires a graded or symmetric structure")

        def graded_component_iterator(self):
            r"""Iterate over graded components in order of depth."""
            raise NotImplementedError("graded_component_iterator requires a graded structure")

        def elements_of_depth_iterator(self, depth: int):
            r"""Iterate over elements at the given depth."""
            raise NotImplementedError("elements_of_depth_iterator requires a graded structure")


# ---------------------------------------------------------------------------
# DisjointUnionEnumeratedSets
# ---------------------------------------------------------------------------


class _DisjointUnionEnumeratedSets(Category_singleton):
    r"""Category for ``DisjointUnionEnumeratedSets`` — concatenation of enumerated families.

    Options:
        ``keepkey=True``  → elements are ``(key, element)`` pairs
        ``facade=False``  → elements are wrapped with this set as parent
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated())

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def __contains__(self, x) -> bool: ...


# ---------------------------------------------------------------------------
# CartesianProduct
# ---------------------------------------------------------------------------


class _CartesianProductSets(Category_singleton):
    r"""Category for ``CartesianProduct`` — raw data structure for Cartesian products.

    Use ``cartesian_product(...)`` at the user level to get the full fledged
    Cartesian product with category inference.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets())

    class ParentMethods:
        @abstract_method
        def cartesian_factors(self) -> tuple:
            r"""Return the tuple of factor sets."""
            ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x) -> bool: ...

        @abstract_method
        def _cartesian_product_of_elements(self, elts) -> SetElement:
            r"""Construct a Cartesian product element from a sequence of factors."""
            ...


# ---------------------------------------------------------------------------
# ConditionSet
# ---------------------------------------------------------------------------


class _ConditionSets(Category_singleton):
    r"""Category for ``ConditionSet`` — subset of a universe satisfying predicates.

    ``ConditionSet(ZZ, is_even)`` returns the set of even integers.
    Inherits ``Set_base``, ``Set_boolean_operators``, ``Set_add_sub_operators``.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().WithBooleanOps())

    class ParentMethods:
        @abstract_method
        def universe(self) -> SageSet:
            r"""Return the ambient set from which elements are drawn."""
            ...

        @abstract_method
        def predicates(self) -> tuple:
            r"""Return the tuple of predicates that elements must satisfy."""
            ...

        @abstract_method
        def __contains__(self, x) -> bool:
            r"""Return ``True`` iff ``x`` is in the universe and all predicates hold."""
            ...

        @abstract_method
        def union(self, X) -> SageSet: ...

        @abstract_method
        def intersection(self, X) -> SageSet: ...

        @abstract_method
        def difference(self, X) -> SageSet: ...

        @abstract_method
        def symmetric_difference(self, X) -> SageSet: ...

        @abstract_method
        def _sympy_(self): ...


# ---------------------------------------------------------------------------
# ImageSubobject
# ---------------------------------------------------------------------------


class _ImageSets(Category_singleton):
    r"""Category for ``ImageSubobject`` — image ``{f(x) | x ∈ X}`` of a set under a map.

    Options:
        ``is_injective`` -- ``None``, ``False``, ``True``, or ``'check'``
        ``inverse``      -- optional inverse map from the image back to X
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets())

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x) -> bool: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def an_element(self) -> SetElement: ...


# ---------------------------------------------------------------------------
# TotallyOrderedFiniteSet
# ---------------------------------------------------------------------------


class _TotallyOrderedFiniteSets(Category_singleton):
    r"""Category for ``TotallyOrderedFiniteSet`` — finite set with user-specified total order.

    Category: ``FiniteEnumeratedSets()`` and ``Posets()``.
    Elements (when ``facade=False``) are ``TotallyOrderedFiniteSetElement`` objects
    supporting ``<``, ``<=``, ``>``, ``>=``.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(
            Sets().Countable().Finite()
,
            Sets().TotallyOrdered(),
        )

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def rank(self, x: SetElement) -> int: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...

        @abstract_method
        def __contains__(self, x) -> bool: ...

        @abstract_method
        def min(self) -> SetElement:
            r"""Return the minimum element under the user-specified order."""
            ...

        @abstract_method
        def max(self) -> SetElement:
            r"""Return the maximum element under the user-specified order."""
            ...

    class ElementMethods:
        @abstract_method
        def __lt__(self, other) -> bool: ...

        @abstract_method
        def __le__(self, other) -> bool: ...

        @abstract_method
        def __gt__(self, other) -> bool: ...

        @abstract_method
        def __ge__(self, other) -> bool: ...


# ---------------------------------------------------------------------------
# FiniteSetMaps
# ---------------------------------------------------------------------------


class _FiniteSetMapsSets(Category_singleton):
    r"""Category for ``FiniteSetMaps`` — the set of all maps between two finite sets.

    Category: ``FiniteMonoids()`` (endo-maps) or ``FiniteEnumeratedSets()`` (general).
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated().Finite())

    class ParentMethods:
        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def identity(self) -> SetElement:
            r"""Return the identity map (endo-maps only)."""
            ...


# ---------------------------------------------------------------------------
# Family
# ---------------------------------------------------------------------------


class _FamilySets(Category_singleton):
    r"""Category for ``Family`` — an indexed family ``(f_i)_{i ∈ I}``.

    The ``Family`` factory returns one of:
        ``TrivialFamily``  -- list/tuple input (identity function)
        ``FiniteFamily``   -- finite dict-based family
        ``LazyFamily``     -- infinite or lazy function-based family
        ``EnumeratedFamily`` -- wraps an enumerated set
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated())

    class ParentMethods:
        @abstract_method
        def keys(self):
            r"""Return the index set."""
            ...

        @abstract_method
        def values(self):
            r"""Return the values as an enumerated set."""
            ...

        @abstract_method
        def __getitem__(self, i) -> SetElement:
            r"""Return the element indexed by ``i``."""
            ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def list(self) -> list: ...

        @abstract_method
        def map(self, f) -> SageSet:
            r"""Return the family ``(f(f_i))_{i ∈ I}``."""
            ...

        @abstract_method
        def zip(self, other) -> SageSet:
            r"""Return the family of pairs ``((f_i, g_i))_{i ∈ I}``."""
            ...


# ---------------------------------------------------------------------------
# EnumeratedSetFromIterator
# ---------------------------------------------------------------------------


class _EnumeratedSetsFromIterator(Category_singleton):
    r"""Category for ``EnumeratedSetFromIterator`` — enumerated set from a callable.

    Built from a callable ``f`` that returns an iterator each time it is called.
    Supports optional element caching.
    """

    def super_categories(self) -> list[Any]:
        return _joined_super_categories(Sets().Enumerated())

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...


# ---------------------------------------------------------------------------
# Constructor collector
# ---------------------------------------------------------------------------


class _NamedSets:
    r"""Constructor collector for Sage's named set entry points.

    Every method calls the canonical Sage constructor, then refines the
    resulting parent into ``Sets()`` and the most specific named-set
    subcategory.

    Usage::

        Sets().NamedSets().Primes()
        Sets().NamedSets().Set(ZZ)
        Sets().NamedSets().IntegerRange(2, 100, 5)
    """

    def __init__(self, category):
        self._category = category

    def __repr__(self) -> str:
        return "named set constructors"

    def category(self):
        return self._category

    # -----------------------------------------------------------------------
    # Set(X) wrapper
    # -----------------------------------------------------------------------

    def Set(self, X=None):
        r"""Return ``Set(X)``, refined into :class:`_SetObjects`.

        If ``X`` is finite (frozenset-backed), the result is further refined
        into :class:`_SetObjectsEnumerated`.
        """
        from sage.sets.set import Set as SageSet

        S = SageSet() if X is None else SageSet(X)
        if S.is_finite():
            return _refine_named_set(S, _SetObjectsEnumerated())
        return _refine_named_set(S, _SetObjects())

    # -----------------------------------------------------------------------
    # FiniteEnumeratedSet
    # -----------------------------------------------------------------------

    def FiniteEnumeratedSet(self, elements):
        r"""Return ``FiniteEnumeratedSet(elements)``, refined into its category."""
        from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as SageFES

        S = SageFES(elements)
        return _refine_named_set(S, _FiniteEnumeratedSetObjects())

    # -----------------------------------------------------------------------
    # IntegerRange
    # -----------------------------------------------------------------------

    def IntegerRange(self, *args, **kwds):
        r"""Return an ``IntegerRange``, refined into :class:`_IntegerRangeSets`.

        Automatically dispatches to :class:`IntegerRangeFinite` or
        :class:`IntegerRangeInfinite` depending on the bounds.
        """
        from sage.sets.integer_range import IntegerRange as SageIR

        S = SageIR(*args, **kwds)
        return _refine_named_set(S, _IntegerRangeSets())

    # -----------------------------------------------------------------------
    # NonNegativeIntegers / PositiveIntegers
    # -----------------------------------------------------------------------

    def NonNegativeIntegers(self):
        r"""Return ``NonNegativeIntegers()``, refined into :class:`_NonNegativeIntegersSets`."""
        from sage.sets.non_negative_integers import NonNegativeIntegers as SageNN

        S = SageNN()
        return _refine_named_set(S, _NonNegativeIntegersSets())

    def PositiveIntegers(self):
        r"""Return ``PositiveIntegers()``, refined into :class:`_PositiveIntegersSets`."""
        from sage.sets.positive_integers import PositiveIntegers as SagePP

        S = SagePP()
        return _refine_named_set(S, _PositiveIntegersSets())

    # -----------------------------------------------------------------------
    # Primes
    # -----------------------------------------------------------------------

    def Primes(self, *args, **kwds):
        r"""Return ``Primes(*args, **kwds)``, refined into :class:`_PrimesSets`."""
        from sage.sets.primes import Primes as SagePrimes

        S = SagePrimes(*args, **kwds)
        return _refine_named_set(S, _PrimesSets())

    # -----------------------------------------------------------------------
    # RealSet
    # -----------------------------------------------------------------------

    def RealSet(self, *args, **kwds):
        r"""Return a ``RealSet``, refined into :class:`_RealSets`."""
        from sage.sets.real_set import RealSet as SageRealSet

        S = SageRealSet(*args, **kwds)
        return _refine_named_set(S, _RealSets())

    # -----------------------------------------------------------------------
    # RecursivelyEnumeratedSet
    # -----------------------------------------------------------------------

    def RecursivelyEnumeratedSet(self, seeds, successors, *args, **kwds):
        r"""Return a ``RecursivelyEnumeratedSet``, refined into :class:`_RecursivelyEnumeratedSets`."""
        from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as SageRES

        S = SageRES(seeds, successors, *args, **kwds)
        return _refine_named_set(S, _RecursivelyEnumeratedSets())

    # -----------------------------------------------------------------------
    # DisjointUnionEnumeratedSets
    # -----------------------------------------------------------------------

    def DisjointUnionEnumeratedSets(self, family, **kwds):
        r"""Return a ``DisjointUnionEnumeratedSets``, refined into :class:`_DisjointUnionEnumeratedSets`."""
        from sage.sets.disjoint_union_enumerated_sets import (
            DisjointUnionEnumeratedSets as SageDUES,
        )

        S = SageDUES(family, **kwds)
        return _refine_named_set(S, _DisjointUnionEnumeratedSets())

    # -----------------------------------------------------------------------
    # CartesianProduct
    # -----------------------------------------------------------------------

    def CartesianProduct(self, sets, **kwds):
        r"""Return a ``CartesianProduct``, refined into :class:`_CartesianProductSets`.

        Note: pass ``category`` explicitly if needed; the default is
        ``Sets().CartesianProducts()``.
        """
        from sage.sets.cartesian_product import CartesianProduct as SageCP

        category = kwds.pop("category", Sets().CartesianProducts())
        S = SageCP(tuple(sets), category=category, **kwds)
        return _refine_named_set(S, _CartesianProductSets())

    # -----------------------------------------------------------------------
    # ConditionSet
    # -----------------------------------------------------------------------

    def ConditionSet(self, universe, *predicates, **kwds):
        r"""Return a ``ConditionSet``, refined into :class:`_ConditionSets`.

        Example::

            Sets().NamedSets().ConditionSet(ZZ, is_even)
        """
        from sage.sets.condition_set import ConditionSet as SageCS

        S = SageCS(universe, *predicates, **kwds)
        return _refine_named_set(S, _ConditionSets())

    # -----------------------------------------------------------------------
    # ImageSubobject
    # -----------------------------------------------------------------------

    def ImageSubobject(self, f, domain_subset, **kwds):
        r"""Return ``ImageSubobject(f, domain_subset)``, refined into :class:`_ImageSets`."""
        from sage.sets.image_set import ImageSubobject as SageIS

        S = SageIS(f, domain_subset, **kwds)
        return _refine_named_set(S, _ImageSets())

    # -----------------------------------------------------------------------
    # TotallyOrderedFiniteSet
    # -----------------------------------------------------------------------

    def TotallyOrderedFiniteSet(self, elements, **kwds):
        r"""Return a ``TotallyOrderedFiniteSet``, refined into :class:`_TotallyOrderedFiniteSets`."""
        from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet as SageTOFS

        S = SageTOFS(elements, **kwds)
        return _refine_named_set(S, _TotallyOrderedFiniteSets())

    # -----------------------------------------------------------------------
    # FiniteSetMaps
    # -----------------------------------------------------------------------

    def FiniteSetMaps(self, domain, codomain=None, **kwds):
        r"""Return a ``FiniteSetMaps`` object, refined into :class:`_FiniteSetMapsSets`."""
        from sage.sets.finite_set_maps import FiniteSetMaps as SageFSM

        if codomain is None:
            S = SageFSM(domain, **kwds)
        else:
            S = SageFSM(domain, codomain, **kwds)
        return _refine_named_set(S, _FiniteSetMapsSets())

    # -----------------------------------------------------------------------
    # Family
    # -----------------------------------------------------------------------

    def Family(self, indices, function=None, **kwds):
        r"""Return a ``Family``, refined into :class:`_FamilySets`."""
        from sage.sets.family import Family as SageFamily

        if function is None:
            S = SageFamily(indices, **kwds)
        else:
            S = SageFamily(indices, function, **kwds)
        return _refine_named_set(S, _FamilySets())

    # -----------------------------------------------------------------------
    # EnumeratedSetFromIterator
    # -----------------------------------------------------------------------

    def EnumeratedSetFromIterator(self, f, args=(), **kwds):
        r"""Return an ``EnumeratedSetFromIterator``, refined into :class:`_EnumeratedSetsFromIterator`."""
        from sage.sets.set_from_iterator import EnumeratedSetFromIterator as SageESFI

        S = SageESFI(f, args, **kwds)
        return _refine_named_set(S, _EnumeratedSetsFromIterator())

    # -----------------------------------------------------------------------
    # Convenience: CartesianProducts via cartesian_product functor
    # -----------------------------------------------------------------------

    def cartesian_product(self, *factors):
        r"""Return ``cartesian_product(factors)``, refined into :class:`_CartesianProductSets`."""
        from sage.categories.cartesian_product import cartesian_product

        S = cartesian_product(list(factors))
        return _refine_named_set(S, _CartesianProductSets())
