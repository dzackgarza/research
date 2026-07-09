r"""Design ruling 2026-07-09 (issue #3 correction): constructors live on
``Lattice`` itself and handle all routing -- subcategory membership is OUTPUT,
never input. You construct E8 as a lattice and you GET a root-generated
lattice; you never need to know its subcategory to construct it.

The lattice name ("E8", "U", ("A", 2)) is construction data, so routing it to
provenance is NOT Gram-detection: the same Gram passed as a raw matrix still
carries no RootGenerated certificate.

Vault decision: constructors-live-on-lattice-itself-subcategory-membership-is-
output-not-input.
"""
from __future__ import annotations

import pytest

from sage.all import QQ, ZZ, matrix
from sage.combinat.root_system.cartan_matrix import CartanMatrix

from sage_lattice_category_spike.lattice_categories import Lattice, Lattices


def test_named_construction_yields_root_generated_membership():
    assert Lattice("A2") in Lattices(ZZ).Even().RootGenerated()
    assert Lattice("E8") in Lattices(ZZ).Even().RootGenerated()
    assert Lattice(("D", 4)) in Lattices(ZZ).Even().RootGenerated()


def test_named_construction_carries_the_cartan_datum():
    assert Lattice("E8").cartan_type() == ("E", 8)
    assert Lattice(("A", 2)).cartan_type() == ("A", 2)


def test_negative_twist_routes_through_lattice_itself():
    E8_neg = Lattice("E8", negative=True)
    assert E8_neg.signature_pair() == (0, 8)
    assert E8_neg in Lattices(ZZ).Even().RootGenerated()
    assert E8_neg.cartan_type() == ("E", 8)


def test_raw_gram_matrix_never_acquires_the_certificate():
    # Same Gram, no name: provenance is construction data, never Gram-detected.
    a2_gram = matrix(QQ, CartanMatrix(["A", 2]))
    assert Lattice(a2_gram) not in Lattices(ZZ).Even().RootGenerated()


def test_hyperbolic_plane_by_name_routes_to_hyperbolic():
    L = Lattice("U")
    assert L in Lattices(ZZ).Indefinite().Hyperbolic()
    assert L not in Lattices(ZZ).Even().RootGenerated()


def test_named_construction_defaults_label_to_the_name():
    assert "A2" in repr(Lattice("A2"))
    assert "E8" in repr(Lattice("E8", negative=True))


def test_names_compose_with_name_routing():
    L.<e, f> = Lattice("U")
    assert repr(2 * e - f) == "2*e - f"
    R.<r1, r2> = Lattice("A2")
    assert repr(r1 + r2) == "r1 + r2"
    assert R in Lattices(ZZ).Even().RootGenerated()


def test_unknown_name_fails_loudly():
    with pytest.raises(AssertionError):
        Lattice("Z5")


def test_negative_twist_requires_a_named_lattice():
    with pytest.raises(AssertionError):
        Lattice(matrix(ZZ, [[2]]), negative=True)


def test_there_is_no_public_root_lattice_constructor():
    # Membership is output, not input: no subcategory-named constructor surface.
    with pytest.raises(ImportError):
        from sage_lattice_category_spike.lattice_categories import RootLattice  # noqa: F401


def test_there_is_no_public_u_constructor():
    # U(n) is composable from existing primitives; a dedicated constructor
    # (let alone string vocabulary like "U(2)") duplicates the algebra.
    with pytest.raises(ImportError):
        from sage_lattice_category_spike.lattice_categories import U  # noqa: F401


def test_scaled_hyperbolic_plane_is_composed_not_dispatched():
    U2 = Lattice("U").twist(2)
    assert U2.gram_matrix() == matrix(QQ, [[0, 2], [2, 0]])
    assert U2 in Lattices(ZZ).Indefinite().Hyperbolic()
