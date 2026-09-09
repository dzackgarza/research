"""Archive reconciliation for varieties, curves, and surfaces."""

from dzack_research.preamble.all import (
    AffineSpace,
    Curves,
    ProjectiveSpace,
    QQ,
    Surfaces,
    Varieties,
)


def test_archived_dimension_subtrees_are_live_full_subcategories() -> None:
    affine_line = AffineSpace(1, QQ, names=("t",))
    affine_plane = AffineSpace(2, QQ, names=("x", "y"))
    projective_line = ProjectiveSpace(1, QQ)
    projective_plane = ProjectiveSpace(2, QQ)

    assert affine_line in Varieties(QQ)
    assert affine_line in Curves(QQ)
    assert affine_line not in Surfaces(QQ)

    assert affine_plane in Varieties(QQ)
    assert affine_plane in Surfaces(QQ)
    assert affine_plane not in Curves(QQ)

    assert projective_line in Curves(QQ)
    assert projective_plane in Surfaces(QQ)


def test_reducible_dimension_one_scheme_is_not_promoted_to_an_archived_variety() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    x, y = plane.coordinate_ring().algebra_generators()
    reducible_curve = plane.closed_subscheme(x * y)

    assert reducible_curve.relative_dimension() == 1
    assert reducible_curve not in Varieties(QQ)
    assert reducible_curve not in Curves(QQ)
