r"""Formal spectra retain the inverse system, not a computational precision."""

from dzack_research.preamble.all import QQ


def test_formal_spectrum_is_distinct_from_completion_and_its_finite_stages() -> None:
    ring = QQ.polynomial_ring("t")
    t = ring.algebra_generator("t")
    formal = ring.formal_spectrum(ring.ideal(t))
    from dzack_research.preamble.categories.abstract_categories.products import DirectedSystem
    from dzack_research.preamble.categories.sets.set_categories import NN

    system = formal.functor()
    assert formal in DirectedSystem(system.base_index_category(), system.codomain())
    assert formal.category() is system.system_category()
    second = formal.thickening_ring(2)
    third = formal.thickening_ring(3)
    transition = formal.transition_ring_map(3, 2)

    assert formal.source_ring() is ring
    assert formal.thickening(2) is not formal
    assert formal.completed_affine_scheme(4) is not formal
    assert transition.domain() is third
    assert transition.codomain() is second
    assert transition(third.quotient_map()(t)) == second.quotient_map()(t)
    lower = system.base_index_category()(NN(1))
    higher = system.base_index_category()(NN(2))
    restriction = system(system.base_index_category().Mor(lower, higher).unique())
    assert formal.base_index_category() is system.base_index_category()
    assert formal.stage(lower) is formal.thickening(2)
    assert formal.transition(system.base_index_category().Mor(lower, higher).unique()) is restriction
    assert restriction.domain() is formal.thickening(2)
    assert restriction.codomain() is formal.thickening(3)


def test_precision_changes_only_the_completion_realization_not_the_formal_object() -> None:
    ring = QQ.polynomial_ring("t")
    t = ring.algebra_generator("t")
    formal = ring.formal_spectrum(ring.ideal(t))
    comparison = formal.compare_precisions(3, 7)
    third_stage = formal.thickening_ring(3)

    assert comparison.domain() is formal.completion(3)
    assert comparison.codomain() is formal.completion(7)
    assert comparison.domain().computation_precision() == 3
    assert comparison.codomain().computation_precision() == 7
    assert formal.completion_projection(3, 3).codomain() is third_stage
    assert formal.completion_projection(7, 3).codomain() is third_stage
    assert comparison.forward().domain() is comparison.domain()
    assert comparison.forward().codomain() is comparison.codomain()


def test_continuous_formal_map_descends_compatibly_to_every_thickening() -> None:
    source = QQ.polynomial_ring("x")
    target = QQ.polynomial_ring("y")
    x = source.algebra_generator("x")
    y = target.algebra_generator("y")
    formal_source = source.formal_spectrum(source.ideal(x))
    formal_target = target.formal_spectrum(target.ideal(y))
    ring_map = target.Mor(source).elementwise(lambda polynomial: source(polynomial(y=x)))
    morphism = formal_source.morphism_to(formal_target, ring_map)
    stage = morphism.thickening_ring_map(3)

    assert morphism.parent() is formal_source.category().Mor(formal_source, formal_target)
    assert morphism.domain() is formal_source
    assert morphism.codomain() is formal_target
    assert stage.domain() is formal_target.thickening_ring(3)
    assert stage.codomain() is formal_source.thickening_ring(3)
    assert stage(stage.domain().quotient_map()(y)) == stage.codomain().quotient_map()(x)
    stage_scheme_map = morphism.thickening_morphism(3)
    assert stage_scheme_map.domain() is formal_source.thickening(3)
    assert stage_scheme_map.codomain() is formal_target.thickening(3)
    assert morphism.completed_ring_map(4, 6).domain() is formal_target.completion(6)
    assert morphism.completed_ring_map(4, 6).codomain() is formal_source.completion(4)
