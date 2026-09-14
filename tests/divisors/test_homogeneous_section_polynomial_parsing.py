r"""Homogeneous polynomial sections accept the engine's exponent containers."""

from dzack_research.preamble.all import ProjectiveSpace, QQ


def test_projective_line_section_parses_multivariate_exponent_tuples() -> None:
    line = ProjectiveSpace(1, QQ, names=("x", "y"))
    sections = line.O(1).global_sections()
    ring = sections.homogeneous_coordinate_ring()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")

    section = sections.section_from_homogeneous_polynomial(x + y)

    assert sections.homogeneous_polynomial(section) == x + y
    assert section == sections.module_generator(x) + sections.module_generator(y)
