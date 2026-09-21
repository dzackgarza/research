r"""Archive reconciliation for formed-module categories and exact form morphisms."""

from dzack_research.preamble.all import Modules, ZZ, finite_ordered_set
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


def test_identity_in_the_formed_mor_is_an_exact_form_morphism() -> None:
    module = ZZ.free_module(finite_ordered_set(("e", "f")))
    formed = FormModules(ZZ)(module.bilinear_forms(ZZ)([[0, 1], [1, 0]]))
    identity = formed.Mor(formed).identity()

    assert identity.domain() is formed
    assert identity.codomain() is formed
    assert identity.preserves_form_exactly()
    assert all(identity(generator) == generator for generator in formed.module_generators())


def test_two_forms_on_one_module_retain_that_module_but_remain_distinct() -> None:
    module = ZZ.free_module(finite_ordered_set(("e", "f")))
    first = FormModules(ZZ)(module.bilinear_forms(ZZ)([[2, 0], [0, 3]]))
    second = FormModules(ZZ)(module.bilinear_forms(ZZ)([[5, 0], [0, 7]]))

    assert first is not second
    assert first.unformed_module() is module
    assert second.unformed_module() is module

    e, f = first.module_generators()
    probe = e + 2 * f
    assert first.scalar_multiple(ZZ(3), probe) == 3 * e + 6 * f

    module_mor = Modules(ZZ).Mor(first, first)
    identity = module_mor.identity()
    doubling = module_mor({"e": 2 * e, "f": 2 * f})
    assert (doubling * identity)(probe) == 2 * e + 4 * f

    assert first.b(e, e) == ZZ(2)
    assert second.b(second.module_generator("e"), second.module_generator("e")) == ZZ(5)


def test_formed_subobject_restricts_the_form_along_its_actual_inclusion() -> None:
    module = ZZ.free_module(finite_ordered_set(("e", "f")))
    ambient = FormModules(ZZ)(module.bilinear_forms(ZZ)([[3, 0], [0, 1]]))
    e = ambient.module_generator("e")
    restricted = ambient.subobject_on((2 * e,))
    underlying = restricted.unformed_module()
    generator = restricted.module_generator(0)

    assert underlying.inclusion().codomain() is ambient
    assert restricted.inclusion().codomain() is ambient
    assert restricted.inclusion()(generator) == 2 * e
    assert restricted.b(generator, generator) == 4 * ambient.b(e, e)
