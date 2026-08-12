"""Projective products and Picard-group arithmetic certificates."""

from sage.all import QQ, ProjectiveSpace, matrix, ZZ


def test_picard_group_structure_on_product_of_lines():
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y

    assert X.Pic().rank() == 2
    assert X.O(0, 0) == X.Pic().zero()
    assert (X.O(2, 1) + X.O(-2, -1)) == X.O(0, 0)
    assert X.O(4, 4) * X.O(1, 2) == 12
    assert X.O(2, 1) ** 2 == 4


def test_picard_lattice_matrix_and_duality_data():
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y

    assert X.Picard_lattice().gram_matrix() == matrix(ZZ, [[0, 1], [1, 0]])
    assert X.canonical_bundle() == X.O(-2, -2)
    assert X.anticanonical_bundle() == X.O(2, 2)
    assert X.anticanonical_bundle().is_ample()
