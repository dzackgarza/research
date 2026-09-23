"""Projective coordinate maps corestrict through closed subschemes by equations."""

from dzack_research.preamble.all import QQ, ProjectiveSpaces


def test_cubic_parametrization_corestricts_to_its_projective_curve() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("s", "t"))
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    target_ring = plane.O(3).global_sections().homogeneous_coordinate_ring()
    x = target_ring.algebra_generator("x")
    y = target_ring.algebra_generator("y")
    z = target_ring.algebra_generator("z")
    curve = plane.closed_subscheme(y**2 * z - x**2 * (x + z))

    source_ring = line.O(3).global_sections().homogeneous_coordinate_ring()
    s = source_ring.algebra_generator("s")
    t = source_ring.algebra_generator("t")
    ambient = line.projective_morphism_from_coordinates(
        plane,
        ((s**2 - t**2) * t, s * (s**2 - t**2), t**3),
    )
    factor = curve.corestriction(ambient)

    assert factor.domain() is line
    assert factor.codomain() is curve
    assert tuple(factor.homogeneous_coordinates()) == tuple(ambient.homogeneous_coordinates())


