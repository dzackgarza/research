r"""Exact arithmetic helpers for the synthetic lattice spike."""

from __future__ import annotations

from sage.combinat.root_system.cartan_matrix import CartanMatrix
from sage.matrix.constructor import matrix
from sage.rings.rational_field import QQ


def named_gram(name):
    if name == "U" or name == "H":
        return matrix(QQ, 2, 2, [0, 1, 1, 0])
    if isinstance(name, str) and len(name) >= 2 and name[0].isalpha() and name[1:].isdigit():
        return matrix(QQ, CartanMatrix([name[0], int(name[1:])]))
    if isinstance(name, (list, tuple)) and len(name) == 2:
        return matrix(QQ, CartanMatrix(list(name)))
    raise ValueError(f"unknown named synthetic lattice: {name!r}")


def as_square_qq_matrix(matrix_data):
    gram = named_gram(matrix_data) if _is_named_gram_data(matrix_data) else matrix(QQ, matrix_data)
    assert gram.is_square(), (
        "lattice Gram matrix must be square; "
        f"found dimensions={gram.nrows()}x{gram.ncols()}"
    )
    assert gram == gram.transpose(), f"lattice Gram matrix must be symmetric; found={gram}"
    gram.set_immutable()
    return gram


def _is_named_gram_data(matrix_data):
    return isinstance(matrix_data, str) or (
        isinstance(matrix_data, (list, tuple))
        and len(matrix_data) == 2
        and isinstance(matrix_data[0], str)
    )


def signature_pair(gram_matrix):
    diagonal_entries = _symmetric_diagonal_entries(matrix(QQ, gram_matrix))
    positives = sum(1 for entry in diagonal_entries if entry > 0)
    negatives = sum(1 for entry in diagonal_entries if entry < 0)
    return positives, negatives


def rational_mod(value, modulus):
    value = QQ(value)
    modulus = QQ(modulus)
    return value - modulus * (value / modulus).floor()


def block_diagonal_matrix(left, right):
    left = matrix(QQ, left)
    right = matrix(QQ, right)
    result = matrix(QQ, left.nrows() + right.nrows(), left.ncols() + right.ncols())
    for i in range(left.nrows()):
        for j in range(left.ncols()):
            result[i, j] = left[i, j]
    for i in range(right.nrows()):
        for j in range(right.ncols()):
            result[left.nrows() + i, left.ncols() + j] = right[i, j]
    result.set_immutable()
    return result


def _symmetric_diagonal_entries(gram):
    assert gram.is_square(), (
        "signature requires a square Gram matrix; "
        f"found dimensions={gram.nrows()}x{gram.ncols()}"
    )
    assert gram == gram.transpose(), f"signature requires a symmetric Gram matrix; found={gram}"
    if gram.nrows() == 0:
        return ()

    pivot_vector = _nonisotropic_vector(gram)
    if pivot_vector is None:
        return (QQ.zero(),) * gram.nrows()

    transform = _basis_with_first_vector(pivot_vector)
    diagonalized = transform * gram * transform.transpose()
    pivot = diagonalized[0, 0]
    assert pivot != 0, (
        "signature pivot vector must have nonzero square; "
        f"vector={pivot_vector}, gram={gram}"
    )
    if gram.nrows() == 1:
        return (pivot,)

    rank = gram.nrows()
    row = matrix(QQ, 1, rank - 1, [diagonalized[0, j] for j in range(1, rank)])
    column = matrix(QQ, rank - 1, 1, [diagonalized[i, 0] for i in range(1, rank)])
    rest = matrix(QQ, rank - 1, rank - 1, [diagonalized[i, j] for i in range(1, rank) for j in range(1, rank)])
    complement = rest - column * row / pivot
    return (pivot,) + _symmetric_diagonal_entries(complement)


def _nonisotropic_vector(gram):
    rank = gram.nrows()
    for i in range(rank):
        if gram[i, i] != 0:
            return [QQ.one() if j == i else QQ.zero() for j in range(rank)]
    for i in range(rank):
        for j in range(i + 1, rank):
            if gram[i, j] != 0:
                return [QQ.one() if k in (i, j) else QQ.zero() for k in range(rank)]
    return None


def _basis_with_first_vector(first_row):
    rank = len(first_row)
    pivot_column = next(i for i, entry in enumerate(first_row) if entry != 0)
    rows = [first_row]
    for i in range(rank):
        if i != pivot_column:
            rows.append([QQ.one() if j == i else QQ.zero() for j in range(rank)])
    return matrix(QQ, rows)
