r"""Which functions on $\mathbb{R}$ are square-integrable."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_rational_functions_in_l2_are_those_with_no_real_pole_and_decay() -> None:
    r"""$1/(1+x^2)$ and $x/(1+x^2)$ are in $L^2(\mathbb{R})$; $x^2$, $1/x$ and $x^2/(1+x^2)$ are not.

    A rational function is square-integrable on $\mathbb{R}$ iff it has no
    real pole and its degree is at most $-1$ at infinity.
    """
    space = Lp(2)
    x = space.indeterminate()

    assert 1 / (1 + x**2) in space
    assert x / (1 + x**2) in space
    assert x**2 not in space
    assert 1 / x not in space
    assert x**2 / (1 + x**2) not in space
    assert space(x / (1 + x**2))(1) == RR(1) / 2


def test_decaying_and_bounded_products_are_in_l2_but_sine_is_not() -> None:
    r"""$x e^{-x^2}$, $3e^{-x^2} - 2/(1+x^2)$ and $\sin(x)/(1+x^2)$ are in $L^2(\mathbb{R})$; $\sin x$ is not."""
    space = Lp(2)
    x = space.indeterminate()

    assert x * exp(-(x**2)) in space
    assert 3 * exp(-(x**2)) - 2 / (1 + x**2) in space
    assert sin(x) / (1 + x**2) in space
    assert sin(x) not in space
    assert space(x * exp(-(x**2)))(2) == 2 * exp(-4)


def test_two_sided_exponential_decay_is_in_l2_but_one_sided_is_not() -> None:
    r"""$\int_{\mathbb{R}} e^{-2|x|}\,dx = 1$, while $e^{-2x}$ is not integrable on $(-\infty, 0]$."""
    space = Lp(2)
    x = space.indeterminate()
    two_sided = space(exp(-abs(x)))

    assert exp(-abs(x)) in space
    assert exp(-x) not in space
    assert space.q(two_sided) == 1
