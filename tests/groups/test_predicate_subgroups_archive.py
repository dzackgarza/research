r"""Archive reconciliation for predicate-defined subgroups.

The archived object retained an ambient group, an exact membership predicate
and the subgroup inclusion.  The live owner keeps that contract and refines
special constructions such as centralizers into dedicated subgroup categories.
"""

from dzack_research.preamble.all import Groups
from dzack_research.preamble.categories.group.predicate_subgroups import (
    CentralizerSubgroups,
    is_predicate_subgroup,
    predicate_subgroup,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/predicate_subgroups.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
    "disposition": "reconciled-live-owner",
}


def test_predicate_subgroup_retains_supergroup_predicate_and_inclusion() -> None:
    group = Groups.S(3)
    subgroup = predicate_subgroup(
        group,
        lambda element: element.determinant() == 1,
        "det(g)=1",
    )

    assert is_predicate_subgroup(subgroup)
    assert subgroup.supergroup() is group
    assert subgroup.one() in subgroup
    assert subgroup.defining_predicate()(subgroup.one()) is True

    inclusion = subgroup.inclusion()
    assert inclusion.domain() is subgroup
    assert inclusion.codomain() is group
    assert inclusion(subgroup.one()) == group.one()


def test_centralizer_is_a_structured_predicate_subgroup() -> None:
    group = Groups.S(3)
    element = group.group_generators()[0]
    centralizer = group.centralizer(element)

    assert is_predicate_subgroup(centralizer)
    assert centralizer in CentralizerSubgroups(group)
    assert centralizer.centralizing_element() == element
    assert element in centralizer
