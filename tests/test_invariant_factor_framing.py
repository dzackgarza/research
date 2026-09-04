from dzack_research.preamble.all import BasedFreeModule, Lattices, ZZ, module_homset
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_literal_cokernel_retains_generator_killed_by_the_relation() -> None:
    target = BasedFreeModule(ZZ, finite_ordered_set(("v", "w")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    quotient = module_homset(relations, target)(
        {"r": target.module_generator("w")}
    ).cokernel()

    v_bar = quotient.module_generator("v")
    w_bar = quotient.module_generator("w")

    labels = quotient.module_generating_set()
    generators = quotient.module_generators()
    assert labels.cardinality() == 2
    assert labels.unrank(0) == "v"
    assert labels.unrank(1) == "w"
    assert generators["v"] == v_bar
    assert generators["w"] == w_bar
    assert v_bar != quotient.zero()
    assert w_bar == quotient.zero()

    normalization = quotient.invariant_factor_form()
    normalized = normalization.codomain()
    assert normalized is not quotient
    assert normalized.number_of_module_generators() == 1
    generator = normalized.module_generators()[0]
    assert normalization(v_bar) == generator
    assert normalization(w_bar) == normalized.zero()
    assert normalization.inverse()(generator) == v_bar


def test_invariant_factor_form_drops_only_unit_factors_and_keeps_free_summands() -> None:
    target = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    quotient = module_homset(relations, target)(
        {"r": target.module_generator("x")}
    ).cokernel()

    factors = quotient.invariant_factors()
    assert factors.cardinality() == 1
    assert factors.unrank(0) == 0
    assert quotient.number_of_module_generators() == 2
    normalization = quotient.invariant_factor_form()
    normalized = normalization.codomain()

    assert normalized.number_of_module_generators() == 1
    normalized_factors = normalized.invariant_factors()
    assert normalized_factors.cardinality() == 1
    assert normalized_factors.unrank(0) == 0
    assert normalized.rank() == 1
    for generator in quotient.module_generators():
        assert normalization.inverse()(normalization(generator)) == generator


def test_unimodular_discriminant_cokernel_keeps_both_dual_basis_classes() -> None:
    discriminant = Lattices(ZZ)("U").discriminant_module()

    assert discriminant.number_of_module_generators() == 2
    assert discriminant.module_generators().cardinality() == 2
    assert all(
        generator == discriminant.zero()
        for generator in discriminant.module_generators()
    )

    normalization = discriminant.invariant_factor_form()
    normalized = normalization.codomain()
    assert normalized.number_of_module_generators() == 0
    assert normalized.is_zero()
    assert all(
        normalization(generator) == normalized.zero()
        for generator in discriminant.module_generators()
    )


def test_u2_discriminant_keeps_the_two_half_basis_classes() -> None:
    discriminant = Lattices(ZZ)([[0, 2], [2, 0]]).discriminant_module()
    generators = discriminant.module_generators()

    assert discriminant.number_of_module_generators() == 2
    assert generators.cardinality() == 2
    assert all(generator.additive_order() == 2 for generator in generators)
    assert generators.unrank(0) != generators.unrank(1)

    normalization = discriminant.invariant_factor_form()
    assert normalization.codomain() is not discriminant
    assert normalization.codomain().number_of_module_generators() == 2
    for generator in generators:
        assert normalization.inverse()(normalization(generator)) == generator


def test_a2_invariant_factor_form_is_a_different_one_generator_framing() -> None:
    discriminant = Lattices(ZZ)("A2").discriminant_quadratic_form()
    normalization = discriminant.invariant_factor_form()
    normalized = normalization.codomain()

    assert discriminant.number_of_module_generators() == 2
    assert normalized.number_of_module_generators() == 1
    normalized_factors = normalized.invariant_factors()
    assert normalized_factors.cardinality() == 1
    assert normalized_factors.unrank(0) == 3
    assert normalization.is_quadratic()
    normalized_generator = normalized.module_generators()[0]
    smith_generator = discriminant.smith_form_module_generators().unrank(0)
    assert normalization.inverse()(normalized_generator) == smith_generator
    for generator in discriminant.module_generators():
        assert normalization.inverse()(normalization(generator)) == generator
        assert normalized.q(normalization(generator)) == discriminant.q(generator)


def test_odd_unimodular_discriminant_normalizes_as_a_bilinear_form() -> None:
    discriminant = Lattices(ZZ)(2).discriminant_bilinear_form()
    normalization = discriminant.invariant_factor_form()
    normalized = normalization.codomain()

    assert discriminant.number_of_module_generators() == 2
    assert discriminant.module_generators().cardinality() == 2
    assert all(generator == discriminant.zero() for generator in discriminant.module_generators())
    assert normalized.number_of_module_generators() == 0
    assert not normalization.is_quadratic()
