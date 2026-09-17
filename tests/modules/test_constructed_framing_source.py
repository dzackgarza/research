r"""Framing sources are fixed before their morphisms are represented."""

from dzack_research.preamble.all import Modules, QQ, ZZ, QuadraticField


def test_free_framing_and_its_enriched_morphism_module_have_fixed_sources() -> None:
    module = QQ.free_module(("x", "y"))
    assert module.framing_source() is module
    frame = module.framing_morphism()
    assert frame.domain() is module and frame.codomain() is module
    x = module.module_generator("x")
    assert frame(x) == x
    morphisms = Modules(QQ).Mor(module, module)
    source = morphisms.framing_source()
    matrix_frame = morphisms.framing_morphism()
    assert matrix_frame.domain() is source
    assert matrix_frame.codomain() is morphisms
    label = next(iter(source.module_generating_set()))
    assert matrix_frame(source.module_generator(label)) == morphisms.module_generator(label)
    assert morphisms.framing_source() is source


def test_the_integral_basis_is_the_order_module_frame() -> None:
    order = QuadraticField(5, "a").ring_of_integers()
    frame = order.framing_morphism()
    assert frame.codomain() is order
    assert frame.domain().base_ring() is ZZ
    assert frame.domain().module_generating_set() is order.module_generating_set()
    for label in order.module_generating_set():
        value = order.module_generator(label)
        assert frame(frame.domain().module_generator(label)) == value
        assert order.linear_combination(order.framing_coefficients(value)) == value
    assert order.multiplication()(order.one(), order.one()) == order.one()
