from dzack_research.preamble.all import ProjectiveSpace, QQ, Schemes
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.divisors.invertible_sheaves import (
    FiniteAtlasInvertibleSheaf,
)
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasModuleGluingDatum,
    FiniteAtlasRefinement,
    compare_finite_atlas_line_bundle_pullback,
    finite_atlas_module_pullback_functor,
)


def _projective_line_refinement():
    line = ProjectiveSpace(1, QQ)
    coarse = line.glued_from_standard_charts().gluing_datum()
    left = coarse.chart(0)
    right = coarse.chart(1)
    overlap = coarse.overlap(0, 1)
    whole_overlap = overlap.distinguished_open(overlap.coordinate_algebra().one())
    left_to_overlap = Isomorphism(
        whole_overlap.corestriction(overlap.categorical_identity_morphism()),
        whole_overlap.inclusion(),
    )
    right_to_overlap = Isomorphism(
        whole_overlap.corestriction(coarse.transition_between(1, 0).forward()),
        coarse.transition_between(0, 1).forward() * whole_overlap.inclusion(),
    )
    fine = Schemes(QQ).glue_affine_atlas(
        (left, right, overlap),
        (
            coarse.transition_between(0, 1),
            left_to_overlap,
            right_to_overlap,
        ),
    ).gluing_datum()
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
    return coarse, fine, refinement


def _identity_transition(label, domain, codomain):
    position = int(domain.module_generating_set().ranking_map()(label))
    target_label = codomain.module_generating_set()[position]
    return codomain.module_generator(target_label)


def _rank_one_sheaf(datum):
    local_modules = {
        index: FreeModule(datum.chart(index).coordinate_algebra(), 1)
        for index in datum.chart_indices()
    }
    transitions = {
        pair: (_identity_transition, _identity_transition)
        for pair in datum.transition_index_set()
    }
    return FiniteAtlasModuleGluingDatum(datum, local_modules, transitions).sheaf()


def _scalar_morphism(source, target, scalar):
    local_maps = {}
    datum = source.atlas_datum()
    for index in datum.chart_indices():
        domain = source.sections_on_chart(index)
        codomain = target.sections_on_chart(index)
        source_label = domain.module_generating_set()[0]
        target_label = codomain.module_generating_set()[0]
        local_maps[index] = module_homset(domain, codomain)(
            {
                source_label: codomain.scalar_multiple(
                    codomain.base_ring()(scalar),
                    codomain.module_generator(target_label),
                )
            }
        )
    return source.morphism_to(target, local_maps)


def test_inverse_image_and_module_pullback_keep_the_structural_map_distinct() -> None:
    coarse, fine, refinement = _projective_line_refinement()
    source = _rank_one_sheaf(coarse)
    pullback = finite_atlas_module_pullback_functor(refinement)
    inverse_image = pullback.inverse_image(source)
    pulled = inverse_image.module_pullback()

    assert inverse_image.scheme_morphism() is refinement.comparison_morphism()
    assert inverse_image.scheme() is fine.scheme()
    for fine_index in fine.chart_indices():
        coarse_index = refinement.coarse_index(fine_index)
        assert inverse_image.source_local_module(fine_index) is source.sections_on_chart(
            coarse_index
        )
        assert inverse_image.structural_ring_map(fine_index) == refinement.chart_map(
            fine_index
        ).coordinate_algebra_morphism()
        assert pulled.sections_on_chart(fine_index).base_ring() is fine.chart(
            fine_index
        ).coordinate_algebra()
        assert pulled.sections_on_chart(fine_index) is not inverse_image.source_local_module(
            fine_index
        )


def test_module_pullback_preserves_nonidentity_maps_identity_and_composition() -> None:
    coarse, fine, refinement = _projective_line_refinement()
    source = _rank_one_sheaf(coarse)
    middle = _rank_one_sheaf(coarse)
    target = _rank_one_sheaf(coarse)
    times_two = _scalar_morphism(source, middle, 2)
    times_three = _scalar_morphism(middle, target, 3)
    composite = times_three * times_two
    pullback = finite_atlas_module_pullback_functor(refinement)

    pulled_two = pullback.on_morphism(times_two)
    pulled_three = pullback.on_morphism(times_three)
    pulled_composite = pullback.on_morphism(composite)
    assert pulled_three * pulled_two == pulled_composite

    identity = source.gluing_datum().identity_morphism()
    pulled_identity = pullback.on_morphism(identity)
    assert pulled_identity == pullback.on_object(source).gluing_datum().identity_morphism()

    for fine_index in fine.chart_indices():
        module = pulled_composite.source().local_module(fine_index)
        label = module.module_generating_set()[0]
        image = pulled_composite.local_map(fine_index)(module.module_generator(label))
        codomain = pulled_composite.target().local_module(fine_index)
        target_label = codomain.module_generating_set()[0]
        assert image == codomain.scalar_multiple(
            codomain.base_ring()(6), codomain.module_generator(target_label)
        )


def test_inverse_image_functor_preserves_composition_before_scalar_extension() -> None:
    coarse, _fine, refinement = _projective_line_refinement()
    source = _rank_one_sheaf(coarse)
    middle = _rank_one_sheaf(coarse)
    target = _rank_one_sheaf(coarse)
    times_two = _scalar_morphism(source, middle, 2)
    times_three = _scalar_morphism(middle, target, 3)
    pullback = finite_atlas_module_pullback_functor(refinement)

    inverse_two = pullback.inverse_image_morphism(times_two)
    inverse_three = pullback.inverse_image_morphism(times_three)
    inverse_composite = pullback.inverse_image_morphism(times_three * times_two)
    composed = inverse_three * inverse_two

    for fine_index in refinement.fine_datum().chart_indices():
        assert composed.local_map(fine_index) == inverse_composite.local_map(fine_index)


def test_generic_module_pullback_agrees_with_transition_unit_line_bundle_pullback() -> None:
    coarse, fine, refinement = _projective_line_refinement()
    source_overlap = coarse.overlap(0, 1)
    ratio = source_overlap.inclusion().coordinate_algebra_morphism()(
        coarse.chart(0).coordinate_algebra().algebra_generator("x1_over_x0")
    )
    bundle = FiniteAtlasInvertibleSheaf(coarse, {(0, 1): ratio})
    comparison = compare_finite_atlas_line_bundle_pullback(refinement, bundle)
    generic = comparison.generic_pullback().gluing_datum()
    specialized = comparison.specialized_module_sheaf().gluing_datum()

    assert comparison.line_bundle() is bundle
    assert comparison.line_bundle_refinement().refined_bundle().gluing_datum() is fine
    assert comparison.inverse() * comparison.forward() == generic.identity_morphism()
    assert comparison.forward() * comparison.inverse() == specialized.identity_morphism()

    for fine_index in fine.chart_indices():
        forward = comparison.forward().local_map(fine_index)
        assert forward.domain() is generic.local_module(fine_index)
        assert forward.codomain() is specialized.local_module(fine_index)

    refined_bundle = comparison.line_bundle_refinement().refined_bundle()
    assert refined_bundle.transition_unit(0, 1) == refinement.overlap_map(
        0, 1
    ).coordinate_algebra_morphism()(bundle.transition_unit(0, 1))
