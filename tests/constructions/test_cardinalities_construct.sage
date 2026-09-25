r"""Finite and infinite cardinal arithmetic lives in the cardinality category."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_basic_cardinal_arithmetic() -> None:
    cardinals = Cardinalities()

    assert cardinal(3) in cardinals
    assert aleph0 in cardinals
    assert continuum in cardinals
    assert cardinal(3) + cardinal(4) == cardinal(7)
    assert cardinal(2) ** cardinal(3) == cardinal(8)
    assert cardinal(2) ** aleph0 == continuum
    assert cardinals.lt(aleph0, continuum)
    assert cardinal(3).is_infinite() is False
    assert aleph0.is_infinite()
    assert aleph0.is_aleph()
    assert aleph0.is_countably_infinite()
    assert aleph0.aleph_index() == ordinal(0)
    assert aleph0.initial_ordinal() == omega(0)
    assert continuum.is_continuum()
    assert continuum.is_uncountably_infinite()
    assert cardinal(3).sort_key() < aleph0.sort_key()
