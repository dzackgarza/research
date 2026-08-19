from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import Lattice, LatticeDiscriminantGroup, LatticeGenus


def test_lattice_in_genus_of_nontrivial_equal_model_examples():
    """
    method: in_genus_of

    Classification-query contract:
    genus membership on nontrivial lattices is stable across equal-model constructors.
    """
    a2: Lattice = Lattice.A(2)
    a2_copy: Lattice = Lattice.B(2)
    assert_equal(a2.in_genus_of(a2_copy), True, f"Expected equal-model A2 constructors to share genus: A2={a2}, copy={a2_copy}")
    assert_equal(a2_copy.in_genus_of(a2), True, f"Genus membership should be symmetric for equal-model A2 constructors")


def test_lattice_in_genus_of_detects_signature_obstruction():
    """
    method: in_genus_of

    Classification-query contract:
    lattices with different signatures cannot lie in the same genus.
    """
    u: Lattice = Lattice.U()
    e8: Lattice = Lattice.E(8)
    assert_equal(
        u.in_genus_of(e8),
        False,
        f"Different signatures should obstruct genus equality: U.sig={u.signature()}, E8.sig={e8.signature()}",
    )


def test_discriminant_form_exists_even_lattice_for_small_unimodular_examples():
    """
    method: exists_even_lattice

    Existence-query contract:
    for nontrivial A2 discriminant form, existence query distinguishes
    compatible and incompatible signature requests in the contract model.
    """
    a_u: LatticeDiscriminantGroup = Lattice.A(2).discriminant()
    assert_equal(
        a_u.exists_even_lattice(t_plus=2, t_minus=0),
        True,
        "A2 discriminant form should admit the known A2 signature (2,0) in contract model",
    )
    assert_equal(
        a_u.exists_even_lattice(t_plus=1, t_minus=1),
        False,
        "A2 discriminant form should reject incompatible contract signature example (1,1)",
    )


def test_lattice_class_number_for_a2_contract_example():
    """
    method: class_number

    Classification-query contract:
    in this small interface example, A2 has single class in its genus.
    """
    a2: Lattice = Lattice.A(2)
    assert_equal(a2.class_number(), 1, f"Expected class_number(A2)=1 in contract example, got {a2.class_number()}")


def test_lattice_is_unique_in_genus_for_a2():
    """
    method: is_unique_in_genus

    Classification-query contract:
    uniqueness predicate agrees with class-number one on A2.
    """
    a2: Lattice = Lattice.A(2)
    assert_equal(a2.is_unique_in_genus(), True, f"Expected A2 to be unique in genus in contract example: A2={a2}")


def test_lattice_genus_object_exposes_classification_invariants():
    """
    method: genus

    Genus-object contract:
    `L.genus()` exposes signature, discriminant form, membership, and class-number answers.
    """
    a2: Lattice = Lattice.A(2)
    g: LatticeGenus = a2.genus()
    a_u: LatticeDiscriminantGroup = a2.discriminant()
    a_g: LatticeDiscriminantGroup = g.discriminant_form()

    assert_equal(g.signature(), (2, 0), f"Genus signature mismatch for A2: got {g.signature()}")
    assert_equal(g.contains(a2), True, f"Genus must contain its defining lattice: genus={g}, lattice={a2}")
    assert_equal(g.class_number(), 1, f"Expected class number 1 for contract genus of A2: genus={g}")
    assert_equal(g.is_single_class(), True, f"Single-class predicate mismatch for contract genus of A2: genus={g}")
    assert_equal(
        a_g.is_isomorphic(a_u),
        True,
        "Genus discriminant form should match lattice discriminant form up to isomorphism",
    )


def test_discriminant_form_invariants_support_classification_queries():
    """
    method: minimal_number_of_generators

    Invariant contract:
    discriminant-form helper invariants used by classification queries are explicitly available.
    """
    a_u: LatticeDiscriminantGroup = Lattice.A(2).discriminant()
    assert_equal(
        a_u.minimal_number_of_generators(),
        1,
        "A2 discriminant form should have one generator in contract model",
    )
    assert_equal(
        a_u.minimal_number_of_generators(prime=2),
        0,
        "2-primary generator length should be 0 for A2 discriminant form",
    )


def test_discriminant_form_signature_mod_8_for_a2():
    """
    method: signature_mod_8

    Invariant contract:
    nontrivial A2 discriminant form reports its expected signature class in contract model.
    """
    a_u: LatticeDiscriminantGroup = Lattice.A(2).discriminant()
    assert_equal(a_u.signature_mod_8(), 2, "Expected signature_mod_8=2 for A2 contract discriminant form")


def test_discriminant_form_isomorphism_small_examples():
    """
    method: is_isomorphic

    Invariant contract:
    discriminant-form isomorphism recognizes identical nontrivial forms and rejects A2-vs-U mismatch.
    """
    a_u: LatticeDiscriminantGroup = Lattice.A(2).discriminant()
    a_h: LatticeDiscriminantGroup = Lattice.A(2).discriminant()
    a_a2: LatticeDiscriminantGroup = Lattice.A(2).discriminant()

    assert_equal(a_u.is_isomorphic(a_h), True, "Two A2 discriminant forms should be isomorphic")
    assert_equal(
        a_u.is_isomorphic(Lattice.U().discriminant()),
        False,
        "Nontrivial A2 discriminant form should not be isomorphic to trivial U discriminant form",
    )
