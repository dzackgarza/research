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


def test_selected_presentation_retains_its_quotient_map_as_the_module_framing() -> None:
    free = ZZ.free_module(finite_ordered_set(("x",)))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    presentation = relations.module_category().Mor(relations, free)(
        {"r": 2 * free.module_generator("x")}
    )

    module = presentation.cokernel()
    framing = module.framing_morphism()

    assert module.framing_morphism() is framing
    assert module.framing_source() is free
    assert module.presentation().codomain() is module.framing_source()
    assert module.presentation_projection() is framing
    assert module.module_generator("x") == framing(free.module_generator("x"))
    displayed = repr(module.module_generators())
    assert displayed.startswith("Module generators: [")
    assert "Indexed family" not in displayed


def test_hermite_and_smith_normalizations_are_distinct_constructions() -> None:
    free = ZZ.free_module(finite_ordered_set(("x", "y")))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    presentation = relations.module_category().Mor(relations, free)(
        {"r": 2 * free.module_generator("x") + 4 * free.module_generator("y")}
    )
    module = presentation.cokernel()
    hermite = module.hermite_form()
    smith = module.invariant_factor_form()

    assert hermite.codomain().module_generating_set() == module.module_generating_set()
    assert smith.codomain().invariant_factors() == module.invariant_factors()
    assert hermite.forward()(module.module_generator("x")) == hermite.codomain().module_generator("x")
    assert hermite.forward()(module.module_generator("y")) == hermite.codomain().module_generator("y")
