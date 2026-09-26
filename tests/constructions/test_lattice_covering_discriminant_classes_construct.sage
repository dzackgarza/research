r"""The unimodular hyperbolic plane has one discriminant class covering root square."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_hyperbolic_plane_root_square_has_only_zero_covering_class() -> None:
    lattice = NamedLattices.U
    classes = lattice.covering_discriminant_classes(-2)

    assert classes.cardinality() == cardinal(1)
    assert lattice.discriminant_group().zero() in classes
