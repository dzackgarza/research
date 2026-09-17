r"""Structured subgroup constructors retain the mathematics that defines them."""

from dzack_research.preamble.all import ZZ, Lattices, Set
from dzack_research.preamble.categories.group.groups import GeneratedSubgroups, OwnedGroups
from dzack_research.preamble.categories.group.predicate_subgroups import (
    CentralizerSubgroups,
    IntersectionSubgroups,
    KernelSubgroups,
    PredicateSubgroups,
    PreimageSubgroups,
    StabilizerSubgroups,
)


def _orthogonal_group():
    lattice = Lattices(ZZ)("A1")
    return lattice, lattice.O()


def test_generated_subgroup_retains_the_selected_generating_family() -> None:
    _lattice, group = _orthogonal_group()
    generator = group.group_generators().an_element()

    subgroup = group.subgroup((generator,))

    assert subgroup in GeneratedSubgroups(group)
    assert subgroup.selected_subgroup_generators().cardinality() == 1
    assert subgroup.selected_subgroup_generators()[0] == generator
    assert subgroup.supergroup() is group
    subobjects = OwnedGroups().Subobjects(group)
    assert subgroup.category().is_subcategory(subobjects)
    assert subobjects.as_slice_object(subgroup).arrow() is subgroup.inclusion()
    trivial = group.subgroup(())
    assert subobjects.Mor(trivial, subgroup).has_morphism()
    assert not subobjects.Mor(subgroup, trivial).has_morphism()


def test_kernel_and_preimage_subgroups_retain_their_defining_maps() -> None:
    _lattice, group = _orthogonal_group()
    representation = group.discriminant_representation()
    target = representation.codomain()
    trivial = target.subgroup(())

    kernel = group.kernel(representation)
    preimage = group.preimage(representation, trivial)

    assert kernel in KernelSubgroups(group)
    assert kernel.kernel_morphism() is representation
    assert preimage in PreimageSubgroups(group)
    assert preimage.preimage_morphism() is representation
    assert preimage.target_subgroup() is trivial


def test_stabilizer_centralizer_and_intersection_retain_their_defining_objects() -> None:
    lattice, group = _orthogonal_group()
    vector = lattice.module_generator(0)
    line = vector.sublattice()
    identity = group.one()

    vector_stabilizer = group.stabilizer(vector)
    setwise = group.stabilizer(line, action="setwise")
    pointwise = group.stabilizer(line, action="pointwise")
    centralizer = group.centralizer(identity)
    intersection = group.intersection(setwise, centralizer)

    assert vector_stabilizer in StabilizerSubgroups(group)
    assert vector_stabilizer.stabilized_object() is vector
    assert vector_stabilizer.stabilizer_action() == "pointwise"

    assert setwise in StabilizerSubgroups(group)
    assert setwise.stabilized_object() is line
    assert setwise.stabilizer_action() == "setwise"
    assert pointwise in StabilizerSubgroups(group)
    assert pointwise.stabilized_object() is line
    assert pointwise.stabilizer_action() == "pointwise"

    assert centralizer in CentralizerSubgroups(group)
    assert centralizer.centralizing_element() is identity

    assert intersection in IntersectionSubgroups(group)
    assert intersection.intersected_subgroups() == Set((setwise, centralizer))


def test_predicate_subgroup_notation_and_structured_routes_use_category_constructors() -> None:
    _lattice, group = _orthogonal_group()
    identity = group.one()
    def predicate(element):
        return element * identity == identity * element

    declared = PredicateSubgroups(group)(predicate, "g commutes with 1")
    notation = group.predicate_subgroup(predicate, "g commutes with 1")
    centralizer = CentralizerSubgroups(group)(identity)

    assert declared.supergroup() is group
    assert notation.supergroup() is group
    assert declared.defining_predicate()(identity)
    assert notation.defining_predicate()(identity)
    assert centralizer.centralizing_element() is identity
    assert centralizer.inclusion().codomain() is group
