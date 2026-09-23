r"""All admissible Young exponents, their a.e. semantics, and the missing pairs."""

import pytest
from sage.all import exp, sgn, sqrt, pi
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import Lp, RR


def test_young_pairings_include_endpoints_and_irrational_exponents() -> None:
    for p, q, r in (
        (1, 1, 1), (1, 2, 2), (2, 2, Infinity), (1, Infinity, Infinity),
        (Infinity, 1, Infinity), (RR(sqrt(2)), RR(sqrt(2)), RR(1) / (RR(sqrt(2)) - RR(1))),
    ):
        left, right, target = (Lp(e).quotient_by_null_functions() for e in (p, q, r))
        pairing = left.convolution_pairing(right)
        assert pairing.domain().tensor_factor(0) is left
        assert pairing.domain().tensor_factor(1) is right
        assert pairing.codomain().integrability_exponent() == target.integrability_exponent()
        assert pairing(left.zero(), right.zero()) == pairing.codomain().zero()
    infinity = Lp(Infinity).quotient_by_null_functions()
    assert infinity(Lp(Infinity).one()) != infinity.zero()
    with pytest.raises(ValueError):
        infinity.convolution_pairing(infinity)


def test_convolution_is_independent_of_a_point_change_in_a_representative() -> None:
    first = Lp(1)
    bounded = Lp(Infinity)
    x = first.indeterminate()
    f = first.quotient_by_null_functions()(first(exp(-x**2)))
    target = bounded.quotient_by_null_functions()
    one, punctured_one = target(bounded.one()), target(bounded(sgn(x)**2))
    pairing = f.parent().convolution_pairing(target)
    expected = target(bounded(sqrt(pi)))
    assert one == punctured_one
    assert pairing(f, one) == expected
    assert pairing(f, punctured_one) == expected
    assert pairing(2 * f, one) == 2 * expected


