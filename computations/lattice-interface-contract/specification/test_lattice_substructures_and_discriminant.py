from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from fractions import Fraction

from .conftest import Lattice, assert_equal

U = Lattice.U()


def test_lattice_element_perp_returns_sublattice_contract():
    """
    method: perp

    Substructure contract:
    for isotropic e in U, e.perp() is a rank-1 degenerate sublattice of ambient U.
    """
    e = U.element([1, 0])
    e_perp = e.perp()

    assert_equal(e_perp.rank(), 1, f"Element perp rank mismatch: element={tuple(e.coords())}")
    assert_equal(e_perp.determinant(), 0, f"Element perp determinant mismatch: element={tuple(e.coords())}")
    assert_equal(e_perp.contains(e), True, f"Element perp containment mismatch: element={tuple(e.coords())}")
    assert_equal(e_perp.ambient(), U, "Element perp ambient mismatch")


def test_lattice_quotient_by_sublattice_contract():
    """
    method: quotient

    Quotient contract:
    for A2 and a rank-1 sublattice, quotient has nontrivial 3-torsion.
    """
    a2 = Lattice.A(2)
    s = a2.sublattice([a2.element([1, 0])])
    quotient = a2.quotient(by=s)
    e = quotient.element(1)
    two_e = e + e

    assert_equal(quotient.order(), 3, "A2 quotient order mismatch for rank-1 sublattice")
    assert_equal(two_e, -e, f"Expected nontrivial 3-torsion relation 2e=-e in quotient: e={e}, two_e={two_e}")


def test_lattice_dual_returns_expected_type_behavior_contract():
    """
    method: dual

    Dual contract:
    E8 is unimodular so E8^vee has determinant 1 and trivial discriminant.
    A2 has determinant 3 so A2^vee has determinant 1/3.
    """
    e8 = Lattice.E(8)
    e8_dual = e8.dual()
    assert_equal((e8_dual.determinant(), e8_dual.discriminant().order()), (1, 1), "E8 dual invariant mismatch")

    a2 = Lattice.A(2)
    a2_dual = a2.dual()
    assert_equal(a2_dual.determinant(), Fraction(1, 3), "A2 dual determinant mismatch")


def test_lattice_discriminant_group_order_contract():
    """
    method: discriminant

    Discriminant contract:
    A2 has discriminant group of order 3.
    """
    a2 = Lattice.A(2)
    disc = a2.discriminant()
    assert_equal(disc.order(), 3, "A2 discriminant order mismatch")


def test_discriminant_group_quadratic_form_contract():
    """
    method: quadratic

    Discriminant-group contract:
    for A2 discriminant group Z/3 with generator g:
    - ord(g) = 3
    - q(g) = 2/3
    - 3g = 0
    """
    disc = Lattice.A(2).discriminant()
    g = disc.generator(0)
    two_g = g + g

    assert_equal(g.order(), 3, "Discriminant element order mismatch")
    assert_equal(disc.quadratic(g), Fraction(2, 3), "Discriminant quadratic mismatch")
    assert_equal(two_g, -g, f"Expected nontrivial relation 2g=-g in discriminant group: g={g}, two_g={two_g}")


def test_discriminant_group_bilinear_form_contract():
    """
    method: bilinear

    Discriminant-group contract:
    for A2 discriminant group Z/3 with generator g, bilinear self-pairing is 2/3.
    """
    disc = Lattice.A(2).discriminant()
    g = disc.generator(0)

    assert_equal(disc.bilinear(g, g), Fraction(2, 3), "Discriminant bilinear mismatch")
