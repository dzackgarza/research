r"""Archive reconciliation for the generic owned group surface."""

from dzack_research.preamble.all import Groups, aleph0

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/groups.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/groups.py",
    "owner_overrides": {
        "OwnedGroups.Subobjects": "src/dzack_research/preamble/categories/abstract_categories/cat.py",
        "OwnedGroups.Subobjects.ParentMethods": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "OwnedGroups.Subobjects.ParentMethods.inclusion": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
    },
    "disposition": "reconciled-live-owner",
}




def test_finite_group_product_retains_group_structure_and_order() -> None:
    product = Groups().product((Groups.C(2), Groups.C(3)))

    assert product in Groups()
    assert product.order() == 6
    assert product.is_isomorphic_to(Groups.C(6))


def test_finite_group_centers_are_owned_subgroups() -> None:
    symmetric = Groups.S(3)
    cyclic = Groups.C(2)

    assert symmetric.center().order() == 1
    assert symmetric.center().supergroup() is symmetric
    assert cyclic.center().order() == 2
    assert cyclic.center().supergroup() is cyclic


def test_finite_group_commutator_subgroups_are_owned() -> None:
    symmetric = Groups.S(3)
    cyclic = Groups.C(4)

    assert symmetric.commutator_subgroup().order() == 3
    assert symmetric.commutator_subgroup().supergroup() is symmetric
    assert cyclic.commutator_subgroup().order() == 1
    assert cyclic.commutator_subgroup().supergroup() is cyclic


def test_group_coproduct_is_the_owned_free_product() -> None:
    coproduct = Groups().coproduct((Groups.C(2), Groups.C(3)))

    assert coproduct in Groups()
    assert coproduct.cardinality() == aleph0
    assert coproduct.group_generators().cardinality() == 2


def test_group_coproduct_factorization_extends_the_factor_maps() -> None:
    two = Groups.C(2)
    three = Groups.C(3)
    target = Groups.S(3)
    construction = Groups().coproduct_construction((two, three))
    diagram = construction.diagram()
    first_index = diagram.domain()(0)
    second_index = diagram.domain()(1)
    two_generator = two.group_generators()[0]
    three_generator = three.group_generators()[0]
    first = two.Mor(target)({two_generator: target((1, 2))})
    second = three.Mor(target)({three_generator: target((1, 2, 3))})
    cocone = (diagram).CoproductCocones().cocone(
        target,
        lambda index: first if index is first_index else second,
    )

    factor = construction.factor(cocone).apex_map()
    first_injection = construction.costructure_morphism(first_index)
    second_injection = construction.costructure_morphism(second_index)
    assert factor(first_injection(two_generator)) == first(two_generator)
    assert factor(second_injection(three_generator)) == second(three_generator)


def test_finite_group_subgroups_are_owned_and_keep_the_ambient_group() -> None:
    cyclic = Groups.C(6)
    subgroups = cyclic.subgroups()

    assert subgroups.cardinality() == 4
    assert tuple(subgroup.cardinality() for subgroup in subgroups) == (1, 2, 3, 6)
    assert all(subgroup.supergroup() is cyclic for subgroup in subgroups)












def test_archived_finite_group_character_surface_is_live_on_the_owned_group() -> None:
    group = Groups.S(3)
    representatives = group.conjugacy_classes_representatives()
    irreducibles = group.irreducible_characters()
    trivial = group.trivial_character()

    assert representatives.cardinality() == irreducibles.cardinality()
    assert trivial in irreducibles
    assert all(trivial(representative) == 1 for representative in representatives)
