r"""Sparse algebra multiplication is defined on the previously constructed module."""

from dzack_research.preamble.all import ZZ




def test_sparse_root_preserves_relationful_component_products_and_maps() -> None:
    from dzack_research.preamble.all import GradedModules
    from dzack_research.preamble.categories.modules import FinitelyPresentedTorsionModules
    from dzack_research.preamble.categories.modules.pure.modules import FramedModules
    from dzack_research.preamble.categories.sets.indexed_families import indexed_family

    piece = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2, 3))
    source = GradedModules(ZZ)(indexed_family(ZZ, lambda _: piece), placements=(FramedModules(ZZ),))
    for algebra in (source.tensor_algebra(), source.symmetric_algebra()):
        x = algebra.algebra_generator(source.module_label_from_component(1, 0))
        y = algebra.algebra_generator(source.module_label_from_component(1, 1))
        assert 2 * x == algebra.zero()
        assert 3 * y == algebra.zero()
        assert x * y == algebra.zero()
        assert algebra.Mor(algebra).identity()(x + y) == x + y
        module = algebra.unformed_module()
        assert algebra.graded_piece(1) is source
        assert algebra.multiplication()(module(x), module(y)) == module.zero()
        assert algebra(module(x)) == x
