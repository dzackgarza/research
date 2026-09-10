r"""Archive reconciliation for represented torsors as chosen-point ``G``-sets."""

from dzack_research.preamble.all import Groups, Torsors, finite_g_set


def test_regular_finite_g_set_refines_to_the_torsor_category_in_place() -> None:
    group = Groups.C(3)
    regular = finite_g_set(tuple(group), group, lambda left, right: left * right)

    torsor = Torsors(group)(regular)

    assert torsor is regular
    assert torsor in Torsors(group)
    assert torsor.acting_group() is group


def test_selected_torsor_point_trivializes_enumeration_and_cardinality() -> None:
    group = Groups.C(3)
    torsor = Torsors(group)(
        finite_g_set(tuple(group), group, lambda left, right: left * right)
    )
    chosen = torsor.an_element()

    expected = tuple(torsor.act(group_element, chosen) for group_element in group)
    assert tuple(torsor) == expected
    assert torsor.cardinality() == group.cardinality()
    assert len(set(expected)) == int(group.cardinality())


def test_torsor_transporter_is_the_unique_group_element_between_points() -> None:
    group = Groups.C(3)
    torsor = Torsors(group)(
        finite_g_set(tuple(group), group, lambda left, right: left * right)
    )
    source = torsor.an_element()
    target = torsor.act(group.group_generators()[0], source)

    transporter = torsor.transporter(source, target)

    assert torsor.act(transporter, source) == target
    assert tuple(
        group_element
        for group_element in group
        if torsor.act(group_element, source) == target
    ) == (transporter,)
