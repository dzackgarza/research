r"""Finite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast, final, override

from sage.categories.finite_enumerated_sets import (
    FiniteEnumeratedSets as SageFiniteEnumeratedSets,
)
from sage.categories.finite_sets import FiniteSets as SageFiniteSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement

from .. import Sets


class _FiniteSets(CategoryWithAxiom):
    r"""Canonical chain: ``Sets().Finite()``."""

    _base_category_class_and_axiom = (Sets, "Finite")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "finite sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageFiniteSets(), Sets().Countable()]

    @override
    @final
    def __contains__(self, S: Any) -> bool:
        return S in SageFiniteSets() or (S in self.base_category() and S.is_finite())

    class ParentMethods:
        @override
        @final
        def is_finite(self) -> bool:
            return True

        @override
        @final
        def cardinality(self) -> Cardinality:
            return SageFiniteEnumeratedSets.ParentMethods.cardinality(self)

        @final
        def __len__(self) -> int:
            r"""Return the finite cardinality as a Python length."""
            return int(self.cardinality())

        @final
        def random_element(self) -> SetElement:
            r"""Return a random element of this finite set."""
            return cast(
                "SetElement",
                SageFiniteEnumeratedSets.ParentMethods.random_element(self),
            )

    class ElementMethods: ...
