r"""Boolean operations set subcategory.

Sets that support set-theoretic boolean operations: union, intersection,
difference, symmetric difference, and complement within an ambient space.
Corresponds to Sage's ``Set_base``, ``Set_boolean_operators``,
``Set_add_sub_operators`` mix-in hierarchy.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Set

from .. import Sets


class _WithBooleanOpsSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "WithBooleanOps")

    def _repr_object_names(self) -> str:
        return "sets with boolean operations"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        @abstract_method
        def union(self, X: Set) -> Set: ...

        @abstract_method
        def intersection(self, X: Set) -> Set: ...

        @abstract_method
        def difference(self, X: Set) -> Set: ...

        @abstract_method
        def symmetric_difference(self, X: Set) -> Set: ...

        @abstract_method
        def complement(self) -> Set:
            r"""Return the complement of ``self`` in its ambient space."""
            ...

        def __or__(self, X: Set) -> Set:
            return self.union(X)

        def __and__(self, X: Set) -> Set:
            return self.intersection(X)

        def __xor__(self, X: Set) -> Set:
            return self.symmetric_difference(X)

        def __add__(self, X: Set) -> Set:
            return self.union(X)

        def __sub__(self, X: Set) -> Set:
            return self.difference(X)
