r"""Sage-backed module family category."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Matrix, RingElement, RModule, RModuleElement, RModuleMorphism

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


class _FinitelyGeneratedPIDQuotientModules(Category_over_base_ring):
    r"""Sage ``FGP_Module_class`` objects represented as ``V/W`` over a PID."""

    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).FinitelyPresented(),
            Modules(R).OverPID(),
        ]

    @final
    def __contains__(self, M: Any) -> bool:
        from sage.modules.fg_pid.fgp_module import FGP_Module_class

        return isinstance(M, FGP_Module_class)

    class ParentMethods:
        @abstract_method
        def order(self) -> RingElement: ...

        @abstract_method
        def invariant_factors(self) -> Sequence[RingElement]: ...

        @abstract_method
        def free_part(self) -> RModule: ...

        @abstract_method
        def torsion_part(self) -> RModule: ...

        @abstract_method
        def element_from_vector(self, vec: Sequence[RingElement]) -> RModuleElement: ...

        @abstract_method
        def invariants(self, include_ones: bool = False) -> tuple[RingElement, ...]: ...

        @abstract_method
        def smith_form_gens(self) -> tuple[RModuleElement, ...]: ...

        @abstract_method
        def hom(
            self,
            images: RModuleMorphism | Matrix | Sequence[RModuleElement] | Mapping[RModuleElement, RModuleElement],
            codomain: RModule | None = None,
            check: bool = True,
        ) -> RModuleMorphism: ...

        @abstract_method
        def V(self) -> RModule: ...

        @abstract_method
        def W(self) -> RModule: ...

        @abstract_method
        def optimized(self) -> RModule: ...

    class ElementMethods: ...
    class MorphismMethods: ...
