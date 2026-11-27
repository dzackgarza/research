r"""QQ ring subcategory spec."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal, final, override

from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer
from sage.rings.laurent_series_ring import LaurentSeriesRing as SageLaurentSeriesRing
from sage.rings.lazy_series_ring import LazyLaurentSeriesRing, LazyPowerSeriesRing
from sage.rings.multi_power_series_ring import MPowerSeriesRing_generic
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.power_series_ring import PowerSeriesRing_generic
from sage.rings.puiseux_series_ring import PuiseuxSeriesRing as SagePuiseuxSeriesRing

from ...cat import Category, Category_singleton
from .. import Rings

if TYPE_CHECKING:
    from ...types import (
        AbelianGroup,
        Field,
        Group,
        Ideal,
        PrimeIdeal,
        Ring,
        RingElement,
        RingMorphism,
    )

_SAGE_POLYNOMIAL_RING_CLASSES = (PolynomialRing_generic, MPolynomialRing_base)
_SAGE_POWER_SERIES_RING_CLASSES = (
    PowerSeriesRing_generic,
    MPowerSeriesRing_generic,
    LazyPowerSeriesRing,
)
_SAGE_LAURENT_SERIES_RING_CLASSES = (
    SageLaurentSeriesRing,
    LazyLaurentSeriesRing,
)
_SAGE_PUISEUX_SERIES_RING_CLASSES = (SagePuiseuxSeriesRing,)
_SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES = _SAGE_LAURENT_SERIES_RING_CLASSES + _SAGE_POWER_SERIES_RING_CLASSES
_SAGE_PUISEUX_SERIES_CONTAINMENT_CLASSES = _SAGE_PUISEUX_SERIES_RING_CLASSES + _SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES

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

class _QQ(Category_singleton):
    r"""Sage's rational field.

    Constructor target: ``Rings().Constructors().QQ()`` refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "rational field"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            _Fields(),
            _QuotientFields(),
            _NumberFields(),
            _GlobalFields(),
            Rings().Characteristic(0),
        ]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import QQ

        return x is QQ

    @final
    def object(self):
        from sage.all import QQ

        return QQ

    class ParentMethods:
        @override
        @final
        def is_algebraically_closed(self) -> bool:
            return False

        @override
        @final
        def algebraic_closure(self) -> Field:
            from sage.all import QQbar

            return QQbar

        @cached_method
        @final
        def as_number_field(self) -> Field:
            from sage.all import ZZ, NumberField, PolynomialRing

            R = PolynomialRing(ZZ, "x")
            return NumberField(R.gen(), "a")

        @override
        @final
        def is_quadratic(self) -> bool:
            return self.as_number_field().is_quadratic()

        @override
        @final
        def is_cyclotomic(self) -> bool:
            return self.as_number_field().is_cyclotomic()

        @override
        @final
        def degree(self) -> Integer:
            return self.as_number_field().degree()

        @override
        @final
        def absolute_degree(self) -> Integer:
            return self.as_number_field().absolute_degree()

        @override
        @final
        def signature(self) -> tuple[Integer, Integer]:
            return self.as_number_field().signature()

        @override
        @final
        def discriminant(self) -> Integer:
            return self.as_number_field().discriminant()

        @override
        @final
        def trace_pairing_discriminant(self, elements: Sequence[RingElement]) -> RingElement:
            return self.as_number_field().discriminant(v=elements)

        @override
        @final
        def absolute_discriminant(self) -> Integer:
            return self.as_number_field().absolute_discriminant()

        @override
        @final
        def galois_group(
            self,
            type: str | None = None,
            algorithm: str = "pari",
            names: str | None = None,
            gc_numbering: bool | None = None,
        ) -> Group:
            return self.as_number_field().galois_group(
                type=type, algorithm=algorithm, names=names, gc_numbering=gc_numbering
            )

        @override
        @final
        def galois_closure(self, names: str | None = None, map: bool = False) -> Field | tuple[Field, RingMorphism]:
            return self.as_number_field().galois_closure(names=names, map=map)

        @override
        @final
        def automorphisms(self) -> list[RingMorphism]:
            return self.as_number_field().automorphisms()

        @override
        @final
        def class_number(self, proof: bool | None = None) -> Integer:
            return self.as_number_field().class_number(proof=proof)

        @override
        @final
        def class_group(self, proof: bool | None = None, names: str = "c") -> AbelianGroup:
            return self.as_number_field().class_group(proof=proof, names=names)

        @override
        @final
        def integral_basis(self) -> tuple[RingElement, ...]:
            return self.as_number_field().integral_basis()

        @override
        @final
        def integral_basis_at_prime(self, prime: Integer) -> tuple[RingElement, ...]:
            return self.as_number_field().integral_basis(v=prime)

        @override
        @final
        def integral_basis_at_primes(self, primes: Sequence[Integer]) -> tuple[RingElement, ...]:
            return self.as_number_field().integral_basis(v=primes)

        @override
        @final
        def power_basis(self) -> tuple[RingElement, ...]:
            return self.as_number_field().power_basis()

        @override
        @final
        def reduced_basis(self, prec: Integer | None = None) -> tuple[RingElement, ...]:
            return self.as_number_field().reduced_basis(prec=prec)

        @override
        @final
        def different(self) -> Ideal:
            return self.as_number_field().different()

        @override
        @final
        def places(
            self, all_complex: bool = False, prec: Integer | None = None
        ) -> tuple[RingMorphism, ...]:
            return self.as_number_field().places(all_complex=all_complex, prec=prec)

        @override
        @final
        def real_embeddings(self, prec: Integer = 53) -> tuple[RingMorphism, ...]:
            return self.as_number_field().real_embeddings(prec=prec)

        @override
        @final
        def complex_embeddings(self, prec: Integer = 53) -> tuple[RingMorphism, ...]:
            return self.as_number_field().complex_embeddings(prec=prec)

        @override
        @final
        def roots_of_unity(self) -> list[RingElement]:
            return self.as_number_field().roots_of_unity()

        @override
        @final
        def regulator(self, proof: bool | None = None) -> RingElement:
            return self.as_number_field().regulator(proof=proof)

        @override
        @final
        def units(self, proof: bool | None = None) -> list[RingElement]:
            return self.as_number_field().units(proof=proof)

        @override
        @final
        def unit_group(self, proof: bool | None = None) -> AbelianGroup:
            return self.as_number_field().unit_group(proof=proof)

        @override
        @final
        def conductor(self, check_abelian: bool = True) -> Integer:
            return self.as_number_field().conductor(check_abelian=check_abelian)

        @override
        @final
        def prime_above(self, x: RingElement, degree: Integer | None = None) -> PrimeIdeal:
            return self.as_number_field().prime_above(x, degree=degree)

        @override
        @final
        def primes_above(self, x: RingElement, degree: Integer | None = None) -> list[PrimeIdeal]:
            return self.as_number_field().primes_above(x, degree=degree)

        @override
        @final
        def S_units(self, S: Sequence[PrimeIdeal], proof: bool = True) -> list[RingElement]:
            return self.as_number_field().S_units(S, proof=proof)

        @override
        @final
        def S_class_group(
            self, S: Sequence[PrimeIdeal], proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup:
            return self.as_number_field().S_class_group(S, proof=proof, names=names)

        @override
        @final
        def ring_of_integers(
            self,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().maximal_order(assume_maximal=assume_maximal)

        @override
        @final
        def ring_of_integers_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().maximal_order(v=prime, assume_maximal=assume_maximal)

        @override
        @final
        def ring_of_integers_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().maximal_order(v=primes, assume_maximal=assume_maximal)

        @override
        @final
        def maximal_order(
            self,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().maximal_order(assume_maximal=assume_maximal)

        @override
        @final
        def maximal_order_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().maximal_order(v=prime, assume_maximal=assume_maximal)

        @override
        @final
        def maximal_order_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().maximal_order(v=primes, assume_maximal=assume_maximal)

        @override
        @final
        def absolute_field(self, names: str) -> Field:
            return self.as_number_field().absolute_field(names)

    class ElementMethods: ...
    class MorphismMethods: ...
