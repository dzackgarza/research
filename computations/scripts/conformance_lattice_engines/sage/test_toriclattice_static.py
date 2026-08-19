from __future__ import annotations

import sage.all  # noqa: F401
from sage.all import IntegralLattice, ZZ, matrix
from sage.geometry.cone import Cone
from sage.geometry.toric_lattice import ToricLattice
from .conftest import assert_equal


def test_toriclattice_dual_pairing_matches_coordinate_dot_product():
    """
    method: dual_pairing

    ToricLattice N and dual lattice M have canonical integer pairing n*m.
    Assertion: Pairing equals coordinate dot product on a concrete pair.
    """
    N = ToricLattice(2)
    M = N.dual()
    n = N(1, -2)
    m = M(3, 5)
    actual = n * m
    expected = 1 * 3 + (-2) * 5
    assert_equal(actual, expected, "ToricLattice dual pairing mismatch")


def test_toriclattice_cone_dual_involution_preserves_ray_count():
    """
    method: cone_dual

    Cone duality over ToricLattice is an involution up to cone equivalence.
    Assertion: Double dual preserves the number of rays.
    """
    N = ToricLattice(2)
    C = Cone([(1, 0), (0, 1)], lattice=N)
    Cdd = C.dual().dual()
    actual = len(Cdd.rays())
    expected = len(C.rays())
    assert_equal(actual, expected, "Cone dual involution mismatch")


def test_toric_cone_accepts_integrallattice_as_lattice_parameter():
    """
    method: cone_from_integrallattice

    Cone(..., lattice=L) accepts free Z-modules beyond ToricLattice, including IntegralLattice.
    Assertion: Cone lattice rank equals the provided lattice rank.
    """
    L = IntegralLattice([[2, 0], [0, 2]])
    C = Cone([(1, 0), (0, 1)], lattice=L)
    actual = C.lattice().rank()
    expected = L.rank()
    assert_equal(actual, expected, "Cone lattice rank mismatch")


def test_integrallattice_cannot_be_built_directly_from_toriclattice_parent():
    """
    method: integrallattice_from_toriclattice_parent

    A ToricLattice parent contributes canonical basis data for an IntegralLattice model.
    Assertion: Parent basis induces the rank-2 identity Gram matrix lattice.
    """
    N = ToricLattice(2)
    L = IntegralLattice(N.basis_matrix())
    actual = (L.rank(), L.gram_matrix())
    expected = (2, matrix(ZZ, [[1, 0], [0, 1]]))
    assert_equal(actual, expected, "IntegralLattice from ToricLattice parent-basis mismatch")


def test_integrallattice_can_be_built_from_toriclattice_basis_matrix():
    """
    method: integrallattice_from_toriclattice_basis_matrix

    A ToricLattice basis matrix can be used to construct an IntegralLattice.
    Assertion: Toric rank-2 standard basis yields identity Gram matrix.
    """
    N = ToricLattice(2)
    L = IntegralLattice(N.basis_matrix())
    actual = L.gram_matrix()
    expected = ZZ.one() * L.gram_matrix().parent().identity_matrix()
    assert_equal(actual, expected, "IntegralLattice from ToricLattice basis mismatch")
