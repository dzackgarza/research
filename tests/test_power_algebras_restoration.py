from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras import (
    AlternatingAlgebraOf,
    DividedPowerAlgebraOf,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    alternating_algebra_functor,
    divided_power_algebra_functor,
)
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    FinitelyPresentedTorsionModules,
    module_homset,
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
    algebra = AlternatingAlgebraOf(module)
    x = algebra.algebra_generator(0)
    y = algebra.algebra_generator(1)

    assert 4 * x == algebra.zero()
    assert 4 * y == algebra.zero()
    assert x * x == algebra.zero()
    assert y * y == algebra.zero()
    assert x * y == -(y * x)
    assert 4 * (x * y) == algebra.zero()
    assert tuple(algebra.graded_piece(2).invariant_factors()) == (4,)
    degree_one_label = next(
        label
        for label in algebra.module_generating_set()
        if int(label.summand_index()) == 1
    )
    assert algebra.module_generator(degree_one_label) == x


def test_divided_power_algebra_has_integral_pd_laws_not_symmetric_multiplication() -> (
    None
):
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    algebra = DividedPowerAlgebraOf(module)
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
    first = module_homset(source, middle)(
        {
            0: middle.module_generator(0) + middle.module_generator(1),
            1: 2 * middle.module_generator(1),
        }
    )
    second = module_homset(middle, target)(
        {0: target.module_generator(0), 1: target.module_generator(1)}
    )

    for functor in (alternating_algebra_functor(ZZ), divided_power_algebra_functor(ZZ)):
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

        identity = functor(module_homset(source, source).identity())
        _assert_power_maps_agree(
            identity,
            functor(source).Hom(functor(source))(
                module_homset(source, source).identity()
            ),
            probes,
        )


def test_canonical_comparison_maps_between_the_four_free_constructions() -> None:
    from dzack_research.preamble.categories.algebras import (
        SymmetricAlgebraOf,
        TensorAlgebraOf,
        divided_to_symmetric,
        symmetric_to_divided,
        tensor_to_alternating,
        tensor_to_symmetric,
    )
    from dzack_research.preamble.all import QQ

    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    tensor = TensorAlgebraOf(module)
    symmetric = SymmetricAlgebraOf(module)
    alternating = AlternatingAlgebraOf(module)
    divided = DividedPowerAlgebraOf(module)
    x_t = tensor.algebra_generator("x")
    y_t = tensor.algebra_generator("y")

    to_symmetric = tensor_to_symmetric(module)
    assert to_symmetric(x_t * y_t - y_t * x_t) == symmetric.zero()

    to_alternating = tensor_to_alternating(module)
    assert to_alternating(x_t * x_t) == alternating.zero()
    assert to_alternating(x_t * y_t + y_t * x_t) == alternating.zero()

    to_divided = symmetric_to_divided(module)
    x_s = symmetric.algebra_generator("x")
    assert to_divided(x_s**3) == 6 * divided.divided_power(
        divided.algebra_generator("x"), 3
    )

    rational_module = BasedFreeModule(QQ, finite_ordered_set(("x", "y")))
    sym_to_div = symmetric_to_divided(rational_module)
    div_to_sym = divided_to_symmetric(rational_module)
    symmetric_q = SymmetricAlgebraOf(rational_module)
    divided_q = DividedPowerAlgebraOf(rational_module)
    x_q = symmetric_q.algebra_generator("x")
    y_q = symmetric_q.algebra_generator("y")
    gamma2x = divided_q.divided_power(divided_q.algebra_generator("x"), 2)
    probe_sym = x_q**2 * y_q + 3 * y_q
    probe_div = gamma2x * divided_q.algebra_generator(
        "y"
    ) + divided_q.algebra_generator("x")
    assert div_to_sym(sym_to_div(probe_sym)) == probe_sym
    assert sym_to_div(div_to_sym(probe_div)) == probe_div
