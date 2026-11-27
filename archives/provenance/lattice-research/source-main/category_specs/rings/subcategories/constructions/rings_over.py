r"""Rings over a fixed ambient ring."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ....cat import (
    Cat,
    Category,
    Category_over_base_ring,
    RegressiveCovariantConstructionCategory,
)
from ....cat.subcategories.constructions.objects_over import (
    structure_codomain,
    structure_domain,
)

if TYPE_CHECKING:
    from ....types import Ring, RingMorphism


class _RingsOver(RegressiveCovariantConstructionCategory, Category_over_base_ring):
    r"""Canonical chain: ``Rings().RingsOver(R)``."""

    _functor_category = "RingsOver"

    @classmethod
    @final
    def default_super_categories(
        cls, category: Category, ambient: Ring
    ) -> list[Category]:
        from ... import Rings

        return Cat().join(
            [
                Rings(),
                super().default_super_categories(category, ambient),
            ]
        )

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"rings over {self.base_ring()}"

    class ParentMethods:
        @abstractmethod
        def base_ring(self) -> Ring: ...

        @abstractmethod
        def coerce_map_from(self, other: Ring) -> RingMorphism: ...

        @final
        def structure_ring(self) -> Ring:
            return self.base_ring()

        @final
        def structure_map(self) -> RingMorphism:
            return self.structure_ring().coerce_map_from(self)

        @final
        def structure_morphism(self) -> RingMorphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
