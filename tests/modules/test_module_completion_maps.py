r"""Functorial finite-module completion over represented Noetherian rings."""

from dzack_research.preamble.all import (
    QQ,
    Modules,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _free_rank_one(ring):
    return ring.free_module(finite_ordered_set(("g",)))


def _cyclic_torsion_module(ring, scalar):
    free = _free_rank_one(ring)
    relations = ring.free_module(finite_ordered_set(("r",)))
    return relations.module_category().Mor(relations, free)(
            {"r": free.scalar_multiple(scalar, free.module_generator("g"))}
        ).cokernel()


def _multiplication(module, scalar):
    label = module.module_generating_set()[0]
    return module.module_category().Mor(module, module)(
        {label: module.scalar_multiple(scalar, module.module_generator(label))}
    )


def test_multiplication_by_x_on_a_free_module_stays_injective_after_completion() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    free = _free_rank_one(ring)
    multiplication = _multiplication(free, x)

    assert multiplication.is_injective()
    completed = multiplication.adic_completion(ring.ideal(x), precision=6)

    construction = completed.completion_construction()
    assert construction.source_morphism() is multiplication
    assert construction.completion() is completed.domain().completion_ring()
    assert completed.domain().completion_source_module() is free
    assert completed.codomain().completion_source_module() is free
    assert completed.domain().completion_ring() is completed.codomain().completion_ring()
    assert completed.is_injective()
    assert completed.kernel().is_zero()


def test_completed_free_exact_sequence_has_residue_field_cokernel() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    free = _free_rank_one(ring)
    completed = _multiplication(free, x).adic_completion(ring.ideal(x), precision=6)
    completion = completed.domain().completion_ring()
    cokernel = completed.cokernel()

    assert not cokernel.is_zero()
    residue_fiber = cokernel.base_change(completion.residue_map())
    assert residue_fiber.module_rank() == 1
    assert completed.cokernel_projection().codomain() is cokernel


def test_torsion_kernel_remains_nonzero_after_completion() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    torsion = _cyclic_torsion_module(ring, x**3)
    multiplication = _multiplication(torsion, x)

    assert not multiplication.is_injective()
    assert not multiplication.kernel().is_zero()

    completed = multiplication.adic_completion(ring.ideal(x), precision=6)
    assert not completed.is_injective()
    assert not completed.kernel().is_zero()


def test_multivariable_free_completion_uses_the_same_module_projection() -> None:
    ring = QQ.polynomial_ring(("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    free = _free_rank_one(ring)
    completed = free.adic_completion(ring.ideal(x, y), precision=5)

    projection = completed.adic_module_projection(3)
    target = completed.adic_module_truncation(3)
    assert projection.domain() is completed
    assert projection.codomain().module_over_extension() is target

    transition = completed.adic_module_transition_map(4, 2)
    assert transition.domain() is completed.adic_module_truncation(4)
    assert transition.codomain().module_over_extension() is completed.adic_module_truncation(2)


def test_free_plus_torsion_completion_preserves_the_selected_presentations() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    free = _free_rank_one(ring)
    torsion = _cyclic_torsion_module(ring, x**2)
    mixed = Modules(ring).biproduct((free, torsion))
    completed = mixed.adic_completion(ring.ideal(x), precision=5)

    assert completed.completion_source_module() is mixed
    assert completed.number_of_module_generators() == mixed.number_of_module_generators()
    assert completed.adic_module_truncation(2).number_of_module_generators() == mixed.number_of_module_generators()


def test_completion_unit_and_projection_form_the_expected_finite_stage_triangle() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    module = _cyclic_torsion_module(ring, x**4)
    completed = module.adic_completion(ring.ideal(x), precision=6)
    unit = completed.completion_unit()
    projection = completed.adic_module_projection(3)
    finite = completed.adic_module_truncation(3)
    finite_projection = finite.base_ring().quotient_map()

    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    projected = projection(unit(generator)).underlying_element()
    direct = finite.module_generator(finite.module_generating_set()[0])

    assert projected == direct
    assert finite_projection.domain() is ring
