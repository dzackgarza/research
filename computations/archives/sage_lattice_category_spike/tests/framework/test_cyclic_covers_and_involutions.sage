"""Cyclic covers and involutive lifts on projective products."""

from sage.all import QQ, ProjectiveSpace


def test_cyclic_cover_datum_and_cover_morphism():
    """Cyclic-cover datum is compatible with branch data and map invariants."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    line_bundle = X.O(2, 2)
    branch_bundle = X.O(4, 4)
    section = branch_bundle.H(0).from_polynomial(
        x0**4 * y0**4
        + x0**4 * y1**4
        + x1**4 * y0**4
        + x1**4 * y1**4
    )

    datum = line_bundle.cyclic_cover_datum(section, 2)
    cover = line_bundle.cyclic_cover(section, 2)

    assert datum.degree() == 2
    assert datum.branch_line_bundle() == branch_bundle
    assert datum.cover_algebra_datum().pieces() == (X.O(0, 0), -line_bundle)
    assert datum.branch_subscheme().dimension() == 1

    assert cover.domain().dimension() == X.dimension()
    assert cover.codomain() == X
    assert cover.cover_degree() == 2
    assert cover.is_finite()
    assert cover.branch_subscheme() == datum.branch_subscheme()
    assert cover.ramification_subscheme().dimension() == 1


def test_involution_lifts_of_cyclic_cover():
    """A branch-even involution has two lifted automorphisms on the cover."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    line_bundle = X.O(2, 2)
    branch_bundle = X.O(4, 4)
    section = branch_bundle.H(0).from_polynomial(
        x0**4 * y0**4
        + x0**4 * y1**4
        + x1**4 * y0**4
        + x1**4 * y1**4
    )
    cover = line_bundle.cyclic_cover(section, 2)

    involution = X.hom([x0, -x1, y0, -y1], X)
    assert cover.branch_scaling(involution) == 1

    lifts = cover.lift_automorphisms(involution)
    assert len(lifts) == 2
    for lift in lifts:
        assert lift.is_automorphism()
        assert lift * lift == cover.domain().identity_morphism()
