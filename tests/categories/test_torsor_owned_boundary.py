r"""The torsor category is an owned group-parameterized mathematical category."""

from dzack_research.preamble.all import FiniteGSets, Groups, Torsors
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)


def test_torsors_are_owned_by_the_actual_acting_group() -> None:
    group = Groups.S(3)
    category = Torsors(group)
    regular = FiniteGSets(group)(tuple(group), lambda left, right: left * right)

    assert isinstance(category, OwnedParameterizedCategory)
    assert category.group() is group
    assert category.acting_group() is group
    assert category.base() is group
    assert group in category.parameter_category()
    assert regular in category
    assert regular in category.super_categories()[0]

    generator = group.group_generators()[0]
    assert regular.transporter(group.one(), generator) == generator


def test_distinct_acting_groups_give_distinct_torsor_categories() -> None:
    symmetric_three = Groups.S(3)
    symmetric_four = Groups.S(4)

    assert Torsors(symmetric_three) is not Torsors(symmetric_four)
    assert Torsors(symmetric_three).group() is symmetric_three
    assert Torsors(symmetric_four).group() is symmetric_four
