from dzack_research.preamble.all import ZZ, Lattices, Sets


def test_vector_locus_distinguishes_norm_and_primitivity() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()

    isotropic = lattice.vector_locus(norm=0)
    primitive_isotropic = lattice.vector_locus(norm=0, primitive=True)

    assert e in isotropic
    assert 2 * e in isotropic
    assert e in primitive_isotropic
    assert 2 * e not in primitive_isotropic
    assert e + f not in isotropic


def test_isotropic_sublattice_locus_does_not_identify_a_vector_with_its_line() -> None:
    lattice = Lattices(ZZ)("U")
    e, _f = lattice.module_generators()
    line = lattice.sublattice_from((2 * e,))
    locus = lattice.isotropic_sublattice_locus(rank=1)

    assert locus in Sets()
    assert line in locus
    assert e not in locus
    assert not line.is_primitive()


def test_isotropic_flag_locus_accepts_arbitrary_prescribed_nested_ranks() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("U")
    e1 = lattice.module_generator(0)
    e2 = lattice.module_generator(2)
    line = lattice.primitive_sublattice_from((e1,))
    plane = lattice.primitive_sublattice_from((e1, e2))

    locus = lattice.isotropic_flag_locus(ranks=(1, 2))

    assert locus in Sets()
    assert (line, plane) in locus
    assert (plane, line) not in locus
    assert line not in locus


def test_existing_complete_isotropic_flag_is_a_member_of_its_rank_locus() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("U")
    flag = lattice.isotropic_flag(
        lattice.module_generator(0),
        lattice.module_generator(2),
    )

    assert flag in lattice.isotropic_flag_locus(ranks=(1, 2))
