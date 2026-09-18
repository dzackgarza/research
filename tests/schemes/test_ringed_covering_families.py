from dzack_research.preamble.all import QQ, AffineSpaces, Schemes
from dzack_research.preamble.categories.abstract_categories.presheaves import CoveringFamilies
from dzack_research.preamble.categories.schemes.gluing import FiniteAffineAtlases
from dzack_research.preamble.categories.schemes.ringed_spaces import LocallyRingedSpaces
from dzack_research.preamble.categories.schemes.schemes import AffineSchemes


def _punctured_plane_covering_family():
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
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


def _redundant_third_chart_refinement(punctured, coarse):
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
    fine = FiniteAffineAtlases(punctured)(
        (left, right, overlap),
        (
            coarse.transition_between(left_index, right_index),
            left_to_overlap,
            right_to_overlap,
        ),
        (
            coarse.chart_embedding(left_index),
            coarse.chart_embedding(right_index),
            coarse.chart_embedding(left_index) * overlap.inclusion(),
        ),
    )
    refinement = FiniteAffineAtlases(punctured).Mor(fine, coarse)(
        (left_index, right_index, left_index),
        (
            left.categorical_identity_morphism(),
            right.categorical_identity_morphism(),
            overlap.inclusion(),
        ),
    )
    return fine, refinement


def test_punctured_plane_cover_is_a_covering_family_in_the_slice() -> None:
    plane, punctured, family = _punctured_plane_covering_family()
    site = LocallyRingedSpaces().SliceCategory(plane)

    assert family in CoveringFamilies(site)
    assert family.target().arrow() == plane.categorical_identity_morphism()
    assert family.member("whole").domain().arrow().domain() is plane
    assert family.member("punctured").domain().arrow().domain() is punctured
    assert punctured not in AffineSchemes(QQ)

    overlap = family.overlap_span("whole", "punctured")
    assert overlap.apex().arrow().domain() is punctured
    assert overlap.left_leg().left() == punctured.inclusion()
    assert overlap.right_leg().left() == punctured.categorical_identity_morphism()
    assert (
        family.member("whole") * overlap.left_leg()
        == family.member("punctured") * overlap.right_leg()
    )


def test_nonaffine_overlap_uses_its_owned_finite_affine_atlas() -> None:
    plane, punctured, family = _punctured_plane_covering_family()
    overlap = family.overlap_span("whole", "punctured")
    atlas = punctured.finite_affine_atlas()

    assert atlas in FiniteAffineAtlases(punctured)
    assert atlas.target().arrow() == punctured.categorical_identity_morphism()
    for index in atlas.chart_indices():
        left_embedding = overlap.left_leg().left() * atlas.chart_embedding(index)
        right_embedding = overlap.right_leg().left() * atlas.chart_embedding(index)
        assert left_embedding.codomain() is plane
        assert right_embedding.codomain() is punctured
        assert (
            family.member("whole").left() * left_embedding
            == family.member("punctured").left() * right_embedding
        )


def test_overlap_atlas_refinement_is_an_owned_covering_family_morphism() -> None:
    _plane, punctured, _family = _punctured_plane_covering_family()
    coarse = punctured.finite_affine_atlas()
    fine, refinement = _redundant_third_chart_refinement(punctured, coarse)

    assert refinement in FiniteAffineAtlases(punctured).Mor(fine, coarse)
    assert refinement.comparison_morphism() == punctured.categorical_identity_morphism()
    assert fine.number_of_charts() == 3
    for index in fine.chart_indices():
        assert (
            coarse.chart_embedding(refinement.coarse_index(index))
            * refinement.chart_map(index)
            == fine.chart_embedding(index)
        )
