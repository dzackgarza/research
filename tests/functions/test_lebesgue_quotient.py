r"""Almost-everywhere classes, not equality of selected pointwise maps."""

from sage.all import exp, sgn
from sage.rings.infinity import Infinity
from sage.misc.unknown import Unknown

from dzack_research.preamble.all import Lp, RR, Sets
from dzack_research.preamble.logic import ask


def test_a_single_point_change_vanishes_in_the_lebesgue_quotient() -> None:
    maps = Lp(Infinity)
    x = maps.indeterminate()
    punctured_one = maps(sgn(x)**2)
    one = maps.one()
    assert punctured_one(RR.zero()) == RR.zero()
    assert one(RR.zero()) == RR.one()
    quotient = maps.quotient_by_null_functions()
    projection = quotient.quotient_projection()
    assert projection.domain() is maps
    assert projection.codomain() is quotient
    assert projection(punctured_one) == projection(one)
    assert projection(punctured_one - one) == quotient.zero()
    assert projection(2 * punctured_one + one) == 3 * projection(one)
    assert ask(maps.almost_everywhere_equal(punctured_one, one)) is True


def test_quotient_keeps_a_nonzero_function_and_does_not_sample_callable_equality() -> None:
    maps = Lp(2)
    x = maps.indeterminate()
    gaussian = maps(exp(-x**2))
    quotient = maps.quotient_by_null_functions()
    assert quotient(gaussian) != quotient.zero()
    assert quotient(gaussian).representative().parent() is maps
    left = maps(Sets().Mor(RR, RR)(lambda t: RR.zero()))
    right = maps(Sets().Mor(RR, RR)(lambda t: RR.zero()))
    assert (quotient(left) == quotient(right)) is Unknown
    assert (quotient(left) != quotient(right)) is Unknown
    assert quotient(left) == quotient(left)
