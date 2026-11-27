r"""One-object subcategories for explicitly-finite named sets.

Covers:
  - FiniteEnumeratedSet  -- explicit finite set backed by a tuple
  - TotallyOrderedFiniteSet -- finite set with user-specified total order
  - FiniteSetMaps -- all maps between two finite sets
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


class _FiniteEnumeratedSetObjects(Category_singleton):
    r"""Category for ``FiniteEnumeratedSet([...])`` -- tuple-backed facade finite set."""

    def super_categories(self) -> list:
        return [_Sets().Countable().Finite().Facade()]

    class ParentMethods:
        @abstract_method
        def list(self) -> list[SetElement]: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x: SetElement) -> bool: ...

        @abstract_method
        def rank(self, x: SetElement) -> int: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...


class _TotallyOrderedFiniteSets(Category_singleton):
    r"""Category for ``TotallyOrderedFiniteSet`` -- finite set with a user-specified total order.

    Sage category: ``FiniteEnumeratedSets()`` and ``Posets()``.
    Elements (when ``facade=False``) are ``TotallyOrderedFiniteSetElement`` objects.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable().Finite(), _Sets().TotallyOrdered()]

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
        def __contains__(self, x: SetElement) -> bool: ...

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
        def __lt__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __le__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __gt__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __ge__(self, other: SetElement) -> bool: ...


class _FiniteSetMapsSets(Category_singleton):
    r"""Category for ``FiniteSetMaps`` -- all maps between two finite sets.

    Sage category: ``FiniteMonoids()`` (endo-maps) or ``FiniteEnumeratedSets()``.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable().Finite()]

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
