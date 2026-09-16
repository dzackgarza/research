"""Archive reconciliation for varieties, curves, and surfaces."""

from dzack_research.preamble.all import (
    QQ,
    AffineSpaces,
    Curves,
    ProjectiveSpaces,
    Surfaces,
    Varieties,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/varieties.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/varieties.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_dimension_subtrees_are_live_full_subcategories() -> None:
    affine_line = AffineSpaces(QQ)(1, names=("t",))
    affine_plane = AffineSpaces(QQ)(2, names=("x", "y"))
    projective_line = ProjectiveSpaces(QQ)(1)
    projective_plane = ProjectiveSpaces(QQ)(2)

    assert affine_line in Varieties(QQ)
    assert affine_line in Curves(QQ)
    assert affine_line not in Surfaces(QQ)

    assert affine_plane in Varieties(QQ)
    assert affine_plane in Surfaces(QQ)
    assert affine_plane not in Curves(QQ)

    assert projective_line in Curves(QQ)
    assert projective_plane in Surfaces(QQ)


def test_reducible_dimension_one_scheme_is_not_promoted_to_an_archived_variety() -> None:
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    x, y = plane.coordinate_ring().algebra_generators()
    reducible_curve = plane.closed_subscheme(x * y)

    assert reducible_curve.relative_dimension() == 1
    assert reducible_curve not in Varieties(QQ)
    assert reducible_curve not in Curves(QQ)
