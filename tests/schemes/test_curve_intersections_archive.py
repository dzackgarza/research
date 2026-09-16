r"""Gathmann's plane-curve intersection multiplicities retained from the archive.

Gathmann, *Plane Algebraic Curves*, Example 2.13 computes multiplicity ``4``
at the origin for ``y^2-x^3`` and ``x^2-y^3``.  Proposition 2.17 gives
multiplicity ``1`` where their linear parts are independent; at ``(1,1)`` the
two gradients are independent.
"""

from dzack_research.preamble.all import QQ, AffineSpaces


def test_two_cuspidal_plane_curves_have_distinct_local_intersection_multiplicities() -> None:
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    algebra = plane.coordinate_ring()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    first = plane.closed_subscheme(y**2 - x**3)
    second = plane.closed_subscheme(x**2 - y**3)

    origin = plane.underlying_space()(algebra.ideal(x, y))
    transverse = plane.underlying_space()(algebra.ideal(x - 1, y - 1))

    assert first.intersection_multiplicity(second, origin) == 4
    assert first.intersection_multiplicity(second, transverse) == 1
