r"""H0 chain-map lifting for nonidentity morphisms of resolved modules."""

from dzack_research.preamble.all import FinitelyPresentedModule, ZZ, module_homset
from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic(modulus):
    free = BasedFreeModule(ZZ, finite_ordered_set(("g",)))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    return FinitelyPresentedModule(
        module_homset(relations, free)(
            {"r": free.scalar_multiple(ZZ(modulus), free.module_generator("g"))}
        )
    )


def test_nonidentity_module_map_lifts_to_a_commuting_resolution_map() -> None:
    source = _cyclic(6)
    target = _cyclic(3)
    morphism = module_homset(source, target)(
        {"g": target.module_generator("g")}
    )
    source_resolution = source.free_resolution()
    target_resolution = target.free_resolution()

    lifted = source_resolution.lift_morphism(morphism, target_resolution)

    generator = source_resolution.term(0).module_generator("g")
    assert target_resolution.augmentation()(lifted.component(0)(generator)) == morphism(
        source_resolution.augmentation()(generator)
    )
    relation = source_resolution.term(1).module_generator(0)
    assert target_resolution.differential(1)(lifted.component(1)(relation)) == lifted.component(0)(
        source_resolution.differential(1)(relation)
    )
