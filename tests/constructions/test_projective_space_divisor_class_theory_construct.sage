r"""For projective space over a field, Picard and divisor class groups agree."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_projective_plane_picard_to_class_group_is_an_isomorphism() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    comparison = plane.divisor_class_theory()

    assert comparison.domain() is plane.picard_group()
    assert comparison.codomain() is plane.class_group()
    assert comparison.is_isomorphism()
