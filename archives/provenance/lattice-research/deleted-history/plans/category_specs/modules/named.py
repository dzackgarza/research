r"""Named Sage module constructors and their concrete method surfaces."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.misc.abstract_method import abstract_method

from ..utils import refine_category

if TYPE_CHECKING:
    from typing import Protocol, TypeVar

    from sage.categories.morphism import Morphism
    from sage.matrix.matrix0 import Matrix
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer
    from sage.structure.element import Element
    from sage.structure.parent import Parent

    Cardinality = Integer | InfinityElement
    RingElement = Element
    RModule = Parent
    RModuleElement = Element
    RModuleMorphism = Morphism
    SubModule = Parent

    class _RefinableModuleLike(Protocol):
        def base_ring(self) -> Parent: ...

        def _refine_category_(self, categories: Sequence[Category]) -> None: ...

    RefinedModuleT = TypeVar("RefinedModuleT", bound=_RefinableModuleLike)


def Modules(*args, **kwds):
    from . import Modules as _Modules

    return _Modules(*args, **kwds)


def _refine_named_module(M: RefinedModuleT, *categories: Category) -> RefinedModuleT:
    R = M.base_ring()
    return refine_category(M, [Modules(R), *categories])


def _joined_super_categories(*categories: Category) -> list[Category]:
    return Category.join(categories, as_list=True)


class _NamedModuleCategory(Category_over_base_ring):
    r"""Base class for Sage-backed named module implementation categories."""


class _NamedModules:
    r"""Constructor collector for Sage's named module entry points."""

    def __init__(self, category):
        self._category = category

    def __repr__(self) -> str:
        return f"named module constructors over {self.base_ring()}"

    def category(self):
        return self._category

    def base_ring(self):
        return self.category().base_ring()

    def FreeModulesWithStandardBasis(self):
        return _FreeModulesWithStandardBasis(self.base_ring())

    def FreeModulesOverIntegralDomains(self):
        return _FreeModulesOverIntegralDomains(self.base_ring())

    def FreeModulesOverPIDs(self):
        return _FreeModulesOverPIDs(self.base_ring())

    def VectorSpaces(self):
        return _VectorSpaces(self.base_ring())

    def RealDoubleVectorSpaces(self):
        return _RealDoubleVectorSpaces(self.base_ring())

    def ComplexDoubleVectorSpaces(self):
        return _ComplexDoubleVectorSpaces(self.base_ring())

    def VectorSubspaces(self):
        return _VectorSubspaces(self.base_ring())

    def VectorSubspacesWithOrderedGeneratingSet(self):
        return _VectorSubspacesWithOrderedGeneratingSet(self.base_ring())

    def VectorSpaceQuotients(self):
        return _VectorSpaceQuotients(self.base_ring())

    def FreeQuadraticModules(self):
        return _FreeQuadraticModules(self.base_ring())

    def CombinatorialFreeModules(self):
        return _CombinatorialFreeModules(self.base_ring())

    def FiniteRankFreeModules(self):
        return _FiniteRankFreeModules(self.base_ring())

    def FreeModuleSubmodules(self):
        return _FreeModuleSubmodules(self.base_ring())

    def FreeModuleSubmodulesWithOrderedGeneratingSet(self):
        return _FreeModuleSubmodulesWithOrderedGeneratingSet(self.base_ring())

    def SubmodulesWithOrderedGeneratingSet(self):
        return _SubmodulesWithOrderedGeneratingSet(self.base_ring())

    def QuotientModulesWithOrderedGeneratingSet(self):
        return _QuotientModulesWithOrderedGeneratingSet(self.base_ring())

    def FreeModuleQuotients(self):
        return _FreeModuleQuotients(self.base_ring())

    def RepresentationModules(self):
        return _RepresentationModules(self.base_ring())

    def FinitelyGeneratedPIDQuotientModules(self):
        return _FinitelyGeneratedPIDQuotientModules(self.base_ring())

    def FreeGradedModules(self):
        return _FreeGradedModules(self.base_ring())

    def FinitelyPresentedGradedModules(self):
        return _FinitelyPresentedGradedModules(self.base_ring())

    def OreModules(self):
        return _OreModules(self.base_ring())

    def IntegerLattices(self):
        return _IntegerLattices(self.base_ring())

    def TorsionQuadraticModules(self):
        return _TorsionQuadraticModules(self.base_ring())

    def RingObjectsAsModules(self):
        return _RingObjectsAsModules(self.base_ring())

    def _category_for_free_module(self, M: RModule) -> Category:
        if M in self.FreeQuadraticModules():
            return self.FreeQuadraticModules()
        if M in self.VectorSpaceQuotients():
            return self.VectorSpaceQuotients()
        if M in self.VectorSubspacesWithOrderedGeneratingSet():
            return self.VectorSubspacesWithOrderedGeneratingSet()
        if M in self.VectorSubspaces():
            return self.VectorSubspaces()
        if M in self.RealDoubleVectorSpaces():
            return self.RealDoubleVectorSpaces()
        if M in self.ComplexDoubleVectorSpaces():
            return self.ComplexDoubleVectorSpaces()
        if M in self.FreeModuleSubmodulesWithOrderedGeneratingSet():
            return self.FreeModuleSubmodulesWithOrderedGeneratingSet()
        if M in self.FreeModuleSubmodules():
            return self.FreeModuleSubmodules()
        if M in self.VectorSpaces():
            return self.VectorSpaces()
        from sage.categories.integral_domains import IntegralDomains
        from sage.categories.principal_ideal_domains import PrincipalIdealDomains

        R = self.base_ring()
        if R in PrincipalIdealDomains():
            return self.FreeModulesOverPIDs()
        if R in IntegralDomains():
            return self.FreeModulesOverIntegralDomains()
        return self.FreeModulesWithStandardBasis()

    def _category_for_quotient_module(self, M: RModule) -> Category:
        if M in self.VectorSpaceQuotients():
            return self.VectorSpaceQuotients()
        if M in self.FreeModuleQuotients():
            return self.FreeModuleQuotients()
        if M in self.FinitelyGeneratedPIDQuotientModules():
            return self.FinitelyGeneratedPIDQuotientModules()
        return self._category_for_free_module(M)

    def FreeModule(self, *args, **kwds):
        from sage.modules.free_module import FreeModule as SageFreeModule

        M = SageFreeModule(self.base_ring(), *args, **kwds)
        if M in self.CombinatorialFreeModules():
            category = self.CombinatorialFreeModules()
        elif M in self.FiniteRankFreeModules():
            category = self.FiniteRankFreeModules()
        else:
            category = self._category_for_free_module(M)
        return _refine_named_module(M, category)

    def VectorSpace(self, *args, **kwds):
        from sage.modules.free_module import VectorSpace as SageVectorSpace

        M = SageVectorSpace(self.base_ring(), *args, **kwds)
        return _refine_named_module(M, self._category_for_free_module(M))

    def FreeQuadraticModule(self, rank, inner_product_matrix, **kwds):
        from sage.modules.free_quadratic_module import FreeQuadraticModule

        M = FreeQuadraticModule(
            self.base_ring(),
            rank,
            inner_product_matrix,
            **kwds,
        )
        return _refine_named_module(M, self.FreeQuadraticModules())

    def span(self, gens, check=True, already_echelonized=False):
        from sage.modules.free_module import span as sage_span

        M = sage_span(
            gens,
            self.base_ring(),
            check=check,
            already_echelonized=already_echelonized,
        )
        return _refine_named_module(M, self._category_for_free_module(M))

    def CombinatorialFreeModule(self, basis_keys, **kwds):
        from sage.combinat.free_module import CombinatorialFreeModule

        M = CombinatorialFreeModule(self.base_ring(), basis_keys, **kwds)
        return _refine_named_module(M, self.CombinatorialFreeModules())

    def FiniteRankFreeModule(self, rank, **kwds):
        from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule

        M = FiniteRankFreeModule(self.base_ring(), rank, **kwds)
        return _refine_named_module(M, self.FiniteRankFreeModules())

    def quotient_of_free_modules(self, V, W):
        M = V / W
        return _refine_named_module(M, self._category_for_quotient_module(M))

    def quotient_module(self, module, submodule, *args, **kwds):
        M = module.quotient_module(submodule, *args, **kwds)
        return _refine_named_module(M, self._category_for_quotient_module(M))

    def FPModule(self, *args, **kwds):
        from sage.modules.fp_graded.module import FPModule

        M = FPModule(*args, **kwds)
        return _refine_named_module(M, self.FinitelyPresentedGradedModules())

    def FreeGradedModule(self, *args, **kwds):
        from sage.modules.fp_graded.free_module import FreeGradedModule

        M = FreeGradedModule(*args, **kwds)
        return _refine_named_module(M, self.FreeGradedModules())

    def OreQuotientModule(self, ore_polynomial_ring, polynomial):
        M = ore_polynomial_ring.quotient_module(polynomial)
        return _refine_named_module(M, self.OreModules())

    def IntegerLattice(self, basis, lll_reduce=True):
        from sage.modules.free_module_integer import IntegerLattice

        M = IntegerLattice(basis, lll_reduce=lll_reduce)
        return _refine_named_module(M, self.IntegerLattices())

    def TorsionQuadraticForm(self, q):
        from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

        M = TorsionQuadraticForm(q)
        return _refine_named_module(M, self.TorsionQuadraticModules())

    def ring_as_rank_one_module(self, ring=None):
        R = self.base_ring() if ring is None else ring
        M = Modules(R).NamedModules().FreeModule(1)
        return _refine_named_module(M, self.FreeModulesWithStandardBasis())

    def ideal_as_submodule(self, ideal):
        return _refine_named_module(ideal, Modules(ideal.ring()).RIdeals())

    def invertible_ideal_as_projective_submodule(self, ideal):
        R = ideal.ring()
        return _refine_named_module(ideal, Modules(R).RIdeals(), Modules(R).Projective())

    def polynomial_ring_as_module(self, *args, **kwds):
        from ..rings import Rings

        S = Rings().NamedRings().PolynomialRing(self.base_ring(), *args, **kwds)
        return _refine_named_module(S, self.RingObjectsAsModules())

    def power_series_ring_as_module(self, *args, **kwds):
        from ..rings import Rings

        S = Rings().NamedRings().PowerSeriesRing(self.base_ring(), *args, **kwds)
        return _refine_named_module(S, self.RingObjectsAsModules())

    def laurent_series_ring_as_module(self, *args, **kwds):
        from ..rings import Rings

        S = Rings().NamedRings().LaurentSeriesRing(self.base_ring(), *args, **kwds)
        return _refine_named_module(S, self.RingObjectsAsModules())

    def puiseux_series_ring_as_module(self, *args, **kwds):
        from ..rings import Rings

        S = Rings().NamedRings().PuiseuxSeriesRing(self.base_ring(), *args, **kwds)
        return _refine_named_module(S, self.RingObjectsAsModules())

    def matrix_ring_as_module(self, n, *args, **kwds):
        from ..rings import Rings

        S = Rings().NamedRings().MatrixRing(self.base_ring(), n, *args, **kwds)
        return _refine_named_module(S, self.RingObjectsAsModules())


class _FreeModulesWithStandardBasis(_NamedModuleCategory):
    r"""Sage ``FreeModule(R, n, with_basis='standard')`` objects."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free().FiniteRank(),
            Modules(R).FinitelyPresented(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import FreeModule_ambient

        return isinstance(M, FreeModule_ambient)

    class ParentMethods:
        @abstract_method
        def degree(self): ...

        @abstract_method
        def rank(self) -> Cardinality: ...

        @abstract_method
        def basis(self): ...

        @abstract_method
        def gens(self): ...

        @abstract_method
        def echelonized_basis(self, *args, **kwds): ...

        @abstract_method
        def basis_matrix(self, *args, **kwds): ...

        @abstract_method
        def span(self, gens, *args, **kwds) -> SubModule: ...

        @abstract_method
        def submodule(self, gens, *args, **kwds) -> SubModule: ...

        @abstract_method
        def linear_combination_of_basis(self, coeffs): ...

        @abstract_method
        def coordinate_vector(self, v, *args, **kwds): ...

    class ElementMethods:
        @abstract_method
        def list(self): ...

        @abstract_method
        def vector(self): ...

        @abstract_method
        def degree(self): ...

        @abstract_method
        def support(self): ...


class _FreeModulesOverIntegralDomains(_NamedModuleCategory):
    r"""Standard-basis free modules over integral domains."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free().FiniteRank(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).FinitelyPresented(),
            Modules(R).OverIntegralDomain(),
        )

    class ParentMethods:
        @abstract_method
        def intersection(self, other) -> SubModule: ...

        @abstract_method
        def saturation(self, *args, **kwds) -> SubModule: ...


class _FreeModulesOverPIDs(_NamedModuleCategory):
    r"""Standard-basis free modules over principal ideal domains."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free().FiniteRank(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).FinitelyPresented(),
            Modules(R).OverIntegralDomain(),
            Modules(R).OverPID(),
        )

    class ParentMethods:
        @abstract_method
        def quotient_module(self, submodule, *args, **kwds) -> RModule: ...

        @abstract_method
        def index_in(self, other) -> Cardinality: ...


class _VectorSpaces(_NamedModuleCategory):
    r"""Sage vector spaces ``VectorSpace(K, n)`` and ``K^n`` for fields K."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free().FiniteRank(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).FinitelyPresented(),
            Modules(R).OverIntegralDomain(),
            Modules(R).OverPID(),
            Modules(R).OverField(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import FreeModule_ambient_field

        return isinstance(M, FreeModule_ambient_field)

    class ParentMethods:
        @abstract_method
        def dimension(self): ...

        @abstract_method
        def linear_dependence(self, vectors, *args, **kwds): ...

        @abstract_method
        def basis_matrix(self, *args, **kwds): ...

        @abstract_method
        def matrix(self, *args, **kwds): ...

        @abstract_method
        def subspace(self, gens, *args, **kwds) -> SubModule: ...

        @abstract_method
        def quotient_module(self, subspace, *args, **kwds) -> RModule: ...


class _RealDoubleVectorSpaces(_NamedModuleCategory):
    r"""Sage ``RDF^n`` vector spaces backed by real double vectors."""

    def super_categories(self):
        R = self.base_ring()
        return [_VectorSpaces(R)]

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import RealDoubleVectorSpace_class

        return isinstance(M, RealDoubleVectorSpace_class) and M.base_ring() == self.base_ring()

    class ParentMethods:
        @abstract_method
        def coordinates(self, v): ...


class _ComplexDoubleVectorSpaces(_NamedModuleCategory):
    r"""Sage ``CDF^n`` vector spaces backed by complex double vectors."""

    def super_categories(self):
        R = self.base_ring()
        return [_VectorSpaces(R)]

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import ComplexDoubleVectorSpace_class

        return isinstance(M, ComplexDoubleVectorSpace_class) and M.base_ring() == self.base_ring()

    class ParentMethods:
        @abstract_method
        def coordinates(self, v): ...


class _VectorSubspaces(_NamedModuleCategory):
    r"""Embedded Sage vector subspaces created by ``span`` and ``subspace``."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(_VectorSpaces(R), Modules(R).Subobjects())

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import FreeModule_submodule_field

        return isinstance(M, FreeModule_submodule_field) and M.base_ring() == self.base_ring()

    class ParentMethods:
        @abstract_method
        def ambient_vector_space(self) -> RModule: ...

        @abstract_method
        def complement(self) -> RModule: ...

        @abstract_method
        def is_subspace(self, other) -> bool: ...


class _VectorSubspacesWithOrderedGeneratingSet(_NamedModuleCategory):
    r"""Embedded vector subspaces with an ordered Sage basis."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            _VectorSubspaces(R),
            Modules(R).WithOrderedGeneratingSet(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import FreeModule_submodule_with_basis_field

        return isinstance(M, FreeModule_submodule_with_basis_field) and M.base_ring() == self.base_ring()

    class ParentMethods:
        @abstract_method
        def basis_matrix(self, *args, **kwds) -> Matrix: ...

        @abstract_method
        def coordinate_module(self, *args, **kwds): ...


class _VectorSpaceQuotients(_NamedModuleCategory):
    r"""Quotients ``V/W`` of Sage vector spaces."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(_VectorSpaces(R), Modules(R).Quotients())

    def __contains__(self, M: Any) -> bool:
        from sage.modules.quotient_module import FreeModule_ambient_field_quotient

        return isinstance(M, FreeModule_ambient_field_quotient) and M.base_ring() == self.base_ring()

    class ParentMethods:
        @abstract_method
        def quotient_map(self) -> RModuleMorphism: ...

        @abstract_method
        def lift_map(self) -> RModuleMorphism: ...

        @abstract_method
        def lift(self, x) -> RModuleElement: ...

        @abstract_method
        def cover(self) -> RModule: ...

        @abstract_method
        def relations(self) -> RModule: ...


class _FreeQuadraticModules(_NamedModuleCategory):
    r"""Sage free modules with an explicit inner-product matrix."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free().FiniteRank(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).FinitelyPresented(),
            Modules(R).WithForms().Bilinear(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_quadratic_module import FreeQuadraticModule_generic

        return isinstance(M, FreeQuadraticModule_generic)

    class ParentMethods:
        @abstract_method
        def inner_product_matrix(self, *args, **kwds) -> Matrix: ...

        @abstract_method
        def gram_matrix(self) -> Matrix: ...

        @abstract_method
        def uses_ambient_inner_product(self) -> bool: ...

    class ElementMethods:
        @abstract_method
        def inner_product(self, other) -> RingElement: ...

        @abstract_method
        def dot_product(self, other) -> RingElement: ...


class _FreeModuleSubmodules(_NamedModuleCategory):
    r"""Submodules created by ``M.submodule(...)`` or ``span(...)``."""

    def super_categories(self):
        R = self.base_ring()
        return [Modules(R).Subobjects()]

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import FreeModule_submodule_pid

        return isinstance(M, FreeModule_submodule_pid)

    class ParentMethods:
        @abstract_method
        def ambient_module(self) -> RModule: ...

        @abstract_method
        def basis_matrix(self, *args, **kwds) -> Matrix: ...

        @abstract_method
        def echelon_basis_matrix(self, *args, **kwds) -> Matrix: ...

        @abstract_method
        def echelonized_basis(self, *args, **kwds): ...

        @abstract_method
        def coordinate_module(self, *args, **kwds): ...

        @abstract_method
        def saturation(self, *args, **kwds) -> SubModule: ...


class _FreeModuleSubmodulesWithOrderedGeneratingSet(_NamedModuleCategory):
    r"""Sage submodules with a user-specified ordered generating set."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Subobjects(),
            Modules(R).WithOrderedGeneratingSet(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.free_module import FreeModule_submodule_with_basis_pid

        return isinstance(M, FreeModule_submodule_with_basis_pid)

    class ParentMethods:
        @abstract_method
        def user_basis(self): ...

        @abstract_method
        def basis_matrix(self, *args, **kwds) -> Matrix: ...


class _CombinatorialFreeModules(_NamedModuleCategory):
    r"""Sage ``CombinatorialFreeModule`` objects with arbitrary basis keys."""

    def super_categories(self):
        from sage.categories.modules_with_basis import ModulesWithBasis

        R = self.base_ring()
        return _joined_super_categories(
            ModulesWithBasis(R),
            Modules(R).Free(),
            Modules(R).WithOrderedGeneratingSet(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.combinat.free_module import CombinatorialFreeModule

        return isinstance(M, CombinatorialFreeModule)

    class ParentMethods:
        @abstract_method
        def monomial(self, i) -> RModuleElement: ...

        @abstract_method
        def linear_combination(self, iter_of_elements_coeff, *args, **kwds): ...

    class ElementMethods:
        @abstract_method
        def monomial_coefficients(self, copy=True): ...


class _SubmodulesWithOrderedGeneratingSet(_NamedModuleCategory):
    r"""Sage ``SubmoduleWithBasis`` mapped to ordered-generating-set vocabulary."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).Subobjects(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.with_basis.subquotient import SubmoduleWithBasis

        return isinstance(M, SubmoduleWithBasis)

    class ParentMethods:
        @abstract_method
        def ambient(self) -> RModule: ...

        @abstract_method
        def lift(self) -> RModuleMorphism: ...

        @abstract_method
        def reduce(self, x) -> RModuleElement: ...

        @abstract_method
        def echelon_form(self, *args, **kwds): ...

        @abstract_method
        def cokernel_basis_indices(self): ...


class _QuotientModulesWithOrderedGeneratingSet(_NamedModuleCategory):
    r"""Sage ``QuotientModuleWithBasis`` mapped to ordered-generating-set vocabulary."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).Quotients(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.with_basis.subquotient import QuotientModuleWithBasis

        return isinstance(M, QuotientModuleWithBasis)

    class ParentMethods:
        @abstract_method
        def ambient(self) -> RModule: ...

        @abstract_method
        def lift(self) -> RModuleMorphism: ...

        @abstract_method
        def retract(self, x) -> RModuleElement: ...

        @abstract_method
        def quotient_module(self, submodule, *args, **kwds) -> RModule: ...


class _FreeModuleQuotients(_NamedModuleCategory):
    r"""Quotients of ambient free modules by submodules."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Quotients(),
            Modules(R).FinitelyPresented(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.quotient_module import QuotientModule_free_ambient

        return isinstance(M, QuotientModule_free_ambient) and M.base_ring() == self.base_ring()

    class ParentMethods:
        @abstract_method
        def ambient_module(self) -> RModule: ...

        @abstract_method
        def cover(self) -> RModule: ...

        @abstract_method
        def relations(self) -> RModule: ...

        @abstract_method
        def free_cover(self) -> RModule: ...

        @abstract_method
        def free_relations(self) -> RModule: ...


class _RepresentationModules(_NamedModuleCategory):
    r"""Group and semigroup representations implemented with bases."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free(),
            Modules(R).WithOrderedGeneratingSet(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.modules.with_basis.representation import Representation_abstract

        return isinstance(M, Representation_abstract)

    class ParentMethods:
        @abstract_method
        def semigroup(self): ...

        @abstract_method
        def side(self): ...

        @abstract_method
        def algebra(self): ...

        @abstract_method
        def representation_matrix(self, g, *args, **kwds): ...

        @abstract_method
        def invariant_module(self, *args, **kwds) -> RModule: ...

        @abstract_method
        def cell_module(self, *args, **kwds) -> RModule: ...


class _FiniteRankFreeModules(_NamedModuleCategory):
    r"""Basis-free finite-rank free modules for tensor calculus."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Free().FiniteRank(),
            Modules(R).FinitelyPresented(),
        )

    def __contains__(self, M: Any) -> bool:
        from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule

        return isinstance(M, FiniteRankFreeModule)

    class ParentMethods:
        @abstract_method
        def rank(self): ...

        @abstract_method
        def basis(self, *args, **kwds): ...

        @abstract_method
        def bases(self): ...

        @abstract_method
        def default_basis(self): ...

        @abstract_method
        def set_default_basis(self, basis): ...

        @abstract_method
        def tensor_module(self, k, l, *args, **kwds): ...

        @abstract_method
        def exterior_power(self, p): ...

        @abstract_method
        def alternating_form(self, degree, name=None, latex_name=None): ...


class _FinitelyGeneratedPIDQuotientModules(_NamedModuleCategory):
    r"""Sage ``FGP_Module_class`` objects represented as ``V/W`` over a PID."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).FinitelyPresented(),
            Modules(R).OverPID(),
        )

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
        def invariants(self): ...

        @abstract_method
        def smith_form_gens(self): ...

        @abstract_method
        def hom(self, images, *args, **kwds) -> RModuleMorphism: ...

        @abstract_method
        def V(self) -> RModule: ...

        @abstract_method
        def W(self) -> RModule: ...

        @abstract_method
        def optimized(self) -> RModule: ...


class _FreeGradedModules(_NamedModuleCategory):
    r"""Free graded modules over connected graded algebras."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(Modules(R).Free(), Modules(R).Graded())

    class ParentMethods:
        @abstract_method
        def generator_degrees(self): ...

        @abstract_method
        def basis(self, degree=None): ...

        @abstract_method
        def suspension(self, t=1): ...

        @abstract_method
        def hom(self, codomain, values, *args, **kwds) -> RModuleMorphism: ...


class _FinitelyPresentedGradedModules(_NamedModuleCategory):
    r"""Cokernels of maps between free graded modules."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).FinitelyPresented(),
            Modules(R).Graded(),
        )

    class ParentMethods:
        @abstract_method
        def generator_degrees(self): ...

        @abstract_method
        def relations(self): ...

        @abstract_method
        def presentation(self): ...

        @abstract_method
        def free_resolution(self, *args, **kwds): ...

        @abstract_method
        def module_morphism(self, *args, **kwds) -> RModuleMorphism: ...


class _OreModules(_NamedModuleCategory):
    r"""Finite free modules over an Ore polynomial ring quotient."""

    def super_categories(self):
        R = self.base_ring()
        return [Modules(R).Free().FiniteRank()]

    class ParentMethods:
        @abstract_method
        def ore_polynomial_ring(self): ...

        @abstract_method
        def pseudomorphism(self): ...

        @abstract_method
        def companion_matrix(self): ...

        @abstract_method
        def characteristic_polynomial(self): ...

        @abstract_method
        def cyclic_vector(self, *args, **kwds): ...


class _IntegerLattices(_NamedModuleCategory):
    r"""Sage integer lattices, including LLL/BKZ-backed lattice methods."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Subobjects(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).OverPID(),
            Modules(R).WithForms().Bilinear(),
        )

    class ParentMethods:
        @abstract_method
        def gram_matrix(self): ...

        @abstract_method
        def LLL(self, *args, **kwds): ...

        @abstract_method
        def BKZ(self, *args, **kwds): ...

        @abstract_method
        def shortest_vector(self, *args, **kwds): ...

        @abstract_method
        def voronoi_cell(self, *args, **kwds): ...


class _TorsionQuadraticModules(_NamedModuleCategory):
    r"""Finite ``ZZ``-modules equipped with a torsion quadratic form."""

    def super_categories(self):
        R = self.base_ring()
        return _joined_super_categories(
            Modules(R).Torsion(),
            Modules(R).WithForms().Quadratic(),
            Modules(R).FinitelyPresented(),
        )

    class ParentMethods:
        @abstract_method
        def gram_matrix_quadratic(self): ...

        @abstract_method
        def gram_matrix_bilinear(self): ...

        @abstract_method
        def invariants(self): ...

        @abstract_method
        def brown_invariant(self, *args, **kwds): ...


class _RingObjectsAsModules(_NamedModuleCategory):
    r"""Ring objects regarded as modules over their structure ring."""

    def super_categories(self):
        R = self.base_ring()
        return [Modules(R)]

    class ParentMethods:
        @abstract_method
        def structure_ring(self): ...

        @abstract_method
        def structure_map(self, *args, **kwds): ...

        @abstract_method
        def module_generators(self, *args, **kwds): ...
