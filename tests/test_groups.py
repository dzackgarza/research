from sage.all import AbelianGroup, FreeGroup, GF, GL, SymmetricGroup
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.group import (
    Groups,
    GroupsWithChosenFiniteGeneratingSet,
    GroupsWithChosenFinitePresentation,
    OwnedAbelianGroups,
    OwnedFiniteAbelianGroups,
    OwnedFiniteGroups,
    OwnedFinitelyGeneratedGroups,
    OwnedFinitelyPresentedGroups,
    OwnedGroups,
    ProfiniteGroups,
    centralizer,
    groups,
)


def test_groups_is_the_owned_flat_catalogue() -> None:
    assert Groups is groups is OwnedGroups
    for group, order in (
        (Groups.C(5), 5),
        (Groups.S(4), 24),
        (Groups.A(4), 12),
        (Groups.D(5), 10),
        (Groups.Q(), 8),
        (Groups.V4(), 4),
        (Groups.GL(2, GF(3)), 48),
        (Groups.SL(2, GF(3)), 24),
        (Groups.Sp(2, GF(3)), 24),
    ):
        assert group in OwnedGroups()
        assert group in OwnedFiniteGroups()
        assert group.order() == order


def test_native_sage_group_constructors_are_admitted_after_import() -> None:
    symmetric = SymmetricGroup(3)
    free = FreeGroup(2)
    abelian = AbelianGroup([2, 4])
    matrix_group = GL(2, GF(3))

    assert symmetric in OwnedFiniteGroups()
    assert free in OwnedFinitelyPresentedGroups()
    assert free not in OwnedFiniteGroups()
    assert abelian in OwnedFiniteAbelianGroups()
    assert matrix_group in OwnedFiniteGroups()


def test_property_categories_are_distinct_from_chosen_data_categories() -> None:
    free = FreeGroup(2)
    assert free in OwnedFinitelyGeneratedGroups()
    assert free in OwnedFinitelyPresentedGroups()
    assert free in GroupsWithChosenFiniteGeneratingSet()
    assert free in GroupsWithChosenFinitePresentation()
    assert free.is_finitely_generated() is True
    assert free.is_finitely_presented() is True


def test_group_generators_are_a_finite_ordered_set_without_hashing_elements() -> None:
    free = FreeGroup(2)
    quotient = free / [free.gen(0) ** 2, free.gen(1) ** 3]

    generators = quotient.group_generators()
    assert generators.cardinality() == 2
    assert tuple(generators) == tuple(quotient.gens())
    assert generators in generators.category()


def test_trivial_quotient_has_empty_generating_set_but_two_presentation_letters() -> None:
    free = FreeGroup(2)
    trivial = free / [free.gen(0), free.gen(1)]

    assert trivial.group_generators().cardinality() == 0
    presenting = trivial.presenting_free_group()
    assert presenting.group_generators().cardinality() == 2


def test_chosen_presentations_are_exposed_on_native_group_objects() -> None:
    free = FreeGroup(1)
    c2 = free / [free.gen(0) ** 2]
    for group in (c2, Groups.C(2), Groups.S(2), Groups.Abelian([2])):
        assert group in OwnedFinitelyPresentedGroups()
        assert group in GroupsWithChosenFinitePresentation()
        relators = tuple(relation.Tietze() for relation in group.defining_relations())
        assert relators == ((1, 1),)


def test_subgroup_inclusion_is_a_real_morphism() -> None:
    group = SymmetricGroup(4)
    subgroup = group.subgroup([group.gen(0)])
    inclusion = subgroup.inclusion()

    assert subgroup.supergroup() is group
    assert inclusion.domain() is subgroup
    assert inclusion.codomain() is group
    assert inclusion.is_injective()
    assert inclusion(subgroup.gen(0)) in group


def test_predicate_centralizer_does_not_require_generators() -> None:
    group = SymmetricGroup(4)
    element = group.gen(0)
    subgroup = centralizer(group, element)

    assert subgroup in OwnedGroups()
    assert subgroup.supergroup() is group
    assert subgroup.one() in subgroup
    assert element in subgroup
    assert group.gen(1) not in subgroup
    assert subgroup.inclusion().domain() is subgroup
    assert subgroup.inclusion().codomain() is group


def test_finite_group_isomorphism_is_decided_but_general_fp_is_not_guessed() -> None:
    assert Groups.C(3).is_isomorphic_to(Groups.C(3)) is True
    assert Groups.C(3).is_isomorphic_to(Groups.S(3)) is False
    assert Groups.Free(2).is_isomorphic_to(Groups.Free(2)) is Unknown


def test_automorphism_group_is_an_owned_group() -> None:
    group = Groups.C(3)
    automorphisms = group.Aut()

    assert automorphisms in OwnedFiniteGroups()
    assert automorphisms.one().inverse() == automorphisms.one()
    assert automorphisms.group_generators().cardinality() == 1


def test_profinite_groups_sit_over_owned_groups() -> None:
    assert ProfiniteGroups().is_subcategory(OwnedGroups())


def test_endomorphisms_of_an_abelian_group_form_a_ring() -> None:
    group = AbelianGroup([3])
    endomorphisms = group.endomorphism_ring()
    one = endomorphisms.one()
    zero = endomorphisms.zero()
    f = one + one
    g = one + one + one

    for element in group:
        assert one(element) == element
        assert zero(element) == group.one()
        assert (f + g)(element) == (g + f)(element)
        assert (f * g)(element) == f(g(element))
        assert (f + -f)(element) == group.one()


def test_abelian_group_has_the_canonical_integer_action() -> None:
    group = AbelianGroup([5])
    action = group.scalar_action()

    assert action.domain() is group.scalar_action().domain()
    assert action.domain() == __import__("sage.all", fromlist=["ZZ"]).ZZ
    assert action.codomain() is group.endomorphism_ring()
    for element in group:
        for n in (-2, -1, 0, 1, 2, 7):
            assert action(n)(element) == element ** n
            assert group.scalar_multiple(n, element) == element ** n
