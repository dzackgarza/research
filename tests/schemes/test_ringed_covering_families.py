from dzack_research.preamble.all import QQ, AffineSpace, Schemes
from dzack_research.preamble.categories.schemes.covering_families import (
    RingedCoveringFamily,
)
from dzack_research.preamble.categories.schemes.gluing import FiniteAtlasRefinement
from dzack_research.preamble.categories.schemes.schemes import AffineSchemes


def _punctured_plane_covering_family():
    plane = AffineSpace(2, QQ, names=("x", "y"))
    algebra = plane.coordinate_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    origin = plane.closed_subscheme(x, y)
    punctured = origin.open_complement()
    family = plane.covering_family(
        {"whole": plane, "punctured": punctured},
        {
            "whole": plane.categorical_identity_morphism(),
            "punctured": punctured.inclusion(),
        },
        {
            ("whole", "punctured"): (
                punctured,
                punctured.inclusion(),
                punctured.categorical_identity_morphism(),
            )
        },
        ambient_chart_index="whole",
    )
    return plane, punctured, family


def _redundant_third_chart_refinement(coarse):
    indices = tuple(coarse.chart_indices())
    left_index, right_index = indices
    left = coarse.chart(left_index)
    right = coarse.chart(right_index)
    overlap = coarse.overlap(left_index, right_index)
    whole_overlap = overlap.distinguished_open(overlap.coordinate_algebra().one())
    left_forward = whole_overlap.corestriction(overlap.categorical_identity_morphism())
    left_inverse = whole_overlap.inclusion()
    left_to_overlap = Schemes(QQ).Core().Mor(
        left_forward.domain(), left_forward.codomain()
    )(left_forward, left_inverse)
    right_forward = whole_overlap.corestriction(
        coarse.transition_between(right_index, left_index).forward()
    )
    right_inverse = (
        coarse.transition_between(left_index, right_index).forward()
        * whole_overlap.inclusion()
    )
    right_to_overlap = Schemes(QQ).Core().Mor(
        right_forward.domain(), right_forward.codomain()
    )(right_forward, right_inverse)
    fine = Schemes(QQ).glue_affine_atlas(
        (left, right, overlap),
        (
            coarse.transition_between(left_index, right_index),
            left_to_overlap,
            right_to_overlap,
        ),
    ).gluing_datum()
    return FiniteAtlasRefinement(
        coarse,
        fine,
        (left_index, right_index, left_index),
        (
            left.categorical_identity_morphism(),
            right.categorical_identity_morphism(),
            overlap.inclusion(),
        ),
    )


def test_punctured_plane_is_retained_as_a_nonaffine_overlap_with_two_embeddings() -> None:
    plane, punctured, family = _punctured_plane_covering_family()

    assert isinstance(family, RingedCoveringFamily)
    assert family.ambient_space() is plane
    overlap = family.overlap("whole", "punctured")
    assert overlap.space() is punctured
    assert overlap.left_embedding() is punctured.inclusion()
    assert overlap.right_embedding() == punctured.categorical_identity_morphism()
    assert punctured not in AffineSchemes(QQ)
    assert (
        family.embedding("whole") * overlap.left_embedding()
        == family.embedding("punctured") * overlap.right_embedding()
    )


def test_nonaffine_overlap_has_affine_refinement_with_both_cover_embeddings() -> None:
    plane, punctured, family = _punctured_plane_covering_family()
    overlap = family.overlap("whole", "punctured")
    refinement = overlap.affine_refinement()

    assert refinement.overlap() is overlap
    assert refinement.atlas_datum() is punctured.gluing_datum()
    assert refinement.comparison_to_overlap() == punctured.categorical_identity_morphism()
    assert refinement.atlas_datum().number_of_charts() == 2
    for index in refinement.chart_indices():
        assert refinement.left_embedding(index).codomain() is plane
        assert refinement.right_embedding(index).codomain() is punctured
        assert (
            family.embedding("whole") * refinement.left_embedding(index)
            == family.embedding("punctured") * refinement.right_embedding(index)
        )


def test_overlap_refinement_comparison_keeps_chart_labels_and_embeddings() -> None:
    plane, punctured, family = _punctured_plane_covering_family()
    overlap = family.overlap("whole", "punctured")
    coarse = overlap.affine_refinement()
    atlas_refinement = _redundant_third_chart_refinement(coarse.atlas_datum())
    fine = coarse.refined_by(atlas_refinement)

    assert fine.coarse_refinement() is coarse
    assert fine.atlas_refinement() is atlas_refinement
    assert fine.comparison_to_overlap().domain() is atlas_refinement.fine_scheme()
    assert fine.comparison_to_overlap().codomain() is punctured
    assert fine.atlas_datum().number_of_charts() == 3
    for index in fine.chart_indices():
        assert fine.left_embedding(index).codomain() is plane
        assert fine.right_embedding(index).codomain() is punctured
        assert (
            family.embedding("whole") * fine.left_embedding(index)
            == family.embedding("punctured") * fine.right_embedding(index)
        )
