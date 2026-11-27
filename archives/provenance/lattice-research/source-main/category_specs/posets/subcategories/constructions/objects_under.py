r"""Coslice construction category of posets under a fixed poset."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory
from ....cat.subcategories.constructions.objects_over import (
    structure_codomain,
    structure_domain,
)

if TYPE_CHECKING:
    from ....types import Poset, PosetMorphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Posets ``Q`` equipped with an order-preserving map ``P -> Q``.

    Canonical chain: ``Posets().ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"posets under {self.base()}"

    class ParentMethods:
        @abstractmethod
        def structure_poset(self) -> Poset:
            r"""Return the source poset of this object-under structure."""
            ...

        @abstractmethod
        def structure_map(self) -> PosetMorphism:
            r"""Return the order-preserving map from the source to this poset."""
            ...

        @final
        def structure_morphism(self) -> PosetMorphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
