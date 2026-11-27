r"""PAdicRings ring subcategory spec."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method
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

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Field,
        Polynomial,
        RealNumber,
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

class _PAdicRings(Category_singleton):
    r"""Common category for Sage p-adic rings and fields.

    Constructor target: p-adic constructors under ``Rings().Constructors()``
    refine through this valued approximate family.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "p-adic rings and fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [ApproximateRingsCategory(), _CompleteRings(), _ValuedRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        from sage.rings.padics.generic_nodes import pAdicFieldGeneric, pAdicRingGeneric

        return isinstance(R, (pAdicFieldGeneric, pAdicRingGeneric))

    class ParentMethods:
        @abstract_method
        def prime(self) -> Integer: ...

        @abstract_method
        def precision_cap(self) -> Integer: ...

        @abstract_method
        def teichmuller(self, x: RingElement | Integer, prec: Integer | None = None) -> RingElement: ...

        @abstract_method
        def teichmuller_system(self) -> list[RingElement]: ...

        @abstract_method
        def inertia_subring(self) -> CompleteRing: ...

        @abstract_method
        def residue_ring(self, n: Integer) -> Ring: ...

        @abstract_method
        def residue_system(self) -> list[RingElement]: ...

        @abstract_method
        def ground_ring(self) -> CompleteRing: ...

        @abstract_method
        def ground_ring_of_tower(self) -> CompleteRing: ...

        @abstract_method
        def ramification_index(self) -> Integer: ...

        @abstract_method
        def e(self) -> Integer: ...

        @abstract_method
        def inertia_degree(self) -> Integer: ...

        @abstract_method
        def f(self) -> Integer: ...

        @abstract_method
        def absolute_e(self) -> Integer: ...

        @abstract_method
        def absolute_f(self) -> Integer: ...

        @abstract_method
        def absolute_ramification_index(self) -> Integer: ...

        @abstract_method
        def absolute_inertia_degree(self) -> Integer: ...

        @abstract_method
        def relative_degree(self) -> Integer: ...

        @abstract_method
        def relative_e(self) -> Integer: ...

        @abstract_method
        def relative_f(self) -> Integer: ...

        @abstract_method
        def relative_ramification_index(self) -> Integer: ...

        @abstract_method
        def relative_inertia_degree(self) -> Integer: ...

        @abstract_method
        def print_mode(self) -> str: ...

        @abstract_method
        def change_precision(self, precision: Integer, precision_type: str | None = None) -> CompleteRing: ...

        @abstract_method
        def change_prime(self, p: Integer) -> CompleteRing: ...

        @abstract_method
        def fraction_field(self) -> Field: ...

        @abstract_method
        def _change_print_mode(self, print_mode: str) -> CompleteRing: ...

        @abstract_method
        def ext(
            self,
            modulus: Polynomial,
            prec: Integer | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            implementation: str = "FLINT",
        ) -> CompleteRing: ...

        @abstract_method
        def frobenius_endomorphism(self, n: Integer = 1) -> RingMorphism: ...

        @abstract_method
        def maximal_unramified_subextension(self) -> CompleteRing: ...

        @abstract_method
        def defining_polynomial(self, var: str | None = None, exact: bool = False) -> RingElement: ...

        @abstract_method
        def integer_ring(self) -> CompleteRing: ...

        @abstract_method
        def exact_ring(self) -> Ring: ...

        @abstract_method
        def metric(self) -> Callable[[RingElement, RingElement], RealNumber]: ...

        @abstract_method
        def metric_function(self) -> Callable[[RingElement, RingElement], RealNumber]: ...

        @abstract_method
        def dist(self, x: RingElement, y: RingElement) -> RealNumber: ...

        @abstract_method
        def is_capped_absolute(self) -> bool: ...

        @abstract_method
        def is_capped_relative(self) -> bool: ...

        @abstract_method
        def is_fixed_mod(self) -> bool: ...

        @abstract_method
        def is_floating_point(self) -> bool: ...

        @abstract_method
        def is_relaxed(self) -> bool: ...

        @abstract_method
        def is_lattice_prec(self) -> bool: ...

        @abstract_method
        def has_pth_root(self) -> bool: ...

        @abstract_method
        def has_root_of_unity(self, n: Integer) -> bool: ...

    class ElementMethods: ...
    class MorphismMethods: ...
