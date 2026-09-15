r"""Construction preserves defining actions and the forgetful functor to Ab."""

from dzack_research.preamble.all import AdditiveGroups, Algebras, GeneralModule, Modules, QQ, Rings


def test_left_regular_matrix_module_retains_its_additive_action() -> None:
    ring = Modules(QQ).End(QQ**2)
    e11 = ring.from_rows([[1, 0], [0, 0]])
    e12 = ring.from_rows([[0, 1], [0, 0]])
    e21 = ring.from_rows([[0, 0], [1, 0]])
    e22 = ring.from_rows([[0, 0], [0, 1]])
    additive_end = AdditiveGroups().AdditiveCommutative().End(ring)
    rho = Rings().Mor(ring, additive_end).elementwise(
        lambda scalar: additive_end.elementwise(lambda element: scalar * element)
    )

    module = Modules(ring)(rho)
    assert module.scalar_action() is rho
    assert module.underlying_additive_group() is ring
    assert module.zero() + module(ring.one()) == module(ring.one())
    assert e12 * (e21 * module(ring.one())) == module(e11)
    assert e21 * (e12 * module(ring.one())) == module(e22)
    assert rho(e12)(e21) == e11
    assert e21 * rho(e12)(ring.one()) == e22
    assert (rho(e12) * rho(e21))(ring.one()) == rho(e11)(ring.one())
    assert (rho(e12) + rho(e21))(ring.one()) == e12 + e21
    assert additive_end.zero()(e12) == ring.zero()
    assert (2 * additive_end.one())(e12) == e12 + e12

    end = Modules(ring).End(module)
    right_e12 = end.elementwise(lambda element: module(element.underlying_element() * e12))
    right_e21 = end.elementwise(lambda element: module(element.underlying_element() * e21))
    assert end in Rings()
    assert end.one()(module(e12)) == module(e12)
    assert (right_e12 * right_e21)(module(ring.one())) == module(e22)
    assert (right_e12 + right_e21)(module(e11)) == module(e12)


def test_additive_forgetting_retains_maps_between_two_actions_on_one_group() -> None:
    ring = Modules(QQ).End(QQ**2)
    exchange = ring.from_rows([[0, 1], [1, 0]])
    e12 = ring.from_rows([[0, 1], [0, 0]])
    e21 = ring.from_rows([[0, 0], [1, 0]])
    additive_end = AdditiveGroups().AdditiveCommutative().End(ring)
    actions = Rings().Mor(ring, additive_end)
    rho = actions.elementwise(
        lambda scalar: additive_end.elementwise(lambda element: scalar * element)
    )
    conjugated = actions.elementwise(
        lambda scalar: additive_end.elementwise(
            lambda element: exchange * scalar * exchange * element
        )
    )
    modules = Modules(ring)
    source = modules(rho)
    target = modules(ring, conjugated)
    forward = modules.Mor(source, target).elementwise(
        lambda element: target(exchange * element.underlying_element())
    )
    inverse = modules.Mor(target, source).elementwise(
        lambda element: source(exchange * element.underlying_element())
    )

    assert target.scalar_action() is conjugated
    assert target.scalar_action()(e12)(ring.one()) == e21
    assert forward(e12 * source(ring.one())) == e12 * forward(source(ring.one()))
    forget = modules.underlying_additive_group_functor()
    assert forget(source) is ring
    assert forget(target) is ring
    assert forget(forward).domain() is ring
    assert forget(forward).codomain() is ring
    assert forget(forward)(ring.one()) == exchange
    assert forget(inverse * forward)(e12) == forget(inverse)(forget(forward)(e12)) == e12
    assert forget(modules.End(source).identity())(e21) == e21


def test_elementwise_module_presentation_supplies_the_same_action_accessor() -> None:
    module = GeneralModule(
        QQ,
        QQ,
        addition=lambda left, right: left + right,
        zero=QQ.zero(),
        negation=lambda element: -element,
        scalar_action=lambda scalar, element: scalar * element,
    )
    rho = module.scalar_action()
    assert rho.domain() is QQ
    assert rho.codomain() is AdditiveGroups().AdditiveCommutative().End(module.underlying_additive_group())
    half = QQ(1) / 2
    assert rho(half)(module(3)) == module(QQ(3) / 2)
    assert half * module(3) == module(QQ(3) / 2)
    end = Modules(QQ).End(module)
    assert end in Algebras(QQ)
    assert end.base_ring() is QQ
    assert end.scalar_action().domain() is QQ
    assert (half * end.one())(module(3)) == module(QQ(3) / 2)
