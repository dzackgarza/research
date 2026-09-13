from dzack_research.preamble.all import PolynomialRing, QQ


def test_localization_units_use_ideal_saturation_over_multivariate_polynomials() -> None:
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    localized = ring.localization(x)
    localization = localized.localization_map()

    inverted = localization(x)
    uninverted = localization(y)

    assert inverted.is_unit()
    assert inverted * inverted.inverse_of_unit() == localized.one()
    assert not uninverted.is_unit()


def test_localizing_at_a_product_makes_each_factor_a_unit() -> None:
    ring = PolynomialRing(QQ, ("s0", "s1"))
    s0 = ring.algebra_generator("s0")
    s1 = ring.algebra_generator("s1")
    localized = ring.localization(s0 * s1)
    localization = localized.localization_map()

    for numerator in (s0, s1, s0**2, s0 * s1):
        unit = localization(numerator)
        assert unit.is_unit()
        assert unit * unit.inverse_of_unit() == localized.one()

    assert not localization(s0 + s1).is_unit()

