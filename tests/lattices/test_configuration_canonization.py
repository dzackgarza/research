from dzack_research.preamble.all import (
    Set,
    ZZ,
    Lattices,
    finite_ordered_set,
    vector_configuration,
)


def test_pairing_configuration_exposes_canonical_gram_and_position_certificate() -> None:
    lattice = Lattices(ZZ)("A3")
    configuration = vector_configuration(lattice, lattice.module_generators())

    canonical = configuration.canonical_pairing_matrix(algorithm="sage")
    certificate = configuration.canonical_position_map(algorithm="sage")

    assert canonical.nrows() == canonical.ncols() == 3
    assert certificate.index_set() is configuration.configuration_positions()
    assert Set(certificate) == Set(certificate.index_set())


def test_canonical_pairing_matrix_is_invariant_under_reversing_an_A3_framing() -> None:
    lattice = Lattices(ZZ)("A3")
    basis = lattice.module_generators()
    forward = vector_configuration(lattice, basis)
    reversed_configuration = vector_configuration(
        lattice,
        finite_ordered_set((basis[2], basis[1], basis[0])),
    )

    assert forward.canonical_pairing_matrix(algorithm="sage") == (
        reversed_configuration.canonical_pairing_matrix(algorithm="sage")
    )


def test_automorphism_group_accepts_the_same_graph_backend_selector() -> None:
    lattice = Lattices(ZZ)("D4")
    configuration = vector_configuration(lattice, lattice.module_generators())

    assert configuration.configuration_automorphism_group(algorithm="sage").order() == 6
