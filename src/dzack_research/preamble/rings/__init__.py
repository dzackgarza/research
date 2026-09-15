r"""Owned ring implementations and the public ring-construction surface."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import refine_matrix_algebra
from dzack_research.preamble.categories.algebras.free_algebras import (
    LaurentPolynomialRing as _LaurentPolynomialRing,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    PolynomialRing as _PolynomialRing,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace as _MatrixSpace
from dzack_research.preamble.categories.rings.commutative_algebra import (
    AdicCompletions,
    DistinguishedOpenSubobject,
    DualNumbers,
    FormalPowerSeriesRings,
    GeneratedIdealView,
    PowerSeriesRing,
    PrimeLocalizations,
    PrimeSpectra,
    QuotientRings,
    ZariskiClosedSubobject,
    Zp,
)
from dzack_research.preamble.categories.rings.commutative_ideals import (
    CommutativeIdeal,
    CommutativeIdeals,
)
from dzack_research.preamble.categories.rings.number_fields import (
    CyclotomicField as _CyclotomicField,
)
from dzack_research.preamble.categories.rings.number_fields import (
    NumberField as _NumberField,
)
from dzack_research.preamble.categories.rings.number_fields import (
    NumberFieldsWithChosenPrimitiveElement,
    OwnedNumberFields,
    _refine_number_field_view,
    _refine_order_view,
)
from dzack_research.preamble.categories.rings.number_fields import (
    QuadraticField as _QuadraticField,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    GF as _GF,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    AdicallyCompleteRings,
    ArtinianRings,
    CommutativeRings,
    CompleteLocalRings,
    DivisionRings,
    Fields,
    IntegralDomains,
    LocalizationRings,
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
    OwnedOrderedRings,
    OwnedOrders,
    OwnedPrincipalIdealDomains,
    OwnedRings,
    OwnedRngs,
    OwnedSemirings,
    PredicateSubrings,
    PrimeFields,
    PrincipalIdealDomains,
    RingHomset,
    RingMorphism,
    Rings,
    _own_ring,
    predicate_subring,
    ring_homset,
    ring_morphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    ComplexField as _ComplexField,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    Qp as _Qp,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    RealField as _RealField,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    Zmod as _Zmod,
)
from dzack_research.preamble.rings.nonnegative_reals import NonNegativeReals
from dzack_research.preamble.rings.real import (
    RR,
    ExactRealField,
    ExactRealNumber,
    RealApproximation,
    RealNumber,
)
from dzack_research.preamble.rings.unit_interval import UnitInterval


def _public_commutative_ring(ring):
    if ring not in OwnedRings().Commutative():
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
    from sage.all import RDF as SageRDF
    from sage.all import ZZ as SageZZ
    from sage.all import QQbar as SageQQbar

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
    "AdicCompletions",
    "AdicallyCompleteRings",
    "ArtinianRings",
    "CommutativeIdeal",
    "CommutativeIdeals",
    "CommutativeRings",
    "OwnedCommutativeRings",
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
    "GF",
    "GeneratedIdealView",
    "IntegerModRing",
    "Integers",
    "IntegralDomains",
    "LaurentPolynomialRing",
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
    "PrimeLocalizations",
    "PrimeSpectra",
    "PrincipalIdealDomains",
    "Qp",
    "QuadraticField",
    "QuotientRings",
    "RR",
    "RealApproximation",
    "RealField",
    "RealNumber",
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
