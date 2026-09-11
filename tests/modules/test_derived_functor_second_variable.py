r"""Tor and Ext retain their functoriality in the second module variable."""

from dzack_research.preamble.all import (
    Ext,
    ExtMap,
    FinitelyPresentedModule,
    FreeModule,
    Tor,
    TorMap,
    ZZ,
)


def _cyclic(integer):
    line = FreeModule(ZZ, 1)
    relations = FreeModule(ZZ, 1)
    return FinitelyPresentedModule(
        relations.Mor(line)({0: ZZ(integer) * line.module_generator(0)})
    )


def test_tor_is_covariant_in_the_second_variable() -> None:
    first = _cyclic(6)
    larger = _cyclic(8)
    source_module = _cyclic(4)
    target_module = _cyclic(2)
    first_quotient = larger.Mor(source_module)({0: source_module.module_generator(0)})
    quotient = source_module.Mor(target_module)({0: target_module.module_generator(0)})

    source = Tor(1, first, source_module)
    target = Tor(1, first, target_module)
    induced = TorMap(1, quotient, first, argument=2)

    assert induced.domain() is source
    assert induced.codomain() is target
    cycle_module = source.cochain_complex().graded_piece(source.degree())
    cycle_label = next(iter(cycle_module.module_generating_set()))
    class_ = source.class_of_cycle(cycle_module.module_generator(cycle_label))
    assert induced(class_).parent() is target

    first_map = TorMap(1, first_quotient, first, argument=2)
    composite = TorMap(1, quotient * first_quotient, first, argument=2)
    larger_source = Tor(1, first, larger)
    larger_cycle_module = larger_source.cochain_complex().graded_piece(larger_source.degree())
    larger_label = next(iter(larger_cycle_module.module_generating_set()))
    larger_class = larger_source.class_of_cycle(
        larger_cycle_module.module_generator(larger_label)
    )
    assert composite(larger_class) == induced(first_map(larger_class))


def test_ext_is_covariant_in_the_second_variable() -> None:
    first = _cyclic(6)
    larger = _cyclic(8)
    source_module = _cyclic(4)
    target_module = _cyclic(2)
    first_quotient = larger.Mor(source_module)({0: source_module.module_generator(0)})
    quotient = source_module.Mor(target_module)({0: target_module.module_generator(0)})

    source = Ext(1, first, source_module)
    target = Ext(1, first, target_module)
    induced = ExtMap(1, quotient, first, argument=2)

    assert induced.domain() is source
    assert induced.codomain() is target
    cycle_module = source.cochain_complex().graded_piece(source.degree())
    cycle_label = next(iter(cycle_module.module_generating_set()))
    class_ = source.class_of_cycle(cycle_module.module_generator(cycle_label))
    assert induced(class_).parent() is target

    first_map = ExtMap(1, first_quotient, first, argument=2)
    composite = ExtMap(1, quotient * first_quotient, first, argument=2)
    larger_source = Ext(1, first, larger)
    larger_cycle_module = larger_source.cochain_complex().graded_piece(larger_source.degree())
    larger_label = next(iter(larger_cycle_module.module_generating_set()))
    larger_class = larger_source.class_of_cycle(
        larger_cycle_module.module_generator(larger_label)
    )
    assert composite(larger_class) == induced(first_map(larger_class))
