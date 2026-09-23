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


def test_initial_ordinals_have_the_corresponding_aleph_cardinals() -> None:
    assert omega(0).cardinality() == aleph(0)
    assert omega(3).cardinality() == aleph(3)
    assert omega(omega(1)).cardinality() == aleph(omega(1))
    assert aleph(omega(1)).initial_ordinal() == omega(omega(1))


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


def test_cardinality_is_functorial_on_set_isomorphisms() -> None:
    from dzack_research.preamble.all import ZZ, Sets

    source = Sets.Δ[2]
    target = __import__("dzack_research.preamble.categories.sets", fromlist=["finite_ordered_set"]).finite_ordered_set((ZZ(10), ZZ(20), ZZ(30)))
    forward = Sets().Mor(source, target)(
        lambda value: target(
            (ZZ(10), ZZ(20), ZZ(30))[source.ranking_map()(value)]
        )
    )
    backward = Sets().Mor(target, source)(
        lambda value: source((ZZ(10), ZZ(20), ZZ(30)).index(value))
    )
    core = Sets().Core()
    isomorphism = core.Mor(source, target)(forward, backward)
    cardinality = Sets().cardinality_functor()

    assert cardinality(source) == cardinal(3)
    assert cardinality(target) == cardinal(3)
    image = cardinality(isomorphism)
    assert image.domain() == cardinal(3)
    assert image.codomain() == cardinal(3)


def test_ordinal_powers_have_ordinal_not_cardinal_exponentiation_size() -> None:
    assert Ordinals()(2).ordinal_power(omega(0)).cardinality() == aleph0
    assert omega(0).ordinal_power(omega(0)).cardinality() == aleph0
    assert Ordinals()(2).ordinal_power(omega(1)).cardinality() == aleph(1)


def test_literal_cardinal_equality_rejects_nonintegral_and_infinite_floats() -> None:
    for candidate in (float("inf"), float("nan"), 1.5, -1, "3"):
        assert (cardinal(3) == candidate) is False
        assert candidate not in Ordinals()


def test_natural_product_does_not_recurse_once_per_ordinary_factor() -> None:
    ordinals = Ordinals()
    assert ordinals.natural_product(*(ordinals.one() for _ in range(2000))) == 1
