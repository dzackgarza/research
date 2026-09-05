r"""The group law is composition, and permutation groups act on the left.

``(g h)(x) = g(h(x))``; the permutation matrices of the natural action
compose the same way, so ``rho(g h) = rho(g) rho(h)``; relators of the
chosen presentation multiply to the identity in the owned order.
"""

from dzack_research.preamble.all import (
    QQ,
    FiniteGSets,
    FreeModule,
    GroupModule,
    Groups,
    Subgroups,
)


def _natural_permutation_module(ring, group, degree):
    module = FreeModule(ring, degree)

    def act(group_element, vector):
        return module.Mor(module)(
            {
                label: module.module_generator(int(group_element(label + 1)) - 1)
                for label in range(degree)
            }
        )(vector)

    return GroupModule(module, group, act)


def test_the_product_of_permutations_is_their_composition() -> None:
    group = Groups.S(4)
    for left in group.group_generators():
        for right in group.group_generators():
            for point in (1, 2, 3, 4):
                assert (left * right)(point) == left(right(point))


def test_the_natural_permutation_representation_is_a_left_action() -> None:
    group = Groups.S(3)
    representation = _natural_permutation_module(QQ, group, 3)
    for left in group.group_generators():
        for right in group.group_generators():
            assert representation.action_of(left * right) == (
                representation.action_of(left) * representation.action_of(right)
            )


def test_chosen_relators_multiply_to_the_identity_in_the_owned_order() -> None:
    for group in (Groups.S(3), Groups.D(4), Groups.A(4)):
        generators = tuple(group.group_generators())
        for relator in group.defining_relations():
            product = group.one()
            for letter in relator.Tietze():
                generator = generators[abs(letter) - 1]
                product = product * (generator if letter > 0 else ~generator)
            assert product.is_one()


def test_orbits_and_stabilizers_of_the_natural_action() -> None:
    symmetric = Groups.S(4)
    assert symmetric.action_on((1, 2, 3, 4)) in FiniteGSets(symmetric)
    assert symmetric.orbits((1, 2, 3, 4)).cardinality() == 1
    assert symmetric.orbit(1).cardinality() == 4
    assert symmetric.is_transitive()
    stabilizer = symmetric.stabilizer(1)
    assert stabilizer in Subgroups(symmetric)
    assert stabilizer.order() == 6
    assert symmetric.left_cosets(stabilizer).cardinality() == 4
    assert Groups.C(2).action_on((1, 2, 3, 4)).orbits().cardinality() == 3
