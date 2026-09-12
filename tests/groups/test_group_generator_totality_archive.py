r"""Archive reconciliation for total group generator-count queries."""

from sage.misc.unknown import Unknown

from dzack_research.preamble.all import QQ, Groups


def test_group_without_chosen_generators_answers_unknown_instead_of_raising() -> None:
    group = Groups.GL(2, QQ)

    assert group.number_of_group_generators() is Unknown


def test_group_with_chosen_generators_keeps_the_exact_count() -> None:
    group = Groups.C(5)

    assert group.number_of_group_generators() == 1
    assert group.number_of_group_generators() == group.group_generators().cardinality()
