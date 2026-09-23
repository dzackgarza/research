from dzack_research.preamble.all import ZZ, Lattices


def test_reordering_the_a3_simple_roots_changes_the_gram_matrix_but_not_its_canonical_form() -> None:
    r"""The canonical pairing matrix depends only on the configuration up to relabelling.

    Framed as ``(a2, a1, a3)`` the ``A3`` simple roots have a Gram matrix in
    which the middle root comes first, different from the chain order
    ``(a1, a2, a3)``; the two are conjugate by a permutation matrix, so their
    canonical forms agree.
    """
    lattice = Lattices(ZZ)("A3")
    first, second, third = lattice.module_generators()
    chain = lattice.vector_configuration((first, second, third))
    middle_first = lattice.vector_configuration((second, first, third))

    assert chain.pairing_matrix() != middle_first.pairing_matrix()
    assert chain.canonical_pairing_matrix(algorithm="sage") == (
        middle_first.canonical_pairing_matrix(algorithm="sage")
    )


def test_automorphism_group_accepts_the_same_graph_backend_selector() -> None:
    lattice = Lattices(ZZ)("D4")
    configuration = lattice.vector_configuration(lattice.module_generators())

    assert configuration.configuration_automorphism_group(algorithm="sage").order() == 6
