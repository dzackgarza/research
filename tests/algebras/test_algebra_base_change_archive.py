r"""Archive reconciliation for algebra scalar extension.

The archived ``AlgebraBaseChangeFunctor(f)`` is now the left adjoint of the
live algebra scalar-extension/restriction adjunction.  This specimen retains
its two essential operations: carrying a finite presentation from ``ZZ`` to
``QQ`` and carrying a nonidentity algebra morphism through the same functor.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FinitelyPresentedAlgebra,
    PolynomialRing,
    SymmetricAlgebraOn,
    algebra_base_change_adjunction,
)


ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/functors/algebra_base_change.sage",
    "live_owner": "src/dzack_research/preamble/categories/functors/algebra_scalar_change.py",
    "disposition": "reconciled-live-owner",
}


def _quadratic_integer_algebra():
    polynomial = SymmetricAlgebraOn(ZZ, ("x",))
    x = polynomial.algebra_generator("x")
    return FinitelyPresentedAlgebra(polynomial, (x**2 - 2,))


def test_archived_algebra_base_change_is_the_live_scalar_extension_functor() -> None:
    algebra = _quadratic_integer_algebra()
    ring_map = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))
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
    ring_map = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))
    extension = algebra_base_change_adjunction(ring_map).left_adjoint()
    extended = extension(algebra)
    extended_involution = extension(involution)
    generator = extended.algebra_generator("x")

    assert extended_involution.domain() is extended
    assert extended_involution.codomain() is extended
    assert extended_involution(generator) == -generator


def test_base_change_adjunction_retains_the_selected_ring_map_identity() -> None:
    first = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))
    second = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))

    first_adjunction = algebra_base_change_adjunction(first)
    second_adjunction = algebra_base_change_adjunction(second)

    assert first_adjunction is algebra_base_change_adjunction(first)
    assert second_adjunction is algebra_base_change_adjunction(second)
    assert first_adjunction is not second_adjunction
    assert first_adjunction.left_adjoint().ring_map() is first
    assert second_adjunction.left_adjoint().ring_map() is second


def test_scalar_restriction_retains_the_selected_ring_map_identity() -> None:
    algebra = PolynomialRing(QQ, "x")
    first_map = QQ.Mor(QQ).identity()
    second_map = QQ.Mor(QQ).identity()

    first = algebra.restrict_scalars(first_map)
    second = algebra.restrict_scalars(second_map)

    assert first is algebra.restrict_scalars(first_map)
    assert second is algebra.restrict_scalars(second_map)
    assert first is not second
    assert first.ring_map() is first_map
    assert second.ring_map() is second_map
