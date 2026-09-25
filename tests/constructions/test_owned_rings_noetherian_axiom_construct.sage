r"""The integers are Noetherian."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_integers_are_noetherian() -> None:
    assert ZZ in NoetherianRings()
    assert ZZ.ideal(6).ideal_generators().cardinality() == cardinal(1)

