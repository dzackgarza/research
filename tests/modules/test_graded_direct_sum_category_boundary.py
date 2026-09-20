r"""Graded direct sums use the owned category meet for their placement."""

from dzack_research.preamble.all import NN, ZZ
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_graded_direct_sum_retains_owned_grading_framing_and_components() -> None:
    zero = ZZ.free_module(finite_ordered_set(()))
    degree_one = ZZ.free_module(finite_ordered_set(("x",)))

    pieces = indexed_family(
        ZZ,
        lambda degree: degree_one if int(degree) == 1 else zero,
    )
    graded = GradedModules(ZZ)(pieces, placements=(FramedModules(ZZ),))
    element = graded.from_component(1, degree_one.module_generator("x"))

    assert graded in GradedModules(ZZ)
    assert graded in FramedModules(ZZ)
    assert graded.graded_piece(1) is degree_one
    assert element.homogeneous_component(1) == degree_one.module_generator("x")
    assert element.homogeneous_component(2) == zero.zero()


def test_graded_direct_sum_accepts_an_owned_product_grading_monoid() -> None:
    bigrades = NN**2
    piece = ZZ.free_module(finite_ordered_set(("x",)))
    graded = GradedModules(ZZ, bigrades)(
        indexed_family(bigrades, lambda _degree: piece),
    )
    degree = bigrades((1, 2))
    element = graded.from_component(degree, piece.module_generator("x"))

    assert graded in GradedModules(ZZ, bigrades)
    assert element.degree() == degree
    assert element.homogeneous_component((1, 2)) == piece.module_generator("x")
