r"""Archive reconciliation for tautological forms and the forgetful adjunction.

The archived form-forgetful module exposed a left adjoint that equips a module
with its universal bilinear or quadratic form and a right adjoint that forgets
that form.  The live module category owns those same adjunctions through
``Modules(R).bilinear_free_form_adjunction()`` and
``Modules(R).quadratic_free_form_adjunction()``.
"""

from dzack_research.preamble.all import Modules, ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/functors/form_forgetful_adjunction.sage",
    "live_owner": "src/dzack_research/preamble/categories/functors/free_forms.py",
    "disposition": "reconciled-live-owner",
}


def _line_and_negation():
    line = ZZ.free_module(finite_ordered_set(("e",)))
    generator = line.module_generator("e")
    negation = line.module_category().Mor(line, line)({"e": -generator})
    return line, negation


def test_archived_bilinear_form_adjunction_is_the_live_free_form_adjunction() -> None:
    line, negation = _line_and_negation()
    adjunction = Modules(ZZ).bilinear_free_form_adjunction()
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    formed = free(line)
    lifted = free(negation)

    assert underlying(formed) is formed
    assert lifted.domain() is formed
    assert lifted.codomain() is formed
    assert lifted(formed.module_generator("e")) == -formed.module_generator("e")
    assert adjunction.unit(line).domain() is line
    assert adjunction.counit(formed).codomain() is formed


def test_archived_quadratic_form_adjunction_is_the_live_free_form_adjunction() -> None:
    line, negation = _line_and_negation()
    adjunction = Modules(ZZ).quadratic_free_form_adjunction()
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    formed = free(line)
    lifted = free(negation)

    assert underlying(formed) is formed
    assert lifted.domain() is formed
    assert lifted.codomain() is formed
    assert lifted(formed.module_generator("e")) == -formed.module_generator("e")
    assert adjunction.unit(line).domain() is line
    assert adjunction.counit(formed).codomain() is formed
