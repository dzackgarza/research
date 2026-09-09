r"""Archive reconciliation for Hermite normalization of presented modules."""

from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedModule,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_hermite_form_changes_only_the_relation_rows() -> None:
    free = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r1", "r2")))
    presentation = module_homset(relations, free)(
        {
            "r1": 2 * free.module_generator("x"),
            "r2": 4 * free.module_generator("x"),
        }
    )
    module = FinitelyPresentedModule(presentation)
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


def test_hermite_and_smith_normalizations_are_distinct_constructions() -> None:
    free = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    presentation = module_homset(relations, free)(
        {"r": 2 * free.module_generator("x") + 4 * free.module_generator("y")}
    )
    module = FinitelyPresentedModule(presentation)
    hermite = module.hermite_form()
    smith = module.invariant_factor_form()

    assert hermite.codomain().module_generating_set() == module.module_generating_set()
    assert smith.codomain().invariant_factors() == module.invariant_factors()
    assert hermite.forward()(module.module_generator("x")) == hermite.codomain().module_generator("x")
    assert hermite.forward()(module.module_generator("y")) == hermite.codomain().module_generator("y")
