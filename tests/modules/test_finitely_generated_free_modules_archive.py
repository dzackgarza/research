"""Archive reconciliation for finite based free modules."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    FinitelyGeneratedFreeModules,
    FreeModuleOn,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    "owner_overrides": {
        "BasedFreeModule": "src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py",
        "Free_ZZ": "src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_based_free_module_is_the_live_free_module_on_ordered_labels() -> None:
    labels = finite_ordered_set(("e", "f"))
    module = BasedFreeModule(ZZ, labels)

    assert module is FreeModuleOn(ZZ, labels)
    assert module in FinitelyGeneratedFreeModules(ZZ)
    assert module.module_generating_set() is labels
    assert int(module.module_rank()) == 2
    assert int(module.number_of_module_generators()) == 2
    assert module.relations().cardinality() == 0
    assert not module.is_torsion()

    generators = module.module_generators()
    assert generators["e"] == module.module_generator("e")
    assert generators["f"] == module.module_generator("f")
    assert module((2, -3)) == 2 * generators["e"] - 3 * generators["f"]


def test_archived_generator_assignment_builds_the_actual_module_morphism() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("e", "f")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    u = target.module_generator("u")
    v = target.module_generator("v")

    morphism = module_homset(source, target)({"e": u + v, "f": 2 * v})
    assert morphism(source.module_generator("e")) == u + v
    assert morphism(source.module_generator("f")) == 2 * v
    assert morphism(3 * source.module_generator("e") - source.module_generator("f")) == 3 * u + v

    line = source.subobject_on((source.module_generator("e"),))
    assert line.inclusion().codomain() is source
    assert line.inclusion()(line.module_generator(0)) == source.module_generator("e")


def test_zero_rank_free_module_keeps_empty_basis_and_zero_relation_presentation() -> None:
    zero = BasedFreeModule(ZZ, finite_ordered_set(()))

    assert zero is FreeModuleOn(ZZ, finite_ordered_set(()))
    assert int(zero.module_rank()) == 0
    assert zero.module_generating_set().cardinality() == 0
    assert zero.relations().cardinality() == 0
    assert zero.is_torsion()
    assert zero.zero() == zero(())
