r"""Module-morphism admission keeps laws, derivations, and hypotheses distinct.

These specimens are intentionally unexecuted until terminal T.  They separate
actual law decisions from construction-derived maps and from arbitrary callables
whose linearity remains conditional.
"""

import pytest
from sage.misc.unknown import Unknown

from dzack_research.preamble.all import GF, Modules, ZZ
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.sets import NN
from dzack_research.preamble.categories.sets.set_categories import Sets


def _coefficient(module, element, label):
    return module.framing_coefficients(module(element)).get(
        label,
        module.base_ring().zero(),
    )


def test_finite_field_zero_and_scalar_maps_are_admitted_but_a_constant_is_not() -> None:
    field = GF(3)
    line = field.free_module(("e",))
    maps = Modules(field).Mor(line, line)
    e = line.module_generator("e")

    zero = maps.zero()
    double = maps.scalar_multiple(field(2), maps.identity())

    assert zero.linearity_decision() is True
    assert double.linearity_decision() is True
    assert double(e) == line.scalar_multiple(field(2), e)

    with pytest.raises(ValueError, match="send zero to zero"):
        maps.elementwise(lambda _element: e)
    with pytest.raises(ValueError, match="send zero to zero"):
        ModuleMorphism(maps, lambda _element: e, elementwise=True)

    with pytest.raises(ValueError, match="not injective"):
        line.Mono(line)({"e": line.zero()})
    assert maps.identity().is_surjective() is True
    assert maps.zero().is_surjective() is False


def test_square_on_the_integer_line_is_refuted_by_a_generator_sum() -> None:
    line = ZZ.free_module(("e",))
    e = line.module_generator("e")
    maps = Modules(ZZ).Mor(line, line)

    def square(element):
        coefficient = _coefficient(line, element, "e")
        return line.scalar_multiple(coefficient * coefficient, e)

    with pytest.raises(ValueError, match="not additive"):
        maps.elementwise(square)


def test_frobenius_on_the_gf4_line_is_additive_but_not_gf4_linear() -> None:
    field = GF(4)
    line = field.free_module(("e",))
    e = line.module_generator("e")
    maps = Modules(field).Mor(line, line)

    def frobenius(element):
        coefficient = _coefficient(line, element, "e")
        return line.scalar_multiple(coefficient**2, e)

    with pytest.raises(ValueError, match="not scalar-linear"):
        maps.elementwise(frobenius)


def _integer_mod_two_presentation():
    free = ZZ.free_module(("x",))
    relations = ZZ.free_module(("r",))
    relation_map = Modules(ZZ).Mor(relations, free)(
        {"r": ZZ(2) * free.module_generator("x")}
    )
    quotient = relation_map.cokernel()
    projection = relation_map.cokernel_projection()
    return free, quotient, projection


def test_generator_assignment_that_violates_a_source_relation_is_rejected() -> None:
    _free, quotient, _projection = _integer_mod_two_presentation()
    label = next(iter(quotient.module_generating_set()))

    with pytest.raises(ValueError, match="do not kill the domain relations"):
        Modules(ZZ).Mor(quotient, ZZ)({label: ZZ.one()})


def test_a_selected_lift_with_a_decidable_bad_section_equation_fails_admission() -> None:
    free, quotient, projection = _integer_mod_two_presentation()
    parent = Modules(ZZ).Mor(free, quotient)
    with pytest.raises(ValueError, match="does not satisfy the section equation"):
        ModuleMorphism(
            parent,
            lambda label: projection(free.module_generator(label)),
            lift=lambda _element: free.zero(),
        )


def test_an_unresolved_selected_lift_cannot_prove_absence_from_the_image() -> None:
    line = ZZ.free_module(("e",))
    e = line.module_generator("e")
    morphism = ModuleMorphism(
        Modules(ZZ).Mor(line, line),
        {"e": e},
        lift=lambda _element: None,
    )

    assert morphism.linearity_decision() is True
    assert morphism.selected_lift_exactness_decision() is Unknown
    with pytest.raises(ValueError, match="exactness is unresolved"):
        morphism.is_in_image(e)


def test_undecided_callable_remains_undecided_under_hom_operations_and_scalar_extension() -> None:
    module = ZZ.free_module(NN)
    maps = Modules(ZZ).Mor(module, module)
    conditional = maps.elementwise(lambda element: element)

    assert conditional.linearity_decision() is Unknown
    assert ModuleMorphism(maps, conditional).linearity_decision() is Unknown
    assert maps(conditional).linearity_decision() is Unknown
    assert (conditional * conditional).linearity_decision() is Unknown
    assert maps.scalar_multiple(ZZ(2), conditional).linearity_decision() is Unknown

    extension = Modules(ZZ).scalar_extension(ZZ.fraction_field_map())
    carried = extension(conditional)
    assert carried.linearity_decision() is Unknown
    label = NN(1000)
    assert carried(carried.domain().module_generator(label)) == carried.codomain().module_generator(label)


def test_generic_mono_epi_admission_distinguishes_unknown_callables_from_constructions() -> None:
    monomorphisms = Sets().Mono(NN, NN)
    epimorphisms = Sets().Epi(NN, NN)

    with pytest.raises(ValueError, match="not decided injective"):
        monomorphisms(lambda element: element)
    with pytest.raises(ValueError, match="not decided surjective"):
        epimorphisms(lambda element: element)

    mono_identity = monomorphisms.identity()
    epi_identity = epimorphisms.identity()
    assert mono_identity.is_injective() is True
    assert epi_identity.is_surjective() is True
    assert (mono_identity * mono_identity).is_injective() is True
    assert (epi_identity * epi_identity).is_surjective() is True
