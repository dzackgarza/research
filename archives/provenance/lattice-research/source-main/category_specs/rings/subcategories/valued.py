r"""ValuedRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, cast, final, override

from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ...utils import with_axiom
from .. import Rings

if TYPE_CHECKING:
    from ...types import (
        RingElement,
        Valuation,
    )


class _ValuedRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().WithValuation()``."""

    _base_category_class_and_axiom = (Rings, "WithValuation")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "valued rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_valued_ring()

    DiscretelyValued = LazyImport(
        "category_specs.rings.subcategories.discrete_valuation_ring",
        "_DiscreteValuationRings",
    )

    class SubcategoryMethods:
        @final
        def DiscretelyValued(self) -> Category:
            return cast(Category, with_axiom(self, "DiscretelyValued"))

    class ParentMethods:
        @override
        @final
        def is_valued_ring(self) -> bool:
            return True

        @abstractmethod
        def valuation(self) -> Valuation: ...

        @abstractmethod
        def roots_of_unity(self) -> list[RingElement]: ...

    class ElementMethods: ...
