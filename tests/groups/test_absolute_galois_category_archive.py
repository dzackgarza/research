r"""Archive reconciliation for the category of realized absolute Galois groups."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
)
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/group/profinite/absolute_galois_group.sage",
        "live_owner": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
        "owner_overrides": {
            "AbsoluteGaloisGroupsOfFiniteFields": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
            "AbsoluteGaloisGroupsOfFiniteFields.super_categories": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
            "AbsoluteGaloisGroupsOfFiniteFields.ParentMethods": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
            "AbsoluteGaloisGroupsOfFiniteFields.ParentMethods.frobenius": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
            "AbsoluteGaloisGroupsOfFiniteFields.ParentMethods.topological_group_generators": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
            "AbsoluteGaloisGroupsOfFiniteFields.ParentMethods.is_abelian": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
            "AbsoluteGaloisGroupsOfFiniteFields.ParentMethods.has_canonical_realization": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
            "LiftCoset": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
            "LiftCoset.ambient": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
            "LiftCoset.representative": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
            "LiftCoset.extension": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
            "absolute_galois_group_category": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
        },
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/group/profinite/absolute_galois_groups.sage",
        "live_owner": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py",
        "owner_overrides": {
            "AbsoluteGaloisGroupParent": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroupParent.base_field": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroupParent.finite_quotient": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroupParent.restriction_map": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroupParent.lift": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.finite_quotient": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.restriction_map": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.open_subgroup": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.open_subgroup_class": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.cyclotomic_character": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.quadratic_character": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.decomposition_group": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.decomposition_group_class": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.inertia_group": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.inertia_group_class": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.frobenius": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.frobenius_class": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.lift": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.lifts": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "AbsoluteGaloisGroups.ParentMethods.topological_generating_family": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
            "absolute_galois_group_factory": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


def test_realized_absolute_galois_group_retains_basepoint_coslice_data() -> None:
    field = GF(5)
    group = AbsoluteGaloisGroup(field)
    embedding = group.base_embedding()
    extension_object = group.extension_object()

    assert group in OwnedGroups()
    assert group in AbsoluteGaloisGroups()
    assert group in ProfiniteGroups()
    assert group.base_field() is field
    assert embedding.domain() is field
    assert embedding.codomain() is group.algebraic_closure()
    assert extension_object.category() is group.slice_category()


def test_absolute_galois_element_is_the_automorphism_square_of_the_slice_object() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    square = group.slice_automorphism(frobenius)

    assert square.domain() is group.extension_object()
    assert square.codomain() is group.extension_object()
    left, right = square.forward().components()
    assert left.domain() is group.base_field()
    assert left.codomain() is group.base_field()
    assert right == frobenius.as_morphism()


def test_finite_field_absolute_galois_group_refines_to_procyclic_specialization() -> None:
    group = AbsoluteGaloisGroup(GF(5))

    assert group in AbsoluteGaloisGroupsOfFiniteFields()
    assert group.is_profinite() is True
    assert group.is_abelian() is True
    assert group.is_finite() is False
    assert tuple(group.topological_group_generators()) == (group.frobenius(),)


def test_finite_field_frobenius_uses_the_full_field_order() -> None:
    field = GF(25, "a")
    group = AbsoluteGaloisGroup(field)
    generator = field.multiplicative_generator()
    frobenius = group.frobenius()

    q = group.base_field_order()
    assert q == 25
    assert frobenius(generator) == generator**q
    assert frobenius(generator) != generator ** field.characteristic()
