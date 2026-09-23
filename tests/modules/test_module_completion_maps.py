r"""Functorial finite-module completion over represented Noetherian rings."""

from dzack_research.preamble.all import (
    QQ,
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

    assert completed.scalar_extension_of() is multiplication
    extension = completed.scalar_extension_functor()
    completion = completed.domain().base_ring()
    assert extension.ring_map().codomain() is completion
    assert extension(free) is completed.domain()
    assert completed.domain() is completed.codomain()
    assert free.base_change_to_completion(completion) is completed.domain()
    assert completed.is_injective()
    assert completed.kernel().is_zero()


def test_completed_free_exact_sequence_has_residue_field_cokernel() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    free = _free_rank_one(ring)
    completed = _multiplication(free, x).adic_completion(ring.ideal(x), precision=6)
    completion = completed.domain().base_ring()
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






def test_completion_unit_and_projection_form_the_expected_finite_stage_triangle() -> None:
    ring = QQ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    module = _cyclic_torsion_module(ring, x**4)
    completed = module.adic_completion(ring.ideal(x), precision=6)
    completion = completed.base_ring()
    unit = module.completion_unit(completion)
    projection = module.adic_module_projection(completion, 3)
    finite = module.adic_module_truncation(completion, 3)
    finite_projection = finite.base_ring().quotient_map()

    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    projected = projection(unit(generator).underlying_element()).underlying_element()
    direct = finite.module_generator(finite.module_generating_set()[0])

    assert projected == direct
    assert finite_projection.domain() is ring
