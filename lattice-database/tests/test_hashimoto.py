"""Fast source-intake checks on Hashimoto table parsing that need no corpus."""

from latticedb import hashimoto


def test_the_group_of_a_genus_symbol_is_the_sum_of_its_cyclic_factors() -> None:
    assert hashimoto.symbol_group("2_II^{-2}, 8_1^{+1}, 5^{-1}") == [2, 2, 5, 8]
