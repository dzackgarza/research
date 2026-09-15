from dzack_research.preamble.all import QQ, ProjectiveSpace, Schemes
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasGluedModuleSheaf,
    FiniteAtlasModuleGluingDatum,
    FiniteAtlasRefinement,
)


def _projective_line_with_redundant_overlap_chart():
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
    return coarse, refinement


def _identity_transition(label, domain, codomain):
    position = int(domain.module_generating_set().ranking_map()(label))
    target_label = codomain.module_generating_set()[position]
    return codomain.module_generator(target_label)


def _rank_two_descent(datum):
    local_modules = {
        index: datum.chart(index).coordinate_algebra().free_module(2)
        for index in datum.chart_indices()
    }
    transitions = {
        pair: (_identity_transition, _identity_transition)
        for pair in datum.transition_index_set()
    }
    return FiniteAtlasModuleGluingDatum(datum, local_modules, transitions)


def test_finite_atlas_sheaf_kernel_cokernel_tensor_and_stalk_map_are_chartwise() -> None:
    datum, _refinement = _projective_line_with_redundant_overlap_chart()
    source_datum = _rank_two_descent(datum)
    target_datum = _rank_two_descent(datum)
    source = source_datum.sheaf()
    target = target_datum.sheaf()
    assert isinstance(source, FiniteAtlasGluedModuleSheaf)

    local_maps = {}
    for index in datum.chart_indices():
        module = source.sections_on_chart(index)
        labels = module.module_generating_set()
        local_maps[index] = module.module_category().Mor(module, target.sections_on_chart(index))(
            {
                labels[0]: target.sections_on_chart(index).module_generator(labels[0]),
                labels[1]: target.sections_on_chart(index).zero(),
            }
        )
    morphism = source.morphism_to(target, local_maps)
    kernel = morphism.kernel_sheaf()
    cokernel = morphism.cokernel_sheaf()

    for index in datum.chart_indices():
        assert kernel.sections_on_chart(index).module_rank() == 1
        assert cokernel.sections_on_chart(index).module_rank() == 1
        assert kernel.sections_on_chart(index) is morphism.local_map(index).kernel()
        assert cokernel.sections_on_chart(index) is morphism.local_map(index).cokernel_projection().codomain()

    tensor = source.tensor_product(kernel)
    for index in datum.chart_indices():
        assert tensor.sections_on_chart(index).module_rank() == 2

    first = next(iter(datum.chart_indices()))
    chart = datum.chart(first)
    coordinate_algebra = chart.coordinate_algebra()
    coordinate_label = next(iter(coordinate_algebra.algebra_generating_set()))
    coordinate = coordinate_algebra.algebra_generator(coordinate_label)
    point = chart.underlying_space()(coordinate_algebra.ideal(coordinate))
    stalk_map = morphism.stalk_map(first, point)
    assert stalk_map.domain() is source.stalk_on_chart(first, point)
    assert stalk_map.codomain() is target.stalk_on_chart(first, point)


def test_finite_atlas_sheaf_operations_survive_affine_refinement() -> None:
    datum, refinement = _projective_line_with_redundant_overlap_chart()
    source = _rank_two_descent(datum).sheaf()
    target = _rank_two_descent(datum).sheaf()
    local_maps = {}
    for index in datum.chart_indices():
        module = source.sections_on_chart(index)
        labels = module.module_generating_set()
        local_maps[index] = module.module_category().Mor(module, target.sections_on_chart(index))(
            {
                labels[0]: target.sections_on_chart(index).module_generator(labels[0]),
                labels[1]: target.sections_on_chart(index).zero(),
            }
        )
    kernel = source.morphism_to(target, local_maps).kernel_sheaf()
    refined = kernel.pullback_to_refinement(refinement)

    assert refined.scheme() is refinement.fine_datum().scheme()
    for index in refinement.fine_datum().chart_indices():
        assert refined.sections_on_chart(index).module_rank() == 1
