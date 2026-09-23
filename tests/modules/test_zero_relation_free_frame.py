r"""A zero relation map presents its free target, with the chosen quotient retained."""

from dzack_research.preamble.all import ZZ, ModulesWithChosenFinitePresentation
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules


def test_zero_relations_place_the_exact_presented_module_with_its_basis():
    relations = ZZ.free_module(("relation",))
    generators = ZZ.free_module(("u", "v"))
    zero = relations.module_category().Mor(relations, generators)({"relation": generators.zero()})
    module = ModulesWithChosenFinitePresentation(ZZ)(zero)

    assert module in FramedFreeModules(ZZ).FinitelyGenerated()
    assert module.module_rank() == 2
    assert module.cokernel_morphism() is zero
    assert module.presentation() is zero
    u, v = module.module_generator("u"), module.module_generator("v")
    assert module.framing_coefficients(2 * u - 3 * v) == {"u": ZZ(2), "v": ZZ(-3)}

    for algebra in (module.tensor_algebra(), module.symmetric_algebra()):
        assert algebra.generating_module() is module
        assert algebra.graded_piece(1) is module
        assert algebra.framing_source() is not module
        x, y = algebra.algebra_generator("u"), algebra.algebra_generator("v")
        element = x * y + 2 * x
        assert algebra.linear_combination(algebra.framing_coefficients(element)) == element


def test_nonzero_relations_do_not_claim_the_selected_generators_are_a_basis():
    relations = ZZ.free_module(("relation",))
    generators = ZZ.free_module(("u",))
    twice = relations.module_category().Mor(relations, generators)({"relation": 2 * generators.module_generator("u")})
    module = ModulesWithChosenFinitePresentation(ZZ)(twice)

    assert module not in FramedFreeModules(ZZ)
    assert module.cokernel_morphism() is twice
    u = module.module_generator("u")
    assert u != module.zero()
    assert 2 * u == module.zero()
