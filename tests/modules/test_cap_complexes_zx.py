"""CAP-backed kernels for cochain complexes over ``ZZ[x]``.

The provider is ModulePresentationsForCAP.  The public objects below are the
ordinary owned modules, subobjects and cohomology quotients; no CAP object is
part of the assertions.
"""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules import (
    CochainComplexes,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _specimen():
    ring = ZZ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    source = ring.free_module(finite_ordered_set(("a", "b")))
    target = ring.free_module(finite_ordered_set(("c",)))
    a = source.module_generator("a")
    b = source.module_generator("b")
    c = target.module_generator("c")
    differential = source.module_category().Mor(source, target)(
        {
            "a": target.scalar_multiple(ring(2), c),
            "b": target.scalar_multiple(x, c),
        }
    )
    complex_ = CochainComplexes(ring)({0: source, 1: target}, {0: differential})
    return ring, x, source, target, a, b, c, differential, complex_


def test_cap_kernel_retains_the_syzygy_inclusion_and_lift() -> None:
    ring, x, source, _target, a, b, _c, differential, _complex = _specimen()
    kernel = differential.kernel()
    candidate = source.scalar_multiple(-x, a) + source.scalar_multiple(ring(2), b)

    assert kernel.inclusion().is_in_image(candidate)
    lifted = kernel.inclusion().lift(candidate)
    assert kernel.inclusion()(lifted) == candidate
    assert int(kernel.number_of_module_generators()) == 1

    coefficients = kernel.framing_coefficients(lifted)
    nonzero = tuple(coefficient for coefficient in coefficients.values() if coefficient)
    assert len(nonzero) == 1
    assert nonzero[0].is_unit()


def test_cap_cohomology_retains_the_quotient_projection_R_mod_2_x() -> None:
    ring, x, _source, target, _a, _b, c, _differential, complex_ = _specimen()
    h1 = complex_.cohomology(1)
    one_class = h1.class_of_cycle(c)

    assert one_class != h1.zero()
    assert h1.class_of_cycle(target.scalar_multiple(ring(2), c)) == h1.zero()
    assert h1.class_of_cycle(target.scalar_multiple(x, c)) == h1.zero()
    assert h1.cycle_representative(one_class) == c




def test_transferred_cap_kernel_handles_nonidentity_maps_between_presented_Zx_modules() -> None:
    ring = ZZ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    source_free = ring.free_module(finite_ordered_set(("a",)))
    source_relations = ring.free_module(finite_ordered_set(("r",)))
    source = source_relations.module_category().Mor(source_relations, source_free)(
            {"r": ring(2) * x * source_free.module_generator("a")}
        ).cokernel()
    target_free = ring.free_module(finite_ordered_set(("c",)))
    target_relations = ring.free_module(finite_ordered_set(("s",)))
    target = target_relations.module_category().Mor(target_relations, target_free)(
            {"s": ring(2) * target_free.module_generator("c")}
        ).cokernel()
    reduction = source.module_category().Mor(source, target)(
        {"a": target.module_generator("c")}
    )

    kernel = reduction.kernel()
    inclusion = kernel.inclusion()
    generator = next(iter(kernel.module_generators()))
    image = inclusion(generator)
    coefficient = source.framing_coefficients(image).get("a", ring.zero())

    assert coefficient in (ring(2), -ring(2))
    assert kernel.scalar_multiple(x, generator) == kernel.zero()
    two_a = source.scalar_multiple(ring(2), source.module_generator("a"))
    lifted = inclusion.lift(two_a)
    assert inclusion(lifted) == two_a
    assert reduction(two_a) == target.zero()
