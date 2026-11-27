r"""Rings under a fixed structure ring."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ....cat import (
    Cat,
    Category,
    Category_over_base_ring,
    CovariantConstructionCategory,
)
from ....cat.subcategories.constructions.objects_over import (
    structure_codomain,
    structure_domain,
)

if TYPE_CHECKING:
    from ....types import Ring, RingMorphism


class _RingsUnder(CovariantConstructionCategory, Category_over_base_ring):
    r"""Canonical chain: ``Rings().RingsUnder(R)``."""

    _functor_category = "RingsUnder"

    @classmethod
    @final
    def default_super_categories(cls, category: Category, base: Ring) -> list[Category]:
        from ... import Rings

        return Cat().join(
            [
                category,
                Rings(),
                super().default_super_categories(category, base),
            ]
        )

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"rings under {self.base_ring()}"

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
            return self.coerce_map_from(self.structure_ring())

        @final
        def structure_morphism(self) -> RingMorphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
