r"""Slice construction category of lattices under a fixed lattice."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory
from ....cat.subcategories.constructions.objects_over import (
    structure_codomain,
    structure_domain,
)

if TYPE_CHECKING:
    from ....types import Lattice, LatticeMorphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Lattices ``M`` equipped with a lattice morphism ``L -> M``.

    Canonical chain: ``Lattices(R).ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @final
    def _repr_object_names(self) -> str:
        return f"lattices under {self.base()}"

    class ParentMethods:
        @abstractmethod
        def structure_lattice(self) -> Lattice: ...

        @abstractmethod
        def structure_map(self) -> LatticeMorphism: ...

        @final
        def structure_morphism(self) -> LatticeMorphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
