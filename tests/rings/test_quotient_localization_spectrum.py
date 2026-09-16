from dzack_research.preamble.all import QQ


def test_localization_of_a_presented_domain_has_its_own_affine_spectrum() -> None:
    presentation = QQ.polynomial_ring(("x", "y", "z"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    z = presentation.algebra_generator("z")
    quadric = (presentation).quotient_by_relations((x * y - z**2,))
    xbar = quadric.algebra_generator("x")
    localized = quadric.localization(xbar)

    ambient = (quadric).affine_spectrum(base_ring=QQ)
    open_scheme = ambient.distinguished_open(xbar)
    localization_map = localized.localization_map()

    assert open_scheme.coordinate_algebra() is localized
    assert localized.localization_source() is quadric
    assert localization_map(xbar).is_unit()
    assert open_scheme.inclusion().coordinate_algebra_morphism() is localization_map
    assert open_scheme.inclusion().domain() is open_scheme
    assert open_scheme.inclusion().codomain() is ambient
