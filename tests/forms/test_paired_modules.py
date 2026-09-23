r"""Hölder pairings of Lebesgue spaces, with values computed by hand."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_the_holder_pairing_of_the_gaussian_in_l1_and_linf_is_root_pi_over_two() -> None:
    r"""$\int_{\mathbb{R}} e^{-x^2} e^{-x^2}\,dx = \int_{\mathbb{R}} e^{-2x^2}\,dx = \sqrt{\pi/2}$."""
    maps = C(oo, RR)
    gaussian = maps(exp(-(maps.indeterminate() ** 2)))
    holder = Lp(1) * Lp(oo)

    assert holder.pairing(Lp(1)(gaussian), Lp(oo)(gaussian)) == RR(sqrt(pi / 2))


def test_the_l2_norm_squared_of_the_gaussian_is_root_pi_over_two() -> None:
    r"""$\|e^{-x^2}\|_2^2 = \int_{\mathbb{R}} e^{-2x^2}\,dx = \sqrt{\pi/2}$, and $q(f) = b(f, f)$."""
    space = Lp(2)
    maps = C(oo, RR)
    gaussian = space(maps(exp(-(maps.indeterminate() ** 2))))

    assert space.b(gaussian, gaussian) == RR(sqrt(pi / 2))
    assert space.q(gaussian) == RR(sqrt(pi / 2))


def test_the_holder_pairing_of_a_geometric_sequence_with_the_constant_one_is_two() -> None:
    r"""$\sum_{n \ge 0} 2^{-n} \cdot 1 = 2$ and $\sum_{n \ge 0} (2^{-n})^2 = 4/3$."""
    n = ell(1).indeterminate()
    holder = ell(1) * ell(oo)
    geometric = ell(2)(2 ** (-ell(2).indeterminate()))

    assert holder.pairing(ell(1)(2 ** (-n)), ell(oo)(1)) == RR(2)
    assert ell(2).q(geometric) == RR(QQ(4) / 3)
