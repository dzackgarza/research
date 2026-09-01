from itertools import permutations

from sage.arith.misc import factorial

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules import (
    AlternatingPower,
    BasedFreeModule,
    DividedPower,
    FinitelyPresentedTorsionModules,
    SymmetricPower,
    TensorPower,
    divided_power_invariant_inclusion,
    divided_power_morphism,
    module_homset,
    symmetric_power_morphism,
    tensor_power_permutation,
    tensor_power_polarization,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().module_generating_set():
        generator = left.domain().module_generator(label)
        assert left(generator) == right(generator)


def test_degree_powers_have_the_expected_free_ranks_and_use_canonical_tensor_products() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    assert TensorPower(module, 2) is TensorPower(module, 2)
    assert TensorPower(module, 3) is TensorPower(module, 3)
    assert TensorPower(module, 2).rank() == 4
    assert SymmetricPower(module, 2).rank() == 3
    assert AlternatingPower(module, 2).rank() == 1
    assert AlternatingPower(module, 3).rank() == 0
    assert DividedPower(module, 3).rank() == 4


def test_integral_divided_powers_distinguish_gamma_from_symmetric_powers() -> None:
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2,))

    assert tuple(TensorPower(module, 3).invariants()) == (2,)
    assert tuple(SymmetricPower(module, 3).invariants()) == (2,)
    assert tuple(DividedPower(module, 2).invariants()) == (4,)
    assert tuple(DividedPower(module, 3).invariants()) == (2,)
    assert tuple(DividedPower(module, 4).invariants()) == (8,)


def test_divided_power_inclusion_and_polarization_are_norm_and_orbit_sum() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    for degree in (2, 3):
        divided = DividedPower(module, degree)
        tensor = TensorPower(module, degree)
        inclusion = divided_power_invariant_inclusion(module, degree)
        polarization = tensor_power_polarization(module, degree)

        for label in divided.module_generating_set():
            generator = divided.module_generator(label)
            assert polarization(inclusion(generator)) == factorial(degree) * generator

        orbit_sum = tuple(permutations(range(degree)))
        for label in tensor.module_generating_set():
            generator = tensor.module_generator(label)
            expected = sum(
                (tensor_power_permutation(module, degree, sigma)(generator) for sigma in orbit_sum),
                tensor.zero(),
            )
            assert inclusion(polarization(generator)) == expected


def test_symmetric_and_divided_powers_are_functorial_on_nontrivial_maps() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    x = module.module_generator("x")
    y = module.module_generator("y")
    shear = module_homset(module, module)({"x": x + y, "y": y})
    scale = module_homset(module, module)({"x": 2 * x, "y": 3 * y})

    for degree, power_morphism in (
        (2, symmetric_power_morphism),
        (3, symmetric_power_morphism),
        (2, divided_power_morphism),
        (3, divided_power_morphism),
    ):
        composite = power_morphism(scale * shear, degree)
        stepwise = power_morphism(scale, degree) * power_morphism(shear, degree)
        _assert_maps_agree(composite, stepwise)

        identity = power_morphism(module_homset(module, module).identity(), degree)
        _assert_maps_agree(identity, module_homset(identity.domain(), identity.codomain()).identity())
