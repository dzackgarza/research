from dzack_research.preamble.all import NamedLattices, Sets


def test_lattice_owns_the_same_primitive_isotropic_membership_condition() -> None:
    lattice = NamedLattices.E10
    locus = lattice.primitive_isotropic_vectors()
    repeated = lattice.primitive_isotropic_vectors()
    isotropic = lattice.basis_vector(0)

    assert locus in Sets()
    assert locus.universe() is lattice
    assert locus.inclusion().codomain() is lattice
    assert isotropic in locus
    assert repeated is locus
    assert isotropic in repeated
    assert lattice.zero() not in locus
    assert 2 * isotropic not in locus


def test_primitive_isotropic_orbit_decomposition_retains_representative_stabilizer_and_transporter() -> None:
    lattice = NamedLattices.E10
    group = lattice.O()
    locus = lattice.primitive_isotropic_vectors()
    decomposition = group.orbit_decomposition(locus)

    assert decomposition in Sets()
    assert decomposition.group() is group
    assert decomposition.locus() is locus
    assert decomposition.representatives().cardinality() == 1

    representative = decomposition.representatives()[0]
    assert representative in locus
    assert decomposition.stabilizer(representative).one() == group.one()
    transporter = decomposition.transporter(representative, representative)
    assert transporter(representative) == representative
