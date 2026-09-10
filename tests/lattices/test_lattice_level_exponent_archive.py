r"""Archive reconciliation for lattice level versus discriminant exponent.

For an even integral lattice the discriminant quadratic form takes values in
``QQ/2ZZ``.  Thus its level need not equal the exponent of the underlying
discriminant group.  Nikulin, *Integral symmetric bilinear forms and some of
their applications* (1980), section 1.3, is the archived source for this
distinction.
"""

from dzack_research.preamble.all import Lattices, ZZ


def test_even_rank_one_level_is_twice_the_discriminant_exponent() -> None:
    lattice = Lattices(ZZ)([[ZZ(2)]])
    discriminant = lattice.discriminant_group()

    assert lattice.is_even()
    assert tuple(discriminant.invariants()) == (ZZ(2),)
    assert lattice.level() == ZZ(4)
    assert lattice.level() != discriminant.invariants()[0]


def test_odd_rank_one_level_equals_the_discriminant_exponent() -> None:
    lattice = Lattices(ZZ)([[ZZ(3)]])
    discriminant = lattice.discriminant_group()

    assert not lattice.is_even()
    assert tuple(discriminant.invariants()) == (ZZ(3),)
    assert lattice.level() == ZZ(3)


def test_unimodular_e8_has_level_one() -> None:
    assert Lattices.E8.discriminant_group().cardinality() == 1
    assert Lattices.E8.level() == ZZ(1)
