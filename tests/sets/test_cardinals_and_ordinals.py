import pytest
from sage.misc.unknown import Unknown

from dzack_research.preamble.all import (
    CardinalComparison,
    Cardinalities,
    Ordinals,
    aleph,
    aleph0,
    cardinal,
    continuum,
    omega,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_cardinalities.sage",
    "live_owner": "tests/sets/test_cardinals_and_ordinals.py",
    "owner_overrides": {
        "test_cardinality_functor_preserves_set_coproducts_and_products": "tests/sets/test_cardinality_construction_comparisons.py",
        "test_power_set_of_naturals_and_real_line_have_the_continuum": "tests/sets/test_cardinality_construction_comparisons.py",
        "test_standard_mathematical_objects_have_their_exact_cardinals": "tests/sets/test_standard_cardinals_archive.py",
    },
    "disposition": "reconciled-live-owner",
}




def test_natural_ordinal_operations_form_the_commutative_semiring() -> None:
    alpha = omega(0)
    beta = omega(1)
    gamma = omega(2)
    assert alpha + beta == beta + alpha
    assert alpha * beta == beta * alpha
    assert (alpha + beta) + gamma == alpha + (beta + gamma)
    assert (alpha * beta) * gamma == alpha * (beta * gamma)
    assert (alpha + beta) * gamma == alpha * gamma + beta * gamma
    assert Ordinals()(2).ordinal_sum(3) == 5
    assert alpha.ordinal_sum(1) != Ordinals()(1).ordinal_sum(alpha)


def test_cardinal_arithmetic_and_order_do_not_assume_continuum_hypothesis() -> None:
    cardinals = Cardinalities()
    assert cardinal(3) + cardinal(5) == cardinal(8)
    assert cardinal(3) * cardinal(5) == cardinal(15)
    assert cardinal(3) ** cardinal(5) == cardinal(243)
    assert aleph0 + continuum == continuum
    assert aleph0 * continuum == continuum
    assert aleph0 ** aleph0 == continuum

    assert cardinals.compare(aleph(1), continuum) is CardinalComparison.LESS_OR_EQUAL
    assert cardinals.Mor(aleph(1), continuum).cardinality() == 1
    assert cardinals.Mor(continuum, aleph(1)).is_empty() is Unknown
    assert cardinals.compare(aleph(2), continuum) is CardinalComparison.INCOMPARABLE
    assert cardinals.Mor(aleph(2), continuum).is_empty() is Unknown
    assert cardinals.Mor(continuum, aleph(2)).is_empty() is Unknown
    with pytest.raises(AssertionError, match="does not decide"):
        cardinals.Mor(continuum, aleph(1)).cardinality()
    assert cardinals.Mor(continuum, aleph0).is_empty() is True
    assert cardinals.Mor(continuum, aleph0).cardinality() == 0
    assert cardinals.Mor(aleph0, continuum).unique_morphism().domain() == aleph0




def test_ordinal_powers_have_ordinal_not_cardinal_exponentiation_size() -> None:
    assert Ordinals()(2).ordinal_power(omega(0)).cardinality() == aleph0
    assert omega(0).ordinal_power(omega(0)).cardinality() == aleph0
    assert Ordinals()(2).ordinal_power(omega(1)).cardinality() == aleph(1)




