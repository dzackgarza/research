r"""The Enriques lattice as a unimodular summand of the K3 lattice.

The archive records the standard decomposition
``L_K3 ~= E10 + (U + U + E8(-1))``.  Both summands are even unimodular, so
there is no finite glue ambiguity: their orthogonal sum already has the K3
lattice's signature and isometry class.
"""

from dzack_research.preamble.all import Lattices


def test_enriques_lattice_and_its_unimodular_complement_sum_to_k3_lattice() -> None:
    enriques = Lattices.E10
    complement = Lattices.U + Lattices.U + Lattices.E8

    assert enriques.signature_pair() == (1, 9)
    assert complement.signature_pair() == (2, 10)
    assert enriques.is_even() and enriques.is_unimodular()
    assert complement.is_even() and complement.is_unimodular()
    assert tuple(enriques.discriminant_group().invariants()) == ()
    assert tuple(complement.discriminant_group().invariants()) == ()
    assert (enriques + complement).is_isometric(Lattices.LK3) is True
