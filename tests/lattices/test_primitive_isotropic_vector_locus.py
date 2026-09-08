from dzack_research.preamble.all import NamedLattices, primitive_isotropic_vectors


def test_lattice_owns_the_same_primitive_isotropic_membership_condition() -> None:
    lattice = NamedLattices.E10
    locus = lattice.primitive_isotropic_vectors()
    standalone = primitive_isotropic_vectors(lattice)
    isotropic = lattice.module_generator(0)

    assert locus.lattice() is lattice
    assert locus.universe() is lattice
    assert isotropic in locus
    assert isotropic in standalone
    assert lattice.zero() not in locus
    assert 2 * isotropic not in locus


def test_primitive_isotropic_orbit_decomposition_retains_representative_stabilizer_and_transporter() -> None:
    lattice = NamedLattices.E10
    group = lattice.O()
    locus = lattice.primitive_isotropic_vectors()
    decomposition = group.orbit_decomposition(locus)

    assert decomposition.group() is group
    assert decomposition.locus() is locus
    assert decomposition.representatives().cardinality() == 1

    representative = decomposition.representatives()[0]
    assert representative in locus
    assert decomposition.stabilizer(representative).one() == group.one()
    transporter = decomposition.transporter(representative, representative)
    assert transporter(representative) == representative
