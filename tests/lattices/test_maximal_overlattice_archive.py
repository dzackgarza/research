r"""Archive reconciliation for a selected maximal overlattice."""

from dzack_research.preamble.all import Lattices


def test_a1_four_maximal_overlattice_is_the_index_two_d4_genus_extension() -> None:
    source = Lattices.A1 ** 4
    inclusion = source.maximal_overlattice()
    target = inclusion.codomain()

    assert inclusion.domain() is source
    assert inclusion.index() == 2
    assert target.is_even()
    assert target.genus() == Lattices.D4.genus()


