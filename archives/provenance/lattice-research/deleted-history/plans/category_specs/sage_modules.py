r"""Spec for the (R,R)-bimodule category ``Modules(R)``.

This is a scaffold for the lattice/module rewrite.  It defines the category
of R-modules over a base ring (or a category of base rings), together with
its axiomatic and functorial subcategories sufficient to support the
bilinear-form / lattice surface in the companion files
``sage_module_morphism.py`` and ``sage_special_modules.py``.

Naming convention used throughout this directory (canonical types):
    Matrix, vector            -- Sage primitives
    Category                  -- a Sage category
    RMod                      -- the Modules(R) category itself
    RModule                   -- an object M in RMod
    RModuleElement            -- an element in some M
    RModHomset                -- Hom_R(M, N) for some M, N in RMod
    RModMorphism              -- an element in some Hom_R(M, N)
    RModEndset                -- End_R(M) for some M in RMod
    RModEndomorphism          -- an element in some End_R(M)
    RModAutset                -- Aut_R(M) for some M in RMod
    RModAutomorphism          -- an element in some Aut_R(M)
    SubModule                 -- an element in RMod.Subobjects()
    QuotientModule            -- an element in RMod.Quotients()
    RModTwistedForms          -- the category of twisted forms
    TwistedForm               -- an object in RModTwistedForms
    RModDual                  -- the Modules dual category, equals linear twisted forms
    DualRModule               -- M^* for some RModule M; an object in RModDual
    Rings                     -- the promoted category of rings
    Ring                      -- an object in Rings
    Ideals                    -- the promoted category of ideals of R as a
                                 subcategory of Modules(R).Subobjects()
    Ideal                     -- an object in Ideals
    RingMorphism              -- a morphism in Rings
    RingEndomorphism          -- an endomorphism in Rings
    RingAutomorphism          -- an automorphism in Rings
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any

from sage.categories import category_with_axiom as _category_with_axiom
from sage.categories.bimodules import Bimodules
from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory
from sage.categories.filtered_modules import FilteredModulesCategory
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.homsets import HomsetsCategory
from sage.categories.objects import Objects
from sage.categories.quotients import QuotientsCategory
from sage.categories.sets_cat import Sets
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.super_modules import SuperModulesCategory
from sage.categories.tensor import TensorProductFunctor, TensorProductsCategory, tensor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from .sage_module_morphism import RModuleHomsets, _RModMorphisms
from .utils import partition_list

if TYPE_CHECKING:
    from sage.matrix.matrix0 import Matrix
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer

    Cardinality = Integer | InfinityElement
    Ring = Any
    RingElement = Any
    RingEndomorphism = Any
    RModule = Any
    RModuleElement = Any
    RModuleMorphism = Any
    RModuleHomset = Any
    RModuleEndSet = Any
    RModuleAutSet = Any
    DualRModule = Any
    FreeModule = Any
    TorsionModule = Any
    SubModule = Any
    QuotientModule = Any
    Ideal = Any
    RModuleForm = Any
    OrderedSet = Any
    ModuleStructure = (
        Callable[[tuple[RingElement, RModuleElement]], RModuleElement]
        | Callable[[RingElement], RingEndomorphism]
    )


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

FinSet = Sets().Finite()

_CUSTOM_AXIOMS = (
    "OverIntegralDomain",
    "OverDedekindDomain",
    "OverPID",
    "OverCommutativeRing",
    "OverField",
    "OverLocalRing",
    "OverCompleteRing",
    "Free",
    "FiniteRank",
    "Torsion",
    "Torsionfree",
    "Projective",
    "WithOrderedGeneratingSet",
    "FinitelyGenerated",
    "FinitelyPresented",
    "RIdeals",
    "WithForms",
    "Bilinear",
    "Quadratic",
    "Symmetric",
    "Alternating",
    "Nondegenerate",
    "Integral",
    "Rational",
)


def _register_custom_axioms() -> None:
    missing = tuple(
        axiom
        for axiom in _CUSTOM_AXIOMS
        if axiom not in _category_with_axiom.all_axioms
    )
    if missing:
        _category_with_axiom.all_axioms += missing


_register_custom_axioms()


# ---------------------------------------------------------------------------
# Categories of categories
# ---------------------------------------------------------------------------

class Categories(Category_singleton):
    r"""A shim to define an infty-category of (Sage) categories."""

    def super_categories(self):
        return [Objects()]

    def __contains__(self, C: Any) -> bool:
        return isinstance(C, Category)

    @classmethod
    def is_over_a_ring(cls, C: Category) -> bool:
        assert C in Categories(), f"Object is not a category: {C}"
        return any(hasattr(D, "base_ring") for D in C.super_categories())

    @classmethod
    def base_ring(cls, C: Category) -> Ring:
        base_ring_cat = next(
            (D for D in C.super_categories() if hasattr(D, "base_ring")),
            None,
        )
        assert base_ring_cat is not None, (
            f"No super category of {C} is a category over a base ring."
        )
        return base_ring_cat.base_ring()


# ---------------------------------------------------------------------------
# ParentMethods / ElementMethods for Modules(R)
# ---------------------------------------------------------------------------
# Note: these classes are bound to Modules below as inner-method providers.
# They reference Modules-level types only via string annotations.

class _RModObjects:
    r"""ParentMethods for ``Modules(R)``.

    ``linear_combination(...)`` is intentionally not provided here: when
    elements are implemented properly the parent does not need it.
    """

    def is_over_integral_domain(self) -> bool:
        return False

    def is_over_dedekind_domain(self) -> bool:
        return False

    def is_over_pid(self) -> bool:
        return False

    def is_over_commutative_ring(self) -> bool:
        return False

    def is_over_field(self) -> bool:
        return False

    def is_over_local_ring(self) -> bool:
        return False

    def is_over_complete_ring(self) -> bool:
        return False

    def is_free(self) -> bool:
        return False

    def is_torsion(self) -> bool:
        return False

    def is_torsionfree(self) -> bool:
        return False

    def is_projective(self) -> bool:
        return False

    def is_finite(self) -> bool:
        return False

    def has_ordered_generating_set(self) -> bool:
        return False

    def is_finitely_generated(self) -> bool:
        return False

    def is_finitely_presented(self) -> bool:
        return False

    def is_ideal(self) -> bool:
        return False

    @cached_method
    def tensor_square(self):
        return self.tensor_power(2)

    def tensor_power(self, n: int):
        match n:
            case 0:
                return self.base_ring()
            case _ if n >= 1:
                return tensor(n * [self])
            case _ if n <= -1:
                return tensor((-n) * [self.dual()])
            case _:
                raise ValueError(f"Unsupported tensor power: {n}")

    def tensor_module(self, p: int, q: int):
        assert p >= 0 and q >= 0, "T_R(M) is NN^2-graded."
        return tensor([self.tensor_power(p), self.dual().tensor_power(q)])

    def quotient(self, N: SubModule) -> QuotientModule:
        return N.inclusion().cokernel()

    @abstract_method
    def annihilator(self) -> Ideal: ...

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
    def dual(self) -> DualRModule: ...

    @abstract_method
    def Hom(self, N: RModule) -> RModuleHomset: ...

    @abstract_method
    def End(self) -> RModuleEndSet: ...

    @abstract_method
    def Aut(self) -> RModuleAutSet: ...

    @abstract_method
    def determinant_module(self) -> RModule:
        r"""Return \Lambda^n_R(M), the top exterior power of M."""
        ...

    @abstract_method
    def __contains__(self, data: RModuleElement | SubModule) -> bool:
        r"""Concrete impls dispatch on RModuleElement vs SubModule."""
        ...

    @abstract_method
    def cardinality(self) -> Cardinality: ...

    @abstract_method
    def is_isomorphic_to(self, other: RModule) -> bool: ...

    @abstract_method
    def is_submodule_of(self, other: RModule) -> bool: ...

    @abstract_method
    def direct_sum(self, other: RModule | Sequence[RModule]) -> RModule: ...

    @abstract_method
    def tensor(self, other: RModule | Sequence[RModule]) -> RModule: ...

    @abstract_method
    def span(self, elts: RModuleElement | Sequence[RModuleElement]) -> SubModule: ...

    def __add__(self, other: RModule) -> RModule:
        return self.direct_sum(other)

    @abstract_method
    def __mul__(self, other: RingElement | RModule) -> RModule:
        r"""``r * M`` = submodule spanned by ``{r*m | m in M}``;
        ``N * M`` = the tensor product ``M \otimes_R N``.
        """
        ...

    # Do not define: submodule(), _mul_, _rmul_, _lmul_

    @abstract_method
    def natural_pairing(self) -> RModuleForm:
        r"""The (1,1) form b: M \otimes_R M^* -> R defined by
        b(v, w^*) := w^*(v).
        """
        ...


class _RModElements:

    def span(self) -> SubModule:
        return self.parent().span([self])

    def inclusion(self) -> RModuleMorphism:
        Rm = self.span()
        f = Rm.inclusion()
        assert f in Rm.Hom(self.parent())
        return f

    def annihilator(self) -> Ideal:
        return self.span().annihilator()

    @abstract_method
    def cyclic_submodule(self) -> SubModule: ...

    def is_primitive(self) -> bool:
        return self.span().inclusion().is_primitive()

    @abstract_method
    def __add__(self, m: RModuleElement) -> RModuleElement: ...

    @abstract_method
    def __mul__(self, r: RingElement) -> RModuleElement: ...

    def __neg__(self) -> RModuleElement:
        R = self.base_ring()
        return R(-1) * self

    @abstract_method
    def _lmul_(self, r: RingElement) -> RModuleElement: ...

    @abstract_method
    def _rmul_(self, r: RingElement) -> RModuleElement: ...

    # TODO: define R*m := m.span() when R == m.base_ring(), or base-change.


# ---------------------------------------------------------------------------
# Functorial constructions (Subobjects / Quotients / Tensor / Cartesian / Dual)
# ---------------------------------------------------------------------------

class _DualObjects(DualObjectsCategory):
    r"""Dual modules M^* := Hom_R(M, R) viewed as integral linear forms."""

    def extra_super_categories(self):
        r"""The dual M^* of an R-module is an integral linear form, i.e. an
        object of ``Modules(R).Homsets().Forms().Linear().Integral()``.
        """
        return [self.base_category().Homsets().Forms().Linear().Integral()]


class _Subobjects(SubobjectsCategory):
    r"""Submodule category.  Extends ``RegressiveCovariantConstructionCategory``
    so ``C.Subobjects()`` is always a subcategory of ``C``.

    TODO: enumerate methods already provided by Sage's SubobjectsCategory.
    """

    @abstract_method
    def as_subobject_of_self(self, M: RModule) -> SubModule:
        r"""Regard M as a submodule of itself via the identity."""
        ...

    class ParentMethods:
        @abstract_method
        def ambient_module(self) -> RModule:
            r"""The ambient R-module of which ``self`` is a submodule."""
            ...

        @abstract_method
        def inclusion(self): ...

        @abstract_method
        def intersect(self, N: SubModule) -> SubModule: ...

        def __and__(self, N: SubModule) -> SubModule:
            return self.intersect(N)

        def index(self) -> Cardinality:
            return self.inclusion().index()

        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        def lift(self, m: RModuleElement) -> RModuleElement:
            return self.inclusion()(m)

        @abstract_method
        def saturation(self) -> SubModule: ...

        @abstract_method
        def __le__(self, other: RModule) -> bool: ...

        def quotient_module(self) -> QuotientModule:
            return self.inclusion().cokernel()


class _Quotients(QuotientsCategory):
    r"""Quotient module category.  Extends
    ``RegressiveCovariantConstructionCategory`` so ``C.Quotients()`` is always
    a subcategory of ``C``.

    TODO: enumerate methods already provided by Sage's QuotientsCategory.
    """

    class ParentMethods:
        @abstract_method
        def projection(self): ...

    class ElementMethods:
        def lift(self) -> RModuleElement:
            return self.projection().lift(self)


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products of R-modules.

    TODO: verify
    r * (m_1 \otimes ... \otimes m_n)
        = (r * m_1) \otimes ... \otimes m_n
        = m_1 \otimes ... \otimes (r * m_n)
    holds at the level of the spec.
    """

    @cached_method
    def extra_super_categories(self):
        r"""Declare that M \otimes_R N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        def construction(self):
            factors = self.tensor_factors()
            return (TensorProductFunctor(), factors)

        @abstract_method
        def tensor_factors(self) -> list[RModule]: ...

        @abstract_method
        def lift_from_product(
            self, elts: Sequence[RModuleElement]
        ) -> RModuleElement:
            r"""Given an ordered set {m_1, ..., m_n} with m_i in M_i, where
            this module is M = M_1 \otimes_R ... \otimes_R M_n, lift the
            product element (m_1, ..., m_n) to m_1 \otimes ... \otimes m_n.
            """
            ...


class _CartesianProducts(CartesianProductsCategory):
    def extra_super_categories(self):
        r"""Declare that M x N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        def __init_extra__(self):
            factors = self._sets
            assert len(factors) > 0, f"No factors found in {self}: {factors}"
            R = factors[0].base_ring()
            assert all(Mi.base_ring() is R for Mi in factors)
            self._base = R

    class ElementMethods:
        def _lmul_(self, x: Any):
            return self.parent()._cartesian_product_of_elements(
                x * y for y in self.cartesian_factors()
            )


# ---------------------------------------------------------------------------
# Forms-axiom subcategory placeholders (wired into Modules.WithForms below)
# ---------------------------------------------------------------------------

class _WithForms(CategoryWithAxiom_over_base_ring):
    r"""Non-full subcategory of pairs (M, f) with f a form on M."""

    class ParentMethods:
        @abstract_method
        def form(self) -> RModuleMorphism: ...

    class SubcategoryMethods:
        @cached_method
        def Bilinear(self):
            r"""(M, b) with b: M \otimes_R M -> S, possibly degenerate."""
            return self._with_axiom("Bilinear")

        @cached_method
        def Quadratic(self):
            r"""(M, q) with q: M -> S^\sigma, possibly degenerate."""
            return self._with_axiom("Quadratic")

        @cached_method
        def Symmetric(self):
            return self._with_axiom("Symmetric")

        @cached_method
        def Alternating(self):
            return self._with_axiom("Alternating")

        @cached_method
        def Nondegenerate(self):
            return self._with_axiom("Nondegenerate")

        @cached_method
        def Integral(self):
            return self._with_axiom("Integral")

        @cached_method
        def Rational(self):
            return self._with_axiom("Rational")


class _BilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules with a bilinear form b: M \otimes_R M -> S."""

    class ParentMethods:
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v, w)


class _QuadraticModules(CategoryWithAxiom_over_base_ring):
    r"""Modules with a quadratic form q: M -> S^\sigma."""

    class ParentMethods:
        def q(self, v: RModuleElement) -> RModuleElement:
            return self.form().q(v)


# ---------------------------------------------------------------------------
# Base-ring property subcategories
# ---------------------------------------------------------------------------

class _OverIntegralDomain(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_integral_domain()

    class ParentMethods:
        def is_over_integral_domain(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _OverDedekindDomain(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        return [self.base_category().OverIntegralDomain()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_dedekind_domain()

    class ParentMethods:
        def is_over_dedekind_domain(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _OverPID(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        return [self.base_category().OverDedekindDomain()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_pid()

    class ParentMethods:
        def is_over_pid(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _OverCommutativeRing(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_commutative_ring()

    class ParentMethods:
        def is_over_commutative_ring(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _OverField(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        return [self.base_category().OverPID()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_field()

    class ParentMethods:
        def is_over_field(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _OverLocalRing(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_local_ring()

    class ParentMethods:
        def is_over_local_ring(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _OverCompleteRing(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_complete_ring()

    class ParentMethods:
        def is_over_complete_ring(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# Axiomatic subcategories (Free / Torsion / Torsionfree / Projective)
# ---------------------------------------------------------------------------

class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        r"""A finite-rank free module is exactly a finitely generated free
        module.

        TODO: a finite-rank free module over a finite ring is itself finite.
        TODO: externalize this category entirely.
        """
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...


class _Free(CategoryWithAxiom_over_base_ring):
    r"""Free R-modules.  Does not assume finitely generated or finitely
    presented; e.g. ``\bigoplus_{z \in CC} CC`` is a free CC-module.
    """

    def extra_super_categories(self):
        r"""Every free R-module is projective."""
        return [self.base_category().Projective()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_free()

    class SubcategoryMethods:
        @cached_method
        def FiniteRank(self):
            r"""Rank is only well-defined for free modules.  This is the
            subcategory where the rank is finite, so M \cong R^n for some
            n < \infty.
            """
            return self._with_axiom("FiniteRank")

    FiniteRank = _FreeFiniteRank

    class ParentMethods:
        def is_free(self) -> bool:
            return True

        @abstract_method
        def rank(self) -> Cardinality:
            r"""Rank is only well-defined for free R-modules; equals the
            cardinality of any generating set (which may be infinite).
            """
            return self.gens().cardinality()


class _Torsion(CategoryWithAxiom_over_base_ring):
    r"""TODO: a torsion module over a finite ring is finite."""
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_torsion()

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _Torsionfree(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_torsionfree()

    class ParentMethods:
        def is_torsionfree(self) -> bool:
            return True

        # override
        def annihilator(self) -> Ideal:
            r"""Ann_R(M) = <0>, the zero ideal of R regarded as an
            R-submodule of R.
            """
            R = self.base_ring()
            return R.ideal(R.zero())

    class ElementMethods: ...
    class MorphismMethods: ...


class _Projective(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_projective()

    class ParentMethods:
        def is_projective(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# Generation properties
# ---------------------------------------------------------------------------

class _WithOrderedGeneratingSet(CategoryWithAxiom_over_base_ring):
    r"""There exists an ordered set ``S = {s_1 <= s_2 <= ...}`` and a
    surjection ``f: R^S \cong R[s_1] \oplus R[s_2] \oplus ... -> M`` where
    the direct sum is ordered.  ``S`` need not be finite.
    """

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_generating_set()

    class ParentMethods:
        def has_ordered_generating_set(self) -> bool:
            return True

        @abstract_method
        def gens(self) -> OrderedSet: ...

        def ngens(self) -> Cardinality:
            return self.gens().cardinality()

        def gen(self, i):
            return self.gens()[i]

    class Homsets(HomsetsCategory):
        class ParentMethods:
            @abstract_method
            def from_function(self, f: Callable[[Any], Any]):
                r"""A morphism f: M_1 -> M_2 can be defined from a
                set-theoretic function f: S_1 -> S_2 on the generating sets.
                """
                ...

    class ElementMethods: ...

    class MorphismMethods:
        @abstract_method
        def to_function(self) -> Callable[[RModuleElement], RModuleElement]: ...


class _FinitelyGenerated(CategoryWithAxiom_over_base_ring):
    r"""Modules M which admit a surjection f: R^n -> M for some n < \infty.

    Implies a preferred choice of generating set.  Does NOT imply finitely
    presented: ker(f) need not be finitely generated.  Counterexample: any
    ideal I in a non-Noetherian ring.
    """

    def extra_super_categories(self):
        return [self.base_category().WithOrderedGeneratingSet()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_finitely_generated()

    class ParentMethods:
        def is_finitely_generated(self) -> bool:
            return True


class _FinitelyPresented(CategoryWithAxiom_over_base_ring):
    r"""Modules M that can be written as <S | R> with S \subseteq M a finite
    generating set and R a finite set of relations.

    Equivalently, M can be written as ``M := coker_R(f: R^m -> R^n)``.
    Finitely presented implies finitely generated, but the converse fails:
    if R is non-Noetherian and I \subseteq R is an ideal that is not
    finitely generated, then R/I is finitely generated but not finitely
    presented (the presentation 0 -> I -> R -> R/I -> 0 has non-fg kernel).
    """

    def extra_super_categories(self):
        r"""Finitely presented means there is a preferred finite presentation.

        If the base ring (or category of base rings) is finite, then every
        finitely presented module is itself finite.
        """
        result = [self.base_category().FinitelyGenerated()]
        R = self.base_ring()
        if (R in Categories() and R.is_subcategory(FinSet)) or R in FinSet:
            # ``Modules(PrincipalIdealDomains())`` is admissible, so
            # ``base_ring`` may itself be a category of rings.
            result.append(FinSet)
        return result

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_finitely_presented()

    class ParentMethods:
        def is_finitely_presented(self) -> bool:
            return True


# ---------------------------------------------------------------------------
# Ideals as a named subcategory of Modules(R).Subobjects()
# ---------------------------------------------------------------------------

class _RIdeals(CategoryWithAxiom_over_base_ring):
    r"""Ideals of R viewed as submodules of R^1.

    This is the named-subcategory entry point ``Modules(R).RIdeals``; the
    parallel ring-side refinement lives in the private ring ideal bridge.
    """

    def extra_super_categories(self):
        return [self.base_category().Subobjects()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_ideal()

    class ParentMethods:
        def is_ideal(self) -> bool:
            return True

        # gens() not defined unless R is Noetherian.
        # don't leak the sage ideal: refine all ring-related categories
        # Should hook into a redefinition that overrides existing ideals category
        ...

    class ElementMethods: ...
    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# The Modules(R) category
# ---------------------------------------------------------------------------

class Modules(Category_module):

    @staticmethod
    def __classcall_private__(cls, base_ring, dispatch=True):
        # Imports inside method to avoid cycles at module load.
        from sage.categories.commutative_rings import CommutativeRings
        from sage.categories.dedekind_domains import DedekindDomains
        from sage.categories.fields import Fields
        from sage.categories.integral_domains import IntegralDomains
        from sage.categories.principal_ideal_domains import PrincipalIdealDomains

        result = super().__classcall__(cls, base_ring)
        if not dispatch:
            return result
        # Cascade from most structure to least.
        if base_ring in Fields():
            return result._with_axiom("OverField")
        if base_ring in PrincipalIdealDomains():
            # Every field is a PID
            return result._with_axiom("OverPID")
        if base_ring in DedekindDomains():
            # Every PID is a Dedekind domain
            return result._with_axiom("OverDedekindDomain")
        if base_ring in IntegralDomains():
            # Every Dedekind domain is an integral domain
            return result._with_axiom("OverIntegralDomain")
        if base_ring in CommutativeRings():
            return result._with_axiom("OverCommutativeRing")
        # TODO: full ring dispatching.
        # TODO: handle Noetherian non-commutative rings.
        # TODO: layer these subcategories appropriately.
        # No special axioms for non-commutative rings yet.
        return result

    def super_categories(self):
        R = self.base_ring()
        return [Bimodules(R, R)]

    def additional_structure(self):
        r"""Return ``None`` if this is a full subcategory of
        ``self.super_categories()``; return ``self`` otherwise.

        Here, R-Mod morphisms are exactly (R, R)-biMod morphisms.
        """
        return None

    # Constructors

    def zero_module(self) -> RModule: ...

    def R(self) -> FreeModule:
        r"""Return R as a rank 1 free R-module."""
        ...

    def torsion_module(self, r: RingElement) -> TorsionModule:
        r"""Return R/r.  Asserts R != 0."""
        ...

    def free_module(self, n: int) -> FreeModule:
        from sage.rings.semirings.non_negative_integer_semiring import NN
        assert n in NN, f"Negative integers are not well-defined ranks: {n}"
        if n == 0:
            return self.zero_module()
        return sum(n * [self.R()])

    def from_ring_elements(self, elts: Sequence[RingElement]) -> RModule:
        r"""Given an ordered subset {r_1, ..., r_n} of R, return
        ``M := R/r_1 \oplus ... \oplus R/r_n``, where R/0 := R.
        """
        from sage.categories.rings import Rings as _Rings
        if not elts:
            return self.zero_module()
        assert all(r.parent() in _Rings() for r in elts), (
            f"All element parents must be rings: {elts}"
        )
        R = elts[0].parent()
        assert all(r.parent() is R for r in elts), (
            f"Elements must share a common ring: {[r.parent() for r in elts]}"
        )
        zs, rs = partition_list(elts, lambda x: x.is_zero())
        F = self.free_module(len(zs))
        T = sum(self.torsion_module(r) for r in rs)
        return F + T

    def from_invariant_factors(self, elts: Sequence[RingElement]) -> RModule:
        return self.from_ring_elements(elts)

    def from_matrix(self, M: Matrix) -> RModule:
        r"""Interpret a matrix as a representation of a morphism
        f: R^m -> R^n and return ``coker(f)``.
        """
        if hasattr(M, "elementary_divisors"):
            return self.from_ring_elements(M.elementary_divisors())
        if hasattr(M, "smith_form"):
            D, _, _ = M.smith_form()
            return self.from_ring_elements(D.diagonal())
        raise TypeError(
            f"Matrix {M} does not appear to support elementary_divisors "
            f"or smith_form."
        )

    class SubcategoryMethods:
        r"""Methods available on every subcategory, not just Modules(R)."""

        @cached_method
        def base_ring(self) -> Ring:
            return Categories.base_ring(self)

        # ---- Axiomatic subcategories -----------------------------------
        # TODO: attach axiom automatically based on R in init.

        ## Ring properties

        @cached_method
        def OverIntegralDomain(self):
            return self._with_axiom("OverIntegralDomain")

        @cached_method
        def OverDedekindDomain(self):
            return self._with_axiom("OverDedekindDomain")

        @cached_method
        def OverPID(self):
            return self._with_axiom("OverPID")

        @cached_method
        def OverCommutativeRing(self):
            return self._with_axiom("OverCommutativeRing")

        @cached_method
        def OverField(self):
            return self._with_axiom("OverField")

        @cached_method
        def OverLocalRing(self):
            return self._with_axiom("OverLocalRing")

        @cached_method
        def OverCompleteRing(self):
            return self._with_axiom("OverCompleteRing")

        ## Homological properties

        @cached_method
        def Free(self):
            return self._with_axiom("Free")

        @cached_method
        def Torsion(self):
            return self._with_axiom("Torsion")

        @cached_method
        def Torsionfree(self):
            return self._with_axiom("Torsionfree")

        @cached_method
        def Projective(self):
            return self._with_axiom("Projective")

        ## Generation properties

        @cached_method
        def WithOrderedGeneratingSet(self):
            return self._with_axiom("WithOrderedGeneratingSet")

        @cached_method
        def FinitelyGenerated(self):
            return self._with_axiom("FinitelyGenerated")

        @cached_method
        def FinitelyPresented(self):
            return self._with_axiom("FinitelyPresented")

        # ---- Functorial constructions -----------------------------------

        @cached_method
        def Subobjects(self):
            return SubobjectsCategory.category_of(self)

        @cached_method
        def Quotients(self):
            return QuotientsCategory.category_of(self)

        @cached_method
        def TensorProducts(self):
            return TensorProductsCategory.category_of(self)

        @cached_method
        def DualObjects(self):
            return DualObjectsCategory.category_of(self)

        dual = DualObjects  # Convenience alias

        ## Extra structure

        @cached_method
        def Filtered(self):
            return FilteredModulesCategory.category_of(self)

        @cached_method
        def Graded(self):
            return GradedModulesCategory.category_of(self)

        @cached_method
        def Super(self):
            return SuperModulesCategory.category_of(self)

        # ---- Axiomatic extra structure ---------------------------------

        @cached_method
        def WithForms(self):
            return self._with_axiom("WithForms")

        @cached_method
        def RIdeals(self):
            return self._with_axiom("RIdeals")

    # ----- Method providers (parents/elements/morphisms/homsets) ------------

    ParentMethods = _RModObjects
    ElementMethods = _RModElements
    MorphismMethods = _RModMorphisms
    Homsets = RModuleHomsets

    # ----- Named subcategories ----------------------------------------------

    RIdeals = _RIdeals

    # ----- Axiomatic subcategories ------------------------------------------

    OverIntegralDomain = _OverIntegralDomain
    OverDedekindDomain = _OverDedekindDomain
    OverPID = _OverPID
    OverCommutativeRing = _OverCommutativeRing
    OverField = _OverField
    OverLocalRing = _OverLocalRing
    OverCompleteRing = _OverCompleteRing

    Free = _Free
    Torsion = _Torsion
    Torsionfree = _Torsionfree
    Projective = _Projective

    ## Generation properties
    WithOrderedGeneratingSet = _WithOrderedGeneratingSet
    FinitelyGenerated = _FinitelyGenerated
    FinitelyPresented = _FinitelyPresented

    # ----- Functorial constructions ----------------------------------------

    Subobjects = _Subobjects
    SubModules = Subobjects
    Quotients = _Quotients
    TensorProducts = _TensorProducts
    CartesianProducts = _CartesianProducts
    DualObjects = _DualObjects

    ## Extra structure
    Filtered = LazyImport('sage.categories.filtered_modules', 'FilteredModules')
    Graded = LazyImport('sage.categories.graded_modules', 'GradedModules')
    Super = LazyImport('sage.categories.super_modules', 'SuperModules')

    # ----- Forms / lattice surface -----------------------------------------

    WithForms = _WithForms          # Non-full subcategory of pairs (M, f).
    Bilinear = _BilinearModules     # (M, b): b: M \otimes_R M -> S.
    Quadratic = _QuadraticModules   # (M, q): q: M -> S^\sigma.
    # Lattices: (M, b) with M a f.g. torsionfree R-module over a domain and
    # b a symmetric nondegenerate integral bilinear form.


# ---------------------------------------------------------------------------
# Composed surfaces (aspirational; resolved once axiom chains are populated)
# ---------------------------------------------------------------------------
# TODO: immediately restrict to Dedekind domains, then to PIDs.  Bilinear /
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
# TODO: subcategory-specific surface
# ---------------------------------------------------------------------------
# - to_matrix
# - identify when Hom_R(M, N) is a matrix algebra
# - identify when End_R(M) is a matrix algebra
# - identify when Aut_R(M) is a subgroup of (GL_n(R), *)
# - iteration on countable objects
# - __contains__ methods
# - to/from_X for X = dict, images, matrix, function


# ---------------------------------------------------------------------------
# Wire custom axiom classes.
# ---------------------------------------------------------------------------

for _axiom, _category_class in (
    ("OverIntegralDomain", _OverIntegralDomain),
    ("OverDedekindDomain", _OverDedekindDomain),
    ("OverPID", _OverPID),
    ("OverCommutativeRing", _OverCommutativeRing),
    ("OverField", _OverField),
    ("OverLocalRing", _OverLocalRing),
    ("OverCompleteRing", _OverCompleteRing),
    ("Free", _Free),
    ("Torsion", _Torsion),
    ("Torsionfree", _Torsionfree),
    ("Projective", _Projective),
    ("WithOrderedGeneratingSet", _WithOrderedGeneratingSet),
    ("FinitelyGenerated", _FinitelyGenerated),
    ("FinitelyPresented", _FinitelyPresented),
    ("RIdeals", _RIdeals),
    ("WithForms", _WithForms),
    ("Bilinear", _BilinearModules),
    ("Quadratic", _QuadraticModules),
):
    _category_class._base_category_class_and_axiom = (Modules, _axiom)

_FreeFiniteRank._base_category_class_and_axiom = (_Free, "FiniteRank")

# The specialized ``FinitelyPresented() ∩ OverPID()`` implementation in
# ``sage_special_modules`` is intentionally not installed here yet.  Installing
# it as ``_FinitelyPresented.OverPID`` recursively re-enters
# ``FinitelyPresented().OverPID()`` once ``OverPID`` is registered as a real
# axiom.  The generic axiom join composes correctly and keeps the category
# surface usable until the meet class is wired with a non-recursive base.
