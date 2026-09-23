r"""Archive reconciliation for the owned plane-curve constructor."""

import pytest

from dzack_research.preamble.all import (
    QQ,
    AffineSpaces,
    ClosedSubschemes,
    Curves,
    ProjectiveSpaces,
)


def test_curve_without_ambient_uses_the_polynomial_framing() -> None:
    polynomial_ring = QQ.polynomial_ring(("x", "y"))
    x, y = polynomial_ring.algebra_generators()
    curve = Curves(QQ).from_equation(y - x**2)

    assert curve in Curves(QQ)
    assert curve in ClosedSubschemes(QQ)
    assert curve.relative_dimension() == 1
    ambient = curve.inclusion().codomain()
    assert ambient in Curves(QQ).super_categories()[0]
    assert ambient.relative_dimension() == 2


def test_curve_with_projective_ambient_retains_the_actual_closed_embedding() -> None:
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    coordinate_ring = plane.coordinate_ring()
    x = coordinate_ring.algebra_generator("x")
    y = coordinate_ring.algebra_generator("y")
    z = coordinate_ring.algebra_generator("z")
    cubic = Curves(QQ).from_equation(y**2 * z - x**3, plane)

    assert cubic in Curves(QQ)
    assert cubic.inclusion().codomain() is plane
    assert cubic.arithmetic_genus() == 1


def test_curve_rejects_a_reducible_one_dimensional_closed_subscheme() -> None:
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    coordinate_ring = plane.coordinate_ring()
    x = coordinate_ring.algebra_generator("x")
    y = coordinate_ring.algebra_generator("y")

    with pytest.raises(AssertionError, match="not an integral curve"):
        Curves(QQ).from_equation(x * y, plane)
