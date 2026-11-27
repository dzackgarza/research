"""Private named ring category implementations."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Literal, assert_never, override

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
from sage.categories.complete_discrete_valuation import (
    CompleteDiscreteValuationFields as SageCompleteDiscreteValuationFields,
)
from sage.categories.complete_discrete_valuation import (
    CompleteDiscreteValuationRings as SageCompleteDiscreteValuationRings,
)
from sage.categories.dedekind_domains import DedekindDomains as SageDedekindDomains
from sage.categories.discrete_valuation import (
    DiscreteValuationFields as SageDiscreteValuationFields,
)
from sage.categories.discrete_valuation import (
    DiscreteValuationRings as SageDiscreteValuationRings,
)
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.euclidean_domains import EuclideanDomains as SageEuclideanDomains
from sage.categories.fields import Fields as SageFields
from sage.categories.finite_fields import FiniteFields as SageFiniteFields
from sage.categories.gcd_domains import GcdDomains as SageGcdDomains
from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.categories.noetherian_rings import NoetherianRings as SageNoetherianRings
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.categories.principal_ideal_domains import (
    PrincipalIdealDomains as SagePrincipalIdealDomains,
)
from sage.categories.quotient_fields import QuotientFields as SageQuotientFields
from sage.categories.rings import Rings as SageRings
from sage.categories.unique_factorization_domains import (
    UniqueFactorizationDomains as SageUniqueFactorizationDomains,
)
from sage.matrix.matrix_space import MatrixSpace
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.abc import ComplexBallField as SageComplexBallField
from sage.rings.abc import ComplexDoubleField as SageComplexDoubleField
from sage.rings.abc import ComplexField as SageComplexField
from sage.rings.abc import ComplexIntervalField as SageComplexIntervalField
from sage.rings.abc import RealBallField as SageRealBallField
from sage.rings.abc import RealDoubleField as SageRealDoubleField
from sage.rings.abc import RealField as SageRealField
from sage.rings.abc import RealIntervalField as SageRealIntervalField
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.integer import Integer
from sage.rings.laurent_series_ring import LaurentSeriesRing as SageLaurentSeriesRing
from sage.rings.lazy_series_ring import LazyLaurentSeriesRing, LazyPowerSeriesRing
from sage.rings.multi_power_series_ring import MPowerSeriesRing_generic
from sage.rings.number_field.number_field import (
    NumberField_cyclotomic,
    NumberField_quadratic,
)
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.power_series_ring import PowerSeriesRing_generic
from sage.rings.puiseux_series_ring import PuiseuxSeriesRing as SagePuiseuxSeriesRing
from sage.structure.factorization import Factorization

from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import (
        AbelianGroup,
        Cardinality,
        CompleteRing,
        ComplexInterval,
        Field,
        Group,
        Ideal,
        LocalRing,
        MaximalIdeal,
        Polynomial,
        PrimeIdeal,
        RealInterval,
        Ring,
        RingElement,
        RingMorphism,
        Valuation,
    )


def Rings(*args, **kwds):
    from . import Rings as _Rings

    return _Rings(*args, **kwds)


def _refine_named_ring(R: Ring, *categories: Category):
    return refine_category(R, [Rings(), *categories])


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


class _CommutativeRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py (references Rings class)

    def _repr_object_names(self) -> str:
        return "commutative rings"

    def super_categories(self) -> list[Category]:
        return [SageCommutativeRings(), Rings()]

    def __contains__(self, R: object) -> bool:
        return R in SageCommutativeRings() or (R in self.base_category() and R.is_commutative_ring())

    IntegralDomains = LazyImport(__name__, "_IntegralDomains")
    Field = LazyImport(__name__, "_Fields")
    Noetherian = LazyImport(__name__, "_NoetherianRings")
    Local = LazyImport(__name__, "_LocalRings")
    Reduced = LazyImport(__name__, "_ReducedRings")

    class SubcategoryMethods:
        @cached_method
        def IntegralDomains(self):
            return self._with_axiom("IntegralDomains")

        @cached_method
        def Field(self):
            return self._with_axiom("Field")

        @cached_method
        def Noetherian(self):
            return self._with_axiom("Noetherian")

        @cached_method
        def Local(self):
            return self._with_axiom("Local")

        @cached_method
        def Reduced(self):
            return self._with_axiom("Reduced")

    class ParentMethods:
        def is_commutative_ring(self) -> bool:
            return True

        @abstract_method
        def completion(self, I: Ideal) -> CompleteRing: ...

        @abstract_method
        # Computable via Macaulay2 (m2) backend.
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        # Computable via Macaulay2 (m2) backend.
        def ngens(self) -> int: ...

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
            **kwds,
        ) -> Ring: ...


class _FiniteRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "finite rings"

    def super_categories(self) -> list[Category]:
        return [SageRings().Finite(), Rings()]

    def __contains__(self, R: object) -> bool:
        return R in SageRings().Finite() or (R in self.base_category() and R.is_finite())

    class ParentMethods:
        def is_finite(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Integer: ...

        @abstract_method
        def order(self) -> Integer: ...


class _DivisionRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "division rings"

    def super_categories(self) -> list[Category]:
        return [SageDivisionRings(), Rings()]

    def __contains__(self, R: object) -> bool:
        return R in SageDivisionRings() or (R in self.base_category() and R.is_division_ring())

    class ParentMethods:
        def is_division_ring(self) -> bool:
            return True


class _TopologicalRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "topological rings"

    def super_categories(self) -> list[Category]:
        return [SageRings().Topological(), Rings()]

    def __contains__(self, R: object) -> bool:
        return R in SageRings().Topological() or (R in self.base_category() and R.is_topological_ring())

    Complete = LazyImport(__name__, "_CompleteRings")

    class SubcategoryMethods:
        @cached_method
        def Complete(self):
            return self._with_axiom("Complete")

    class ParentMethods:
        def is_topological_ring(self) -> bool:
            return True


class _Fields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_CommutativeRings, "Field")

    def _repr_object_names(self) -> str:
        return "fields"

    def super_categories(self) -> list[Category]:
        return [
            SageFields(),
            _CommutativeRings(),
            _DivisionRings(),
            _EuclideanDomains(),
            _IntegrallyClosedDomains(),
            _NoetherianRings(),
            _ReducedRings(),
            Rings().KrullDimension(0),
        ]

    def __contains__(self, R: object) -> bool:
        return R in SageFields() or (R in self.base_category() and R.is_field())

    Finite = LazyImport(__name__, "_FiniteFields")
    NumberFields = LazyImport(__name__, "_NumberFields")
    AlgebraicallyClosed = LazyImport(__name__, "_AlgebraicallyClosedFields")
    LocalFields = LazyImport(__name__, "_LocalFields")
    GlobalFields = LazyImport(__name__, "_GlobalFields")

    class SubcategoryMethods:
        @cached_method
        def NumberFields(self):
            return self._with_axiom("NumberFields")

        @cached_method
        def AlgebraicallyClosed(self):
            return self._with_axiom("AlgebraicallyClosed")

        @cached_method
        def LocalFields(self):
            return self._with_axiom("LocalFields")

        @cached_method
        def GlobalFields(self):
            return self._with_axiom("GlobalFields")

    @cached_method
    def QQ(self):
        return _QQ()

    @cached_method
    def RR(self):
        return _RR()

    @cached_method
    def CC(self):
        return _CC()

    class ParentMethods:
        @abstract_method
        def is_algebraically_closed(self) -> bool: ...

        @abstract_method
        def algebraic_closure(self) -> Field: ...

        @override
        def gcd(self, r: RingElement, s: RingElement) -> RingElement:
            match (r.is_zero() and s.is_zero()):
                case True:
                    return self.zero()
                case False:
                    assert not r.is_zero() or not s.is_zero()
                    return self.one()
                case unreachable:
                    assert_never(unreachable)

        @override
        def completion(self, I: Ideal) -> CompleteRing:
            # Field case split: only the zero and unit ideals exist.
            match I:
                case _ if I.is_zero():
                    return self
                case _ if I.is_one():
                    return self
                case unreachable:
                    assert_never(unreachable)

    class ElementMethods:
        @abstract_method
        def inverse(self): ...


class _IntegralDomains(CategoryWithAxiom):
    _base_category_class_and_axiom = (_CommutativeRings, "IntegralDomains")

    def _repr_object_names(self) -> str:
        return "integral domains"

    def super_categories(self) -> list[Category]:
        return [SageIntegralDomains(), _CommutativeRings()]

    def __contains__(self, R: object) -> bool:
        return R in SageIntegralDomains() or (R in self.base_category() and R.is_integral_domain())

    Gcd = LazyImport(__name__, "_GcdDomains")
    UniqueFactorization = LazyImport(__name__, "_UniqueFactorizationDomains")
    PrincipalIdeal = LazyImport(__name__, "_PrincipalIdealDomains")
    Euclidean = LazyImport(__name__, "_EuclideanDomains")
    IntegrallyClosed = LazyImport(__name__, "_IntegrallyClosedDomains")
    Dedekind = LazyImport(__name__, "_DedekindDomains")

    class SubcategoryMethods:
        @cached_method
        def Gcd(self):
            return self._with_axiom("Gcd")

        @cached_method
        def UniqueFactorization(self):
            return self._with_axiom("UniqueFactorization")

        @cached_method
        def PrincipalIdeal(self):
            return self._with_axiom("PrincipalIdeal")

        @cached_method
        def Euclidean(self):
            return self._with_axiom("Euclidean")

        @cached_method
        def IntegrallyClosed(self):
            return self._with_axiom("IntegrallyClosed")

        @cached_method
        def Dedekind(self):
            return self._with_axiom("Dedekind")

    class ParentMethods:
        @abstract_method
        def fraction_field(self) -> Field: ...

        @abstract_method
        def localization(
            self,
            additional_units: RingElement | Sequence[RingElement],
            names: str | Sequence[str] | None = None,
            normalize: bool = True,
            category: Category | None = None,
        ) -> LocalRing: ...

    class ElementMethods:
        @abstract_method
        def divides(self, other) -> bool: ...

    class MorphismMethods:
        @abstract_method
        def extend_to_fraction_field(self) -> RingMorphism: ...


class _NoetherianRings(CategoryWithAxiom):
    _base_category_class_and_axiom = (_CommutativeRings, "Noetherian")

    def _repr_object_names(self) -> str:
        return "noetherian rings"

    def super_categories(self) -> list[Category]:
        return [SageNoetherianRings(), _CommutativeRings()]

    def __contains__(self, R: object) -> bool:
        return R in SageNoetherianRings() or (R in self.base_category() and R.is_noetherian())


class _ReducedRings(CategoryWithAxiom):
    _base_category_class_and_axiom = (_CommutativeRings, "Reduced")

    def _repr_object_names(self) -> str:
        return "reduced rings"

    def super_categories(self) -> list[Category]:
        return [_CommutativeRings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_reduced()

    class ParentMethods:
        def is_reduced(self) -> bool:
            return True

        @abstract_method
        def integral_closure(self) -> Ring: ...


class _GcdDomains(CategoryWithAxiom):
    _base_category_class_and_axiom = (_IntegralDomains, "Gcd")

    def _repr_object_names(self) -> str:
        return "gcd domains"

    def super_categories(self) -> list[Category]:
        return [SageGcdDomains(), _IntegralDomains()]

    def __contains__(self, R: object) -> bool:
        return R in SageGcdDomains() or (R in self.base_category() and R.is_gcd_domain())

    class ParentMethods:
        def is_gcd_domain(self) -> bool:
            return True

        @abstract_method
        def gcd(self, r: RingElement, s: RingElement) -> RingElement: ...

    class ElementMethods:
        @abstract_method
        def gcd(self, other: RingElement) -> RingElement: ...

        @abstract_method
        def lcm(self, other: RingElement) -> RingElement: ...

        @abstract_method
        def xgcd(self, other: RingElement) -> tuple[RingElement, RingElement, RingElement]: ...


class _UniqueFactorizationDomains(CategoryWithAxiom):
    _base_category_class_and_axiom = (_IntegralDomains, "UniqueFactorization")

    def _repr_object_names(self) -> str:
        return "unique factorization domains"

    def super_categories(self) -> list[Category]:
        return [SageUniqueFactorizationDomains(), _GcdDomains()]

    def __contains__(self, R: object) -> bool:
        return R in SageUniqueFactorizationDomains() or (R in self.base_category() and R.is_unique_factorization_domain())

    class ElementMethods:
        @abstract_method
        def factor(self) -> Factorization: ...

        @abstract_method
        def is_irreducible(self) -> bool: ...

        @abstract_method
        def is_prime(self) -> bool: ...


class _PrincipalIdealDomains(CategoryWithAxiom):
    _base_category_class_and_axiom = (_IntegralDomains, "PrincipalIdeal")

    def _repr_object_names(self) -> str:
        return "principal ideal domains"

    def super_categories(self) -> list[Category]:
        return [SagePrincipalIdealDomains(), _UniqueFactorizationDomains()]

    def __contains__(self, R: object) -> bool:
        return R in SagePrincipalIdealDomains() or (R in self.base_category() and R.is_pid())

    class ParentMethods:
        def is_pid(self) -> bool:
            return True

        def ideal_generator(self, I: Ideal) -> RingElement:
            assert I.is_principal(), "PID ideal_generator expects a principal ideal"
            return I.gen()

        @override
        def gcd(self, r: RingElement, s: RingElement) -> RingElement:
            return self.ideal_generator(self.ideal(r, s))


class _EuclideanDomains(CategoryWithAxiom):
    _base_category_class_and_axiom = (_IntegralDomains, "Euclidean")

    def _repr_object_names(self) -> str:
        return "euclidean domains"

    def super_categories(self) -> list[Category]:
        return [SageEuclideanDomains(), _PrincipalIdealDomains()]

    def __contains__(self, R: object) -> bool:
        return R in SageEuclideanDomains() or (R in self.base_category() and R.is_euclidean_domain())


class _IntegrallyClosedDomains(CategoryWithAxiom):
    _base_category_class_and_axiom = (_IntegralDomains, "IntegrallyClosed")

    def _repr_object_names(self) -> str:
        return "integrally closed domains"

    def super_categories(self) -> list[Category]:
        return [_IntegralDomains()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_integrally_closed()

    class ParentMethods:
        def is_integrally_closed(self) -> bool:
            return True

        def integral_closure(self) -> Ring:
            return self


class _DedekindDomains(CategoryWithAxiom):
    _base_category_class_and_axiom = (_IntegralDomains, "Dedekind")

    def _repr_object_names(self) -> str:
        return "Dedekind domains"

    def super_categories(self) -> list[Category]:
        return [
            SageDedekindDomains(),
            _IntegralDomains(),
            _NoetherianRings(),
            _IntegrallyClosedDomains(),
            Rings().KrullDimension(1),
        ]

    def __contains__(self, R: object) -> bool:
        return R in SageDedekindDomains() or (R in self.base_category() and R.is_dedekind_domain())

    class ParentMethods:
        def is_dedekind_domain(self) -> bool:
            return True


class _ValuedRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "valued rings"

    def super_categories(self) -> list[Category]:
        return [Rings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_valued_ring()

    DiscretelyValued = LazyImport(__name__, "_DiscreteValuationRings")

    class SubcategoryMethods:
        @cached_method
        def DiscretelyValued(self):
            return self._with_axiom("DiscretelyValued")

    class ParentMethods:
        def is_valued_ring(self) -> bool:
            return True

        @abstract_method
        def valuation(self) -> Valuation: ...

        @abstract_method
        def roots_of_unity(self) -> list[RingElement]: ...


class _DiscreteValuationRings(CategoryWithAxiom):
    _base_category_class_and_axiom = (_ValuedRings, "DiscretelyValued")

    def _repr_object_names(self) -> str:
        return "discrete valuation rings"

    def super_categories(self) -> list[Category]:
        return [SageDiscreteValuationRings(), _EuclideanDomains(), _ValuedRings()]

    def __contains__(self, R: object) -> bool:
        return R in SageDiscreteValuationRings() or (R in self.base_category() and R.is_discrete_valuation_ring())

    class ParentMethods:
        def is_discrete_valuation_ring(self) -> bool:
            return True

        @abstract_method
        def uniformizer_pow(self, n: Integer) -> RingElement: ...

        @abstract_method
        def residue_characteristic(self) -> Integer: ...


class _DiscreteValuationFields(Category_singleton):
    def _repr_object_names(self) -> str:
        return "discrete valuation fields"

    def super_categories(self) -> list[Category]:
        return [SageDiscreteValuationFields(), _Fields(), _DiscreteValuationRings()]

    def __contains__(self, R: object) -> bool:
        return R in SageDiscreteValuationFields() or (R in _Fields() and R.is_discrete_valuation_field())

    class ParentMethods:
        def is_discrete_valuation_field(self) -> bool:
            return True


class _CompleteRings(CategoryWithAxiom):
    _base_category_class_and_axiom = (_TopologicalRings, "Complete")

    def _repr_object_names(self) -> str:
        return "complete rings"

    def super_categories(self) -> list[Category]:
        return [_TopologicalRings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_complete_ring()

    class ParentMethods:
        def is_complete_ring(self) -> bool:
            return True


class _LocalRings(CategoryWithAxiom):
    _base_category_class_and_axiom = (_CommutativeRings, "Local")

    def _repr_object_names(self) -> str:
        return "local rings"

    def super_categories(self) -> list[Category]:
        return [_CommutativeRings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_local_ring()

    class ParentMethods:
        def is_local_ring(self) -> bool:
            return True

        @abstract_method
        def maximal_ideal(self) -> MaximalIdeal: ...

        @abstract_method
        def residue_field(self) -> Field: ...


class _CompleteDiscreteValuationObjects(Category_singleton):
    r"""Common element surface for complete discrete valuation rings and fields."""

    def _repr_object_names(self) -> str:
        return "complete discrete valuation rings and fields"

    def super_categories(self) -> list[Category]:
        return [_CompleteRings(), _ValuedRings()]

    def __contains__(self, R: object) -> bool:
        return R in _CompleteDiscreteValuationRings() or (R in _CompleteDiscreteValuationFields())

    class ElementMethods:
        @abstract_method
        def valuation(self) -> Cardinality: ...

        @abstract_method
        def denominator(self) -> RingElement: ...

        @abstract_method
        def numerator(self) -> RingElement: ...

        @abstract_method
        def lift_to_precision(self, absprec: Integer | None = None) -> RingElement: ...


class _CompleteDiscreteValuationRings(Category_singleton):
    def _repr_object_names(self) -> str:
        return "complete discrete valuation rings"

    def super_categories(self) -> list[Category]:
        return [
            SageCompleteDiscreteValuationRings(),
            _CompleteDiscreteValuationObjects(),
            _CompleteRings(),
            _DiscreteValuationRings(),
        ]

    def __contains__(self, R: object) -> bool:
        return R in SageCompleteDiscreteValuationRings() or (
            R in _DiscreteValuationRings() and R.is_complete_discrete_valuation_ring()
        )

    class ParentMethods:
        def is_complete_discrete_valuation_ring(self) -> bool:
            return True


class _CompleteDiscreteValuationFields(Category_singleton):
    def _repr_object_names(self) -> str:
        return "complete discrete valuation fields"

    def super_categories(self) -> list[Category]:
        return [
            SageCompleteDiscreteValuationFields(),
            _CompleteDiscreteValuationObjects(),
            _CompleteRings(),
            _DiscreteValuationFields(),
        ]

    def __contains__(self, R: object) -> bool:
        return R in SageCompleteDiscreteValuationFields() or (
            R in _DiscreteValuationFields() and R.is_complete_discrete_valuation_field()
        )

    class ParentMethods:
        def is_complete_discrete_valuation_field(self) -> bool:
            return True


class _FiniteFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_Fields, "Finite")

    def _repr_object_names(self) -> str:
        return "finite fields"

    def super_categories(self) -> list[Category]:
        return [SageFiniteFields(), _Fields(), _FiniteRings()]

    def __contains__(self, R: object) -> bool:
        return R in SageFiniteFields() or (R in self.base_category() and R.is_finite_field())

    class ParentMethods:
        def is_finite_field(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Integer: ...

        @abstract_method
        def order(self) -> Integer: ...

        @abstract_method
        def multiplicative_generator(self) -> RingElement: ...

        @abstract_method
        def primitive_element(self) -> RingElement: ...

        @abstract_method
        def modulus(self) -> RingElement: ...

        @abstract_method
        def factored_order(self) -> Factorization: ...

        @abstract_method
        def galois_group(self) -> Group: ...

        @abstract_method
        def dual_basis(
            self,
            basis: Sequence[RingElement] | None = None,
            check: bool = True,
        ) -> tuple[RingElement, ...]: ...


class _NumberFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_Fields, "NumberFields")

    def _repr_object_names(self) -> str:
        return "number fields"

    def super_categories(self) -> list[Category]:
        return [SageNumberFields(), _Fields()]

    def __contains__(self, R: object) -> bool:
        return R in SageNumberFields() or (R in self.base_category() and R.is_number_field())

    Quadratic = LazyImport(__name__, "_QuadraticNumberFields")
    Cyclotomic = LazyImport(__name__, "_CyclotomicFields")

    class SubcategoryMethods:
        @cached_method
        def Quadratic(self):
            return self._with_axiom("Quadratic")

        @cached_method
        def Cyclotomic(self):
            return self._with_axiom("Cyclotomic")

    class ParentMethods:
        def is_number_field(self) -> bool:
            return True

        @abstract_method
        def is_quadratic(self) -> bool: ...

        @abstract_method
        def is_cyclotomic(self) -> bool: ...

        @abstract_method
        def degree(self) -> Integer: ...

        @abstract_method
        def absolute_degree(self) -> Integer: ...

        @abstract_method
        def signature(self) -> tuple[Integer, Integer]: ...

        @abstract_method
        def discriminant(self, v: Sequence[RingElement] | None = None) -> Integer | RingElement: ...

        @abstract_method
        def absolute_discriminant(self) -> Integer: ...

        @abstract_method
        def galois_group(
            self,
            type: str | None = None,
            algorithm: str = "pari",
            names: str | None = None,
            gc_numbering: bool | None = None,
        ) -> Group: ...

        @abstract_method
        def galois_closure(self, names: str | None = None, map: bool = False) -> Field | tuple[Field, RingMorphism]: ...

        @abstract_method
        def automorphisms(self) -> list[RingMorphism]: ...

        @abstract_method
        def class_number(self, proof: bool | None = None) -> Integer: ...

        @abstract_method
        def class_group(self, proof: bool | None = None, names: str = "c") -> AbelianGroup: ...

        @abstract_method
        def integral_basis(self, v: RingElement | Sequence[RingElement] | None = None) -> tuple[RingElement, ...]: ...

        @abstract_method
        def power_basis(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def reduced_basis(self, prec: Integer | int | None = None) -> tuple[RingElement, ...]: ...

        @abstract_method
        def different(self) -> Ideal: ...

        @abstract_method
        def places(
            self, all_complex: bool = False, prec: Integer | int | None = None
        ) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def real_embeddings(self, prec: Integer | int = 53) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def complex_embeddings(self, prec: Integer | int = 53) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def roots_of_unity(self) -> list[RingElement]: ...

        @abstract_method
        def regulator(self, proof: bool | None = None) -> RingElement: ...

        @abstract_method
        def units(self, proof: bool | None = None) -> list[RingElement]: ...

        @abstract_method
        def unit_group(self, proof: bool | None = None) -> AbelianGroup: ...

        @abstract_method
        def conductor(self, check_abelian: bool = True) -> Integer: ...

        @abstract_method
        def prime_above(self, x: RingElement, degree: Integer | int | None = None) -> PrimeIdeal: ...

        @abstract_method
        def primes_above(self, x: RingElement, degree: Integer | int | None = None) -> list[PrimeIdeal]: ...

        @abstract_method
        def S_units(self, S: Sequence[PrimeIdeal], proof: bool = True) -> list[RingElement]: ...

        @abstract_method
        def S_class_group(
            self, S: Sequence[PrimeIdeal], proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup: ...

        @abstract_method
        def ring_of_integers(
            self,
            v: Integer | Sequence[Integer] | None = None,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstract_method
        def maximal_order(
            self,
            v: Integer | Sequence[Integer] | None = None,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstract_method
        def absolute_field(self, names: str) -> Field: ...

    class ElementMethods:
        @abstract_method
        def norm(self, K: Field | None = None) -> RingElement: ...

        @abstract_method
        def trace(self, K: Field | None = None) -> RingElement: ...

        @abstract_method
        def minpoly(self, var: str = "x", algorithm: str | None = None) -> RingElement: ...

        @abstract_method
        def charpoly(self, var: str = "x", algorithm: str | None = None) -> RingElement: ...


class _AlgebraicallyClosedFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_Fields, "AlgebraicallyClosed")

    def _repr_object_names(self) -> str:
        return "algebraically closed fields"

    def super_categories(self) -> list[Category]:
        return [_Fields()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_algebraically_closed()

    class ParentMethods:
        def is_algebraically_closed(self) -> bool:
            return True

        def algebraic_closure(self) -> Field:
            return self


class _LocalFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_Fields, "LocalFields")

    def _repr_object_names(self) -> str:
        return "local fields"

    def super_categories(self) -> list[Category]:
        return [_Fields(), _TopologicalRings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_local_field()

    class ParentMethods:
        def is_local_field(self) -> bool:
            return True


class _GlobalFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_Fields, "GlobalFields")

    def _repr_object_names(self) -> str:
        return "global fields"

    def super_categories(self) -> list[Category]:
        return [_Fields()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_global_field()

    Archimedean = LazyImport(__name__, "_ArchimedeanGlobalFields")
    NonArchimedean = LazyImport(__name__, "_NonArchimedeanGlobalFields")

    class SubcategoryMethods:
        @cached_method
        def Archimedean(self):
            return self._with_axiom("Archimedean")

        @cached_method
        def NonArchimedean(self):
            return self._with_axiom("NonArchimedean")

    class ParentMethods:
        def is_global_field(self) -> bool:
            return True


class _ArchimedeanGlobalFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_GlobalFields, "Archimedean")

    def _repr_object_names(self) -> str:
        return "archimedean global fields"

    def super_categories(self) -> list[Category]:
        return [_GlobalFields()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_archimedean_global_field()

    class ParentMethods:
        def is_archimedean_global_field(self) -> bool:
            return True


class _NonArchimedeanGlobalFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_GlobalFields, "NonArchimedean")

    def _repr_object_names(self) -> str:
        return "nonarchimedean global fields"

    def super_categories(self) -> list[Category]:
        return [_GlobalFields()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and R.is_nonarchimedean_global_field()

    class ParentMethods:
        def is_nonarchimedean_global_field(self) -> bool:
            return True


class _QuadraticNumberFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_NumberFields, "Quadratic")

    def _repr_object_names(self) -> str:
        return "quadratic number fields"

    def super_categories(self) -> list[Category]:
        return [_NumberFields()]

    def __contains__(self, R: object) -> bool:
        if isinstance(R, NumberField_quadratic):
            return True
        if R in SageNumberFields():
            return R.degree() == 2
        return R in self.base_category() and R.is_quadratic_number_field()

    class ParentMethods:
        def is_quadratic(self) -> bool:
            return True

        def is_quadratic_number_field(self) -> bool:
            return True


class _CyclotomicFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_NumberFields, "Cyclotomic")

    def _repr_object_names(self) -> str:
        return "cyclotomic fields"

    def super_categories(self) -> list[Category]:
        return [_NumberFields()]

    def __contains__(self, R: object) -> bool:
        if isinstance(R, NumberField_cyclotomic):
            return True
        if R in SageNumberFields():
            return False
        return R in self.base_category() and R.is_cyclotomic_field()

    class ParentMethods:
        def is_cyclotomic(self) -> bool:
            return True

        def is_cyclotomic_field(self) -> bool:
            return True


class _QuotientFields(Category_singleton):
    def _repr_object_names(self) -> str:
        return "quotient fields"

    def super_categories(self) -> list[Category]:
        return [SageQuotientFields(), _Fields()]

    def __contains__(self, R: object) -> bool:
        return R in SageQuotientFields() or (R in _Fields() and R.is_quotient_field())

    class ParentMethods:
        def is_quotient_field(self) -> bool:
            return True


class _PAdicRings(Category_singleton):
    r"""Common category for Sage p-adic rings and fields."""

    def _repr_object_names(self) -> str:
        return "p-adic rings and fields"

    def super_categories(self) -> list[Category]:
        return [_CompleteRings(), _ValuedRings()]

    def __contains__(self, R: object) -> bool:
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
        def change(self, **kwds) -> CompleteRing: ...

        @abstract_method
        def ext(self, *args, **kwds) -> CompleteRing: ...

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
        def metric(self): ...

        @abstract_method
        def metric_function(self): ...

        @abstract_method
        def dist(self, x, y): ...

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


class _AlgebraicFields(Category_singleton):
    r"""Common category for Sage's ``AA`` and ``QQbar`` parents."""

    def _repr_object_names(self) -> str:
        return "algebraic real and complex fields"

    def super_categories(self) -> list[Category]:
        return [_Fields(), Rings().Characteristic(0)]

    def __contains__(self, x: object) -> bool:
        from sage.all import AA, QQbar

        return x is AA or x is QQbar

    class ParentMethods:
        @abstract_method
        def default_interval_prec(self) -> Integer: ...

        @abstract_method
        def common_polynomial(self, poly: Polynomial): ...

        @abstract_method
        def polynomial_root(
            self, poly: Polynomial, interval: RealInterval | ComplexInterval, multiplicity: Integer | int = 1
        ) -> RingElement: ...


class _NamedRings:
    r"""Constructor collector for Sage's named ring entry points."""

    def __repr__(self) -> str:
        return "named Sage ring constructors"

    def __contains__(self, R: object) -> bool:
        if isinstance(R, MatrixSpace):
            return R.nrows() == R.ncols()
        return any(
            R in category
            for category in (
                _ZZ(),
                _QQ(),
                _QQbar(),
                _AA(),
                _RR(),
                _CC(),
                _Zp(),
                _Qp(),
                _IntegerModRings(),
                _RealFields(),
                _ComplexFields(),
                _RealDoubleFields(),
                _ComplexDoubleFields(),
                _RealIntervalFields(),
                _ComplexIntervalFields(),
                _RealBallFields(),
                _ComplexBallFields(),
                _FiniteFields(),
                _NumberFields(),
                _QuadraticNumberFields(),
                _CyclotomicFields(),
                _PolynomialRings(),
                _PowerSeriesRings(),
                _LaurentSeriesRings(),
                _PuiseuxSeriesRings(),
            )
        )

    def ZZ(self):
        from sage.all import ZZ

        return _refine_named_ring(ZZ, _ZZ())

    def QQ(self):
        from sage.all import QQ

        return _refine_named_ring(QQ, _QQ())

    def QQbar(self):
        from sage.all import QQbar

        return _refine_named_ring(QQbar, _QQbar())

    def AA(self):
        from sage.all import AA

        return _refine_named_ring(AA, _AA())

    def RR(self):
        from sage.all import RR

        return _refine_named_ring(RR, _RR())

    def CC(self):
        from sage.all import CC

        return _refine_named_ring(CC, _CC())

    def RDF(self):
        from sage.all import RDF

        return _refine_named_ring(RDF, _RealDoubleFields())

    def CDF(self):
        from sage.all import CDF

        return _refine_named_ring(CDF, _ComplexDoubleFields())

    def RIF(self):
        from sage.all import RIF

        return _refine_named_ring(RIF, _RealIntervalFields())

    def CIF(self):
        from sage.all import CIF

        return _refine_named_ring(CIF, _ComplexIntervalFields())

    def RealField(self, *args, **kwds):
        from sage.all import RR, RealField

        R = RealField(*args, **kwds)
        categories = [_RealFields()]
        if R is RR:
            categories.append(_RR())
        return _refine_named_ring(R, *categories)

    def ComplexField(self, *args, **kwds):
        from sage.all import CC, ComplexField

        R = ComplexField(*args, **kwds)
        categories = [_ComplexFields()]
        if R is CC:
            categories.append(_CC())
        return _refine_named_ring(R, *categories)

    def RealBallField(self, *args, **kwds):
        from sage.all import RealBallField

        return _refine_named_ring(RealBallField(*args, **kwds), _RealBallFields())

    def ComplexBallField(self, *args, **kwds):
        from sage.all import ComplexBallField

        return _refine_named_ring(ComplexBallField(*args, **kwds), _ComplexBallFields())

    def IntegerModRing(self, *args, **kwds):
        from sage.all import IntegerModRing

        return _refine_named_ring(IntegerModRing(*args, **kwds), _IntegerModRings())

    def Zmod(self, *args, **kwds):
        from sage.all import Zmod

        return _refine_named_ring(Zmod(*args, **kwds), _IntegerModRings())

    def Integers(self, *args, **kwds):
        from sage.all import Integers

        return _refine_named_ring(Integers(*args, **kwds), _IntegerModRings())

    def GF(self, *args, **kwds):
        from sage.all import GF

        return _refine_named_ring(GF(*args, **kwds), _FiniteFields())

    def FiniteField(self, *args, **kwds):
        from sage.all import FiniteField

        return _refine_named_ring(FiniteField(*args, **kwds), _FiniteFields())

    def NumberField(self, *args, **kwds):
        from sage.all import NumberField

        R = NumberField(*args, **kwds)
        categories = [_NumberFields()]
        if R.degree() == 2:
            categories.append(_QuadraticNumberFields())
        if isinstance(R, NumberField_cyclotomic):
            categories.append(_CyclotomicFields())
        return _refine_named_ring(R, *categories)

    def QuadraticField(self, *args, **kwds):
        from sage.all import QuadraticField

        return _refine_named_ring(QuadraticField(*args, **kwds), _QuadraticNumberFields())

    def CyclotomicField(self, *args, **kwds):
        from sage.all import CyclotomicField

        return _refine_named_ring(CyclotomicField(*args, **kwds), _CyclotomicFields())

    def Zp(self, *args, **kwds):
        from sage.all import Zp

        return _refine_named_ring(Zp(*args, **kwds), _Zp())

    def Qp(self, *args, **kwds):
        from sage.all import Qp

        return _refine_named_ring(Qp(*args, **kwds), _Qp())

    def Zq(self, *args, **kwds):
        from sage.all import Zq

        return _refine_named_ring(Zq(*args, **kwds), _Zp())

    def Qq(self, *args, **kwds):
        from sage.all import Qq

        return _refine_named_ring(Qq(*args, **kwds), _Qp())

    def PolynomialRing(self, *args, **kwds):
        from sage.all import PolynomialRing

        R = PolynomialRing(*args, **kwds)
        return _refine_named_ring(
            R,
            _PolynomialRings().RingsUnder(R.base_ring()),
        )

    def PowerSeriesRing(self, *args, **kwds):
        from sage.all import PowerSeriesRing

        R = PowerSeriesRing(*args, **kwds)
        return _refine_named_ring(
            R,
            _PowerSeriesRings().RingsUnder(R.base_ring()),
        )

    def LaurentSeriesRing(self, *args, **kwds):
        from sage.all import LaurentSeriesRing

        R = LaurentSeriesRing(*args, **kwds)
        return _refine_named_ring(
            R,
            _LaurentSeriesRings().RingsUnder(R.base_ring()),
        )

    def PuiseuxSeriesRing(self, *args, **kwds):
        from sage.all import PuiseuxSeriesRing

        R = PuiseuxSeriesRing(*args, **kwds)
        return _refine_named_ring(
            R,
            _PuiseuxSeriesRings().RingsUnder(R.base_ring()),
        )

    def MatrixRing(self, base_ring, n, *args, **kwds):
        from .matrix_algebras import _MatrixAlgebras

        R = MatrixSpace(base_ring, n, n, *args, **kwds)
        return _refine_named_ring(
            R,
            _MatrixAlgebras(R.base_ring(), R.nrows(), R.ncols()),
        )


class _IntegerModRings(Category_singleton):
    r"""Category of Sage rings ``IntegerModRing(n)`` and aliases."""

    def _repr_object_names(self) -> str:
        return "integer residue class rings"

    def super_categories(self) -> list[Category]:
        return [_FiniteRings(), _CommutativeRings()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, IntegerModRing_generic)

    class ParentMethods:
        @abstract_method
        def modulus(self) -> RingElement: ...

        @abstract_method
        def factored_order(self) -> Factorization: ...

        @abstract_method
        def unit_gens(self, **kwds) -> tuple[RingElement, ...]: ...

        @abstract_method
        def multiplicative_generator(self) -> RingElement: ...


class _RealPrecisionFields(Category_singleton):
    r"""Common category for Sage real approximate fields with fixed precision."""

    def _repr_object_names(self) -> str:
        return "real precision fields"

    def super_categories(self) -> list[Category]:
        return [_Fields(), _CompleteRings(), _LocalFields(), Rings().Characteristic(0)]

    def __contains__(self, R: object) -> bool:
        return isinstance(
            R,
            (
                SageRealField,
                SageRealDoubleField,
                SageRealIntervalField,
                SageRealBallField,
            ),
        )

    class ParentMethods:
        @abstract_method
        def precision(self) -> Integer: ...

        @abstract_method
        def complex_field(self) -> Field: ...


class _ComplexPrecisionFields(Category_singleton):
    r"""Common category for Sage complex approximate fields with fixed precision."""

    def _repr_object_names(self) -> str:
        return "complex precision fields"

    def super_categories(self) -> list[Category]:
        return [_Fields(), _CompleteRings(), _LocalFields(), Rings().Characteristic(0)]

    def __contains__(self, R: object) -> bool:
        return isinstance(
            R,
            (
                SageComplexField,
                SageComplexDoubleField,
                SageComplexIntervalField,
                SageComplexBallField,
            ),
        )

    class ParentMethods:
        @abstract_method
        def precision(self) -> Integer: ...


class _ScientificNotationFields(Category_singleton):
    r"""Approximate fields whose display mode supports scientific notation."""

    def _repr_object_names(self) -> str:
        return "scientific-notation fields"

    def super_categories(self) -> list[Category]:
        return [_Fields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(
            R,
            (
                SageRealField,
                SageComplexField,
                SageRealIntervalField,
                SageComplexIntervalField,
            ),
        )

    class ParentMethods:
        @abstract_method
        def scientific_notation(self, status: bool | None = None) -> bool: ...


class _RealFields(Category_singleton):
    r"""Category of Sage real floating point fields ``RealField(prec)``."""

    def _repr_object_names(self) -> str:
        return "real fields"

    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields(), _ScientificNotationFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageRealField)


class _ComplexFields(Category_singleton):
    r"""Category of Sage complex floating point fields ``ComplexField(prec)``."""

    def _repr_object_names(self) -> str:
        return "complex fields"

    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields(), _ScientificNotationFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageComplexField)


class _RealDoubleFields(Category_singleton):
    r"""Category of Sage real double fields ``RDF``."""

    def _repr_object_names(self) -> str:
        return "real double fields"

    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageRealDoubleField)


class _ComplexDoubleFields(Category_singleton):
    r"""Category of Sage complex double fields ``CDF``."""

    def _repr_object_names(self) -> str:
        return "complex double fields"

    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageComplexDoubleField)


class _RealIntervalFields(Category_singleton):
    r"""Category of Sage real interval fields ``RealIntervalField(prec)``."""

    def _repr_object_names(self) -> str:
        return "real interval fields"

    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields(), _ScientificNotationFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageRealIntervalField)

    class ParentMethods:
        @abstract_method
        def middle_field(self) -> Field: ...


class _ComplexIntervalFields(Category_singleton):
    r"""Category of Sage complex interval fields ``ComplexIntervalField(prec)``."""

    def _repr_object_names(self) -> str:
        return "complex interval fields"

    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields(), _ScientificNotationFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageComplexIntervalField)

    class ParentMethods:
        @abstract_method
        def real_field(self) -> Field: ...

        @abstract_method
        def middle_field(self) -> Field: ...


class _RealBallFields(Category_singleton):
    r"""Category of Sage real ball fields ``RealBallField(prec)``."""

    def _repr_object_names(self) -> str:
        return "real ball fields"

    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageRealBallField)


class _ComplexBallFields(Category_singleton):
    r"""Category of Sage complex ball fields ``ComplexBallField(prec)``."""

    def _repr_object_names(self) -> str:
        return "complex ball fields"

    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields()]

    def __contains__(self, R: object) -> bool:
        return isinstance(R, SageComplexBallField)


class _QQbar(Category_singleton):
    def _repr_object_names(self) -> str:
        return "algebraic field"

    def super_categories(self) -> list[Category]:
        return [_AlgebraicFields()]

    def __contains__(self, x: object) -> bool:
        from sage.all import QQbar

        return x is QQbar

    def object(self):
        from sage.all import QQbar

        return QQbar

    class ParentMethods:
        @override
        def polynomial_root(
            self, poly: Polynomial, interval: RealInterval | ComplexInterval, multiplicity: Integer | int = 1
        ) -> RingElement: ...

    class ElementMethods:
        @override
        def nth_root(self, n: Integer, all: bool = False) -> RingElement | list[RingElement]: ...


class _AA(Category_singleton):
    def _repr_object_names(self) -> str:
        return "algebraic real field"

    def super_categories(self) -> list[Category]:
        return [_AlgebraicFields()]

    def __contains__(self, x: object) -> bool:
        from sage.all import AA

        return x is AA

    def object(self):
        from sage.all import AA

        return AA

    class ParentMethods:
        @override
        def polynomial_root(
            self, poly: Polynomial, interval: RealInterval, multiplicity: Integer | int = 1
        ) -> RingElement: ...

    class ElementMethods:
        @override
        def nth_root(self, n: Integer, all: bool = False) -> RingElement | list[RingElement]: ...


class _ZZ(Category_singleton):
    def _repr_object_names(self) -> str:
        return "integer ring"

    def super_categories(self) -> list[Category]:
        return [
            _EuclideanDomains(),
            _DedekindDomains(),
            Rings().Characteristic(0),
        ]

    def __contains__(self, x: object) -> bool:
        from sage.all import ZZ

        return x is ZZ

    def object(self):
        from sage.all import ZZ

        return ZZ


class _QQ(Category_singleton):
    def _repr_object_names(self) -> str:
        return "rational field"

    def super_categories(self) -> list[Category]:
        return [
            _Fields(),
            _QuotientFields(),
            _NumberFields(),
            _GlobalFields(),
            Rings().Characteristic(0),
        ]

    def __contains__(self, x: object) -> bool:
        from sage.all import QQ

        return x is QQ

    def object(self):
        from sage.all import QQ

        return QQ

    class ParentMethods:
        @override
        def is_algebraically_closed(self) -> bool:
            return False

        @override
        def algebraic_closure(self) -> Field:
            from sage.all import QQbar

            return QQbar

        @cached_method
        def as_number_field(self) -> Field:
            from sage.all import ZZ, NumberField, PolynomialRing

            R = PolynomialRing(ZZ, "x")
            return NumberField(R.gen(), "a")

        @override
        def is_quadratic(self) -> bool:
            return self.as_number_field().is_quadratic()

        @override
        def is_cyclotomic(self) -> bool:
            return self.as_number_field().is_cyclotomic()

        @override
        def degree(self) -> Integer:
            return self.as_number_field().degree()

        @override
        def absolute_degree(self) -> Integer:
            return self.as_number_field().absolute_degree()

        @override
        def signature(self) -> tuple[Integer, Integer]:
            return self.as_number_field().signature()

        @override
        def discriminant(self, v: Sequence[RingElement] | None = None) -> Integer | RingElement:
            return self.as_number_field().discriminant(v=v)

        @override
        def absolute_discriminant(self) -> Integer:
            return self.as_number_field().absolute_discriminant()

        @override
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
        def galois_closure(self, names: str | None = None, map: bool = False) -> Field | tuple[Field, RingMorphism]:
            return self.as_number_field().galois_closure(names=names, map=map)

        @override
        def automorphisms(self) -> list[RingMorphism]:
            return self.as_number_field().automorphisms()

        @override
        def class_number(self, proof: bool | None = None) -> Integer:
            return self.as_number_field().class_number(proof=proof)

        @override
        def class_group(self, proof: bool | None = None, names: str = "c") -> AbelianGroup:
            return self.as_number_field().class_group(proof=proof, names=names)

        @override
        def integral_basis(self, v: RingElement | Sequence[RingElement] | None = None) -> tuple[RingElement, ...]:
            return self.as_number_field().integral_basis(v=v)

        @override
        def power_basis(self) -> tuple[RingElement, ...]:
            return self.as_number_field().power_basis()

        @override
        def reduced_basis(self, prec: Integer | int | None = None) -> tuple[RingElement, ...]:
            return self.as_number_field().reduced_basis(prec=prec)

        @override
        def different(self) -> Ideal:
            return self.as_number_field().different()

        @override
        def places(
            self, all_complex: bool = False, prec: Integer | int | None = None
        ) -> tuple[RingMorphism, ...]:
            return self.as_number_field().places(all_complex=all_complex, prec=prec)

        @override
        def real_embeddings(self, prec: Integer | int = 53) -> tuple[RingMorphism, ...]:
            return self.as_number_field().real_embeddings(prec=prec)

        @override
        def complex_embeddings(self, prec: Integer | int = 53) -> tuple[RingMorphism, ...]:
            return self.as_number_field().complex_embeddings(prec=prec)

        @override
        def roots_of_unity(self) -> list[RingElement]:
            return self.as_number_field().roots_of_unity()

        @override
        def regulator(self, proof: bool | None = None) -> RingElement:
            return self.as_number_field().regulator(proof=proof)

        @override
        def units(self, proof: bool | None = None) -> list[RingElement]:
            return self.as_number_field().units(proof=proof)

        @override
        def unit_group(self, proof: bool | None = None) -> AbelianGroup:
            return self.as_number_field().unit_group(proof=proof)

        @override
        def conductor(self, check_abelian: bool = True) -> Integer:
            return self.as_number_field().conductor(check_abelian=check_abelian)

        @override
        def prime_above(self, x: RingElement, degree: Integer | int | None = None) -> PrimeIdeal:
            return self.as_number_field().prime_above(x, degree=degree)

        @override
        def primes_above(self, x: RingElement, degree: Integer | int | None = None) -> list[PrimeIdeal]:
            return self.as_number_field().primes_above(x, degree=degree)

        @override
        def S_units(self, S: Sequence[PrimeIdeal], proof: bool = True) -> list[RingElement]:
            return self.as_number_field().S_units(S, proof=proof)

        @override
        def S_class_group(
            self, S: Sequence[PrimeIdeal], proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup:
            return self.as_number_field().S_class_group(S, proof=proof, names=names)

        @override
        def ring_of_integers(
            self,
            v: Integer | Sequence[Integer] | None = None,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().ring_of_integers(v=v, assume_maximal=assume_maximal)

        @override
        def maximal_order(
            self,
            v: Integer | Sequence[Integer] | None = None,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            return self.as_number_field().maximal_order(v=v, assume_maximal=assume_maximal)

        @override
        def absolute_field(self, names: str) -> Field:
            return self.as_number_field().absolute_field(names)


class _RR(Category_singleton):
    def _repr_object_names(self) -> str:
        return "real field with 53 bits of precision"

    def super_categories(self) -> list[Category]:
        return [_RealFields(), _Fields(), _CompleteRings(), _LocalFields()]

    def __contains__(self, x: object) -> bool:
        from sage.all import RR

        return x is RR

    def object(self):
        from sage.all import RR

        return RR


class _CC(Category_singleton):
    def _repr_object_names(self) -> str:
        return "complex field with 53 bits of precision"

    def super_categories(self) -> list[Category]:
        return [
            _ComplexFields(),
            _Fields(),
            _CompleteRings(),
            _LocalFields(),
            _AlgebraicallyClosedFields(),
        ]

    def __contains__(self, x: object) -> bool:
        from sage.all import CC

        return x is CC

    def object(self):
        from sage.all import CC

        return CC


class _Zp(Category_singleton):
    r"""Category of p-adic integer rings (all primes p, all precision types)."""

    def _repr_object_names(self) -> str:
        return "p-adic integer rings"

    def super_categories(self) -> list[Category]:
        return [_PAdicRings(), _CompleteDiscreteValuationRings(), _LocalRings()]

    def __contains__(self, R: object) -> bool:
        from sage.rings.padics.generic_nodes import pAdicRingGeneric

        return isinstance(R, pAdicRingGeneric)

    class ParentMethods:
        @override
        def completion(self, I: Ideal) -> CompleteRing:
            match I:
                case _ if I.is_zero():
                    return self
                case _ if not I.is_zero():
                    return self
                case unreachable:
                    assert_never(unreachable)


class _Qp(Category_singleton):
    r"""Category of p-adic fields (all primes p, all precision types)."""

    def _repr_object_names(self) -> str:
        return "p-adic fields"

    def super_categories(self) -> list[Category]:
        return [_PAdicRings(), _CompleteDiscreteValuationFields(), _LocalFields()]

    def __contains__(self, R: object) -> bool:
        from sage.rings.padics.generic_nodes import pAdicFieldGeneric

        return isinstance(R, pAdicFieldGeneric)

    class ParentMethods:
        @abstract_method
        def composite(self, subfield1: Field, subfield2: Field) -> Field: ...

        @abstract_method
        def subfield(self, generators: Sequence[RingElement]) -> Field: ...

        @abstract_method
        def subfields_of_degree(self, n: Integer) -> Integer: ...

        @abstract_method
        def exact_field(self) -> Field: ...


class _PolynomialRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "polynomial rings"

    def super_categories(self) -> list[Category]:
        return [Rings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and (isinstance(R, _SAGE_POLYNOMIAL_RING_CLASSES) or isinstance(R, self.parent_class))

    class ParentMethods:
        def is_polynomial_ring(self) -> bool:
            return True

        @override
        def extension(
            self,
            poly: RingElement,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            **kwds,
        ) -> Ring:
            base_ext = self.base_ring().extension(poly, name=name, names=names, **kwds)
            return self.change_ring(base_ext)

        @override
        def completion(self, I: Ideal) -> CompleteRing:
            from sage.rings.infinity import oo

            assert I.is_principal(), "polynomial ring completion expects a principal ideal"
            p = I.gen()
            assert p.is_irreducible(), "polynomial ring completion expects an irreducible generator"
            return super().completion(p, prec=oo)

        @abstract_method
        def gen(self, n: Integer | int = 0) -> RingElement: ...

        @abstract_method
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def change_ring(self, R: Ring) -> Ring: ...

        @abstract_method
        def change_var(self, var: str) -> Ring: ...

        @abstract_method
        def monomials_of_degree(self, n: Integer) -> tuple[RingElement, ...]: ...

        @abstract_method
        def monics(self, *args, **kwds): ...

        @abstract_method
        def cyclotomic_polynomial(self, n: Integer) -> RingElement: ...

        @abstract_method
        def weil_polynomials(self, *args, **kwds): ...


class _PuiseuxSeriesRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "Puiseux series rings"

    def super_categories(self) -> list[Category]:
        return [Rings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_PUISEUX_SERIES_CONTAINMENT_CLASSES) or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        def is_puiseux_series_ring(self) -> bool:
            return True

        @override
        def extension(
            self,
            poly: RingElement,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            **kwds,
        ) -> Ring:
            base_ext = self.base_ring().extension(poly, name=name, names=names, **kwds)
            return self.change_ring(base_ext)

        @abstract_method
        def change_ring(self, R: Ring) -> Ring: ...

        @abstract_method
        def gen(self, n: Integer | int = 0) -> RingElement: ...

        @abstract_method
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def ngens(self) -> int: ...

        @abstract_method
        def laurent_series_ring(self) -> Ring: ...

        @abstract_method
        def default_prec(self) -> Integer | int: ...


class _LaurentSeriesRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "Laurent series rings"

    def super_categories(self) -> list[Category]:
        return [_PuiseuxSeriesRings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES) or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        def is_laurent_series_ring(self) -> bool:
            return True

        @override
        def extension(
            self,
            poly: RingElement,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            **kwds,
        ) -> Ring:
            base_ext = self.base_ring().extension(poly, name=name, names=names, **kwds)
            return self.change_ring(base_ext)

        @abstract_method
        def default_prec(self) -> Integer | int: ...

        @abstract_method
        def gen(self, n: Integer | int = 0) -> RingElement: ...

        @abstract_method
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def ngens(self) -> int: ...

        @abstract_method
        def power_series_ring(self) -> Ring: ...

        @abstract_method
        def change_ring(self, R: Ring) -> Ring: ...


class _PowerSeriesRings(CategoryWithAxiom):
    # _base_category_class_and_axiom set in __init__.py

    def _repr_object_names(self) -> str:
        return "power series rings"

    def super_categories(self) -> list[Category]:
        return [_LaurentSeriesRings()]

    def __contains__(self, R: object) -> bool:
        return R in self.base_category() and (isinstance(R, _SAGE_POWER_SERIES_RING_CLASSES) or isinstance(R, self.parent_class))

    class ParentMethods:
        def is_power_series_ring(self) -> bool:
            return True

        @override
        def extension(
            self,
            poly: RingElement,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            **kwds,
        ) -> Ring:
            base_ext = self.base_ring().extension(poly, name=name, names=names, **kwds)
            return self.change_ring(base_ext)

        @abstract_method
        def default_prec(self) -> Integer | int: ...

        @abstract_method
        def gen(self, n: Integer | int = 0) -> RingElement: ...

        @abstract_method
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def ngens(self) -> int: ...

        @abstract_method
        def laurent_series_ring(self) -> Ring: ...

        @abstract_method
        def change_ring(self, R: Ring) -> Ring: ...

        @abstract_method
        def change_var(self, var: str) -> Ring: ...
