"""Exact invariants of a symmetric bilinear form with rational values.

Let `L` be a free module of finite rank over the integers with basis
`e_1, ..., e_n`, and `b` a symmetric bilinear form on `L` with rational
values. The Gram tensor of the lattice is `b` itself, a symmetric
(0,2)-tensor. Every function here takes its components `b(e_i, e_j)`.
All arithmetic is exact (FLINT).
"""

from fractions import Fraction
from itertools import combinations, product
from math import isqrt, lcm

from flint import fmpq, fmpq_mat, fmpz_mat

type GramTensor = tuple[tuple[Fraction, ...], ...]
"""Components: entry `[i][j]` is `b(e_i, e_j)`."""


def _components(gram_tensor: GramTensor) -> fmpq_mat:
    return fmpq_mat([[fmpq(value.numerator, value.denominator) for value in row] for row in gram_tensor])


def is_integer_valued(gram_tensor: GramTensor) -> bool:
    """Whether `b(x, y)` is an integer for all `x`, `y` in `L`: by bilinearity, whether every component is."""
    return all(value.denominator == 1 for row in gram_tensor for value in row)


def determinant(gram_tensor: GramTensor) -> Fraction:
    """Return `det(b(e_i, e_j))`.

    Another basis of `L` has components `b(e'_i, e'_j) = sum_kl P_ik b(e_k, e_l) P_jl`
    with `P` invertible over the integers, so the determinant changes by
    `det(P)^2 = 1`: it is an invariant of the lattice.
    """
    value = _components(gram_tensor).det()
    return Fraction(int(value.p), int(value.q))


def inertia(gram_tensor: GramTensor) -> tuple[int, int, int]:
    """Return `(n_plus, n_minus, n_zero)` for the form `b` on the rational vector space `V` that `L` spans.

    `V` has a basis `v_1, ..., v_n` with `b(v_i, v_j) = 0` for `i != j`, and
    the numbers of `i` with `b(v_i, v_i)` positive, negative and zero do not
    depend on that basis (Sylvester's law of inertia). Both statements:
    https://en.wikipedia.org/wiki/Symmetric_bilinear_form#Orthogonal_basis

    The loop is the induction that proves the first statement. It takes `v`
    with `b(v, v) != 0`, replaces each other vector `w` by
    `w - (b(w, v) / b(v, v)) v`, which is orthogonal to `v`, and continues in
    the span of the replaced vectors. When `b(x, x) = 0` for every remaining
    `x` and `b(x, y) != 0` for some pair, `v = x + y` has
    `b(v, v) = 2 b(x, y) != 0`. When no such pair exists, `b` vanishes on the
    span of the remaining vectors, and they complete the orthogonal basis.
    """
    rank = len(gram_tensor)
    components = _components(gram_tensor)

    def b(x: fmpq_mat, y: fmpq_mat) -> fmpq:
        return (x.transpose() * components * y)[0, 0]

    remaining = [fmpq_mat(rank, 1, [int(i == j) for i in range(rank)]) for j in range(rank)]
    values: list[fmpq] = []
    while remaining:
        position = next((i for i, x in enumerate(remaining) if b(x, x) != 0), None)
        if position is None:
            pair = next(((i, j) for i, j in combinations(range(len(remaining)), 2) if b(remaining[i], remaining[j]) != 0), None)
            if pair is None:
                break
            position = pair[0]
            remaining[position] = remaining[pair[0]] + remaining[pair[1]]
        v = remaining.pop(position)
        values.append(b(v, v))
        remaining = [w - v * (b(w, v) / values[-1]) for w in remaining]
    n_plus = sum(1 for value in values if value > 0)
    return n_plus, len(values) - n_plus, len(remaining)


def discriminant_invariants(gram_tensor: GramTensor) -> tuple[int, ...]:
    """Return the invariant factors `d_1 | d_2 | ...`, each greater than 1, of the discriminant group.

    `b` must be integer valued with nonzero determinant. The correlation
    `c: L -> Hom(L, Z)`, `x -> b(x, -)`, is then an injective morphism of free
    modules of the same rank, and the discriminant group is its cokernel, the
    finite abelian group `Z/d_1 + Z/d_2 + ...`. In the basis `e_i` of `L` and
    the basis of `Hom(L, Z)` dual to it, the matrix of `c` has the entries
    `b(e_i, e_j)`; its Smith normal form gives the `d_i`.
    """
    assert is_integer_valued(gram_tensor), "the correlation has values in Hom(L, Z) only for an integer-valued form"
    correlation = fmpz_mat([[int(value) for value in row] for row in gram_tensor])
    smith = correlation.snf()
    diagonal = [abs(int(smith[index, index])) for index in range(len(gram_tensor))]
    assert all(factor != 0 for factor in diagonal), "the cokernel of the correlation is finite only for a nonzero determinant"
    return tuple(factor for factor in diagonal if factor > 1)


def _integer_components(gram_tensor: GramTensor) -> tuple[int, tuple[tuple[int, ...], ...]]:
    """Return `(k, components of k b)` for the least positive integer `k` such that `k b` is integer valued."""
    scale = lcm(*(value.denominator for row in gram_tensor for value in row))
    return scale, tuple(tuple(int(value * scale) for value in row) for row in gram_tensor)


def _is_root(pairings: tuple[int, ...], norm: int) -> bool:
    """Whether a primitive `r` with `b(r, e_k) = pairings[k]` and `b(r, r) = norm` is a root of `L`: `norm != 0`, and the reflection `s_r` is in `O(L)`.

    `s_r(x) = x - (2 b(x, r) / b(r, r)) r` is an isometry of `L` tensor `Q`
    and its own inverse. It maps `L` into `L` exactly when
    `(2 b(x, r) / b(r, r)) r` is in `L` for every `x` in `L`. `r` is
    primitive, so that holds exactly when `2 b(x, r) / b(r, r)` is an
    integer, and by linearity in `x` exactly when it is for each `x = e_k`.

    The condition does not change when `b` is replaced by `k b`, `k != 0`.
    """
    return norm != 0 and all(2 * pairing % norm == 0 for pairing in pairings)


def generate(vectors: list[tuple[int, ...]], rank: int) -> bool:
    """Whether the vectors, given by their coordinates in the basis `e_i`, generate `L`.

    The morphism `Z^m -> L` that sends the basis to the vectors is surjective
    exactly when its cokernel is zero: when its Smith normal form has `rank`
    invariant factors, all equal to 1.
    """
    if len(vectors) < rank:
        return False
    smith = fmpz_mat(vectors).snf()
    return all(abs(int(smith[index, index])) == 1 for index in range(rank))


def generating_root_norms(gram_tensor: GramTensor) -> tuple[Fraction, ...] | None:
    """Return a set `S` of values of `b(r, r)` such that the roots `r` with `b(r, r)` in `S` generate `L`, or `None`.

    The roots are sought among the `r` with coordinates in `{-1, 0, 1}` and at
    most three nonzero coordinates. A returned `S` proves `L = Z Phi_S(L)`.
    `None` proves nothing: `L` can have roots that are not of that form.

    Among the sets that these roots prove, the result has the fewest elements,
    and then the least absolute values.
    """
    rank = len(gram_tensor)
    scale, components = _integer_components(gram_tensor)
    roots: dict[int, list[tuple[int, ...]]] = {}
    for size in range(1, min(rank, 3) + 1):
        for support in combinations(range(rank), size):
            for signs in product((1, -1), repeat=size - 1):
                coefficients = dict(zip(support, (1, *signs), strict=True))
                pairings = tuple(sum(sign * components[i][k] for i, sign in coefficients.items()) for k in range(rank))
                norm = sum(sign * pairings[i] for i, sign in coefficients.items())
                if _is_root(pairings, norm):
                    roots.setdefault(norm, []).append(tuple(coefficients.get(k, 0) for k in range(rank)))
    if not generate([r for found in roots.values() for r in found], rank):
        return None
    norms = sorted(roots, key=lambda norm: (abs(norm), norm))
    subsets = (subset for size in range(1, len(norms) + 1) for subset in combinations(norms, size))
    chosen = next(subset for subset in subsets if generate([r for norm in subset for r in roots[norm]], rank))
    return tuple(Fraction(norm, scale) for norm in chosen)


def is_rational_square(value: Fraction) -> bool:
    if value < 0:
        return False
    return isqrt(value.numerator) ** 2 == value.numerator and isqrt(value.denominator) ** 2 == value.denominator
