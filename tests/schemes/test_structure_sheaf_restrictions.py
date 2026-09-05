from __future__ import annotations


def test_distinguished_affine_cover_has_function_restrictions_and_overlap_composition() -> None:
    from dzack_research.preamble.all import QQ, PolynomialRing, Spec

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)

    left, right = cover.opens()
    overlap = cover.overlap(0, 1)
    sheaf = scheme.structure_sheaf()

    assert left.ambient_scheme() is scheme
    assert right.ambient_scheme() is scheme
    assert left.is_distinguished_open()
    assert left.distinguished_open_element() == x
    assert sheaf.sections_on_distinguished_open(left) is left.coordinate_algebra()
    assert sheaf.sections_on_distinguished_open(overlap) is overlap.coordinate_algebra()

    global_to_left = sheaf.restriction_map(scheme, left)
    global_to_overlap = sheaf.restriction_map(scheme, overlap)
    left_to_overlap = cover.structure_sheaf_restriction(0, 1)
    right_to_overlap = cover.structure_sheaf_restriction(1, 0)

    assert left_to_overlap.domain() is left.coordinate_algebra()
    assert left_to_overlap.codomain() is overlap.coordinate_algebra()
    assert right_to_overlap.domain() is right.coordinate_algebra()
    assert right_to_overlap.codomain() is overlap.coordinate_algebra()
    assert left_to_overlap(global_to_left(x)) == global_to_overlap(x)
    assert right_to_overlap(
        sheaf.restriction_map(scheme, right)(x)
    ) == global_to_overlap(x)

    inverse_x = left.coordinate_algebra().fraction(algebra.one(), x)
    assert (
        left_to_overlap(inverse_x) * global_to_overlap(x)
        == overlap.coordinate_algebra().one()
    )


def test_affine_module_sheaf_restriction_is_linear_over_function_restriction() -> None:
    from dzack_research.preamble.all import QQ, FreeModule, PolynomialRing, Spec

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    left = cover.open(0)
    right = cover.open(1)
    overlap = cover.overlap(0, 1)

    module = FreeModule(algebra, 1)
    generator = module.module_generator(0)
    sheaf = scheme.associated_module_sheaf(module)
    left_sections = sheaf.sections_on_distinguished_open(left)
    overlap_sections = sheaf.sections_on_distinguished_open(overlap)
    restriction = sheaf.restriction_map(left, overlap)
    function_restriction = scheme.structure_sheaf().restriction_map(left, overlap)

    assert left_sections.localization_source_module() is module
    assert overlap_sections.localization_source_module() is module
    assert restriction.domain() is left_sections
    assert restriction.codomain().module_over_extension() is overlap_sections
    assert restriction.codomain().ring_map() is function_restriction

    localized_generator = left_sections.fraction(generator)
    inverse_x = left.coordinate_algebra().fraction(algebra.one(), x)
    scaled = left_sections.scalar_multiple(inverse_x, localized_generator)
    restricted_scaled = restriction(scaled).underlying_element()
    expected = overlap_sections.scalar_multiple(
        function_restriction(inverse_x),
        overlap_sections.fraction(generator),
    )
    assert restricted_scaled == expected

    global_to_left = sheaf.restriction_map(scheme, left)
    global_to_right = sheaf.restriction_map(scheme, right)
    global_to_overlap = sheaf.restriction_map(scheme, overlap)
    via_left = restriction(global_to_left(generator).underlying_element())
    via_right = sheaf.restriction_map(right, overlap)(
        global_to_right(generator).underlying_element()
    )
    assert via_left.underlying_element() == global_to_overlap(generator).underlying_element()
    assert via_right.underlying_element() == global_to_overlap(generator).underlying_element()


def test_distinguished_affine_cover_rejects_a_noncover_and_noncontainment() -> None:
    from dzack_research.preamble.all import QQ, PolynomialRing, Spec

    algebra = PolynomialRing(QQ, ("x", "y"))
    x, y = algebra.algebra_generators()
    scheme = Spec(algebra)

    try:
        scheme.distinguished_open_cover(x, y)
    except ValueError as error:
        assert "do not cover" in str(error)
    else:
        raise AssertionError("D(x) and D(y) do not cover the affine plane")

    x_open = scheme.distinguished_open(x)
    y_open = scheme.distinguished_open(y)
    try:
        scheme.structure_sheaf().restriction_map(x_open, y_open)
    except ValueError as error:
        assert "not contained" in str(error)
    else:
        raise AssertionError("D(y) is not contained in D(x)")
