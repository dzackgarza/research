r"""Archive reconciliation for functorial cardinal arithmetic."""

import pytest

from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal


def comparison(source, target):
    cardinals = Cardinalities()
    return cardinals.Mor(cardinal(source), cardinal(target)).unique_morphism()


def test_cardinal_sum_and_product_act_on_comparison_morphisms() -> None:
    cardinals = Cardinalities()
    first = comparison(2, 5)
    second = comparison(3, 7)

    summed = cardinals.sum_morphism(first, second)
    product = cardinals.product_morphism(first, second)

    assert summed.domain() == cardinal(5)
    assert summed.codomain() == cardinal(12)
    assert product.domain() == cardinal(6)
    assert product.codomain() == cardinal(35)


def test_cardinal_power_acts_covariantly_for_nonzero_base() -> None:
    cardinals = Cardinalities()
    base = comparison(2, 3)
    exponent = comparison(1, 2)
    powered = cardinals.power_morphism(base, exponent)

    assert powered.domain() == cardinal(2)
    assert powered.codomain() == cardinal(9)


def test_cardinal_power_refuses_exponent_monotonicity_at_zero_base() -> None:
    cardinals = Cardinalities()
    base = comparison(0, 1)
    exponent = comparison(1, 2)

    with pytest.raises(ValueError, match="nonzero source base"):
        cardinals.power_morphism(base, exponent)
