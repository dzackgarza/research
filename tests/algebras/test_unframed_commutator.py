r"""The commutator and its arrows share the arbitrary-module algebra entry."""

from sage.misc.unknown import Unknown
from dzack_research.preamble.all import Algebras, LieAlgebraMorphism, LieAlgebraHomset, Modules, QQ
from dzack_research.preamble.categories.modules.general_modules import GeneralModules


def test_unframed_associative_product_and_its_commutator_use_the_actual_tensor():
    module = GeneralModules(QQ).from_operations(QQ,
        addition=lambda x, y: x + y, zero=QQ.zero(), negation=lambda x: -x,
        scalar_action=lambda r, x: r * x, verify=False)
    tensor = Modules(QQ).tensor_product((module, module))
    product = tensor.from_bilinear_map(module, lambda x, y: module(x.underlying_element() * y.underlying_element()))
    associative = Algebras(QQ).Associative()(module, product)
    functor = Algebras(QQ).Associative().commutator_lie_algebra()
    lie = functor(associative)
    assert lie is not associative
    assert lie.unformed_module() is associative
    assert lie.multiplication().domain().tensor_factor(0) is associative
    assert lie.multiplication().domain().tensor_factor(1) is associative
    x, y = lie(associative(module(QQ(2)))), lie(associative(module(QQ(3))))
    assert x * y == lie.zero()
    assert associative(module(QQ(2))) * associative(module(QQ(3))) == associative(module(QQ(6)))
    arrows = LieAlgebraHomset(lie, lie)
    assert arrows is Algebras(QQ).Lie().Mor(lie, lie)
    linear = Modules(QQ).Mor(lie, lie).identity()
    identity = LieAlgebraMorphism(arrows, linear)
    assert identity(x) == x
    assert identity.is_multiplicative() is Unknown
    algebra_identity = Algebras(QQ).Associative().Mor(associative, associative).identity()
    assert functor(algebra_identity)(x) == x
