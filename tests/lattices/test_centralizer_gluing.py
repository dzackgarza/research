r"""The primitive extension cut out by an involution, and its centralizer data.

The cited specimen is the Enriques involution on the K3 lattice: its invariant
lattice is ``U(2) + E8(-2)``, two-elementary of type ``(10, 10, 0)``, and its
coinvariant lattice is ``T_En`` of rank twelve (Barth--Peters--Van de Ven,
*Compact Complex Surfaces*, ch. VIII; Nikulin's classification of
two-elementary involutions).  Both discriminant groups then have order
``2^10``, and since the K3 lattice is unimodular the glue subgroup is all of
``A_{S_En}``, so the orthogonal sum has index ``2^10`` in the K3 lattice.
"""

from dzack_research.preamble.all import (
    Involutions,
    Lattices,
    NamedLattices,
    ZZ,
    cyclotomic_summand,
    isometry_primitive_extension,
)


def _hyperbolic_swap():
    lattice = NamedLattices.U
    first, second = lattice.module_generators().unrank(0), lattice.module_generators().unrank(1)
    return lattice, lattice.Aut()({0: second, 1: first})


def test_the_swap_of_the_hyperbolic_plane_glues_two_rank_one_lattices() -> None:
    lattice, swap = _hyperbolic_swap()
    first, second = lattice.module_generators().unrank(0), lattice.module_generators().unrank(1)
    assert swap * swap == lattice.Aut().one()

    extension = isometry_primitive_extension(swap)
    assert extension.lattice is lattice
    assert extension.invariant.rank() == 1
    assert extension.coinvariant.rank() == 1
    assert extension.acts_as_negation_on_coinvariants()

    invariant_vector = extension.invariant.embedded_module_generators()[
        extension.invariant.module_generating_set().unrank(0)
    ]
    coinvariant_vector = extension.coinvariant.embedded_module_generators()[
        extension.coinvariant.module_generating_set().unrank(0)
    ]
    assert invariant_vector.q() == 2
    assert coinvariant_vector.q() == -2
    assert lattice.b(invariant_vector, coinvariant_vector) == 0
    assert swap(invariant_vector) == invariant_vector
    assert swap(coinvariant_vector) == -coinvariant_vector

    # A_{Z(e+f)} and A_{Z(e-f)} both have order two and U is unimodular, so
    # the glue subgroup is the whole of the first and the index is two.
    assert extension.index() == 2
    assert extension.gluing_subgroup().cardinality() == 2
    assert extension.glue().domain() is extension.gluing_subgroup()
    assert invariant_vector in (first + second, -(first + second))
    assert coinvariant_vector in (first - second, second - first)


def test_the_swap_restricts_to_plus_and_minus_one_on_its_summands() -> None:
    lattice, swap = _hyperbolic_swap()
    extension = isometry_primitive_extension(swap)

    assert swap in extension.centralizer_group()
    assert lattice.Aut().one() in extension.centralizer_group()

    invariant_summand = extension.invariant.inclusion().domain()
    coinvariant_summand = extension.coinvariant.inclusion().domain()
    invariant_part = extension.invariant_restriction(swap)
    coinvariant_part = extension.coinvariant_restriction(swap)

    assert invariant_part == invariant_summand.Aut().one()
    assert coinvariant_part != coinvariant_summand.Aut().one()
    assert all(
        coinvariant_part(generator) == -generator
        for generator in coinvariant_summand.module_generators()
    )


def test_the_first_two_cyclotomic_summands_split_an_involution() -> None:
    _lattice, swap = _hyperbolic_swap()

    fixed = cyclotomic_summand(swap, 1)
    negated = cyclotomic_summand(swap, 2)
    assert fixed.rank() == 1
    assert negated.rank() == 1
    assert fixed.is_primitive()
    assert negated.is_primitive()

    fixed_inclusion = fixed.inclusion()
    assert all(
        swap(fixed_inclusion(generator)) == fixed_inclusion(generator)
        for generator in fixed.module_generators()
    )
    negated_inclusion = negated.inclusion()
    assert all(
        swap(negated_inclusion(generator)) == -negated_inclusion(generator)
        for generator in negated.module_generators()
    )


def test_the_enriques_involution_glues_S_En_to_T_En_with_index_1024() -> None:
    involution = Involutions.I_En
    extension = isometry_primitive_extension(involution)

    assert extension.lattice is NamedLattices.LK3
    assert extension.invariant.rank() == 10
    assert extension.coinvariant.rank() == 12
    assert extension.acts_as_negation_on_coinvariants()
    assert extension.coinvariant.inclusion().domain().is_isometric(NamedLattices.TEn)

    assert extension.invariant.discriminant_group().cardinality() == 1024
    assert extension.coinvariant.discriminant_group().cardinality() == 1024
    assert extension.index() == 1024
    assert extension.gluing_subgroup().cardinality() == 1024


def test_the_enriques_cyclotomic_summands_are_the_two_eigen_sublattices() -> None:
    involution = Involutions.I_En

    assert cyclotomic_summand(involution, 1).rank() == 10
    assert cyclotomic_summand(involution, 2).rank() == 12
    assert cyclotomic_summand(involution, 3).rank() == 0


def _a2_diagram_involution():
    r"""Return ``A2`` with the involution swapping its two simple roots.

    The Gram matrix of ``A2`` is symmetric under that swap, so the swap is an
    isometry.  It fixes ``a1 + a2``, of square ``-2``, and negates
    ``a1 - a2``, of square ``-6``: the invariant and coinvariant lattices are
    both of rank one and their discriminant groups have orders two and six.
    """
    lattice = Lattices(ZZ)("A2")
    labels = tuple(lattice.module_generating_set())
    first, second = tuple(lattice.module_generators())
    return lattice, lattice.Aut()({labels[0]: second, labels[1]: first})


def _negation(summand):
    r"""Return ``-1`` in ``O(summand)``, an isometry of every lattice."""
    return summand.Aut()(
        tuple(-generator for generator in summand.module_generators())
    )


def test_a_compatible_pair_reassembles_the_swap_of_the_hyperbolic_plane() -> None:
    lattice, swap = _hyperbolic_swap()
    extension = isometry_primitive_extension(swap)

    invariant_part = extension.invariant_restriction(swap)
    coinvariant_part = extension.coinvariant_restriction(swap)
    assert extension.pair_preserves_glue_graph(invariant_part, coinvariant_part)

    assembled = extension.centralizer_element(invariant_part, coinvariant_part)
    assert assembled.parent() is lattice.Aut()
    assert assembled == swap


def test_reassembly_inverts_restriction_on_the_four_pairs_over_the_hyperbolic_plane() -> None:
    lattice, swap = _hyperbolic_swap()
    extension = isometry_primitive_extension(swap)
    invariant_summand = extension.invariant.inclusion().domain()
    coinvariant_summand = extension.coinvariant.inclusion().domain()

    # Both summands have rank one, so each orthogonal group is {1,-1} and
    # there are four pairs.  A_{Z(e+f)} has order two and so has no
    # automorphism but the identity, so every pair preserves the glue graph:
    # the four assembled isometries are the whole of O(U), which is the
    # centralizer of the swap because O(U) is abelian.
    pairs = tuple(
        (invariant_part, coinvariant_part)
        for invariant_part in (
            invariant_summand.Aut().one(),
            _negation(invariant_summand),
        )
        for coinvariant_part in (
            coinvariant_summand.Aut().one(),
            _negation(coinvariant_summand),
        )
    )
    assert all(
        extension.pair_preserves_glue_graph(invariant_part, coinvariant_part)
        for invariant_part, coinvariant_part in pairs
    )
    assembled = tuple(
        extension.centralizer_element(invariant_part, coinvariant_part)
        for invariant_part, coinvariant_part in pairs
    )

    for pair, element in zip(pairs, assembled, strict=True):
        invariant_part, coinvariant_part = pair
        assert element in extension.centralizer_group()
        assert extension.invariant_restriction(element) == invariant_part
        assert extension.coinvariant_restriction(element) == coinvariant_part

    identity, swap_again, _negated_swap, negation = assembled
    assert identity == lattice.Aut().one()
    assert swap_again == swap
    assert all(
        negation(generator) == -generator
        for generator in lattice.module_generators()
    )


def test_the_a2_diagram_involution_reassembles_across_a_nontrivial_glue() -> None:
    lattice, involution = _a2_diagram_involution()
    extension = isometry_primitive_extension(involution)

    assert extension.invariant.rank() == 1
    assert extension.coinvariant.rank() == 1
    assert extension.invariant.discriminant_group().cardinality() == 2
    assert extension.coinvariant.discriminant_group().cardinality() == 6
    # A_{Z(a1-a2)} is cyclic of order six, on which negation acts
    # non-trivially; the glue subgroup is its subgroup of order two, and the
    # index of the orthogonal sum is that order.
    assert extension.index() == 2
    assert extension.gluing_subgroup().cardinality() == 2

    invariant_part = extension.invariant_restriction(involution)
    coinvariant_part = extension.coinvariant_restriction(involution)
    assert extension.pair_preserves_glue_graph(invariant_part, coinvariant_part)
    assert (
        extension.centralizer_element(invariant_part, coinvariant_part)
        == involution
    )


def test_the_a2_centralizer_splits_the_single_root_orbit_in_two() -> None:
    lattice, involution = _a2_diagram_involution()
    extension = isometry_primitive_extension(involution)

    roots = lattice.vectors_of_square(-2)
    assert len(roots) == 6
    assert len(lattice.O().vector_orbit_representatives(-2)) == 1

    # The centralizer of the diagram involution in O(A2) is generated by that
    # involution and by -1, so it has order four: the orbit of a1 is
    # {a1, a2, -a1, -a2} and the orbit of a1 + a2 is {a1 + a2, -(a1 + a2)}.
    representatives = extension.equivariant_vector_orbit_representatives(-2)
    assert len(representatives) == 2
    assert all(representative in roots for representative in representatives)
    assert len(
        tuple(
            representative
            for representative in representatives
            if involution(representative) == representative
        )
    ) == 1
