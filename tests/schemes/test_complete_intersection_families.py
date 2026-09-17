"""Projective complete-intersection families retain equations under scalar base change."""

from dzack_research.preamble.all import (
    QQ,
    ProjectiveCompleteIntersections,
    ProjectiveSpaces,
)


def _hesse_cubic_family():
    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    plane = ProjectiveSpaces(parameter)(2, names=("x", "y", "z"))
    sections = plane.O(3).global_sections()
    ring = sections.homogeneous_coordinate_ring()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    z = ring.algebra_generator("z")
    scalar = ring.algebra_structure_morphism()
    equation = x**3 + y**3 + z**3 - scalar(parameter(3) * t) * x * y * z
    family = ProjectiveCompleteIntersections(plane.scheme_base_ring())(plane, equation)
    return parameter, family


def test_complete_intersection_family_retains_relative_multidegree_and_morphism() -> None:
    parameter, family = _hesse_cubic_family()

    assert family.scheme_base_ring() is parameter
    assert family.family_base_scheme() is family.base_scheme()
    assert family.family_morphism() is family.structure_morphism()
    assert tuple(family.defining_degrees()) == (3,)
    assert family.expected_dimension() == 1
    assert family.adjunction_twist_degree() == 0


def test_complete_intersection_family_base_change_keeps_equation_and_projection() -> None:
    parameter, family = _hesse_cubic_family()
    at_zero = parameter.Mor(QQ)({"t": QQ.zero()})
    at_one = parameter.Mor(QQ)({"t": QQ.one()})
    smooth = family.base_change(at_zero)
    singular = family.base_change(at_one)

    assert smooth.base_change_source_complete_intersection() is family
    assert smooth.base_change_projection().domain() is smooth
    assert smooth.base_change_projection().codomain() is family
    assert tuple(smooth.defining_degrees()) == (3,)
    assert tuple(singular.defining_degrees()) == (3,)
    assert smooth.is_smooth()
    assert not singular.is_smooth()
