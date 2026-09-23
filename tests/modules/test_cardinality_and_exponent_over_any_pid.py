r"""Cardinality and exponent read from the base ring, not from the integers.

Over a principal ideal domain ``M`` decomposes as ``R^r`` together with the
cyclic quotients of its nonzero non-unit invariant factors, so the cardinality
of its underlying set is ``|R|^r`` times the orders of those quotients, and its
exponent is the one generator of ``Ann_R(M)``.  Neither statement mentions the
integers, and ``GF(5)[t]`` exhibits both without them.
"""

from dzack_research.preamble.all import (
    GF,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic_module(ring, scalar):
    r"""Return ``R/(scalar)`` presented on one generator."""
    free = ring.free_module(finite_ordered_set(("g",)))
    relations = ring.free_module(finite_ordered_set(("r",)))
    return relations.module_category().Mor(relations, free)(
            {"r": free.scalar_multiple(scalar, free.module_generator("g"))}
        ).cokernel()


def test_a_cyclic_module_over_a_polynomial_pid_counts_its_residues() -> None:
    ring = GF(5).polynomial_ring("t")
    t = ring.algebra_generator("t")
    module = _cyclic_module(ring, t**2)

    assert module.cardinality() == 25
    assert module.cardinality().is_finite()
    assert module.exponent() == t**2






