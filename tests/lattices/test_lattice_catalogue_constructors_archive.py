r"""Archive specimens for the standard integral lattice catalogue constructors.

These are the source-backed constructors from
``archives/preamble/categories/modules/framed/formed/lattices.sage`` that are
independent of the still-unresolved Leech-lattice realization.  Each result is
built through the live owned lattice category and its orthogonal sums.
"""

from dzack_research.preamble.all import Lattices, ZZ

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/lattices.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattices.py",
    "owner_overrides": {
        "Lattices.namespace": "src/dzack_research/preamble/all.py",
        "Lattices.install": "src/dzack_research/preamble/all.py",
    },
    "disposition": "reconciled-live-owner",
}


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


def test_leech_lattice_uses_the_rootless_even_unimodular_archive_contract() -> None:
    leech = Lattices.leech_lattice()

    assert leech.module_rank() == 24
    assert leech.signature_pair() == (0, 24)
    assert leech.is_even()
    assert abs(leech.gram_matrix().determinant()) == 1
    assert leech.roots().cardinality() == 0


def test_non_simply_laced_root_lattices_use_the_integral_cartan_symmetrizer() -> None:
    f4 = Lattices.root_lattice("F", 4)
    g2 = Lattices.root_lattice("G", 2)

    assert f4.module_rank() == 4
    assert f4.gram_matrix().determinant() == ZZ(4)
    assert tuple(abs(f4.b(root, root)) for root in f4.simple_roots()) == (4, 4, 2, 2)

    assert g2.module_rank() == 2
    assert g2.gram_matrix().determinant() == ZZ(3)
    assert tuple(abs(g2.b(root, root)) for root in g2.simple_roots()) == (6, 2)
