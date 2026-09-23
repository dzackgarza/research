r"""Fraction fields as localizations at the nonzero elements."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_localizing_the_integers_at_their_nonzero_elements_gives_the_rationals() -> None:
    r"""(Z - 0)^{-1} Z = Q: the comparison sends the fraction 1/2 to 1/2 and 6/4 to 3/2,
    and is bijective (Atiyah-Macdonald ch. 3)."""
    localization = ZZ.fraction_field_localization()
    comparison = localization.fraction_field_comparison()

    assert comparison(localization.fraction(ZZ(1), ZZ(2))) == QQ(1) / 2
    assert comparison(localization.fraction(ZZ(6), ZZ(4))) == QQ(3) / 2
    assert localization.fraction(ZZ(6), ZZ(4)) == localization.fraction(ZZ(3), ZZ(2))
    assert comparison.is_injective()
    assert comparison.is_surjective()


def test_fraction_fields_of_countable_polynomial_domains_remain_countable() -> None:
    domains = (
        GF(5).polynomial_ring("t"),
        QQ.polynomial_ring("x"),
    )

    for domain in domains:
        field = domain.fraction_field()
        assert field.cardinality() == aleph0
        assert field.regular_module().cardinality() == aleph0


def test_localizing_a_free_module_then_passing_to_q_is_the_base_change_to_q() -> None:
    r"""For M = Z^2 and S = Z - 0, S^{-1}M = M (x)_Z S^{-1}Z = M (x)_Z Q = Q^2
    (Atiyah-Macdonald 3.5)."""
    module = ZZ.free_module(2)
    localization = ZZ.fraction_field_localization()
    localized = localization.localization_functor()(module)
    via_localization = Modules(localization).scalar_extension(localization.fraction_field_comparison())(localized)
    direct = Modules(ZZ).scalar_extension(ZZ.fraction_field_map())(module)

    assert via_localization in VectorSpaces(QQ)
    assert direct in VectorSpaces(QQ)
    assert via_localization.module_rank() == 2
    assert direct.module_rank() == 2
    half_e = direct.scalar_multiple(QQ(1) / 2, direct.module_generator(0))
    assert 2 * half_e == direct.module_generator(0)


def test_selected_and_prime_localizations_do_not_collapse_to_the_fraction_field() -> None:
    at_two = ZZ.localization(ZZ(2))
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
