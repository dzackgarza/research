"""Fast source-intake checks on Höhn–Mason stabilizer logic that need no corpus."""

from latticedb import hoehn_mason


def test_the_group_order_is_the_order_of_the_closure() -> None:
    # The rotation by a quarter turn generates the cyclic group of order 4.
    assert hoehn_mason.group_order([((0, -1), (1, 0))]) == 4
