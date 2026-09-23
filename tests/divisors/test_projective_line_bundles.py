r"""Standard projective line bundles use the generic finite-atlas descent owner."""

from dzack_research.preamble.all import (
    QQ,
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


