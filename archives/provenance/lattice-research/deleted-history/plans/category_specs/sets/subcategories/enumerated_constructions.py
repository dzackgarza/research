r"""One-object subcategories for constructed enumerated sets.

Covers:
  - RecursivelyEnumeratedSet -- seeds + successor function
  - DisjointUnionEnumeratedSets -- concatenation of enumerated families
  - Family -- indexed family (f_i)_{i in I}
  - EnumeratedSetFromIterator -- enumerated set built from a callable
  - CartesianProduct -- Cartesian product of sets
  - ImageSubobject -- image {f(x) | x in X} under a map
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Set, SetElement


def _Sets():
    from .. import Sets as _S
    return _S()


class _RecursivelyEnumeratedSets(Category_singleton):
    r"""Category for ``RecursivelyEnumeratedSet`` -- seeds + successor function.

    Supports: generic, symmetric, graded, forest structure types.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def breadth_first_search_iterator(self):
            r"""Return a BFS iterator over ``self``."""
            ...

        @abstract_method
        def depth_first_search_iterator(self):
            r"""Return a DFS iterator over ``self``."""
            ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def graded_component(self, depth: int) -> list:
            r"""Return elements at the given BFS depth (graded/symmetric structures)."""
            ...

        @abstract_method
        def graded_component_iterator(self):
            r"""Iterate over graded components in order of depth."""
            ...

        @abstract_method
        def elements_of_depth_iterator(self, depth: int):
            r"""Iterate over elements at the given depth."""
            ...


class _DisjointUnionEnumeratedSets(Category_singleton):
    r"""Category for ``DisjointUnionEnumeratedSets`` -- concatenation of enumerated families.

    Options: ``keepkey=True`` (elements are (key, element) pairs),
    ``facade=False`` (elements are wrapped with this set as parent).
    """

    def super_categories(self) -> list:
        return [_Sets().Countable()]

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
        def __contains__(self, x: SetElement) -> bool: ...


class _FamilySets(Category_singleton):
    r"""Category for ``Family`` -- an indexed family (f_i)_{i in I}.

    Returns one of: TrivialFamily, FiniteFamily, LazyFamily, EnumeratedFamily.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable()]

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
        def __getitem__(self, i: SetElement) -> SetElement:
            r"""Return the element indexed by ``i``."""
            ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def list(self) -> list[SetElement]: ...

        @abstract_method
        def map(self, f) -> Set:
            r"""Return the family ``(f(f_i))_{i in I}``."""
            ...

        @abstract_method
        def zip(self, other: Set) -> Set:
            r"""Return the family of pairs ``((f_i, g_i))_{i in I}``."""
            ...


class _EnumeratedSetsFromIterator(Category_singleton):
    r"""Category for ``EnumeratedSetFromIterator`` -- enumerated set from a callable.

    Built from a callable ``f`` that returns an iterator. Supports optional caching.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...


class _CartesianProductSets(Category_singleton):
    r"""Category for ``CartesianProduct`` -- raw data structure for Cartesian products.

    Use ``cartesian_product(...)`` at the user level.
    """

    def super_categories(self) -> list:
        return [_Sets()]

    class ParentMethods:
        @abstract_method
        def cartesian_factors(self) -> tuple:
            r"""Return the tuple of factor sets."""
            ...

        @abstract_method
        def cartesian_projection(self, i: int) -> Set:
            r"""Return the projection onto factor ``i``."""
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
        def __contains__(self, x: SetElement) -> bool: ...

        @abstract_method
        def _cartesian_product_of_elements(self, elts) -> SetElement:
            r"""Construct a Cartesian product element from a sequence of factors."""
            ...


class _ImageSets(Category_singleton):
    r"""Category for ``ImageSubobject`` -- image {f(x) | x in X} of a set under a map.

    Options: ``is_injective`` (None, False, True, or 'check'), ``inverse``.
    """

    def super_categories(self) -> list:
        return [_Sets()]

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x: SetElement) -> bool: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def an_element(self) -> SetElement: ...
