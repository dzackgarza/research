r"""The integers lie in the commutative refinement of owned rings."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_integer_multiplication_is_commutative() -> None:
    assert ZZ in CommutativeRings()
    assert ZZ(2) * ZZ(3) == ZZ(3) * ZZ(2)

