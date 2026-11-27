r"""Slice construction category of set objects over a fixed set."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory
from ....cat.subcategories.constructions.objects_over import structure_codomain, structure_domain

if TYPE_CHECKING:
    from ....types import CategoryObject, Morphism


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Objects ``Y`` equipped with a structure morphism ``Y -> X``.

    Canonical chain: ``Sets().ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"objects over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_object(self) -> CategoryObject:
            r"""Return the base set object of this object-over structure."""
            ...

        @abstract_method
        def structure_map(self) -> Morphism:
            r"""Return the structure map to the base set object."""
            ...

        @override
        @final
        def structure_morphism(self) -> Morphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
    class MorphismMethods: ...
