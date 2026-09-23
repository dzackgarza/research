from dzack_research.preamble.all import (
    ZZ,
    Lattices,
    finite_ordered_set,
)




def test_canonical_pairing_matrix_is_invariant_under_reversing_an_A3_framing() -> None:
    lattice = Lattices(ZZ)("A3")
    basis = lattice.module_generators()
    forward = lattice.vector_configuration(basis)
    reversed_configuration = lattice.vector_configuration(
        finite_ordered_set((basis[2], basis[1], basis[0]))
    )

    assert forward.canonical_pairing_matrix(algorithm="sage") == (
        reversed_configuration.canonical_pairing_matrix(algorithm="sage")
    )


def test_automorphism_group_accepts_the_same_graph_backend_selector() -> None:
    lattice = Lattices(ZZ)("D4")
    configuration = lattice.vector_configuration(lattice.module_generators())

    assert configuration.configuration_automorphism_group(algorithm="sage").order() == 6
