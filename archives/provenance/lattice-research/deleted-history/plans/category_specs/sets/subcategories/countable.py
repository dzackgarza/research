r"""Countable set subcategories (countable, and finite/infinite countable)."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, final, override

from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as SageFiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as SageInfiniteEnumeratedSets
from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, Set, SetElement, SetMorphism

from .. import Sets


class _CountableSets(CategoryWithAxiom):
    r"""Countable sets — sets admitting an explicit enumeration (injection into N).

    Canonical chain: ``Sets().Countable()``.

    Sage's ``EnumeratedSets`` axiom captures exactly countability: a set is
    countable iff there exists an enumeration f: X -> N, which is an iterator.
    """

    _base_category_class_and_axiom = (Sets, "Countable")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "countable sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets(), SageEnumeratedSets()]

    class ParentMethods:
        @override
        @final
        def is_countable(self) -> bool:
            return True

        @override
        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstract_method
        def __getitem__(self, i: Integer) -> SetElement:
            r"""Return the ``i``-th element in the chosen enumeration."""
            ...

        @override
        @abstract_method
        def rank(self, e: SetElement) -> Integer:
            r"""Return the enumeration index of ``e``."""
            ...

        @override
        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @override
        @abstract_method
        def is_empty(self) -> bool: ...

        @override
        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def map(self, f: SetMorphism, name: str | None = None, *, is_injective: bool = True) -> Set:
            r"""Return the image of this enumerated set under ``f``."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...


class _FiniteCountableSets(CategoryWithAxiom):
    r"""Finite countable sets — ``Sets().Countable().Finite()``.

    Canonical chain: ``Sets().Countable().Finite()``.
    """

    _base_category_class_and_axiom = (_CountableSets, "Finite")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "finite countable sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageFiniteEnumeratedSets(), Sets().Countable(), Sets().Finite()]

    class ParentMethods:
        @override
        @abstract_method
        def __len__(self) -> Integer: ...

        @override
        @abstract_method
        def random_element(self) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...


class _InfiniteCountableSets(CategoryWithAxiom):
    r"""Infinite countable sets — ``Sets().Countable().Infinite()``.

    Canonical chain: ``Sets().Countable().Infinite()``.
    """

    _base_category_class_and_axiom = (_CountableSets, "Infinite")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "infinite countable sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageInfiniteEnumeratedSets(), Sets().Countable(), Sets().Infinite()]

    class ParentMethods:
        @override
        @abstract_method
        def random_element(self) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
