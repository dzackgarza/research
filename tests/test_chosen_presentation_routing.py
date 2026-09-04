from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules.pure.modules import (
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _SelectedFinitePresentationModules,
    _presentation_matrix,
)
from dzack_research.preamble.categories.functors.tensor_hom import (
    TensorByFunctor,
    InternalHomFromFunctor,
)


def test_finite_free_has_chosen_zero_presentation_without_selected_backend():
    module = ZZ**2
    assert module in ModulesWithChosenFinitePresentation(ZZ)
    assert module not in _SelectedFinitePresentationModules(ZZ)
    matrix = _presentation_matrix(module)
    assert matrix.nrows() == 0
    assert matrix.ncols() == 2


def test_tensor_hom_functors_are_defined_on_chosen_presentations():
    module = ZZ**2
    assert TensorByFunctor(module).domain() is ModulesWithChosenFinitePresentation(ZZ)
    assert InternalHomFromFunctor(module).domain() is ModulesWithChosenFinitePresentation(ZZ)
