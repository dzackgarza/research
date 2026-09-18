from dzack_research.preamble.all import QQ, ProjectiveSpaces, Schemes
from dzack_research.preamble.categories.schemes.gluing import FiniteAtlasRefinement
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    QuasiCoherentSheaves,
)


def _projective_line_with_redundant_overlap_chart():
    line = ProjectiveSpaces(QQ)(1)
    coarse = line.glued_from_standard_charts().gluing_datum()
    left = coarse.chart(0)
    right = coarse.chart(1)
    overlap = coarse.overlap(0, 1)
    whole_overlap = overlap.distinguished_open(overlap.coordinate_algebra().one())

    left_forward = whole_overlap.corestriction(overlap.categorical_identity_morphism())
    left_inverse = whole_overlap.inclusion()
    left_to_overlap = Schemes(QQ).Core().Mor(
        left_forward.domain(), left_forward.codomain()
    )(left_forward, left_inverse)
    right_forward = whole_overlap.corestriction(
        coarse.transition_between(1, 0).forward()
    )
    right_inverse = coarse.transition_between(0, 1).forward() * whole_overlap.inclusion()
    right_to_overlap = Schemes(QQ).Core().Mor(
        right_forward.domain(), right_forward.codomain()
    )(right_forward, right_inverse)
    fine_scheme = Schemes(QQ).glue_affine_atlas(
        (left, right, overlap),
        (
            coarse.transition_between(0, 1),
            left_to_overlap,
            right_to_overlap,
        ),
    )
    fine = fine_scheme.gluing_datum()
    refinement = FiniteAtlasRefinement(
        coarse,
        fine,
        (0, 1, 0),
        (
            left.categorical_identity_morphism(),
            right.categorical_identity_morphism(),
            overlap.inclusion(),
        ),
    )
    return line, coarse, fine, refinement


def test_redundant_projective_line_chart_refines_the_standard_atlas() -> None:
    _line, coarse, fine, refinement = _projective_line_with_redundant_overlap_chart()
    comparison = refinement.comparison_morphism()

    assert comparison.domain() is fine.scheme()
    assert comparison.codomain() is coarse.scheme()
    assert refinement.coarse_index(0) == 0
    assert refinement.coarse_index(1) == 1
    assert refinement.coarse_index(2) == 0
    assert comparison.local_map(2) == coarse.chart_embedding(0) * fine.chart(2).inclusion()

    # The two original coarse charts give a section of the comparison.  On
    # them the composite is literally the identity chart embedding; the third
    # fine chart is the represented overlap already contained in chart zero.
    section = coarse.scheme().Mor(fine.scheme())(
        (fine.chart_embedding(0), fine.chart_embedding(1))
    )
    for index in (0, 1):
        assert comparison * section.local_map(index) == coarse.chart_embedding(index)
    assert (
        section.local_map(0) * fine.chart(2).inclusion()
        == fine.chart_embedding(2)
    )


def test_nontrivial_line_bundle_pulls_back_with_actual_local_isomorphisms() -> None:
    line, coarse, fine, refinement = _projective_line_with_redundant_overlap_chart()
    source_overlap = coarse.overlap(0, 1)
    ratio = source_overlap.inclusion().coordinate_algebra_morphism()(
        line.standard_affine_chart(0).coordinate_algebra().algebra_generator(
            "x1_over_x0"
        )
    )
    bundle = QuasiCoherentSheaves(coarse.scheme()).Invertible().WithChosenTrivialization()(
        coarse,
        {(0, 1): ratio},
    )
    comparison = refinement.pullback_invertible_sheaf(bundle)
    refined = comparison.refined_bundle()

    assert comparison.coarse_bundle() is bundle
    assert refined.gluing_datum() is fine
    assert comparison.scheme_comparison() is refinement.comparison_morphism()
    assert refined.transition_unit(0, 2) == fine.overlap(0, 2).coordinate_algebra().one()
    assert refined.transition_unit(0, 1) == refinement.overlap_map(
        0, 1
    ).coordinate_algebra_morphism()(bundle.transition_unit(0, 1))

    for fine_index in fine.chart_indices():
        local = comparison.local_isomorphism(fine_index)
        assert local.forward().domain().base_ring() is fine.chart(
            fine_index
        ).coordinate_algebra()
        assert local.forward().codomain() is refined.local_module(fine_index)
        local_domain = local.forward().domain()
        assert local.inverse() * local.forward() == local_domain.module_category().Mor(
            local_domain,
            local_domain,
        ).identity()
