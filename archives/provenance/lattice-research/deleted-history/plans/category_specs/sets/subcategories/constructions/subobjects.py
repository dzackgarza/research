r"""Subobject construction category for sets.

For sets, subobjects are subsets. The class still extends Sage's construction
category so it can attach to arbitrary subcategories via ``category_of``.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category, SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Set, SetElement, Subset, SympySet


class Subsets(SubobjectsCategory):
    r"""Subobjects of sets, equivalently subsets with an ambient set.

    Canonical chain: ``Sets().Subobjects()``.
    """

    @final
    def Of(
        self,
        ambient: Set,
        predicates: Sequence[Callable[[SetElement], bool]],
        *,
        names: str | tuple[str, ...] | None = None,
        category: Category | None = None,
    ) -> Subset:
        r"""Return the predicate-defined subset of ``ambient``.

        Sage's ``ConditionSet`` is the backing implementation, not a public
        category.  The public mathematical object is the resulting subobject of
        ``ambient``.
        """
        from ....utils import refine_category
        from ... import Sets
        from ..condition import condition_subset

        subset_category = self if category is None else category
        subset = condition_subset(
            ambient,
            predicates,
            names=names,
            category=subset_category,
        )
        return refine_category(subset, [Sets(), self])

    class ParentMethods:
        @abstract_method
        def ambient(self) -> Set:
            r"""Return the ambient set of which ``self`` is a subset."""
            ...

        @final
        def ambient_set(self) -> Set:
            r"""Return the ambient set of which ``self`` is a subset."""
            return self.ambient()

        @final
        def predicate(self) -> Callable[[SetElement], bool]:
            r"""Return the characteristic predicate inside ``ambient()``."""
            return lambda x: x in self

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool:
            r"""Return whether ``x`` lies in ``ambient()`` and satisfies ``predicate()``."""
            ...

        @abstract_method
        def union(self, X: Subset) -> Subset:
            r"""Return the condition-backed set-theoretic union of ``self`` and ``X``."""
            ...

        @abstract_method
        def intersection(self, X: Subset) -> Subset:
            r"""Return the condition-backed intersection of ``self`` and ``X``."""
            ...

        @abstract_method
        def difference(self, X: Subset) -> Subset:
            r"""Return the condition-backed set-theoretic difference ``self \ X``."""
            ...

        @abstract_method
        def symmetric_difference(self, X: Subset) -> Subset:
            r"""Return the condition-backed symmetric difference of ``self`` and ``X``."""
            ...

        @abstract_method
        def complement(self) -> Subset:
            r"""Return the condition-backed complement of ``self`` in its ambient set."""
            ...

        @abstract_method
        def _sympy_(self) -> SympySet:
            r"""Return the symbolic set corresponding to this subset."""
            ...

        @final
        def __or__(self, X: Subset) -> Subset:
            return self.union(X)

        @final
        def __and__(self, X: Subset) -> Subset:
            return self.intersection(X)

        @final
        def __xor__(self, X: Subset) -> Subset:
            return self.symmetric_difference(X)

        @final
        def __sub__(self, X: Subset) -> Subset:
            return self.difference(X)

    class ElementMethods: ...
    class MorphismMethods: ...


