r"""Cardinality and exponent read from the base ring, not from the integers.

Over a principal ideal domain ``M`` decomposes as ``R^r`` together with the
cyclic quotients of its nonzero non-unit invariant factors, so the cardinality
of its underlying set is ``|R|^r`` times the orders of those quotients, and its
exponent is the one generator of ``Ann_R(M)``.  Neither statement mentions the
integers, and ``GF(5)[t]`` exhibits both without them.
"""

from dzack_research.preamble.all import GF, Modules


def test_F5t_mod_t_squared_has_25_elements_and_exponent_t_squared() -> None:
    r"""\(\mathbb F_5[t]/(t^2)\) has \(\mathbb F_5\)-basis \(1, t\), so \(5^2 = 25\) elements,
    and \(\operatorname{Ann}(\mathbb F_5[t]/(t^2)) = (t^2)\)."""
    ring = GF(5)["t"]
    t = ring.gen()
    free = Modules(ring)(ring**1)
    (g,) = free.module_generators()
    relations = Modules(ring)(ring**1)
    (r,) = relations.module_generators()
    module = relations.Mor(free)({r: t**2 * g}).cokernel()

    assert module.cardinality() == 25
    assert module.exponent() == t**2
    assert module.annihilator() == ring.ideal(t**2)
