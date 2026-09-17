r"""Composition algebras use the same module/tensor construction as other algebras."""

from sage.misc.unknown import Unknown
from dzack_research.preamble.all import Algebras, Modules, QQ, ZZ
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.pure.modules import TensorProductModules


def test_linear_endomorphisms_have_a_tensor_composition_with_fixed_endpoints():
    module = QQ.free_module(2)
    endomorphisms = Modules(QQ).Mor(module, module)
    first = endomorphisms({0: module.zero(), 1: module.module_generator(0)})
    second = endomorphisms({0: module.module_generator(1), 1: module.zero()})
    multiplication = endomorphisms.multiplication()
    assert endomorphisms.unformed_module() is endomorphisms
    assert multiplication.domain() in TensorProductModules(QQ)
    assert multiplication.domain().tensor_factor(0) is endomorphisms
    assert multiplication.domain().tensor_factor(1) is endomorphisms
    assert multiplication.codomain() is endomorphisms
    assert multiplication(first, second) == first * second
    assert multiplication(first, second) != multiplication(second, first)
    assert multiplication(endomorphisms.one(), first) == first
    scalar = endomorphisms.algebra_structure_morphism()(QQ(3))
    assert scalar(module.module_generator(0)) == 3 * module.module_generator(0)


def test_additive_endomorphisms_of_rationals_keep_integer_not_rational_scalars():
    endomorphisms = AdditiveGroups().AdditiveCommutative().End(QQ)
    assert endomorphisms.base_ring() is ZZ
    assert endomorphisms.algebra_base_ring() is ZZ
    assert endomorphisms in Algebras(ZZ).Associative().Unital()
    first = endomorphisms.elementwise(lambda x: 2 * x)
    second = endomorphisms.elementwise(lambda x: 3 * x)
    product = endomorphisms.multiplication()(first, second)
    assert product(QQ(5)) == QQ(30)
    assert endomorphisms.multiplication().domain().tensor_factor(0) is endomorphisms
    assert endomorphisms.multiplication().codomain() is endomorphisms
    assert (first == second) is Unknown
    assert (first != second) is Unknown
    assert endomorphisms.scalar_multiple(ZZ(3), first)(QQ(5)) == QQ(30)
