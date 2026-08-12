"""Cohomological and intersection invariants on projective products."""

from sage.all import QQ, ProjectiveSpace


def test_product_chow_pairing_and_self_intersection() -> None:
    """Intersection pairing agrees with bidegree arithmetic."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y

    L = X.O(4, 4)
    M = X.O(1, 2)
    N = X.O(2, 1)

    assert L * M == 12
    assert L * N == 12
    assert L ** 2 == 32
    assert N.top_self_intersection() == 6


def test_bundle_cohomology_dimensions_match_expected_formula() -> None:
    """`H(i)` dimensions on small divisors are numerically stable."""
    P1_x = ProjectiveSpace(QQ, 1, names=("u", "v"))
    P1_y = ProjectiveSpace(QQ, 1, names=("w", "z"))
    X = P1_x * P1_y

    L = X.O(4, 4)
    assert L.H(0).dimension() == 25
    assert L.H(1).dimension() == 0
    assert L.H(2).dimension() == 0
    assert L.cohomology().dimensions() == (25, 0, 0)

    K = X.canonical_bundle()
    assert K.cohomology().dimensions() == (0, 0, 1)
