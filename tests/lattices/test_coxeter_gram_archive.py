r"""Archive reconciliation for Coxeter root-Gram classification invariants."""

from dzack_research.preamble.all import ZZ, CoxeterDiagrams, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/coxeter_tdd_specs/unit/test_gram_matrices.sage",
    "live_owner": "tests/lattices/test_coxeter_gram_archive.py",
    "owner_overrides": {
        "test_triangle_group_333_is_the_a2_schlafli_matrix": "tests/lattices/test_coxeter_literature.py",
        "test_square_group_is_the_dihedral_group_of_order_eight": "tests/lattices/test_coxeter_literature.py",
        "test_a_gram_matrix_must_be_symmetric": "tests/forms/test_constructor_obligations_archive.py",
        "test_an_integral_lattice_must_have_integral_gram_entries": "tests/forms/test_constructor_obligations_archive.py",
    },
    "disposition": "reconciled-live-owner",
}




def test_a2_root_lattice_has_archived_determinant_signature_and_discriminant() -> None:
    lattice = CoxeterDiagrams().from_cartan_type(["A", 2], rooted=True).root_lattice()
    signature = lattice.signature_pair()

    assert lattice.gram_matrix().determinant() == 3
    assert signature.first() == 0
    assert signature.second() == 2
    assert lattice.discriminant() == -3
    assert lattice.is_nondegenerate()


def test_a_series_root_gram_determinants_retain_the_alternating_sign() -> None:
    for rank, determinant in ((1, -2), (2, 3), (3, -4), (4, 5)):
        lattice = CoxeterDiagrams().from_cartan_type(["A", rank], rooted=True).root_lattice()
        signature = lattice.signature_pair()
        assert int(lattice.module_rank()) == rank
        assert lattice.gram_matrix().determinant() == determinant
        assert signature.first() == 0
        assert signature.second() == rank


def test_affine_a2_and_ultraparallel_edge_distinguish_radical_from_indefiniteness() -> None:
    affine_lattice = Lattices(ZZ)([[-2, 1, 1], [1, -2, 1], [1, 1, -2]])
    affine_diagram = CoxeterDiagrams().from_cartan_type(["A", 2, 1])
    affine_signature = affine_lattice.signature_pair()

    assert affine_lattice.gram_matrix().determinant() == 0
    assert affine_signature.first() == 0
    assert affine_signature.second() == 2
    assert affine_lattice.radical().module_rank() == 1
    assert affine_diagram.is_parabolic()
    assert not affine_diagram.is_elliptic()

    hyperbolic_lattice = Lattices(ZZ)([[-2, 3], [3, -2]])
    hyperbolic_diagram = CoxeterDiagrams().from_roots(hyperbolic_lattice.module_generators())
    hyperbolic_signature = hyperbolic_lattice.signature_pair()
    assert hyperbolic_lattice.gram_matrix().determinant() == -5
    assert hyperbolic_signature.first() == 1
    assert hyperbolic_signature.second() == 1
    assert hyperbolic_lattice.is_nondegenerate()
    assert not hyperbolic_diagram.is_elliptic()
    assert not hyperbolic_diagram.is_parabolic()
