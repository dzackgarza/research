r"""Module-morphism admission keeps laws, derivations, and hypotheses distinct.

These specimens are intentionally unexecuted until terminal T.  They separate
actual law decisions from construction-derived maps and from arbitrary callables
whose linearity remains conditional.
"""

import pytest

from dzack_research.preamble.all import *


def _coefficient(module, element, label):
    return module.framing_coefficients(module(element)).get(
        label,
        module.base_ring().zero(),
    )


def test_frobenius_on_the_gf4_line_is_additive_but_not_gf4_linear() -> None:
    field = GF(4)
    line = field.free_module(("e",))
    e = line.module_generator("e")
    maps = Modules(field).Mor(line, line)

    def frobenius(element):
        coefficient = _coefficient(line, element, "e")
        return line.scalar_multiple(coefficient**2, e)

    with pytest.raises(ValueError):
        maps.elementwise(frobenius)
