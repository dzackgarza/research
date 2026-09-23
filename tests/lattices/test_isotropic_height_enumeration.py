from dzack_research.preamble.all import ZZ, HyperbolicLattices, Lattices


def test_height_one_isotropic_vectors_in_u_plus_a1_are_exactly_zero_and_four_rays() -> None:
    lattice = HyperbolicLattices(ZZ)(Lattices(ZZ)("U") + Lattices(ZZ)("A1"))
    e, f = lattice.basis_vector(0), lattice.basis_vector(1)
    timelike = e + f

    vectors = lattice.isotropic_elements_below_height(timelike, 1)

    assert vectors.cardinality() == 5
    for expected in (lattice.zero(), e, -e, f, -f):
        assert expected in vectors
    assert all(vector.q() == 0 for vector in vectors)
    assert all(abs(lattice.b(vector, timelike)) <= 1 for vector in vectors)


def test_a_nontimelike_height_vector_is_refused_before_shell_enumeration() -> None:
    lattice = HyperbolicLattices(ZZ)(Lattices(ZZ)("U") + Lattices(ZZ)("A1"))
    isotropic = lattice.basis_vector(0)

    try:
        lattice.isotropic_elements_below_height(isotropic, 1)
    except AssertionError:
        pass
    else:
        raise AssertionError("an isotropic controlling vector is not timelike")
