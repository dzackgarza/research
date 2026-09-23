from itertools import permutations

from sage.arith.misc import factorial

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules import (
    FinitelyPresentedTorsionModules,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().module_generating_set():
        generator = left.domain().module_generator(label)
        assert left(generator) == right(generator)


def test_degree_powers_have_the_expected_free_ranks_and_use_canonical_tensor_products() -> None:
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    assert module.tensor_power(2) is module.tensor_power(2)
    assert module.tensor_power(3) is module.tensor_power(3)
    assert module.tensor_power(2).module_rank() == 4
    assert module.symmetric_power(2).module_rank() == 3
    assert module.exterior_power(2).module_rank() == 1
    assert module.exterior_power(3).module_rank() == 0
    assert module.divided_power_module(3).module_rank() == 4


def test_integral_divided_powers_distinguish_gamma_from_symmetric_powers() -> None:
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2,))

    _factors = module.tensor_power(3).invariant_factors()
    assert _factors.cardinality() == 1
    assert _factors[0] == 2

    _factors = module.symmetric_power(3).invariant_factors()
    assert _factors.cardinality() == 1
    assert _factors[0] == 2
    _factors = module.divided_power_module(2).invariant_factors()
    assert _factors.cardinality() == 1
    assert _factors[0] == 4
    _factors = module.divided_power_module(3).invariant_factors()
    assert _factors.cardinality() == 1
    assert _factors[0] == 2
    _factors = module.divided_power_module(4).invariant_factors()
    assert _factors.cardinality() == 1
    assert _factors[0] == 8


def test_divided_power_inclusion_and_polarization_are_norm_and_orbit_sum() -> None:
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    for degree in (2, 3):
        divided = module.divided_power_module(degree)
        tensor = module.tensor_power(degree)
        inclusion = module.divided_power_invariant_inclusion(degree)
        polarization = module.tensor_power_polarization(degree)

        for label in divided.module_generating_set():
            generator = divided.module_generator(label)
            assert polarization(inclusion(generator)) == ZZ(int(factorial(degree))) * generator

        orbit_sum = tuple(permutations(range(degree)))
        for label in tensor.module_generating_set():
            generator = tensor.module_generator(label)
            expected = sum(
                (module.tensor_power_permutation(degree, sigma)(generator) for sigma in orbit_sum),
                tensor.zero(),
            )
            assert inclusion(polarization(generator)) == expected


def test_symmetric_and_divided_powers_are_functorial_on_nontrivial_maps() -> None:
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    x = module.module_generator("x")
    y = module.module_generator("y")
    shear = module.module_category().Mor(module, module)({"x": x + y, "y": y})
    scale = module.module_category().Mor(module, module)({"x": 2 * x, "y": 3 * y})

    for induced_power in (
        lambda morphism: morphism.symmetric_power(2),
        lambda morphism: morphism.symmetric_power(3),
        lambda morphism: morphism.divided_power(2),
        lambda morphism: morphism.divided_power(3),
    ):
        composite = induced_power(scale * shear)
        stepwise = induced_power(scale) * induced_power(shear)
        _assert_maps_agree(composite, stepwise)

        identity = induced_power(module.module_category().Mor(module, module).identity())
        identity_domain = identity.domain()
        identity_codomain = identity.codomain()
        _assert_maps_agree(
            identity,
            identity_domain.module_category().Mor(identity_domain, identity_codomain).identity(),
        )


