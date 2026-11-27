r"""CommutativeRings ring subcategory spec."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
from sage.misc.abstract_method import abstract_method
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

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        CompleteRing,
        Ideal,
        Integer,
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

class _CommutativeRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative()``."""
    _base_category_class_and_axiom = (Rings, "Commutative")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "commutative rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageCommutativeRings(), Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageCommutativeRings() or (R in self.base_category() and R.is_commutative_ring())

    IntegralDomains = LazyImport("category_specs.rings.subcategories.integral_domain", "_IntegralDomains")
    Field = LazyImport("category_specs.rings.subcategories.field", "_Fields")
    Noetherian = LazyImport("category_specs.rings.subcategories.noetherian", "_NoetherianRings")
    Local = LazyImport("category_specs.rings.subcategories.local", "_LocalRings")
    Reduced = LazyImport("category_specs.rings.subcategories.reduced", "_ReducedRings")

    class SubcategoryMethods:
        @cached_method
        @final
        def IntegralDomains(self) -> Category:
            return self._with_axiom("IntegralDomains")

        @cached_method
        @final
        def Field(self) -> Category:
            return self._with_axiom("Field")

        @cached_method
        @final
        def Noetherian(self) -> Category:
            return self._with_axiom("Noetherian")

        @cached_method
        @final
        def Local(self) -> Category:
            return self._with_axiom("Local")

        @cached_method
        @final
        def Reduced(self) -> Category:
            return self._with_axiom("Reduced")

    class ParentMethods:
        @override
        @final
        def is_commutative_ring(self) -> bool:
            return True

        @abstract_method
        def completion(self, I: Ideal) -> CompleteRing: ...

        @abstract_method
        # Computable via Macaulay2 (m2) backend.
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        # Computable via Macaulay2 (m2) backend.
        def ngens(self) -> Integer: ...

        @abstract_method
        # Computable via Macaulay2 (m2) backend.
        def characteristic(self) -> Integer: ...

        @abstract_method
        # Computable via Macaulay2 (m2) backend.
        def krull_dimension(self) -> Cardinality: ...

        @abstract_method
        # Computable via Macaulay2 (m2) backend.
        def hilbert_polynomial(self) -> RingElement: ...

        @abstract_method
        def extension(
            self,
            poly: RingElement,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            *,
            latex_name: str | None = None,
            latex_names: str | Sequence[str] | None = None,
            map: bool = False,
            embedding: RingMorphism | None = None,
            implementation: str | None = None,
            prec: Integer | None = None,
            print_mode: str | None = None,
        ) -> Ring: ...

    class ElementMethods: ...
    class MorphismMethods: ...
