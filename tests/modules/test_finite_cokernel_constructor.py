r"""Finite cokernel construction retains its arrow and an actual free presentation."""

import pytest

from dzack_research.preamble.all import NN, ZZ, ModulesWithChosenFinitePresentation
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules


def test_presented_source_is_not_mistaken_for_a_free_relation_module():
    free = ZZ.free_module(1)
    twice = free.Mor(free)({0: 2 * free.module_generator(0)})
    torsion = twice.cokernel()
    arrow = torsion.Mor(free)({0: free.zero()})
    quotient = ModulesWithChosenFinitePresentation(ZZ)(arrow)

    assert quotient.cokernel_morphism() is arrow
    assert quotient.presentation().domain() in FramedFreeModules(ZZ)
    assert quotient.presentation().codomain() in FramedFreeModules(ZZ)
    assert quotient.presentation().domain() is not torsion
    assert quotient.cokernel_projection().domain() is free
    assert quotient.cokernel_projection()(arrow(torsion.module_generator(0))) == quotient.zero()
    assert quotient.module_rank() == 1


def test_finite_presentation_entry_rejects_an_infinite_source_framing():
    source = ZZ.free_module(NN)
    target = ZZ.free_module(1)
    arrow = source.Mor(target)(lambda label: target.zero())
    with pytest.raises(AssertionError, match="finite framing"):
        ModulesWithChosenFinitePresentation(ZZ)(arrow)


def test_infinite_numerator_module_can_have_finite_zero_localization():
    ring = ZZ.polynomial_ring(("x",))
    x = ring.algebra_generator("x")
    free = ring.free_module(1)
    numerator = free.Mor(free)({0: x * free.module_generator(0)}).cokernel()
    localized = ring.localization(x).localize_module(numerator)
    assert localized.is_zero() is True
    assert localized.is_finite() is True
