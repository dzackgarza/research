r"""Archive reconciliation for the category of realized absolute Galois groups."""

from dzack_research.preamble.all import GF, ZZ
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
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








def test_finite_field_frobenius_uses_the_full_field_order() -> None:
    field = GF(25, "a")
    group = AbsoluteGaloisGroup(field)
    generator = field.multiplicative_generator()
    frobenius = group.frobenius()

    q = group.base_field_order()
    assert q.parent() is ZZ
    assert (q + ZZ.one()).parent() is ZZ
    assert frobenius.frobenius_exponent().parent() is ZZ
    assert q == 25
    assert frobenius(generator) == generator**q
    assert frobenius(generator) != generator ** field.characteristic()
