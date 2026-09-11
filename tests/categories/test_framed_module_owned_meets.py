r"""Framed free and finitely presented modules use owned construction meets."""

from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModuleOn,
    FramedFreeModules,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.rings import session_ring_objects


def test_labeled_free_module_keeps_owned_framing_and_freeness() -> None:
    integers = session_ring_objects()["ZZ"]
    module = FreeModuleOn(integers, finite_ordered_set(("x", "y")))

    assert module in FramedFreeModules(integers)
    assert module in FinitelyGeneratedFreeModules(integers)
    assert tuple(module.module_generating_set()) == ("x", "y")


def test_presented_module_keeps_owned_selected_presentation() -> None:
    integers = session_ring_objects()["ZZ"]
    target = FreeModuleOn(integers, finite_ordered_set(("x", "y")))
    relations = FreeModuleOn(integers, finite_ordered_set(("r",)))
    presentation = module_homset(relations, target)(
        {"r": 2 * target.module_generator("x")}
    )
    module = FinitelyPresentedModule(presentation)

    assert module in ModulesWithChosenFinitePresentation(integers)
    assert module.presentation().domain() is relations
    assert module.presentation().codomain() is target
