"""Static ring category surface for the module redesign.

This file defines a new ``Rings`` category as a staged replacement for Sage's
ring category.  Every named category below is mathematical: it records the
expected Sage-backed method surface and has immediate supercategories in
existing Sage ring categories where Sage provides them.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, overload, override

from sage.categories.commutative_ring_ideals import CommutativeRingIdeals
from sage.categories.rings import Rings as SageRings
from sage.matrix.matrix_space import MatrixSpace
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer
from sage.rings.number_field.number_field import NumberField_cyclotomic

from ..cat import Cat, Category, Category_ideal, Category_singleton
from ..modules import Modules
from ..utils import refine_category
from .homsets import RingAutCategory, RingEndCategory, RingHomCategory
from .matrix_algebras import (
    _MatrixAlgebras,
)
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.rings_over import _RingsOver
from .subcategories.constructions.rings_under import _RingsUnder
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

_CommutativeRings = LazyImport("category_specs.rings.subcategories.commutative", "_CommutativeRings")
_FiniteRings = LazyImport("category_specs.rings.subcategories.finite", "_FiniteRings")
_DivisionRings = LazyImport("category_specs.rings.subcategories.division", "_DivisionRings")
_TopologicalRings = LazyImport("category_specs.rings.subcategories.topological", "_TopologicalRings")
_Fields = LazyImport("category_specs.rings.subcategories.field", "_Fields")
_IntegralDomains = LazyImport("category_specs.rings.subcategories.integral_domain", "_IntegralDomains")
_NoetherianRings = LazyImport("category_specs.rings.subcategories.noetherian", "_NoetherianRings")
_ReducedRings = LazyImport("category_specs.rings.subcategories.reduced", "_ReducedRings")
_GcdDomains = LazyImport("category_specs.rings.subcategories.gcd_domain", "_GcdDomains")
_UniqueFactorizationDomains = LazyImport("category_specs.rings.subcategories.unique_factorization_domain", "_UniqueFactorizationDomains")
_PrincipalIdealDomains = LazyImport("category_specs.rings.subcategories.principal_ideal_domain", "_PrincipalIdealDomains")
_EuclideanDomains = LazyImport("category_specs.rings.subcategories.euclidean_domain", "_EuclideanDomains")
_IntegrallyClosedDomains = LazyImport("category_specs.rings.subcategories.integrally_closed_domain", "_IntegrallyClosedDomains")
_DedekindDomains = LazyImport("category_specs.rings.subcategories.dedekind_domain", "_DedekindDomains")
ApproximateRingsCategory = LazyImport("category_specs.rings.subcategories.approximate", "ApproximateRingsCategory")
_ValuedRings = LazyImport("category_specs.rings.subcategories.valued", "_ValuedRings")
_DiscreteValuationRings = LazyImport("category_specs.rings.subcategories.discrete_valuation_ring", "_DiscreteValuationRings")
_DiscreteValuationFields = LazyImport("category_specs.rings.subcategories.discrete_valuation_field", "_DiscreteValuationFields")
_CompleteRings = LazyImport("category_specs.rings.subcategories.complete", "_CompleteRings")
_LocalRings = LazyImport("category_specs.rings.subcategories.local", "_LocalRings")
_CompleteDiscreteValuationObjects = LazyImport("category_specs.rings.subcategories.complete_discrete_valuation_object", "_CompleteDiscreteValuationObjects")
_CompleteDiscreteValuationRings = LazyImport("category_specs.rings.subcategories.complete_discrete_valuation_ring", "_CompleteDiscreteValuationRings")
_CompleteDiscreteValuationFields = LazyImport("category_specs.rings.subcategories.complete_discrete_valuation_field", "_CompleteDiscreteValuationFields")
_FiniteFields = LazyImport("category_specs.rings.subcategories.finite_field", "_FiniteFields")
_NumberFields = LazyImport("category_specs.rings.subcategories.number_field", "_NumberFields")
_AlgebraicallyClosedFields = LazyImport("category_specs.rings.subcategories.algebraically_closed_field", "_AlgebraicallyClosedFields")
_LocalFields = LazyImport("category_specs.rings.subcategories.local_field", "_LocalFields")
_GlobalFields = LazyImport("category_specs.rings.subcategories.global_field", "_GlobalFields")
_ArchimedeanGlobalFields = LazyImport("category_specs.rings.subcategories.archimedean_global_field", "_ArchimedeanGlobalFields")
_NonArchimedeanGlobalFields = LazyImport("category_specs.rings.subcategories.nonarchimedean_global_field", "_NonArchimedeanGlobalFields")
_QuadraticNumberFields = LazyImport("category_specs.rings.subcategories.quadratic_number_field", "_QuadraticNumberFields")
_CyclotomicFields = LazyImport("category_specs.rings.subcategories.cyclotomic_field", "_CyclotomicFields")
_QuotientFields = LazyImport("category_specs.rings.subcategories.quotient_field", "_QuotientFields")
_PAdicRings = LazyImport("category_specs.rings.subcategories.p_adic_ring", "_PAdicRings")
_AlgebraicFields = LazyImport("category_specs.rings.subcategories.algebraic_field", "_AlgebraicFields")
_IntegerModRings = LazyImport("category_specs.rings.subcategories.integer_mod_ring", "_IntegerModRings")
_RealPrecisionFields = LazyImport("category_specs.rings.subcategories.real_precision_field", "_RealPrecisionFields")
_ComplexPrecisionFields = LazyImport("category_specs.rings.subcategories.complex_precision_field", "_ComplexPrecisionFields")
_ScientificNotationFields = LazyImport("category_specs.rings.subcategories.scientific_notation_field", "_ScientificNotationFields")
_RealFields = LazyImport("category_specs.rings.subcategories.real_field", "_RealFields")
_ComplexFields = LazyImport("category_specs.rings.subcategories.complex_field", "_ComplexFields")
_RealDoubleFields = LazyImport("category_specs.rings.subcategories.real_double_field", "_RealDoubleFields")
_ComplexDoubleFields = LazyImport("category_specs.rings.subcategories.complex_double_field", "_ComplexDoubleFields")
_RealIntervalFields = LazyImport("category_specs.rings.subcategories.real_interval_field", "_RealIntervalFields")
_ComplexIntervalFields = LazyImport("category_specs.rings.subcategories.complex_interval_field", "_ComplexIntervalFields")
_RealBallFields = LazyImport("category_specs.rings.subcategories.real_ball_field", "_RealBallFields")
_ComplexBallFields = LazyImport("category_specs.rings.subcategories.complex_ball_field", "_ComplexBallFields")
_QQbar = LazyImport("category_specs.rings.subcategories.algebraic_closure_of_rational_field", "_QQbar")
_AA = LazyImport("category_specs.rings.subcategories.real_algebraic_field", "_AA")
_ZZ = LazyImport("category_specs.rings.subcategories.integer_ring", "_ZZ")
_QQ = LazyImport("category_specs.rings.subcategories.rational_field", "_QQ")
_RR = LazyImport("category_specs.rings.subcategories.real_field_53", "_RR")
_CC = LazyImport("category_specs.rings.subcategories.complex_field_53", "_CC")
_Zp = LazyImport("category_specs.rings.subcategories.p_adic_integer_ring", "_Zp")
_Qp = LazyImport("category_specs.rings.subcategories.p_adic_field", "_Qp")
_PolynomialRings = LazyImport("category_specs.rings.subcategories.polynomial_ring", "_PolynomialRings")
_PuiseuxSeriesRings = LazyImport("category_specs.rings.subcategories.puiseux_series_ring", "_PuiseuxSeriesRings")
_LaurentSeriesRings = LazyImport("category_specs.rings.subcategories.laurent_series_ring", "_LaurentSeriesRings")
_PowerSeriesRings = LazyImport("category_specs.rings.subcategories.power_series_ring", "_PowerSeriesRings")

if TYPE_CHECKING:
    from ..types import (
        Cardinality,
        FreeModule,
        Ideal,
        Matrix,
        Monoid,
        Polynomial,
        Ring,
        RingElement,
        RingMorphism,
        TermOrder,
    )


# ---------------------------------------------------------------------------
# Ring parent method surface — ABC, no default return values
# ---------------------------------------------------------------------------


class _RingObjectMethods:
    r"""Abstract parent methods for all objects in ``Rings``."""

    @abstract_method
    def is_exact(self) -> bool: ...

    @abstract_method
    def is_commutative_ring(self) -> bool: ...

    @abstract_method
    def is_division_ring(self) -> bool: ...

    @abstract_method
    def is_finite(self) -> bool: ...

    @abstract_method
    def is_topological_ring(self) -> bool: ...

    @abstract_method
    def is_valued_ring(self) -> bool: ...

    @abstract_method
    def is_discrete_valuation_ring(self) -> bool: ...

    @abstract_method
    def is_discrete_valuation_field(self) -> bool: ...

    @abstract_method
    def is_complete_discrete_valuation_ring(self) -> bool: ...

    @abstract_method
    def is_complete_discrete_valuation_field(self) -> bool: ...

    @abstract_method
    def is_pid(self) -> bool: ...

    @abstract_method
    def is_gcd_domain(self) -> bool: ...

    @abstract_method
    def is_unique_factorization_domain(self, proof: bool = True) -> bool: ...

    @abstract_method
    def is_euclidean_domain(self) -> bool: ...

    @abstract_method
    def is_reduced(self) -> bool: ...

    @abstract_method
    def is_dedekind_domain(self) -> bool: ...

    @abstract_method
    def is_finite_field(self) -> bool: ...

    @abstract_method
    def is_number_field(self) -> bool: ...

    @abstract_method
    def is_quotient_field(self) -> bool: ...

    @abstract_method
    def is_local_ring(self) -> bool: ...

    @abstract_method
    def is_complete_ring(self) -> bool: ...

    @abstract_method
    def is_polynomial_ring(self) -> bool: ...

    @abstract_method
    def is_power_series_ring(self) -> bool: ...

    @abstract_method
    def is_laurent_series_ring(self) -> bool: ...

    @abstract_method
    def is_puiseux_series_ring(self) -> bool: ...

    @abstract_method
    def is_local_field(self) -> bool: ...

    @abstract_method
    def is_global_field(self) -> bool: ...

    @abstract_method
    def is_archimedean_global_field(self) -> bool: ...

    @abstract_method
    def is_nonarchimedean_global_field(self) -> bool: ...

    @abstract_method
    def is_quadratic_number_field(self) -> bool: ...

    @abstract_method
    def is_cyclotomic_field(self) -> bool: ...

    @abstract_method
    def ideal_monoid(self) -> Monoid: ...

    @final
    def __pow__(self, n: Integer) -> FreeModule:
        return Modules(self).Constructors().FreeModule(n)


# ---------------------------------------------------------------------------
# Ring element method surface — universal ring element abstract interface
# ---------------------------------------------------------------------------


class _RingElementMethods:
    r"""Abstract element methods present on all ring elements."""

    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def is_one(self) -> bool: ...

    @abstract_method
    def is_nilpotent(self) -> bool: ...

    @final
    def is_idempotent(self) -> bool:
        return self * self == self

    @abstract_method
    def additive_order(self) -> Cardinality: ...

    @abstract_method
    def multiplicative_order(self) -> Cardinality: ...

    @abstract_method
    def is_square(self) -> bool: ...

    @abstract_method
    def abs(self) -> RingElement: ...

    @abstract_method
    def nth_root(
        self,
        n: Integer,
        extend: bool = False,
        all: bool = False,
        algorithm: str | None = None,
        cunningham: bool = False,
        prec: Integer | None = None,
    ) -> RingElement | list[RingElement]: ...

    @abstract_method
    def sqrt(
        self,
        extend: bool = True,
        all: bool = False,
        name: str | None = None,
    ) -> RingElement | list[RingElement]: ...

    @abstract_method
    def powers(self, n: Integer) -> list[RingElement]: ...

    @final
    def principal_ideal(self) -> Ideal:
        return self.parent().principal_ideal(self)


# ---------------------------------------------------------------------------
# Ring morphism method surface — universal ring homomorphism abstract interface
# ---------------------------------------------------------------------------


class _RingMorphismMethods:
    r"""Abstract morphism methods present on all ring homomorphisms."""

    @abstract_method
    def image(self, I: Ideal | None = None) -> Ideal: ...

    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def kernel(self) -> Ideal: ...

    @abstract_method
    def section(self) -> RingMorphism: ...


# ---------------------------------------------------------------------------
# Ideal category — parent/element/morphism surfaces
# ---------------------------------------------------------------------------


class _RingIdealParentMethods:
    r"""Abstract parent methods for ring ideals."""

    @final
    def is_ideal(self) -> bool:
        return True

    @abstract_method
    def ring(self) -> Ring: ...

    @abstract_method
    def gen(self, i: Integer = 0) -> RingElement: ...

    @abstract_method
    def gens(self) -> tuple[RingElement, ...]: ...

    @abstract_method
    def ngens(self) -> Integer: ...

    @abstract_method
    def gens_reduced(self) -> tuple[RingElement, ...]: ...

    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def is_one(self) -> bool: ...

    @abstract_method
    def is_trivial(self) -> bool: ...

    @abstract_method
    def is_prime(self) -> bool: ...

    @abstract_method
    def is_maximal(self) -> bool: ...

    @abstract_method
    def is_primary(self) -> bool: ...

    @abstract_method
    def is_principal(self) -> bool: ...

    @abstract_method
    def is_idempotent(self) -> bool: ...

    @abstract_method
    def divides(self, other: RingElement) -> bool: ...

    @abstract_method
    def norm(self) -> RingElement: ...

    @abstract_method
    def radical(self) -> Ideal: ...

    @abstract_method
    def reduce(self, f: RingElement) -> RingElement: ...

    @abstract_method
    def random_element(
        self,
        degree: Integer | tuple[Integer, Integer] | None = None,
        compute_gb: bool = False,
        terms: Cardinality | None = None,
        choose_degree: bool = False,
        monic: bool = False,
        coefficient_lower_bound: Integer | None = None,
        coefficient_upper_bound: Integer | None = None,
        distribution: str | None = None,
    ) -> RingElement: ...


class _RingIdealElementMethods:
    r"""Abstract element methods for elements of ring ideals."""

    @abstract_method
    def is_unit(self) -> bool: ...

    @abstract_method
    def is_zero(self) -> bool: ...


class _RingIdealMorphismMethods:
    r"""Ring-ideal-specific morphism methods; generic morphism methods are inherited."""


class _RingIdeals(Category_ideal):
    r"""Ideals of a ring in the redesigned category surface.

    Canonical chain: ``Rings().Ideals(R)``.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "ring ideals"

    @override
    @final
    def super_categories(self) -> list[Category]:
        R = self.ring()
        return [CommutativeRingIdeals(R), Modules(R).RIdeals()]

    @classmethod
    @final
    def from_sage_ideal(cls, sage_ideal: Ideal) -> Ideal:
        R = sage_ideal.ring()
        return refine_category(sage_ideal.parent(), [cls(R), Modules(R).RIdeals()])

    ParentMethods = _RingIdealParentMethods
    ElementMethods = _RingIdealElementMethods
    MorphismMethods = _RingIdealMorphismMethods


# ---------------------------------------------------------------------------
# Rings — the root category
# ---------------------------------------------------------------------------


class Rings(Category_singleton):
    r"""Replacement ring category, staged below Sage's existing ``Rings``.

    Canonical chain: ``Rings()``.
    """

    class Constructors:
        r"""Constructor collector for Sage ring entry points.

        This helper owns constructor provenance: each method names a Sage
        entry point and refines the result into the tightest known ring
        subcategories.
        """

        @final
        def __repr__(self) -> str:
            return "Sage ring constructors"

        @final
        def ZZ(self) -> Ring:
            from sage.all import ZZ

            return refine_category(ZZ, [Rings(), _ZZ()])

        @final
        def QQ(self) -> Ring:
            from sage.all import QQ

            return refine_category(QQ, [Rings(), _QQ()])

        @final
        def QQbar(self) -> Ring:
            from sage.all import QQbar

            return refine_category(QQbar, [Rings(), _QQbar()])

        @final
        def AA(self) -> Ring:
            from sage.all import AA

            return refine_category(AA, [Rings(), _AA()])

        @final
        def RR(self) -> Ring:
            from sage.all import RR

            return refine_category(RR, [Rings(), _RR()])

        @final
        def CC(self) -> Ring:
            from sage.all import CC

            return refine_category(CC, [Rings(), _CC()])

        @final
        def RDF(self) -> Ring:
            from sage.all import RDF

            return refine_category(RDF, [Rings(), _RealDoubleFields()])

        @final
        def CDF(self) -> Ring:
            from sage.all import CDF

            return refine_category(CDF, [Rings(), _ComplexDoubleFields()])

        @final
        def RIF(self) -> Ring:
            from sage.all import RIF

            return refine_category(RIF, [Rings(), _RealIntervalFields()])

        @final
        def CIF(self) -> Ring:
            from sage.all import CIF

            return refine_category(CIF, [Rings(), _ComplexIntervalFields()])

        @final
        def RealField(self, prec: Integer = 53, sci_not: bool = False, rnd: str = "RNDN") -> Ring:
            from sage.all import RR, RealField

            R = RealField(prec=prec, sci_not=sci_not, rnd=rnd)
            categories = [_RealFields()]
            if R is RR:
                categories.append(_RR())
            return refine_category(R, [Rings(), *categories])

        @final
        def ComplexField(self, prec: Integer = 53, names: str | None = None) -> Ring:
            from sage.all import CC, ComplexField

            R = ComplexField(prec=prec, names=names)
            categories = [_ComplexFields()]
            if R is CC:
                categories.append(_CC())
            return refine_category(R, [Rings(), *categories])

        @final
        def RealBallField(self, prec: Integer = 53) -> Ring:
            from sage.all import RealBallField

            return refine_category(RealBallField(prec), [Rings(), _RealBallFields()])

        @final
        def ComplexBallField(self, prec: Integer = 53) -> Ring:
            from sage.all import ComplexBallField

            return refine_category(ComplexBallField(prec), [Rings(), _ComplexBallFields()])

        @final
        def IntegerModRing(
            self,
            order: Integer = 0,
            is_field: bool = False,
            category: Category | None = None,
        ) -> Ring:
            from sage.all import IntegerModRing

            return refine_category(IntegerModRing(order, is_field=is_field, category=category), [Rings(), _IntegerModRings()])

        @final
        def Zmod(
            self,
            order: Integer = 0,
            is_field: bool = False,
            category: Category | None = None,
        ) -> Ring:
            from sage.all import Zmod

            return refine_category(Zmod(order, is_field=is_field, category=category), [Rings(), _IntegerModRings()])

        @final
        def Integers(
            self,
            order: Integer = 0,
            is_field: bool = False,
            category: Category | None = None,
        ) -> Ring:
            from sage.all import Integers

            return refine_category(Integers(order, is_field=is_field, category=category), [Rings(), _IntegerModRings()])

        @final
        def GF(
            self,
            order: Integer,
            name: str | None = None,
            modulus: Polynomial | str | None = None,
            names: str | None = None,
            impl: str | None = None,
            proof: bool | None = None,
            check_prime: bool = True,
            check_irreducible: bool = True,
            prefix: str | None = None,
            repr: str | None = None,
            elem_cache: bool | None = None,
        ) -> Ring:
            from sage.all import GF

            return refine_category(
                GF(
                    order,
                    name=name,
                    modulus=modulus,
                    names=names,
                    impl=impl,
                    proof=proof,
                    check_prime=check_prime,
                    check_irreducible=check_irreducible,
                    prefix=prefix,
                    repr=repr,
                    elem_cache=elem_cache,
                ),
                [Rings(), _FiniteFields()],
            )

        @final
        def FiniteField(
            self,
            order: Integer,
            name: str | None = None,
            modulus: Polynomial | str | None = None,
            names: str | None = None,
            impl: str | None = None,
            proof: bool | None = None,
            check_prime: bool = True,
            check_irreducible: bool = True,
            prefix: str | None = None,
            repr: str | None = None,
            elem_cache: bool | None = None,
        ) -> Ring:
            from sage.all import FiniteField

            return refine_category(
                FiniteField(
                    order,
                    name=name,
                    modulus=modulus,
                    names=names,
                    impl=impl,
                    proof=proof,
                    check_prime=check_prime,
                    check_irreducible=check_irreducible,
                    prefix=prefix,
                    repr=repr,
                    elem_cache=elem_cache,
                ),
                [Rings(), _FiniteFields()],
            )

        @final
        def NumberField(
            self,
            polynomial: Polynomial,
            name: str | None = None,
            check: bool = True,
            names: str | None = None,
            embedding: RingElement | None = None,
            latex_name: str | None = None,
            assume_disc_small: bool = False,
            maximize_at_primes: Sequence[Integer] | None = None,
            structure: RingMorphism | None = None,
            *,
            latex_names: str | None = None,
        ) -> Ring:
            from sage.all import NumberField

            R = NumberField(
                polynomial,
                name=name,
                check=check,
                names=names,
                embedding=embedding,
                latex_name=latex_name,
                assume_disc_small=assume_disc_small,
                maximize_at_primes=maximize_at_primes,
                structure=structure,
                latex_names=latex_names,
            )
            categories = [_NumberFields()]
            if R.degree() == 2:
                categories.append(_QuadraticNumberFields())
            if isinstance(R, NumberField_cyclotomic):
                categories.append(_CyclotomicFields())
            return refine_category(R, [Rings(), *categories])

        @final
        def NumberFieldTower(
            self,
            polynomials: Sequence[Polynomial],
            names: str | Sequence[str],
            check: bool = True,
            embeddings: Sequence[RingElement] | None = None,
            latex_names: str | Sequence[str] | None = None,
            assume_disc_small: bool = False,
            maximize_at_primes: Sequence[Integer] | None = None,
            structures: Sequence[RingMorphism] | None = None,
        ) -> Ring:
            from sage.rings.number_field.number_field import NumberFieldTower

            R = NumberFieldTower(
                polynomials,
                names,
                check=check,
                embeddings=embeddings,
                latex_names=latex_names,
                assume_disc_small=assume_disc_small,
                maximize_at_primes=maximize_at_primes,
                structures=structures,
            )
            return refine_category(R, [Rings(), _NumberFields()])

        @final
        def QuadraticField(
            self,
            D: RingElement | Integer,
            name: str = "a",
            check: bool = True,
            embedding: bool | RingElement = True,
            latex_name: str = "sqrt",
        ) -> Ring:
            from sage.all import QuadraticField

            return refine_category(
                QuadraticField(D, name=name, check=check, embedding=embedding, latex_name=latex_name),
                [Rings(), _QuadraticNumberFields()],
            )

        @final
        def CyclotomicField(
            self,
            n: Integer = 0,
            names: str | None = None,
            embedding: bool | RingElement = True,
        ) -> Ring:
            from sage.all import CyclotomicField

            return refine_category(CyclotomicField(n, names=names, embedding=embedding), [Rings(), _CyclotomicFields()])

        @final
        def Zp(
            self,
            p: Integer,
            prec: Integer | None = None,
            type: str = "capped-rel",
            print_mode: str | None = None,
            names: str | None = None,
            ram_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_alphabet: str | None = None,
            print_max_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            label: str | None = None,
        ) -> Ring:
            from sage.all import Zp

            return refine_category(
                Zp(
                    p,
                    prec=prec,
                    type=type,
                    print_mode=print_mode,
                    names=names,
                    ram_name=ram_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_alphabet=print_alphabet,
                    print_max_terms=print_max_terms,
                    show_prec=show_prec,
                    check=check,
                    label=label,
                ),
                [Rings(), _Zp()],
            )

        @final
        def ZpWithPrecisionCaps(
            self,
            p: Integer,
            relative_cap: Integer,
            absolute_cap: Integer,
            type: str = "lattice-cap",
            print_mode: str | None = None,
            names: str | None = None,
            ram_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_alphabet: str | None = None,
            print_max_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            label: str | None = None,
        ) -> Ring:
            assert type.startswith("lattice-"), f"Precision caps require a lattice p-adic type: {type}"
            from sage.all import Zp

            return refine_category(
                Zp(
                    p,
                    prec=(relative_cap, absolute_cap),
                    type=type,
                    print_mode=print_mode,
                    names=names,
                    ram_name=ram_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_alphabet=print_alphabet,
                    print_max_terms=print_max_terms,
                    show_prec=show_prec,
                    check=check,
                    label=label,
                ),
                [Rings(), _Zp()],
            )

        @final
        def ZpRelaxed(
            self,
            p: Integer,
            default_prec: Integer,
            halting_prec: Integer,
            secure: bool = False,
            print_mode: str | None = None,
            names: str | None = None,
            ram_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_alphabet: str | None = None,
            print_max_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
        ) -> Ring:
            from sage.all import Zp

            return refine_category(
                Zp(
                    p,
                    prec=(default_prec, halting_prec, secure),
                    type="relaxed",
                    print_mode=print_mode,
                    names=names,
                    ram_name=ram_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_alphabet=print_alphabet,
                    print_max_terms=print_max_terms,
                    show_prec=show_prec,
                    check=check,
                ),
                [Rings(), _Zp()],
            )

        @final
        def Qp(
            self,
            p: Integer,
            prec: Integer | None = None,
            type: str = "capped-rel",
            print_mode: str | None = None,
            names: str | None = None,
            ram_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_alphabet: str | None = None,
            print_max_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            label: str | None = None,
        ) -> Ring:
            from sage.all import Qp

            return refine_category(
                Qp(
                    p,
                    prec=prec,
                    type=type,
                    print_mode=print_mode,
                    names=names,
                    ram_name=ram_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_alphabet=print_alphabet,
                    print_max_terms=print_max_terms,
                    show_prec=show_prec,
                    check=check,
                    label=label,
                ),
                [Rings(), _Qp()],
            )

        @final
        def QpWithPrecisionCaps(
            self,
            p: Integer,
            relative_cap: Integer,
            absolute_cap: Integer,
            type: str = "lattice-cap",
            print_mode: str | None = None,
            names: str | None = None,
            ram_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_alphabet: str | None = None,
            print_max_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            label: str | None = None,
        ) -> Ring:
            assert type.startswith("lattice-"), f"Precision caps require a lattice p-adic type: {type}"
            from sage.all import Qp

            return refine_category(
                Qp(
                    p,
                    prec=(relative_cap, absolute_cap),
                    type=type,
                    print_mode=print_mode,
                    names=names,
                    ram_name=ram_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_alphabet=print_alphabet,
                    print_max_terms=print_max_terms,
                    show_prec=show_prec,
                    check=check,
                    label=label,
                ),
                [Rings(), _Qp()],
            )

        @final
        def QpRelaxed(
            self,
            p: Integer,
            default_prec: Integer,
            halting_prec: Integer,
            secure: bool = False,
            print_mode: str | None = None,
            names: str | None = None,
            ram_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_alphabet: str | None = None,
            print_max_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
        ) -> Ring:
            from sage.all import Qp

            return refine_category(
                Qp(
                    p,
                    prec=(default_prec, halting_prec, secure),
                    type="relaxed",
                    print_mode=print_mode,
                    names=names,
                    ram_name=ram_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_alphabet=print_alphabet,
                    print_max_terms=print_max_terms,
                    show_prec=show_prec,
                    check=check,
                ),
                [Rings(), _Qp()],
            )

        @final
        def Zq(
            self,
            q: Integer,
            prec: Integer | None = None,
            type: str = "capped-rel",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            from sage.all import Zq

            return refine_category(
                Zq(
                    q,
                    prec=prec,
                    type=type,
                    modulus=modulus,
                    names=names,
                    print_mode=print_mode,
                    ram_name=ram_name,
                    res_name=res_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_max_ram_terms=print_max_ram_terms,
                    print_max_unram_terms=print_max_unram_terms,
                    print_max_terse_terms=print_max_terse_terms,
                    show_prec=show_prec,
                    check=check,
                    implementation=implementation,
                ),
                [Rings(), _Zp()],
            )

        @final
        def ZqFromPrimePower(
            self,
            p: Integer,
            degree: Integer,
            prec: Integer | None = None,
            type: str = "capped-rel",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            from sage.all import Zq

            return refine_category(
                Zq(
                    (p, degree),
                    prec=prec,
                    type=type,
                    modulus=modulus,
                    names=names,
                    print_mode=print_mode,
                    ram_name=ram_name,
                    res_name=res_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_max_ram_terms=print_max_ram_terms,
                    print_max_unram_terms=print_max_unram_terms,
                    print_max_terse_terms=print_max_terse_terms,
                    show_prec=show_prec,
                    check=check,
                    implementation=implementation,
                ),
                [Rings(), _Zp()],
            )

        @final
        def ZqFromPrimePowerFactorization(
            self,
            factorization: Sequence[tuple[Integer, Integer]],
            prec: Integer | None = None,
            type: str = "capped-rel",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            from sage.all import Zq

            return refine_category(
                Zq(
                    factorization,
                    prec=prec,
                    type=type,
                    modulus=modulus,
                    names=names,
                    print_mode=print_mode,
                    ram_name=ram_name,
                    res_name=res_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_max_ram_terms=print_max_ram_terms,
                    print_max_unram_terms=print_max_unram_terms,
                    print_max_terse_terms=print_max_terse_terms,
                    show_prec=show_prec,
                    check=check,
                    implementation=implementation,
                ),
                [Rings(), _Zp()],
            )

        @final
        def ZqWithPrecisionCaps(
            self,
            q: Integer,
            relative_cap: Integer,
            absolute_cap: Integer,
            type: str = "lattice-cap",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            r"""Return the unramified ``Z_p``-extension with residue field of order ``q`` and lattice precision caps.

            ``relative_cap`` bounds relative precision and ``absolute_cap`` bounds
            absolute lattice precision for the extension ring.
            """
            assert type.startswith("lattice-"), f"Precision caps require a lattice p-adic type: {type}"
            assert False, (
                "Installed Sage has no unramified Zq extension constructor for split "
                "lattice relative/absolute precision caps; keep this admitted name "
                "deferred until Sage exposes a lattice-precision extension route."
            )

        @final
        def Qq(
            self,
            q: Integer,
            prec: Integer | None = None,
            type: str = "capped-rel",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            from sage.all import Qq

            return refine_category(
                Qq(
                    q,
                    prec=prec,
                    type=type,
                    modulus=modulus,
                    names=names,
                    print_mode=print_mode,
                    ram_name=ram_name,
                    res_name=res_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_max_ram_terms=print_max_ram_terms,
                    print_max_unram_terms=print_max_unram_terms,
                    print_max_terse_terms=print_max_terse_terms,
                    show_prec=show_prec,
                    check=check,
                    implementation=implementation,
                ),
                [Rings(), _Qp()],
            )

        @final
        def QqFromPrimePower(
            self,
            p: Integer,
            degree: Integer,
            prec: Integer | None = None,
            type: str = "capped-rel",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            from sage.all import Qq

            return refine_category(
                Qq(
                    (p, degree),
                    prec=prec,
                    type=type,
                    modulus=modulus,
                    names=names,
                    print_mode=print_mode,
                    ram_name=ram_name,
                    res_name=res_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_max_ram_terms=print_max_ram_terms,
                    print_max_unram_terms=print_max_unram_terms,
                    print_max_terse_terms=print_max_terse_terms,
                    show_prec=show_prec,
                    check=check,
                    implementation=implementation,
                ),
                [Rings(), _Qp()],
            )

        @final
        def QqFromPrimePowerFactorization(
            self,
            factorization: Sequence[tuple[Integer, Integer]],
            prec: Integer | None = None,
            type: str = "capped-rel",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            from sage.all import Qq

            return refine_category(
                Qq(
                    factorization,
                    prec=prec,
                    type=type,
                    modulus=modulus,
                    names=names,
                    print_mode=print_mode,
                    ram_name=ram_name,
                    res_name=res_name,
                    print_pos=print_pos,
                    print_sep=print_sep,
                    print_max_ram_terms=print_max_ram_terms,
                    print_max_unram_terms=print_max_unram_terms,
                    print_max_terse_terms=print_max_terse_terms,
                    show_prec=show_prec,
                    check=check,
                    implementation=implementation,
                ),
                [Rings(), _Qp()],
            )

        @final
        def QqWithPrecisionCaps(
            self,
            q: Integer,
            relative_cap: Integer,
            absolute_cap: Integer,
            type: str = "lattice-cap",
            modulus: Polynomial | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            ram_name: str | None = None,
            res_name: str | None = None,
            print_pos: bool | None = None,
            print_sep: str | None = None,
            print_max_ram_terms: Integer | None = None,
            print_max_unram_terms: Integer | None = None,
            print_max_terse_terms: Integer | None = None,
            show_prec: bool | None = None,
            check: bool = True,
            implementation: str = "FLINT",
        ) -> Ring:
            r"""Return the unramified ``Q_p``-extension with residue field of order ``q`` and lattice precision caps.

            ``relative_cap`` bounds relative precision and ``absolute_cap`` bounds
            absolute lattice precision for the extension field.
            """
            assert type.startswith("lattice-"), f"Precision caps require a lattice p-adic type: {type}"
            assert False, (
                "Installed Sage has no unramified Qq extension constructor for split "
                "lattice relative/absolute precision caps; keep this admitted name "
                "deferred until Sage exposes a lattice-precision extension route."
            )

        @overload
        def PolynomialRing(
            self,
            base_ring: Ring,
            *,
            name: str,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> Ring: ...

        @overload
        def PolynomialRing(
            self,
            base_ring: Ring,
            *,
            n: Integer,
            name: str,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> Ring: ...

        @overload
        def PolynomialRing(
            self,
            base_ring: Ring,
            *,
            names: str | Sequence[str],
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> Ring: ...

        @overload
        def PolynomialRing(
            self,
            base_ring: Ring,
            *,
            n: Integer,
            names: str | Sequence[str],
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> Ring: ...

        @overload
        def PolynomialRing(
            self,
            base_ring: Ring,
            *,
            n: Integer,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> Ring: ...

        @overload
        def PolynomialRing(
            self,
            base_ring: Ring,
            *,
            n: Integer,
            var_array: str | Sequence[str],
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> Ring: ...

        @final
        def PolynomialRing(
            self,
            base_ring: Ring,
            *,
            n: Integer | None = None,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            var_array: str | Sequence[str] | None = None,
            sparse: bool | None = None,
            order: str | TermOrder = "degrevlex",
            implementation: str | None = None,
        ) -> Ring:
            from sage.all import PolynomialRing

            variable_spec_count = sum(spec is not None for spec in (name, names, var_array))
            assert variable_spec_count <= 1, "PolynomialRing expects at most one named variable specification"

            if name is not None:
                R = (
                    PolynomialRing(
                        base_ring,
                        name=name,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                    if n is None
                    else PolynomialRing(
                        base_ring,
                        n,
                        name=name,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                )
            elif names is not None:
                R = (
                    PolynomialRing(
                        base_ring,
                        names=names,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                    if n is None
                    else PolynomialRing(
                        base_ring,
                        n,
                        names=names,
                        sparse=sparse,
                        order=order,
                        implementation=implementation,
                    )
                )
            elif var_array is not None:
                assert n is not None, "PolynomialRing var_array construction expects n"
                R = PolynomialRing(
                    base_ring,
                    n,
                    var_array=var_array,
                    sparse=sparse,
                    order=order,
                    implementation=implementation,
                )
            else:
                assert n is not None, "PolynomialRing expects name, names, var_array, or n"
                R = PolynomialRing(
                    base_ring,
                    n,
                    sparse=sparse,
                    order=order,
                    implementation=implementation,
                )
            return refine_category(R, [Rings(), _PolynomialRings().RingsUnder(R.base_ring())])

        @final
        def PowerSeriesRing(
            self,
            base_ring: Ring,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> Ring:
            from sage.all import PowerSeriesRing

            R = PowerSeriesRing(
                base_ring,
                name=name,
                sparse=sparse,
                default_prec=default_prec,
                implementation=implementation,
            )
            return refine_category(R, [Rings(), _PowerSeriesRings().RingsUnder(R.base_ring())])

        @final
        def MultivariatePowerSeriesRing(
            self,
            base_ring: Ring,
            *,
            names: str | Sequence[str],
            num_gens: Integer | None = None,
            sparse: bool = False,
            default_prec: Integer | None = None,
            order: str = "negdeglex",
        ) -> Ring:
            from sage.all import PowerSeriesRing

            R = PowerSeriesRing(
                base_ring,
                names=names,
                sparse=sparse,
                default_prec=default_prec,
                order=order,
                num_gens=num_gens,
            )
            return refine_category(R, [Rings(), _PowerSeriesRings().RingsUnder(R.base_ring())])

        @final
        def MultivariatePowerSeriesRingWithGeneratorPrefix(
            self,
            base_ring: Ring,
            *,
            prefix: str,
            num_gens: Integer,
            sparse: bool = False,
            default_prec: Integer | None = None,
            order: str = "negdeglex",
        ) -> Ring:
            from sage.all import PowerSeriesRing

            R = PowerSeriesRing(
                base_ring,
                num_gens,
                prefix,
                sparse=sparse,
                default_prec=default_prec,
                order=order,
            )
            return refine_category(R, [Rings(), _PowerSeriesRings().RingsUnder(R.base_ring())])

        @final
        def LaurentSeriesRing(
            self,
            base_ring: Ring,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> Ring:
            from sage.all import LaurentSeriesRing

            R = LaurentSeriesRing(
                base_ring,
                name=name,
                sparse=sparse,
                default_prec=default_prec,
                implementation=implementation,
            )
            return refine_category(R, [Rings(), _LaurentSeriesRings().RingsUnder(R.base_ring())])

        @final
        def LaurentSeriesRingFromPowerSeriesRing(self, power_series_ring: Ring) -> Ring:
            from sage.all import LaurentSeriesRing

            R = LaurentSeriesRing(power_series_ring)
            return refine_category(R, [Rings(), _LaurentSeriesRings().RingsUnder(R.base_ring())])

        @final
        def PuiseuxSeriesRing(
            self,
            base_ring: Ring,
            name: str,
            *,
            sparse: bool = False,
            default_prec: Integer | None = None,
            implementation: str | None = None,
        ) -> Ring:
            from sage.all import PuiseuxSeriesRing

            R = PuiseuxSeriesRing(
                base_ring,
                name=name,
                sparse=sparse,
                default_prec=default_prec,
                implementation=implementation,
            )
            return refine_category(R, [Rings(), _PuiseuxSeriesRings().RingsUnder(R.base_ring())])

        @final
        def PuiseuxSeriesRingFromLaurentSeriesRing(self, laurent_series_ring: Ring) -> Ring:
            from sage.all import PuiseuxSeriesRing

            R = PuiseuxSeriesRing(laurent_series_ring)
            return refine_category(R, [Rings(), _PuiseuxSeriesRings().RingsUnder(R.base_ring())])

        @final
        def MatrixRing(
            self,
            base_ring: Ring,
            n: Integer,
            sparse: bool = False,
            implementation: str | type[Matrix] | None = None,
        ) -> Ring:
            R = MatrixSpace(base_ring, n, n, sparse=sparse, implementation=implementation)
            return refine_category(R, [Rings(), _MatrixAlgebras(R.base_ring(), R.nrows(), R.ncols())])

    _Constructors = Constructors

    @cached_method
    @final
    def Constructors(self):
        r"""Return the Sage ring constructor collector."""
        return self.__class__._Constructors()

    @override
    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageRings(),)

    @override
    @final
    def super_categories(self) -> list[Category]:
        from ..sets import Sets

        return [Sets(), SageRings()]

    @override
    @final
    def additional_structure(self) -> Category | None:
        return None

    class SubcategoryMethods:
        r"""Mixin providing ``SubcategoryMethods`` axiom and functorial selectors."""

        @cached_method
        @final
        def Commutative(self) -> Category:
            return self._with_axiom("Commutative")

        @cached_method
        @final
        def Division(self) -> Category:
            return self._with_axiom("Division")

        @cached_method
        @final
        def Finite(self) -> Category:
            return self._with_axiom("Finite")

        @cached_method
        @final
        def Topological(self) -> Category:
            return self._with_axiom("Topological")

        @cached_method
        @final
        def Approximate(self) -> Category:
            return ApproximateRingsCategory()

        @cached_method
        @final
        def WithValuation(self) -> Category:
            return self._with_axiom("WithValuation")

        @cached_method
        @final
        def Characteristic(self, p: Integer) -> Category:
            from .subcategories.constructions.characteristic import _CharacteristicRings

            return _CharacteristicRings(self, p)

        @cached_method
        @final
        def KrullDimension(self, n: Integer) -> Category:
            from .subcategories.constructions.krull_dimension import _KrullDimension

            return _KrullDimension(self, n)

        @cached_method
        @final
        def Polynomial(self) -> Category:
            return self._with_axiom("Polynomial")

        @cached_method
        @final
        def PowerSeries(self) -> Category:
            return self._with_axiom("PowerSeries")

        @cached_method
        @final
        def LaurentSeries(self) -> Category:
            return self._with_axiom("LaurentSeries")

        @cached_method
        @final
        def PuiseuxSeries(self) -> Category:
            return self._with_axiom("PuiseuxSeries")

        @cached_method
        @final
        def RingsUnder(self, structure_ring: Ring) -> Category:
            from .subcategories.constructions.rings_under import _RingsUnder

            return _RingsUnder.category_of(self, structure_ring)

        @cached_method
        @final
        def RingsOver(self, structure_ring: Ring) -> Category:
            from .subcategories.constructions.rings_over import _RingsOver

            return _RingsOver.category_of(self, structure_ring)

        @cached_method
        @final
        def AlgebrasOver(self, structure_ring: Ring) -> Category:
            from ..algebras import Algebras

            return Algebras(structure_ring)

        @cached_method
        @final
        def PolynomialRings(self) -> Category:
            return self.Polynomial()

        @cached_method
        @final
        def PolynomialRingsOver(self, structure_ring: Ring) -> Category:
            return self.Polynomial().RingsUnder(structure_ring)

        @cached_method
        @final
        def PolynomialOver(self, structure_ring: Ring) -> Category:
            return self.PolynomialRingsOver(structure_ring)

        @cached_method
        @final
        def PowerSeriesRings(self) -> Category:
            return self.PowerSeries()

        @cached_method
        @final
        def PowerSeriesRingsOver(self, structure_ring: Ring) -> Category:
            return self.PowerSeries().RingsUnder(structure_ring)

        @cached_method
        @final
        def PowerSeriesOver(self, structure_ring: Ring) -> Category:
            return self.PowerSeriesRingsOver(structure_ring)

        @cached_method
        @final
        def LaurentSeriesRings(self) -> Category:
            return self.LaurentSeries()

        @cached_method
        @final
        def LaurentSeriesRingsOver(self, structure_ring: Ring) -> Category:
            return self.LaurentSeries().RingsUnder(structure_ring)

        @cached_method
        @final
        def LaurentSeriesOver(self, structure_ring: Ring) -> Category:
            return self.LaurentSeriesRingsOver(structure_ring)

        @cached_method
        @final
        def PuiseuxSeriesRings(self) -> Category:
            return self.PuiseuxSeries()

        @cached_method
        @final
        def PuiseuxSeriesRingsOver(self, structure_ring: Ring) -> Category:
            return self.PuiseuxSeries().RingsUnder(structure_ring)

        @cached_method
        @final
        def PuiseuxSeriesOver(self, structure_ring: Ring) -> Category:
            return self.PuiseuxSeriesRingsOver(structure_ring)

        @cached_method
        @final
        def QuotientRingsOf(self, structure_ring: Ring) -> Category:
            return self.Quotients().RingsUnder(structure_ring)

        @cached_method
        @final
        def QuotientsOf(self, structure_ring: Ring) -> Category:
            return self.QuotientRingsOf(structure_ring)

        @cached_method
        @final
        def SubringsOf(self, structure_ring: Ring) -> Category:
            return self.Subobjects().RingsOver(structure_ring)


    # ----- Axiomatic subcategories -----------------------------------------

    Commutative = _CommutativeRings
    Division = _DivisionRings
    Finite = _FiniteRings
    Topological = _TopologicalRings
    WithValuation = _ValuedRings
    Polynomial = _PolynomialRings
    PowerSeries = _PowerSeriesRings
    LaurentSeries = _LaurentSeriesRings
    PuiseuxSeries = _PuiseuxSeriesRings

    # ----- Functorial constructions ----------------------------------------

    Subobjects = _Subobjects
    Subquotients = _Subquotients
    Quotients = _Quotients
    RingsUnder = _RingsUnder
    RingsOver = _RingsOver
    ObjectsUnder = _RingsUnder
    ObjectsOver = _RingsOver
    CartesianProducts = _CartesianProducts
    MatrixAlgebras = _MatrixAlgebras

    HomCategory = RingHomCategory

    ParentMethods = _RingObjectMethods
    ElementMethods = _RingElementMethods
    MorphismMethods = _RingMorphismMethods


RingsCategory = Rings
RingsObject = Rings.ParentMethods
RingsElement = Rings.ElementMethods
RingsMorphism = Rings.MorphismMethods
RingsHomCategory = RingHomCategory
RingsEndCategory = RingEndCategory
RingsAutCategory = RingAutCategory
RingsHom = RingHomCategory.ParentMethods
RingsEnd = RingEndCategory.ParentMethods
RingsAut = RingAutCategory.ParentMethods
RingsEndomorphism = RingEndCategory.ElementMethods
RingsAutomorphism = RingAutCategory.ElementMethods
