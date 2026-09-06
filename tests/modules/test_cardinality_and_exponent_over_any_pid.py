r"""Cardinality and exponent read from the base ring, not from the integers.

Over a principal ideal domain ``M`` decomposes as ``R^r`` together with the
cyclic quotients of its nonzero non-unit invariant factors, so the cardinality
of its underlying set is ``|R|^r`` times the orders of those quotients, and its
exponent is the one generator of ``Ann_R(M)``.  Neither statement mentions the
integers, and ``GF(5)[t]`` exhibits both without them.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedModule,
    GF,
    PolynomialRing,
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


def test_a_cyclic_module_over_a_polynomial_pid_counts_its_residues() -> None:
    ring = PolynomialRing(GF(5), "t")
    t = ring.algebra_generator("t")
    module = _cyclic_module(ring, t**2)

    assert module.cardinality() == 25
    assert module.cardinality().is_finite()
    assert module.exponent() == t**2


def test_a_free_module_over_a_polynomial_pid_is_infinite_with_zero_exponent() -> None:
    ring = PolynomialRing(GF(5), "t")
    module = BasedFreeModule(ring, finite_ordered_set(("x", "y")))

    assert not module.cardinality().is_finite()
    assert module.exponent() == ring.zero()


def test_a_finite_abelian_group_keeps_its_order_and_exponent() -> None:
    module = _cyclic_module(ZZ, ZZ(6))

    assert module.cardinality() == 6
    assert module.exponent() == ZZ(6)


def test_the_zero_module_is_the_only_one_with_a_unit_exponent() -> None:
    zero = _cyclic_module(ZZ, ZZ(1))
    nonzero = _cyclic_module(ZZ, ZZ(6))

    assert zero.cardinality() == 1
    assert zero.exponent().is_unit()
    assert not nonzero.exponent().is_unit()
