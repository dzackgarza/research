r"""Finite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.finite_sets import FiniteSets as SageFiniteSets
from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement

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
        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @final
        def __len__(self) -> Integer:
            r"""Return the finite cardinality as a Python length."""
            return int(self.cardinality())

        @abstract_method
        def random_element(self) -> SetElement:
            r"""Return a random element of this finite set."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
