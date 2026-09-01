from sage.categories.monoids import Monoids as SageMonoids
from sage.rings.infinity import Infinity


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_unit_interval_is_the_young_convolution_monoid() -> None:
    session = _session()
    QQ = session["QQ"]
    UnitInterval = session["UnitInterval"]
    NonNegativeReals = session["NonNegativeReals"]
    GradedModules = session["GradedModules"]

    half = UnitInterval(QQ(1) / 2)
    one = UnitInterval.one()
    zero = UnitInterval.zero()

    assert UnitInterval in SageMonoids()
    assert QQ(1) / 2 in UnitInterval
    assert QQ(1) in UnitInterval
    assert QQ(0) in UnitInterval
    assert QQ(2) not in UnitInterval
    assert Infinity not in UnitInterval
    assert one * one == one
    assert one * half == half
    assert half * half == zero
    assert zero * one == zero
    assert GradedModules(session["QQ"], UnitInterval).grading_monoid() is UnitInterval
    assert GradedModules(session["QQ"], UnitInterval) is not GradedModules(
        session["QQ"], NonNegativeReals
    )

    try:
        zero * zero
    except ValueError as error:
        assert "not in [0, 1]" in str(error)
    else:
        raise AssertionError("expected a ValueError")
