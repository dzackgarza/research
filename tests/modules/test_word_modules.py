r"""The relationful word module is constructed before either algebra product."""

from dzack_research.preamble.all import Algebras, GradedModules, Modules, ZZ
from dzack_research.preamble.categories.modules import FinitelyPresentedTorsionModules
from dzack_research.preamble.categories.modules.word_modules import _module_on_word_quotient
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_word_module_preserves_component_torsion_and_the_degree_inclusion() -> None:
    pieces = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2, 3))
    from dzack_research.preamble.categories.modules.pure.modules import FramedModules
    source = GradedModules(ZZ)(indexed_family(ZZ, lambda _: pieces), placements=(FramedModules(ZZ),))
    two_label = source.module_label_from_component(1, 0)
    three_label = source.module_label_from_component(1, 1)
    for flavor in ("tensor", "symmetric"):
        module = _module_on_word_quotient(source, flavor)
        assert module in Modules(ZZ)
        assert module not in Algebras(ZZ)
        labels = module.degree_basis(2)
        mixed = labels(lambda i: two_label if int(i) == 0 else three_label) if flavor == "tensor" else labels.from_multiplicities({two_label: 1, three_label: 1})
        value = module.module_generator(module.basis_label(2, mixed))
        assert value == module.zero()
        assert module.framing_morphism().codomain() is module
        assert module.framing_morphism()(module.framing_source().module_generator(module.basis_label(2, mixed))) == module.zero()
        assert module.graded_piece(1) is source
        square = labels(lambda _: two_label) if flavor == "tensor" else labels.from_multiplicities({two_label: 2})
        piece = module.graded_piece(2)
        square_element = piece.module_generator(square)
        assert 2 * square_element == piece.zero()
        assert piece.inclusion()(square_element) == module.from_component(2, square_element)
        assert piece.inclusion().lift(module.from_component(2, square_element)) == square_element
