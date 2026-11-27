r"""Slice construction category of modules under a fixed module."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory
from ....cat.subcategories.constructions.objects_over import (
    structure_codomain,
    structure_domain,
)

if TYPE_CHECKING:
    from ....types import RModMorphism, RModule


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Modules ``N`` equipped with an ``R``-linear map ``M -> N``.

    Canonical chain: ``Modules(R).ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"modules under {self.base()}"

    class ParentMethods:
        @abstractmethod
        def structure_module(self) -> RModule: ...

        @abstractmethod
        def structure_map(self) -> RModMorphism: ...

        @final
        def structure_morphism(self) -> RModMorphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
