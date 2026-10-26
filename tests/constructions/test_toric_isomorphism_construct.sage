r"""A toric variety is isomorphic to itself."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_projective_plane_is_isomorphic_to_itself() -> None:
    plane = RationalPolyhedralFans(ZZ.free_module(2)).projective_space_fan().toric_variety(QQ)

    assert plane.is_isomorphic_to(plane)
