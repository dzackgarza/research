"""Non-toric product and base-change family regression contracts."""

from sage.all import AffineSpace, QQ, ProjectiveSpace


def test_affine_tensored_product_backbone_is_non_toric_affine():
    """Tensor-product affine presentations keep the expected apex dimension."""
    A1 = AffineSpace(QQ, 1, names=("u", "v"))
    A2 = AffineSpace(QQ, 2, names=("x", "y", "z"))
    mixed_affine = A1.product(A2)

    assert mixed_affine.backend() == "affine-presentation tensor product"
    assert mixed_affine.apex().dimension() == 3


def test_projective_and_affine_base_change_products():
    """Hybrid products keep projection interfaces and base schemes."""
    P1_left = ProjectiveSpace(QQ, 1, names=("a0", "a1"))
    P1_right = ProjectiveSpace(QQ, 1, names=("b0", "b1"))
    X = P1_left * P1_right
    assert X.backend() == "projective-presentation product"
    assert X.apex().dimension() == 2

    AA2 = AffineSpace(QQ, 2, names=("t", "u"))
    mixed = X.product(AA2)
    assert mixed.backend() == "affine-base-change product"
    assert mixed.apex().base_scheme() is AA2
    assert mixed.left_projection().codomain() is X
    assert mixed.right_projection().codomain() is AA2
