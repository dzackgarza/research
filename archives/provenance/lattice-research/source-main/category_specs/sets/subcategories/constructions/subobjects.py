r"""Subobject construction category for sets.

For sets, subobjects are subsets. The class still extends Sage's construction
category so it can attach to arbitrary subcategories via ``category_of``.
"""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.sets_cat import Sets as SageSets

from ....cat import Category, SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Cardinality, Set, SetElement, Subset, SympySet


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
        from ..condition import condition_subset

        subset_category = self if category is None else category
        subset = condition_subset(
            ambient,
            predicates,
            names=names,
        )
        return refine_category(subset, subset_category)

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> Set:
            r"""Return the ambient set of which ``self`` is a subset."""
            ...

        @abstractmethod
        def __call__(self, x: SetElement) -> SetElement:
            r"""Coerce an ambient element into this subset when possible."""
            ...

        @final
        def ambient_set(self) -> Set:
            r"""Return the ambient set of which ``self`` is a subset."""
            return self.ambient()

        @final
        def is_universe(self) -> bool:
            r"""Return whether this subset equals its ambient set."""
            return self == self.ambient()

        @final
        def lift(self, x: SetElement) -> SetElement:
            r"""Include an element of this subobject into its ambient set."""
            assert x in self, f"{x} is not in {self}"
            return self.ambient()(x)

        @final
        def retract(self, x: SetElement) -> SetElement:
            r"""Retract an ambient element when it lies in the subset."""
            return self(x)

        @final
        def predicate(self) -> Callable[[SetElement], bool]:
            r"""Return the characteristic predicate inside ``ambient()``."""
            return lambda x: x in self

        @override
        @final
        def is_finite(self) -> bool:
            if self.ambient().is_finite():
                return True
            raise NotImplementedError(
                "subobject finiteness requires finite ambient or explicit cardinality"
            )

        @override
        @final
        def is_empty(self) -> bool:
            if self.ambient().is_finite():
                return all(x not in self for x in self.ambient())
            raise NotImplementedError(
                "subobject emptiness requires finite ambient or explicit search"
            )

        @override
        @final
        def cardinality(self) -> Cardinality:
            if self.ambient().is_finite():
                from sage.rings.integer import Integer

                return Integer(sum(x in self for x in self.ambient()))
            raise NotImplementedError(
                "subobject cardinality requires finite ambient or implementation"
            )

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool:
            r"""Return whether ``x`` lies in ``ambient()`` and satisfies predicate."""
            ...

        @final
        def _subobjects_category(self) -> Subsets:
            from ... import Sets

            return Sets().Subobjects()

        def union(self, X: Subset) -> Subset:
            r"""Return the condition-backed union of ``self`` and ``X``."""
            return self._subobjects_category().Of(
                self.ambient(), (lambda x: x in self or x in X,)
            )

        def intersection(self, X: Subset) -> Subset:
            r"""Return the condition-backed intersection of ``self`` and ``X``."""
            return self._subobjects_category().Of(
                self.ambient(), (lambda x: x in self and x in X,)
            )

        def difference(self, X: Subset) -> Subset:
            r"""Return the condition-backed set-theoretic difference ``self \ X``."""
            return self._subobjects_category().Of(
                self.ambient(), (lambda x: x in self and x not in X,)
            )

        def symmetric_difference(self, X: Subset) -> Subset:
            r"""Return the condition-backed symmetric difference with ``X``."""
            return self._subobjects_category().Of(
                self.ambient(), (lambda x: (x in self) != (x in X),)
            )

        @final
        def complement(self) -> Subset:
            r"""Return the condition-backed complement in the ambient set."""
            return self._subobjects_category().Of(
                self.ambient(), (lambda x: x not in self,)
            )

        @final
        def _sympy_(self) -> SympySet:
            r"""Return the symbolic set corresponding to this subset."""
            return SageSets.ParentMethods._sympy_(self)

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
