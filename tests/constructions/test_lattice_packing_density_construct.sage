r"""The integer lattice tiles the line by touching unit intervals."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_integer_line_has_packing_density_one() -> None:
    lattice = Lattices(ZZ)(ZZ^1)

    assert lattice.packing_density() == 1
