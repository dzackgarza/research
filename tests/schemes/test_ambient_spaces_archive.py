"""Archive reconciliation for the ambient affine/projective space constructors."""

from dzack_research.preamble.all import (
    AffineSpace,
    AffineSpaces,
    ProjectiveSpace,
    ProjectiveSpaces,
    QQ,
)


def test_archived_affine_space_constructor_is_the_live_owned_constructor() -> None:
    affine = AffineSpace(2, QQ, names=("x", "y"))

    assert affine in AffineSpaces(QQ)
    assert affine.relative_dimension() == 2
    assert affine.scheme_base_ring() is QQ
    assert tuple(affine.coordinate_ring().variable_names()) == ("x", "y")


def test_archived_projective_space_constructor_is_the_live_owned_constructor() -> None:
    projective = ProjectiveSpace(2, QQ, names=("x", "y", "z"))

    assert projective in ProjectiveSpaces(QQ)
    assert projective.relative_dimension() == 2
    assert projective.scheme_base_ring() is QQ
    assert tuple(projective.coordinate_ring().variable_names()) == ("x", "y", "z")
