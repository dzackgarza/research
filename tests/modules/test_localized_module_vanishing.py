r"""Vanishing of a localized module, decided by an ideal computation.

A finitely generated module localizes to zero exactly when its annihilator
meets the inverted set.  Inverting ``x`` kills ``QQ[x]/(x)``, and the
saturation of the annihilator reports that without ever enumerating the
infinite underlying set of the localization.  At a prime the same criterion
says the module is zero away from its support.
"""

from dzack_research.preamble.all import (
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

    assert module.localize(x).is_zero()


def test_inverting_a_scalar_outside_the_annihilator_keeps_the_module() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    module = _cyclic_module(ring, x)

    assert not module.localize(x - ring.one()).is_zero()


def test_a_torsion_module_vanishes_at_a_prime_outside_its_support() -> None:
    module = _cyclic_module(ZZ, ZZ(6))

    assert module.localize_at_prime(ZZ.ideal(ZZ(5))).is_zero()
    assert not module.localize_at_prime(ZZ.ideal(ZZ(3))).is_zero()
