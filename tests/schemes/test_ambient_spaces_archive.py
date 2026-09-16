"""Archive reconciliation for the ambient affine/projective space owners."""

from dzack_research.preamble.all import (
    QQ,
    AffineSpaces,
    ProjectiveSpaces,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/ambient_spaces.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/schemes.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_affine_space_constructor_is_owned_by_affine_spaces() -> None:
    affine = AffineSpaces(QQ)(2, names=("x", "y"))

    assert affine in AffineSpaces(QQ)
    assert affine.relative_dimension() == 2
    assert affine.scheme_base_ring() is QQ
    assert tuple(affine.coordinate_ring().variable_names()) == ("x", "y")


def test_archived_projective_space_constructor_is_owned_by_projective_spaces() -> None:
    projective = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))

    assert projective in ProjectiveSpaces(QQ)
    assert projective.relative_dimension() == 2
    assert projective.scheme_base_ring() is QQ
    assert tuple(projective.coordinate_ring().variable_names()) == ("x", "y", "z")
