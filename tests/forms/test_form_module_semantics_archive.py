r"""Archive reconciliation for formed-module categories and exact form morphisms."""

from dzack_research.preamble.all import ZZ, finite_ordered_set
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearFormModules,
    FormModules,
    QuadraticFormModules,
    SymmetricBilinearFormModules,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/form_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py",
    "disposition": "reconciled-live-owner",
}


def test_form_module_refines_the_represented_module_by_the_selected_form_type() -> None:
    module = ZZ.free_module(finite_ordered_set(("e", "f")))
    bilinear = module.bilinear_forms(ZZ)([[2, 1], [1, -2]])
    formed = FormModules(ZZ)(bilinear)

    assert formed.unformed_module() is module
    assert formed.form() is bilinear
    assert formed in FormModules(ZZ)
    assert formed in BilinearFormModules(ZZ)
    assert formed in SymmetricBilinearFormModules(ZZ)
    assert formed not in QuadraticFormModules(ZZ)


def test_quadratic_form_module_is_not_reclassified_as_a_bilinear_form_module() -> None:
    module = ZZ.free_module(finite_ordered_set(("e",)))
    quadratic = module.quadratic_forms(ZZ)([[2]])
    formed = FormModules(ZZ)(quadratic)

    assert formed.unformed_module() is module
    assert formed.form() is quadratic
    assert formed in FormModules(ZZ)
    assert formed in QuadraticFormModules(ZZ)
    assert formed not in BilinearFormModules(ZZ)


def test_identity_in_the_formed_homset_is_an_exact_form_morphism() -> None:
    module = ZZ.free_module(finite_ordered_set(("e", "f")))
    formed = FormModules(ZZ)(module.bilinear_forms(ZZ)([[0, 1], [1, 0]]))
    identity = formed.Mor(formed).identity()

    assert identity.domain() is formed
    assert identity.codomain() is formed
    assert identity.preserves_form_exactly()
    assert all(identity(generator) == generator for generator in formed.module_generators())
