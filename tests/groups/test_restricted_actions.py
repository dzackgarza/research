r"""The action restricted to invariant and isotypic pieces of a group module.

The permutation module of the symmetric group on three letters splits over
the rationals into the trivial line and the two-dimensional standard
representation.  Both pieces are stable, so each carries the restricted
action, and the restricted characters identify which piece is which: the
trivial character is one everywhere, while the standard character takes the
values two, zero and minus one on the identity, a transposition and a
three-cycle.
"""

from dzack_research.preamble.all import (
    FreeModule,
    Groups,
    Modules,
    QQ,
)


def _permutation_module():
    group = Groups.S(3)
    points = (1, 2, 3)
    module = FreeModule(QQ, len(points))

    def act(group_element, vector):
        return module.Mor(module)(
            {
                label: module.module_generator(
                    int(group_element(points[label])) - 1
                )
                for label in range(len(points))
            }
        )(vector)

    return group, Modules(QQ[group])(module, act)


def _transposition_and_three_cycle(group):
    transposition = next(
        element for element in group.group_generators() if element.order() == 2
    )
    three_cycle = next(
        element for element in group.group_generators() if element.order() == 3
    )
    return transposition, three_cycle


def test_the_standard_isotypic_component_carries_the_standard_representation() -> None:
    group, representation = _permutation_module()
    transposition, three_cycle = _transposition_and_three_cycle(group)
    standard = representation.isotypic_decomposition().nontrivial_components().unrank(0)

    equivariant = representation.restrict_action_to(standard.inclusion())
    restricted = equivariant.domain()
    character = restricted.character()

    assert equivariant.codomain() is representation
    assert restricted in Modules(QQ[group])
    assert restricted.rank() == 2
    assert character(group.one()) == 2
    assert character(transposition) == 0
    assert character(three_cycle) == -1
    # The standard representation has no invariant vector.
    assert restricted.module_invariants().rank() == 0


def test_the_invariants_carry_the_trivial_action_of_the_group() -> None:
    group, representation = _permutation_module()
    transposition, three_cycle = _transposition_and_three_cycle(group)
    invariants = representation.module_invariants()

    restricted = representation.restrict_action_to(invariants.inclusion()).domain()
    character = restricted.character()

    assert restricted.rank() == 1
    assert character(group.one()) == 1
    assert character(transposition) == 1
    assert character(three_cycle) == 1
