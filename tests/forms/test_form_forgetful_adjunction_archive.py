r"""Archive reconciliation for tautological forms and the forgetful adjunction.

The archived form-forgetful module exposed a left adjoint that equips a module
with its universal bilinear or quadratic form and a right adjoint that forgets
that form.  The live ``free_forms`` owner keeps those same constructions under
``BilinearFreeFormAdjunction`` and ``QuadraticFreeFormAdjunction``; the old
public names are exact aliases, not a parallel implementation.
"""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.functors.free_forms import (
    BilinearFormForgetfulAdjunction,
    BilinearFreeFormAdjunction,
    QuadraticFormForgetfulAdjunction,
    QuadraticFreeFormAdjunction,
    TautologicalBilinearFormFunctor,
    TautologicalQuadraticFormFunctor,
)
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
    assert BilinearFormForgetfulAdjunction is BilinearFreeFormAdjunction
    assert TautologicalBilinearFormFunctor is not None

    line, negation = _line_and_negation()
    adjunction = BilinearFormForgetfulAdjunction(ZZ)
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
    assert QuadraticFormForgetfulAdjunction is QuadraticFreeFormAdjunction
    assert TautologicalQuadraticFormFunctor is not None

    line, negation = _line_and_negation()
    adjunction = QuadraticFormForgetfulAdjunction(ZZ)
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
