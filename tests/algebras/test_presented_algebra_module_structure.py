r"""A presented algebra answers for its module structure from its construction.

The Gaussian field presented over the rationals, \(\mathbf{Q}[x]/(x^2+1)\), is
an algebra over \(\mathbf{Q}\) and therefore a \(\mathbf{Q}\)-module, free of
rank two on \(1\) and \(i\).  The scalar ring is stated once, by the algebra
level, and travels through the ring level to the host, so every question the
module level asks -- what the scalars are, what the generators are, how a
scalar acts -- is answered by the construction.

The two assertions on ``base`` and ``base_ring`` are the ones that separate a
threaded construction from a restated one: the algebra level declares the
ring, and nothing below it repeats the declaration.
"""

from dzack_research.preamble.all import (
    FinitelyGeneratedFreeModules,
    Modules,
    QQ,
    QuadraticField,
    cardinal,
)


def _gaussian_algebra():
    r"""Return ``QQ[x]/(x^2+1)``, the Gaussian field on its chosen presentation."""
    return QuadraticField(-1, "i").as_algebra()


def test_the_scalar_ring_reaches_the_host_from_the_algebra_level() -> None:
    gaussian = _gaussian_algebra()

    assert gaussian.base() is QQ
    assert gaussian.base_ring() is QQ
    assert gaussian in Modules(QQ)
    assert gaussian in FinitelyGeneratedFreeModules(QQ)


def test_the_gaussian_algebra_is_free_of_rank_two_on_one_and_i() -> None:
    gaussian = _gaussian_algebra()
    primitive = gaussian.algebra_generator("i")

    assert gaussian.number_of_module_generators() == cardinal(2)
    assert tuple(gaussian.module_generators()) == (gaussian.one(), primitive)
    assert primitive * primitive == -gaussian.one()


def test_the_rationals_act_on_the_gaussian_algebra_through_the_module_level() -> None:
    gaussian = _gaussian_algebra()
    primitive = gaussian.algebra_generator("i")
    half = QQ(1) / QQ(2)

    assert gaussian.scalar_multiple(QQ(3), primitive) == primitive + primitive + primitive
    assert gaussian.scalar_multiple(half, primitive) + gaussian.scalar_multiple(half, primitive) == primitive
    assert gaussian.scalar_multiple(QQ(2), gaussian.one() + primitive) == gaussian(2) + gaussian.scalar_multiple(QQ(2), primitive)
