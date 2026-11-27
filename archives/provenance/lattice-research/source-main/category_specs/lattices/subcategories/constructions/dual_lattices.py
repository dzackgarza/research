r"""Metric-dual lattice construction category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import Category_module
from ...homsets import LatticeHomCategory

if TYPE_CHECKING:
    from ....cat import Category
    from ....types import DiscriminantGroupElement, Lattice, LatticeMorphism, Ring


class DualLatticesCategory(Category_module):
    r"""Metric-dual lattices ``L^\# = {v in L_K | b(v, L) subset R}``.

    Canonical chain: ``Lattices(R).DualLattices()``.

    This is not the category-theoretic Hom-dual construction.  Hom-dual objects
    live under ``Lattices(R).DualObjects()`` or the module ``DualObjects()``
    construction and have evaluation-bearing elements by definition.

    Diagnostics: when the global category diagnostic flag is enabled, implementations
    should emit a category diagnostic if an entry point named ``dual`` or a Sage
    compatibility spelling could make this metric-dual construction look like the
    Hom-dual construction.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"metric-dual lattices over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        from ... import Lattices

        return [Lattices(self.base_ring()).Rational()]

    class ParentMethods:
        @abstractmethod
        def primal_lattice(self) -> Lattice: ...

        @abstractmethod
        def inclusion_morphism(self) -> LatticeMorphism: ...

        @abstractmethod
        def value_ring(self) -> Ring:
            """Return the value ring used to define the metric dual."""
            ...

        @abstractmethod
        def codual(self, *, value_ring: Ring | None = None) -> Lattice:
            """Return the codual lattice with respect to the specified value ring."""
            ...

        @abstractmethod
        def dual_pairing_lattice(self) -> Lattice:
            """Return the lattice carrying the primal-dual pairing."""
            ...

        @abstractmethod
        def projection_to_discriminant_group(self) -> LatticeMorphism:
            """Return the quotient map from the dual lattice to L^vee/L."""
            ...

    class ElementMethods:
        @abstractmethod
        def discriminant_class(self) -> DiscriminantGroupElement:
            r"""Return the image of this metric-dual element in ``L^\#/L``."""
            ...



DualLatticesObject = DualLatticesCategory.ParentMethods
DualLatticesElement = DualLatticesCategory.ElementMethods
DualLatticesMorphism = LatticeHomCategory.ElementMethods
