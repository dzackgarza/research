r"""FiniteRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.rings import Rings as SageRings
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings

if TYPE_CHECKING:
    pass


class _FiniteRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Finite()``."""

    _base_category_class_and_axiom = (Rings, "Finite")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "finite rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageRings().Finite(), Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageRings().Finite() or (
            R in self.base_category() and R.is_finite()
        )

    class ParentMethods:
        @override
        @final
        def is_finite(self) -> bool:
            return True

        @abstractmethod
        def cardinality(self) -> Integer: ...

        @abstractmethod
        def order(self) -> Integer: ...

    class ElementMethods: ...
