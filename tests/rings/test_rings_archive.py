r"""Archive reconciliation for the core owned-ring surface.

The archived ring category supplied polynomial extensions, free module powers,
the canonical algebra structure over the ring itself, centers/centrality and
prime fields.  These are now operations of the live owned ring rather than an
installed compatibility layer.
"""

from dzack_research.preamble.all import (
    CommutativeRings,
    MatrixSpace,
    Modules,
    OwnedRings,
    PrimeField,
    PrimeFields,
    QQ,
    ZZ,
)


def test_archived_ring_polynomial_and_module_constructions_are_live_operations() -> None:
    polynomial = QQ["x, y"]
    x, y = polynomial.algebra_generators()
    plane = QQ**2

    assert polynomial in OwnedRings()
    assert tuple(polynomial.algebra_generating_set()) == ("x", "y")
    assert x.parent() is polynomial
    assert y.parent() is polynomial
    assert plane in Modules(QQ)
    assert plane.module_rank() == 2


def test_archived_ring_center_and_centrality_are_live_subring_semantics() -> None:
    matrices = MatrixSpace(QQ, 2)
    center = matrices.ring_center()

    assert center in OwnedRings()
    assert center in CommutativeRings()
    assert center.ambient_ring() is matrices
    assert center.inclusion().codomain() is matrices
    assert matrices.one() in center
    assert matrices.is_central(matrices.one()) is True
    noncentral = next(iter(matrices.algebra_generators()))
    assert noncentral not in center
    assert matrices.is_central(noncentral) is False


def test_archived_prime_field_constructor_is_live_category_placement() -> None:
    field = PrimeField(5)

    assert field in PrimeFields()
    assert field in OwnedRings()
    assert field.characteristic() == ZZ(5)
    assert field.ring_center() is field
