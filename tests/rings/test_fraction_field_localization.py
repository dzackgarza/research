import pytest

from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    aleph0,
    BasedFreeModule,
    Localization,
    NumberField,
    PolynomialRing,
)
from dzack_research.preamble.categories.functors.module_localization import (
    module_localization_functor,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_fraction_field_is_the_nonzero_localization_with_canonical_realization() -> None:
    nonzero = ZZ.nonzero_multiplicative_submonoid()
    localization = ZZ.fraction_field_localization()

    assert Localization(ZZ, nonzero) is localization
    assert localization.localization_source() is ZZ
    assert localization.base_ring() is ZZ
    assert localization.localization_submonoid() is nonzero
    assert localization.fraction_field_realization() is QQ
    assert ZZ.fraction_field() is QQ
    assert ZZ(0) not in nonzero
    assert ZZ(2) in nonzero

    comparison = localization.fraction_field_comparison()
    inverse = localization.fraction_field_comparison_inverse()
    half = localization.fraction(ZZ(1), ZZ(2))
    assert comparison(half) == QQ(1) / QQ(2)
    assert inverse(comparison(half)) == half



def test_fraction_fields_of_countable_polynomial_domains_remain_countable() -> None:
    domains = (
        PolynomialRing(GF(5), "t"),
        PolynomialRing(QQ, "x"),
    )

    for domain in domains:
        field = domain.fraction_field()
        assert field.cardinality() == aleph0
        assert field.regular_module().cardinality() == aleph0


def test_fraction_field_map_factors_through_the_localization_map() -> None:
    localization = ZZ.fraction_field_localization()
    source_map = localization.localization_map()
    comparison = localization.fraction_field_comparison()
    fraction_map = ZZ.fraction_field_map()

    assert fraction_map.domain() is ZZ
    assert fraction_map.codomain() is QQ
    for integer in (ZZ(-3), ZZ(0), ZZ(5)):
        assert fraction_map(integer) == comparison(source_map(integer))


def test_field_fraction_field_keeps_the_canonical_field_identity() -> None:
    assert QQ.fraction_field() is QQ
    assert QQ.fraction_field_localization() is QQ
    assert QQ.fraction_field_map().is_identity()


def test_module_localization_and_fraction_scalar_change_have_the_same_generic_fibre() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("e", "f")))
    localization = ZZ.fraction_field_localization()
    localized = module_localization_functor(localization)(module)
    to_field = Modules(localization).scalar_extension(
        localization.fraction_field_comparison()
    )
    via_localization = to_field(localized)
    direct = Modules(ZZ).scalar_extension(ZZ.fraction_field_map())(module)

    assert via_localization.base_ring() is QQ
    assert direct.base_ring() is QQ
    assert via_localization.module_rank() == direct.module_rank() == 2


def test_selected_and_prime_localizations_do_not_collapse_to_the_fraction_field() -> None:
    at_two = Localization(ZZ, ZZ(2))
    at_three = ZZ.spectrum()(3).local_ring()
    fractions = ZZ.fraction_field_localization()

    assert at_two is not fractions
    assert at_three is not fractions
    assert at_two(ZZ(2)).is_unit()
    assert not at_two(ZZ(3)).is_unit()
    assert at_three(ZZ(2)).is_unit()
    assert not at_three(ZZ(3)).is_unit()
    assert fractions(ZZ(2)).is_unit()
    assert fractions(ZZ(3)).is_unit()


def test_zero_divisor_ring_does_not_use_the_fraction_field_specialization() -> None:
    quotient = ZZ.quotient_ring(ZZ.ideal(6))

    with pytest.raises(ValueError, match="not an integral domain"):
        quotient.fraction_field()


def test_number_field_order_keeps_its_canonical_fraction_field() -> None:
    polynomial_ring = PolynomialRing(QQ, "x")
    x = polynomial_ring.algebra_generator("x")
    field = NumberField(x**2 - 5, "a")
    order = field.ring_of_integers()

    localization = order.fraction_field_localization()
    assert order.fraction_field() is field
    assert localization.fraction_field_realization() is field
    assert order.fraction_field_map().codomain() is field
