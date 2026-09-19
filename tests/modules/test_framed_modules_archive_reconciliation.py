r"""Archive reconciliation for framed modules and their rationalization."""

from dzack_research.preamble.all import ZZ, FramedModules, finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/framed_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    "owner_overrides": {
        "FramedModuleParent": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_selected_framing_retains_its_index_set_generators_and_surjection() -> None:
    labels = finite_ordered_set(("x", "y"))
    module = ZZ.free_module(labels)
    framing = module.framing_morphism()

    assert module in FramedModules(ZZ)
    assert module.framing_morphism() is framing
    assert module.framing_source() is module
    assert module.module_generating_set() is labels
    assert module.module_generator_morphism() is framing.module_generator_morphism()
    assert module.module_generator_morphism().domain() is labels
    assert framing.codomain() is module
    assert framing.domain().module_generating_set() is labels
    for label in labels:
        assert framing(framing.domain().module_generator(label)) == module.module_generator(label)


def test_framed_module_vector_space_is_fraction_field_base_change() -> None:
    labels = finite_ordered_set(("x", "y"))
    module = ZZ.free_module(labels)
    vector_space = module.vector_space()
    rationals = ZZ.fraction_field_map().codomain()

    assert vector_space.base_ring() is rationals
    assert vector_space.module_generating_set() is labels
    for label in labels:
        assert vector_space.module_generator(label).parent() is vector_space
