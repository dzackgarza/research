from dzack_research.preamble.all import ZZ, Lattices, finite_ordered_set


def test_every_A2_graph_automorphism_lifts_through_gap_to_a_lattice_isometry() -> None:
    lattice = Lattices(ZZ)("A2")
    configuration = lattice.vector_configuration(lattice.module_generators())
    automorphisms = configuration.configuration_automorphism_group()

    lifted = finite_ordered_set([
        configuration.configuration_isometry_from_automorphism(automorphism)
        for automorphism in automorphisms
    ])

    assert lifted.cardinality() == 2
    assert all(isometry.parent() is configuration.O() for isometry in lifted)


def test_full_framing_graph_automorphisms_lift_to_the_ambient_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("D4")
    configuration = lattice.vector_configuration(lattice.module_generators())
    automorphisms = configuration.configuration_automorphism_group()

    lifted = finite_ordered_set([
        configuration.ambient_isometry_from_automorphism(automorphism)
        for automorphism in automorphisms
    ])

    assert lifted.cardinality() == 6
    assert all(isometry.parent() is lattice.O() for isometry in lifted)
