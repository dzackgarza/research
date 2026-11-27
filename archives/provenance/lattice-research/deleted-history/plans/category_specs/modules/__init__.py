r"""Spec for the (R,R)-bimodule category ``Modules(R)``.

Naming convention — Sage vs. ours:
    Modules(R)          -- our category of R-modules (this file)
    SageModules(R)      -- sage.categories.modules.Modules(R)
    CommutativeRings()  -- our Rings().Commutative()
    SageCommutativeRings -- sage.categories.commutative_rings.CommutativeRings
    (similarly for Fields, IntegralDomains, PrincipalIdealDomains, etc.)

Canonical type aliases used throughout this package:
    Matrix, vector            -- Sage primitives
    Category                  -- a Sage category
    RMod                      -- the Modules(R) category itself
    RModule                   -- an object M in RMod
    RModuleElement            -- an element in some M
    RModHom                   -- Hom_R(M, N) for some M, N in RMod
    RModMorphism              -- an element in some Hom_R(M, N)
    RModEnd                   -- End_R(M) for some M in RMod
    RModEndomorphism          -- an element in some End_R(M)
    RModAut                   -- Aut_R(M) for some M in RMod
    RModAutomorphism          -- an element in some Aut_R(M)
    SubModule                 -- an element in RMod.Subobjects()
    QuotientModule            -- an element in RMod.Quotients()
    DualModule                -- M^* for some RModule M
    Rings                     -- our promoted category of rings
    Ring                      -- an object in Rings
    Ideals                    -- our promoted category of ideals of R as a
                                 subcategory of Modules(R).Subobjects()
    Ideal                     -- an object in Ideals
    RingMorphism              -- a morphism in Rings
    RingEndomorphism          -- an endomorphism in Rings
    RingAutomorphism          -- an automorphism in Rings
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, final, overload, override

from sage.categories.bimodules import Bimodules as SageBimodules
from sage.categories.tensor import tensor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import (
    Cat,
    Category,
    Category_module,
    DualObjectsCategory,
    FilteredModulesCategory,
    GradedModulesCategory,
    SuperModulesCategory,
    TensorProductsCategory,
)
from ..utils import refine_category
from .homsets import RModuleAutCategory, RModuleEndCategory, RModuleHomCategory, _RModMorphisms
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import _DualObjects
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients
from .subcategories.constructions.tensor_products import _TensorProducts

_RepresentationModules = LazyImport("category_specs.modules.subcategories.representation_modules", "_RepresentationModules")
_FreeGradedModules = LazyImport("category_specs.modules.subcategories.free_graded_modules", "_FreeGradedModules")
_FinitelyPresentedGradedModules = LazyImport(
    "category_specs.modules.subcategories.finitely_presented_graded_modules", "_FinitelyPresentedGradedModules"
)
_OreModules = LazyImport("category_specs.modules.subcategories.ore_modules", "_OreModules")
_IntegerLattices = LazyImport("category_specs.modules.subcategories.integer_lattices", "_IntegerLattices")
TorsionQuadraticModulesCategory = LazyImport(
    "category_specs.forms.subcategories.torsion_quadratic_modules", "TorsionQuadraticModulesCategory"
)
_RingObjectsAsModules = LazyImport("category_specs.modules.subcategories.ring_objects_as_modules", "_RingObjectsAsModules")

if TYPE_CHECKING:
    from ..types import (
        Algebra,
        AlgebraElement,
        Cardinality,
        CategoryElement,
        DualModule,
        FreeModule,
        Ideal,
        Integer,
        Matrix,
        ModuleStructure,
        ProjectiveModule,
        QuotientModule,
        Ring,
        RingElement,
        RMod,
        RModAut,
        RModEnd,
        RModHom,
        RModMorphism,
        RModule,
        RModuleElement,
        RModuleForm,
        Set,
        SetFamily,
        SubModule,
        TermOrder,
        TorsionModule,
    )


class _RModObjects:
    r"""ParentMethods for ``Modules(R)``.

    This class owns the base parent-method surface for R-modules; structural
    subcategories override these predicates when they add module structure.

    ``linear_combination(...)`` is intentionally not provided here: when
    elements are implemented properly the parent does not need it.
    """

    @final
    def is_over_integral_domain(self) -> bool:
        return False

    @final
    def is_over_dedekind_domain(self) -> bool:
        return False

    @final
    def is_over_pid(self) -> bool:
        return False

    @final
    def is_over_commutative_ring(self) -> bool:
        return False

    @final
    def is_over_field(self) -> bool:
        return False

    @final
    def is_over_local_ring(self) -> bool:
        return False

    @final
    def is_over_complete_ring(self) -> bool:
        return False

    @final
    def is_free(self) -> bool:
        return False

    @final
    def is_torsion(self) -> bool:
        return False

    @final
    def is_torsionfree(self) -> bool:
        return False

    @final
    def is_projective(self) -> bool:
        return False

    @final
    def is_finite(self) -> bool:
        return False

    @final
    def has_ordered_generating_set(self) -> bool:
        return False

    @final
    def has_basis(self) -> bool:
        return False

    @final
    def has_ordered_basis(self) -> bool:
        return False

    @final
    def is_finitely_generated(self) -> bool:
        return False

    @final
    def is_finitely_presented(self) -> bool:
        return False

    @final
    def is_ideal(self) -> bool:
        return False

    @final
    def has_form(self) -> bool:
        return False

    @final
    def is_bilinear(self) -> bool:
        return False

    @final
    def is_quadratic(self) -> bool:
        return False

    @final
    def is_lattice(self) -> bool:
        return False

    @final
    def is_representation_module(self) -> bool:
        return False

    @final
    def is_free_graded_module(self) -> bool:
        return False

    @final
    def is_finitely_presented_graded_module(self) -> bool:
        return False

    @final
    def is_ore_module(self) -> bool:
        return False

    @final
    def is_torsion_quadratic_module(self) -> bool:
        return False

    @final
    def is_ring_object_as_module(self) -> bool:
        return False

    @cached_method
    @final
    def tensor_square(self):
        return self.tensor_power(2)

    @final
    def tensor_power(self, n: Integer):
        match n:
            case 0:
                return self.base_ring()
            case _ if n >= 1:
                return tensor(n * [self])
            case _ if n <= -1:
                return tensor((-n) * [self.dual()])
            case _:
                assert False, f"Unsupported tensor power: {n}"

    @final
    def tensor_module(self, p: Integer, q: Integer):
        assert p >= 0 and q >= 0, "T_R(M) is NN^2-graded."
        return tensor([self.tensor_power(p), self.dual().tensor_power(q)])

    @abstract_method
    def annihilator(self) -> Ideal: ...

    @final
    def __truediv__(self, N: SubModule) -> QuotientModule:
        return self.quotient(N)

    @abstract_method
    def torsion_submodule(self) -> SubModule:
        r"""M_tors := <{m in M | r*m = 0 for some r in R}>
        = <{m in M | Ann_R(m) != 0}>.
        """
        ...

    @abstract_method
    def tensor_algebra(self) -> RModule:
        r"""Return T_R(M) := \bigoplus_n \bigoplus_{p+q=n} T_R(M)[p,q]."""
        ...

    @abstract_method
    def base_change(self, S: Ring) -> RModule:
        r"""Return a representation of M_S := M \otimes_R S in S-Mod."""
        ...

    @abstract_method
    def module_structure(self) -> ModuleStructure:
        r"""The map sigma: R x M -> M such that r.m := sigma(r, m).

        May equivalently be interpreted as a ring morphism
        sigma: R -> End_R(M), where r.m := sigma(r)(m).  Made explicit so
        that M can be twisted by composing with a ring endomorphism.
        """
        ...

    @abstract_method
    def modify_module_structure(self, sigma: ModuleStructure):
        r"""Define a new module structure sigma': R -> End_R(M) so that
        r.m = sigma'(r)(m), replacing the existing sigma.
        """
        ...

    @abstract_method
    def symmetric_algebra(self) -> RModule: ...

    @abstract_method
    def alternating_algebra(self) -> RModule: ...

    @abstract_method
    def dual(self) -> DualModule: ...

    @abstract_method
    def determinant_module(self) -> RModule:
        r"""Return \Lambda^n_R(M), the top exterior power of M."""
        ...

    @abstract_method
    def cardinality(self) -> Cardinality: ...

    @abstract_method
    def is_isomorphic_to(self, other: RModule) -> bool: ...

    @abstract_method
    def is_submodule_of(self, other: RModule) -> bool: ...

    @overload
    def direct_sum(self, other: RModule) -> RModule: ...

    @overload
    def direct_sum(self, modules: Sequence[RModule]) -> RModule: ...

    @abstract_method
    def direct_sum(self, other: RModule) -> RModule: ...

    @overload
    def tensor(self, other: RModule) -> RModule: ...

    @overload
    def tensor(self, modules: Sequence[RModule]) -> RModule: ...

    @abstract_method
    def tensor(self, other: RModule) -> RModule: ...

    @abstract_method
    def intersection(self, other: SubModule) -> SubModule: ...

    @abstract_method
    def span(
        self,
        gens: RModuleElement | Sequence[RModuleElement],
        check: bool = True,
        already_echelonized: bool = False,
    ) -> SubModule: ...

    @final
    def __add__(self, other: RModule) -> RModule:
        return self.direct_sum(other)

    @abstract_method
    def __mul__(self, other: RingElement | RModule) -> RModule:
        r"""``r * M`` = submodule spanned by ``{r*m | m in M}``;
        ``N * M`` = the tensor product ``M \otimes_R N``.
        """
        ...

    @final
    def submodule(
        self,
        gens: RModuleElement | Sequence[RModuleElement],
        check: bool = True,
        already_echelonized: bool = False,
    ) -> SubModule:
        return self.span(gens, check=check, already_echelonized=already_echelonized)

    @abstract_method
    def quotient_module(self, submodule: SubModule, check: bool = True) -> QuotientModule: ...

    # Do not define: _mul_, _rmul_, _lmul_

    @abstract_method
    def natural_pairing(self) -> RModuleForm:
        r"""The (1,1) form b: M \otimes_R M^* -> R defined by b(v, w^*) := w^*(v)."""
        ...


class _RModElements:
    r"""ElementMethods introduced by ``Modules(R)`` for elements of R-modules."""

    @final
    def span(self) -> SubModule:
        return self.parent().span([self])

    @final
    def inclusion(self) -> RModMorphism:
        Rm = self.span()
        f = Rm.inclusion()
        assert f in Rm.Hom(self.parent())
        return f

    @final
    def annihilator(self) -> Ideal:
        return self.span().annihilator()

    @abstract_method
    def cyclic_submodule(self) -> SubModule: ...

    @final
    def is_primitive(self) -> bool:
        return self.span().inclusion().is_primitive()

    @abstract_method
    def __add__(self, m: RModuleElement) -> RModuleElement: ...

    @abstract_method
    def __mul__(self, r: RingElement) -> RModuleElement: ...

    @final
    def __neg__(self) -> RModuleElement:
        R = self.base_ring()
        return R(-1) * self

    @abstract_method
    def _lmul_(self, r: RingElement) -> RModuleElement: ...

    @abstract_method
    def _rmul_(self, r: RingElement) -> RModuleElement: ...

    # TODO: define R*m := m.span() when R == m.base_ring(), or base-change.

# ---------------------------------------------------------------------------
# The Modules(R) category
# ---------------------------------------------------------------------------


class Modules(Category_module):
    r"""Canonical chain: ``Modules(R)``."""

    @override
    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageBimodules(self.base_ring(), self.base_ring()),)

    @staticmethod
    @final
    def __classcall_private__(cls, base_ring, dispatch=True):
        from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
        from sage.categories.dedekind_domains import DedekindDomains as SageDedekindDomains
        from sage.categories.fields import Fields as SageFields
        from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
        from sage.categories.principal_ideal_domains import PrincipalIdealDomains as SagePrincipalIdealDomains

        result = super().__classcall__(cls, base_ring)
        if not dispatch:
            return result
        # Cascade from most structure to least.
        if base_ring in SageFields():
            return result._with_axiom("OverField")
        if base_ring in SagePrincipalIdealDomains():
            return result._with_axiom("OverPID")
        if base_ring in SageDedekindDomains():
            return result._with_axiom("OverDedekindDomain")
        if base_ring in SageIntegralDomains():
            return result._with_axiom("OverIntegralDomain")
        if base_ring in SageCommutativeRings():
            return result._with_axiom("OverCommutativeRing")
        # TODO: full ring dispatching. -- [needs approach]
        # TODO: handle Noetherian non-commutative rings. -- [needs approach]
        return result

    @override
    @final
    def super_categories(self):
        from ..sets import Sets

        R = self.base_ring()
        return [Sets(), SageBimodules(R, R)]

    @override
    @final
    def additional_structure(self):
        r"""Return ``None`` because R-Mod morphisms are exactly (R,R)-biMod morphisms."""
        return None

    # ------------------------------------------------------------------
    # Constructors
    # ------------------------------------------------------------------

    class Constructors:
        r"""Sage module constructor entry points over ``self.base_ring()``.

        This helper owns constructor provenance: each method names a Sage
        entry point and refines the result into the tightest known module
        subcategories.
        """

        @final
        def __init__(self, category: RMod) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return f"Sage module constructors over {self.base_ring()}"

        @final
        def category(self) -> RMod:
            return self._category

        @final
        def base_ring(self) -> Ring:
            return self.category().base_ring()

        @final
        def _refine_constructed_module(self, M: RModule, categories: Sequence[Category]) -> RModule:
            return refine_category(M, [Modules(M.base_ring()), *categories])

        @final
        def _standard_free_module_categories(self) -> list[Category]:
            C = self.category()
            return [C.Free().FiniteRank().WithOrderedBasis()]

        @final
        def _finite_rank_free_module_categories(self) -> list[Category]:
            C = self.category()
            return [C.Free().FiniteRank()]

        @final
        def _submodule_categories(self, *, with_ordered_basis: bool = False) -> list[Category]:
            C = self.category()
            if with_ordered_basis:
                return [C.WithOrderedBasis().Subobjects()]
            return [C.Subobjects()]

        @final
        def _quotient_categories(self, *, with_ordered_basis: bool = False) -> list[Category]:
            C = self.category()
            if with_ordered_basis:
                return [C.WithOrderedBasis().Quotients()]
            return [C.Quotients()]

        @final
        def _categories_for_free_module(self, M: RModule) -> list[Category]:
            from sage.modules.free_module import (
                ComplexDoubleVectorSpace_class,
                FreeModule_ambient_field,
                FreeModule_submodule_field,
                FreeModule_submodule_pid,
                FreeModule_submodule_with_basis_field,
                FreeModule_submodule_with_basis_pid,
                RealDoubleVectorSpace_class,
            )
            from sage.modules.free_quadratic_module import FreeQuadraticModule_generic
            from sage.modules.quotient_module import FreeModule_ambient_field_quotient

            if isinstance(M, FreeQuadraticModule_generic):
                C = self.category()
                return [*self._standard_free_module_categories(), C.WithForms().Bilinear(), C.WithForms().Quadratic()]
            if isinstance(M, FreeModule_ambient_field_quotient):
                return self._quotient_categories()
            if isinstance(M, FreeModule_submodule_with_basis_field):
                return self._submodule_categories(with_ordered_basis=True)
            if isinstance(M, FreeModule_submodule_field):
                return self._submodule_categories()
            if isinstance(M, RealDoubleVectorSpace_class):
                return self._standard_free_module_categories()
            if isinstance(M, ComplexDoubleVectorSpace_class):
                return self._standard_free_module_categories()
            if isinstance(M, FreeModule_submodule_with_basis_pid):
                return self._submodule_categories(with_ordered_basis=True)
            if isinstance(M, FreeModule_submodule_pid):
                return self._submodule_categories()
            if isinstance(M, FreeModule_ambient_field):
                return self._standard_free_module_categories()
            return self._standard_free_module_categories()

        @final
        def _categories_for_quotient_module(self, M: RModule) -> list[Category]:
            from sage.modules.fg_pid.fgp_module import FGP_Module_class
            from sage.modules.quotient_module import FreeModule_ambient_field_quotient, QuotientModule_free_ambient

            if isinstance(M, FreeModule_ambient_field_quotient):
                return self._quotient_categories()
            if isinstance(M, QuotientModule_free_ambient):
                return self._quotient_categories()
            if isinstance(M, FGP_Module_class):
                C = self.category()
                return [C.FinitelyGenerated(), C.FinitelyPresented(), C.OverPID()]
            return self._categories_for_free_module(M)

        @final
        def _categories_for_combinatorial_free_module(self) -> list[Category]:
            C = self.category()
            return [C.Free(), C.WithBasis(), C.WithOrderedGeneratingSet()]

        @final
        def FreeModule(
            self,
            rank: Integer,
            sparse: bool = False,
            *,
            inner_product_matrix: Matrix | None = None,
        ) -> RModule:
            from sage.modules.free_module import FreeModule as SageFreeModule

            M = SageFreeModule(
                self.base_ring(),
                rank,
                sparse,
                inner_product_matrix,
            )
            categories = self._categories_for_free_module(M)
            return self._refine_constructed_module(M, categories)

        @final
        def FreeModuleWithBasisKeys(
            self,
            basis_keys: Set | SetFamily,
            sparse: bool = False,
        ) -> RModule:
            from sage.modules.free_module import FreeModule as SageFreeModule

            M = SageFreeModule(self.base_ring(), basis_keys, sparse)
            from sage.combinat.free_module import CombinatorialFreeModule

            if isinstance(M, CombinatorialFreeModule):
                categories = self._categories_for_combinatorial_free_module()
            else:
                categories = self._categories_for_free_module(M)
            return self._refine_constructed_module(M, categories)

        @final
        def FreeModuleWithoutBasis(
            self,
            rank: Integer,
            sparse: bool = False,
        ) -> RModule:
            from sage.modules.free_module import FreeModule as SageFreeModule

            M = SageFreeModule(self.base_ring(), rank, sparse, with_basis=None)
            return self._refine_constructed_module(M, self._finite_rank_free_module_categories())

        @final
        def FreeModuleWithInnerProductRows(
            self,
            rank: Integer,
            inner_product_rows: Sequence[Sequence[RingElement]],
            *,
            sparse: bool = False,
        ) -> RModule:
            from sage.matrix.constructor import matrix

            return self.FreeModule(rank, sparse=sparse, inner_product_matrix=matrix(self.base_ring(), inner_product_rows))

        @final
        def FreeModuleWithInnerProductEntries(
            self,
            rank: Integer,
            inner_product_entries: Sequence[RingElement],
            *,
            sparse: bool = False,
        ) -> RModule:
            from sage.matrix.constructor import matrix

            return self.FreeModule(rank, sparse=sparse, inner_product_matrix=matrix(self.base_ring(), rank, rank, inner_product_entries))

        @final
        def VectorSpace(
            self,
            dimension: Integer,
            sparse: bool = False,
            *,
            inner_product_matrix: Matrix | None = None,
        ) -> RModule:
            from sage.modules.free_module import VectorSpace as SageVectorSpace

            M = SageVectorSpace(
                self.base_ring(),
                dimension,
                sparse,
                inner_product_matrix,
            )
            return self._refine_constructed_module(M, self._categories_for_free_module(M))

        @final
        def VectorSpaceWithBasisKeys(
            self,
            basis_keys: Set | SetFamily,
            sparse: bool = False,
        ) -> RModule:
            from sage.modules.free_module import VectorSpace as SageVectorSpace

            M = SageVectorSpace(self.base_ring(), basis_keys, sparse)
            return self._refine_constructed_module(M, self._categories_for_combinatorial_free_module())

        @final
        def VectorSpaceWithoutBasis(
            self,
            dimension: Integer,
            sparse: bool = False,
        ) -> RModule:
            from sage.modules.free_module import VectorSpace as SageVectorSpace

            M = SageVectorSpace(self.base_ring(), dimension, sparse, with_basis=None)
            return self._refine_constructed_module(M, self._finite_rank_free_module_categories())

        @final
        def VectorSpaceWithInnerProductRows(
            self,
            dimension: Integer,
            inner_product_rows: Sequence[Sequence[RingElement]],
            *,
            sparse: bool = False,
        ) -> RModule:
            from sage.matrix.constructor import matrix

            return self.VectorSpace(dimension, sparse=sparse, inner_product_matrix=matrix(self.base_ring(), inner_product_rows))

        @final
        def VectorSpaceWithInnerProductEntries(
            self,
            dimension: Integer,
            inner_product_entries: Sequence[RingElement],
            *,
            sparse: bool = False,
        ) -> RModule:
            from sage.matrix.constructor import matrix

            return self.VectorSpace(
                dimension,
                sparse=sparse,
                inner_product_matrix=matrix(self.base_ring(), dimension, dimension, inner_product_entries),
            )

        @final
        def FreeQuadraticModule(
            self,
            rank: Integer,
            inner_product_matrix: Matrix,
            sparse: bool = False,
        ) -> RModule:
            from sage.modules.free_quadratic_module import FreeQuadraticModule

            M = FreeQuadraticModule(
                self.base_ring(),
                rank,
                inner_product_matrix,
                sparse=sparse,
            )
            return self._refine_constructed_module(
                M,
                [
                    *self._standard_free_module_categories(),
                    self.category().WithForms().Bilinear(),
                    self.category().WithForms().Quadratic(),
                ],
            )

        @final
        def FreeQuadraticModuleFromRows(
            self,
            rank: Integer,
            inner_product_rows: Sequence[Sequence[RingElement]],
            sparse: bool = False,
        ) -> RModule:
            from sage.matrix.constructor import matrix

            return self.FreeQuadraticModule(rank, matrix(self.base_ring(), inner_product_rows), sparse=sparse)

        @final
        def FreeQuadraticModuleFromEntries(
            self,
            rank: Integer,
            inner_product_entries: Sequence[RingElement],
            sparse: bool = False,
        ) -> RModule:
            from sage.matrix.constructor import matrix

            return self.FreeQuadraticModule(rank, matrix(self.base_ring(), rank, rank, inner_product_entries), sparse=sparse)

        @final
        def span(
            self,
            gens: Sequence[RModuleElement] | Matrix,
            check: bool = True,
            already_echelonized: bool = False,
        ) -> SubModule:
            from sage.modules.free_module import span as sage_span

            M = sage_span(gens, self.base_ring(), check=check, already_echelonized=already_echelonized)
            return self._refine_constructed_module(M, self._categories_for_free_module(M))

        @final
        def CombinatorialFreeModule(
            self,
            basis_keys: Set | SetFamily,
            element_class: type[CategoryElement] | None = None,
            category: Category | tuple[Category, ...] | None = None,
            prefix: str | None = None,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.combinat.free_module import CombinatorialFreeModule

            M = CombinatorialFreeModule(
                self.base_ring(),
                basis_keys,
                element_class=element_class,
                category=category,
                prefix=prefix,
                names=names,
            )
            return self._refine_constructed_module(M, self._categories_for_combinatorial_free_module())

        @final
        def FiniteRankFreeModule(
            self,
            rank: Integer,
            name: str | None = None,
            latex_name: str | None = None,
            start_index: Integer = 0,
            output_formatter: Callable[[RingElement], str] | Callable[[RingElement, str], str] | None = None,
        ) -> FreeModule:
            from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule

            M = FiniteRankFreeModule(
                self.base_ring(),
                rank,
                name=name,
                latex_name=latex_name,
                start_index=start_index,
                output_formatter=output_formatter,
            )
            return self._refine_constructed_module(M, self._finite_rank_free_module_categories())

        @final
        def quotient_of_free_modules(self, V: FreeModule, W: SubModule) -> QuotientModule:
            M = V / W
            return self._refine_constructed_module(M, self._categories_for_quotient_module(M))

        @final
        def quotient_module(self, module: RModule, submodule: SubModule, check: bool = True) -> QuotientModule:
            M = module.quotient_module(submodule, check=check)
            return self._refine_constructed_module(M, self._categories_for_quotient_module(M))

        @final
        def FPModule(
            self,
            algebra: Algebra,
            generator_degrees: Sequence[Integer],
            relations: Sequence[Sequence[AlgebraElement]] = (),
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            return self.FPModuleFromPresentation(
                algebra,
                generator_degrees=generator_degrees,
                relations=relations,
                names=names,
            )

        @final
        def FPModuleFromPresentation(
            self,
            algebra: Algebra,
            *,
            generator_degrees: Sequence[Integer],
            relations: Sequence[Sequence[AlgebraElement]] = (),
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.modules.fp_graded.module import FPModule

            M = FPModule(algebra, generator_degrees=generator_degrees, relations=relations, names=names)
            return self._refine_constructed_module(M, [self.category().FinitelyPresentedGradedModules()])

        @final
        def FPModuleFromCokernelMap(self, defining_map: RModMorphism, names: str | tuple[str, ...] | None = None) -> RModule:
            from sage.modules.fp_graded.module import FPModule

            M = FPModule(defining_map, names=names)
            return self._refine_constructed_module(M, [self.category().FinitelyPresentedGradedModules()])

        @final
        def FPModuleFromFreeGradedModule(
            self,
            module: RModule,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.modules.fp_graded.module import FPModule

            assert module in self.category().FreeGradedModules(), f"Expected a free graded module: {module}"
            M = FPModule(module, names=names)
            return self._refine_constructed_module(M, [self.category().FinitelyPresentedGradedModules()])

        @final
        def FreeGradedModule(
            self,
            algebra: Algebra,
            generator_degrees: Sequence[Integer],
            category: Category | None = None,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.modules.fp_graded.free_module import FreeGradedModule

            M = FreeGradedModule(algebra, generator_degrees, category=category, names=names)
            return self._refine_constructed_module(M, [self.category().FreeGradedModules()])

        @final
        def OreQuotientModule(self, ore_polynomial_ring: Ring, polynomial: RingElement) -> RModule:
            M = ore_polynomial_ring.quotient_module(polynomial)
            return self._refine_constructed_module(M, [self.category().OreModules()])

        @final
        def IntegerLatticeFromBasisMatrix(
            self,
            basis: Matrix,
            lll_reduce: bool = True,
        ) -> RModule:
            from sage.modules.free_module_integer import IntegerLattice

            M = IntegerLattice(basis, lll_reduce=lll_reduce)
            return self._refine_constructed_module(M, [self.category().IntegerLattices()])

        @final
        def IntegerLatticeFromBasisRows(
            self,
            basis_rows: Sequence[Sequence[RingElement]],
            lll_reduce: bool = True,
        ) -> RModule:
            from sage.matrix.constructor import matrix
            from sage.rings.integer_ring import ZZ

            return self.IntegerLatticeFromBasisMatrix(matrix(ZZ, basis_rows), lll_reduce=lll_reduce)

        @final
        def IntegerLatticeFromOrderElement(self, element: RingElement, lll_reduce: bool = True) -> RModule:
            from sage.modules.free_module_integer import IntegerLattice

            M = IntegerLattice(element, lll_reduce=lll_reduce)
            return self._refine_constructed_module(M, [self.category().IntegerLattices()])

        @final
        def IntegerLattice(
            self,
            basis: Matrix,
            lll_reduce: bool = True,
        ) -> RModule:
            return self.IntegerLatticeFromBasisMatrix(basis, lll_reduce=lll_reduce)

        @final
        def TorsionQuadraticForm(self, q: Matrix) -> RModule:
            from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

            M = TorsionQuadraticForm(q)
            return self._refine_constructed_module(M, [self.category().TorsionQuadraticModules()])

        @final
        def TorsionQuadraticFormFromRows(self, q_rows: Sequence[Sequence[RingElement]]) -> RModule:
            from sage.matrix.constructor import matrix
            from sage.rings.rational_field import QQ

            return self.TorsionQuadraticForm(matrix(QQ, q_rows))

        @final
        def ring_as_rank_one_module(self, ring: Ring | None = None) -> FreeModule:
            R = self.base_ring() if ring is None else ring
            M = Modules(R).Constructors().FreeModule(rank=1)
            return self._refine_constructed_module(M, [self.category().Free().FiniteRank().WithOrderedBasis()])

        @final
        def ideal_as_submodule(self, ideal: Ideal) -> SubModule:
            return self._refine_constructed_module(ideal, [Modules(ideal.ring()).RIdeals()])

        @final
        def invertible_ideal_as_projective_submodule(self, ideal: Ideal) -> ProjectiveModule:
            R = ideal.ring()
            return self._refine_constructed_module(ideal, [Modules(R).RIdeals(), Modules(R).Projective()])

        @overload
        def polynomial_ring_as_module(
            self,
            *,
            name: str,
            n: Integer | None = None,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> RModule: ...

        @overload
        def polynomial_ring_as_module(
            self,
            *,
            names: str | Sequence[str],
            n: Integer | None = None,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> RModule: ...

        @overload
        def polynomial_ring_as_module(
            self,
            *,
            var_array: str | Sequence[str],
            n: Integer,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> RModule: ...

        @overload
        def polynomial_ring_as_module(
            self,
            *,
            n: Integer,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> RModule: ...

        @final
        def polynomial_ring_as_module(
            self,
            *,
            n: Integer | None = None,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            var_array: str | Sequence[str] | None = None,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().PolynomialRing(
                self.base_ring(),
                n=n,
                name=name,
                names=names,
                var_array=var_array,
                sparse=sparse,
                order=order,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def power_series_ring_as_module(
            self,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().PowerSeriesRing(
                self.base_ring(),
                name=name,
                sparse=sparse,
                default_prec=default_prec,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def multivariate_power_series_ring_as_module(
            self,
            names: str | Sequence[str],
            *,
            num_gens: Integer | None = None,
            sparse: bool = False,
            default_prec: Integer | None = None,
            order: str = "negdeglex",
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().MultivariatePowerSeriesRing(
                self.base_ring(),
                names=names,
                num_gens=num_gens,
                sparse=sparse,
                default_prec=default_prec,
                order=order,
            )
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def multivariate_power_series_ring_with_generator_prefix_as_module(
            self,
            prefix: str,
            num_gens: Integer,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            order: str = "negdeglex",
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().MultivariatePowerSeriesRingWithGeneratorPrefix(
                self.base_ring(),
                prefix=prefix,
                num_gens=num_gens,
                sparse=sparse,
                default_prec=default_prec,
                order=order,
            )
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def laurent_series_ring_as_module(
            self,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().LaurentSeriesRing(
                self.base_ring(),
                name=name,
                sparse=sparse,
                default_prec=default_prec,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def laurent_series_ring_from_power_series_as_module(self, power_series_ring: Ring) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().LaurentSeriesRingFromPowerSeriesRing(power_series_ring)
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def puiseux_series_ring_as_module(
            self,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().PuiseuxSeriesRing(
                self.base_ring(),
                name=name,
                sparse=sparse,
                default_prec=default_prec,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def puiseux_series_ring_from_laurent_series_as_module(self, laurent_series_ring: Ring) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().PuiseuxSeriesRingFromLaurentSeriesRing(laurent_series_ring)
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

        @final
        def matrix_ring_as_module(
            self,
            n: Integer,
            sparse: bool = False,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().MatrixRing(
                self.base_ring(),
                n,
                sparse=sparse,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, [self.category().RingObjectsAsModules()])

    _Constructors = Constructors

    @cached_method
    @final
    def Constructors(self):
        r"""Return the Sage module constructor collector over ``self.base_ring()``."""
        return self.__class__._Constructors(self)

    @abstract_method
    def zero_module(self) -> RModule: ...

    @abstract_method
    def R(self) -> FreeModule:
        r"""Return R as a rank 1 free R-module."""
        ...

    @abstract_method
    def torsion_module(self, r: RingElement) -> TorsionModule:
        r"""Return R/r.  Asserts R != 0."""
        ...

    @final
    def free_module(self, n: Integer) -> FreeModule:
        from sage.rings.semirings.non_negative_integer_semiring import NN

        assert n in NN, f"Negative integers are not well-defined ranks: {n}"
        if n == 0:
            return self.zero_module()
        return sum(n * [self.R()])

    @final
    def from_ring_elements(self, elts: Sequence[RingElement]) -> RModule:
        r"""Given an ordered subset {r_1, ..., r_n} of R, return
        ``M := R/r_1 \oplus ... \oplus R/r_n``, where R/0 := R.
        """
        from sage.categories.rings import Rings as SageRings

        if not elts:
            return self.zero_module()
        assert all(r.parent() in SageRings() for r in elts), f"All element parents must be rings: {elts}"
        R = elts[0].parent()
        assert all(r.parent() is R for r in elts), f"Elements must share a common ring: {[r.parent() for r in elts]}"
        zs = [r for r in elts if r.is_zero()]
        rs = [r for r in elts if not r.is_zero()]
        F = self.free_module(len(zs))
        T = sum(self.torsion_module(r) for r in rs)
        return F + T

    @final
    def from_invariant_factors(self, elts: Sequence[RingElement]) -> RModule:
        return self.from_ring_elements(elts)

    @final
    def from_matrix(self, M: Matrix) -> RModule:
        r"""Interpret a matrix as a representation of a morphism
        f: R^m -> R^n and return ``coker(f)``.
        """
        from .subcategories.finitely_presented_over_pid import FinitelyPresentedModulesOverPID

        return FinitelyPresentedModulesOverPID.from_matrix(self, M)

    # ------------------------------------------------------------------
    # SubcategoryMethods — available on every subcategory of Modules(R)
    # ------------------------------------------------------------------

    class SubcategoryMethods:
        @cached_method
        @final
        def base_ring(self) -> Ring:
            return self.base_category().base_ring()

        ## Ring properties

        @cached_method
        @final
        def OverIntegralDomain(self) -> Category:
            return self._with_axiom("OverIntegralDomain")

        @cached_method
        @final
        def OverDedekindDomain(self) -> Category:
            return self._with_axiom("OverDedekindDomain")

        @cached_method
        @final
        def OverPID(self) -> Category:
            return self._with_axiom("OverPID")

        @cached_method
        @final
        def OverCommutativeRing(self) -> Category:
            return self._with_axiom("OverCommutativeRing")

        @cached_method
        @final
        def OverField(self) -> Category:
            return self._with_axiom("OverField")

        @cached_method
        @final
        def OverLocalRing(self) -> Category:
            return self._with_axiom("OverLocalRing")

        @cached_method
        @final
        def OverCompleteRing(self) -> Category:
            return self._with_axiom("OverCompleteRing")

        ## Homological properties

        @cached_method
        @final
        def Free(self) -> Category:
            return self._with_axiom("Free")

        @cached_method
        @final
        def Torsion(self) -> Category:
            return self._with_axiom("Torsion")

        @cached_method
        @final
        def Torsionfree(self) -> Category:
            return self._with_axiom("Torsionfree")

        @cached_method
        @final
        def Projective(self) -> Category:
            return self._with_axiom("Projective")

        ## Generation properties

        @cached_method
        @final
        def WithBasis(self) -> Category:
            return self._with_axiom("WithBasis")

        @cached_method
        @final
        def WithOrderedBasis(self) -> Category:
            return self._with_axiom("WithOrderedBasis")

        @cached_method
        @final
        def WithOrderedGeneratingSet(self) -> Category:
            return self._with_axiom("WithOrderedGeneratingSet")

        @cached_method
        @final
        def FinitelyGenerated(self) -> Category:
            return self._with_axiom("FinitelyGenerated")

        @cached_method
        @final
        def FinitelyPresented(self) -> Category:
            return self._with_axiom("FinitelyPresented")

        @cached_method
        @final
        def TensorProducts(self) -> Category:
            return TensorProductsCategory.category_of(self)

        @cached_method
        @final
        def DualObjects(self) -> Category:
            return DualObjectsCategory.category_of(self)

        dual = DualObjects

        ## Extra structure

        @cached_method
        @final
        def Filtered(self) -> Category:
            return FilteredModulesCategory.category_of(self)

        @cached_method
        @final
        def Graded(self) -> Category:
            return GradedModulesCategory.category_of(self)

        @cached_method
        @final
        def Super(self) -> Category:
            return SuperModulesCategory.category_of(self)

        ## Forms

        @cached_method
        @final
        def WithForms(self) -> Category:
            return self._with_axiom("WithForms")

        @cached_method
        @final
        def RIdeals(self) -> Category:
            return self._with_axiom("RIdeals")

        @cached_method
        @final
        def RepresentationModules(self) -> Category:
            return _RepresentationModules(self.base_ring())

        @cached_method
        @final
        def FreeGradedModules(self) -> Category:
            return _FreeGradedModules(self.base_ring())

        @cached_method
        @final
        def FinitelyPresentedGradedModules(self) -> Category:
            return _FinitelyPresentedGradedModules(self.base_ring())

        @cached_method
        @final
        def OreModules(self) -> Category:
            return _OreModules(self.base_ring())

        @cached_method
        @final
        def IntegerLattices(self) -> Category:
            return _IntegerLattices(self.base_ring())

        @cached_method
        @final
        def TorsionQuadraticModules(self) -> Category:
            return TorsionQuadraticModulesCategory(self.base_ring())

        @cached_method
        @final
        def RingObjectsAsModules(self) -> Category:
            return _RingObjectsAsModules(self.base_ring())

    # ------------------------------------------------------------------
    # Method providers
    # ------------------------------------------------------------------

    ParentMethods = _RModObjects
    ElementMethods = _RModElements
    MorphismMethods = _RModMorphisms
    HomCategory = RModuleHomCategory

    # ------------------------------------------------------------------
    # Named subcategories
    # ------------------------------------------------------------------

    RIdeals = LazyImport("category_specs.modules.subcategories.r_ideals", "_RIdeals")

    # ------------------------------------------------------------------
    # Axiomatic subcategories — ring properties
    # ------------------------------------------------------------------

    OverIntegralDomain = LazyImport("category_specs.modules.subcategories.over_integral_domain", "_OverIntegralDomain")
    OverDedekindDomain = LazyImport("category_specs.modules.subcategories.over_dedekind_domain", "_OverDedekindDomain")
    OverPID = LazyImport("category_specs.modules.subcategories.over_pid", "_OverPID")
    OverCommutativeRing = LazyImport("category_specs.modules.subcategories.over_commutative_ring", "_OverCommutativeRing")
    OverField = LazyImport("category_specs.modules.subcategories.over_field", "_OverField")
    OverLocalRing = LazyImport("category_specs.modules.subcategories.over_local_ring", "_OverLocalRing")
    OverCompleteRing = LazyImport("category_specs.modules.subcategories.over_complete_ring", "_OverCompleteRing")

    # ------------------------------------------------------------------
    # Axiomatic subcategories — homological
    # ------------------------------------------------------------------

    Free = LazyImport("category_specs.modules.subcategories.free", "_Free")
    Torsion = LazyImport("category_specs.modules.subcategories.torsion", "_Torsion")
    Torsionfree = LazyImport("category_specs.modules.subcategories.torsionfree", "_Torsionfree")
    Projective = LazyImport("category_specs.modules.subcategories.projective", "_Projective")

    # ------------------------------------------------------------------
    # Axiomatic subcategories — generation
    # ------------------------------------------------------------------

    WithBasis = LazyImport("category_specs.modules.subcategories.with_basis", "_WithBasis")
    WithOrderedBasis = LazyImport("category_specs.modules.subcategories.with_basis", "_WithOrderedBasis")
    WithOrderedGeneratingSet = LazyImport(
        "category_specs.modules.subcategories.with_ordered_generating_set", "_WithOrderedGeneratingSet"
    )
    FinitelyGenerated = LazyImport("category_specs.modules.subcategories.finitely_generated", "_FinitelyGenerated")
    FinitelyPresented = LazyImport("category_specs.modules.subcategories.finitely_presented", "_FinitelyPresented")

    # ------------------------------------------------------------------
    # Functorial constructions
    # ------------------------------------------------------------------

    Subobjects = _Subobjects
    SubModules = Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    TensorProducts = _TensorProducts
    CartesianProducts = _CartesianProducts
    DualObjects = _DualObjects

    Filtered = LazyImport("sage.categories.filtered_modules", "FilteredModules")
    Graded = LazyImport("sage.categories.graded_modules", "GradedModules")
    Super = LazyImport("sage.categories.super_modules", "SuperModules")

    # ------------------------------------------------------------------
    # Forms / lattice surface
    # ------------------------------------------------------------------

    WithForms = LazyImport("category_specs.forms.subcategories.with_forms", "FormedModulesCategory")
    # Lattices: (M, b) with M a f.g. torsionfree R-module over a domain and
    # b a symmetric nondegenerate integral bilinear form.


# ---------------------------------------------------------------------------
# Composed surfaces (aspirational; resolved once axiom chains are populated)
# ---------------------------------------------------------------------------
# TODO: immediately restrict to Dedekind domains, then to PIDs.  Bilinear / -- [needs approach]
# quadratic modules and (rational) lattices are wanted over PIDs (so they
# are free of finite rank).
#
# Lattices = (
#     Modules(IntegralDomains())
#         .FinitelyGenerated()
#         .Torsionfree()
#         .WithForms()
#         .Bilinear()
#         .Symmetric()
#         .Nondegenerate()
#         .Integral()
# )
# RationalLattices = (
#     Modules(IntegralDomains())
#         .FinitelyGenerated()
#         .Torsionfree()
#         .OverIntegralDomain()
#         .WithForms()
#         .Bilinear()
#         .Symmetric()
#         .Nondegenerate()
#         .Rational()
# )


# ---------------------------------------------------------------------------
# TODO: subcategory-specific surface -- [needs approach]
# ---------------------------------------------------------------------------
# - to_matrix
# - identify when Hom_R(M, N) is a matrix algebra
# - identify when End_R(M) is a matrix algebra
# - identify when Aut_R(M) is a subgroup of (GL_n(R), *)
# - iteration on countable objects
# - __contains__ methods
# - to/from_X for X = dict, images, matrix, function


# The specialized ``FinitelyPresented() ∩ OverPID()`` implementation in
# ``subcategories/finitely_presented_over_pid.py`` is intentionally not installed here
# yet. Installing it as ``_FinitelyPresented.OverPID`` recursively re-enters
# ``FinitelyPresented().OverPID()`` once ``OverPID`` is registered as a real
# axiom.  The generic axiom join composes correctly and keeps the category
# surface usable until the meet class is wired with a non-recursive base.


ModulesCategory = Modules
ModulesObject = Modules.ParentMethods
ModulesElement = Modules.ElementMethods
ModulesMorphism = Modules.MorphismMethods
ModulesHomCategory = RModuleHomCategory
ModulesEndCategory = RModuleEndCategory
ModulesAutCategory = RModuleAutCategory
ModulesHom = RModuleHomCategory.ParentMethods
ModulesEnd = RModuleEndCategory.ParentMethods
ModulesAut = RModuleAutCategory.ParentMethods
ModulesEndomorphism = RModuleEndCategory.ElementMethods
ModulesAutomorphism = RModuleAutCategory.ElementMethods
