r"""Archived finite-isometry structure descriptions at the live group owner."""


from dzack_research.preamble.all import ZZ, Lattices


def test_rank_one_root_lattice_has_cyclic_order_two_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("A1")

    assert lattice.O().structure_description() == "C2"
    assert lattice.O().cardinality() == 2


