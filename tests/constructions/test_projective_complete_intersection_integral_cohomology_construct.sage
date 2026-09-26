r"""A smooth projective complete intersection exposes its integral singular cohomology directly."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_fermat_quartic_direct_degree_two_cohomology_matches_integral_topology() -> None:
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    quartic = space.closed_subscheme(x0**4 + x1**4 + x2**4 + x3**4)

    assert quartic.integral_singular_cohomology(2) == quartic.integral_topology().integral_cohomology(2)
