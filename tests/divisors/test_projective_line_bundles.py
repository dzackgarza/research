r"""Standard projective line bundles use the generic finite-atlas descent owner."""

from dzack_research.preamble.all import (
    FiniteAtlasInvertibleSheaf,
    ProjectiveSpace,
    QQ,
)


def test_projective_O_one_is_descent_on_the_actual_projective_space() -> None:
    line = ProjectiveSpace(1, QQ)
    bundle = line.O(1)
    atlas = bundle.gluing_datum()
    overlap = atlas.overlap(0, 1)
    ratio = overlap.inclusion().coordinate_algebra_morphism()(
        line._standard_chart_coordinate(0, 1)
    )

    assert isinstance(bundle, FiniteAtlasInvertibleSheaf)
    assert bundle.scheme() is line
    assert atlas.scheme() is line
    assert atlas.chart_embedding(0).codomain() is line
    assert bundle.degree() == 1
    assert bundle.transition_unit(0, 1) == ratio
    assert bundle.global_sections().module_rank() == 2
    assert bundle.is_ample()
    assert bundle.is_basepoint_free()


def test_projective_line_bundle_tensor_dual_and_canonical_degrees_are_exact() -> None:
    plane = ProjectiveSpace(2, QQ)
    hyperplane = plane.O(1)
    square = hyperplane.tensor_power(2)
    dual = hyperplane.dual()

    assert hyperplane.tensor_product(hyperplane).degree() == 2
    assert square.degree() == 2
    assert dual.degree() == -1
    assert hyperplane.tensor_product(dual).degree() == 0
    assert not dual.is_ample()
    assert not dual.is_basepoint_free()
    assert plane.canonical_line_bundle().degree() == -3
    assert plane.anticanonical_line_bundle().degree() == 3


def test_projective_section_multiplication_is_polynomial_multiplication_on_actual_modules() -> None:
    line = ProjectiveSpace(1, QQ)
    linear = line.O(1)
    quadratic = line.O(2)
    multiplication = linear.section_multiplication(linear)
    comparison = quadratic.homogeneous_polynomial_comparison()
    labels = tuple(linear.global_sections().module_generating_set())
    x0 = linear.global_sections().module_generator(labels[0])
    x1 = linear.global_sections().module_generator(labels[1])

    product = multiplication(x0, x1)

    assert multiplication.left_factor() is linear.global_sections()
    assert multiplication.right_factor() is linear.global_sections()
    assert multiplication.codomain() is quadratic.global_sections()
    assert product.parent() is quadratic.global_sections()
    assert comparison.forward()(product) == product
    assert product != quadratic.global_sections().zero()


def test_projective_line_bundle_base_change_retains_projection_and_section_comparison() -> None:
    from dzack_research.preamble.all import QuadraticField

    field = QuadraticField(2, "s")
    ring_map = QQ.Mor(field)(lambda element: field(element))
    line = ProjectiveSpace(1, QQ)
    bundle = line.O(2)

    changed = bundle.base_change(ring_map)
    comparison = changed.section_base_change_comparison()

    assert changed.scheme().scheme_base_ring() is field
    assert changed.base_change_source_bundle() is bundle
    assert changed.base_change_projection() is changed.scheme().left_projection()
    assert changed.base_change_projection().codomain() is line
    assert comparison.forward().domain().base_ring() is field
    assert comparison.forward().codomain() is changed.global_sections()
    assert comparison.forward().domain().module_rank() == changed.global_sections().module_rank()


def test_projective_O_pullback_uses_generic_finite_atlas_refinement() -> None:
    from dzack_research.preamble.categories.schemes.gluing import (
        FiniteAtlasRefinement,
        compare_finite_atlas_line_bundle_pullback,
    )

    line = ProjectiveSpace(1, QQ)
    bundle = line.O(1)
    coarse = bundle.gluing_datum()
    fine = coarse.presentation()
    indices = tuple(coarse.chart_indices())
    refinement = FiniteAtlasRefinement(
        coarse,
        fine,
        {index: index for index in indices},
        {
            index: coarse.chart(index).categorical_identity_morphism()
            for index in indices
        },
    )
    comparison = compare_finite_atlas_line_bundle_pullback(refinement, bundle)
    pulled = comparison.line_bundle_refinement().refined_bundle()

    assert refinement.comparison_morphism().domain() is fine.scheme()
    assert refinement.comparison_morphism().codomain() is line
    assert refinement.comparison_morphism().domain() is not line
    assert comparison.line_bundle() is bundle
    assert pulled.scheme() is fine.scheme()
    assert pulled.gluing_datum() is fine
    for index in fine.chart_indices():
        local = comparison.line_bundle_refinement().local_isomorphism(index)
        assert local.forward().domain().base_ring() is fine.chart(index).coordinate_algebra()
        assert local.forward().codomain() is pulled.local_module(index)
