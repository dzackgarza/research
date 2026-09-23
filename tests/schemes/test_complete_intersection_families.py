"""Projective complete-intersection families retain equations under scalar base change."""

import pytest

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


def test_final_height_does_not_make_the_selected_equations_a_regular_sequence() -> None:
    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    plane = ProjectiveSpaces(parameter)(2, names=("x", "y", "z"))
    x, y, _z = plane.homogeneous_coordinate_generators()
    ring = x.parent()
    scalar_t = ring.algebra_structure_morphism()(t)
    # (tx, ty, 1-t) = (x, y, 1-t) has height 3, but x annihilates
    # ty modulo (tx).  Degree-zero homogeneous equations are permitted.
    with pytest.raises(AssertionError, match="regular sequence"):
        ProjectiveCompleteIntersections(parameter)(
            plane, scalar_t * x, scalar_t * y, ring.one() - scalar_t,
        )
    regular = ProjectiveCompleteIntersections(parameter)(
        plane, ring.one() - scalar_t, x, y,
    )
    assert regular.complete_intersection_codimension() == 3


def test_nonflat_scalar_change_does_not_retain_regular_sequence_placement() -> None:
    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    plane = ProjectiveSpaces(parameter)(2, names=("x", "y", "z"))
    x, _y, _z = plane.homogeneous_coordinate_generators()
    scalar_t = x.parent().algebra_structure_morphism()(t)
    family = ProjectiveCompleteIntersections(parameter)(plane, scalar_t * x)
    at_zero = parameter.Mor(QQ)({"t": QQ.zero()})
    at_one = parameter.Mor(QQ)({"t": QQ.one()})
    special = family.base_change(at_zero)
    regular = family.base_change(at_one)
    assert special not in ProjectiveCompleteIntersections(QQ)
    assert regular in ProjectiveCompleteIntersections(QQ)
    assert special.left_projection().codomain() is family
    assert regular.left_projection().codomain() is family
