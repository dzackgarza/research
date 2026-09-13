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
