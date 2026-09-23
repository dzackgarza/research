r"""Framing sources are fixed before their morphisms are represented."""

import pytest

from dzack_research.preamble.all import Modules, QQ, ZZ, QuadraticField
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    FramingMorphism,
)
from dzack_research.preamble.categories.sets import NN


def test_free_framing_and_its_enriched_morphism_module_have_fixed_sources() -> None:
    module = QQ.free_module(("x", "y"))
    assert module.framing_source() is module
    x = module.module_generator("x")
    frame = module.framing_morphism()
    assert frame.domain() is module and frame.codomain() is module
    assert frame.module_generator_morphism() is module.module_generator_morphism()
    assert frame.linearity_decision() is True
    assert frame(x) == x
    assert frame(module.linear_combination(module.framing_coefficients(x))) == x
    morphisms = Modules(QQ).Mor(module, module)
    source = morphisms.framing_source()
    label = next(iter(source.module_generating_set()))
    generator_before_frame = morphisms.module_generator(label)
    doubled = morphisms.identity() + morphisms.identity()
    matrix_frame = morphisms.framing_morphism()
    assert matrix_frame.domain() is source
    assert matrix_frame.codomain() is morphisms
    assert matrix_frame.module_generator_morphism() is morphisms.module_generator_morphism()
    assert matrix_frame.linearity_decision() is True
    assert morphisms.module_generator(label) == generator_before_frame
    assert matrix_frame(source.module_generator(label)) == morphisms.module_generator(label)
    assert matrix_frame(
        source.linear_combination(morphisms.framing_coefficients(generator_before_frame))
    ) == generator_before_frame
    assert morphisms.framing_source() is source
    assert doubled(module.module_generator("x")) == 2 * module.module_generator("x")

    nested = Modules(QQ).Mor(morphisms, morphisms)
    nested_zero = nested.zero()
    nested_source = nested.framing_source()
    nested_label = next(iter(nested_source.module_generating_set()))
    nested_generator = nested.module_generator(nested_label)
    nested_frame = nested.framing_morphism()
    assert nested.framing_source() is nested_source
    assert nested.module_generator(nested_label) == nested_generator
    assert nested_frame.domain() is nested_source
    assert nested_frame.codomain() is nested
    assert nested_frame.module_generator_morphism() is nested.module_generator_morphism()
    assert nested_frame.linearity_decision() is True
    assert nested_zero(morphisms.zero()) == morphisms.zero()


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


def test_relationful_module_framing_data_are_fixed_before_arrow_realization() -> None:
    free = ZZ.free_module(("x",))
    relations = ZZ.free_module(("r",))
    relation_map = relations.module_category().Mor(relations, free)(
        {"r": ZZ(2) * free.module_generator("x")}
    )
    module = relation_map.cokernel()

    source = module.framing_source()
    selected_presentation = module.presentation()
    generator = module.module_generator("x")
    assert module.framing_source() is source
    assert selected_presentation.codomain() is source
    assert generator + module.zero() == generator

    framing = module.framing_morphism()
    assert framing.domain() is source
    assert framing.codomain() is module
    assert framing.module_generator_morphism() is module.module_generator_morphism()
    assert framing.linearity_decision() is True
    assert framing(source.module_generator("x")) == generator
    assert framing(
        source.linear_combination(module.framing_coefficients(generator))
    ) == generator
    assert module.presentation_projection() is framing
    assert module.framing_source() is source

    endomorphisms = Modules(ZZ).Mor(module, module)
    mor_presentation = endomorphisms.presentation()
    mor_source = endomorphisms.framing_source()
    assert mor_presentation.codomain() is mor_source
    mor_framing = endomorphisms.framing_morphism()
    assert mor_framing.domain() is mor_source
    assert endomorphisms.presentation_projection() is mor_framing


def test_a_nonsurjective_module_map_cannot_be_relabelled_as_the_selected_framing() -> None:
    line = ZZ.free_module(("e",))
    endomorphisms = Modules(ZZ).Mor(line, line)
    zero = endomorphisms({"e": line.zero()})

    assert zero.is_surjective() is False
    with pytest.raises(ValueError, match="selected generator map"):
        FramingMorphism(endomorphisms, zero.module_generator_morphism())


def test_infinite_free_framing_is_linear_without_finite_presentation_rows() -> None:
    module = ZZ.free_module(NN)
    generator = module.module_generator(NN(1000))
    source = module.framing_source()
    framing = module.framing_morphism()

    assert source is module
    assert framing.domain() is source
    assert framing.codomain() is module
    assert framing.module_generator_morphism() is module.module_generator_morphism()
    assert framing.linearity_decision() is True
    assert framing(generator) == generator
    assert framing(
        source.linear_combination(module.framing_coefficients(generator))
    ) == generator
