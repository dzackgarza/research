r"""The blowup of the projective plane at one point is a degree-eight del Pezzo surface."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_one_point_blowup_has_anticanonical_bundle_and_del_pezzo_degree_eight() -> None:
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    blowup = ProjectivePointBlowups(QQ)(plane.point_morphism((1, 1, 1)))

    assert blowup.canonical_bundle() == blowup.canonical_line_bundle()
    assert blowup.anticanonical_bundle() == blowup.anticanonical_line_bundle()
    assert blowup.is_del_pezzo()
    assert blowup.del_pezzo_degree() == 8
