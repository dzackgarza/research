r"""Construction-specific subgroup parents retain the mathematics that defines them."""

from dzack_research.preamble.all import Groups, Subgroups
from dzack_research.preamble.categories.group.groups import GeneratedSubgroups
from dzack_research.preamble.categories.group.predicate_subgroups import (
    CentralizerSubgroups,
    IntersectionSubgroups,
    KernelSubgroups,
    PreimageSubgroups,
    StabilizerSubgroups,
    centralizer,
    intersection_subgroup,
    preimage_subgroup,
)


def test_generated_subgroup_retains_its_selected_generators() -> None:
    group = Groups.S(3)
    generator = group.group_generators()[0]

    subgroup = group.subgroup((generator,))

    assert subgroup in Subgroups(group)
    assert subgroup in GeneratedSubgroups(group)
    assert tuple(subgroup.selected_subgroup_generators()) == (generator,)
    assert generator in subgroup


def test_kernel_and_preimage_are_distinct_structured_subgroup_constructions() -> None:
    group = Groups.S(3)
    identity = group.Mor(group).identity()
    generator = group.group_generators()[0]
    target = group.subgroup((generator,))

    kernel = identity.kernel()
    preimage = preimage_subgroup(identity, target)

    assert kernel in KernelSubgroups(group)
    assert kernel.kernel_morphism() is identity
    assert kernel.order() == 1

    assert preimage in PreimageSubgroups(group)
    assert preimage.preimage_morphism() is identity
    assert preimage.target_subgroup() is target
    assert generator in preimage


def test_stabilizer_centralizer_and_intersection_retain_their_defining_data() -> None:
    group = Groups.S(4)
    action = group.action_on((1, 2, 3, 4))
    stabilizer = action.stabilizer(1)
    element = group.group_generators()[0]
    commuting = centralizer(group, element)
    intersection = intersection_subgroup(group, (stabilizer, commuting))

    assert stabilizer in StabilizerSubgroups(group)
    assert stabilizer.stabilized_object() == 1
    assert stabilizer.stabilizer_action() == "pointwise"

    assert commuting in CentralizerSubgroups(group)
    assert commuting.centralizing_element() == element

    assert intersection in IntersectionSubgroups(group)
    assert intersection.intersected_subgroups() == (stabilizer, commuting)
    assert all(candidate in stabilizer and candidate in commuting for candidate in intersection)
