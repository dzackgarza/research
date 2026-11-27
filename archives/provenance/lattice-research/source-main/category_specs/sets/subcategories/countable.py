r"""Countable set subcategories (countable, and finite/infinite countable)."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, cast, final, override

from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.categories.finite_enumerated_sets import (
    FiniteEnumeratedSets as SageFiniteEnumeratedSets,
)
from sage.categories.infinite_enumerated_sets import (
    InfiniteEnumeratedSets as SageInfiniteEnumeratedSets,
)

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
        @final
        def __iter__(self) -> Iterator[SetElement]:
            return cast(
                "Iterator[SetElement]", SageEnumeratedSets.ParentMethods.__iter__(self)
            )

        @override
        @final
        def __getitem__(self, i: Integer) -> SetElement:
            r"""Return the ``i``-th element in the chosen enumeration."""
            return cast(
                "SetElement", SageEnumeratedSets.ParentMethods.__getitem__(self, i)
            )

        @override
        @final
        def rank(self, e: SetElement) -> Integer:
            r"""Return the enumeration index of ``e``."""
            return SageEnumeratedSets.ParentMethods.rank(self, e)

        @override
        @final
        def cardinality(self) -> Cardinality:
            if self.is_finite():
                return cast(
                    "Cardinality",
                    SageFiniteEnumeratedSets.ParentMethods.cardinality(self),
                )

            from sage.rings.infinity import infinity

            return infinity

        @override
        @final
        def is_empty(self) -> bool:
            return cast(bool, SageEnumeratedSets.ParentMethods.is_empty(self))

        @override
        @final
        def random_element(self) -> SetElement:
            if self.is_finite():
                return cast(
                    "SetElement",
                    SageFiniteEnumeratedSets.ParentMethods.random_element(self),
                )
            return cast(
                "SetElement",
                SageInfiniteEnumeratedSets.ParentMethods.random_element(self),
            )

        @final
        def map(
            self, f: SetMorphism, name: str | None = None, *, is_injective: bool = True
        ) -> Set:
            r"""Return the image of this enumerated set under ``f``."""
            return cast(
                "Set",
                SageEnumeratedSets.ParentMethods.map(
                    self, f, name=name, is_injective=is_injective
                ),
            )

    class ElementMethods: ...



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
        @final
        def __len__(self) -> int:
            return SageFiniteEnumeratedSets.ParentMethods.__len__(self)

        @override
        @final
        def random_element(self) -> SetElement:
            return cast(
                "SetElement",
                SageFiniteEnumeratedSets.ParentMethods.random_element(self),
            )

    class ElementMethods: ...



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
        @final
        def random_element(self) -> SetElement:
            return cast(
                "SetElement",
                SageInfiniteEnumeratedSets.ParentMethods.random_element(self),
            )

    class ElementMethods: ...
