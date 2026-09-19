from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_localization_ring_owns_the_module_localization_functor_and_object() -> None:
    localization = ZZ.localization(ZZ(2))
    module = ZZ.free_module(finite_ordered_set(("e", "f")))

    functor = localization.localization_functor()
    assert functor.localization_ring() is localization

    through_ring = localization.localize_module(module)
    through_module = module.localize(localization)
    through_functor = functor(module)

    assert through_ring is through_functor
    assert through_module is through_functor
    assert through_functor.localization_ring() is localization
    assert through_functor.localization_source_module() is module
    assert through_functor.localization_functor() is functor
    framing = through_functor.framing_morphism()
    assert through_functor.framing_source().module_generating_set() is through_functor.module_generating_set()
    assert through_functor.framing_morphism() is framing
    assert framing.domain() is through_functor.framing_source()
    assert framing.codomain() is through_functor


def test_nonidentity_map_uses_the_same_localization_functor_and_endpoints() -> None:
    localization = ZZ.localization(ZZ(2))
    module = ZZ.free_module(finite_ordered_set(("e", "f")))
    e = module.module_generator("e")
    f = module.module_generator("f")
    morphism = module.module_category().Mor(module, module)(
        {"e": e + f, "f": 3 * f}
    )

    localized = localization.localize_module(module)
    localized_morphism = localization.localization_functor()(morphism)

    assert localized_morphism.domain() is localized
    assert localized_morphism.codomain() is localized
    assert localized_morphism.scalar_extension_of() is morphism
    assert localized_morphism.scalar_extension_functor() is localization.localization_functor()
    assert localized_morphism(localized.module_generator("e")) == (
        localized.module_generator("e") + localized.module_generator("f")
    )
    assert localized_morphism(localized.module_generator("f")) == 3 * localized.module_generator("f")
