r"""Archive reconciliation for the generating family of an ideal as a module."""

from dzack_research.preamble.all import ZZ


def test_fractional_ideal_generators_are_the_module_generating_family() -> None:
    ideal = ZZ.fractional_ideal(ZZ(2))

    assert ideal.ideal_generators() is ideal.module_generators()
    assert tuple(ideal.ideal_generators()) == tuple(ideal.module_generators())
    assert ideal.ideal_generators().index_set() is ideal.module_generating_set()


def test_fractional_generators_are_not_replaced_by_integral_copies() -> None:
    half = ZZ.fractional_ideal(ZZ.fraction_field()(1) / 2)
    generator = next(iter(half.ideal_generators()))

    assert generator.parent() is half
    assert half.inclusion()(generator) == ZZ.fraction_field()(1) / 2
