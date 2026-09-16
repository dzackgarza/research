r"""Different chain lifts induce the same Tor and Ext maps."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules.pure.modules import (
    FreeResolutionMorphism,
)


def _cyclic_two():
    free = ZZ.free_module(1)
    relations = ZZ.free_module(1)
    return relations.Mor(free)({0: 2 * free.module_generator(0)}).cokernel()


def _multiplication(module, scalar):
    return module.module_category().Mor(module, module)(
        {label: scalar * module.module_generator(label) for label in module.module_generating_set()}
    )


def test_two_resolution_lifts_of_the_identity_are_chain_homotopic() -> None:
    module = _cyclic_two()
    identity = module.module_category().Mor(module, module).identity()
    resolution = module.free_resolution(2)
    canonical = resolution.lift_morphism(identity, resolution)
    triple_zero = _multiplication(resolution.term(0), ZZ(3))
    triple_one = _multiplication(resolution.term(1), ZZ(3))
    alternative = FreeResolutionMorphism(
        resolution,
        resolution,
        identity,
        {0: triple_zero, 1: triple_one},
    )

    homotopy = alternative.chain_homotopy_to(canonical)
    generator = resolution.term(0).module_generator(0)
    assert resolution.differential(1)(homotopy.component(0)(generator)) == 2 * generator


def test_tor_and_ext_maps_do_not_depend_on_the_selected_chain_lift() -> None:
    module = _cyclic_two()
    identity = module.module_category().Mor(module, module).identity()
    resolution = module.free_resolution(2)
    canonical = resolution.lift_morphism(identity, resolution)
    alternative = FreeResolutionMorphism(
        resolution,
        resolution,
        identity,
        {
            0: _multiplication(resolution.term(0), ZZ(3)),
            1: _multiplication(resolution.term(1), ZZ(3)),
        },
    )

    tor_canonical = identity.tor_map(module, degree=1, lift=canonical)
    tor_alternative = identity.tor_map(module, degree=1, lift=alternative)
    ext_canonical = identity.ext_map(module, degree=1, lift=canonical)
    ext_alternative = identity.ext_map(module, degree=1, lift=alternative)

    tor_source = tor_canonical.domain()
    tor_cycle_module = tor_source.cochain_complex().graded_piece(tor_source.degree())
    tor_label = next(iter(tor_cycle_module.module_generating_set()))
    tor_class = tor_source.class_of_cycle(tor_cycle_module.module_generator(tor_label))
    assert tor_canonical(tor_class) == tor_alternative(tor_class)

    ext_source = ext_canonical.domain()
    ext_cycle_module = ext_source.cochain_complex().graded_piece(ext_source.degree())
    ext_label = next(iter(ext_cycle_module.module_generating_set()))
    ext_class = ext_source.class_of_cycle(ext_cycle_module.module_generator(ext_label))
    assert ext_canonical(ext_class) == ext_alternative(ext_class)
