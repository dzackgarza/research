"""Exact invariants of a symmetric matrix with rational entries.

Every function takes the Gram matrix of a symmetric bilinear form on a free
module of finite rank. All arithmetic is exact: integer matrices in FLINT,
rationals as `fractions.Fraction`.
"""

from fractions import Fraction
from math import isqrt, lcm

from flint import fmpz_mat

type Gram = tuple[tuple[Fraction, ...], ...]


def _cleared(gram: Gram) -> tuple[int, fmpz_mat]:
    """Return `(d, d * gram)` with `d` the least common denominator of the entries."""
    denominator = lcm(*(entry.denominator for row in gram for entry in row))
    return denominator, fmpz_mat([[int(entry * denominator) for entry in row] for row in gram])


def is_integer_matrix(gram: Gram) -> bool:
    return all(entry.denominator == 1 for row in gram for entry in row)


def determinant(gram: Gram) -> Fraction:
    denominator, cleared = _cleared(gram)
    return Fraction(int(cleared.det()), denominator ** len(gram))


def _sign_variations(coefficients: list[int]) -> int:
    nonzero = [coefficient for coefficient in coefficients if coefficient != 0]
    return sum(1 for left, right in zip(nonzero, nonzero[1:]) if (left > 0) != (right > 0))


def inertia(gram: Gram) -> tuple[int, int, int]:
    """Return `(n_plus, n_minus, n_zero)`, the numbers of positive, negative and zero eigenvalues.

    Let `p` be the characteristic polynomial, `V(p)` the number of sign
    variations of its nonzero coefficients, and `q(x) = p(-x)`. Descartes'
    rule of signs gives `n_plus <= V(p)` and `n_minus <= V(q)`
    (https://en.wikipedia.org/wiki/Descartes%27_rule_of_signs). A real
    symmetric matrix has only real eigenvalues, so
    `n_plus + n_minus + n_zero` is the degree. The assertion below checks
    `V(p) + V(q) + n_zero` against the degree; when it holds, both
    inequalities are equalities.
    """
    rank = len(gram)
    _, cleared = _cleared(gram)
    coefficients = [int(coefficient) for coefficient in cleared.charpoly().coeffs()]
    n_zero = next(index for index, coefficient in enumerate(coefficients) if coefficient != 0)
    n_plus = _sign_variations(coefficients)
    n_minus = _sign_variations([coefficient * (-1) ** index for index, coefficient in enumerate(coefficients)])
    assert n_plus + n_minus + n_zero == rank, "the characteristic polynomial of a symmetric matrix has only real roots"
    return n_plus, n_minus, n_zero


def discriminant_invariants(gram: Gram) -> tuple[int, ...]:
    """Return the invariant factors `d_1 | d_2 | ...`, each greater than 1, of the cokernel of `gram`.

    The Gram matrix must have integer entries and nonzero determinant. The
    cokernel of `L -> Hom(L, Z)`, `x -> b(x, -)`, is then the finite abelian
    group `Z/d_1 + Z/d_2 + ...`, the discriminant group of the lattice.
    """
    assert is_integer_matrix(gram), "the discriminant group is defined for an integer Gram matrix"
    rank = len(gram)
    _, cleared = _cleared(gram)
    smith = cleared.snf()
    diagonal = [abs(int(smith[index, index])) for index in range(rank)]
    assert all(entry != 0 for entry in diagonal), "the discriminant group is finite only for a nonzero determinant"
    return tuple(entry for entry in diagonal if entry > 1)


def is_rational_square(value: Fraction) -> bool:
    if value < 0:
        return False
    return isqrt(value.numerator) ** 2 == value.numerator and isqrt(value.denominator) ** 2 == value.denominator
