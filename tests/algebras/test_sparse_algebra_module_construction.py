r"""Sparse algebra multiplication is defined on the previously constructed module."""

from dzack_research.preamble.all import Algebras, Modules, ZZ
from dzack_research.preamble.categories.sets.set_categories import NN


def test_sparse_products_keep_the_word_module_and_its_tensor_endpoints() -> None:
    source = ZZ.free_module(NN)
    for algebra in (source.tensor_algebra(), source.symmetric_algebra()):
        module = algebra.unformed_module()
        x, y = algebra.algebra_generator(2), algebra.algebra_generator(5)
        assert module is not algebra
        assert module in Modules(ZZ)
        assert module not in Algebras(ZZ)
        assert module.graded_piece(1) is source
        assert algebra.graded_piece(2) is module.graded_piece(2)
        multiplication = algebra.multiplication()
        assert multiplication.domain().tensor_factor(0) is module
        assert multiplication.domain().tensor_factor(1) is module
        assert multiplication.codomain() is module
        assert algebra(multiplication(module(x), module(y))) == x * y
        assert algebra(module(x + y)) == x + y
        assert algebra.one() * x == x
        assert x * algebra.one() == x
        assert algebra.algebra_structure_morphism()(ZZ(3)) == 3 * algebra.one()
        assert algebra.Mor(algebra).identity()(x * y) == x * y


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
