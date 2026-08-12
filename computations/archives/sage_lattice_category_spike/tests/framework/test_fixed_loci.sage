"""Fixed-point subscheme behavior for explicit automorphisms."""

from sage.all import QQ, ProjectiveSpace


def test_fixed_locus_for_product_sign_and_swap_actions() -> None:
    """Coordinate sign automorphisms realize zero- and one-dimensional fixed loci."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    diagonal_sign = X.hom([x0, -x1, y0, -y1], X)
    fixed_sign = diagonal_sign.fixed_subscheme()
    assert fixed_sign.dimension() == 0
    assert len(fixed_sign.rational_points()) == 4

    factor_swap = X.hom([y0, y1, x0, x1], X)
    fixed_swap = factor_swap.fixed_subscheme()
    assert fixed_swap.dimension() == 1
