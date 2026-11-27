r"""Sage-backed module family category."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Cardinality, Matrix, Ring, RingElement, RModule, RModuleElement, SubModule

_FreeModulesWithStandardBasis = LazyImport("category_specs.modules.subcategories.free_modules_with_standard_basis", "_FreeModulesWithStandardBasis")
_FreeModulesOverIntegralDomains = LazyImport("category_specs.modules.subcategories.free_modules_over_integral_domains", "_FreeModulesOverIntegralDomains")
_FreeModulesOverPIDs = LazyImport("category_specs.modules.subcategories.free_modules_over_pids", "_FreeModulesOverPIDs")
_VectorSpaces = LazyImport("category_specs.modules.subcategories.vector_spaces", "_VectorSpaces")
_RealDoubleVectorSpaces = LazyImport("category_specs.modules.subcategories.real_double_vector_spaces", "_RealDoubleVectorSpaces")
_ComplexDoubleVectorSpaces = LazyImport("category_specs.modules.subcategories.complex_double_vector_spaces", "_ComplexDoubleVectorSpaces")
_VectorSubspaces = LazyImport("category_specs.modules.subcategories.vector_subspaces", "_VectorSubspaces")
_VectorSubspacesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.vector_subspaces_with_ordered_generating_set", "_VectorSubspacesWithOrderedGeneratingSet")
_VectorSpaceQuotients = LazyImport("category_specs.modules.subcategories.vector_space_quotients", "_VectorSpaceQuotients")
_FreeQuadraticModules = LazyImport("category_specs.modules.subcategories.free_quadratic_modules", "_FreeQuadraticModules")
_FreeModuleSubmodules = LazyImport("category_specs.modules.subcategories.free_module_submodules", "_FreeModuleSubmodules")
_FreeModuleSubmodulesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.free_module_submodules_with_ordered_generating_set", "_FreeModuleSubmodulesWithOrderedGeneratingSet")
_SubmodulesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.submodules_with_ordered_generating_set", "_SubmodulesWithOrderedGeneratingSet")
_QuotientModulesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.quotient_modules_with_ordered_generating_set", "_QuotientModulesWithOrderedGeneratingSet")
_FreeModuleQuotients = LazyImport("category_specs.modules.subcategories.free_module_quotients", "_FreeModuleQuotients")
_RepresentationModules = LazyImport("category_specs.modules.subcategories.representation_modules", "_RepresentationModules")
_FiniteRankFreeModules = LazyImport("category_specs.modules.subcategories.finite_rank_free_modules", "_FiniteRankFreeModules")
_FinitelyGeneratedPIDQuotientModules = LazyImport("category_specs.modules.subcategories.finitely_generated_pid_quotient_modules", "_FinitelyGeneratedPIDQuotientModules")
_FreeGradedModules = LazyImport("category_specs.modules.subcategories.free_graded_modules", "_FreeGradedModules")
_FinitelyPresentedGradedModules = LazyImport("category_specs.modules.subcategories.finitely_presented_graded_modules", "_FinitelyPresentedGradedModules")
_OreModules = LazyImport("category_specs.modules.subcategories.ore_modules", "_OreModules")
_IntegerLattices = LazyImport("category_specs.modules.subcategories.integer_lattices", "_IntegerLattices")
_TorsionQuadraticModules = LazyImport("category_specs.modules.subcategories.torsion_quadratic_modules", "_TorsionQuadraticModules")
_RingObjectsAsModules = LazyImport("category_specs.modules.subcategories.ring_objects_as_modules", "_RingObjectsAsModules")


class _VectorSpaces(Category_over_base_ring):
    r"""Sage vector spaces ``VectorSpace(K, n)`` and ``K^n`` for fields K."""

    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).Free().FiniteRank(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).FinitelyPresented(),
            Modules(R).OverIntegralDomain(),
            Modules(R).OverPID(),
            Modules(R).OverField(),
        ]

    @final
    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import FreeModule_ambient_field

        return isinstance(M, FreeModule_ambient_field)

    class ParentMethods:
        @abstract_method
        def dimension(self) -> Cardinality: ...

        @abstract_method
        def linear_dependence(
            self,
            vectors: Sequence[RModuleElement],
            zeros: Literal["left", "right"] = "left",
            check: bool = True,
        ) -> list[RModuleElement]: ...

        @abstract_method
        def basis_matrix(self, ring: Ring | None = None) -> Matrix: ...

        @abstract_method
        def matrix(self) -> Matrix: ...

        @abstract_method
        def subspace(
            self,
            gens: RModule | Matrix | Sequence[RModuleElement] | Sequence[Sequence[RingElement]],
            check: bool = True,
            already_echelonized: bool = False,
        ) -> SubModule: ...

        @abstract_method
        def quotient_module(
            self,
            subspace: SubModule | RModule | Matrix | Sequence[RModuleElement] | Sequence[Sequence[RingElement]],
            check: bool = True,
        ) -> RModule: ...

    class ElementMethods: ...
    class MorphismMethods: ...
