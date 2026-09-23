from dzack_research.preamble.all import (
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/pure/finitely_generated/finitely_generated_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    "disposition": "reconciled-live-owner",
}


def test_presented_pid_module_has_actual_short_free_resolution() -> None:
    f0 = ZZ.free_module(finite_ordered_set(("x", "y")))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    presentation = relations.module_category().Mor(relations, f0)(
        {"r": 6 * f0.module_generator("x")}
    )
    module = presentation.cokernel()
    resolution = module.free_resolution()

    assert resolution.module() is module
    assert resolution.term(0) is f0
    assert resolution.term(1).module_rank() == 1
    assert resolution.term(2).module_rank() == 0
    assert resolution.differential(1).is_injective()
    assert resolution.augmentation().codomain() is module
    assert resolution.is_exact()
    generator = resolution.term(1).module_generator(0)
    assert resolution.differential(1)(generator) == 6 * f0.module_generator("x")
    assert resolution.augmentation()(resolution.differential(1)(generator)) == module.zero()


def test_noninjective_presentation_is_replaced_by_actual_relation_submodule() -> None:
    f0 = ZZ.free_module(finite_ordered_set(("x",)))
    relations = ZZ.free_module(finite_ordered_set(("r1", "r2")))
    presentation = relations.module_category().Mor(relations, f0)(
        {
            "r1": 2 * f0.module_generator("x"),
            "r2": 4 * f0.module_generator("x"),
        }
    )
    module = presentation.cokernel()
    resolution = module.free_resolution()

    assert not presentation.is_injective()
    assert resolution.term(1).module_rank() == 1
    assert resolution.differential(1).is_injective()
    assert resolution.is_exact()
    invariants = module.invariant_factors()
    assert int(invariants.cardinality()) == 1
    assert invariants[0] == ZZ(2)




