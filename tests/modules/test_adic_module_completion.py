"""Finite presented modules complete by scalar extension along the ring completion."""

from dzack_research.preamble.all import (
    Modules,
    QQ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _torsion_module():
    ring = QQ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    free = ring.free_module(finite_ordered_set(("g",)))
    relations = ring.free_module(finite_ordered_set(("r",)))
    module = relations.module_category().Mor(relations, free)(
            {"r": free.scalar_multiple(x**2, free.module_generator("g"))}
        ).cokernel()
    return ring, x, module


def test_finite_module_completion_is_the_same_selected_presentation_after_scalar_extension() -> None:
    ring, x, module = _torsion_module()
    ideal = ring.ideal(x)

    completed = module.adic_completion(ideal, precision=6)
    completion = completed.base_ring()
    adjunction = Modules(ring).base_change_adjunction(completion.completion_map())

    assert adjunction.left_adjoint()(module) is completed
    assert module.base_change_to_completion(completion) is completed
    assert completion.ideal_of_definition() is ideal
    assert completion.completion_source() is ring
    assert completed.base_ring().computation_precision() == 6
    assert completed.number_of_module_generators() == module.number_of_module_generators()


def test_completed_module_retains_the_canonical_map_and_adic_truncations() -> None:
    ring, x, module = _torsion_module()
    completed = module.adic_completion(ring.ideal(x), precision=6)

    completion = completed.base_ring()
    unit = module.completion_unit(completion)
    truncation = module.adic_module_truncation(completion, 3)

    assert unit.domain() is module
    assert truncation.base_ring() is completed.base_ring().adic_truncation(3)
    assert truncation.number_of_module_generators() == module.number_of_module_generators()
