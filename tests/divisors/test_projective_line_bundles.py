r"""Standard projective line bundles use the generic finite-atlas descent owner."""

from dzack_research.preamble.all import (
    QQ,
    FiniteAtlasInvertibleSheaf,
    ProjectiveSpaces,
    Schemes,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.schemes.ringed_spaces import QuasiCoherentSheaves

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_base_change_and_bundles.sage",
    "live_owner": "tests/divisors/test_projective_line_bundles.py",
    "disposition": "reconciled-live-owner",
}


def test_projective_O_one_is_descent_on_the_actual_projective_space() -> None:
    line = ProjectiveSpaces(QQ)(1)
    bundle = line.O(1)
    atlas = bundle.gluing_datum()
    overlap = atlas.overlap(0, 1)
    ratio = overlap.inclusion().coordinate_algebra_morphism()(
        line._standard_chart_coordinate(0, 1)
    )

    assert isinstance(bundle, FiniteAtlasInvertibleSheaf)
    assert bundle in QuasiCoherentSheaves(line).Invertible()
    assert bundle in QuasiCoherentSheaves(line).Invertible().WithChosenTrivialization()
    assert bundle.trivializing_cover() is atlas
    assert bundle.scheme() is line
    assert atlas.scheme() is line
    assert atlas.chart_embedding(0).codomain() is line
    assert bundle.degree() == 1
    assert bundle.transition_unit(0, 1) == ratio
    assert bundle.global_sections().module_rank() == 2
    assert bundle.is_ample()
    assert bundle.is_basepoint_free()


def test_projective_line_bundle_tensor_dual_and_canonical_degrees_are_exact() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    hyperplane = plane.O(1)
    square = hyperplane.tensor_power(2)
    dual = hyperplane.dual_sheaf()

    assert hyperplane.tensor_product(hyperplane).degree() == 2
    assert square.degree() == 2
    assert dual.degree() == -1
    assert hyperplane.tensor_product(dual).degree() == 0
    assert not dual.is_ample()
    assert not dual.is_basepoint_free()
    assert plane.canonical_line_bundle().degree() == -3
    assert plane.anticanonical_line_bundle().degree() == 3


def test_projective_section_multiplication_is_polynomial_multiplication_on_actual_modules() -> None:
    line = ProjectiveSpaces(QQ)(1)
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
    line = ProjectiveSpaces(QQ)(1)
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
    )

    line = ProjectiveSpaces(QQ)(1)
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
    comparison = refinement.compare_line_bundle_pullback(bundle)
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


def test_projective_closed_subscheme_restriction_is_the_closed_immersion_pullback_image() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    x, y, z = plane.homogeneous_coordinate_generators()
    conic = plane.closed_subscheme(x * z - y**2)
    inclusion = conic.inclusion()
    bundle = plane.O(2)

    restricted = bundle.restrict_to(conic)

    assert restricted is inclusion.module_pullback(bundle)
    assert restricted in QuasiCoherentSheaves(conic)
    assert restricted in QuasiCoherentSheaves(conic).Invertible()
    assert restricted not in (
        QuasiCoherentSheaves(conic).Invertible().WithChosenTrivialization()
    )
    assert restricted.pullback_morphism() is inclusion
    assert restricted.ambient_line_bundle() is bundle
    assert restricted.degree() == 2


def test_restricted_projective_line_bundle_comparison_is_a_quasi_coherent_isomorphism() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    x, y, z = plane.homogeneous_coordinate_generators()
    conic = plane.closed_subscheme(x * z - y**2)
    left = plane.O(1).restrict_to(conic)
    right = plane.O(1).restrict_to(conic)

    comparison = left.canonical_isomorphism_to(right)
    sheaves = QuasiCoherentSheaves(conic)

    assert comparison in sheaves.Core().Mor(left, right)
    assert comparison.forward() in sheaves.Mor(left, right)
    assert comparison.inverse() in sheaves.Mor(right, left)
    assert comparison.forward().ambient_morphism().domain() is left.ambient_line_bundle()
    assert comparison.forward().ambient_morphism().codomain() is right.ambient_line_bundle()


def test_projection_pullback_places_degree_in_the_selected_product_factor() -> None:
    labels = finite_ordered_set(("left", "right"))
    line = ProjectiveSpaces(QQ)(1)
    product = Schemes(QQ).product(indexed_family(labels, lambda _label: line))
    projection = product.projection("left")
    bundle = line.O(2)

    pulled = bundle.pullback(projection)
    section_pullback = bundle.global_sections().pullback(projection)

    assert pulled.projective_product() is product
    assert pulled.multidegree().index_set() is labels
    assert pulled.multidegree()["left"] == 2
    assert pulled.multidegree()["right"] == 0
    assert section_pullback.domain() is bundle.global_sections()
    assert section_pullback.codomain() is pulled.global_sections()
    assert section_pullback.is_injective()
    assert section_pullback.domain().module_rank() == section_pullback.codomain().module_rank() == 3


def test_identity_base_change_preserves_projective_dimension_and_bundle_degree() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    identity = QQ.Mor(QQ).identity()
    changed_plane = plane.base_change(identity)
    changed_bundle = plane.O(1).base_change(identity)

    assert changed_plane.relative_dimension() == plane.relative_dimension() == 2
    assert changed_bundle.degree() == 1
    assert changed_bundle.scheme() is changed_plane
    assert changed_bundle.base_change_projection().codomain() is plane
