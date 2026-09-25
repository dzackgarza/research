r"""Affine and projective planes over fields are surfaces."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_affine_and_projective_planes_are_surfaces(field) -> None:
    affine_plane = AffineSpaces(field)(2)
    projective_plane = ProjectiveSpaces(field)(2)

    assert affine_plane in Surfaces(field)
    assert projective_plane in Surfaces(field)
    assert affine_plane.dimension() == 2
    assert projective_plane.dimension() == 2
