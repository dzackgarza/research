r"""A grading is a family of modules; multiplying degrees requires extra structure."""

import pytest

from dzack_research.preamble.all import GradedModules, ZZ
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_set_graded_sum_keeps_projections_and_degree_preserving_maps() -> None:
    indices = finite_ordered_set(("left", "right"))
    piece = ZZ.free_module(1)
    category = GradedModules(ZZ, indices)
    module = category(indexed_family(indices, lambda _: piece))
    x = module.from_component("left", piece.module_generator(0))
    y = module.from_component("right", piece.module_generator(0))
    identity = category.Mor(module, module).elementwise(lambda element: element)
    assert module.grading_index_set() is indices
    assert module.projection("left")(x + y) == piece.module_generator(0)
    assert module.projection("right")(x) == piece.zero()
    assert identity(x + y) == x + y
    assert (identity * identity)(x) == x
    with pytest.raises(TypeError, match="monoid"):
        module.combine_degrees("left", "right")
