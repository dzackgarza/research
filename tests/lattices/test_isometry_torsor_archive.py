from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_isometry_torsor_transporter_recovers_the_acting_element() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)("A2")
    homset = lattice.Isom(lattice)
    witness = homset.an_element()
    reflection = lattice.reflection(lattice.basis_vector(0))
    moved = reflection * witness

    transporter = homset.transporter(witness, moved)

    assert transporter == reflection
    assert transporter * witness == moved
