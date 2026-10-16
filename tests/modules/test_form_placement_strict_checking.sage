r"""A zero rank-one form is degenerate; the form [2] over ZZ is not perfect.

The form [1] is both nondegenerate and unimodular. These determinant
computations are independent of the category a constructor is asked to use.
"""

import pytest

from dzack_research.preamble.all import *


@pytest.mark.parametrize("property_name, entry", (("Nondegenerate", 0), ("Unimodular", 2)))
def test_strict_form_placement_reads_the_actual_pairing(property_name, entry):
    module = ZZ.free_module(("e",))
    form = module.bilinear_hom_space(ZZ)([[entry]])
    category = (FormModules(ZZ).Nondegenerate() if property_name == "Nondegenerate"
                else FormModules(ZZ).Unimodular())
    previous = strict_checking()
    try:
        strict_checking(False)
        declared = category(form)
        with pytest.raises(ValueError):
            declared.validate_form_placement()

        strict_checking(True)
        with pytest.raises(ValueError):
            category(form)
    finally:
        strict_checking(previous)


def test_a_unit_form_is_valid_under_strict_checking():
    module = ZZ.free_module(("e",))
    form = module.bilinear_hom_space(ZZ)([[1]])
    previous = strict_checking()
    try:
        strict_checking(True)
        perfect = FormModules(ZZ).Unimodular()(form)

        assert perfect.determinant() == 1
        assert perfect.is_nondegenerate() is True
        assert perfect.is_unimodular() is True
    finally:
        strict_checking(previous)
