r"""The coproduct of three sets is the coproduct over a three-element index set.

Folding the binary coproduct gives an object with two summands, one of which
is itself a coproduct, so an injection is named by a path rather than by an
index.  Both objects satisfy the universal property and they are not the same
object; the one over the index set is the coproduct (`CON-14`), which is what
``product`` already builds.
"""

from dzack_research.preamble.all import (
    Sets,
    cardinal,
)


def test_three_sets_coproduct_over_a_three_element_index_set() -> None:
    factors = (Sets.Δ[0], Sets.Δ[1], Sets.Δ[2])

    coproduct = Sets().coproduct(factors)

    assert coproduct.index_set().cardinality() == cardinal(3)
    assert coproduct.cardinality() == cardinal(6)


def test_each_factor_is_the_summand_at_its_own_index() -> None:
    factors = (Sets.Δ[0], Sets.Δ[1], Sets.Δ[2])

    coproduct = Sets().coproduct(factors)
    index_set = coproduct.index_set()

    for position, factor in enumerate(factors):
        assert coproduct.cofactor(index_set(position)) is factor


def test_the_binary_coproduct_is_unchanged() -> None:
    r"""Two factors already were the coproduct over a two-element index set."""
    coproduct = Sets().coproduct((Sets.Δ[1], Sets.Δ[2]))

    assert coproduct.index_set().cardinality() == cardinal(2)
    assert coproduct.cardinality() == cardinal(5)
