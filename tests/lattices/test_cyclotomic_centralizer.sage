r"""Cyclotomic decompositions of finite-order isometries and their gluing."""

from dzack_research.preamble.all import *


def cyclic_permutation_of_Z3():
    lattice = Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    labels = lattice.module_generating_set()
    first, second, third = lattice.module_generators()
    return lattice.O()({labels[0]: second, labels[1]: third, labels[2]: first})


def negation_of(lattice):
    return lattice.O()(
        {
            label: -lattice.module_generator(label)
            for label in lattice.module_generating_set()
        }
    )


def test_the_three_cycle_on_Z3_splits_into_Phi1_and_Phi3_parts_glued_with_index_three() -> None:
    r"""The 3-cycle fixes Z(1,1,1) (norm 3) and acts with order 3 on the
    sum-zero sublattice A2 (discriminant 3); their sum has index
    sqrt(3 * 3 / 1) = 3 in Z^3.  A reflection of A2 does not commute with an
    order-3 rotation of A2 (the dihedral group of order 6 is nonabelian)."""
    isometry = cyclic_permutation_of_Z3()
    decomposition = isometry.cyclotomic_decomposition(3)

    assert Set(decomposition.nonzero_divisors()) == Set((1, 3))
    assert decomposition.summand(1).module_rank() == 1
    assert decomposition.summand(3).module_rank() == 2
    assert decomposition.index() == 3
    assert decomposition.gluing_quotient().cardinality() == 3

    restrictions = decomposition.component_isometries()
    assert restrictions[1] == decomposition.summand(1).O().one()
    assert restrictions[3] != decomposition.summand(3).O().one()

    cyclotomic = decomposition.summand(3)
    root_reflection = cyclotomic.reflection(cyclotomic.basis_vector(0))
    assert root_reflection in cyclotomic.O()
    assert root_reflection not in decomposition.component_centralizers()[3]


def test_cyclotomic_component_tuple_lifts_exactly_when_it_preserves_the_glue() -> None:
    isometry = cyclic_permutation_of_Z3()
    decomposition = isometry.cyclotomic_decomposition(3)
    restrictions = decomposition.component_isometries()

    lifted = decomposition.lift_component_isometries(
        {1: restrictions[1], 3: restrictions[3]}
    )

    assert lifted == isometry
    assert lifted in decomposition.centralizer_group()

    incompatible = {
        1: decomposition.summand(1).O().one(),
        3: negation_of(decomposition.summand(3)),
    }
    assert incompatible[3] in decomposition.component_centralizers()[3]
    assert not decomposition.component_isometries_extend(incompatible)


def test_the_centralizer_of_minus_one_on_Z2_is_the_signed_permutation_group_of_order_8() -> None:
    r"""O(I_2) is the signed permutation group (Z/2)^2 x| S_2 of order 8, and -1
    is central in it, so its centralizer is all of O(I_2)."""
    lattice = Lattices(ZZ)([[1, 0], [0, 1]])
    minus_one = negation_of(lattice)

    assert lattice.O().cardinality() == 8
    assert minus_one.centralizer_group().cardinality() == 8
    first, second = lattice.module_generators()
    swap = lattice.O()({0: second, 1: first})
    assert swap in minus_one.centralizer_group()
    assert swap(first) == second
