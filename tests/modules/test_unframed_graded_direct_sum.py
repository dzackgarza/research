r"""A graded direct sum keeps unframed summands when equipped with a product."""

from dzack_research.preamble.all import Algebras, GradedModules, Modules, QQ, ZZ
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Set


def test_unframed_direct_sum_retains_its_pieces_and_constructor_under_an_algebra() -> None:
    piece = GeneralModules(QQ).from_operations(
        Set(QQ), addition=lambda x, y: x + y, zero=QQ.zero(),
        negation=lambda x: -x, scalar_action=lambda r, x: r * x, verify=False,
    )
    pieces = indexed_family(ZZ, lambda degree: piece)
    module = GradedModules(QQ, ZZ)(pieces)
    tensor = Modules(QQ).tensor_product((module, module))
    zero_product = tensor.from_bilinear_map(module, lambda x, y: module.zero())
    algebra = Algebras(QQ)(module, zero_product)
    vector = module.injection(ZZ(2))(piece(QQ(3)))
    lifted = algebra(vector)

    assert algebra.unformed_module() is module
    assert algebra in GradedModules(QQ, ZZ)
    assert algebra.graded_piece(ZZ(2)) is piece
    assert module(lifted) == vector
    assert module.projection(ZZ(2))(vector) == piece(QQ(3))
    assert module.projection(ZZ(1))(vector) == piece.zero()
    assert lifted * lifted == algebra.zero()
    assert algebra.scalar_multiple(QQ(2), lifted).homogeneous_component(ZZ(2)) == piece(QQ(6))


def test_direct_sum_does_not_turn_unknown_component_equality_into_inequality() -> None:
    from sage.misc.unknown import Unknown

    piece = GeneralModules(QQ).from_operations(
        Set(QQ), addition=lambda x, y: x + y, zero=QQ.zero(),
        negation=lambda x: -x, scalar_action=lambda r, x: r * x, verify=False,
    )
    tensor = Modules(QQ).tensor_product((piece, piece))
    graded = GradedModules(QQ, ZZ)(indexed_family(ZZ, lambda degree: tensor))
    element = graded.from_component(ZZ(1), tensor.pure_tensor(piece(QQ(1)), piece(QQ(1))))

    assert (element == graded.zero()) is Unknown
    assert (element != graded.zero()) is Unknown
    assert element + (-element) == graded.zero()
