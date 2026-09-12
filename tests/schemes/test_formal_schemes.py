r"""Formal spectra retain the inverse system, not a computational precision."""

from dzack_research.preamble.all import QQ, PolynomialRing
from dzack_research.preamble.categories.rings.ring_foundation import ring_homset
from dzack_research.preamble.categories.schemes.formal_schemes import (
    formal_affine_morphism,
    formal_spectrum,
)


def test_formal_spectrum_is_distinct_from_completion_and_its_finite_stages() -> None:
    ring = PolynomialRing(QQ, "t")
    t = ring.algebra_generator("t")
    formal = formal_spectrum(ring, ring.ideal(t))
    second = formal.thickening_ring(2)
    third = formal.thickening_ring(3)
    transition = formal.transition_ring_map(3, 2)

    assert formal.source_ring() is ring
    assert formal.thickening(2) is not formal
    assert formal.completed_affine_scheme(4) is not formal
    assert transition.domain() is third
    assert transition.codomain() is second
    assert transition(third.quotient_map()(t)) == second.quotient_map()(t)


def test_precision_changes_only_the_completion_realization_not_the_formal_object() -> None:
    ring = PolynomialRing(QQ, "t")
    t = ring.algebra_generator("t")
    formal = formal_spectrum(ring, ring.ideal(t))
    comparison = formal.compare_precisions(3, 7)
    third_stage = formal.thickening_ring(3)

    assert comparison.formal_spectrum() is formal
    assert comparison.first_completion().computation_precision() == 3
    assert comparison.second_completion().computation_precision() == 7
    assert formal.completion_projection(3, 3).codomain() is third_stage
    assert formal.completion_projection(7, 3).codomain() is third_stage
    assert comparison.forward().domain() is comparison.first_completion()
    assert comparison.forward().codomain() is comparison.second_completion()


def test_continuous_formal_map_descends_compatibly_to_every_thickening() -> None:
    source = PolynomialRing(QQ, "x")
    target = PolynomialRing(QQ, "y")
    x = source.algebra_generator("x")
    y = target.algebra_generator("y")
    formal_source = formal_spectrum(source, source.ideal(x))
    formal_target = formal_spectrum(target, target.ideal(y))
    ring_map = ring_homset(target, source).elementwise(lambda polynomial: source(polynomial(y=x)))
    morphism = formal_affine_morphism(formal_source, formal_target, ring_map)
    stage = morphism.thickening_ring_map(3)

    assert stage.domain() is formal_target.thickening_ring(3)
    assert stage.codomain() is formal_source.thickening_ring(3)
    assert stage(stage.domain().quotient_map()(y)) == stage.codomain().quotient_map()(x)
    assert morphism.completed_ring_map(4, 6).domain() is formal_target.completion(6)
    assert morphism.completed_ring_map(4, 6).codomain() is formal_source.completion(4)
