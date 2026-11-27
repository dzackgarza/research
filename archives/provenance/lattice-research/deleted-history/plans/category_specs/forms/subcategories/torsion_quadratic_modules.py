r"""Finite torsion modules with quadratic forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ...cat import Category_over_base_ring
from ...modules import Modules

if TYPE_CHECKING:
    from ...types import Matrix, RingElement


class TorsionQuadraticModulesCategory(Category_over_base_ring):
    r"""Finite ``ZZ``-modules equipped with a torsion quadratic form.

    Canonical chain: ``FinitelyPresentedModulesOverPID(ZZ).Torsion().WithForms().Quadratic()``.
    """

    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).Torsion(),
            Modules(R).WithForms().Quadratic(),
            Modules(R).FinitelyPresented(),
        ]

    class ParentMethods:
        @final
        def is_torsion_quadratic_module(self) -> bool:
            return True

        @abstract_method
        def gram_matrix_quadratic(self) -> Matrix: ...

        @abstract_method
        def gram_matrix_bilinear(self) -> Matrix: ...

        @abstract_method
        def invariants(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def brown_invariant(self) -> RingElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...


TorsionQuadraticModulesObject = TorsionQuadraticModulesCategory.ParentMethods
TorsionQuadraticModulesElement = TorsionQuadraticModulesCategory.ElementMethods
TorsionQuadraticModulesMorphism = TorsionQuadraticModulesCategory.MorphismMethods
