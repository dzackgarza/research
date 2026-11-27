r"""Overlattice construction category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, TypeAlias

from ....cat import Category_module
from ...homsets import LatticeHomCategory

if TYPE_CHECKING:
    from ....cat import Category
    from ....types import Cardinality, Lattice, LatticeMorphism


class OverlatticesCategory(Category_module):
    r"""Overlattices of a lattice inside its rational span.

    Canonical chain: ``Lattices(R).Overlattices(L)``.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"overlattices over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        from ... import Lattices

        return [Lattices(self.base_ring()).Rational()]

    class ParentMethods:
        @abstractmethod
        def base_lattice(self) -> Lattice: ...

        @abstractmethod
        def base_inclusion(self) -> LatticeMorphism: ...

        @abstractmethod
        def index(self) -> Cardinality: ...

        @abstractmethod
        def glue_subgroup(self) -> object:
            """Return the subgroup of the base discriminant group defining this overlattice."""
            ...

        @abstractmethod
        def isotropic_subgroup(self) -> object:
            """Return the isotropic subgroup defining this integral overlattice."""
            ...

        @abstractmethod
        def discriminant_form(self) -> object:
            """Return the discriminant form of this overlattice."""
            ...

        @abstractmethod
        def preimage_of_subgroup(self, H: object) -> Lattice:
            """Return the overlattice preimage of a discriminant-group subgroup."""
            ...

        @abstractmethod
        def is_integral(self) -> bool:
            """Return whether the induced Gram matrix is integral."""
            ...

        @abstractmethod
        def is_even(self) -> bool:
            """Return whether the induced quadratic form is even."""
            ...

    class ElementMethods: ...



OverlatticesObject : TypeAlias = OverlatticesCategory.ParentMethods
OverlatticesElement : TypeAlias = OverlatticesCategory.ElementMethods
OverlatticesMorphism : TypeAlias = LatticeHomCategory.ElementMethods
