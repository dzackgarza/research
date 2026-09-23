r"""Archived finite-isometry structure descriptions at the live group owner."""

import pytest

from dzack_research.preamble.all import ZZ, Lattices


def test_rank_one_root_lattice_has_cyclic_order_two_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("A1")

    assert lattice.O().structure_description() == "C2"
    assert lattice.O().cardinality() == 2


def test_indefinite_orthogonal_group_does_not_claim_a_finite_gap_description() -> None:
    lattice = Lattices(ZZ)("U")

    with pytest.raises(AssertionError):
        lattice.O().structure_description()
