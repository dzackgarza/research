from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import Lattice, LatticeAutomorphism, assert_equal

L = Lattice.U()
O = L.orthogonal_group()


def test_indefinite_lattice_isotropic_existence_and_witness_contract():
    """
    method: isotropic_vector

    Orbit prerequisites:
    U contains nonzero isotropic vectors and lattice/element norm APIs agree on them.
    """
    assert_equal(L.has_isotropic_vector(), True, "IndefiniteLattice.has_isotropic_vector mismatch")

    x = L.isotropic_vector()
    assert tuple(x.coords()) != (0, 0), f"IndefiniteLattice.isotropic_vector returned zero: x={x}"

    assert_equal((L.norm(x), x.norm()), (0, 0), "IndefiniteLattice isotropic norm mismatch")


def test_indefinite_lattice_primitive_isotropic_vectors_contains_standard_rays():
    """
    method: primitive_isotropic_vectors

    Orbit prerequisites:
    primitive isotropic ray enumeration in U includes +-e1 and +-e2 for small bound.
    """
    vs = L.primitive_isotropic_vectors(bound=1)
    as_tuples = {tuple(v.coords()) for v in vs}
    expected_subset = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    missing = sorted(expected_subset - as_tuples)
    assert not missing, (
        "IndefiniteLattice.primitive_isotropic_vectors missing expected rays: "
        f"missing={missing}, actual={sorted(as_tuples)}"
    )


def test_indefinite_lattice_isotropic_orbit_representatives_contract():
    """
    method: isotropic_orbit_representatives

    Orbit contract:
    representatives are isotropic and pairwise non-conjugate under O(U).
    """
    reps = L.isotropic_orbit_representatives(bound=4, primitive=True)
    rep_coords = {tuple(r.coords()) for r in reps}
    expected_primitive_isotropic_rays = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    assert rep_coords & expected_primitive_isotropic_rays, (
        "isotropic_orbit_representatives missing canonical primitive isotropic rays: "
        f"rep_coords={sorted(rep_coords)}"
    )

    for r in reps:
        assert_equal((L.norm(r), r.norm()), (0, 0), f"Orbit representative is not isotropic: rep={r}")

    for i, ri in enumerate(reps):
        for rj in reps[i + 1 :]:
            assert_equal(
                O.same_orbit(ri, rj),
                False,
                f"Distinct orbit representatives must be non-conjugate: ri={ri}, rj={rj}",
            )


def test_orthogonal_group_orbit_of_isotropic_vector_contract():
    """
    method: orbit

    Orbit contract:
    vectors in `O(U).orbit(x)` are isotropic and each lies in the same orbit as x.
    """
    x = L.isotropic_vector()
    orb = O.orbit(x, bound=8)
    x_coords = tuple(x.coords())
    orb_coords = {tuple(y.coords()) for y in orb}
    assert x_coords in orb_coords, (
        f"OrthogonalGroup.orbit should contain the seed vector: x={x_coords}, orbit={sorted(orb_coords)}"
    )

    for y in orb:
        assert_equal((L.norm(y), y.norm()), (0, 0), f"Orbit vector is not isotropic: y={y}")
        assert_equal(O.same_orbit(x, y), True, f"Orbit membership mismatch: x={x}, y={y}")


def test_orthogonal_group_stabilizer_contains_nontrivial_isometry():
    """
    method: stabilizer

    Orbit contract:
    stabilizer subgroup is checked with a nontrivial lattice isometry witness.
    """
    x = L.isotropic_vector()
    stab = O.stabilizer(x)
    swap = LatticeAutomorphism(L, ((0, 1), (1, 0)))
    assert_equal(stab.contains(swap), True, f"Stabilizer should contain nontrivial swap isometry: vector={x}")
