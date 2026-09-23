r"""Square-integrable functions on the real line.

$f \in L^2(\mathbb R)$ exactly when $\int_{\mathbb R} |f|^2 < \infty$.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def smooth_maps_and_coordinate():
    maps = C(Infinity, RR)
    return maps, maps.indeterminate()


def test_the_gaussian_is_square_integrable_and_x_squared_and_sine_are_not() -> None:
    r"""$\int e^{-2x^2}\,dx = \sqrt{\pi/2}$; $x^2$ and $\sin x$ have divergent square integrals.

    Source: the Gaussian integral; by hand.
    """
    maps, x = smooth_maps_and_coordinate()
    L = Lp(2)
    gaussian = L(maps(exp(-x**2)))
    assert gaussian(0) == 1
    assert L.q(gaussian) == sqrt(pi / 2)
    assert exp(-x**2) in L
    assert x**2 not in L
    assert sin(x) not in L


def test_the_integral_pairing_on_minus_one_one_gives_x_x_two_thirds_and_x_x2_zero() -> None:
    r"""$\int_{-1}^1 x^2\,dx = 2/3$ and $\int_{-1}^1 x^3\,dx = 0$ (an odd integrand).

    Source: by hand.
    """
    maps = C(Infinity, RR)
    x = maps.coordinate()
    xx = maps.integral(x * x, 0)
    xxx = maps.integral(x * x * x, 0)
    assert xx(1) - xx(-1) == QQ(2) / 3
    assert xxx(1) - xxx(-1) == 0


def test_rational_functions_in_l2_are_those_of_degree_at_most_minus_one_without_real_poles() -> None:
    r"""$1/(1+x^2)$ decays like $x^{-2}$; $1/x$ has a non-square-integrable pole at $0$;
    $x^2/(1+x^2) \to 1$ at infinity.

    Source: comparison with $\int |x|^{-2k}$; by hand.
    """
    maps, x = smooth_maps_and_coordinate()
    L = Lp(2)
    assert 1 / (1 + x**2) in L
    assert x / (1 + x**2) in L
    assert 1 / x not in L
    assert x**2 / (1 + x**2) not in L


def test_bounded_multiples_and_decaying_tails_are_in_l2_and_tanh_is_not() -> None:
    r"""$|\sin x/(1+x^2)| \le 1/(1+x^2)$, $\operatorname{sech}(x^2) \le 2e^{-x^2}$, $e^{-\cosh x} \le e^{-|x|/2}$
    are square integrable; $\tanh x \to \pm 1$ is not.

    Source: comparison test; by hand.
    """
    maps, x = smooth_maps_and_coordinate()
    L = Lp(2)
    assert sin(x) / (1 + x**2) in L
    assert sech(x**2) in L
    assert exp(-cosh(x)) in L
    assert tanh(x) not in L


def test_exp_minus_abs_x_is_in_l2_and_exp_minus_x_is_not() -> None:
    r"""$\int e^{-2|x|} = 1$; $\int_{-\infty}^0 e^{-2x} = \infty$. Source: by hand."""
    maps, x = smooth_maps_and_coordinate()
    L = Lp(2)
    assert exp(-abs(x)) in L
    assert exp(-x) not in L


def test_zero_and_x_times_the_gaussian_are_in_l2() -> None:
    r"""$\int x^2 e^{-2x^2}\,dx = \sqrt{\pi/2}/4$. Source: Gaussian moments; by hand."""
    maps, x = smooth_maps_and_coordinate()
    L = Lp(2)
    assert L.zero() in L
    weighted = L(maps(x * exp(-x**2)))
    assert weighted(2) == 2 * exp(-4)
    assert L.q(weighted) == sqrt(pi / 2) / 4
