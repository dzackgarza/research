"""Singularity and ADE invariants on low-degree families."""

from sage.all import QQ, ProjectiveSpace


def test_curve_singularity_local_invariants_match_A1_and_A3():
    """Simple curves in P1 x P1 recover expected ADE fingerprints."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    curve_a1 = X.subscheme([x1**2 * y0**2 + x0**2 * y1**2])
    p_a1 = curve_a1((1, 0, 1, 0))
    assert p_a1.is_singular()
    assert p_a1.ADE_type() == "A1"
    assert p_a1.milnor_number() == 1
    assert p_a1.tjurina_number() == 1

    curve_a3 = X.subscheme(
        [x0**2 * x1**2 * y0**4
         + x0**4 * y1**4
         + x1**4 * y0**4
         + x1**4 * y1**4]
    )
    p_a3 = curve_a3((1, 0, 1, 0))
    assert p_a3.is_singular()
    assert p_a3.ADE_type() == "A3"
    assert p_a3.milnor_number() == 3
    assert p_a3.tjurina_number() == 3


def test_smooth_curve_points_are_nonsingular():
    """A transverse linear curve has no singular test points."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()
    smooth_curve = X.subscheme([x0 * y0 + x1 * y1])
    p = smooth_curve((1, 0, 0, 1))
    assert not p.is_singular()
