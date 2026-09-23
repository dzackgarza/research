r"""Vanishing of a localized module, decided by an ideal computation.

A finitely generated module localizes to zero exactly when its annihilator
meets the inverted set.  Inverting ``x`` kills ``QQ[x]/(x)``, and the
saturation of the annihilator reports that without ever enumerating the
infinite underlying set of the localization.  At a prime the same criterion
says the module is zero away from its support.
"""

from dzack_research.preamble.all import (
    AdditiveGroups,
    QQ,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic_module(ring, scalar):
    r"""Return ``R/(scalar)`` presented on one generator."""
    free = ring.free_module(finite_ordered_set(("g",)))
    relations = ring.free_module(finite_ordered_set(("r",)))
    return relations.module_category().Mor(relations, free)(
            {"r": free.scalar_multiple(scalar, free.module_generator("g"))}
        ).cokernel()


def test_inverting_the_annihilator_kills_a_cyclic_module() -> None:
    ring = QQ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    module = _cyclic_module(ring, x)

    localized = module.localize(x)

    assert localized.is_zero()
    assert localized.scalar_action().codomain() is AdditiveGroups().AdditiveCommutative().End(
        localized.underlying_additive_group()
    )


def test_inverting_a_scalar_outside_the_annihilator_keeps_the_module() -> None:
    ring = QQ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    module = _cyclic_module(ring, x)

    assert not module.localize(x - ring.one()).is_zero()


def test_a_torsion_module_vanishes_at_a_prime_outside_its_support() -> None:
    module = _cyclic_module(ZZ, ZZ(6))

    assert module.localize_at_prime(ZZ.ideal(ZZ(5))).is_zero()
    assert not module.localize_at_prime(ZZ.ideal(ZZ(3))).is_zero()


