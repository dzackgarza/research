r"""Functorial construction categories for ``Sets``.

This file defines categories like ``Subobjects()`` which provide set-theoretic
operations (union, intersection, etc.) that only make sense within a fixed
ambient context.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.subobjects import SubobjectsCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from sage.structure.parent import Parent
    SageSet = Parent


class _Subobjects(SubobjectsCategory):
    r"""Subobject category for sets.

    Provides the lattice of subsets of a fixed ambient set, with operations
    like intersection and complement.
    """

    class ParentMethods:
        @abstract_method
        def ambient_set(self) -> SageSet:
            r"""Return the ambient set of which ``self`` is a subobject."""
            ...

        @abstract_method
        def union(self, X: SageSet) -> SageSet:
            r"""Return the set-theoretic union ``self ∪ X``."""
            ...

        @abstract_method
        def intersection(self, X: SageSet) -> SageSet:
            r"""Return the set-theoretic intersection ``self ∩ X``."""
            ...

        @abstract_method
        def difference(self, X: SageSet) -> SageSet:
            r"""Return the set-theoretic difference ``self \ X``."""
            ...

        @abstract_method
        def symmetric_difference(self, X: SageSet) -> SageSet:
            r"""Return the symmetric difference ``self △ X``."""
            ...

        @abstract_method
        def complement(self) -> SageSet:
            r"""Return the complement of ``self`` in its ambient set."""
            ...

        def __or__(self, X: SageSet) -> SageSet:
            return self.union(X)

        def __and__(self, X: SageSet) -> SageSet:
            return self.intersection(X)

        def __xor__(self, X: SageSet) -> SageSet:
            return self.symmetric_difference(X)

        def __sub__(self, X: SageSet) -> SageSet:
            return self.difference(X)
