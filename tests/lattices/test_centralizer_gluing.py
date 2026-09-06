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
    NamedLattices,
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
