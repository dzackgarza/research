r"""Owned ring implementations and the public ring-construction surface."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.rings.commutative_algebra import (
    AdicCompletions,
    DistinguishedOpenSubobjects,
    FormalPowerSeriesRings,
    GeneratedIdealView,
    PrimeLocalizations,
    PrimeSpectra,
    QuotientRings,
    ZariskiClosedSubobjects,
    Zp,
)
from dzack_research.preamble.categories.rings.commutative_ideals import (
    CommutativeIdeals,
)
from dzack_research.preamble.categories.rings.field_morphisms import ExactFieldMorphism
from dzack_research.preamble.categories.rings.number_fields import (
    CyclotomicField as _CyclotomicField,
)
from dzack_research.preamble.categories.rings.number_fields import (
    NumberFieldsWithChosenPrimitiveElement,
    OwnedNumberFields,
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
    Orders,
    binomial,
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
    RingMor,
    RingMorphism,
    Rings,
    _own_ring,
    _set_owned_ring_display,
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
    cos,
    cosh,
    e,
    exp,
    log,
    pi,
    sech,
    sgn,
    sin,
    sinh,
    sqrt,
    tan,
    tanh,
    zeta,
    ExactRealField,
    ExactRealNumber,
    RealApproximation,
    RealNumber,
)
from dzack_research.preamble.rings.unit_interval import UnitInterval


def _public_commutative_ring(ring):
    if ring not in OwnedRings().Commutative():
        raise TypeError(
            f"expected a commutative ring, but {ring!r} is not in the category of commutative rings"
        )
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

    integers = _own_ring(SageZZ)
    rationals = _own_ring(SageQQ)
    _set_owned_ring_display(integers, "Integer Ring")
    _set_owned_ring_display(rationals, "Rational Field")
    aa = _public_commutative_ring(_own_ring(SageAA))
    _set_owned_ring_display(aa, "Real Algebraic Field")
    qqbar = _public_commutative_ring(_own_ring(SageQQbar))
    _set_owned_ring_display(qqbar, "Algebraic Closure of Rational Field")
    rdf = _public_commutative_ring(_own_ring(SageRDF))
    _set_owned_ring_display(rdf, "Real double field", kind="real")
    cdf = _public_commutative_ring(_own_ring(SageCDF))
    _set_owned_ring_display(cdf, "Complex double field", kind="complex")
    cc = _public_commutative_ring(_own_ring(SageCC))
    _set_owned_ring_display(
        cc,
        f"Complex field with {SageCC.precision()} bits precision",
        kind="complex",
    )
    return {
        "ZZ": integers,
        "QQ": rationals,
        "AA": aa,
        "QQbar": qqbar,
        "RR": RR,
        "RDF": rdf,
        "CDF": cdf,
        "CC": cc,
    }


def ring_constructor_surface() -> dict[str, object]:
    r"""Return the constructors exported into a preamble session."""
    return {
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
    "CommutativeIdeals",
    "CommutativeRings",
    "OwnedCommutativeRings",
    "CompleteLocalRings",
    "ComplexField",
    "CyclotomicField",
    "DistinguishedOpenSubobjects",
    "DivisionRings",
    "ExactFieldMorphism",
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
    "LocalizationRings",
    "LocalRings",
    "NoetherianRings",
    "NonNegativeReals",
    "NumberFieldsWithChosenPrimitiveElement",
    "OrderedRings",
    "Orders",
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
    "binomial",
    "cos",
    "cosh",
    "e",
    "exp",
    "log",
    "pi",
    "sech",
    "sgn",
    "sin",
    "sinh",
    "sqrt",
    "tan",
    "tanh",
    "zeta",
    "RealApproximation",
    "RealField",
    "RealNumber",
    "RingMor",
    "RingMorphism",
    "Rings",
    "UnitInterval",
    "ZariskiClosedSubobjects",
    "Zmod",
    "Zp",
    "ring_constructor_surface",
]
