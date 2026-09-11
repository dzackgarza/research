r"""Graded direct sums use the owned category meet for their placement."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
)
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_graded_direct_sum_retains_owned_grading_framing_and_components() -> None:
    zero = BasedFreeModule(ZZ, finite_ordered_set(()))
    degree_one = BasedFreeModule(ZZ, finite_ordered_set(("x",)))

    def piece(degree):
        if int(degree) == 1:
            return degree_one
        return zero

    graded = GradedDirectSumModule(ZZ, piece, name="one generator in degree one")
    element = graded.from_component(1, degree_one.module_generator("x"))

    assert graded in GradedModules(ZZ)
    assert graded in FramedModules(ZZ)
    assert graded.graded_piece(1) is degree_one
    assert element.homogeneous_component(1) == degree_one.module_generator("x")
    assert element.homogeneous_component(2) == zero.zero()
