r"""Projective n-space has canonical bundle O(-n-1)."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_projective_plane_canonical_and_anticanonical_bundles() -> None:
    plane = ProjectiveSpaces(QQ)(2)

    assert plane.canonical_bundle() == plane.canonical_line_bundle() == plane.O(-3)
    assert plane.anticanonical_bundle() == plane.anticanonical_line_bundle() == plane.O(3)
