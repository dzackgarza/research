import pytest

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.functors.cochain_complexes import cochain_underlying_graded_module_functor
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    CochainComplex,
    CochainComplexes,
    FinitelyPresentedModule,
    GradedModules,
    cochain_homset,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _rank_one(label):
    return BasedFreeModule(ZZ, finite_ordered_set((label,)))


def test_cochain_complex_is_a_structured_graded_module_and_checks_d_squared() -> None:
    C0 = _rank_one("e")
    C1 = _rank_one("f")
    d0 = module_homset(C0, C1)({"e": 2 * C1.module_generator("f")})
    complex_ = CochainComplex(ZZ, {0: C0, 1: C1}, {0: d0})

    assert complex_ in CochainComplexes(ZZ)
    assert complex_ in GradedModules(ZZ)
    assert complex_.differential().degree_shift() == 1
    assert complex_.d(complex_.from_component(0, C0.module_generator("e"))) == (
        complex_.from_component(1, 2 * C1.module_generator("f"))
    )

    C2 = _rank_one("g")
    d1 = module_homset(C1, C2)({"f": C2.module_generator("g")})
    with pytest.raises(ValueError, match=r"d\^2 is nonzero"):
        CochainComplex(ZZ, {0: C0, 1: C1, 2: C2}, {0: d0, 1: d1})


def test_generic_cohomology_uses_kernel_image_and_cokernel() -> None:
    C0 = _rank_one("e")
    C1 = _rank_one("f")
    d0 = module_homset(C0, C1)({"e": 2 * C1.module_generator("f")})
    complex_ = CochainComplex(ZZ, {0: C0, 1: C1}, {0: d0})

    assert complex_.cohomology(0).is_zero()
    h1 = complex_.cohomology(1)
    invariant_factors = h1.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors.unrank(0) == ZZ(2)
    f = C1.module_generator("f")
    one_class = h1.class_of_cycle(f)
    assert h1.cycle_representative(one_class) == f
    assert h1.class_of_cycle(2 * f) == h1.zero()


def test_presented_pid_cohomology_uses_semantic_kernel_and_image_backends() -> None:
    source_free = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    source_relations = BasedFreeModule(ZZ, finite_ordered_set(("r4",)))
    source = FinitelyPresentedModule(
        module_homset(source_relations, source_free)(
            {"r4": 4 * source_free.module_generator("x")}
        )
    )
    target_free = BasedFreeModule(ZZ, finite_ordered_set(("y",)))
    target_relations = BasedFreeModule(ZZ, finite_ordered_set(("r2",)))
    target = FinitelyPresentedModule(
        module_homset(target_relations, target_free)(
            {"r2": 2 * target_free.module_generator("y")}
        )
    )
    differential = module_homset(source, target)(
        {"x": target.module_generator("y")}
    )
    complex_ = CochainComplex(
        ZZ,
        {0: source, 1: target},
        {0: differential},
    )

    h0 = complex_.cohomology(0)
    h1 = complex_.cohomology(1)
    invariant_factors = h0.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors.unrank(0) == ZZ(2)
    assert h1.is_zero()

    two_x = source.scalar_multiple(ZZ(2), source.module_generator("x"))
    two_x_class = h0.class_of_cycle(two_x)
    assert two_x_class != h0.zero()
    assert h0.cycle_representative(two_x_class) == two_x


def test_cochain_morphisms_are_degree_zero_chain_maps() -> None:
    C0 = _rank_one("e")
    C1 = _rank_one("f")
    d0 = module_homset(C0, C1)({"e": 2 * C1.module_generator("f")})
    complex_ = CochainComplex(ZZ, {0: C0, 1: C1}, {0: d0})

    identity = cochain_homset(complex_, complex_).identity()
    element = complex_.from_component(0, 3 * C0.module_generator("e"))
    assert identity(element) == element

    bad_degree_zero = module_homset(C0, C0)({"e": C0.zero()})
    degree_one_identity = module_homset(C1, C1).identity()
    with pytest.raises(ValueError, match="cochain square"):
        cochain_homset(complex_, complex_)(
            {0: bad_degree_zero, 1: degree_one_identity}
        )


def test_forgetful_functor_retains_the_same_graded_module() -> None:
    C0 = _rank_one("e")
    complex_ = CochainComplex(ZZ, {0: C0}, {})
    forget = cochain_underlying_graded_module_functor(ZZ)

    assert forget(complex_) is complex_
    assert forget.domain() is CochainComplexes(ZZ)
    assert forget.codomain() is GradedModules(ZZ)
