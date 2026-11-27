r"""Slice construction category of posets over a fixed poset."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory
from ....cat.subcategories.constructions.objects_over import structure_codomain, structure_domain

if TYPE_CHECKING:
    from ....types import Poset, PosetMorphism


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Posets ``Q`` equipped with an order-preserving map ``Q -> P``.

    Canonical chain: ``Posets().ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"posets over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_poset(self) -> Poset:
            r"""Return the target poset of this object-over structure."""
            ...

        @abstract_method
        def structure_map(self) -> PosetMorphism:
            r"""Return the order-preserving map from this poset to the target."""
            ...

        @override
        @final
        def structure_morphism(self) -> PosetMorphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
    class MorphismMethods: ...
