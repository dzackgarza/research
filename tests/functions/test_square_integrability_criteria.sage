r"""Which elementary maps ``RR -> RR`` are square-integrable.

A polynomial ``p != 0`` is not in ``L^2(RR)`` (``int p^2 = oo``); a rational
function ``p/q`` in lowest terms is in ``L^2`` exactly when ``q`` has no real
root and ``deg q >= deg p + 1``; ``sin`` and ``cos`` of a linear argument are
not, their squares averaging ``1/2``; a Gaussian times a polynomially bounded
map is; a sum of an ``L^2`` map and a non-``L^2`` map is not, since ``L^2`` is
a vector space.  Values: ``int x^2 e^{-x^2} dx = sqrt(pi)/2`` by parts from the
Gaussian integral.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403

import pytest


def test_gaussians_times_bounded_maps_are_square_integrable() -> None:
    r"""``x^2 e^{-x^2}``, ``sin(x) e^{-x^2}``, ``e^{-x^4}`` and ``e^{-x^2} + e^{-|x|}`` are in ``L^2(RR)``."""
    space = Lp(2)
    x = space.indeterminate()

    assert space(x * x * exp(-x * x))(1) == exp(-1)
    assert space(sin(x) * exp(-x * x))(0) == 0
    assert space(exp(-x * x * x * x))(1) == exp(-1)
    assert space(exp(-x * x) + exp(-abs(x)))(0) == 2


def test_the_second_moment_of_the_gaussian() -> None:
    r"""``int x^2 e^{-x^2} dx = sqrt(pi) / 2``."""
    space = Lp(1)
    x = space.indeterminate()

    assert space.integration_morphism()(space(x * x * exp(-x * x))) == sqrt(pi) / 2


def test_nonzero_polynomials_are_not_square_integrable() -> None:
    r"""``int x^2 = int x^4 = oo``."""
    space = Lp(2)
    x = space.indeterminate()

    with pytest.raises(ValueError):
        space(x)
    with pytest.raises(ValueError):
        space(x * x)


def test_cosine_is_not_square_integrable() -> None:
    r"""``int_0^{2 pi N} cos^2 = pi N`` grows without bound."""
    space = Lp(2)
    x = space.indeterminate()

    with pytest.raises(ValueError):
        space(cos(x))


def test_a_square_integrable_map_plus_sine_is_not_square_integrable() -> None:
    r"""If ``e^{-x^2} + sin x`` were in ``L^2`` then so would ``sin x`` be, since ``L^2`` is a vector space."""
    space = Lp(2)
    x = space.indeterminate()

    with pytest.raises(ValueError):
        space(exp(-x * x) + sin(x))


def test_the_gaussian_is_in_every_Lp() -> None:
    r"""``e^{-x^2}`` is bounded and integrable, hence in ``L^p`` for every ``p >= 1``; its value at 0 is 1."""
    x = Lp(3).indeterminate()

    assert Lp(3)(exp(-x * x))(0) == 1
    assert Lp(oo)(exp(-x * x))(0) == 1


def test_a_rational_function_without_real_poles_decaying_like_one_over_x_is_square_integrable() -> None:
    r"""``x / (x^2 + pi)`` has no real pole and ``deg q = deg p + 1``: it is in ``L^2`` and not ``L^1``."""
    x = Lp(2).indeterminate()

    assert Lp(2)(x / (x * x + pi))(0) == 0
    with pytest.raises(ValueError):
        Lp(1)(x / (x * x + pi))


def test_sine_of_a_multiple_of_x_is_not_square_integrable() -> None:
    r"""``int sin(2x)^2 = oo``."""
    x = Lp(2).indeterminate()

    with pytest.raises(ValueError):
        Lp(2)(sin(2 * x))
