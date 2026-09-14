r"""Archive reconciliation for formed-module categories and exact form morphisms."""

from dzack_research.preamble.all import ZZ, BasedFreeModule, finite_ordered_set
from dzack_research.preamble.categories.forms import BilinearForms, QuadraticForms
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearFormModules,
    FormModule,
    FormModules,
    QuadraticFormModules,
    SymmetricBilinearFormModules,
    formed_module_homset,
    is_form_morphism,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/form_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py",
    "disposition": "reconciled-live-owner",
}


def test_form_module_refines_the_represented_module_by_the_selected_form_type() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("e", "f")))
    bilinear = BilinearForms(module, ZZ)([[2, 1], [1, -2]])
    formed = FormModule(bilinear)

    assert formed.unformed_module() is module
    assert formed.form() is bilinear
    assert formed in FormModules(ZZ)
    assert formed in BilinearFormModules(ZZ)
    assert formed in SymmetricBilinearFormModules(ZZ)
    assert formed not in QuadraticFormModules(ZZ)


def test_quadratic_form_module_is_not_reclassified_as_a_bilinear_form_module() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    quadratic = QuadraticForms(module, ZZ)([[2]])
    formed = FormModule(quadratic)

    assert formed.unformed_module() is module
    assert formed.form() is quadratic
    assert formed in FormModules(ZZ)
    assert formed in QuadraticFormModules(ZZ)
    assert formed not in BilinearFormModules(ZZ)


def test_identity_in_the_formed_homset_is_an_exact_form_morphism() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("e", "f")))
    formed = FormModule(BilinearForms(module, ZZ)([[0, 1], [1, 0]]))
    identity = formed_module_homset(formed, formed).identity()

    assert identity.domain() is formed
    assert identity.codomain() is formed
    assert is_form_morphism(identity)
    assert all(identity(generator) == generator for generator in formed.module_generators())
