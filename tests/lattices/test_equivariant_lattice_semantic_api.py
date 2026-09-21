from dzack_research.preamble.all import ZZ, Lattices


def _swap_on_hyperbolic_plane():
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    swap = lattice.O()((f, e))
    return lattice, e, f, swap


def test_lattice_with_isometry_owns_the_equipped_object_and_centralizer() -> None:
    lattice, _e, _f, swap = _swap_on_hyperbolic_plane()
    equipped = lattice.with_isometry(swap)
    centralizer = equipped.centralizer_group()
    inclusion = centralizer.inclusion()

    assert equipped.lattice() is lattice
    assert equipped.isometry() == swap
    assert swap in centralizer
    assert centralizer.centralizing_element() == swap
    assert inclusion.domain() is centralizer
    assert inclusion.codomain() is lattice.O()
    assert inclusion(swap) == swap
    assert equipped.primitive_extension().isometry == swap


def test_equivariant_sublattice_carries_the_restricted_isometry() -> None:
    lattice, e, f, swap = _swap_on_hyperbolic_plane()
    equipped = lattice.with_isometry(swap)
    diagonal = lattice.primitive_sublattice_from((e + f,))

    restricted = equipped.equivariant_sublattice(diagonal)

    assert restricted.lattice() is diagonal
    assert restricted.isometry() == diagonal.O().one()


def test_nonstable_sublattice_is_not_laundered_into_an_equivariant_object() -> None:
    lattice, e, _f, swap = _swap_on_hyperbolic_plane()
    equipped = lattice.with_isometry(swap)
    line = lattice.primitive_sublattice_from((e,))

    try:
        equipped.equivariant_sublattice(line)
    except ValueError:
        pass
    else:
        raise AssertionError("the coordinate line is moved by the swap")


def test_identity_equivariant_isometry_is_the_live_orthogonal_identity() -> None:
    lattice, _e, _f, swap = _swap_on_hyperbolic_plane()
    equipped = lattice.with_isometry(swap)

    witness = equipped.equivariant_isometry_to(equipped)

    assert witness == lattice.O().one()


def test_definite_equivariant_isometry_search_is_exhaustive() -> None:
    lattice = Lattices(ZZ)("A1")
    identity = lattice.with_isometry(lattice.O().one())
    negation = lattice.O()((-lattice.module_generator(0),))
    equipped_negation = lattice.with_isometry(negation)

    assert identity.equivariant_isometry_to(equipped_negation) is None
