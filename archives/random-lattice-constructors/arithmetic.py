r"""Exact arithmetic helpers for the synthetic lattice spike."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeGuard, cast

from sage.combinat.root_system.cartan_matrix import CartanMatrix
from sage.matrix.constructor import diagonal_matrix, matrix, random_matrix
from sage.misc.randstate import seed as random_seed
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ
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
    gram = named_gram(matrix_data) if _is_named_gram_data(matrix_data) else matrix(QQ, matrix_data)
    assert gram.is_square(), f"lattice Gram matrix must be square; found dimensions={gram.nrows()}x{gram.ncols()}; fix the caller's Gram data"
    assert gram == gram.transpose(), f"lattice Gram matrix must be symmetric (definitional for every object of the tree); found={gram}; fix the caller's Gram data"
    gram.set_immutable()
    return GramMatrix(gram)


def _is_named_gram_data(matrix_data: object) -> TypeGuard[LatticeName]:
    return isinstance(matrix_data, str) or (isinstance(matrix_data, (list, tuple)) and len(matrix_data) == 2 and isinstance(matrix_data[0], str))


def _random_unimodular_congruence(seed_gram: Matrix) -> Matrix:
    r"""Conjugate ``seed_gram`` by a random ``SL(n, ZZ)`` matrix ``A``: the
    ``algorithm="unimodular"`` draw has determinant exactly ``+1``. The
    congruence ``A^T G A`` keeps the SIGNATURE of ``G`` by Sylvester's law of
    inertia (true for any real invertible ``A``, independent of ``det(A)``), and
    keeps the DETERMINANT because ``det(A^T G A) = det(A)^2 det(G) = det(G)``
    using ``det(A)^2 = 1``. The caller scopes the random state (via ``seed``)
    and chooses the diagonal seed's invariants.
    """
    basis_change = random_matrix(ZZ, seed_gram.nrows(), algorithm="unimodular")
    return basis_change.transpose() * seed_gram * basis_change


def random_gram_of_signature(pos: int, neg: int, *, seed: int) -> Matrix:
    r"""A random integral Gram matrix of signature ``(pos, neg)``, general
    determinant (random positive magnitudes on the diagonal seed).

    Construction DATA, not a lattice: hand it to ``Lattice`` to get a lattice
    routed into its existing category by refinement. There is no "random
    lattice" object -- randomness is a property of this generator.
    """
    assert pos >= 0 and neg >= 0 and pos + neg > 0, f"signature must be nonnegative with positive rank; got ({pos}, {neg})"
    with random_seed(seed):
        diagonal = [ZZ.random_element(1, 4) for _ in range(pos)] + [-ZZ.random_element(1, 4) for _ in range(neg)]
        return _random_unimodular_congruence(diagonal_matrix(ZZ, diagonal))


def random_unimodular_gram_of_signature(pos: int, neg: int, *, seed: int) -> Matrix:
    r"""A random unimodular integral Gram matrix of signature ``(pos, neg)``: the
    unit-diagonal seed ``diag(1^pos, (-1)^neg)`` has determinant ``+-1``,
    preserved by the congruence."""
    assert pos >= 0 and neg >= 0 and pos + neg > 0, f"signature must be nonnegative with positive rank; got ({pos}, {neg})"
    with random_seed(seed):
        return _random_unimodular_congruence(diagonal_matrix(ZZ, [1] * pos + [-1] * neg))


def random_gram_of_determinant(determinant: int, rank: int, *, seed: int) -> Matrix:
    r"""A random integral Gram matrix of the given ``determinant``: the seed
    ``diag(determinant, 1, ..., 1)`` has that determinant, preserved by the
    congruence."""
    assert determinant != 0 and rank > 0, f"determinant must be nonzero and rank positive; got determinant={determinant}, rank={rank}"
    with random_seed(seed):
        return _random_unimodular_congruence(diagonal_matrix(ZZ, [determinant] + [1] * (rank - 1)))


def random_gram_of_rank(rank: int, *, seed: int) -> Matrix:
    r"""A random nondegenerate integral Gram matrix of the given ``rank``, with no
    constraint on signature or determinant: a random nonzero-diagonal seed under
    the congruence."""
    assert rank > 0, f"rank must be positive; got {rank}"
    with random_seed(seed):
        diagonal = [ZZ.random_element(1, 4) if ZZ.random_element(0, 2) == 0 else -ZZ.random_element(1, 4) for _ in range(rank)]
        return _random_unimodular_congruence(diagonal_matrix(ZZ, diagonal))


def signature_pair(gram_matrix: object) -> SignaturePair:
    positives, negatives, _zero = QuadraticForm(QQ, 2 * matrix(QQ, gram_matrix)).signature_vector()
    return positives, negatives


def rational_mod(value: Any, modulus: Any) -> Any:
    value = QQ(value)
    modulus = QQ(modulus)
    return value - modulus * (value / modulus).floor()
