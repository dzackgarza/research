r"""Archive reconciliation for chosen group-generator count queries."""

from dzack_research.preamble.all import QQ, Groups


def test_group_without_chosen_generators_has_no_chosen_generator_count() -> None:
    group = Groups.GL(2, QQ)

    assert not hasattr(group, "number_of_group_generators")


def test_group_with_chosen_generators_keeps_the_exact_count() -> None:
    group = Groups.C(5)

    assert group.number_of_group_generators() == 1
    assert group.number_of_group_generators() == group.group_generators().cardinality()
