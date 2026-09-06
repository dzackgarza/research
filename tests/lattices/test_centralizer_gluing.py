r"""The primitive extension cut out by a lattice isometry, and its centralizer data.

The cited specimen is the Enriques involution on the K3 lattice: its invariant
lattice is ``U(2) + E8(-2)``, two-elementary of type ``(10, 10, 0)``, and its
coinvariant lattice is ``T_En`` of rank twelve (Barth--Peters--Van de Ven,
*Compact Complex Surfaces*, ch. VIII; Nikulin's classification of
two-elementary involutions).  Both discriminant groups then have order
``2^10``, and since the K3 lattice is unimodular the glue subgroup is all of
``A_{S_En}``, so the orthogonal sum has index ``2^10`` in the K3 lattice.

The odd specimen is the cyclic permutation of the coordinates of ``I_3``.  Its
invariant lattice is the diagonal, of square three, and its coinvariant
lattice is the rank-two root lattice orthogonal to that diagonal.  ``I_3`` is
odd while that coinvariant summand is even, so the glue of this extension is
an anti-isometry of the ``QQ/ZZ``-valued bilinear discriminant forms, and the
same criterion and the same assembly must answer there as in the even case.
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

    # U is even, so this extension is glued by its quadratic discriminant
    # forms and the criterion below is read there.
    assert lattice.is_even()
    assert extension.glue().is_quadratic()

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


def test_the_a2_centralizer_separates_two_roots_that_o_a2_identifies() -> None:
    lattice, involution = _a2_diagram_involution()
    centralizer = isometry_primitive_extension(involution).centralizer_group()
    first, second = tuple(lattice.module_generators())
    invariant_root = first + second

    # a1, a2 and a1 + a2 are roots, and O(A2) has one orbit of square -2, so
    # the full group carries any of them to any other.
    assert first.q() == -2
    assert second.q() == -2
    assert invariant_root.q() == -2
    assert lattice.O().vectors_are_equivalent(first, invariant_root)

    # The centralizer of the diagram involution is generated by that
    # involution and by -1, so its orbit of a1 is {a1, a2, -a1, -a2} and its
    # orbit of a1 + a2 is {a1 + a2, -(a1 + a2)}: it separates the two halves
    # of the single root orbit.
    assert centralizer.vectors_are_equivalent(first, second)
    assert centralizer.vectors_are_equivalent(first, -first)
    assert centralizer.vectors_are_equivalent(invariant_root, -invariant_root)
    assert not centralizer.vectors_are_equivalent(first, invariant_root)
    assert not centralizer.vectors_are_equivalent(second, invariant_root)


def _cubic_cyclic_permutation():
    r"""Return ``I_3`` with the cyclic permutation of its three coordinates.

    The permutation ``e1 -> e2 -> e3 -> e1`` is an isometry of ``I_3`` of
    order three.  It fixes exactly the diagonal ``ZZ(e1 + e2 + e3)``, of
    square three, and its coinvariant lattice is the rank-two root lattice
    orthogonal to that diagonal, whose Gram matrix is ``[[2,-1],[-1,2]]``.
    Both discriminant groups are cyclic of order three, and the orthogonal
    sum of the two summands has index three in ``I_3``.

    ``I_3`` is odd and its coinvariant summand is even, so this is the
    specimen on which the glue and the pair criterion have to be read on the
    ``QQ/ZZ``-valued bilinear discriminant forms although one summand
    supports a quadratic one.
    """
    lattice = Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    labels = tuple(lattice.module_generating_set())
    first, second, third = tuple(lattice.module_generators())
    return lattice, lattice.Aut()(
        {labels[0]: second, labels[1]: third, labels[2]: first}
    )


def test_the_cubic_cyclic_permutation_glues_an_odd_lattice_bilinearly() -> None:
    lattice, rotation = _cubic_cyclic_permutation()
    extension = isometry_primitive_extension(rotation)

    assert not lattice.is_even()
    assert extension.invariant.rank() == 1
    assert extension.coinvariant.rank() == 2
    assert extension.coinvariant.inclusion().domain().is_even()

    assert not extension.glue().is_quadratic()
    assert extension.invariant.discriminant_group().cardinality() == 3
    assert extension.coinvariant.discriminant_group().cardinality() == 3
    assert extension.index() == 3
    assert extension.gluing_subgroup().cardinality() == 3


def test_a_compatible_pair_reassembles_the_cubic_cyclic_permutation() -> None:
    lattice, rotation = _cubic_cyclic_permutation()
    extension = isometry_primitive_extension(rotation)
    invariant_summand = extension.invariant.inclusion().domain()

    # The rotation is the identity on the diagonal and lies in the Weyl group
    # of the coinvariant root lattice, which acts trivially on its
    # discriminant group; the pair of its two restrictions therefore acts as
    # the identity on the glue graph.
    invariant_part = extension.invariant_restriction(rotation)
    coinvariant_part = extension.coinvariant_restriction(rotation)
    assert invariant_part == invariant_summand.Aut().one()
    assert extension.pair_preserves_glue_graph(invariant_part, coinvariant_part)

    assembled = extension.centralizer_element(invariant_part, coinvariant_part)
    assert assembled.parent() is lattice.Aut()
    assert assembled in extension.centralizer_group()
    assert all(
        assembled(generator) == rotation(generator)
        for generator in lattice.module_generators()
    )


def test_the_negation_pair_reassembles_minus_one_on_the_cubic_lattice() -> None:
    lattice, rotation = _cubic_cyclic_permutation()
    extension = isometry_primitive_extension(rotation)
    invariant_summand = extension.invariant.inclusion().domain()
    coinvariant_summand = extension.coinvariant.inclusion().domain()

    # The graph of gamma is a subgroup of the sum of the two discriminant
    # forms, so negation on both factors permutes it.  The assembled isometry
    # is -1 on I_3, reached by clearing the denominator three of the
    # orthogonal sum.
    invariant_part = _negation(invariant_summand)
    coinvariant_part = _negation(coinvariant_summand)
    assert extension.pair_preserves_glue_graph(invariant_part, coinvariant_part)

    assembled = extension.centralizer_element(invariant_part, coinvariant_part)
    assert assembled.parent() is lattice.Aut()
    assert assembled in extension.centralizer_group()
    assert all(
        assembled(generator) == -generator
        for generator in lattice.module_generators()
    )
    assert extension.invariant_restriction(assembled) == invariant_part
    assert extension.coinvariant_restriction(assembled) == coinvariant_part


def test_negating_one_summand_of_the_cubic_split_breaks_the_glue_graph() -> None:
    _lattice, rotation = _cubic_cyclic_permutation()
    extension = isometry_primitive_extension(rotation)
    invariant_summand = extension.invariant.inclusion().domain()
    coinvariant_summand = extension.coinvariant.inclusion().domain()

    # gamma is injective on a group of order three, so ``(x, -gamma x)`` lies
    # on the graph only where ``gamma x = -gamma x``, that is only at zero.
    # A pair that is the identity on one summand and negation on the other is
    # therefore an isometry of the orthogonal sum that does not extend to
    # I_3, and Nikulin's criterion says so.
    assert not extension.pair_preserves_glue_graph(
        invariant_summand.Aut().one(), _negation(coinvariant_summand)
    )
    assert not extension.pair_preserves_glue_graph(
        _negation(invariant_summand), coinvariant_summand.Aut().one()
    )
