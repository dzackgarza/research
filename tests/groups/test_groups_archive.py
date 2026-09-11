r"""Archive reconciliation for the generic owned group surface."""

from dzack_research.preamble.all import GF, Groups
from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFiniteGeneratingSet,
    GroupsWithChosenFinitePresentation,
    OwnedFiniteGroups,
    OwnedFinitelyGeneratedGroups,
    OwnedFinitelyPresentedGroups,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/groups.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/groups.py",
    "owner_overrides": {
        "OwnedGroups.Subobjects": "src/dzack_research/preamble/categories/abstract_categories/constructions.py",
        "OwnedGroups.Subobjects.ParentMethods": "src/dzack_research/preamble/categories/abstract_categories/constructions.py",
        "OwnedGroups.Subobjects.ParentMethods.inclusion": "src/dzack_research/preamble/categories/abstract_categories/constructions.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_native_group_constructors_cross_into_owned_property_categories() -> None:
    linear = Groups.GL(2, GF(3))
    free = Groups.Free(2)

    assert linear in OwnedFiniteGroups()
    assert free in OwnedFinitelyGeneratedGroups()
    assert free in OwnedFinitelyPresentedGroups()
    assert free in GroupsWithChosenFiniteGeneratingSet()
    assert free in GroupsWithChosenFinitePresentation()
    assert free.is_finitely_generated() is True
    assert free.is_finitely_presented() is True


def test_generated_subgroup_retains_an_actual_inclusion_into_its_supergroup() -> None:
    group = Groups.S(3)
    generator = group.group_generators()[0]
    subgroup = group.subgroup((generator,))
    inclusion = subgroup.inclusion()

    assert subgroup.supergroup() is group
    assert inclusion.domain() is subgroup
    assert inclusion.codomain() is group
    assert inclusion.is_injective()
    assert inclusion(subgroup.group_generators()[0]) in group


def test_conjugation_is_a_group_morphism_into_the_automorphism_group() -> None:
    group = Groups.S(3)
    conjugation = group.conjugation_morphism()
    automorphisms = group.Aut()
    first, second = tuple(group.group_generators())[:2]

    assert conjugation.domain() is group
    assert conjugation.codomain() is automorphisms
    assert conjugation(first).parent() is automorphisms
    assert conjugation(first * second) == conjugation(first) * conjugation(second)


def test_endomorphisms_of_an_abelian_group_form_the_live_endomorphism_ring() -> None:
    group = Groups.Abelian([3])
    endomorphisms = group.endomorphism_ring()
    one = endomorphisms.one()
    zero = endomorphisms.zero()
    twice = one + one

    assert endomorphisms.domain() is group
    assert endomorphisms.codomain() is group
    for element in group:
        assert one(element) == element
        assert zero(element) == group.one()
        assert twice(element) == element * element
        assert (twice * twice)(element) == twice(twice(element))


def test_archived_abelian_group_is_a_module_over_the_integers_by_its_power_action() -> None:
    from dzack_research.preamble.all import ZZ

    group = Groups.Abelian([2, 4])
    action = group.scalar_action()
    element = tuple(group.group_generators())[0] * tuple(group.group_generators())[1]

    assert action.domain() is ZZ
    assert action.codomain() is group.endomorphism_ring()
    for exponent in (-3, -1, 0, 1, 2, 4, 6):
        scalar = ZZ(exponent)
        assert action(scalar)(element) == element**exponent
        assert group.scalar_multiple(scalar, element) == element**exponent


def test_archived_discriminant_module_keeps_group_and_module_structure_on_one_parent() -> None:
    from dzack_research.preamble.all import Lattices, Modules, ZZ
    from dzack_research.preamble.categories.group.groups import OwnedFiniteAbelianGroups

    discriminant = Lattices(ZZ)("A2").discriminant_group()

    assert discriminant in OwnedFiniteAbelianGroups()
    assert discriminant in Modules(ZZ)
    element = next(iter(discriminant))
    order = ZZ(element.additive_order())
    assert discriminant.scalar_multiple(order, element) == discriminant.zero()


def test_archived_finite_group_character_surface_is_live_on_the_owned_group() -> None:
    group = Groups.S(3)
    representatives = group.conjugacy_classes_representatives()
    irreducibles = group.irreducible_characters()
    trivial = group.trivial_character()

    assert representatives.cardinality() == irreducibles.cardinality()
    assert trivial in irreducibles
    assert all(trivial(representative) == 1 for representative in representatives)
