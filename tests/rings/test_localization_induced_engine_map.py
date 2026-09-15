from dzack_research.preamble.all import PolynomialRing, QQ, CommutativeAlgebras


def test_localization_induced_map_retains_a_native_realization() -> None:
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    localized_x = ring.localization(x)
    localized_xy = ring.localization(x, y)

    induced = localized_x.induced_morphism(localized_xy.localization_map())
    on_spectra = CommutativeAlgebras(QQ).spectrum()(induced)

    assert induced(localized_x.localization_map()(x)).is_unit()
    assert induced(localized_x.localization_map()(y)) == localized_xy.localization_map()(y)
    assert on_spectra.coordinate_algebra_morphism() is induced
