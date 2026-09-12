r"""Archive specimens for the standard integral lattice catalogue constructors.

These are the source-backed constructors from
``archives/preamble/categories/modules/framed/formed/lattices.sage`` that are
independent of the still-unresolved Leech-lattice realization.  Each result is
built through the live owned lattice category and its orthogonal sums.
"""

from dzack_research.preamble.all import Lattices, ZZ


def test_odd_and_even_unimodular_signature_constructors_keep_their_forms() -> None:
    odd = Lattices.IPQ(2, 1)
    even = Lattices.IIPQ(1, 9)

    assert odd.signature_pair() == (2, 1)
    assert abs(odd.gram_matrix().determinant()) == 1
    assert not odd.is_even()

    assert even.signature_pair() == (1, 9)
    assert abs(even.gram_matrix().determinant()) == 1
    assert even.is_even()


def test_polarized_k3_complement_and_rank_one_constructor_have_archived_grams() -> None:
    line = Lattices.rank_one_negative(3)
    complement = Lattices.LK3_2d(2)

    assert line.gram_matrix()[0, 0] == ZZ(-6)
    assert complement.module_rank() == 21
    assert complement.signature_pair() == (2, 19)
    assert abs(complement.gram_matrix().determinant()) == 4


def test_hyperkaehler_bbf_lattices_have_the_standard_ranks_and_signatures() -> None:
    expected = {
        ("K3", 2): (23, (3, 20)),
        ("Kum", 2): (7, (3, 4)),
        ("OG6", 2): (8, (3, 5)),
        ("OG10", 2): (24, (3, 21)),
    }

    for (deformation_type, n), (rank, signature) in expected.items():
        lattice = Lattices.hyperkaehler_lattice(deformation_type, n)
        assert lattice.module_rank() == rank
        assert lattice.signature_pair() == signature
        assert lattice.base_ring() is ZZ
