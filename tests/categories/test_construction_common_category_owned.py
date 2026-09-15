r"""Mixed structures use the explicitly selected common mathematical owner."""

from dzack_research.preamble.all import ZZ, Lattices, Modules


def test_biproduct_of_formed_and_plain_modules_dispatches_to_the_common_module_owner() -> None:
    formed = Lattices(ZZ)("A2")
    plain = ZZ.free_module(1)

    direct_sum = Modules(ZZ).biproduct((formed, plain))

    assert direct_sum in Modules(ZZ)
    assert direct_sum.module_rank() == 3
    assert direct_sum not in Lattices(ZZ)
