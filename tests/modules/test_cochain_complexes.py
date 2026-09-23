
from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules import (
    CochainComplexes,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _rank_one(label):
    return ZZ.free_module(finite_ordered_set((label,)))




def test_generic_cohomology_uses_kernel_image_and_cokernel() -> None:
    C0 = _rank_one("e")
    C1 = _rank_one("f")
    d0 = C0.module_category().Mor(C0, C1)({"e": 2 * C1.module_generator("f")})
    complex_ = CochainComplexes(ZZ)({0: C0, 1: C1}, {0: d0})

    assert complex_.cohomology(0).is_zero()
    h1 = complex_.cohomology(1)
    invariant_factors = h1.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors[0] == ZZ(2)
    f = C1.module_generator("f")
    one_class = h1.class_of_cycle(f)
    assert h1.cycle_representative(one_class) == f
    assert h1.class_of_cycle(2 * f) == h1.zero()


def test_presented_pid_cohomology_uses_semantic_kernel_and_image_backends() -> None:
    source_free = ZZ.free_module(finite_ordered_set(("x",)))
    source_relations = ZZ.free_module(finite_ordered_set(("r4",)))
    source = source_relations.module_category().Mor(source_relations, source_free)(
            {"r4": 4 * source_free.module_generator("x")}
        ).cokernel()
    target_free = ZZ.free_module(finite_ordered_set(("y",)))
    target_relations = ZZ.free_module(finite_ordered_set(("r2",)))
    target = target_relations.module_category().Mor(target_relations, target_free)(
            {"r2": 2 * target_free.module_generator("y")}
        ).cokernel()
    differential = source.module_category().Mor(source, target)(
        {"x": target.module_generator("y")}
    )
    complex_ = CochainComplexes(ZZ)(
        {0: source, 1: target},
        {0: differential},
    )

    h0 = complex_.cohomology(0)
    h1 = complex_.cohomology(1)
    invariant_factors = h0.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors[0] == ZZ(2)
    assert h1.is_zero()

    two_x = source.scalar_multiple(ZZ(2), source.module_generator("x"))
    two_x_class = h0.class_of_cycle(two_x)
    assert two_x_class != h0.zero()
    assert h0.cycle_representative(two_x_class) == two_x




