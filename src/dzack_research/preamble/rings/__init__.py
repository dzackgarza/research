r"""Owned ring implementations and the public ring-construction surface."""

from dzack_research.preamble.categories.rings.ring_foundation import LocalizationRings
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.rings.real import (
    ExactRealField,
    ExactRealNumber,
    RR,
    RealApproximation,
    RealNumber,
)
from dzack_research.preamble.rings.nonnegative_reals import NonNegativeReals
from dzack_research.preamble.rings.unit_interval import UnitInterval

from dzack_research.preamble.categories.rings.ring_foundation import (
    AdicallyCompleteRings,
    ArtinianRings,
    CommutativeRings,
    CompleteLocalRings,
    ComplexField as _ComplexField,
    DivisionRings,
    Fields,
    FiniteField as _FiniteField,
    GF as _GF,
    IntegerModRing as _IntegerModRing,
    Integers as _Integers,
    IntegralDomains,
    LocalRings,
    NoetherianRings,
    OrderedRings,
    OwnedAdicallyCompleteRings,
    OwnedArtinianRings,
    OwnedCategoryOverBaseRing,
    OwnedCommutativeRings,
    OwnedCompleteLocalRings,
    OwnedDivisionRings,
    OwnedFields,
    OwnedIntegralDomains,
    OwnedLocalRings,
    OwnedNoetherianRings,
    OwnedOrders,
    OwnedOrderedRings,
    OwnedPrincipalIdealDomains,
    OwnedRings,
    OwnedRngs,
    OwnedSemirings,
    PredicateSubrings,
    PrimeField as _PrimeField,
    PrimeFields,
    PrincipalIdealDomains,
    Qp as _Qp,
    RealField as _RealField,
    RingHomset,
    RingMorphism,
    Rings,
    Zmod as _Zmod,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
    predicate_subring,
    ring_homset,
    ring_morphism,
)
from dzack_research.preamble.categories.rings.commutative_ideals import (
    CommutativeIdeal,
    CommutativeIdeals,
)
from dzack_research.preamble.categories.rings.commutative_algebra import (
    AdicCompletion,
    AdicCompletions,
    DistinguishedOpenSubobject,
    DualNumbers,
    FormalPowerSeriesRings,
    GeneratedIdealView,
    Localization,
    PowerSeriesRing,
    PrimeLocalization,
    PrimeLocalizations,
    PrimeSpectra,
    QuotientRing,
    QuotientRings,
    ResidueField,
    ZariskiClosedSubobject,
    Zp,
)
from dzack_research.preamble.categories.rings.number_fields import (
    CyclotomicField as _CyclotomicField,
    NumberField as _NumberField,
    NumberFieldsWithChosenPrimitiveElement,
    OwnedNumberFields,
    QuadraticField as _QuadraticField,
    _refine_number_field_view,
    _refine_order_view,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    LaurentPolynomialRing as _LaurentPolynomialRing,
    PolynomialRing as _PolynomialRing,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace as _MatrixSpace
from dzack_research.preamble.categories.algebras.algebras import refine_matrix_algebra


def _public_commutative_ring(ring):
    if ring not in OwnedCommutativeRings():
        raise TypeError("the public commutative-ring surface requires an owned commutative ring")
    return ring


def GF(*args, **kwargs):
    return _public_commutative_ring(_GF(*args, **kwargs))


FiniteField = GF


def PrimeField(characteristic):
    return GF(characteristic)


def Zmod(*args, **kwargs):
    return _public_commutative_ring(_Zmod(*args, **kwargs))


IntegerModRing = Zmod
Integers = Zmod


def Qp(*args, **kwargs):
    return _public_commutative_ring(_Qp(*args, **kwargs))


def RealField(*args, **kwargs):
    return _public_commutative_ring(_RealField(*args, **kwargs))


def ComplexField(*args, **kwargs):
    return _public_commutative_ring(_ComplexField(*args, **kwargs))


def CyclotomicField(*args, **kwargs):
    return _CyclotomicField(*args, **kwargs)


def QuadraticField(*args, **kwargs):
    return _QuadraticField(*args, **kwargs)


def NumberField(polynomial, *args, **kwargs):
    return _NumberField(polynomial, *args, **kwargs)


def PolynomialRing(base_ring, *args, **kwargs):
    return _PolynomialRing(base_ring, *args, **kwargs)


def LaurentPolynomialRing(base_ring, *args, **kwargs):
    return _LaurentPolynomialRing(base_ring, *args, **kwargs)


def FractionField(ring, *args, **kwargs):
    r"""Return the owned fraction field of ``ring``."""
    if args or kwargs:
        raise TypeError("FractionField takes one owned ring")
    return ring.fraction_field()


def MatrixSpace(base_ring, nrows, ncols=None):
    r"""Return the public finite matrix Hom, with algebra structure when square."""
    return refine_matrix_algebra(_MatrixSpace(base_ring, nrows, ncols))


@cached_function
def session_ring_objects() -> dict[str, object]:
    r"""Return the standard session scalar names under their owned parents."""
    from sage.all import AA as SageAA
    from sage.all import CC as SageCC
    from sage.all import CDF as SageCDF
    from sage.all import QQ as SageQQ
    from sage.all import QQbar as SageQQbar
    from sage.all import RDF as SageRDF
    from sage.all import ZZ as SageZZ

    integers = _refine_order_view(_own_ring(SageZZ))
    rationals = _refine_number_field_view(_own_ring(SageQQ))
    return {
        "ZZ": integers,
        "QQ": rationals,
        "AA": _public_commutative_ring(_own_ring(SageAA)),
        "QQbar": _public_commutative_ring(_own_ring(SageQQbar)),
        "RR": RR,
        "RDF": _public_commutative_ring(_own_ring(SageRDF)),
        "CDF": _public_commutative_ring(_own_ring(SageCDF)),
        "CC": _public_commutative_ring(_own_ring(SageCC)),
    }


def ring_constructor_surface() -> dict[str, object]:
    r"""Return the constructors exported into a preamble session."""
    return {
        "DualNumbers": DualNumbers,
        "GF": GF,
        "FiniteField": FiniteField,
        "PrimeField": PrimeField,
        "Zmod": Zmod,
        "IntegerModRing": IntegerModRing,
        "Integers": Integers,
        "Zp": Zp,
        "Qp": Qp,
        "RealField": RealField,
        "ComplexField": ComplexField,
        "CyclotomicField": CyclotomicField,
        "QuadraticField": QuadraticField,
        "NumberField": NumberField,
        "PolynomialRing": PolynomialRing,
        "LaurentPolynomialRing": LaurentPolynomialRing,
        "PowerSeriesRing": PowerSeriesRing,
        "ResidueField": ResidueField,
        "MatrixSpace": MatrixSpace,
    }


def _restore_session_ring_bindings(scope: dict) -> None:
    r"""Restore public scalar names after Sage code has modified a namespace.

    This is namespace repair only: the objects returned by
    :func:`session_ring_objects` are already fully constructed owned objects.
    """
    scope.update(session_ring_objects())
    scope.update(ring_constructor_surface())


__all__ = [
    "AdicCompletion",
    "AdicCompletions",
    "AdicallyCompleteRings",
    "ArtinianRings",
    "CommutativeIdeal",
    "CommutativeIdeals",
    "CommutativeRings",
    "CompleteLocalRings",
    "ComplexField",
    "CyclotomicField",
    "DistinguishedOpenSubobject",
    "DivisionRings",
    "DualNumbers",
    "ExactRealField",
    "ExactRealNumber",
    "Fields",
    "FiniteField",
    "FormalPowerSeriesRings",
    "FractionField",
    "GF",
    "GeneratedIdealView",
    "IntegerModRing",
    "Integers",
    "IntegralDomains",
    "LaurentPolynomialRing",
    "Localization",
    "LocalizationRings",
    "LocalRings",
    "MatrixSpace",
    "NoetherianRings",
    "NonNegativeReals",
    "NumberField",
    "NumberFieldsWithChosenPrimitiveElement",
    "OrderedRings",
    "OwnedAdicallyCompleteRings",
    "OwnedArtinianRings",
    "OwnedCategoryOverBaseRing",
    "OwnedCommutativeRings",
    "OwnedCompleteLocalRings",
    "OwnedDivisionRings",
    "OwnedFields",
    "OwnedIntegralDomains",
    "OwnedLocalRings",
    "OwnedNoetherianRings",
    "OwnedNumberFields",
    "OwnedOrders",
    "OwnedOrderedRings",
    "OwnedPrincipalIdealDomains",
    "OwnedRings",
    "OwnedRngs",
    "OwnedSemirings",
    "PolynomialRing",
    "PowerSeriesRing",
    "PredicateSubrings",
    "PrimeField",
    "PrimeFields",
    "PrimeLocalization",
    "PrimeLocalizations",
    "PrimeSpectra",
    "PrincipalIdealDomains",
    "Qp",
    "QuadraticField",
    "QuotientRing",
    "QuotientRings",
    "RR",
    "RealApproximation",
    "RealField",
    "RealNumber",
    "ResidueField",
    "RingHomset",
    "RingMorphism",
    "Rings",
    "UnitInterval",
    "ZariskiClosedSubobject",
    "Zmod",
    "Zp",
    "predicate_subring",
    "ring_constructor_surface",
    "ring_homset",
    "ring_morphism",
]
