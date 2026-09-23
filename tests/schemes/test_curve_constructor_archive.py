r"""Archive reconciliation for the owned plane-curve constructor."""


from dzack_research.preamble.all import (
    QQ,
    Curves,
    ProjectiveSpaces,
)




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


