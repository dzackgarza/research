r"""Cotangent and tangent spaces at a point of an affine spectrum.

The cotangent space is the fibre of the module of Kähler differentials, and the
tangent space is its dual over the residue field.  For the affine plane both
have dimension two at every point; for the node ``y^2 = x^3 + x^2`` the
cotangent space at the origin still has dimension two while the curve has
dimension one, which is what makes the origin singular.
"""

from dzack_research.preamble.all import (
    FinitelyPresentedAlgebra,
    KahlerDifferentials,
    PolynomialRing,
    QQ,
)


def test_the_affine_plane_has_a_two_dimensional_cotangent_space() -> None:
    plane = PolynomialRing(QQ, "x,y")
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    differentials = KahlerDifferentials(plane)
    origin = plane.spectrum()(plane.ideal(x, y))

    assert differentials.cotangent_space(origin).dimension() == 2
    assert differentials.tangent_space(origin).base_ring() is origin.residue_field()


def test_the_node_has_a_two_dimensional_cotangent_space_at_its_singular_point() -> None:
    plane = PolynomialRing(QQ, "x,y")
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    node = FinitelyPresentedAlgebra(plane, [y**2 - x**3 - x**2])
    differentials = KahlerDifferentials(node)
    origin = node.spectrum()(node.ideal(node(x), node(y)))

    assert differentials.cotangent_space(origin).dimension() == 2
