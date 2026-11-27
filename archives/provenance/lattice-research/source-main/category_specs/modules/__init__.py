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

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, TypeVar, final, overload, override

from sage.categories.bimodules import Bimodules as SageBimodules
from sage.categories.tensor import tensor
from sage.misc.lazy_import import LazyImport

from ..cat import (
    Category,
    Category_module,
    DualObjectsCategory,
    FilteredModulesCategory,
    SuperModulesCategory,
    TensorProductsCategory,
)
from ..cat import (
    GradedModulesCategory as GradedModulesCategory,
)
from ..utils import refine_category
from .homsets import (
    RModuleAutCategory,
    RModuleEndCategory,
    RModuleHomCategory,
)
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import _DualObjects
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients
from .subcategories.constructions.tensor_products import _TensorProducts

_F = TypeVar("_F", bound=Callable[..., object])

_RepresentationModules = LazyImport(
    "category_specs.modules.subcategories.representation_modules",
    "_RepresentationModules",
)
_FreeGradedModules = LazyImport(
    "category_specs.modules.subcategories.free_graded_modules", "_FreeGradedModules"
)
_FinitelyPresentedGradedModules = LazyImport(
    "category_specs.modules.subcategories.finitely_presented_graded_modules",
    "_FinitelyPresentedGradedModules",
)
_Graded = LazyImport("category_specs.modules.subcategories.graded", "_Graded")
_OreModules = LazyImport(
    "category_specs.modules.subcategories.ore_modules", "_OreModules"
)
_IntegerLattices = LazyImport(
    "category_specs.modules.subcategories.integer_lattices", "_IntegerLattices"
)
TorsionQuadraticModulesCategory = LazyImport(
    "category_specs.forms.subcategories.torsion_quadratic_modules",
    "TorsionQuadraticModulesCategory",
)
_RingObjectsAsModules = LazyImport(
    "category_specs.modules.subcategories.ring_objects_as_modules",
    "_RingObjectsAsModules",
)

if TYPE_CHECKING:
    from ..spec_core import ConstructorRegistry
    from ..types import (
        Algebra,
        AlgebraElement,
        Cardinality,
        CategoryElement,
        DualModule,
        Ideal,
        Integer,
        Matrix,
        ModuleStructure,
        OrePolynomialRing,
        ProjectiveModule,
        QuotientModule,
        Ring,
        RingElement,
        RingMorphism,
        RMod,
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
    from ..types import (
        FreeModule as FreeModuleType,
    )


class _RModObjects:
    r"""ParentMethods for ``Modules(R)``.

    This class owns the base parent-method surface for R-modules; structural
    subcategories override these predicates when they add module structure.

    ``linear_combination(...)`` is intentionally not provided here: when
    elements are implemented properly the parent does not need it.
    """

    @abstractmethod
    def zero(self) -> RModuleElement: ...

    @abstractmethod
    def base_ring(self) -> Ring: ...

    @abstractmethod
    def is_over_integral_domain(self) -> bool: ...

    @abstractmethod
    def is_over_dedekind_domain(self) -> bool: ...

    @abstractmethod
    def is_over_pid(self) -> bool: ...

    @abstractmethod
    def is_over_commutative_ring(self) -> bool: ...

    @abstractmethod
    def is_over_field(self) -> bool: ...

    @abstractmethod
    def is_over_local_ring(self) -> bool: ...

    @abstractmethod
    def is_over_complete_ring(self) -> bool: ...

    @abstractmethod
    def is_free(self) -> bool: ...

    @abstractmethod
    def is_torsion(self) -> bool: ...

    @abstractmethod
    def is_torsionfree(self) -> bool: ...

    @abstractmethod
    def is_projective(self) -> bool: ...

    @abstractmethod
    def is_finite(self) -> bool: ...

    @abstractmethod
    def has_ordered_generating_set(self) -> bool: ...

    @abstractmethod
    def has_basis(self) -> bool: ...

    @abstractmethod
    def has_ordered_basis(self) -> bool: ...

    @abstractmethod
    def is_finitely_generated(self) -> bool: ...

    @abstractmethod
    def is_finitely_presented(self) -> bool: ...

    @abstractmethod
    def is_ideal(self) -> bool: ...

    @abstractmethod
    def has_form(self) -> bool: ...

    @abstractmethod
    def is_bilinear(self) -> bool: ...

    @abstractmethod
    def is_quadratic(self) -> bool: ...

    @abstractmethod
    def is_lattice(self) -> bool: ...

    @abstractmethod
    def is_representation_module(self) -> bool: ...

    @abstractmethod
    def is_free_graded_module(self) -> bool: ...

    @abstractmethod
    def is_finitely_presented_graded_module(self) -> bool: ...

    @abstractmethod
    def is_graded(self) -> bool: ...

    @abstractmethod
    def is_ore_module(self) -> bool: ...

    @abstractmethod
    def is_torsion_quadratic_module(self) -> bool: ...

    @abstractmethod
    def is_ring_object_as_module(self) -> bool: ...
    @final
    def tensor_square(self) -> RModule | Ring:
        return self.tensor_power(2)

    @final
    def tensor_power(self, n: Integer) -> RModule | Ring:
        match n:
            case 0:
                return self.base_ring()
            case _ if n >= 1:
                tensor_product: RModule = tensor(n * [self])
                return tensor_product
            case _ if n <= -1:
                tensor_product: RModule = tensor((-n) * [self.dual()])
                return tensor_product
            case _:
                assert False, f"Unsupported tensor power: {n}"

    @final
    def tensor_module(self, p: Integer, q: Integer) -> RModule:
        assert p >= 0 and q >= 0, "T_R(M) is NN^2-graded."
        tensor_product: RModule = tensor(
            [self.tensor_power(p), self.dual().tensor_power(q)]
        )
        return tensor_product

    @abstractmethod
    def annihilator(self) -> Ideal: ...

    @final
    def __truediv__(self, N: SubModule) -> QuotientModule:
        return self.quotient_module(N)

    @abstractmethod
    def torsion_submodule(self) -> SubModule:
        r"""M_tors := <{m in M | r*m = 0 for some r in R}>
        = <{m in M | Ann_R(m) != 0}>.
        """
        ...

    @abstractmethod
    def tensor_algebra(self) -> RModule:
        r"""Return T_R(M) := \bigoplus_n \bigoplus_{p+q=n} T_R(M)[p,q]."""
        ...

    @abstractmethod
    def base_change(self, morphism: RingMorphism) -> RModule:
        r"""Return a representation of M_S := S \otimes_R M in S-Mod."""
        ...

    @abstractmethod
    def module_structure(self) -> ModuleStructure:
        r"""The map sigma: R x M -> M such that r.m := sigma(r, m).

        May equivalently be interpreted as a ring morphism
        sigma: R -> End_R(M), where r.m := sigma(r)(m).  Made explicit so
        that M can be twisted by composing with a ring endomorphism.
        """
        ...

    def modify_module_structure(self, sigma: ModuleStructure) -> None:
        r"""Rejected as an unqualified public root method.

        Use named constructions instead:

        - ``base_change(morphism)`` or ``extend_scalars(phi: R -> S)``
          (extension of scalars / base change),
        - ``restrict_scalars(phi: S -> R)`` (restriction of scalars),
        - ``twist_scalar_action(sigma)`` (twist by ring endomorphism),
        - or explicit isomorphism transport.

        See ``DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES``.
        """
        raise NotImplementedError(
            "modify_module_structure is not an unqualified root method. "
            "Use base_change, restrict_scalars, twist_scalar_action, "
            "or explicit isomorphism transport instead. "
            "See DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES."
        )

    @abstractmethod
    def symmetric_algebra(self) -> RModule: ...

    @abstractmethod
    def alternating_algebra(self) -> RModule: ...

    @abstractmethod
    def dual(self) -> DualModule:
        r"""Return the Hom-dual module ``Hom_R(M, R)``.

        Diagnostics: when the global category diagnostic flag is enabled, emit a
        category diagnostic if a subclass or interop path has an adjacent metric-dual
        convention.  The diagnostic should say that this method returns the
        evaluation-bearing Hom object; metric duals such as ``L^\#`` belong to the
        formed/lattice metric-dual construction when that structure is present.
        """
        ...

    @abstractmethod
    def determinant_module(self) -> RModule:
        r"""Return \Lambda^n_R(M), the top exterior power of M."""
        ...

    @abstractmethod
    def cardinality(self) -> Cardinality: ...

    @abstractmethod
    def is_isomorphic_to(self, other: RModule) -> bool: ...

    @overload
    def direct_sum(self, other: RModule) -> RModule: ...

    @overload
    def direct_sum(self, other: Sequence[RModule]) -> RModule: ...

    @abstractmethod
    def direct_sum(self, other: RModule | Sequence[RModule]) -> RModule: ...

    @overload
    def tensor(self, other: RModule) -> RModule: ...

    @overload
    def tensor(self, other: Sequence[RModule]) -> RModule: ...

    @abstractmethod
    def tensor(self, other: RModule | Sequence[RModule]) -> RModule: ...

    @abstractmethod
    def intersection(self, other: SubModule) -> SubModule: ...

    @abstractmethod
    def span(
        self,
        gens: RModuleElement | Sequence[RModuleElement],
        check: bool = True,
        already_echelonized: bool = False,
    ) -> SubModule: ...

    @final
    def __add__(self, other: RModule) -> RModule:
        return self.direct_sum(other)

    @abstractmethod
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

    @abstractmethod
    def quotient_module(
        self, submodule: SubModule, check: bool = True
    ) -> QuotientModule: ...

    # Do not define: _mul_, _rmul_, _lmul_

    @abstractmethod
    def natural_pairing(self) -> RModuleForm:
        r"""The (1,1) form b: M \otimes_R M^* -> R defined by b(v, w^*) := w^*(v)."""
        ...


class _RModElements:
    r"""ElementMethods introduced by ``Modules(R)`` for elements of R-modules."""

    @abstractmethod
    def parent(self) -> RModule: ...

    @abstractmethod
    def base_ring(self) -> Ring: ...

    @abstractmethod
    def is_zero(self) -> bool: ...

    @final
    def span(self) -> SubModule:
        return self.cyclic_submodule()

    @final
    def inclusion(self) -> RModMorphism:
        Rm = self.span()
        f = Rm.inclusion()
        assert f in Rm.Hom(self.parent())
        return f

    @final
    def annihilator(self) -> Ideal:
        ideal: Ideal = self.span().annihilator()
        return ideal

    @abstractmethod
    def cyclic_submodule(self) -> SubModule: ...

    @final
    def is_primitive(self) -> bool:
        return bool(self.span().inclusion().is_primitive())

    @abstractmethod
    def __add__(self, m: RModuleElement) -> RModuleElement: ...

    @abstractmethod
    def __mul__(self, r: RingElement) -> RModuleElement: ...

    @abstractmethod
    def tensor(self, other: RModuleElement) -> RModuleElement: ...

    @final
    def __neg__(self) -> RModuleElement:
        R = self.base_ring()
        return self._lmul_(R(-1))

    @abstractmethod
    def _lmul_(self, r: RingElement) -> RModuleElement: ...

    @abstractmethod
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
    def __classcall_private__(
        cls: type[Modules], base_ring: Ring, dispatch: bool = True
    ) -> Modules:
        from sage.categories.commutative_rings import (
            CommutativeRings as SageCommutativeRings,
        )
        from sage.categories.dedekind_domains import (
            DedekindDomains as SageDedekindDomains,
        )
        from sage.categories.fields import Fields as SageFields
        from sage.categories.integral_domains import (
            IntegralDomains as SageIntegralDomains,
        )
        from sage.categories.principal_ideal_domains import (
            PrincipalIdealDomains as SagePrincipalIdealDomains,
        )

        result: Modules = super().__classcall__(cls, base_ring)
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
    def super_categories(self) -> list[Category]:
        from ..sets import Sets

        R = self.base_ring()
        return [Sets(), SageBimodules(R, R)]

    @override
    @final
    def additional_structure(self) -> None:
        r"""Return ``None`` because R-Mod morphisms are exactly bimodule morphisms."""
        return None

    # ------------------------------------------------------------------
    # Constructors
    # ------------------------------------------------------------------

    class _Constructors:
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
        def provenance(self) -> ConstructorRegistry:
            r"""Return typed provenance records for module constructors."""
            from category_specs.spec_core import constructor_registry_for_category

            return constructor_registry_for_category(
                self.category(),
                owner_category=f"Modules({self.base_ring()})",
                id_prefix="modules",
            )

        @final
        def category(self) -> RMod:
            return self._category

        @final
        def base_ring(self) -> Ring:
            base_ring: Ring = self.category().base_ring()
            return base_ring

        @final
        def _refine_constructed_module(
            self, M: RModule, category: Category
        ) -> RModule:
            return refine_category(M, category, test=False)

        @final
        def _standard_free_module_category(self) -> Category:
            C = self.category()
            return C.Free().FinitelyPresented().FiniteRank().WithOrderedBasis()

        @final
        def _finite_rank_free_module_category(self) -> Category:
            C = self.category()
            return C.Free().FiniteRank()

        @final
        def _submodule_categories(
            self, *, with_ordered_basis: bool = False
        ) -> Category:
            C = self.category()
            if with_ordered_basis:
                return C.WithOrderedBasis().Subobjects()
            return C.Subobjects()

        @final
        def _quotient_categories(
            self, *, with_ordered_basis: bool = False
        ) -> Category:
            C = self.category()
            if with_ordered_basis:
                return C.WithOrderedBasis().Quotients()
            return C.Quotients()

        @final
        def _categories_for_free_module(self, M: RModule) -> Category:
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
            from sage.tensor.modules.finite_rank_free_module import (
                FiniteRankFreeModule,
            )

            if isinstance(M, FreeQuadraticModule_generic):
                C = self.category()
                return C.WithForms().Bilinear().Quadratic()
            if isinstance(M, FreeModule_ambient_field_quotient):
                return self._quotient_categories()
            if isinstance(M, FiniteRankFreeModule):
                return self._finite_rank_free_module_category()
            if isinstance(M, FreeModule_submodule_with_basis_field):
                return self._submodule_categories(with_ordered_basis=True)
            if isinstance(M, FreeModule_submodule_field):
                return self._submodule_categories()
            if isinstance(M, RealDoubleVectorSpace_class):
                return self._standard_free_module_category()
            if isinstance(M, ComplexDoubleVectorSpace_class):
                return self._standard_free_module_category()
            if isinstance(M, FreeModule_submodule_with_basis_pid):
                return self._submodule_categories(with_ordered_basis=True)
            if isinstance(M, FreeModule_submodule_pid):
                return self._submodule_categories()
            if isinstance(M, FreeModule_ambient_field):
                return self._standard_free_module_category()
            return self._standard_free_module_category()

        @final
        def _categories_for_quotient_module(self, M: RModule) -> Category:
            from sage.modules.fg_pid.fgp_module import FGP_Module_class
            from sage.modules.quotient_module import (
                FreeModule_ambient_field_quotient,
                QuotientModule_free_ambient,
            )

            if isinstance(M, FreeModule_ambient_field_quotient):
                return self._quotient_categories()
            if isinstance(M, QuotientModule_free_ambient):
                return self._quotient_categories()
            if isinstance(M, FGP_Module_class):
                C = self.category()
                return C.FinitelyGenerated().FinitelyPresented().OverPID().Quotients()
            return self._categories_for_free_module(M)

        @final
        def _categories_for_combinatorial_free_module(self) -> Category:
            C = self.category()
            return C.Free().WithBasis().WithOrderedGeneratingSet()

        @overload
        def FreeModule(
            self,
            *,
            rank: Integer,
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def FreeModule(
            self,
            *,
            basis_keys: Set | SetFamily,
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def FreeModule(
            self,
            *,
            rank: Integer,
            with_basis: None,
            sparse: bool = False,
        ) -> RModule: ...

        @overload
        def FreeModule(
            self,
            *,
            rank: Integer,
            inner_product_matrix: Matrix,
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def FreeModule(
            self,
            *,
            rank: Integer,
            inner_product_rows: Sequence[Sequence[RingElement]],
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def FreeModule(
            self,
            *,
            rank: Integer,
            inner_product_entries: Sequence[RingElement],
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @final
        def FreeModule(
            self,
            *,
            rank: Integer | None = None,
            basis_keys: Set | SetFamily | None = None,
            sparse: bool = False,
            inner_product_matrix: Matrix | None = None,
            inner_product_rows: Sequence[Sequence[RingElement]] | None = None,
            inner_product_entries: Sequence[RingElement] | None = None,
            with_basis: str | None = "standard",
        ) -> RModule:
            from sage.matrix.constructor import matrix
            from sage.modules.free_module import FreeModule as SageFreeModule

            supplied_inner_products = sum(
                data is not None
                for data in (
                    inner_product_matrix,
                    inner_product_rows,
                    inner_product_entries,
                )
            )
            if supplied_inner_products > 1:
                raise ValueError("specify exactly one inner product input shape")
            if inner_product_rows is not None:
                inner_product_matrix = matrix(self.base_ring(), inner_product_rows)
            if inner_product_entries is not None:
                if rank is None:
                    raise ValueError("inner_product_entries requires rank")
                inner_product_matrix = matrix(
                    self.base_ring(), rank, rank, inner_product_entries
                )

            M = SageFreeModule(
                self.base_ring(),
                sparse=sparse,
                inner_product_matrix=inner_product_matrix,
                rank=rank,
                basis_keys=basis_keys,
                with_basis=with_basis,
            )
            categories = self._categories_for_free_module(M)
            return self._refine_constructed_module(M, categories)

        @overload
        def VectorSpace(
            self,
            *,
            dimension: Integer,
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def VectorSpace(
            self,
            *,
            basis_keys: Set | SetFamily,
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def VectorSpace(
            self,
            *,
            dimension: Integer,
            with_basis: None,
            sparse: bool = False,
        ) -> RModule: ...

        @overload
        def VectorSpace(
            self,
            *,
            dimension: Integer,
            inner_product_matrix: Matrix,
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def VectorSpace(
            self,
            *,
            dimension: Integer,
            inner_product_rows: Sequence[Sequence[RingElement]],
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @overload
        def VectorSpace(
            self,
            *,
            dimension: Integer,
            inner_product_entries: Sequence[RingElement],
            sparse: bool = False,
            with_basis: str = "standard",
        ) -> RModule: ...

        @final
        def VectorSpace(
            self,
            *,
            dimension: Integer | None = None,
            basis_keys: Set | SetFamily | None = None,
            sparse: bool = False,
            inner_product_matrix: Matrix | None = None,
            inner_product_rows: Sequence[Sequence[RingElement]] | None = None,
            inner_product_entries: Sequence[RingElement] | None = None,
            with_basis: str | None = "standard",
        ) -> RModule:
            from sage.matrix.constructor import matrix
            from sage.modules.free_module import VectorSpace as SageVectorSpace

            supplied_inner_products = sum(
                data is not None
                for data in (
                    inner_product_matrix,
                    inner_product_rows,
                    inner_product_entries,
                )
            )
            if supplied_inner_products > 1:
                raise ValueError("specify exactly one inner product input shape")
            if inner_product_rows is not None:
                inner_product_matrix = matrix(self.base_ring(), inner_product_rows)
            if inner_product_entries is not None:
                if dimension is None:
                    raise ValueError("inner_product_entries requires dimension")
                inner_product_matrix = matrix(
                    self.base_ring(), dimension, dimension, inner_product_entries
                )

            M = SageVectorSpace(
                self.base_ring(),
                sparse=sparse,
                inner_product_matrix=inner_product_matrix,
                dimension=dimension,
                basis_keys=basis_keys,
                with_basis=with_basis,
            )
            return self._refine_constructed_module(
                M, self._categories_for_free_module(M)
            )

        @overload
        def FreeQuadraticModule(
            self,
            *,
            rank: Integer,
            inner_product_matrix: Matrix,
            sparse: bool = False,
        ) -> RModule: ...

        @overload
        def FreeQuadraticModule(
            self,
            *,
            rank: Integer,
            inner_product_rows: Sequence[Sequence[RingElement]],
            sparse: bool = False,
        ) -> RModule: ...

        @overload
        def FreeQuadraticModule(
            self,
            *,
            rank: Integer,
            inner_product_entries: Sequence[RingElement],
            sparse: bool = False,
        ) -> RModule: ...

        @final
        def FreeQuadraticModule(
            self,
            *,
            rank: Integer,
            inner_product_matrix: Matrix | None = None,
            inner_product_rows: Sequence[Sequence[RingElement]] | None = None,
            inner_product_entries: Sequence[RingElement] | None = None,
            sparse: bool = False,
        ) -> RModule:
            from sage.matrix.constructor import matrix
            from sage.modules.free_quadratic_module import FreeQuadraticModule

            supplied_inner_products = sum(
                data is not None
                for data in (
                    inner_product_matrix,
                    inner_product_rows,
                    inner_product_entries,
                )
            )
            if supplied_inner_products != 1:
                raise ValueError("specify exactly one inner product input shape")
            if inner_product_rows is not None:
                inner_product_matrix = matrix(self.base_ring(), inner_product_rows)
            if inner_product_entries is not None:
                inner_product_matrix = matrix(
                    self.base_ring(), rank, rank, inner_product_entries
                )

            M = FreeQuadraticModule(
                self.base_ring(),
                rank,
                inner_product_matrix,
                sparse=sparse,
            )
            return self._refine_constructed_module(
                M,
                self.category().WithForms().Bilinear().Quadratic(),
            )

        @final
        def span(
            self,
            gens: Sequence[RModuleElement] | Matrix,
            check: bool = True,
            already_echelonized: bool = False,
        ) -> SubModule:
            from sage.modules.free_module import span as sage_span

            M = sage_span(
                gens,
                self.base_ring(),
                check=check,
                already_echelonized=already_echelonized,
            )
            return self._refine_constructed_module(
                M, self._categories_for_free_module(M)
            )

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
            return self._refine_constructed_module(
                M, self._categories_for_combinatorial_free_module()
            )

        @final
        def FiniteRankFreeModule(
            self,
            rank: Integer,
            name: str | None = None,
            latex_name: str | None = None,
            start_index: Integer = 0,
            output_formatter: Callable[[RingElement], str]
            | Callable[[RingElement, str], str]
            | None = None,
        ) -> FreeModuleType:
            from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule

            M = FiniteRankFreeModule(
                self.base_ring(),
                rank,
                name=name,
                latex_name=latex_name,
                start_index=start_index,
                output_formatter=output_formatter,
            )
            return self._refine_constructed_module(
                M, self._finite_rank_free_module_category()
            )

        @final
        def quotient_of_free_modules(
            self, V: FreeModuleType, W: SubModule
        ) -> QuotientModule:
            M = V.quotient_module(W)
            return self._refine_constructed_module(
                M, self._categories_for_quotient_module(M)
            )

        @final
        def quotient_module(
            self, module: RModule, submodule: SubModule, check: bool = True
        ) -> QuotientModule:
            M = module.quotient_module(submodule, check=check)
            return self._refine_constructed_module(
                M, self._categories_for_quotient_module(M)
            )

        @overload
        def FPModule(
            self,
            *,
            algebra: Algebra,
            generator_degrees: Sequence[Integer],
            relations: Sequence[Sequence[AlgebraElement]] = (),
            names: str | tuple[str, ...] | None = None,
        ) -> RModule: ...

        @overload
        def FPModule(
            self,
            *,
            defining_map: RModMorphism,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule: ...

        @overload
        def FPModule(
            self,
            *,
            module: RModule,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule: ...

        @final
        def FPModule(
            self,
            *,
            algebra: Algebra | None = None,
            generator_degrees: Sequence[Integer] | None = None,
            relations: Sequence[Sequence[AlgebraElement]] = (),
            defining_map: RModMorphism | None = None,
            module: RModule | None = None,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.modules.fp_graded.module import FPModule

            presentation_shape = algebra is not None or generator_degrees is not None
            supplied_shapes = sum(
                (
                    presentation_shape,
                    defining_map is not None,
                    module is not None,
                )
            )
            if supplied_shapes != 1:
                raise ValueError("specify exactly one FPModule input shape")
            if defining_map is not None:
                M = FPModule(defining_map, names=names)
            elif module is not None:
                assert module in self.category().FreeGradedModules(), (
                    f"Expected a free graded module: {module}"
                )
                M = FPModule(module, names=names)
            else:
                if algebra is None or generator_degrees is None:
                    raise ValueError("algebra and generator_degrees are required")
                M = FPModule(
                    algebra,
                    generator_degrees=generator_degrees,
                    relations=relations,
                    names=names,
                )
            return self._refine_constructed_module(
                M, self.category().FinitelyPresentedGradedModules()
            )

        @final
        def FreeGradedModule(
            self,
            algebra: Algebra,
            generator_degrees: Sequence[Integer],
            category: Category | None = None,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.modules.fp_graded.free_module import FreeGradedModule

            M = FreeGradedModule(
                algebra, generator_degrees, category=category, names=names
            )
            return self._refine_constructed_module(
                M, self.category().FreeGradedModules()
            )

        @final
        def OreQuotientModule(
            self, ore_polynomial_ring: OrePolynomialRing, polynomial: RingElement
        ) -> RModule:
            M = ore_polynomial_ring.quotient_module(polynomial)
            return self._refine_constructed_module(M, self.category().OreModules())

        @final
        def IntegerLattice(
            self,
            *,
            basis: Matrix | Sequence[Sequence[RingElement]] | RingElement,
            lll_reduce: bool = True,
        ) -> RModule:
            from sage.modules.free_module_integer import IntegerLattice

            M = IntegerLattice(basis, lll_reduce=lll_reduce)
            return self._refine_constructed_module(
                M, self.category().IntegerLattices()
            )

        @final
        def TorsionQuadraticForm(
            self, *, q: Matrix | Sequence[Sequence[RingElement]]
        ) -> RModule:
            from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

            M = TorsionQuadraticForm(q)
            return self._refine_constructed_module(
                M, self.category().TorsionQuadraticModules()
            )

        @final
        def ring_as_rank_one_module(self, ring: Ring | None = None) -> RModule:
            M, _, _ = self.rank_one_module_with_ring_isomorphisms(ring=ring)
            return M

        @final
        def rank_one_module_with_ring_isomorphisms(
            self, ring: Ring | None = None, basis: RingElement | None = None
        ) -> tuple[RModule, RModMorphism, RModMorphism]:
            R = self.base_ring() if ring is None else ring
            if basis is not None:
                basis = R(basis)
                if not basis.is_unit():
                    raise ValueError("basis element must be a unit")
            from sage.modules.free_module import FreeModule as SageFreeModule
            from sage.modules.free_module_morphism import (
                BaseIsomorphism1D_from_FM,
                BaseIsomorphism1D_to_FM,
            )

            M = SageFreeModule(R, 1)
            Hfrom = M.Hom(R)
            Hto = R.Hom(M)
            from_M = Hfrom.__make_element_class__(BaseIsomorphism1D_from_FM)(
                Hfrom, basis=basis
            )
            to_M = Hto.__make_element_class__(BaseIsomorphism1D_to_FM)(
                Hto, basis=basis
            )
            refined_module = self._refine_constructed_module(
                M, Modules(R).Free().FiniteRank().WithOrderedBasis()
            )
            return refined_module, from_M, to_M

        @final
        def ideal_as_submodule(self, ideal: Ideal) -> SubModule:
            from sage.modules.free_module import FreeModule as SageFreeModule

            R = ideal.ring()
            M = SageFreeModule(R, 1).submodule(
                [[generator] for generator in ideal.gens()]
            )
            return self._refine_constructed_module(M, Modules(R).RIdeals())

        @final
        def invertible_ideal_as_projective_submodule(
            self, ideal: Ideal
        ) -> ProjectiveModule:
            R = ideal.ring()
            M = self.ideal_as_submodule(ideal)
            return self._refine_constructed_module(
                M, Modules(R).Projective().RIdeals()
            )

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

            constructors = Rings().Constructors()
            base_ring = self.base_ring()
            if name is not None:
                S = (
                    constructors.PolynomialRing(
                        base_ring,
                        name=name,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                    if n is None
                    else constructors.PolynomialRing(
                        base_ring,
                        n=n,
                        name=name,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                )
            elif names is not None:
                S = (
                    constructors.PolynomialRing(
                        base_ring,
                        names=names,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                    if n is None
                    else constructors.PolynomialRing(
                        base_ring,
                        n=n,
                        names=names,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                )
            elif var_array is not None:
                assert n is not None, "Polynomial var_array construction requires n"
                S = constructors.PolynomialRing(
                    base_ring,
                    n=n,
                    var_array=var_array,
                    sparse=sparse,
                    order=order,
                    implementation=implementation,
                )
            else:
                assert n is not None, "Polynomial ring construction requires variables"
                S = constructors.PolynomialRing(
                    base_ring,
                    n=n,
                    sparse=sparse,
                    order=order,
                    implementation=implementation,
                )
            return self._refine_constructed_module(
                S, self.category().RingObjectsAsModules()
            )

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

            S = (
                Rings()
                .Constructors()
                .PowerSeriesRing(
                    self.base_ring(),
                    name=name,
                    sparse=sparse,
                    default_prec=default_prec,
                    implementation=implementation,
                )
            )
            return self._refine_constructed_module(
                S, self.category().RingObjectsAsModules()
            )

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

            S = (
                Rings()
                .Constructors()
                .MultivariatePowerSeriesRing(
                    self.base_ring(),
                    names=names,
                    num_gens=num_gens,
                    sparse=sparse,
                    default_prec=default_prec,
                    order=order,
                )
            )
            return self._refine_constructed_module(
                S, self.category().RingObjectsAsModules()
            )

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

            S = (
                Rings()
                .Constructors()
                .MultivariatePowerSeriesRingWithGeneratorPrefix(
                    self.base_ring(),
                    prefix=prefix,
                    num_gens=num_gens,
                    sparse=sparse,
                    default_prec=default_prec,
                    order=order,
                )
            )
            return self._refine_constructed_module(
                S, self.category().RingObjectsAsModules()
            )

        @overload
        def laurent_series_ring_as_module(
            self,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> RModule: ...

        @overload
        def laurent_series_ring_as_module(
            self,
            *,
            power_series_ring: Ring,
        ) -> RModule: ...

        @final
        def laurent_series_ring_as_module(
            self,
            name: str | None = None,
            *,
            power_series_ring: Ring | None = None,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            if power_series_ring is not None:
                assert name is None
                assert sparse is False
                assert default_prec is None
                assert implementation is None
                S = (
                    Rings()
                    .Constructors()
                    .LaurentSeriesRing(power_series_ring=power_series_ring)
                )
            else:
                assert name is not None
                S = (
                    Rings()
                    .Constructors()
                    .LaurentSeriesRing(
                        self.base_ring(),
                        name=name,
                        sparse=sparse,
                        default_prec=default_prec,
                        implementation=implementation,
                    )
                )
            return self._refine_constructed_module(
                S, self.category().RingObjectsAsModules()
            )

        @overload
        def puiseux_series_ring_as_module(
            self,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> RModule: ...

        @overload
        def puiseux_series_ring_as_module(
            self,
            *,
            laurent_series_ring: Ring,
        ) -> RModule: ...

        @final
        def puiseux_series_ring_as_module(
            self,
            name: str | None = None,
            *,
            laurent_series_ring: Ring | None = None,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            if laurent_series_ring is not None:
                assert name is None
                assert sparse is False
                assert default_prec is None
                assert implementation is None
                S = (
                    Rings()
                    .Constructors()
                    .PuiseuxSeriesRing(laurent_series_ring=laurent_series_ring)
                )
            else:
                assert name is not None
                S = (
                    Rings()
                    .Constructors()
                    .PuiseuxSeriesRing(
                        self.base_ring(),
                        name=name,
                        sparse=sparse,
                        default_prec=default_prec,
                        implementation=implementation,
                    )
                )
            return self._refine_constructed_module(
                S, self.category().RingObjectsAsModules()
            )

        @final
        def matrix_ring_as_module(
            self,
            n: Integer,
            sparse: bool = False,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = (
                Rings()
                .Constructors()
                .MatrixRing(
                    self.base_ring(),
                    n,
                    sparse=sparse,
                    implementation=implementation,
                )
            )
            return self._refine_constructed_module(
                S, self.category().RingObjectsAsModules()
            )
    @final
    def Constructors(self) -> Modules._Constructors:
        r"""Return the Sage module constructor collector over ``self.base_ring()``."""
        return self.__class__._Constructors(self)

    @abstractmethod
    def zero_module(self) -> RModule: ...

    @abstractmethod
    def R(self) -> FreeModuleType:
        r"""Return R as a rank 1 free R-module."""
        ...

    @abstractmethod
    def torsion_module(self, r: RingElement) -> TorsionModule:
        r"""Return R/r.  Asserts R != 0."""
        ...

    @final
    def free_module(self, n: Integer) -> FreeModuleType:
        from sage.rings.semirings.non_negative_integer_semiring import NN

        assert n in NN, f"Negative integers are not well-defined ranks: {n}"
        if n == 0:
            return self.zero_module()
        free_module: FreeModuleType = sum(n * [self.R()])
        return free_module

    @final
    def from_ring_elements(self, elts: Sequence[RingElement]) -> RModule:
        r"""Given an ordered subset {r_1, ..., r_n} of R, return
        ``M := R/r_1 \oplus ... \oplus R/r_n``, where R/0 := R.
        """
        from sage.categories.rings import Rings as SageRings

        if not elts:
            return self.zero_module()
        assert all(r.parent() in SageRings() for r in elts), (
            f"All element parents must be rings: {elts}"
        )
        R = elts[0].parent()
        assert all(r.parent() is R for r in elts), (
            f"Elements must share a common ring: {[r.parent() for r in elts]}"
        )
        zs = [r for r in elts if r.is_zero()]
        rs = [r for r in elts if not r.is_zero()]
        F = self.free_module(len(zs))
        torsion_summands: list[RModule] = [self.torsion_module(r) for r in rs]
        T = (
            self.zero_module()
            if not torsion_summands
            else torsion_summands[0].direct_sum(torsion_summands[1:])
        )
        module: RModule = F + T
        return module

    @final
    def from_invariant_factors(self, elts: Sequence[RingElement]) -> RModule:
        return self.from_ring_elements(elts)

    @final
    def from_matrix(self, M: Matrix) -> RModule:
        r"""Interpret a matrix as a representation of a morphism
        f: R^m -> R^n and return ``coker(f)``.
        """
        from .subcategories.finitely_presented_over_pid import (
            FinitelyPresentedModulesOverPID,
        )

        return FinitelyPresentedModulesOverPID.from_matrix(self, M)

    # ------------------------------------------------------------------
    # SubcategoryMethods — available on every subcategory of Modules(R)
    # ------------------------------------------------------------------

    class SubcategoryMethods:
        @final
        def Constructors(self) -> Modules._Constructors:
            r"""Return the module constructor collector for this module category."""
            return Modules._Constructors(self)
        @final
        def base_ring(self) -> Ring:
            base_ring: Ring = self.base_category().base_ring()
            return base_ring

        ## Ring properties
        @final
        def OverIntegralDomain(self) -> Category:
            return self._with_axiom("OverIntegralDomain")
        @final
        def OverDedekindDomain(self) -> Category:
            return self._with_axiom("OverDedekindDomain")
        @final
        def OverPID(self) -> Category:
            return self._with_axiom("OverPID")
        @final
        def OverCommutativeRing(self) -> Category:
            return self._with_axiom("OverCommutativeRing")
        @final
        def OverField(self) -> Category:
            return self._with_axiom("OverField")
        @final
        def OverLocalRing(self) -> Category:
            return self._with_axiom("OverLocalRing")
        @final
        def OverCompleteRing(self) -> Category:
            return self._with_axiom("OverCompleteRing")

        ## Homological properties
        @final
        def Free(self) -> Category:
            return self._with_axiom("Free")
        @final
        def Torsion(self) -> Category:
            return self._with_axiom("Torsion")
        @final
        def Torsionfree(self) -> Category:
            return self._with_axiom("Torsionfree")
        @final
        def Projective(self) -> Category:
            return self._with_axiom("Projective")

        ## Generation properties
        @final
        def WithBasis(self) -> Category:
            return self._with_axiom("WithBasis")
        @final
        def WithOrderedBasis(self) -> Category:
            return self._with_axiom("WithOrderedBasis")
        @final
        def WithOrderedGeneratingSet(self) -> Category:
            return self._with_axiom("WithOrderedGeneratingSet")
        @final
        def FinitelyGenerated(self) -> Category:
            return self._with_axiom("FinitelyGenerated")
        @final
        def FinitelyPresented(self) -> Category:
            return self._with_axiom("FinitelyPresented")
        @final
        def TensorProducts(self) -> Category:
            tensor_products: Category = TensorProductsCategory.category_of(self)
            return tensor_products
        @final
        def DualObjects(self) -> Category:
            dual_objects: Category = DualObjectsCategory.category_of(self)
            return dual_objects

        dual = DualObjects

        ## Extra structure
        @final
        def Filtered(self) -> Category:
            filtered: Category = FilteredModulesCategory.category_of(self)
            return filtered
        @final
        def Graded(self) -> Category:
            return self._with_axiom("Graded")
        @final
        def Super(self) -> Category:
            super_category: Category = SuperModulesCategory.category_of(self)
            return super_category

        ## Forms
        @final
        def WithForms(self) -> Category:
            return self._with_axiom("WithForms")
        @final
        def RIdeals(self) -> Category:
            return self._with_axiom("RIdeals")
        @final
        def RepresentationModules(self) -> Category:
            representation_modules: Category = _RepresentationModules(self.base_ring())
            return representation_modules
        @final
        def FreeGradedModules(self) -> Category:
            free_graded_modules: Category = _FreeGradedModules(self.base_ring())
            return free_graded_modules
        @final
        def FinitelyPresentedGradedModules(self) -> Category:
            finitely_presented_graded_modules: Category = (
                _FinitelyPresentedGradedModules(self.base_ring())
            )
            return finitely_presented_graded_modules
        @final
        def OreModules(self) -> Category:
            ore_modules: Category = _OreModules(self.base_ring())
            return ore_modules
        @final
        def IntegerLattices(self) -> Category:
            integer_lattices: Category = _IntegerLattices(self.base_ring())
            return integer_lattices
        @final
        def TorsionQuadraticModules(self) -> Category:
            torsion_quadratic_modules: Category = TorsionQuadraticModulesCategory(
                self.base_ring()
            )
            return torsion_quadratic_modules
        @final
        def RingObjectsAsModules(self) -> Category:
            ring_objects_as_modules: Category = _RingObjectsAsModules(
                self.base_ring()
            )
            return ring_objects_as_modules

    # ------------------------------------------------------------------
    # Method providers
    # ------------------------------------------------------------------

    ParentMethods = _RModObjects
    ElementMethods = _RModElements
    HomCategory = RModuleHomCategory

    # ------------------------------------------------------------------
    # Named subcategories
    # ------------------------------------------------------------------

    RIdeals = LazyImport("category_specs.modules.subcategories.r_ideals", "_RIdeals")

    # ------------------------------------------------------------------
    # Axiomatic subcategories — ring properties
    # ------------------------------------------------------------------

    OverIntegralDomain = LazyImport(
        "category_specs.modules.subcategories.over_integral_domain",
        "_OverIntegralDomain",
    )
    OverDedekindDomain = LazyImport(
        "category_specs.modules.subcategories.over_dedekind_domain",
        "_OverDedekindDomain",
    )
    OverPID = LazyImport("category_specs.modules.subcategories.over_pid", "_OverPID")
    OverCommutativeRing = LazyImport(
        "category_specs.modules.subcategories.over_commutative_ring",
        "_OverCommutativeRing",
    )
    OverField = LazyImport(
        "category_specs.modules.subcategories.over_field", "_OverField"
    )
    OverLocalRing = LazyImport(
        "category_specs.modules.subcategories.over_local_ring", "_OverLocalRing"
    )
    OverCompleteRing = LazyImport(
        "category_specs.modules.subcategories.over_complete_ring", "_OverCompleteRing"
    )

    # ------------------------------------------------------------------
    # Axiomatic subcategories — homological
    # ------------------------------------------------------------------

    Free = LazyImport("category_specs.modules.subcategories.free", "_Free")
    Torsion = LazyImport("category_specs.modules.subcategories.torsion", "_Torsion")
    Torsionfree = LazyImport(
        "category_specs.modules.subcategories.torsionfree", "_Torsionfree"
    )
    Projective = LazyImport(
        "category_specs.modules.subcategories.projective", "_Projective"
    )

    # ------------------------------------------------------------------
    # Axiomatic subcategories — generation
    # ------------------------------------------------------------------

    WithBasis = LazyImport(
        "category_specs.modules.subcategories.with_basis", "_WithBasis"
    )
    WithOrderedBasis = LazyImport(
        "category_specs.modules.subcategories.with_basis", "_WithOrderedBasis"
    )
    WithOrderedGeneratingSet = LazyImport(
        "category_specs.modules.subcategories.with_ordered_generating_set",
        "_WithOrderedGeneratingSet",
    )
    FinitelyGenerated = LazyImport(
        "category_specs.modules.subcategories.finitely_generated", "_FinitelyGenerated"
    )
    FinitelyPresented = LazyImport(
        "category_specs.modules.subcategories.finitely_presented", "_FinitelyPresented"
    )
    Graded = _Graded

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
    Super = LazyImport("sage.categories.super_modules", "SuperModules")

    # ------------------------------------------------------------------
    # Forms / lattice surface
    # ------------------------------------------------------------------

    WithForms = LazyImport(
        "category_specs.forms.subcategories.with_forms", "FormedModulesCategory"
    )
    # Lattices: (M, b) with M a f.g. torsionfree R-module over a domain and
    # b a symmetric nondegenerate integral bilinear form.


# ---------------------------------------------------------------------------
# Composed surfaces (aspirational; resolved once axiom chains are populated)
# ---------------------------------------------------------------------------
# TODO: immediately restrict to Dedekind domains, then to PIDs.
# Bilinear / -- [needs approach]
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
type ModulesObject = Modules.ParentMethods
type ModulesElement = Modules.ElementMethods
ModulesMorphism = RModuleHomCategory.ElementMethods
ModulesHomCategory = RModuleHomCategory
ModulesEndCategory = RModuleEndCategory
ModulesAutCategory = RModuleAutCategory
ModulesHom = RModuleHomCategory.ParentMethods
ModulesEnd = RModuleEndCategory.ParentMethods
ModulesAut = RModuleAutCategory.ParentMethods
ModulesEndomorphism = RModuleEndCategory.ElementMethods
ModulesAutomorphism = RModuleAutCategory.ElementMethods
