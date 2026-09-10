r"""Archive reconciliation for algebra scalar extension.

The archived ``AlgebraBaseChangeFunctor(f)`` is now the left adjoint of the
live algebra scalar-extension/restriction adjunction.  This specimen retains
its two essential operations: carrying a finite presentation from ``ZZ`` to
``QQ`` and carrying a nonidentity algebra morphism through the same functor.
"""

from dzack_research.preamble.all import (
    FinitelyPresentedAlgebra,
    QQ,
    SymmetricAlgebraOn,
    ZZ,
    algebra_base_change_adjunction,
)
from dzack_research.preamble.categories.rings import ring_homset


def _quadratic_integer_algebra():
    polynomial = SymmetricAlgebraOn(ZZ, ("x",))
    x = polynomial.algebra_generator("x")
    return FinitelyPresentedAlgebra(polynomial, (x**2 - 2,))


def test_archived_algebra_base_change_is_the_live_scalar_extension_functor() -> None:
    algebra = _quadratic_integer_algebra()
    ring_map = ring_homset(ZZ, QQ)(lambda scalar: QQ(scalar))
    extension = algebra_base_change_adjunction(ring_map).left_adjoint()
    extended = extension(algebra)

    assert extended.base_ring() is QQ
    assert extended.algebra_generating_set() is algebra.algebra_generating_set()
    generator = extended.algebra_generator("x")
    assert generator**2 == extended(2)
    assert extended.relations().cardinality() == algebra.relations().cardinality()


def test_archived_algebra_base_change_carries_a_nonidentity_morphism() -> None:
    algebra = _quadratic_integer_algebra()
    involution = algebra.Mor(algebra)(
        {"x": -algebra.algebra_generator("x")}
    )
    ring_map = ring_homset(ZZ, QQ)(lambda scalar: QQ(scalar))
    extension = algebra_base_change_adjunction(ring_map).left_adjoint()
    extended = extension(algebra)
    extended_involution = extension(involution)
    generator = extended.algebra_generator("x")

    assert extended_involution.domain() is extended
    assert extended_involution.codomain() is extended
    assert extended_involution(generator) == -generator
