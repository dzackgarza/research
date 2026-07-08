r"""Exact arithmetic helpers for the synthetic lattice spike."""

from __future__ import annotations

from typing import Any

from sage.combinat.root_system.cartan_matrix import CartanMatrix
from sage.matrix.constructor import matrix
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.rational_field import QQ

from ..lexicon.foundations import SignaturePair


def named_gram(name: object) -> Any:
    if name == "U" or name == "H":
        return matrix(QQ, 2, 2, [0, 1, 1, 0])
    if isinstance(name, str) and len(name) >= 2 and name[0].isalpha() and name[1:].isdigit():
        return matrix(QQ, CartanMatrix([name[0], int(name[1:])]))
    if isinstance(name, (list, tuple)) and len(name) == 2:
        return matrix(QQ, CartanMatrix(list(name)))
    assert False, f"unknown named synthetic lattice: {name!r}; fix the caller's lattice name"


def as_square_qq_matrix(matrix_data: object) -> Any:
    gram = named_gram(matrix_data) if _is_named_gram_data(matrix_data) else matrix(QQ, matrix_data)
    assert gram.is_square(), f"lattice Gram matrix must be square; found dimensions={gram.nrows()}x{gram.ncols()}; fix the caller's Gram data"
    assert gram == gram.transpose(), f"lattice Gram matrix must be symmetric (definitional for every object of the tree); found={gram}; fix the caller's Gram data"
    gram.set_immutable()
    return gram


def _is_named_gram_data(matrix_data: object) -> bool:
    return isinstance(matrix_data, str) or (isinstance(matrix_data, (list, tuple)) and len(matrix_data) == 2 and isinstance(matrix_data[0], str))


def signature_pair(gram_matrix: object) -> SignaturePair:
    positives, negatives, _zero = QuadraticForm(QQ, 2 * matrix(QQ, gram_matrix)).signature_vector()
    return positives, negatives


def rational_mod(value: Any, modulus: Any) -> Any:
    value = QQ(value)
    modulus = QQ(modulus)
    return value - modulus * (value / modulus).floor()
