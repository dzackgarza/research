from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.modules.free_module_integer import IntegerLattice
from .conftest import assert_runtime_methods_covered


def test_integerlattice_discriminant_matches_det_bbt():
    """
    method: discriminant

    discriminant() is det(B*B^T) for the Euclidean embedded basis matrix B.
    Assertion: Rank-2 diagonal basis gives the expected determinant 4.
    """
    L = IntegerLattice([[1, 0], [0, 2]])
    actual = L.discriminant()
    expected = 4
    assert actual == expected, f"IntegerLattice.discriminant mismatch: actual={actual}, expected={expected}"


def test_integerlattice_lll_returns_matrix_and_sets_reduced_basis():
    """
    method: LLL

    LLL() returns a reduced basis matrix and updates self.reduced_basis.
    Assertion: Return value is a matrix and reduced_basis is populated with matching rank.
    """
    L = IntegerLattice([[4, 1], [1, 3]])
    R = L.LLL()
    actual_rows = R.nrows()
    expected_rows = 2
    assert actual_rows == expected_rows, (
        f"IntegerLattice.LLL return row count mismatch: actual={actual_rows}, expected={expected_rows}"
    )
    actual_reduced_rows = L.reduced_basis.nrows()
    expected_reduced_rows = 2
    assert actual_reduced_rows == expected_reduced_rows, (
        "IntegerLattice.reduced_basis row count mismatch: "
        f"actual={actual_reduced_rows}, expected={expected_reduced_rows}"
    )


def test_integerlattice_bkz_preserves_lattice_rank():
    """
    method: BKZ

    BKZ() applies block reduction to the basis matrix in Euclidean embedding space.
    Assertion: BKZ reduction preserves rank (row count).
    """
    L = IntegerLattice([[1, 1, 0], [0, 2, 1], [1, 0, 2]])
    R = L.BKZ(block_size=2)
    actual = R.nrows()
    expected = L.rank()
    assert actual == expected, f"IntegerLattice.BKZ rank mismatch: actual={actual}, expected={expected}"


def test_integerlattice_shortest_vector_has_expected_norm_rank_one():
    """
    method: shortest_vector

    shortest_vector() solves exact SVP for the IntegerLattice object.
    Assertion: In rank one it returns the generator up to sign.
    """
    L = IntegerLattice([[3]])
    v = L.shortest_vector()
    actual = abs(v[0])
    expected = 3
    assert actual == expected, f"IntegerLattice.shortest_vector mismatch: actual={actual}, expected={expected}"


def test_integerlattice_closest_vector_exact_rank_one():
    """
    method: closest_vector

    closest_vector(t) solves exact CVP to target t in the Euclidean model.
    Assertion: In rank one it returns the nearest basis multiple.
    """
    L = IntegerLattice([[4]])
    c = L.closest_vector((7,))
    actual = c[0]
    expected = 8
    assert actual == expected, f"IntegerLattice.closest_vector mismatch: actual={actual}, expected={expected}"


def test_integerlattice_hkz_preserves_rank():
    """
    method: HKZ

    HKZ() computes full-block BKZ reduction.
    Assertion: Output basis row count equals lattice rank.
    """
    L = IntegerLattice([[1, 1, 0], [0, 2, 1], [1, 0, 2]])
    R = L.HKZ()
    actual = R.nrows()
    expected = L.rank()
    assert actual == expected, f"IntegerLattice.HKZ rank mismatch: actual={actual}, expected={expected}"


def test_integerlattice_volume_square_matches_discriminant():
    """
    method: volume

    volume() is covolume of the lattice in Euclidean space.
    Assertion: volume^2 equals discriminant.
    """
    L = IntegerLattice([[1, 0], [0, 2]])
    actual = L.volume() ** 2
    expected = L.discriminant()
    assert actual == expected, f"IntegerLattice.volume mismatch: actual={actual}, expected={expected}"


def test_integerlattice_is_unimodular_false_for_scaled_basis():
    """
    method: is_unimodular

    is_unimodular() checks determinant ±1 of the Gram matrix.
    Assertion: Basis [[1,0],[0,2]] is not unimodular.
    """
    L = IntegerLattice([[1, 0], [0, 2]])
    actual = L.is_unimodular()
    expected = False
    assert actual == expected, f"IntegerLattice.is_unimodular mismatch: actual={actual}, expected={expected}"


def test_integerlattice_approximate_closest_vector_returns_lattice_vector():
    """
    method: approximate_closest_vector

    approximate_closest_vector(t, ...) returns a lattice vector approximation for CVP.
    Assertion: In rank one the output lies in 4Z for basis [[4]].
    """
    L = IntegerLattice([[4]])
    v = L.approximate_closest_vector((7,))
    actual = (v[0] % 4 == 0)
    expected = True
    assert actual == expected, (
        f"IntegerLattice.approximate_closest_vector lattice-membership mismatch: actual={actual}, expected={expected}, v={v}"
    )


def test_integerlattice_update_reduced_basis_sets_attribute():
    """
    method: update_reduced_basis

    update_reduced_basis() refreshes internal reduced basis state.
    Assertion: Updated reduced basis has full lattice rank.
    """
    L = IntegerLattice([[2, 1], [1, 2]])
    L.update_reduced_basis(L.basis_matrix())
    actual = L.reduced_basis.rank()
    expected = L.rank()
    assert actual == expected, (
        f"IntegerLattice.update_reduced_basis mismatch: actual={actual}, expected={expected}"
    )


def test_integerlattice_reduced_basis_preserves_discriminant_after_lll():
    """
    method: reduced_basis

    reduced_basis stores the current reduced basis matrix after reduction.
    Assertion: Gram determinant of reduced_basis equals the lattice discriminant.
    """
    L = IntegerLattice([[4, 1], [1, 3]])
    L.LLL()
    R = L.reduced_basis
    actual = (R * R.transpose()).det()
    expected = L.discriminant()
    assert actual == expected, (
        f"IntegerLattice.reduced_basis discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_integerlattice_babai_returns_lattice_vector_rank_one():
    """
    method: babai

    babai(t) returns a nearest-plane approximation to CVP target t.
    Assertion: For basis [[4]], output coordinate is divisible by 4.
    """
    L = IntegerLattice([[4]])
    v = L.babai((7,))
    actual = (v[0] % 4 == 0)
    expected = True
    assert actual == expected, f"IntegerLattice.babai mismatch: actual={actual}, expected={expected}, v={v}"


def test_integerlattice_voronoi_cell_has_vertices():
    """
    method: voronoi_cell

    voronoi_cell() returns the Voronoi polytope for a positive definite lattice.
    Assertion: Standard Z^2 Voronoi cell has four vertices.
    """
    L = IntegerLattice([[1, 0], [0, 1]])
    P = L.voronoi_cell()
    actual = len(P.vertices())
    expected = 4
    assert actual == expected, f"IntegerLattice.voronoi_cell mismatch: actual={actual}, expected={expected}"


def test_integerlattice_voronoi_relevant_vectors_nonempty():
    """
    method: voronoi_relevant_vectors

    voronoi_relevant_vectors() returns facet-defining vectors of Voronoi cell.
    Assertion: Standard Z^2 has four Voronoi-relevant vectors.
    """
    L = IntegerLattice([[1, 0], [0, 1]])
    V = L.voronoi_relevant_vectors()
    actual = len(V)
    expected = 4
    assert actual == expected, (
        f"IntegerLattice.voronoi_relevant_vectors mismatch: actual={actual}, expected={expected}"
    )


def test_integerlattice_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant IntegerLattice runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = IntegerLattice([[1, 1], [0, 2]])
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.modules.free_module_integer",),
    )
