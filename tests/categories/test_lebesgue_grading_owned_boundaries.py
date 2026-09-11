r"""Lebesgue grading objects meet their mathematical categories in the owned graph."""

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AssociativeAlgebras,
    CommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.functions.lebesgue_graded import (
    GradedLebesgueAlgebra,
    GradedLebesgueModule,
    LebesgueConvolutionAlgebra,
    LebesgueGradedModules,
)
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.rings.nonnegative_reals import NonNegativeReals
from dzack_research.preamble.rings.real import RR
from dzack_research.preamble.rings.unit_interval import UnitInterval


def test_holder_graded_module_is_owned_by_both_grading_categories() -> None:
    module = GradedLebesgueModule(NonNegativeReals)

    assert module in LebesgueGradedModules(RR)
    assert module in GradedModules(RR, NonNegativeReals)
    assert module.grading_monoid() is NonNegativeReals


def test_pointwise_algebra_retains_all_owned_refinements() -> None:
    algebra = GradedLebesgueAlgebra

    assert algebra in LebesgueGradedModules(RR)
    assert algebra in GradedAlgebras(RR, NonNegativeReals)
    assert algebra in Algebras(RR)
    assert algebra in AssociativeAlgebras(RR)
    assert algebra in CommutativeAlgebras(RR)
    assert algebra.grading_monoid() is NonNegativeReals


def test_convolution_algebra_keeps_nonunital_owned_placement() -> None:
    algebra = LebesgueConvolutionAlgebra

    assert algebra in LebesgueGradedModules(RR)
    assert algebra in AssociativeAlgebras(RR)
    assert algebra not in Algebras(RR)
    assert algebra not in GradedAlgebras(RR, UnitInterval)
    assert algebra.grading_monoid() is UnitInterval
