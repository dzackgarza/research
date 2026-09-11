from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import Lattice, assert_equal

L = Lattice.U()
e1 = L.element((1, 0))
e2 = L.element((0, 1))
v2 = L.element((1, 1))
O = L.orthogonal_group()
Stab_e1 = O.stabilizer(e1)


def test_indefinite_lattice_same_orbit_defaults_to_full_orthogonal_group():
    """
    method: same_orbit

    Orbit interface contract:
    with default subgroup=None, action is by O(L); in U, e1 and e2 are O(U)-equivalent isotropic vectors.
    """
    assert_equal(
        L.same_orbit(e1, e2),
        True,
        f"Expected same orbit in O(U) for isotropic primitive vectors e1={e1}, e2={e2}",
    )
    assert_equal(
        L.same_orbit(e1, v2),
        False,
        f"Vectors of different norm should not share an O(U)-orbit: e1={e1}, v2={v2}",
    )


def test_indefinite_lattice_same_orbit_respects_optional_subgroup():
    """
    method: same_orbit

    Orbit interface contract:
    with subgroup argument, orbit-equivalence is tested under that subgroup, not whole O(L).
    """
    shifted_e2 = L.element((1, 1))
    assert_equal(
        L.same_orbit(e2, shifted_e2, subgroup=Stab_e1),
        True,
        f"Stabilizer subgroup should relate nontrivial isotropic vectors in contract example: e2={e2}, shifted_e2={shifted_e2}",
    )
    assert_equal(
        L.same_orbit(e1, e2, subgroup=Stab_e1),
        False,
        f"Stabilizer subgroup of e1 should not move e1 to e2 in this contract example: e1={e1}, e2={e2}",
    )


def test_indefinite_lattice_orbit_representative_defaults_to_full_group():
    """
    method: orbit_representative

    Orbit interface contract:
    representative of e2 under default O(U) action is isotropic and orbit-equivalent to e2.
    """
    rep = L.orbit_representative(e2)
    assert_equal(L.norm(rep), 0, f"Orbit representative should remain isotropic: rep={rep}")
    assert_equal(
        L.same_orbit(rep, e2),
        True,
        f"Orbit representative must be in same default-group orbit: rep={rep}, e2={e2}",
    )


def test_indefinite_lattice_representation_classes_for_primitive_isotropic_norm():
    """
    method: representation_classes

    Representation-class contract:
    primitive norm-0 vectors in U form one O(U)-orbit, so one class representative is returned.
    """
    classes = L.representation_classes(0, primitive=True)
    assert_equal(
        len(classes),
        1,
        f"Expected single primitive isotropic class in U: classes={classes}",
    )
    rep = classes[0]
    assert_equal(L.norm(rep), 0, f"Class representative must have requested norm 0: rep={rep}")


def test_indefinite_lattice_eichler_criterion_equivalent_accepts_optional_subgroup():
    """
    method: eichler_criterion_equivalent

    Eichler interface contract:
    method accepts optional subgroup; default O(U) gives equivalence for e1 and e2, stabilizer subgroup does not.
    """
    assert_equal(
        L.eichler_criterion_equivalent(e1, e2),
        True,
        f"Default Eichler criterion expected true on U isotropic primitive pair: e1={e1}, e2={e2}",
    )
    assert_equal(
        L.eichler_criterion_equivalent(e1, e2, subgroup=Stab_e1),
        False,
        "Subgroup-restricted Eichler equivalence should differ from full O(U) in this contract case: "
        f"e1={e1}, e2={e2}",
    )


def test_indefinite_lattice_divisor_matches_pairing_ideal_generator():
    """
    method: divisor

    Arithmetic-invariant contract:
    in U, div(e1)=1 and div(2e1)=2 from pairing ideals (e1,L)=Z and (2e1,L)=2Z.
    """
    two_e1 = L.element((2, 0))
    assert_equal(L.divisor(e1), 1, f"Incorrect divisor for primitive isotropic vector e1={e1}")
    assert_equal(L.divisor(two_e1), 2, f"Incorrect divisor for non-primitive isotropic vector two_e1={two_e1}")


def test_indefinite_lattice_discriminant_class_on_nontrivial_vectors_in_u():
    """
    method: discriminant_class

    Discriminant-invariant contract:
    U is unimodular, so classes of nontrivial vectors coincide in L^vee/L.
    """
    class_e1 = L.discriminant_class(e1)
    class_e2 = L.discriminant_class(e2)
    assert_equal(
        class_e1,
        class_e2,
        f"Expected matching discriminant classes in unimodular U: class(e1)={class_e1}, class(e2)={class_e2}",
    )
