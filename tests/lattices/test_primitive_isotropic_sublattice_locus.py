from dzack_research.preamble.all import NamedLattices


def test_rank_one_primitive_isotropic_locus_distinguishes_vectors_from_sublattices() -> None:
    lattice = NamedLattices.E10
    vector = lattice.module_generator(0)
    line = lattice.primitive_sublattice_from((vector,))
    locus = lattice.primitive_isotropic_sublattices(rank=1)

    assert locus.lattice() is lattice
    assert locus.rank() == 1
    assert line in locus
    assert vector not in locus
    assert line.inclusion().codomain() is lattice


def test_isotropic_sublattice_orbit_decomposition_uses_cusp_stabilizers_and_transporters() -> None:
    lattice = NamedLattices.E10
    group = lattice.O()
    locus = lattice.primitive_isotropic_sublattices(rank=1)
    decomposition = group.orbit_decomposition(locus)

    assert decomposition.group() is group
    assert decomposition.locus() is locus
    assert decomposition.representatives().cardinality() == 1

    representative = decomposition.representatives()[0]
    assert representative in locus
    assert decomposition.stabilizer(representative).one() == group.one()
    transporter = decomposition.transporter(representative, representative)
    image = transporter(representative.inclusion()(representative.module_generator(0)))
    assert image.parent() is lattice
