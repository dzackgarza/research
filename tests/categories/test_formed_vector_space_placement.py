"""Formed copies retain vector-space placement over a field."""

from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    VectorSpaces,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearFormModules,
    FormModules,
    FreeFormModules,
    SymmetricBilinearFormModules,
)


def test_a_formed_copy_of_a_rational_vector_space_is_still_a_vector_space() -> None:
    module = QQ.free_module(2)
    formed = module.equip_bilinear_form(QQ, [[1, 0], [0, 1]])

    assert module in VectorSpaces(QQ)
    assert formed in VectorSpaces(QQ)
    assert formed.unformed_module() is module


def test_finite_free_form_keeps_all_implied_form_refinements() -> None:
    formed = QQ.free_module(2).equip_bilinear_form(QQ, [[1, 0], [0, 1]])

    assert formed in FreeFormModules(QQ)
    assert formed in FormModules(QQ).FinitelyGenerated()
    assert formed in FreeFormModules(QQ).FinitelyGenerated()
    assert formed in FormModules(QQ).FinitelyPresented()
    assert formed in BilinearFormModules(QQ).FinitelyPresented()
    assert formed in SymmetricBilinearFormModules(QQ)


def test_base_change_of_an_integral_form_to_a_field_has_vector_space_placement() -> None:
    integral = ZZ.free_module(2).equip_bilinear_form(ZZ, [[2, 1], [1, 2]])
    rational = integral.base_change(ZZ.Mor(QQ)(lambda scalar: QQ(scalar)))
    mod_three = integral.base_change(ZZ.Mor(GF(3))(lambda scalar: GF(3)(scalar)))

    assert rational in VectorSpaces(QQ)
    assert mod_three in VectorSpaces(GF(3))
    assert integral.base_ring() is ZZ
