from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedModule,
    ZZ,
    free_resolution,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_presented_pid_module_has_actual_short_free_resolution() -> None:
    f0 = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    presentation = module_homset(relations, f0)(
        {"r": 6 * f0.module_generator("x")}
    )
    module = FinitelyPresentedModule(presentation)
    resolution = module.free_resolution()

    assert resolution.module() is module
    assert resolution.term(0) is f0
    assert resolution.term(1).rank() == 1
    assert resolution.term(2).rank() == 0
    assert resolution.differential(1).is_injective()
    assert resolution.augmentation().codomain() is module
    assert resolution.is_exact()
    generator = resolution.term(1).module_generator(0)
    assert resolution.differential(1)(generator) == 6 * f0.module_generator("x")
    assert resolution.augmentation()(resolution.differential(1)(generator)) == module.zero()


def test_noninjective_presentation_is_replaced_by_actual_relation_submodule() -> None:
    f0 = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r1", "r2")))
    presentation = module_homset(relations, f0)(
        {
            "r1": 2 * f0.module_generator("x"),
            "r2": 4 * f0.module_generator("x"),
        }
    )
    module = FinitelyPresentedModule(presentation)
    resolution = free_resolution(module)

    assert not presentation.is_injective()
    assert resolution.term(1).rank() == 1
    assert resolution.differential(1).is_injective()
    assert resolution.is_exact()
    invariants = module.invariant_factors()
    assert int(invariants.cardinality()) == 1
    assert invariants[0] == ZZ(2)


def test_free_module_has_trivial_free_resolution() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    resolution = module.free_resolution()

    assert resolution.length() == 0
    assert resolution.term(0) is module
    assert resolution.term(1).rank() == 0
    assert resolution.augmentation().domain() is module
    assert resolution.augmentation().codomain() is module
    for generator in module.module_generators():
        assert resolution.augmentation()(generator) == generator
    assert resolution.is_exact()
