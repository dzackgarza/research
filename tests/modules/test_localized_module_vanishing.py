r"""Vanishing of a localized module, decided by an ideal computation.

A finitely generated module localizes to zero exactly when its annihilator
meets the inverted set.  Inverting ``x`` kills ``QQ[x]/(x)``, and the
saturation of the annihilator reports that without ever enumerating the
infinite underlying set of the localization.  At a prime the same criterion
says the module is zero away from its support.
"""

from dzack_research.preamble.all import (
    AdditiveGroups,
    BasedFreeModule,
    FinitelyPresentedModule,
    PolynomialRing,
    QQ,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic_module(ring, scalar):
    r"""Return ``R/(scalar)`` presented on one generator."""
    free = BasedFreeModule(ring, finite_ordered_set(("g",)))
    relations = BasedFreeModule(ring, finite_ordered_set(("r",)))
    return FinitelyPresentedModule(
        module_homset(relations, free)(
            {"r": free.scalar_multiple(scalar, free.module_generator("g"))}
        )
    )


def test_inverting_the_annihilator_kills_a_cyclic_module() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    module = _cyclic_module(ring, x)

    localized = module.localize(x)

    assert localized.is_zero()
    assert localized.scalar_action().codomain() is AdditiveGroups().AdditiveCommutative().End(
        localized.underlying_additive_group()
    )


def test_inverting_a_scalar_outside_the_annihilator_keeps_the_module() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    module = _cyclic_module(ring, x)

    assert not module.localize(x - ring.one()).is_zero()


def test_a_torsion_module_vanishes_at_a_prime_outside_its_support() -> None:
    module = _cyclic_module(ZZ, ZZ(6))

    assert module.localize_at_prime(ZZ.ideal(ZZ(5))).is_zero()
    assert not module.localize_at_prime(ZZ.ideal(ZZ(3))).is_zero()


def test_localizing_a_free_module_preserves_its_fraction_action_and_map() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    free = BasedFreeModule(ring, finite_ordered_set(("g",)))
    generator = free.module_generator("g")
    localized = free.localize(x)

    assert localized.scalar_action().codomain() is AdditiveGroups().AdditiveCommutative().End(
        localized.underlying_additive_group()
    )
    assert localized.scalar_multiple(
        localized.base_ring()(x), localized.module_generator("g")
    ) == localized.fraction(free.scalar_multiple(x, generator))

    doubling = module_homset(free, free)(
        {"g": free.scalar_multiple(ring(2), generator)}
    )
    localized_doubling = localized.localization_functor()(doubling)
    assert localized_doubling(localized.module_generator("g")) == localized.scalar_multiple(
        localized.base_ring()(2), localized.module_generator("g")
    )
