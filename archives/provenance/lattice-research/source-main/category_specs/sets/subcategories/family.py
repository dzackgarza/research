r"""One-object subcategory for Sage indexed families."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton

if TYPE_CHECKING:
    from ...types import Cardinality, Set, SetElement, SetFamily, SetMorphism


from ...cat import Category
from .. import Sets


class _FamilySets(Category_singleton):
    r"""Indexed families ``(f_i)_{i in I}``, finite, lazy, trivial, or enumerated.

    Constructor target:
    ``Sets().Constructors().Family(indices, function)`` refines Sage's family
    parent here.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable()]

    class ParentMethods:
        @abstractmethod
        def hidden_keys(self) -> Set:
            r"""Return the index keys hidden by this family presentation."""
            ...

        @abstractmethod
        def keys(self) -> Set:
            r"""Return the index set of this family."""
            ...

        @abstractmethod
        def values(self) -> Set:
            r"""Return the set of values appearing in this family."""
            ...

        @abstractmethod
        def items(self) -> Set:
            r"""Return the set of indexed pairs of this family."""
            ...

        @abstractmethod
        def zip(
            self, f: SetMorphism, other: SetFamily, name: str | None = None
        ) -> SetFamily:
            r"""Return the family obtained by applying ``f`` pointwise to two
            families.
            """
            ...

        @abstractmethod
        def map(self, f: SetMorphism, name: str | None = None) -> SetFamily:
            r"""Return the pointwise image family under ``f``."""
            ...

        @abstractmethod
        def inverse_family(self) -> SetFamily:
            r"""Return the inverse family when this family is bijectively indexed."""
            ...

        @final
        def has_key(self, k: SetElement) -> bool:
            r"""Return whether ``k`` is an index key of this family."""
            return k in self.keys() or k in self.hidden_keys()

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool: ...

        @override
        @abstractmethod
        def __len__(self) -> int: ...

        @override
        @abstractmethod
        def cardinality(self) -> Cardinality: ...

        @override
        @abstractmethod
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstractmethod
        def __getitem__(self, i: SetElement) -> SetElement: ...

    class ElementMethods: ...
