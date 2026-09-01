from sage.categories.additive_monoids import AdditiveMonoids as SageAdditiveMonoids
from sage.rings.infinity import Infinity, minus_infinity
from sage.rings.semirings.non_negative_integer_semiring import NN


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_nonnegative_extended_reals_are_the_additive_monoid_of_holder_degrees() -> None:
    session = _session()
    QQ = session["QQ"]
    RR = session["RR"]
    NonNegativeReals = session["NonNegativeReals"]
    GradedAlgebras = session["GradedAlgebras"]

    half = NonNegativeReals(QQ(1) / 2)
    one = NonNegativeReals(1)
    infinity = NonNegativeReals(Infinity)

    assert NonNegativeReals in SageAdditiveMonoids()
    assert NN(3) in NonNegativeReals
    assert QQ(1) / 2 in NonNegativeReals
    assert Infinity in NonNegativeReals
    assert RR(-1) not in NonNegativeReals
    assert minus_infinity not in NonNegativeReals
    assert half + half == one
    assert one + infinity == infinity
    assert infinity + infinity == infinity
    assert NonNegativeReals.zero() + half == half
    assert ~NonNegativeReals.zero() == infinity
    assert ~infinity == NonNegativeReals.zero()
    assert ~half == NonNegativeReals(2)
    assert GradedAlgebras(QQ, NonNegativeReals) is not GradedAlgebras(QQ, NN)
    assert GradedAlgebras(QQ, NonNegativeReals).grading_monoid() is NonNegativeReals
