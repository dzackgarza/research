from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import QQ, ZZ, matrix, vector
from .conftest import assert_runtime_methods_covered


def test_matrix_lll_preserves_row_span_rank():
    """
    method: LLL

    Matrix.LLL() returns an LLL-reduced basis matrix of the row lattice.
    Assertion: Row-rank is preserved by reduction.
    """
    M = matrix(ZZ, [[4, 1], [1, 3]])
    R = M.LLL()
    actual = R.rank()
    expected = M.rank()
    assert actual == expected, f"Matrix.LLL rank mismatch: actual={actual}, expected={expected}"


def test_matrix_lll_gram_returns_unimodular_transform():
    """
    method: LLL_gram

    Matrix.LLL_gram() returns unimodular U with U^T G U reduced for Gram matrix G.
    Assertion: Returned transform has determinant ±1.
    """
    G = matrix(ZZ, [[4, 1], [1, 3]])
    U = G.LLL_gram()
    actual = abs(U.det())
    expected = 1
    assert actual == expected, f"Matrix.LLL_gram unimodularity mismatch: actual={actual}, expected={expected}"


def test_matrix_smith_form_diagonal_divisibility():
    """
    method: smith_form

    smith_form() returns diagonal invariant factors of an integer matrix.
    Assertion: Nonzero invariant factors satisfy divisibility d1 | d2.
    """
    M = matrix(ZZ, [[2, 4], [6, 8]])
    D, _, _ = M.smith_form()
    d1, d2 = D[0, 0], D[1, 1]
    actual_nonzero = d1 != 0
    expected_nonzero = True
    assert actual_nonzero == expected_nonzero, (
        f"Matrix.smith_form first invariant nonzero mismatch: actual={actual_nonzero}, expected={expected_nonzero}; d1={d1}"
    )
    actual_divides = (d2 % d1 == 0)
    expected_divides = True
    assert actual_divides == expected_divides, (
        f"Matrix.smith_form divisibility mismatch: actual={actual_divides}, expected={expected_divides}; d1={d1}, d2={d2}"
    )


def test_matrix_base_ring_is_zz():
    """
    method: base_ring

    base_ring() returns coefficient ring of matrix entries.
    Assertion: Base ring is ZZ.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.base_ring()
    expected = ZZ
    assert actual == expected, f"Matrix.base_ring mismatch: actual={actual}, expected={expected}"


def test_matrix_change_ring_to_qq_preserves_shape():
    """
    method: change_ring

    change_ring(R) coerces entries into ring R.
    Assertion: Shape is preserved after change_ring(QQ).
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    N = M.change_ring(ZZ.fraction_field())
    actual = (N.nrows(), N.ncols())
    expected = (M.nrows(), M.ncols())
    assert actual == expected, f"Matrix.change_ring shape mismatch: actual={actual}, expected={expected}"


def test_matrix_det_alias_matches_determinant():
    """
    method: det

    det() aliases determinant().
    Assertion: det equals determinant.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.det()
    expected = M.determinant()
    assert actual == expected, f"Matrix.det alias mismatch: actual={actual}, expected={expected}"


def test_matrix_determinant_known_value():
    """
    method: determinant

    determinant() computes matrix determinant.
    Assertion: det([[2,1],[1,2]]) = 3.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.determinant()
    expected = 3
    assert actual == expected, f"Matrix.determinant mismatch: actual={actual}, expected={expected}"


def test_matrix_gcd_divides_all_entries():
    """
    method: gcd

    gcd() is gcd of all entries for integer matrix.
    Assertion: gcd divides each entry.
    """
    M = matrix(ZZ, [[4, 6], [10, 14]])
    g = M.gcd()
    actual = all(M[i, j] % g == 0 for i in range(M.nrows()) for j in range(M.ncols()))
    expected = True
    assert actual == expected, f"Matrix.gcd mismatch: actual={actual}, expected={expected}, gcd={g}"


def test_matrix_positive_definite_detected():
    """
    method: is_positive_definite

    is_positive_definite() checks positive definiteness.
    Assertion: [[2,1],[1,2]] is positive definite.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_positive_definite()
    expected = True
    assert actual == expected, (
        f"Matrix.is_positive_definite mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_is_primitive_true_when_entry_gcd_one():
    """
    method: is_primitive

    is_primitive() checks whether entry gcd is 1.
    Assertion: Matrix with entries gcd 1 is primitive.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_primitive()
    expected = True
    assert actual == expected, f"Matrix.is_primitive mismatch: actual={actual}, expected={expected}"


def test_matrix_is_singular_false_for_nonzero_det():
    """
    method: is_singular

    is_singular() checks determinant zero.
    Assertion: [[2,1],[1,2]] is nonsingular.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_singular()
    expected = False
    assert actual == expected, f"Matrix.is_singular mismatch: actual={actual}, expected={expected}"


def test_matrix_ncols_returns_column_count():
    """
    method: ncols

    ncols() returns number of columns.
    Assertion: 2x2 example has 2 columns.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.ncols()
    expected = 2
    assert actual == expected, f"Matrix.ncols mismatch: actual={actual}, expected={expected}"


def test_matrix_norm_nonnegative():
    """
    method: norm

    norm() returns a nonnegative matrix norm.
    Assertion: Norm is positive for nonzero matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    v = M.norm()
    actual = v > 0
    expected = True
    assert actual == expected, f"Matrix.norm mismatch: actual={v}, expected=>0"


def test_matrix_nrows_returns_row_count():
    """
    method: nrows

    nrows() returns number of rows.
    Assertion: 2x2 example has 2 rows.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.nrows()
    expected = 2
    assert actual == expected, f"Matrix.nrows mismatch: actual={actual}, expected={expected}"


def test_matrix_rank_full_for_positive_definite_example():
    """
    method: rank

    rank() returns linear rank over base field.
    Assertion: Positive-definite 2x2 matrix has rank 2.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.rank()
    expected = 2
    assert actual == expected, f"Matrix.rank mismatch: actual={actual}, expected={expected}"


def test_matrix_trace_equals_sum_of_diagonal():
    """
    method: trace

    trace() is sum of diagonal entries.
    Assertion: trace equals 2+2 on sample matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.trace()
    expected = 4
    assert actual == expected, f"Matrix.trace mismatch: actual={actual}, expected={expected}"


def test_matrix_transpose_swaps_off_diagonal_entries():
    """
    method: transpose

    transpose() swaps row/column positions.
    Assertion: Symmetric sample equals its transpose.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.transpose()
    expected = M
    assert actual == expected, f"Matrix.transpose mismatch: actual={actual}, expected={expected}"


def test_matrix_charpoly_matches_characteristic_polynomial():
    """
    method: charpoly

    charpoly() aliases characteristic_polynomial().
    Assertion: Two APIs return equal polynomial.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.charpoly()
    expected = M.characteristic_polynomial()
    assert actual == expected, f"Matrix.charpoly mismatch: actual={actual}, expected={expected}"


def test_matrix_characteristic_polynomial_has_expected_roots():
    """
    method: characteristic_polynomial

    characteristic_polynomial() encodes eigenvalues.
    Assertion: Sample polynomial factors as (x-3)(x-1).
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    x = M.base_ring()["x"].gen()
    actual = M.characteristic_polynomial()
    expected = x**2 - 4 * x + 3
    assert actual == expected, (
        f"Matrix.characteristic_polynomial mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_kernel_rank_zero_for_invertible_over_Q():
    """
    method: kernel

    kernel() returns nullspace over base ring/field context.
    Assertion: Kernel rank is 0 for nonzero determinant sample.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.kernel().rank()
    expected = 0
    assert actual == expected, f"Matrix.kernel mismatch: actual={actual}, expected={expected}"


def test_matrix_left_kernel_rank_zero():
    """
    method: left_kernel

    left_kernel() returns left nullspace.
    Assertion: Rank is 0 on full-rank sample.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.left_kernel().rank()
    expected = 0
    assert actual == expected, f"Matrix.left_kernel mismatch: actual={actual}, expected={expected}"


def test_matrix_right_kernel_rank_zero():
    """
    method: right_kernel

    right_kernel() returns right nullspace.
    Assertion: Rank is 0 on full-rank sample.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.right_kernel().rank()
    expected = 0
    assert actual == expected, f"Matrix.right_kernel mismatch: actual={actual}, expected={expected}"


def test_matrix_echelon_form_preserves_rank():
    """
    method: echelon_form

    echelon_form() row-reduces matrix over base ring.
    Assertion: Rank is preserved.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    E = M.echelon_form()
    actual = E.rank()
    expected = M.rank()
    assert actual == expected, f"Matrix.echelon_form mismatch: actual={actual}, expected={expected}"


def test_matrix_inverse_is_rational_inverse():
    """
    method: inverse

    inverse() computes matrix inverse over fraction field.
    Assertion: M * M^{-1} equals identity over QQ.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    Minv = M.inverse()
    I = M.change_ring(Minv.base_ring()) * Minv
    actual = I
    expected = I.parent().identity_matrix()
    assert actual == expected, f"Matrix.inverse mismatch: actual={actual}, expected={expected}"


def test_matrix_is_invertible_matches_unit_condition_over_ZZ():
    """
    method: is_invertible

    is_invertible() over ZZ means determinant is a unit.
    Assertion: det=3 matrix is not invertible over ZZ.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_invertible()
    expected = False
    assert actual == expected, f"Matrix.is_invertible mismatch: actual={actual}, expected={expected}"


def test_matrix_is_symmetric_true_for_symmetric_input():
    """
    method: is_symmetric

    is_symmetric() checks M == M^T.
    Assertion: Sample matrix is symmetric.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_symmetric()
    expected = True
    assert actual == expected, f"Matrix.is_symmetric mismatch: actual={actual}, expected={expected}"


def test_matrix_is_diagonal_false_for_off_diagonal_nonzero():
    """
    method: is_diagonal

    is_diagonal() checks off-diagonal zeros.
    Assertion: Sample matrix with ones off-diagonal is not diagonal.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_diagonal()
    expected = False
    assert actual == expected, f"Matrix.is_diagonal mismatch: actual={actual}, expected={expected}"


def test_matrix_eigenvalues_sum_equals_trace():
    """
    method: eigenvalues

    eigenvalues() returns algebraic eigenvalue multiset.
    Assertion: Sum equals matrix trace.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    vals = M.eigenvalues()
    actual = sum(vals)
    expected = M.trace()
    assert actual == expected, f"Matrix.eigenvalues mismatch: actual={actual}, expected={expected}"


def test_matrix_rows_length_matches_nrows():
    """
    method: rows

    rows() returns list of row vectors.
    Assertion: Length equals nrows().
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = len(M.rows())
    expected = M.nrows()
    assert actual == expected, f"Matrix.rows mismatch: actual={actual}, expected={expected}"


def test_matrix_columns_length_matches_ncols():
    """
    method: columns

    columns() returns list of column vectors.
    Assertion: Length equals ncols().
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = len(M.columns())
    expected = M.ncols()
    assert actual == expected, f"Matrix.columns mismatch: actual={actual}, expected={expected}"


def test_matrix_row_accessor_matches_rows_list_entry():
    """
    method: row

    row(i) returns i-th row vector.
    Assertion: row(0) equals rows()[0].
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.row(0)
    expected = M.rows()[0]
    assert actual == expected, f"Matrix.row mismatch: actual={actual}, expected={expected}"


def test_matrix_column_accessor_matches_columns_list_entry():
    """
    method: column

    column(j) returns j-th column vector.
    Assertion: column(0) equals columns()[0].
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.column(0)
    expected = M.columns()[0]
    assert actual == expected, f"Matrix.column mismatch: actual={actual}, expected={expected}"


def test_matrix_diagonal_entries_match_constructor():
    """
    method: diagonal

    diagonal() returns diagonal entries.
    Assertion: Diagonal is [2,2] on sample matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.diagonal()
    expected = [2, 2]
    assert actual == expected, f"Matrix.diagonal mismatch: actual={actual}, expected={expected}"


def test_matrix_is_square_true_for_two_by_two():
    """
    method: is_square

    is_square() checks nrows == ncols.
    Assertion: Sample is square.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_square()
    expected = True
    assert actual == expected, f"Matrix.is_square mismatch: actual={actual}, expected={expected}"


def test_matrix_rref_is_identity_for_invertible_over_Q():
    """
    method: rref

    rref() computes reduced row echelon form over fraction field.
    Assertion: Invertible sample has identity rref.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.rref()
    expected = actual.parent().identity_matrix()
    assert actual == expected, f"Matrix.rref mismatch: actual={actual}, expected={expected}"


def test_matrix_echelonize_mutates_to_echelon_form():
    """
    method: echelonize

    echelonize() performs in-place row-echelon reduction.
    Assertion: In-place result equals echelon_form() of original matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    expected = M.echelon_form()
    M.echelonize()
    actual = M
    assert actual == expected, f"Matrix.echelonize mismatch: actual={actual}, expected={expected}"


def test_matrix_left_nullity_matches_left_kernel_rank():
    """
    method: left_nullity

    left_nullity() equals left kernel rank.
    Assertion: Equality holds on full-rank sample.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.left_nullity()
    expected = M.left_kernel().rank()
    assert actual == expected, f"Matrix.left_nullity mismatch: actual={actual}, expected={expected}"


def test_matrix_right_nullity_matches_right_kernel_rank():
    """
    method: right_nullity

    right_nullity() equals right kernel rank.
    Assertion: Equality holds on full-rank sample.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.right_nullity()
    expected = M.right_kernel().rank()
    assert actual == expected, f"Matrix.right_nullity mismatch: actual={actual}, expected={expected}"


def test_matrix_list_length_equals_entry_count():
    """
    method: list

    list() returns flattened entries.
    Assertion: Length equals nrows*ncols.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = len(M.list())
    expected = M.nrows() * M.ncols()
    assert actual == expected, f"Matrix.list mismatch: actual={actual}, expected={expected}"


def test_matrix_items_count_equals_nonzero_positions():
    """
    method: items

    items() returns dictionary-style iterator over nonzero entries.
    Assertion: Count equals number of nonzero positions.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = len(list(M.items()))
    expected = len(M.nonzero_positions())
    assert actual == expected, f"Matrix.items mismatch: actual={actual}, expected={expected}"


def test_matrix_dense_matrix_preserves_entries():
    """
    method: dense_matrix

    dense_matrix() returns dense representation with same entries.
    Assertion: Dense form equals original matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.dense_matrix()
    expected = M
    assert actual == expected, f"Matrix.dense_matrix mismatch: actual={actual}, expected={expected}"


def test_matrix_sparse_matrix_preserves_entries():
    """
    method: sparse_matrix

    sparse_matrix() returns sparse representation with same entries.
    Assertion: Sparse form equals original matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.sparse_matrix()
    expected = M
    assert actual == expected, f"Matrix.sparse_matrix mismatch: actual={actual}, expected={expected}"


def test_matrix_augment_increases_column_count_by_other_columns():
    """
    method: augment

    augment(N) concatenates matrices by columns.
    Assertion: ncols increases by N.ncols.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    N = matrix(ZZ, [[1], [0]])
    A = M.augment(N)
    actual = A.ncols()
    expected = M.ncols() + N.ncols()
    assert actual == expected, f"Matrix.augment mismatch: actual={actual}, expected={expected}"


def test_matrix_stack_increases_row_count_by_other_rows():
    """
    method: stack

    stack(N) concatenates matrices by rows.
    Assertion: nrows increases by N.nrows.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    N = matrix(ZZ, [[0, 1]])
    S = M.stack(N)
    actual = S.nrows()
    expected = M.nrows() + N.nrows()
    assert actual == expected, f"Matrix.stack mismatch: actual={actual}, expected={expected}"


def test_matrix_matrix_from_rows_selects_requested_rows():
    """
    method: matrix_from_rows

    matrix_from_rows(idx) extracts rows by index.
    Assertion: Selecting first row yields 1x2 matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    R = M.matrix_from_rows([0])
    actual = (R.nrows(), R.ncols())
    expected = (1, 2)
    assert actual == expected, (
        f"Matrix.matrix_from_rows mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_matrix_from_columns_selects_requested_columns():
    """
    method: matrix_from_columns

    matrix_from_columns(idx) extracts columns by index.
    Assertion: Selecting first column yields 2x1 matrix.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    C = M.matrix_from_columns([0])
    actual = (C.nrows(), C.ncols())
    expected = (2, 1)
    assert actual == expected, (
        f"Matrix.matrix_from_columns mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_submatrix_extracts_requested_block_shape():
    """
    method: submatrix

    submatrix(r,c,nr,nc) extracts a rectangular block.
    Assertion: 1x1 block extraction has shape (1,1).
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    B = M.submatrix(0, 0, 1, 1)
    actual = (B.nrows(), B.ncols())
    expected = (1, 1)
    assert actual == expected, f"Matrix.submatrix mismatch: actual={actual}, expected={expected}"


def test_matrix_swap_rows_changes_row_order_in_place():
    """
    method: swap_rows

    swap_rows(i,j) swaps rows in place.
    Assertion: Row 0 becomes previous row 1 after swap.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    old = M.row(1)
    M.swap_rows(0, 1)
    actual = M.row(0)
    expected = old
    assert actual == expected, f"Matrix.swap_rows mismatch: actual={actual}, expected={expected}"


def test_matrix_swap_columns_changes_column_order_in_place():
    """
    method: swap_columns

    swap_columns(i,j) swaps columns in place.
    Assertion: Column 0 becomes previous column 1 after swap.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    old = M.column(1)
    M.swap_columns(0, 1)
    actual = M.column(0)
    expected = old
    assert actual == expected, f"Matrix.swap_columns mismatch: actual={actual}, expected={expected}"


def test_matrix_with_swapped_rows_returns_new_matrix_with_swapped_order():
    """
    method: with_swapped_rows

    with_swapped_rows(i,j) returns swapped-row copy.
    Assertion: Returned matrix has row 0 equal original row 1.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    W = M.with_swapped_rows(0, 1)
    actual = W.row(0)
    expected = M.row(1)
    assert actual == expected, (
        f"Matrix.with_swapped_rows mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_with_swapped_columns_returns_new_matrix_with_swapped_order():
    """
    method: with_swapped_columns

    with_swapped_columns(i,j) returns swapped-column copy.
    Assertion: Returned matrix has column 0 equal original column 1.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    W = M.with_swapped_columns(0, 1)
    actual = W.column(0)
    expected = M.column(1)
    assert actual == expected, (
        f"Matrix.with_swapped_columns mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_inverse_of_unit_identity_fixed():
    """
    method: inverse_of_unit

    inverse_of_unit() inverts matrix units over base ring.
    Assertion: Identity inverse_of_unit is identity.
    """
    I = matrix(ZZ, [[1, 0], [0, 1]])
    actual = I.inverse_of_unit()
    expected = I
    assert actual == expected, f"Matrix.inverse_of_unit mismatch: actual={actual}, expected={expected}"


def test_matrix_is_unit_true_exactly_for_identity_over_ZZ():
    """
    method: is_unit

    is_unit() checks invertibility in matrix ring over base ring.
    Assertion: Identity is a unit.
    """
    I = matrix(ZZ, [[1, 0], [0, 1]])
    actual = I.is_unit()
    expected = True
    assert actual == expected, f"Matrix.is_unit mismatch: actual={actual}, expected={expected}"


def test_matrix_left_kernel_matrix_row_count_equals_left_nullity():
    """
    method: left_kernel_matrix

    left_kernel_matrix() basis matrix rows equal left nullity.
    Assertion: Row count equals left_nullity.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    K = M.left_kernel_matrix()
    actual = K.nrows()
    expected = M.left_nullity()
    assert actual == expected, (
        f"Matrix.left_kernel_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_right_kernel_matrix_row_count_equals_right_nullity():
    """
    method: right_kernel_matrix

    right_kernel_matrix() basis matrix rows equal right nullity.
    Assertion: Row count equals right_nullity.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    K = M.right_kernel_matrix()
    actual = K.nrows()
    expected = M.right_nullity()
    assert actual == expected, (
        f"Matrix.right_kernel_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_eigenvectors_right_contains_eigenvalue_three():
    """
    method: eigenvectors_right

    eigenvectors_right() returns right eigenspaces data.
    Assertion: Eigenvalue 3 is present.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    vals = [ev for ev, _, _ in M.eigenvectors_right()]
    actual = 3 in vals
    expected = True
    assert actual == expected, (
        f"Matrix.eigenvectors_right mismatch: actual={actual}, expected={expected}, vals={vals}"
    )


def test_matrix_eigenvectors_left_contains_eigenvalue_one():
    """
    method: eigenvectors_left

    eigenvectors_left() returns left eigenspaces data.
    Assertion: Eigenvalue 1 is present.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    vals = [ev for ev, _, _ in M.eigenvectors_left()]
    actual = 1 in vals
    expected = True
    assert actual == expected, (
        f"Matrix.eigenvectors_left mismatch: actual={actual}, expected={expected}, vals={vals}"
    )


def test_matrix_lu_reconstructs_original_matrix():
    """
    method: LU

    LU() returns factors with permutation data reconstructing matrix.
    Assertion: Product L*U equals permuted original matrix for returned pivoting.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    P, L, U = M.LU()
    actual = P * M
    expected = L * U
    assert actual == expected, f"Matrix.LU mismatch: actual={actual}, expected={expected}"


def test_matrix_add_multiple_of_row_updates_target_row():
    """
    method: add_multiple_of_row

    add_multiple_of_row(i,j,c) performs row_i += c*row_j in place.
    Assertion: Updated row equals expected linear combination.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    before = M.row(0)
    M.add_multiple_of_row(0, 1, 2)
    actual = M.row(0)
    expected = before + 2 * matrix(ZZ, [[1, 2], [3, 4]]).row(1)
    assert actual == expected, (
        f"Matrix.add_multiple_of_row mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_add_multiple_of_column_updates_target_column():
    """
    method: add_multiple_of_column

    add_multiple_of_column(i,j,c) performs col_i += c*col_j in place.
    Assertion: Updated column equals expected linear combination.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    before = M.column(0)
    M.add_multiple_of_column(0, 1, 2)
    actual = M.column(0)
    expected = before + 2 * matrix(ZZ, [[1, 2], [3, 4]]).column(1)
    assert actual == expected, (
        f"Matrix.add_multiple_of_column mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_add_to_entry_changes_single_entry():
    """
    method: add_to_entry

    add_to_entry(i,j,c) increments one entry in place.
    Assertion: Only selected entry changes by c.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    M.add_to_entry(0, 0, 5)
    actual = M[0, 0]
    expected = 6
    assert actual == expected, f"Matrix.add_to_entry mismatch: actual={actual}, expected={expected}"


def test_matrix_adjoint_classical_times_matrix_equals_det_identity():
    """
    method: adjoint_classical

    adjoint_classical() returns classical adjoint matrix.
    Assertion: adj(A)*A = det(A) * I.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    Adj = M.adjoint_classical()
    actual = Adj * M
    expected = M.det() * matrix.identity(ZZ, 2)
    assert actual == expected, (
        f"Matrix.adjoint_classical mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_adjugate_equals_adjoint_classical():
    """
    method: adjugate

    adjugate() is the classical adjoint.
    Assertion: adjugate equals adjoint_classical.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.adjugate()
    expected = M.adjoint_classical()
    assert actual == expected, f"Matrix.adjugate mismatch: actual={actual}, expected={expected}"


def test_matrix_anticommutator_definition_matches_sum():
    """
    method: anticommutator

    anticommutator(B) equals AB + BA.
    Assertion: API result matches defining expression.
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[2, 0], [1, 1]])
    actual = A.anticommutator(B)
    expected = A * B + B * A
    assert actual == expected, (
        f"Matrix.anticommutator mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_antitranspose_involution():
    """
    method: antitranspose

    antitranspose() is an involution.
    Assertion: Applying antitranspose twice returns original matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.antitranspose().antitranspose()
    expected = M
    assert actual == expected, (
        f"Matrix.antitranspose mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_apply_map_adds_one_entrywise():
    """
    method: apply_map

    apply_map(f) applies map entrywise.
    Assertion: Sum of entries increases by matrix size for f(x)=x+1.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    N = M.apply_map(lambda x: x + 1)
    actual = sum(N.list())
    expected = sum(M.list()) + M.nrows() * M.ncols()
    assert actual == expected, f"Matrix.apply_map mismatch: actual={actual}, expected={expected}"


def test_matrix_block_sum_has_additive_dimensions():
    """
    method: block_sum

    block_sum(B) forms block-diagonal direct sum.
    Assertion: Dimensions add in both directions.
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[2, 1], [1, 2]])
    C = A.block_sum(B)
    actual = (C.nrows(), C.ncols())
    expected = (A.nrows() + B.nrows(), A.ncols() + B.ncols())
    assert actual == expected, f"Matrix.block_sum mismatch: actual={actual}, expected={expected}"


def test_matrix_cholesky_reconstructs_positive_definite_matrix():
    """
    method: cholesky

    cholesky() returns factor R with R^T R = A for positive-definite A.
    Assertion: Reconstruction equals original matrix.
    """
    A = matrix(QQ, [[2, 1], [1, 2]])
    R = A.cholesky()
    actual = R * R.transpose()
    expected = A
    assert actual == expected, f"Matrix.cholesky mismatch: actual={actual}, expected={expected}"


def test_matrix_column_space_dimension_equals_rank():
    """
    method: column_space

    column_space() returns span of columns.
    Assertion: Dimension equals matrix rank.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.column_space().dimension()
    expected = M.rank()
    assert actual == expected, (
        f"Matrix.column_space mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_commutator_definition_matches_difference():
    """
    method: commutator

    commutator(B) equals AB - BA.
    Assertion: API result matches defining expression.
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[2, 0], [1, 1]])
    actual = A.commutator(B)
    expected = A * B - B * A
    assert actual == expected, f"Matrix.commutator mismatch: actual={actual}, expected={expected}"


def test_matrix_conjugate_transpose_equals_transpose_over_integers():
    """
    method: conjugate_transpose

    conjugate_transpose() reduces to transpose over real/integer entries.
    Assertion: conjugate_transpose equals transpose.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.conjugate_transpose()
    expected = M.transpose()
    assert actual == expected, (
        f"Matrix.conjugate_transpose mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_delete_columns_reduces_column_count():
    """
    method: delete_columns

    delete_columns(indices) removes selected columns.
    Assertion: Column count drops by number of removed indices.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    N = M.delete_columns([1])
    actual = N.ncols()
    expected = M.ncols() - 1
    assert actual == expected, (
        f"Matrix.delete_columns mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_delete_rows_reduces_row_count():
    """
    method: delete_rows

    delete_rows(indices) removes selected rows.
    Assertion: Row count drops by number of removed indices.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    N = M.delete_rows([1])
    actual = N.nrows()
    expected = M.nrows() - 1
    assert actual == expected, f"Matrix.delete_rows mismatch: actual={actual}, expected={expected}"


def test_matrix_dense_rows_length_matches_nrows():
    """
    method: dense_rows

    dense_rows() returns explicit row list.
    Assertion: Number of returned rows equals nrows.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = len(M.dense_rows())
    expected = M.nrows()
    assert actual == expected, f"Matrix.dense_rows mismatch: actual={actual}, expected={expected}"


def test_matrix_dense_columns_length_matches_ncols():
    """
    method: dense_columns

    dense_columns() returns explicit column list.
    Assertion: Number of returned columns equals ncols.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = len(M.dense_columns())
    expected = M.ncols()
    assert actual == expected, (
        f"Matrix.dense_columns mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_dimensions_matches_nrows_ncols():
    """
    method: dimensions

    dimensions() returns (nrows, ncols).
    Assertion: Tuple matches nrows/ncols APIs.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.dimensions()
    expected = (M.nrows(), M.ncols())
    assert actual == expected, f"Matrix.dimensions mismatch: actual={actual}, expected={expected}"


def test_matrix_eigenmatrix_right_diagonalizes_symmetric_example():
    """
    method: eigenmatrix_right

    eigenmatrix_right() returns eigenvalue/eigenvector matrix data.
    Assertion: Returned matrix has full rank for matrix with distinct eigenvalues.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    _, P = M.eigenmatrix_right()
    actual = P.rank()
    expected = M.nrows()
    assert actual == expected, (
        f"Matrix.eigenmatrix_right mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_eigenspaces_right_dimensions_sum_to_size():
    """
    method: eigenspaces_right

    eigenspaces_right() returns eigenspace decomposition.
    Assertion: Sum of eigenspace dimensions equals matrix size for diagonalizable sample.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    spaces = M.eigenspaces_right()
    actual = sum(V.dimension() for _, V in spaces)
    expected = M.nrows()
    assert actual == expected, (
        f"Matrix.eigenspaces_right mismatch: actual={actual}, expected={expected}, spaces={spaces}"
    )


def test_matrix_eigenvalue_multiplicity_for_distinct_eigenvalue_is_one():
    """
    method: eigenvalue_multiplicity

    eigenvalue_multiplicity(lam) returns algebraic multiplicity.
    Assertion: Eigenvalue 3 has multiplicity 1 for [[2,1],[1,2]].
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.eigenvalue_multiplicity(3)
    expected = 1
    assert actual == expected, (
        f"Matrix.eigenvalue_multiplicity mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_elementary_divisors_multiply_to_determinant_absolute():
    """
    method: elementary_divisors

    elementary_divisors() are invariant factors over PID.
    Assertion: Product equals |determinant| for full-rank square matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    divisors = M.elementary_divisors()
    actual = ZZ.prod(divisors)
    expected = abs(M.det())
    assert actual == expected, (
        f"Matrix.elementary_divisors mismatch: actual={actual}, expected={expected}, divisors={divisors}"
    )


def test_matrix_extended_echelon_form_preserves_rank():
    """
    method: extended_echelon_form

    extended_echelon_form() computes echelon-like normal form.
    Assertion: Rank is preserved.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    E = M.extended_echelon_form()
    actual = E.rank()
    expected = M.rank()
    assert actual == expected, (
        f"Matrix.extended_echelon_form mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_fitting_ideal_zero_has_generator_determinant_for_full_rank():
    """
    method: fitting_ideal

    fitting_ideal(0) for square full-rank matrix is generated by determinant.
    Assertion: Determinant lies in the returned ideal.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    I = M.fitting_ideal(0)
    actual = M.det() in I
    expected = True
    assert actual == expected, (
        f"Matrix.fitting_ideal mismatch: actual={actual}, expected={expected}, ideal={I}, det={M.det()}"
    )


def test_matrix_gram_schmidt_returns_two_orthogonal_vectors():
    """
    method: gram_schmidt

    gram_schmidt() orthogonalizes row vectors.
    Assertion: Dot product of returned basis vectors is zero.
    """
    M = matrix(QQ, [[1, 0], [1, 1]])
    Qb, _ = M.gram_schmidt()
    actual = Qb[0].dot_product(Qb[1])
    expected = 0
    assert actual == expected, f"Matrix.gram_schmidt mismatch: actual={actual}, expected={expected}"


def test_matrix_hessenberg_form_preserves_characteristic_polynomial():
    """
    method: hessenberg_form

    hessenberg_form() is similar to original matrix.
    Assertion: Characteristic polynomial is preserved.
    """
    M = matrix(QQ, [[1, 2], [3, 4]])
    H = M.hessenberg_form()
    actual = H.charpoly()
    expected = M.charpoly()
    assert actual == expected, (
        f"Matrix.hessenberg_form mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_image_dimension_equals_rank():
    """
    method: image

    image() is column-space image of linear map.
    Assertion: Image dimension equals rank.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.image().dimension()
    expected = M.rank()
    assert actual == expected, f"Matrix.image mismatch: actual={actual}, expected={expected}"


def test_matrix_insert_row_increases_row_count_by_one():
    """
    method: insert_row

    insert_row(i,row) inserts a row at index i.
    Assertion: Row count increases by one.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    N = M.insert_row(1, [5, 6])
    actual = N.nrows()
    expected = M.nrows() + 1
    assert actual == expected, f"Matrix.insert_row mismatch: actual={actual}, expected={expected}"


def test_matrix_integer_kernel_dimension_matches_nullity():
    """
    method: integer_kernel

    integer_kernel() computes kernel over integers.
    Assertion: Kernel dimension equals right nullity for integer matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 6]])
    actual = M.integer_kernel().dimension()
    expected = M.right_nullity()
    assert actual == expected, (
        f"Matrix.integer_kernel mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_is_dense_true_for_dense_constructor():
    """
    method: is_dense

    is_dense() checks storage type.
    Assertion: Standard constructor yields dense matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.is_dense()
    expected = True
    assert actual == expected, f"Matrix.is_dense mismatch: actual={actual}, expected={expected}"


def test_matrix_is_sparse_false_for_dense_constructor():
    """
    method: is_sparse

    is_sparse() checks sparse storage representation.
    Assertion: Standard constructor matrix is not sparse.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.is_sparse()
    expected = False
    assert actual == expected, f"Matrix.is_sparse mismatch: actual={actual}, expected={expected}"


def test_matrix_is_hermitian_true_for_symmetric_integer_matrix():
    """
    method: is_hermitian

    is_hermitian() generalizes symmetry over involutive rings.
    Assertion: Real symmetric matrix is Hermitian.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.is_hermitian()
    expected = True
    assert actual == expected, f"Matrix.is_hermitian mismatch: actual={actual}, expected={expected}"


def test_matrix_is_one_true_for_identity():
    """
    method: is_one

    is_one() checks multiplicative identity matrix.
    Assertion: Identity matrix satisfies is_one.
    """
    I = matrix.identity(ZZ, 2)
    actual = I.is_one()
    expected = True
    assert actual == expected, f"Matrix.is_one mismatch: actual={actual}, expected={expected}"


def test_matrix_linear_combination_of_rows_matches_manual_combination():
    """
    method: linear_combination_of_rows

    linear_combination_of_rows(c) forms sum c_i * row_i.
    Assertion: Result matches manual linear combination.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    coeffs = [2, -1]
    actual = M.linear_combination_of_rows(coeffs)
    expected = 2 * M.row(0) - M.row(1)
    assert actual == expected, (
        f"Matrix.linear_combination_of_rows mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_linear_combination_of_columns_matches_manual_combination():
    """
    method: linear_combination_of_columns

    linear_combination_of_columns(c) forms sum c_j * col_j.
    Assertion: Result matches manual linear combination.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    coeffs = [2, -1]
    actual = M.linear_combination_of_columns(coeffs)
    expected = 2 * M.column(0) - M.column(1)
    assert actual == expected, (
        f"Matrix.linear_combination_of_columns mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_from_rows_and_columns_extracts_expected_entry():
    """
    method: matrix_from_rows_and_columns

    matrix_from_rows_and_columns(rows, cols) extracts a submatrix.
    Assertion: Extracted 1x1 block equals original selected entry.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    S = M.matrix_from_rows_and_columns([1], [0])
    actual = S[0, 0]
    expected = M[1, 0]
    assert actual == expected, (
        f"Matrix.matrix_from_rows_and_columns mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_over_field_changes_base_ring_to_fraction_field():
    """
    method: matrix_over_field

    matrix_over_field() coerces matrix to base field.
    Assertion: Base ring is QQ for integer matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.matrix_over_field().base_ring()
    expected = QQ
    assert actual == expected, (
        f"Matrix.matrix_over_field mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_space_dimensions_match_parent_shape():
    """
    method: matrix_space

    matrix_space() returns parent matrix space.
    Assertion: Parent dimensions equal matrix shape.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    S = M.matrix_space()
    actual = (S.nrows(), S.ncols())
    expected = (M.nrows(), M.ncols())
    assert actual == expected, f"Matrix.matrix_space mismatch: actual={actual}, expected={expected}"


def test_matrix_minimal_polynomial_divides_characteristic_polynomial():
    """
    method: minimal_polynomial

    minimal_polynomial() divides characteristic polynomial.
    Assertion: charpoly mod minpoly is zero.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    m = M.minimal_polynomial()
    c = M.charpoly()
    actual = c % m
    expected = 0
    assert actual == expected, (
        f"Matrix.minimal_polynomial mismatch: actual={actual}, expected={expected}, minpoly={m}, charpoly={c}"
    )


def test_matrix_minpoly_matches_minimal_polynomial():
    """
    method: minpoly

    minpoly() aliases minimal_polynomial().
    Assertion: Both APIs return identical polynomial.
    """
    M = matrix(ZZ, [[2, 1], [1, 2]])
    actual = M.minpoly()
    expected = M.minimal_polynomial()
    assert actual == expected, f"Matrix.minpoly mismatch: actual={actual}, expected={expected}"


def test_matrix_nonzero_positions_cardinality_equals_nonzero_entries_count():
    """
    method: nonzero_positions

    nonzero_positions() lists coordinates of nonzero entries.
    Assertion: Count equals number of nonzero entries by direct scan.
    """
    M = matrix(ZZ, [[1, 0], [0, 4]])
    actual = len(M.nonzero_positions())
    expected = sum(1 for a in M.list() if a != 0)
    assert actual == expected, (
        f"Matrix.nonzero_positions mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_nonzero_positions_in_row_matches_row_support():
    """
    method: nonzero_positions_in_row

    nonzero_positions_in_row(i) gives support of row i.
    Assertion: Returned indices match direct row scan.
    """
    M = matrix(ZZ, [[1, 0], [3, 4]])
    actual = M.nonzero_positions_in_row(1)
    expected = [j for j in range(M.ncols()) if M[1, j] != 0]
    assert actual == expected, (
        f"Matrix.nonzero_positions_in_row mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_nonzero_positions_in_column_matches_column_support():
    """
    method: nonzero_positions_in_column

    nonzero_positions_in_column(j) gives support of column j.
    Assertion: Returned indices match direct column scan.
    """
    M = matrix(ZZ, [[1, 0], [3, 4]])
    actual = M.nonzero_positions_in_column(0)
    expected = [i for i in range(M.nrows()) if M[i, 0] != 0]
    assert actual == expected, (
        f"Matrix.nonzero_positions_in_column mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_numpy_export_preserves_shape():
    """
    method: numpy

    numpy() exports to NumPy array.
    Assertion: Exported array shape matches matrix dimensions.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    A = M.numpy()
    actual = A.shape
    expected = (M.nrows(), M.ncols())
    assert actual == expected, f"Matrix.numpy mismatch: actual={actual}, expected={expected}"


def test_matrix_permanent_known_value_for_2x2():
    """
    method: permanent

    permanent() computes sum over permutation products without sign.
    Assertion: permanent([[1,2],[3,4]]) = 1*4 + 2*3 = 10.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.permanent()
    expected = 10
    assert actual == expected, f"Matrix.permanent mismatch: actual={actual}, expected={expected}"


def test_matrix_pivot_rows_length_equals_rank():
    """
    method: pivot_rows

    pivot_rows() returns pivot row indices.
    Assertion: Number of pivots equals rank.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = len(M.pivot_rows())
    expected = M.rank()
    assert actual == expected, f"Matrix.pivot_rows mismatch: actual={actual}, expected={expected}"


def test_matrix_pivots_length_equals_rank():
    """
    method: pivots

    pivots() returns pivot column indices.
    Assertion: Number of pivots equals rank.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = len(M.pivots())
    expected = M.rank()
    assert actual == expected, f"Matrix.pivots mismatch: actual={actual}, expected={expected}"


def test_matrix_qdet_specializes_to_determinant_for_commutative_ring():
    """
    method: qdet

    qdet() produces a quantum determinant polynomial.
    Assertion: Specializing at q=1 gives the usual determinant.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.qdet()(q=1)
    expected = M.det()
    assert actual == expected, f"Matrix.qdet mismatch: actual={actual}, expected={expected}"


def test_matrix_reverse_rows_and_columns_is_involution():
    """
    method: reverse_rows_and_columns

    reverse_rows_and_columns() reverses row and column order in place.
    Assertion: Applying twice returns original matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    M.reverse_rows_and_columns()
    M.reverse_rows_and_columns()
    actual = M
    expected = matrix(ZZ, [[1, 2], [3, 4]])
    assert actual == expected, (
        f"Matrix.reverse_rows_and_columns mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_rook_vector_length_matches_min_dimension_plus_one():
    """
    method: rook_vector

    rook_vector() returns rook polynomial coefficients.
    Assertion: Length is min(nrows,ncols)+1.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = len(M.rook_vector())
    expected = min(M.nrows(), M.ncols()) + 1
    assert actual == expected, f"Matrix.rook_vector mismatch: actual={actual}, expected={expected}"


def test_matrix_row_space_dimension_equals_rank():
    """
    method: row_space

    row_space() returns subspace spanned by rows.
    Assertion: Dimension equals rank.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.row_space().dimension()
    expected = M.rank()
    assert actual == expected, f"Matrix.row_space mismatch: actual={actual}, expected={expected}"


def test_matrix_singular_values_count_equals_min_dimension():
    """
    method: singular_values

    singular_values() returns singular-value list.
    Assertion: Count equals min(nrows, ncols).
    """
    M = matrix(QQ, [[1, 2], [3, 4]])
    actual = len(M.singular_values())
    expected = min(M.nrows(), M.ncols())
    assert actual == expected, (
        f"Matrix.singular_values mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_solve_right_solves_linear_system():
    """
    method: solve_right

    solve_right(b) solves A x = b.
    Assertion: Substituting solution reproduces right-hand side.
    """
    A = matrix(QQ, [[1, 2], [3, 4]])
    b = vector(QQ, [1, 0])
    x = A.solve_right(b)
    actual = A * x
    expected = b
    assert actual == expected, f"Matrix.solve_right mismatch: actual={actual}, expected={expected}"


def test_matrix_trace_of_product_matches_direct_trace():
    """
    method: trace_of_product

    trace_of_product(B) computes tr(A*B) efficiently.
    Assertion: Value equals trace(A*B).
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[2, 0], [1, 1]])
    actual = A.trace_of_product(B)
    expected = (A * B).trace()
    assert actual == expected, (
        f"Matrix.trace_of_product mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_with_added_multiple_of_row_matches_in_place_update():
    """
    method: with_added_multiple_of_row

    with_added_multiple_of_row(i,j,c) returns updated copy.
    Assertion: Result matches explicit in-place update on clone.
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[1, 2], [3, 4]])
    B.add_multiple_of_row(0, 1, 2)
    actual = A.with_added_multiple_of_row(0, 1, 2)
    expected = B
    assert actual == expected, (
        f"Matrix.with_added_multiple_of_row mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_with_added_multiple_of_column_matches_in_place_update():
    """
    method: with_added_multiple_of_column

    with_added_multiple_of_column(i,j,c) returns updated copy.
    Assertion: Result matches explicit in-place update on clone.
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[1, 2], [3, 4]])
    B.add_multiple_of_column(0, 1, 2)
    actual = A.with_added_multiple_of_column(0, 1, 2)
    expected = B
    assert actual == expected, (
        f"Matrix.with_added_multiple_of_column mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_with_rescaled_row_matches_in_place_update():
    """
    method: with_rescaled_row

    with_rescaled_row(i,c) returns copy with one row scaled.
    Assertion: Result matches in-place row scaling on clone.
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[1, 2], [3, 4]])
    B.rescale_row(0, 2)
    actual = A.with_rescaled_row(0, 2)
    expected = B
    assert actual == expected, (
        f"Matrix.with_rescaled_row mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_with_rescaled_col_matches_in_place_update():
    """
    method: with_rescaled_col

    with_rescaled_col(j,c) returns copy with one column scaled.
    Assertion: Result matches in-place column scaling on clone.
    """
    A = matrix(ZZ, [[1, 2], [3, 4]])
    B = matrix(ZZ, [[1, 2], [3, 4]])
    B.rescale_col(1, 2)
    actual = A.with_rescaled_col(1, 2)
    expected = B
    assert actual == expected, (
        f"Matrix.with_rescaled_col mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_zero_pattern_matrix_marks_nonzero_support():
    """
    method: zero_pattern_matrix

    zero_pattern_matrix() returns indicator matrix for zero entries.
    Assertion: Zero entries map to 1 and nonzero entries map to 0.
    """
    M = matrix(ZZ, [[1, 0], [0, 4]])
    Z = M.zero_pattern_matrix()
    actual = Z.list()
    expected = [0, 1, 1, 0]
    assert actual == expected, (
        f"Matrix.zero_pattern_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_bkz_preserves_lattice_rank():
    """
    method: BKZ

    BKZ() returns a block-reduced basis for the same row lattice.
    Assertion: Rank is preserved.
    """
    M = matrix(ZZ, [[4, 1], [1, 3]])
    B = M.BKZ()
    actual = B.rank()
    expected = M.rank()
    assert actual == expected, f"Matrix.BKZ mismatch: actual={actual}, expected={expected}"


def test_matrix_decomposition_direct_sum_dimensions_match():
    """
    method: decomposition

    decomposition() returns decomposition of the ambient module.
    Assertion: Sum of component dimensions equals ambient rank.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    dec = M.decomposition()
    actual = sum(U.rank() for (U, _) in dec)
    expected = M.ncols()
    assert actual == expected, (
        f"Matrix.decomposition mismatch: actual={actual}, expected={expected}, decomposition={dec}"
    )


def test_matrix_frobenius_form_preserves_characteristic_polynomial():
    """
    method: frobenius_form

    frobenius_form() is rational-canonical and similar to original.
    Assertion: Characteristic polynomial is preserved.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    F = M.frobenius_form()
    actual = F.charpoly()
    expected = M.charpoly()
    assert actual == expected, (
        f"Matrix.frobenius_form mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_height_equals_max_abs_entry():
    """
    method: height

    height() is maximum absolute value of entries for integer matrix.
    Assertion: height([[1,2],[3,4]]) equals 4.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.height()
    expected = 4
    assert actual == expected, f"Matrix.height mismatch: actual={actual}, expected={expected}"


def test_matrix_index_in_saturation_for_scaled_identity():
    """
    method: index_in_saturation

    index_in_saturation() measures finite index to saturation.
    Assertion: 2I_2 has saturation index 4.
    """
    M = matrix(ZZ, [[2, 0], [0, 2]])
    actual = M.index_in_saturation()
    expected = 4
    assert actual == expected, (
        f"Matrix.index_in_saturation mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_integer_valued_polynomials_generators_annihilate_mod_z():
    """
    method: integer_valued_polynomials_generators

    integer_valued_polynomials_generators() returns generators for null ideal over Z.
    Assertion: First generator matches generator of null_ideal().
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    g, _ = M.integer_valued_polynomials_generators()
    actual = g
    expected = M.null_ideal().gen()
    assert actual == expected, (
        f"Matrix.integer_valued_polynomials_generators mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_is_lll_reduced_true_after_lll():
    """
    method: is_LLL_reduced

    is_LLL_reduced() checks LLL reducedness.
    Assertion: Output of LLL() is LLL-reduced.
    """
    M = matrix(ZZ, [[4, 1], [1, 3]])
    actual = M.LLL().is_LLL_reduced()
    expected = True
    assert actual == expected, (
        f"Matrix.is_LLL_reduced mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_null_ideal_generator_annihilates_matrix():
    """
    method: null_ideal

    null_ideal() consists of integer polynomials annihilating the matrix.
    Assertion: Generator evaluated at matrix is zero matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    g = M.null_ideal().gen()
    actual = g(M)
    expected = matrix.zero(ZZ, M.nrows(), M.ncols())
    assert actual == expected, f"Matrix.null_ideal mismatch: actual={actual}, expected={expected}"


def test_matrix_p_minimal_polynomials_returns_dict():
    """
    method: p_minimal_polynomials

    p_minimal_polynomials(p) returns map s -> (p^s)-minimal polynomial data.
    Assertion: All returned exponents are positive integers.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    data = M.p_minimal_polynomials(ZZ(2))
    actual = all(k > 0 for k in data.keys())
    expected = True
    assert actual == expected, (
        f"Matrix.p_minimal_polynomials mismatch: actual={actual}, expected={expected}, data={data}"
    )


def test_matrix_prod_of_row_sums_matches_manual_product():
    """
    method: prod_of_row_sums

    prod_of_row_sums(cols) multiplies row sums restricted to selected columns.
    Assertion: Value matches manual computation on columns [0,1].
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.prod_of_row_sums([0, 1])
    expected = (1 + 2) * (3 + 4)
    assert actual == expected, (
        f"Matrix.prod_of_row_sums mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_randomize_density_zero_preserves_entries():
    """
    method: randomize

    randomize(density=0) performs no entry modifications.
    Assertion: Matrix remains unchanged.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    before = list(M.list())
    M.randomize(density=0)
    actual = list(M.list())
    expected = before
    assert actual == expected, f"Matrix.randomize mismatch: actual={actual}, expected={expected}"


def test_matrix_rational_reconstruction_recovers_integer_matrix_for_large_modulus():
    """
    method: rational_reconstruction

    rational_reconstruction(N) lifts entries from residue representatives modulo N.
    Assertion: For sufficiently large N, reconstruction returns original integer matrix.
    """
    M = matrix(ZZ, [[1, 2], [3, 4]])
    actual = M.rational_reconstruction(ZZ(101))
    expected = M.change_ring(QQ)
    assert actual == expected, (
        f"Matrix.rational_reconstruction mismatch: actual={actual}, expected={expected}"
    )


def test_matrix_saturation_of_scaled_identity_is_identity():
    """
    method: saturation

    saturation() computes saturated lattice generated by rows.
    Assertion: Saturation of rows of 2I_2 is I_2.
    """
    M = matrix(ZZ, [[2, 0], [0, 2]])
    actual = M.saturation()
    expected = matrix.identity(ZZ, 2)
    assert actual == expected, f"Matrix.saturation mismatch: actual={actual}, expected={expected}"


def test_matrix_symplectic_form_returns_standard_form_for_basis():
    """
    method: symplectic_form

    symplectic_form() returns alternating form and change-of-basis data.
    Assertion: Standard 2x2 symplectic matrix is returned for canonical example.
    """
    M = matrix(ZZ, [[0, 1], [-1, 0]])
    J, _ = M.symplectic_form()
    actual = J
    expected = matrix(ZZ, [[0, 1], [-1, 0]])
    assert actual == expected, f"Matrix.symplectic_form mismatch: actual={actual}, expected={expected}"


def test_matrix_methods_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant Matrix runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = matrix(ZZ, [[2, 1], [1, 2]])
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.matrix.matrix_integer_dense",),
    )
