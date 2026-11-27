r"""Positive-definite lattice algorithms.

This category owns Euclidean enumeration and reduction methods.  Integral,
indefinite lattices must not inherit these methods merely because Sage exposes
some of them on integer-lattice classes.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, cast, final

from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric as SageIntegerSymmetricLattice,
)

from ...cat import CategoryWithAxiom_over_base_ring
from ..chain import LatticesCategory

if TYPE_CHECKING:
    from ...types import Lattice, Polyhedron, RingElement, RModuleElement, SetFamily


class _PositiveDefiniteLattices(CategoryWithAxiom_over_base_ring):
    r"""Positive-definite lattices with Euclidean algorithms.

    Canonical chain: ``Lattices(R).PositiveDefinite()``.
    """

    _base_category_class_and_axiom = (LatticesCategory, "PositiveDefinite")
    _defining_predicates = ("is_positive_definite",)

    class ParentMethods:
        @final
        def is_positive_definite(self) -> bool:
            return True

        @abstractmethod
        def minimum(self) -> RingElement: ...

        @abstractmethod
        def LLL(self) -> Lattice: ...

        @abstractmethod
        def BKZ(self) -> Lattice: ...

        @abstractmethod
        def shortest_vector(self) -> RModuleElement: ...

        @abstractmethod
        def closest_vector(self, target: RModuleElement) -> RModuleElement: ...

        @abstractmethod
        def short_vectors(self, bound: RingElement) -> SetFamily:
            r"""Return vectors ``v`` whose norm ``b(v, v)`` is at most ``bound``."""
            ...

        @final
        def short_vectors_up_to_sign(self, bound: RingElement) -> SetFamily:
            r"""Return representatives for the sign orbits ``{v, -v}``."""
            return SageIntegerSymmetricLattice.short_vectors(
                cast(SageIntegerSymmetricLattice, self), bound, up_to_sign_flag=True
            )

        @abstractmethod
        def voronoi_cell(self) -> Polyhedron: ...

    class ElementMethods: ...
