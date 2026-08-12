"""Complete-intersection and quotient-family certificates."""

from sage.all import CyclicPermutationGroup, QQ, ProjectiveSpace


def test_complete_intersection_certificate_for_an_affine_quadric_surface() -> None:
    """A quadratic surface in P4 has the expected complete-intersection data."""
    P = ProjectiveSpace(QQ, 4, names=("A", "B", "C", "D", "E"))
    A, B, C, D, E = P.gens()

    W = P.subscheme([B * D - A * E, C**2 - A * E])
    K = W.canonical_bundle()
    minus_K = W.anticanonical_bundle()

    assert W.is_complete_intersection()
    assert W.complete_intersection_degrees() == (2, 2)
    assert W.complete_intersection_certificate().degree_matches()
    assert W.is_normal()
    assert W.is_gorenstein()
    assert W.is_del_Pezzo()
    assert K == W.O(-1)
    assert minus_K == W.O(1)
    assert minus_K.is_ample()
    assert minus_K**2 == 4
    assert W.anticanonical_degree() == 4
    assert W.del_Pezzo_degree() == 4


def test_diagonal_sign_quotient_family_has_global_quotient_data() -> None:
    """Diagonal sign automorphisms induce compatible enriques quotient families."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    involution = X.hom([x0, -x1, y0, -y1], X)
    X.Aut().action(CyclicPermutationGroup(2), [involution])
    quotient_family = X.O(0, 0).complete_linear_system().cyclic_cover_family(
        X.O(0, 0),
        2,
        parameter_names=("a",),
    )
    enriques = quotient_family.enriques_lift(involution, fiber_scalar=-1)
    enriques_quotient = enriques.quotient()

    assert enriques.is_automorphism()
    assert enriques.is_compatible()
    assert enriques_quotient.base_scheme() is quotient_family.parameter_space()
    assert enriques_quotient.covered_scheme().is_separated()
