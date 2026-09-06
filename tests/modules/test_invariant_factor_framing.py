from dzack_research.preamble.all import (
    BasedFreeModule,
    Cardinalities,
    Lattices,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
)


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
    assert normalized.rank() in Cardinalities()
    for generator in quotient.module_generators():
        assert normalization.inverse()(normalization(generator)) == generator


def test_torsion_free_pid_module_has_global_and_local_free_trivializations() -> None:
    from pytest import raises

    target = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    quotient = module_homset(relations, target)(
        {"r": target.module_generator("x")}
    ).cokernel()

    assert tuple(quotient._invariants_with_units()) == (ZZ.one(), ZZ.zero())
    assert quotient.is_torsion_free()
    assert quotient.is_projective()
    assert quotient.is_locally_free()

    trivialization = quotient.finite_free_trivialization()
    free = trivialization.codomain()
    assert trivialization.domain() is quotient
    assert free in FinitelyGeneratedFreeModules(ZZ)
    assert free.rank() == 1
    for generator in quotient.module_generators():
        assert trivialization.inverse()(trivialization(generator)) == generator

    torsion_free_projection = quotient.torsion_free_quotient_projection()
    assert torsion_free_projection(quotient.module_generator("x")) == (
        torsion_free_projection.codomain().zero()
    )
    assert torsion_free_projection(quotient.module_generator("y")) != (
        torsion_free_projection.codomain().zero()
    )

    point = ZZ.spectrum()(ZZ.ideal(5))
    local_trivialization = quotient.local_free_trivialization(point)
    assert local_trivialization.domain().localization_source_module() is quotient
    assert local_trivialization.codomain().localization_source_module() is free
    for label in local_trivialization.domain().module_generating_set():
        generator = local_trivialization.domain().module_generator(label)
        assert local_trivialization.inverse()(local_trivialization(generator)) == generator

    torsion = module_homset(relations, target)(
        {"r": 2 * target.module_generator("x")}
    ).cokernel()
    assert not torsion.is_projective()
    assert not torsion.is_locally_free()
    with raises(ValueError, match="with torsion is not finite free"):
        torsion.finite_free_trivialization()


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
