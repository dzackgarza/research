from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules import (
    FinitelyPresentedTorsionModules,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_power_maps_agree(left, right, probes) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for probe in probes:
        assert left(probe) == right(probe)


def test_exterior_algebra_of_a_presented_module_imposes_linear_relations_and_wedge_laws() -> (
    None
):
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4, 4))
    algebra = module.exterior_algebra()
    x = algebra.algebra_generator(0)
    y = algebra.algebra_generator(1)

    assert 4 * x == algebra.zero()
    assert 4 * y == algebra.zero()
    assert x * x == algebra.zero()
    assert y * y == algebra.zero()
    assert x * y == -(y * x)
    assert 4 * (x * y) == algebra.zero()
    _factors = algebra.graded_piece(2).invariant_factors()
    assert _factors.cardinality() == 1
    assert _factors[0] == 4
    degree_one_label = next(
        label
        for label in algebra.module_generating_set()
        if int(label.summand_index()) == 1
    )
    assert algebra.module_generator(degree_one_label) == x


def test_divided_power_algebra_has_integral_pd_laws_not_symmetric_multiplication() -> (
    None
):
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    algebra = module.divided_power_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")

    gamma2x = algebra.divided_power(x, 2)
    gamma2y = algebra.divided_power(y, 2)
    gamma3x = algebra.divided_power(x, 3)
    assert x * x == 2 * gamma2x
    assert gamma2x * x == 3 * gamma3x
    assert algebra.divided_power(x + y, 2) == gamma2x + x * y + gamma2y
    assert x * y == y * x
    assert algebra.augmentation(algebra.one() + x + gamma2y) == ZZ.one()


def test_exterior_and_divided_power_algebras_are_functorial_on_presented_modules() -> (
    None
):
    source = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((8, 8))
    middle = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4, 4))
    target = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2, 2))
    first = source.module_category().Mor(source, middle)(
        {
            0: middle.module_generator(0) + middle.module_generator(1),
            1: 2 * middle.module_generator(1),
        }
    )
    second = middle.module_category().Mor(middle, target)(
        {0: target.module_generator(0), 1: target.module_generator(1)}
    )

    modules = source.module_category()
    for functor in (modules.exterior_algebra(), modules.divided_power_algebra()):
        source_algebra = functor(source)
        first_map = functor(first)
        second_map = functor(second)
        composite = functor(second * first)
        stepwise = second_map * first_map
        probes = [
            source_algebra.one(),
            source_algebra.algebra_generator(0),
            source_algebra.algebra_generator(1),
            source_algebra.algebra_generator(0) * source_algebra.algebra_generator(1),
        ]
        if source_algebra.flavor() == "divided":
            probes.append(
                source_algebra.divided_power(source_algebra.algebra_generator(0), 3)
            )
        _assert_power_maps_agree(composite, stepwise, probes)

        identity = functor(source.module_category().Mor(source, source).identity())
        _assert_power_maps_agree(
            identity,
            functor(source).Mor(functor(source))(
                source.module_category().Mor(source, source).identity()
            ),
            probes,
        )


def test_canonical_comparison_maps_between_the_four_free_constructions() -> None:
    from dzack_research.preamble.all import QQ

    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    tensor = module.tensor_algebra()
    symmetric = module.symmetric_algebra()
    alternating = module.exterior_algebra()
    divided = module.divided_power_algebra()
    x_t = tensor.algebra_generator("x")
    y_t = tensor.algebra_generator("y")

    to_symmetric = module.tensor_to_symmetric()
    assert to_symmetric(x_t * y_t - y_t * x_t) == symmetric.zero()

    to_alternating = module.tensor_to_alternating()
    assert to_alternating(x_t * x_t) == alternating.zero()
    assert to_alternating(x_t * y_t + y_t * x_t) == alternating.zero()

    to_divided = module.symmetric_to_divided()
    x_s = symmetric.algebra_generator("x")
    assert to_divided(x_s**3) == 6 * divided.divided_power(
        divided.algebra_generator("x"), 3
    )

    rational_module = QQ.free_module(finite_ordered_set(("x", "y")))
    sym_to_div = rational_module.symmetric_to_divided()
    div_to_sym = rational_module.divided_to_symmetric()
    symmetric_q = rational_module.symmetric_algebra()
    divided_q = rational_module.divided_power_algebra()
    x_q = symmetric_q.algebra_generator("x")
    y_q = symmetric_q.algebra_generator("y")
    gamma2x = divided_q.divided_power(divided_q.algebra_generator("x"), 2)
    probe_sym = x_q**2 * y_q + 3 * y_q
    probe_div = gamma2x * divided_q.algebra_generator(
        "y"
    ) + divided_q.algebra_generator("x")
    assert div_to_sym(sym_to_div(probe_sym)) == probe_sym
    assert sym_to_div(div_to_sym(probe_div)) == probe_div


def test_power_algebras_construct_their_exact_sum_before_the_product() -> None:
    from dzack_research.preamble.all import Algebras, GradedModules, Modules

    source = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4, 4))
    for algebra, degree_piece in (
        (source.exterior_algebra(), source.exterior_power),
        (source.divided_power_algebra(), source.divided_power_module),
    ):
        module = algebra.unformed_module()
        assert module is not algebra
        assert module in GradedModules(ZZ)
        assert module not in Algebras(ZZ)
        assert module.graded_piece(2) is degree_piece(2)
        assert module.graded_piece(-1).zero() == module.graded_piece(-1).an_element()
        x = algebra.algebra_generator(0)
        y = algebra.algebra_generator(1)
        multiplication = algebra.multiplication()
        assert multiplication.codomain() is module
        assert multiplication.domain().tensor_factor(0) is module
        assert multiplication.domain().tensor_factor(1) is module
        assert algebra(multiplication(module(x), module(y))) == x * y
        assert algebra(module(x + y)) == x + y
        assert module(x + y) == module(x) + module(y)
        assert algebra.one() * x == x
        assert 4 * x == algebra.zero()
        assert module.projection(1)(module(x)) == source.module_generator(0)


def test_divided_power_algebra_framing_includes_higher_integral_generators() -> None:
    source = ZZ.free_module(finite_ordered_set(("x",)))
    algebra = source.divided_power_algebra()
    x = algebra.algebra_generator("x")
    gamma_two = algebra.divided_power(x, 2)
    piece = algebra.graded_piece(2)
    label = algebra.module_label_from_component(2, next(iter(piece.module_generating_set())))
    assert label in algebra.algebra_generating_set()
    assert algebra.algebra_generator(label) == gamma_two
    assert x * x == 2 * gamma_two
