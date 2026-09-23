r"""Young's convolution inequality $L^p * L^q \subseteq L^r$ for $1/p + 1/q = 1 + 1/r$."""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403


@pytest.mark.parametrize(
    "p, q, r",
    [
        (1, 1, 1),
        (1, 2, 2),
        (2, 2, oo),
        (1, oo, oo),
        (oo, 1, oo),
        (RR(sqrt(2)), RR(sqrt(2)), 1 / (RR(sqrt(2)) - 1)),
    ],
)
def test_convolution_of_lp_and_lq_lands_in_lr(p, q, r) -> None:
    r"""$1/p + 1/q = 1 + 1/r$, including the endpoints and $p = q = \sqrt2$, $r = 1/(\sqrt2 - 1)$.

    Source: Lieb–Loss, *Analysis*, Theorem 4.2.
    """
    left = Lp(p).quotient_by_null_functions()
    right = Lp(q).quotient_by_null_functions()
    pairing = left.convolution_pairing(right)

    assert pairing.codomain().integrability_exponent() == r


def test_the_gaussian_convolved_with_one_is_root_pi_on_every_representative() -> None:
    r"""$(e^{-x^2} * 1)(y) = \int e^{-x^2}\,dx = \sqrt\pi$, and changing $1$ at $0$ does not change it."""
    first = Lp(1)
    bounded = Lp(oo)
    x = first.indeterminate()
    f = first.quotient_by_null_functions()(first(exp(-(x**2))))
    target = bounded.quotient_by_null_functions()
    one = target(bounded.one())
    punctured_one = target(bounded(sgn(x) ** 2))
    pairing = f.parent().convolution_pairing(target)
    expected = target(bounded(sqrt(pi)))

    assert pairing(f, one) == expected
    assert pairing(f, punctured_one) == expected
    assert pairing(2 * f, one) == 2 * expected
