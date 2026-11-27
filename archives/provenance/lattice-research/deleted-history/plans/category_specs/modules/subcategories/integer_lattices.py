r"""Integral lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, Literal, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Integer, Matrix, Polyhedron, RealNumber, RModuleElement



class _IntegerLattices(Category_over_base_ring):
    r"""Finite-rank integral bilinear modules with lattice algorithms.

    Constructor target: ``Modules(ZZ).Constructors().IntegerLattice(...)``
    refines here as the legacy module-side route toward ``Lattices(ZZ)``.
    """

    @override
    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).Subobjects(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).OverPID(),
            Modules(R).WithForms().Bilinear(),
        ]

    class ParentMethods:
        @override
        @final
        def is_lattice(self) -> bool:
            return True

        @abstract_method
        def gram_matrix(self) -> Matrix: ...

        @abstract_method
        def LLL(
            self,
            delta: RealNumber | None = None,
            eta: RealNumber | None = None,
            algorithm: str = "fpLLL:wrapper",
            fp: str | None = None,
            prec: Integer = 0,
            early_red: bool = False,
            use_givens: bool = False,
            use_siegel: bool = False,
            transformation: bool = False,
        ) -> Matrix: ...

        @abstract_method
        def BKZ(
            self,
            delta: RealNumber | None = None,
            algorithm: str = "fpLLL",
            fp: str | None = None,
            block_size: Integer = 10,
            prune: Integer = 0,
            use_givens: bool = False,
            precision: Integer = 0,
            proof: bool | None = None,
        ) -> Matrix: ...

        @abstract_method
        def shortest_vector(
            self,
            update_reduced_basis: bool = True,
            algorithm: Literal["fplll", "pari"] = "fplll",
        ) -> RModuleElement: ...

        @abstract_method
        def voronoi_cell(self, radius: RealNumber | None = None) -> Polyhedron: ...

    class ElementMethods: ...
    class MorphismMethods: ...
