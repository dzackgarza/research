import pytest

from dzack_research.preamble.all import AffineSpaces, QQ, ProjectiveSpaces, Schemes
from dzack_research.preamble.categories.schemes.gluing import FiniteAffineAtlases
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    QuasiCoherentSheaves,
    zariski_coverage,
)


def _projective_line_with_redundant_overlap_chart():
    line = ProjectiveSpaces(QQ)(1)
    coarse = line.standard_affine_atlas()
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
    fine = FiniteAffineAtlases(line)(
        (left, right, overlap),
        (
            coarse.transition_between(0, 1),
            left_to_overlap,
            right_to_overlap,
        ),
        (
            coarse.chart_embedding(0),
            coarse.chart_embedding(1),
            coarse.chart_embedding(0) * overlap.inclusion(),
        ),
    )
    refinement = FiniteAffineAtlases(line).Mor(fine, coarse)(
        (0, 1, 0),
        (
            left.categorical_identity_morphism(),
            right.categorical_identity_morphism(),
            overlap.inclusion(),
        ),
    )
    return line, coarse, fine, refinement


def test_redundant_projective_line_chart_refines_the_standard_atlas() -> None:
    line, coarse, fine, refinement = _projective_line_with_redundant_overlap_chart()
    comparison = refinement.comparison_morphism()

    assert refinement in FiniteAffineAtlases(line).Mor(fine, coarse)
    assert coarse in zariski_coverage(line)
    assert coarse.coverage() is zariski_coverage(line)
    assert comparison == line.categorical_identity_morphism()
    assert refinement.coarse_index(0) == 0
    assert refinement.coarse_index(1) == 1
    assert refinement.coarse_index(2) == 0
    assert refinement.chart_map(2) == coarse.overlap(0, 1).inclusion()
    assert coarse.chart_embedding(0) * refinement.chart_map(2) == fine.chart_embedding(2)


def test_proper_singleton_open_is_not_a_finite_affine_atlas() -> None:
    line = AffineSpaces(QQ)(1, names=("x",))
    x = line.coordinate_algebra().algebra_generator("x")
    proper_open = line.distinguished_open(x)

    with pytest.raises(ValueError, match="do not jointly cover"):
        FiniteAffineAtlases(line)(
            (proper_open,),
            (),
            (proper_open.inclusion(),),
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
