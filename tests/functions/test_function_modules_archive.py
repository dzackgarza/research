r"""Archive reconciliation for the function-module mathematics.

The historical ``smooth_functions`` and ``square_integrable_functions``
parents were replaced by the general mapping-space and Lebesgue-space owners.
These specimens retain the independent mathematical assertions from that
archive without reinstating its separate module hierarchy.
"""

import pytest

from sage.all import SR, exp, sin
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import C, Lp, RR


def test_archived_function_modules_are_the_live_mapping_and_lebesgue_spaces() -> None:
    smooth = C(Infinity, RR)
    square_integrable = Lp(2)
    x = smooth.indeterminate()

    f = smooth(x**2)
    g = smooth(x)
    assert (f + g)(3) == 12
    assert (2 * f)(3) == 18

    gaussian = square_integrable(smooth(exp(-(x**2))))
    assert gaussian(0) == 1
    assert square_integrable.b(gaussian, gaussian) == square_integrable.q(gaussian)


def test_symbolic_l2_membership_retains_the_archived_exact_rational_boundary() -> None:
    space = Lp(2)
    x = SR.var("x")

    assert space(1 / (1 + x**2))(0) == 1
    assert space(x / (1 + x**2))(1) == RR(1) / 2

    with pytest.raises(ValueError, match="not square-integrable"):
        space(x**2)
    with pytest.raises(ValueError, match="not square-integrable"):
        space(1 / x)
    with pytest.raises(ValueError, match="not square-integrable"):
        space(x**2 / (1 + x**2))


def test_symbolic_l2_membership_retains_schwartz_sum_and_bounded_product_cases() -> None:
    space = Lp(2)
    x = SR.var("x")

    assert space(x * exp(-(x**2)))(2) == 2 * exp(-4)
    assert space(3 * exp(-(x**2)) - 2 / (1 + x**2))(0) == 1
    assert space(sin(x) / (1 + x**2))(0) == 0

    with pytest.raises(ValueError, match="not square-integrable"):
        space(sin(x))


def test_opaque_callable_remains_an_explicit_placement_claim() -> None:
    space = Lp(2)

    placed = space(lambda point: point**2)
    assert placed(3) == 9
    assert (placed + space.zero())(3) == 9
