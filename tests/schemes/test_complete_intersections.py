
from dzack_research.preamble.all import (
    QQ,
    ProjectiveCompleteIntersections,
    ProjectiveSpaces,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_quotients_and_complete_intersections.sage",
    "live_owner": "tests/schemes/test_complete_intersections.py",
    "owner_overrides": {
        "test_diagonal_sign_quotient_family_has_global_quotient_data": "tests/schemes/test_horikawa_enriques_family.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_projective_complete_intersection_retains_equations_multidegree_and_adjunction_integer() -> None:
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    curve = ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0 * x1 - x2**2, x0**3 + x1**3 + x3**3
    )

    assert curve in ProjectiveCompleteIntersections(QQ)
    assert curve.complete_intersection_ambient() is space
    assert tuple(curve.defining_degrees()) == (2, 3)
    assert curve.complete_intersection_codimension() == 2
    assert curve.expected_dimension() == 1
    assert curve.adjunction_twist_degree() == 1
    assert curve.is_gorenstein()




def test_smooth_complete_intersection_surface_uses_adjunction_for_del_pezzo_degree() -> None:
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    cubic = ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0**3 + x1**3 + x2**3 + x3**3
    )

    assert cubic.expected_dimension() == 2
    assert cubic.anticanonical_twist_degree() == 1
    assert cubic.projective_degree() == 3
    assert cubic.is_del_pezzo()
    assert cubic.del_pezzo_degree() == 3


def test_quartic_k3_boundary_is_not_misclassified_as_del_pezzo() -> None:
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    quartic = ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0**4 + x1**4 + x2**4 + x3**4
    )

    assert quartic.expected_dimension() == 2
    assert quartic.adjunction_twist_degree() == 0
    assert quartic.anticanonical_twist_degree() == 0
    assert not quartic.is_del_pezzo()


def test_normality_of_complete_intersections_uses_r1_not_smoothness() -> None:
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, _x3 = space.homogeneous_coordinate_generators()
    quadric_cone = ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0 * x1 - x2**2
    )

    assert not quadric_cone.is_smooth()
    assert quadric_cone.is_normal()
    assert quadric_cone.is_gorenstein()


def test_a_singular_complete_intersection_curve_is_not_normal() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    x, y, z = plane.homogeneous_coordinate_generators()
    cusp = ProjectiveCompleteIntersections(plane.scheme_base_ring())(
        plane, y**2 * z - x**3
    )

    assert not cusp.is_smooth()
    assert not cusp.is_normal()
    assert cusp.is_gorenstein()


def test_complete_intersection_adjunction_is_an_actual_line_bundle_isomorphism() -> None:
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    curve = ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0 * x1 - x2**2, x0**3 + x1**3 + x3**3
    )
    isomorphism = curve.adjunction_isomorphism()

    assert isomorphism.domain().scheme() is curve
    assert curve.canonical_line_bundle().scheme() is curve
    assert curve.canonical_line_bundle().degree() == 1
    assert curve.restricted_ambient_canonical_bundle().degree() == -4
    assert curve.normal_determinant_line_bundle().degree() == 5
    assert curve.adjunction_target().degree() == 1
    assert isomorphism.domain() is curve.canonical_line_bundle()
    assert isomorphism.codomain() is curve.adjunction_target()
    assert isomorphism.inverse().domain() is curve.adjunction_target()
    assert curve.adjunction_isomorphism() is isomorphism
    composite = isomorphism.inverse() * isomorphism
    assert composite.domain() is curve.canonical_line_bundle()
    assert composite.codomain() is curve.canonical_line_bundle()


def test_del_pezzo_complete_intersection_uses_actual_anticanonical_ampleness() -> None:
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    cubic = ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0**3 + x1**3 + x2**3 + x3**3
    )

    anticanonical = cubic.anticanonical_line_bundle()
    assert anticanonical.scheme() is cubic
    assert anticanonical.degree() == 1
    assert anticanonical.is_ample()
    assert cubic.is_del_pezzo()


def test_two_quadrics_in_projective_four_space_form_a_degree_four_del_pezzo_surface() -> None:
    space = ProjectiveSpaces(QQ)(4, names=("A", "B", "C", "D", "E"))
    A, B, C, D, E = space.homogeneous_coordinate_generators()
    surface = ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, B * D - A * E, C**2 - A * E
    )

    assert tuple(surface.defining_degrees()) == (2, 2)
    assert surface.expected_dimension() == 2
    assert surface.anticanonical_twist_degree() == 1
    assert surface.projective_degree() == 4
    assert surface.is_gorenstein()
    assert surface.is_del_pezzo()
    assert surface.del_pezzo_degree() == 4
    anticanonical = surface.anticanonical_line_bundle()
    assert anticanonical.degree() == 1
    assert anticanonical.is_ample()
