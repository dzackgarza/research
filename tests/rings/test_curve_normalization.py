r"""Normalization, conductor, and delta for represented affine curve domains."""

import pytest

from dzack_research.preamble.all import QQ, ZZ


def _cusp_ring():
    polynomial = QQ.polynomial_ring("x", "y")
    x, y = (polynomial.algebra_generator(name) for name in ("x", "y"))
    return polynomial.quotient_ring(polynomial.ideal(y**2 - x**3))


def test_cusp_normalization_retains_the_actual_finite_birational_map() -> None:
    cusp = _cusp_ring()
    normalization = cusp.normalization()
    normalization_map = cusp.normalization_map()

    assert normalization_map.domain() is cusp
    assert normalization_map.codomain() is normalization
    assert normalization.is_normal()
    assert not cusp.is_normal()
    assert cusp.delta_invariant() == 1


def test_cusp_conductor_is_a_proper_ideal_of_the_original_curve_ring() -> None:
    cusp = _cusp_ring()
    conductor = cusp.conductor_ideal()

    assert conductor.ring() is cusp
    assert cusp.zero() in conductor
    assert cusp.one() not in conductor


def test_a_smooth_affine_line_is_its_own_normalization() -> None:
    polynomial = QQ.polynomial_ring("x", "y")
    x, y = (polynomial.algebra_generator(name) for name in ("x", "y"))
    line = polynomial.quotient_ring(polynomial.ideal(y - x))

    assert line.is_normal()
    assert line.delta_invariant() == 0
    assert line.conductor_ideal() == line.ideal(line.one())


def test_normalization_rejects_a_non_polynomial_quotient_at_its_frontier() -> None:
    quotient = ZZ.quotient_ring(ZZ.ideal(ZZ(6)))

    with pytest.raises(AssertionError, match="symmetric-algebra presentation"):
        quotient.normalization()
