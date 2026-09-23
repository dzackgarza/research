r"""Archive reconciliation for the remaining generic group-hierarchy semantics."""

from dzack_research.preamble.all import GF, Groups
from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFiniteGeneratingSet,
    OwnedFiniteGroups,
    OwnedFinitelyGeneratedGroups,
    OwnedFinitelyPresentedGroups,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_group_hierarchy.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/groups.py",
    "owner_overrides": {
        "test_trivial_action_is_a_functor_into_group_lattices": "src/dzack_research/preamble/categories/functors/group_actions.py",
        "test_trivial_action_carries_lattice_maps_to_equivariant_ones": "src/dzack_research/preamble/categories/functors/group_actions.py",
        "test_invariants_is_right_adjoint_to_the_trivial_action": "src/dzack_research/preamble/categories/functors/group_actions.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_generating_set_is_distinct_from_presenting_free_group() -> None:
    free = Groups.Free(2)
    generators = tuple(free.group_generators())
    trivial = free.quotient_by_relators(generators)

    assert trivial.group_generators().cardinality() == 0
    assert trivial.presenting_free_group().group_generators().cardinality() == 2
    assert all(generator in trivial for generator in trivial.group_generators())


def test_finite_generation_is_the_finiteness_of_the_selected_generating_family() -> None:
    cyclic = Groups.C(5)

    assert cyclic in OwnedFinitelyGeneratedGroups()
    assert cyclic in GroupsWithChosenFiniteGeneratingSet()
    assert cyclic.group_generators().cardinality() == 1
    assert cyclic.number_of_group_generators() == 1


def test_four_realizations_of_c2_retain_the_one_generator_square_relation() -> None:
    free = Groups.Free(1)
    generator = tuple(free.group_generators())[0]
    realizations = (
        free.quotient_by_relators((generator * generator,)),
        Groups.C(2).presentation(),
        Groups.S(2).presentation(),
        Groups.Abelian([2]).presentation(),
    )

    for group in realizations:
        assert group in OwnedFinitelyPresentedGroups()
        presenting = group.presenting_free_group()
        generator = next(iter(presenting.group_generators()))
        assert presenting.group_generators().cardinality() == 1
        relators = tuple(
            tuple(relation.parent().reduced_word(relation))
            for relation in group.defining_relations()
        )
        assert relators == ((generator, generator),)


def test_flat_group_catalogue_constructs_standard_finite_and_infinite_families() -> None:
    finite_groups = (
        (Groups.C(5), 5),
        (Groups.S(4), 24),
        (Groups.A(4), 12),
        (Groups.D(5), 10),
        (Groups.Q(), 8),
        (Groups.V4(), 4),
        (Groups.GL(2, GF(3)), 48),
        (Groups.SL(2, GF(3)), 24),
        (Groups.Sp(2, GF(3)), 24),
    )

    for group, order in finite_groups:
        assert group in Groups()
        assert group in OwnedFiniteGroups()
        assert group.order() == order

    assert Groups.Free(2) in Groups()
    assert Groups.Braid(4) in Groups()
