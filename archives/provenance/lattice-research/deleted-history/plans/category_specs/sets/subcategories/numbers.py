r"""One-object subcategories for number-theoretic infinite sets.

Covers: NonNegativeIntegers, PositiveIntegers, Primes, IntegerRange.
All are countable facade sets (finite or infinite depending on parameters).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement


def _Sets():
    from .. import Sets as _S
    return _S()


class _IntegerRangeSets(Category_singleton):
    r"""Category for ``IntegerRange`` -- arithmetic progressions of integers.

    Finite when both bounds are finite (``FiniteEnumeratedSets().Facade()``);
    infinite when one bound is infinite (``InfiniteEnumeratedSets().Facade()``).
    """

    def super_categories(self) -> list:
        return [_Sets().Countable().Facade()]

    class ParentMethods:
        @abstract_method
        def rank(self, x: SetElement) -> int: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def next(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x: SetElement) -> bool: ...

        @abstract_method
        def __len__(self) -> int: ...


class _NonNegativeIntegersSets(Category_singleton):
    r"""Category for ``NonNegativeIntegers()`` -- the set N_0 = {0, 1, 2, ...}.

    Elements are plain Sage ``Integer`` objects with parent ``ZZ``; facade set.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable().Infinite().Facade()]

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
        def __contains__(self, x: SetElement) -> bool: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def from_integer(self, n: int) -> SetElement:
            r"""Return the element corresponding to the integer ``n``."""
            ...


class _PositiveIntegersSets(Category_singleton):
    r"""Category for ``PositiveIntegers()`` -- the set N_+ = {1, 2, 3, ...}.

    Subclass of ``_NonNegativeIntegersSets``; ``first()`` = 1.
    """

    def super_categories(self) -> list:
        return [_NonNegativeIntegersSets()]

    class ParentMethods:
        @abstract_method
        def rank(self, x: SetElement) -> int: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...

        @abstract_method
        def _sympy_(self):
            r"""Return SymPy ``Naturals``."""
            ...


class _PrimesSets(Category_singleton):
    r"""Category for ``Primes()`` -- the set of all prime numbers.

    With congruence conditions (``modulus``, ``classes``), the set is finite
    and falls in ``CountableFiniteFacade``; otherwise it is infinite.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable().Facade()]

    class ParentMethods:
        @abstract_method
        def __contains__(self, x: SetElement) -> bool:
            r"""Return ``True`` iff ``x`` is prime (and satisfies any congruence condition)."""
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
