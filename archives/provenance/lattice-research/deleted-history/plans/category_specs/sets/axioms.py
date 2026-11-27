r"""Axiomatic subcategory mixin classes for ``Sets``.

Every class here is a ``CategoryWithAxiom`` wired into ``Sets`` in
``__init__.py`` via the ``_base_category_class_and_axiom`` pattern.

Naming convention:
    Sets()                  -- our category (this package)
    SageSets()              -- sage.categories.sets_cat.Sets()
    FiniteSets()            -- our Sets().Finite()
    SageFiniteSets()        -- sage.categories.finite_sets.FiniteSets()
    EnumeratedSets()        -- our Sets().Enumerated()
    SageEnumeratedSets()    -- sage.categories.enumerated_sets.EnumeratedSets()
    etc.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as SageFiniteEnumeratedSets
from sage.categories.finite_sets import FiniteSets as SageFiniteSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as SageInfiniteEnumeratedSets
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import (
        Cardinality,
        RealNumber,
        Set,
        SetElement,
    )


def Sets():
    from . import Sets as _Sets

    return _Sets()


def _refine_named_set(S: Any, *categories: Any):
    return refine_category(S, [Sets(), *categories])


# ---------------------------------------------------------------------------
# Finiteness / Countability axioms
# ---------------------------------------------------------------------------


class _CountableSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets, "Countable") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "countable sets"

    def super_categories(self) -> list[Any]:

        return [Sets(), SageEnumeratedSets()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return True

        @abstract_method
        def __iter__(self):
            r"""Return an iterator over the elements of ``self``."""
            ...

        @abstract_method
        def first(self) -> SetElement:
            r"""Return the first element of ``self`` under the canonical enumeration."""
            ...

        @abstract_method
        def next(self, e: SetElement) -> SetElement:
            r"""Return the element immediately following ``e`` in the canonical enumeration."""
            ...

        @abstract_method
        def unrank(self, n: int) -> SetElement:
            r"""Return the element at 0-based position ``n``."""
            ...

        @abstract_method
        def rank(self, e: SetElement) -> int:
            r"""Return the 0-based position of ``e`` in the canonical enumeration."""
            ...

        def is_empty(self) -> bool:
            r"""Return whether ``self`` is empty."""
            try:
                next(iter(self))
                return False
            except StopIteration:
                return True

        def iterator_range(self, start=None, stop=None, step=None):
            r"""Iterate over the rank range ``[start, stop)`` with stride ``step``."""
            step = 1 if step is None else step
            start = 0 if start is None else start
            if stop is None:
                i = start
                while True:
                    try:
                        yield self.unrank(i)
                    except IndexError:
                        return
                    i += step
            else:
                for j in range(start, stop, step):
                    yield self.unrank(j)


class _UncountableSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets, "Uncountable") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "uncountable sets"

    def super_categories(self) -> list[Any]:
        return [Sets().Infinite()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return False

        def is_uncountable(self) -> bool:
            return True


class _FiniteSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets, "Finite") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "finite sets"

    def super_categories(self) -> list[Any]:
        return [SageFiniteSets(), Sets().Countable()]

    def __contains__(self, S: Any) -> bool:
        return S in SageFiniteSets() or (S in self.base_category() and S.is_finite())

    class ParentMethods:
        def is_finite(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        def __len__(self) -> int:
            return int(self.cardinality())

        @abstract_method
        def list(self) -> list[SetElement]:
            r"""Return a fresh list of the elements of ``self``."""
            ...

        @abstract_method
        def tuple(self) -> tuple[SetElement, ...]:
            r"""Return a (cached) tuple of the elements of ``self``."""
            ...

        @abstract_method
        def random_element(self) -> SetElement:
            r"""Return a uniformly random element of ``self``."""
            ...

        def unrank_range(self, start=None, stop=None, step=None) -> list[SetElement]:
            r"""Return the rank-range ``[start, stop)`` as a list."""
            return list(self.iterator_range(start, stop, step))


class _InfiniteSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets, "Infinite") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "infinite sets"

    def super_categories(self) -> list[Any]:
        return [SageSets().Infinite(), Sets()]

    def __contains__(self, S: Any) -> bool:
        return S in SageSets().Infinite() or (S in self.base_category() and not S.is_finite())

    class ParentMethods:
        def is_finite(self) -> bool:
            return False

        def cardinality(self) -> Cardinality:
            from sage.rings.infinity import infinity

            return infinity


class _FiniteCountableSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets().Countable(), "Finite") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "finite countable sets"

    def super_categories(self) -> list[Any]:

        return [SageFiniteEnumeratedSets(), Sets().Countable(), Sets().Finite()]

    class ParentMethods:
        def random_element(self) -> SetElement:
            r"""Return a uniformly random element (by sampling the list)."""
            import random

            return random.choice(self.list())

        def _cardinality_from_iterator(self) -> Cardinality:
            r"""Brute-force cardinality by iterating through all elements."""
            from sage.rings.integer import Integer

            return Integer(sum(1 for _ in self))

        def _list_from_iterator(self) -> list[SetElement]:
            r"""Build and cache the element list by iterating."""
            return list(iter(self))


class _InfiniteCountableSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets().Countable(), "Infinite") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "infinite countable sets"

    def super_categories(self) -> list[Any]:

        return [SageInfiniteEnumeratedSets(), Sets().Countable(), Sets().Infinite()]


# ---------------------------------------------------------------------------
# Facade sets
# ---------------------------------------------------------------------------


class _FacadeSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets, "Facade") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "facade sets"

    def super_categories(self) -> list[Any]:
        return [SageSets().Facade(), Sets()]

    class ParentMethods:
        def is_facade(self) -> bool:
            return True

        @abstract_method
        def _element_constructor_(self, element):
            r"""Coerce ``element`` into ``self`` via the facade parents."""
            ...

        @abstract_method
        def facade_for(self) -> tuple:
            r"""Return the tuple of parents this set is a facade for."""
            ...


# ---------------------------------------------------------------------------
# Topological / Metric sets
# ---------------------------------------------------------------------------


class _TopologicalSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets, "Topological") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "topological sets"

    def super_categories(self) -> list[Any]:
        return [SageSets().Topological(), Sets()]

    class SubcategoryMethods:
        @cached_method
        def Metric(self):
            return self._with_axiom("Metric")

    class ParentMethods:
        def is_topological(self) -> bool:
            return True

        @abstract_method
        def is_connected(self) -> bool:
            r"""Return whether ``self`` is a connected topological space."""
            ...

        @abstract_method
        def closure(self) -> SageSet:
            r"""Return the topological closure of ``self``."""
            ...

        @abstract_method
        def interior(self) -> SageSet:
            r"""Return the topological interior of ``self``."""
            ...

        @abstract_method
        def boundary(self) -> SageSet:
            r"""Return the topological boundary of ``self``."""
            ...

        @abstract_method
        def is_open(self) -> bool:
            r"""Return whether ``self`` is open in its ambient topological space."""
            ...

        @abstract_method
        def is_closed(self) -> bool:
            r"""Return whether ``self`` is closed in its ambient topological space."""
            ...

        @abstract_method
        def is_compact(self) -> bool:
            r"""Return whether ``self`` is compact."""
            ...


class _MetricSets(CategoryWithAxiom):
    # _base_category_class_and_axiom = (_TopologicalSets, "Metric") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "metric sets"

    def super_categories(self) -> list[Any]:
        return [SageSets().Metric(), _TopologicalSets()]

    class ParentMethods:
        def is_metric(self) -> bool:
            return True

        @abstract_method
        def metric(self, x: SetElement, y: SetElement) -> RealNumber:
            r"""Return the metric distance between ``x`` and ``y``."""
            ...

        @abstract_method
        def ball(self, center: SetElement, radius: RealNumber) -> Set:
            r"""Return the open ball of given ``radius`` around ``center``."""
            ...

        @abstract_method
        def dist(self, x: SetElement, y: SetElement) -> RealNumber:
            r"""Alias for :meth:`metric`."""
            ...


# ---------------------------------------------------------------------------
# Totally ordered sets
# ---------------------------------------------------------------------------


class _TotallyOrdered(CategoryWithAxiom):
    # _base_category_class_and_axiom = (Sets, "TotallyOrdered") — wired in __init__.py

    def _repr_object_names(self) -> str:
        return "totally ordered sets"

    def super_categories(self) -> list[Any]:
        return [Sets()]

    class ParentMethods:
        def is_totally_ordered(self) -> bool:
            return True

        @abstract_method
        def rank(self, x: SetElement) -> int:
            r"""Return the 0-based position of ``x`` in the total order."""
            ...

        @abstract_method
        def unrank(self, n: int) -> SetElement:
            r"""Return the element at 0-based position ``n``."""
            ...

        @abstract_method
        def min(self) -> SetElement:
            r"""Return the minimum element of ``self``."""
            ...

        @abstract_method
        def max(self) -> SetElement:
            r"""Return the maximum element of ``self``."""
            ...

    class ElementMethods:
        @abstract_method
        def __lt__(self, other: SetElement) -> bool:
            r"""Return whether ``self`` is strictly less than ``other``."""
            ...

        @abstract_method
        def __le__(self, other: SetElement) -> bool:
            r"""Return whether ``self`` is less than or equal to ``other``."""
            ...

        def __gt__(self, other: SetElement) -> bool:
            return other.__lt__(self)

        def __ge__(self, other: SetElement) -> bool:
            return other.__le__(self)
