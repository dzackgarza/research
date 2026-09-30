"""Exact invariants of a symmetric bilinear form with rational values.

Let `L` be a free module of finite rank over the integers with basis
`e_1, ..., e_n`, and `b` a symmetric bilinear form on `L` with rational
values. The Gram tensor of the lattice is `b` itself, a symmetric
(0,2)-tensor. Every function here takes its components `b(e_i, e_j)`.
All arithmetic is exact (FLINT, and PARI for the vectors `x` with `b(x, x)`
below a bound in a definite lattice).
"""

from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt, lcm

from cypari2 import Gen, Pari
from flint import fmpq, fmpq_mat, fmpz_mat

type GramTensor = tuple[tuple[Fraction, ...], ...]
"""Components: entry `[i][j]` is `b(e_i, e_j)`."""

type Vector = tuple[int, ...]
"""Coordinates of an element of `L` in the basis `e_1, ..., e_n`."""

_PARI = Pari()


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


def _integer_components(gram_tensor: GramTensor) -> tuple[int, tuple[Vector, ...]]:
    """Return `(k, components of k b)` for the least positive integer `k` such that `k b` is integer valued."""
    scale = lcm(*(value.denominator for row in gram_tensor for value in row))
    return scale, tuple(tuple(int(value * scale) for value in row) for row in gram_tensor)


def pairing(gram_tensor: GramTensor, x: Vector, y: Vector) -> Fraction:
    """Return `b(x, y)`."""
    return sum((x[i] * gram_tensor[i][j] * y[j] for i in range(len(x)) for j in range(len(y)) if x[i] and y[j]), Fraction(0))


def restriction(gram_tensor: GramTensor, vectors: tuple[Vector, ...]) -> GramTensor:
    """Return the components `b(v_i, v_j)` for the given vectors `v_1, v_2, ...`."""
    return tuple(tuple(pairing(gram_tensor, x, y) for y in vectors) for x in vectors)


def orthogonal_sum(summands: tuple[GramTensor, ...]) -> GramTensor:
    """Return the components of the form of the orthogonal sum, in the union of the bases of the summands."""
    offsets = [sum(len(summand) for summand in summands[:index]) for index in range(len(summands))]
    rank = sum(len(summand) for summand in summands)
    rows = [[Fraction(0)] * rank for _ in range(rank)]
    for offset, summand in zip(offsets, summands, strict=True):
        for i, row in enumerate(summand):
            rows[offset + i][offset : offset + len(summand)] = row
    return tuple(tuple(row) for row in rows)


def _root_norm(components: tuple[Vector, ...], r: Vector) -> int | None:
    """Return `b(r, r)` when `r` is a root of `L`, for an integer-valued `b` with the given components, and `None` when `r` is not a root.

    A root is a primitive `r` with `b(r, r) != 0` such that the reflection
    `s_r` is in `O(L)`. `s_r(x) = x - (2 b(x, r) / b(r, r)) r` is an isometry
    of `L` tensor `Q` and its own inverse. It maps `L` into `L` exactly when
    `(2 b(x, r) / b(r, r)) r` is in `L` for every `x` in `L`. `r` is
    primitive, so that holds exactly when `2 b(x, r) / b(r, r)` is an
    integer, and by linearity in `x` exactly when it is for each `x = e_k`.
    """
    if gcd(*r) != 1:
        return None
    pairings = [sum(row[i] * r[i] for i in range(len(r))) for row in components]
    norm = sum(pairings[i] * r[i] for i in range(len(r)))
    return norm if norm != 0 and all(2 * value % norm == 0 for value in pairings) else None


def is_root(gram_tensor: GramTensor, r: Vector) -> bool:
    """Whether `r` is a root of `L`. `L` and `L` with the form `k b`, `k != 0`, have the same roots."""
    return _root_norm(_integer_components(gram_tensor)[1], r) is not None


def pari_version() -> tuple[int, int, int]:
    """The version of the PARI library that computes here."""
    major, minor, patch = _PARI.version()
    return int(major), int(minor), int(patch)


def _positive_integer_form(gram_tensor: GramTensor) -> tuple[int, tuple[Vector, ...], Gen]:
    """Return `(k, components of k b, PARI matrix of B)` for a definite `b`, where `B = k b` or `B = -k b` is positive definite and integer valued.

    `k` is the least positive integer for which `k b` is integer valued.
    """
    rank = len(gram_tensor)
    sign = 1 if gram_tensor[0][0] > 0 else -1
    scale, components = _integer_components(gram_tensor)
    return scale, components, _PARI.matrix(rank, rank, [sign * value for row in components for value in row])


def minimum_and_kissing_number(gram_tensor: GramTensor) -> tuple[Fraction, int]:
    """Return the least value of `|b(x, x)|` over nonzero `x` and the number of `x` that attain it, for a definite `b`.

    PARI's `qfminim` enumerates the vectors of least norm of the positive
    definite integer form `B = k |b|` (Fincke and Pohst). The least value of
    `|b(x, x)|` is the least value of `B` divided by `k`, and the number of
    vectors counts both `x` and `-x`.
    """
    scale, _, form = _positive_integer_form(gram_tensor)
    count, least, _ = form.qfminim(None, 0)
    return Fraction(int(least), scale), int(count)


def theta_coefficients(gram_tensor: GramTensor, bound: int) -> tuple[int, ...]:
    """Return `(a_0, ..., a_bound)`, `a_k` the number of `x` with `|b(x, x)| = k`, for a definite integer-valued `b`.

    PARI's `qfrep` counts, for `k = 1, ..., bound`, the pairs `x, -x` with `B(x, x) = k`.
    """
    assert is_integer_valued(gram_tensor), "the coefficients of the theta series are indexed by integers only for an integer-valued form"
    _, _, form = _positive_integer_form(gram_tensor)
    return (1, *(2 * int(pairs) for pairs in form.qfrep(bound)))


def is_isotropic(gram_tensor: GramTensor) -> bool:
    """Whether `b(x, x) = 0` for some nonzero `x`, for a nondegenerate `b`.

    PARI's `qfsolve` returns a nonzero rational solution of `b(x, x) = 0`
    when one exists (a column), and an integer that names the obstruction
    when none does. A rational solution clears to an element of `L`.
    """
    rank = len(gram_tensor)
    assert determinant(gram_tensor) != 0, "`qfsolve` decides isotropy of a nondegenerate form; a degenerate form is isotropic on its radical"
    solution = _PARI.matrix(rank, rank, [str(value) for row in gram_tensor for value in row]).qfsolve()
    return solution.type() == "t_COL"


def definite_roots(gram_tensor: GramTensor) -> dict[Vector, Fraction]:
    """Return the roots of `L` for a definite `b`: one of `r`, `-r` for each root, with `b(r, r)`.

    Let `B = k b` be integer valued and positive definite, `k` an integer.
    Let `r` be a root and `B(r, L) = d Z`, `d > 0`. `B(r, r)` is in `d Z` and
    divides `2 d`, so `B(r, r)` is `d` or `2 d`. `r / d` is in the dual
    lattice `L*` of `(L, B)`, and its class in `L* / L` has order `d`,
    because `r` is primitive; so `d` divides the exponent `e` of `L* / L`.

    For each `d` that divides `e`, the roots with `B(r, L) = d Z` are
    therefore among the `x` in `L_d = {x in L : B(x, L) in d Z}` with
    `B(x, x) / d <= 2`, which PARI's `qfminim` lists for the positive
    definite form `B / d` on `L_d`. `matsnf` gives `U`, `V` invertible over
    the integers with `U B V` diagonal, with entries `D_i`. For `x = V y`,
    `B x` is in `d Z^n` exactly when each `D_i y_i` is in `d Z`, so the
    columns of `V diag(d / gcd(d, D_i))` are a basis of `L_d`.
    """
    rank = len(gram_tensor)
    scale, components, form = _positive_integer_form(gram_tensor)
    _, right, smith = form.matsnf(1)
    diagonal = [abs(int(smith[i, i])) for i in range(rank)]
    exponent = max(diagonal)
    roots: dict[Vector, Fraction] = {}
    for d in (d for d in range(1, exponent + 1) if exponent % d == 0):
        basis = right * _PARI.matdiagonal([d // gcd(d, factor) for factor in diagonal])
        short = basis * (basis.mattranspose() * form * basis / d).qfminim(2, None, 0)[2]
        for column in range(short.ncols()):
            r = tuple(int(short[i, column]) for i in range(rank))
            norm = _root_norm(components, r)
            if norm is not None:
                roots[r if next(c for c in r if c) > 0 else tuple(-c for c in r)] = Fraction(norm, scale)
    return roots


def invariant_factors(vectors: list[Vector], rank: int) -> tuple[int, ...]:
    """Return the nonzero invariant factors `d_1 | d_2 | ...` of the morphism `Z^m -> L` that sends the basis to the vectors.

    Let `M` be the image, and `M'` the primitive sublattice `L cap (M tensor Q)`.
    The number of factors is the rank of `M`, and `M' / M` is
    `Z/d_1 + Z/d_2 + ...`: the product of the factors is `[M' : M]`.
    """
    if not vectors:
        return ()
    smith = fmpz_mat(vectors).snf()
    diagonal = (abs(int(smith[index, index])) for index in range(min(len(vectors), rank)))
    return tuple(factor for factor in diagonal if factor != 0)


def generate(vectors: list[Vector], rank: int) -> bool:
    """Whether the vectors generate `L`: whether the morphism `Z^m -> L` has `rank` invariant factors, all equal to 1."""
    return invariant_factors(vectors, rank) == (1,) * rank


def span_basis(vectors: list[Vector]) -> tuple[Vector, ...]:
    """Return the basis in Hermite normal form of the sublattice that the vectors generate.

    Two lists of vectors generate the same sublattice exactly when they have the same result.
    """
    if not vectors:
        return ()
    hermite = fmpz_mat(vectors).hnf()
    rows = (tuple(int(hermite[i, j]) for j in range(hermite.ncols())) for i in range(hermite.nrows()))
    return tuple(row for row in rows if any(row))


def generating_norms(roots: dict[Vector, Fraction], rank: int) -> tuple[Fraction, ...]:
    """Return a set `S` such that the given roots `r` with `b(r, r)` in `S` generate `L`. The given roots must generate `L`.

    Among the sets `S` of values `b(r, r)` of the given roots, the result has
    the fewest elements, and then the least absolute values.
    """
    norms = sorted(set(roots.values()), key=lambda norm: (abs(norm), norm))
    subsets = (subset for size in range(1, len(norms) + 1) for subset in combinations(norms, size))
    return next(subset for subset in subsets if generate([r for r, norm in roots.items() if norm in subset], rank))


def is_rational_square(value: Fraction) -> bool:
    if value < 0:
        return False
    return isqrt(value.numerator) ** 2 == value.numerator and isqrt(value.denominator) ** 2 == value.denominator
