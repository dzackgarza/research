from dzack_research.preamble.all import ZZ, Lattices


def _hyperbolic_swap():
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    swap = lattice.O()((f, e))
    return lattice, swap


def test_lattice_isometry_owns_its_primitive_extension_and_centralizer() -> None:
    lattice, swap = _hyperbolic_swap()
    extension = swap.primitive_extension()

    assert extension.isometry is swap
    assert extension.lattice is lattice
    assert extension.invariant is swap.invariant_lattice()
    assert extension.orthogonal_complement is swap.formed_coinvariants()
    assert swap in swap.centralizer_group()
    assert lattice.O().one() in swap.centralizer_group()


def test_involution_cyclotomic_summands_are_the_owned_plus_and_minus_lattices() -> None:
    _lattice, swap = _hyperbolic_swap()
    plus = swap.cyclotomic_summand(1)
    minus = swap.cyclotomic_summand(2)

    assert plus.module_rank() == 1
    assert minus.module_rank() == 1
    assert plus.is_primitive()
    assert minus.is_primitive()
    assert plus.ambient_lattice() is swap.domain()
    assert minus.ambient_lattice() is swap.domain()


def test_involution_primitive_extension_retains_the_glue_criterion() -> None:
    _lattice, swap = _hyperbolic_swap()
    extension = swap.primitive_extension()
    invariant_part = extension.invariant_restriction(swap)
    coinvariant_part = extension.coinvariant_restriction(swap)

    assert extension.pair_preserves_glue_graph(invariant_part, coinvariant_part)
    assert extension.centralizer_element(invariant_part, coinvariant_part) == swap
