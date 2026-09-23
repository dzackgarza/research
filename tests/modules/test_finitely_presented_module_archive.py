r"""Archive reconciliation for Hermite normalization of presented modules."""

from dzack_research.preamble.all import (
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py",
    "owner_overrides": {
        "FinitelyPresentedModules": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "FinitelyPresentedModules.ParentMethods.framing_morphism": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_hermite_form_changes_only_the_relation_rows() -> None:
    free = ZZ.free_module(finite_ordered_set(("x",)))
    relations = ZZ.free_module(finite_ordered_set(("r1", "r2")))
    presentation = relations.module_category().Mor(relations, free)(
        {
            "r1": 2 * free.module_generator("x"),
            "r2": 4 * free.module_generator("x"),
        }
    )
    module = presentation.cokernel()
    normalization = module.hermite_form()
    normalized = normalization.codomain()

    assert normalization.domain() is module
    assert normalized.module_generating_set() == module.module_generating_set()
    assert normalized.presentation().domain().module_rank() == 1
    relation_generator = normalized.presentation().domain().module_generator(0)
    assert normalized.presentation()(relation_generator) == (
        2 * normalized.presentation().codomain().module_generator("x")
    )
    assert normalization.forward()(module.module_generator("x")) == normalized.module_generator("x")
    assert normalization.inverse()(normalized.module_generator("x")) == module.module_generator("x")




