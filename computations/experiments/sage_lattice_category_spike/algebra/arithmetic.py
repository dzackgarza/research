r"""Exact arithmetic helpers for the synthetic lattice spike."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeGuard, cast

from sage.combinat.root_system.cartan_matrix import CartanMatrix
from sage.matrix.constructor import matrix
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.rational_field import QQ
from sage.structure.element import Matrix

from ..lexicon.foundations import CartanType, GramMatrix, SignaturePair

if TYPE_CHECKING:
    from .domain_algebra import LatticeName


def named_gram(name: object) -> Matrix:
    if name == "U" or name == "H":
        return matrix(QQ, 2, 2, [0, 1, 1, 0])
    cartan_type = named_cartan_type(name)
    assert cartan_type is not None, f"unknown named synthetic lattice: {name!r}; fix the caller's lattice name"
    return matrix(QQ, CartanMatrix(list(cartan_type)))


def named_cartan_type(name: object) -> CartanType | None:
    r"""The Cartan datum a lattice name designates, or None for U/H.

    The name is construction data, so the datum it resolves to is a
    provenance certificate (never detected from the Gram); only the
    simply-laced A/D/E types have symmetric Cartan matrices, hence Grams."""
    if name == "U" or name == "H":
        return None
    if isinstance(name, str) and len(name) >= 2 and name[1:].isdigit():
        letter, rank = name[0].upper(), int(name[1:])
    elif isinstance(name, (list, tuple)) and len(name) == 2:
        letter, rank = str(name[0]).upper(), int(name[1])
    else:
        assert False, f"unknown named synthetic lattice: {name!r}; fix the caller's lattice name"
    assert letter in ("A", "D", "E"), (
        f"named lattices are U/H and the simply-laced types A/D/E (B/C/F/G Cartan matrices are not symmetric, hence not Gram matrices); found {name!r}"
    )
    return cast("CartanType", (letter, rank))


def as_square_qq_matrix(matrix_data: object) -> GramMatrix:
    """The one Gram codec: parse, assert square + symmetric (definitional for
    every object of the tree), immutabilize, and return the witness."""
    gram = named_gram(matrix_data) if is_named_gram_data(matrix_data) else matrix(QQ, matrix_data)
    assert gram.is_square(), f"lattice Gram matrix must be square; found dimensions={gram.nrows()}x{gram.ncols()}; fix the caller's Gram data"
    assert gram == gram.transpose(), f"lattice Gram matrix must be symmetric (definitional for every object of the tree); found={gram}; fix the caller's Gram data"
    gram.set_immutable()
    return GramMatrix(gram)


def is_named_gram_data(matrix_data: object) -> TypeGuard[LatticeName]:
    return isinstance(matrix_data, str) or (isinstance(matrix_data, (list, tuple)) and len(matrix_data) == 2 and isinstance(matrix_data[0], str))


def signature_pair(gram_matrix: object) -> SignaturePair:
    positives, negatives, _zero = QuadraticForm(QQ, 2 * matrix(QQ, gram_matrix)).signature_vector()
    return positives, negatives


def rational_mod(value: Any, modulus: Any) -> Any:
    value = QQ(value)
    modulus = QQ(modulus)
    return value - modulus * (value / modulus).floor()
