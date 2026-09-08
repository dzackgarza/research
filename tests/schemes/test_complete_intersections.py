import pytest

from dzack_research.preamble.all import (
    ProjectiveCompleteIntersection,
    ProjectiveCompleteIntersections,
    ProjectiveSpace,
    QQ,
)


def test_projective_complete_intersection_retains_equations_multidegree_and_adjunction_integer() -> None:
    space = ProjectiveSpace(3, QQ)
    x0, x1, x2, x3 = space.gens()
    curve = ProjectiveCompleteIntersection(
        space.closed_subscheme(x0 * x1 - x2**2, x0**3 + x1**3 + x3**3)
    )

    assert curve in ProjectiveCompleteIntersections(QQ)
    assert curve.complete_intersection_ambient() is space
    assert tuple(curve.defining_degrees()) == (2, 3)
    assert curve.complete_intersection_codimension() == 2
    assert curve.expected_dimension() == 1
    assert curve.adjunction_twist_degree() == 1
    assert curve.is_gorenstein()


def test_redundant_homogeneous_equations_are_not_misclassified_as_a_complete_intersection() -> None:
    space = ProjectiveSpace(3, QQ)
    x0, x1, _x2, _x3 = space.gens()
    redundant = space.closed_subscheme(x0, x0 * x1)

    with pytest.raises(ValueError):
        ProjectiveCompleteIntersection(redundant)


def test_smooth_complete_intersection_surface_uses_adjunction_for_del_pezzo_degree() -> None:
    space = ProjectiveSpace(3, QQ)
    x0, x1, x2, x3 = space.gens()
    cubic = ProjectiveCompleteIntersection(
        space.closed_subscheme(x0**3 + x1**3 + x2**3 + x3**3)
    )

    assert cubic.expected_dimension() == 2
    assert cubic.anticanonical_twist_degree() == 1
    assert cubic.projective_degree() == 3
    assert cubic.is_del_pezzo()
    assert cubic.del_pezzo_degree() == 3


def test_quartic_k3_boundary_is_not_misclassified_as_del_pezzo() -> None:
    space = ProjectiveSpace(3, QQ)
    x0, x1, x2, x3 = space.gens()
    quartic = ProjectiveCompleteIntersection(
        space.closed_subscheme(x0**4 + x1**4 + x2**4 + x3**4)
    )

    assert quartic.expected_dimension() == 2
    assert quartic.adjunction_twist_degree() == 0
    assert quartic.anticanonical_twist_degree() == 0
    assert not quartic.is_del_pezzo()


def test_normality_of_complete_intersections_uses_r1_not_smoothness() -> None:
    space = ProjectiveSpace(3, QQ)
    x0, x1, x2, _x3 = space.gens()
    quadric_cone = ProjectiveCompleteIntersection(
        space.closed_subscheme(x0 * x1 - x2**2)
    )

    assert not quadric_cone.is_smooth()
    assert quadric_cone.is_normal()
    assert quadric_cone.is_gorenstein()


def test_a_singular_complete_intersection_curve_is_not_normal() -> None:
    plane = ProjectiveSpace(2, QQ)
    x, y, z = plane.gens()
    cusp = ProjectiveCompleteIntersection(plane.closed_subscheme(y**2 * z - x**3))

    assert not cusp.is_smooth()
    assert not cusp.is_normal()
    assert cusp.is_gorenstein()
