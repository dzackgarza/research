r"""Smooth functions on $\mathbb{R}$ and the sequence spaces $\ell^p$: textbook values."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_maclaurin_and_taylor_coefficients_of_elementary_functions() -> None:
    r"""$e^x = \sum x^n/n!$, $\sin x = x - x^3/6 + \dots$, $1/(1+x) = \sum (-1)^n x^n$, $e^x = e\sum (x-1)^n/n!$.

    Source: Apostol, *Calculus* I, §10.7 and §10.9.
    """
    maps = C(oo, RR)
    x = maps.indeterminate()
    exponential = maps(exp(x))
    maclaurin = exponential.maclaurin_series()
    at_one = exponential.taylor_series(1)
    sine = maps(sin(x)).maclaurin_series()
    geometric = maps(1 / (1 + x)).maclaurin_series()
    cubic = maps(x**3).maclaurin_series()

    assert maclaurin[0] == 1
    assert maclaurin[1] == 1
    assert maclaurin[5] == QQ(1) / factorial(5)
    assert at_one[0] == exp(1)
    assert at_one[1] == exp(1)
    assert at_one[2] == exp(1) / 2
    assert sine[0] == 0
    assert sine[1] == 1
    assert sine[2] == 0
    assert sine[3] == QQ(-1) / 6
    assert geometric[0] == 1
    assert geometric[1] == -1
    assert geometric[3] == -1
    assert cubic[3] == 1
    assert cubic[4] == 0


def test_the_l2_norm_squared_of_the_gaussian_is_root_pi_over_two() -> None:
    r"""$\|e^{-x^2}\|_2^2 = \int_{\mathbb{R}} e^{-2x^2}\,dx = \sqrt{\pi/2}$."""
    space = Lp(2)
    maps = C(oo, RR)
    gaussian = space(maps(exp(-(maps.indeterminate() ** 2))))

    assert space.b(gaussian, gaussian) == RR(sqrt(pi / 2))
    assert space.q(gaussian) == RR(sqrt(pi / 2))


def test_the_ell2_norm_squared_of_the_geometric_sequence_is_four_thirds() -> None:
    r"""$\sum_{n \ge 0} (2^{-n})^2 = \sum 4^{-n} = 4/3$."""
    space = ell(2)
    geometric = space(2 ** (-space.indeterminate()))

    assert space.b(geometric, geometric) == RR(QQ(4) / 3)
    assert space.q(geometric) == RR(QQ(4) / 3)


def test_the_holder_conjugate_of_ell_p_is_ell_q_with_one_over_p_plus_one_over_q_one() -> None:
    r"""$\ell^1 \times \ell^\infty \to \mathbb{R}$ sends $(2^{-n}, 1)$ to $2$; $\ell^2$ is its own conjugate; $\ell^3$ pairs with $\ell^{3/2}$."""
    n = ell(1).indeterminate()
    holder = ell(1) * ell(oo)

    assert holder.pairing(ell(1)(2 ** (-n)), ell(oo)(1)) == RR(2)
    assert ell(2).pairing_module().right_module().integrability_exponent() == 2
    assert ell(3).pairing_module().right_module().integrability_exponent() == QQ(3) / 2


def test_ell2_pairings_sum_classical_series() -> None:
    r"""Euler's sums through the $\ell^2$ pairing, indices $n \ge 0$.

    $\sum 1/(n+1)^2 = \pi^2/6$, $\sum 1/(n+1)^4 = \pi^4/90$,
    $\sum 1/(n+1)^3 = \zeta(3)$, $\sum 2^{-n}/(n+1) = 2\log 2$,
    $\sum (-1)^n/(n+1)^2 = \pi^2/12$, $\sum 2^{-n}/n! = e^{1/2}$, and the
    $\ell^1 \times \ell^\infty$ pairing gives $\sum 1/n! = e$.  Source:
    Knopp, *Theory and Application of Infinite Series*, §§26, 32, 54.
    """
    n = ell(2).indeterminate()
    geometric = ell(2)(2 ** (-n))
    harmonic = ell(2)(1 / (n + 1))
    basel = ell(2)(1 / (n + 1) ** 2)
    alternating = ell(2)((-1) ** n / (n + 1))
    exponential = ell(2)(1 / factorial(n))

    assert ell(2).b(harmonic, harmonic) == RR(pi**2 / 6)
    assert ell(2).b(basel, basel) == RR(pi**4 / 90)
    assert ell(2).b(harmonic, basel) == RR(zeta(3))
    assert ell(2).b(geometric, harmonic) == RR(2 * log(2))
    assert ell(2).b(harmonic, alternating) == RR(pi**2 / 12)
    assert ell(2).b(exponential, geometric) == RR(exp(QQ(1) / 2))
    assert (ell(1) * ell(oo)).pairing(ell(1)(1 / factorial(n)), ell(oo)(1)) == RR(exp(1))
