r"""Almost-everywhere classes, not equality of selected pointwise maps."""

from sage.all import sgn
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import Lp, RR
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




