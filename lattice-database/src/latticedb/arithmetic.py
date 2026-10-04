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
from math import gcd, lcm

from cypari2 import Gen, Pari
from flint import fmpq, fmpq_mat, fmpz_mat

type GramTensor = tuple[tuple[Fraction, ...], ...]
"""Components: entry `[i][j]` is `b(e_i, e_j)`."""

type Vector = tuple[int, ...]
"""Coordinates of an element of `L` in the basis `e_1, ..., e_n`."""

# `qfisom` on two distinct even unimodular lattices of rank 16 grew the stack to 128 MB; the stack grows on demand up to this bound.
_PARI = Pari(sizemax=2**30)


def _components(gram_tensor: GramTensor) -> fmpq_mat:
    return fmpq_mat(
        [
            [fmpq(value.numerator, value.denominator) for value in row]
            for row in gram_tensor
        ]
    )


def is_perfect(rank: int, minimal_vectors: list[list[int]]) -> bool:
    """Whether the rank-one tensors of the minimal shell span Sym^2(Q^rank)."""
    rows = [
        [vector[i] * vector[j] for i in range(rank) for j in range(i, rank)]
        for vector in minimal_vectors
    ]
    return fmpq_mat(rows).rank() == rank * (rank + 1) // 2


def bad_reduction_primes(determinant: int) -> tuple[int, ...]:
    """Return the primes that divide `2 det`, in increasing order: the primes `p` at which `Q(x) = b(x, x)` is degenerate modulo `p`.

    For odd `p`, `Q` modulo `p` is nondegenerate exactly when `p` does not divide
    `det`. Modulo 2, `Q(x) = sum_i b(e_i, e_i) x_i^2` is the square of a linear
    form, so 2 is always among them.
    """
    assert determinant != 0, (
        "the reduction of a degenerate form is degenerate at every prime"
    )
    return tuple(int(prime) for prime in _PARI.factor(2 * abs(determinant))[0])


def quadratic_character(rank: int, determinant: int) -> int:
    """Return the discriminant `d` of the field `Q(sqrt(D))` for `D = (-1)^m det` and `rank = 2m`, and 1 when `D` is a square.

    For a prime `p` that does not divide `2 det`, the Kronecker symbol `(d / p)`
    is the Legendre symbol `(D / p)`, because `D / d` is the square of a
    rational number prime to `p`. It is 1 exactly when `Q` modulo `p` is the sum of
    `m` hyperbolic planes (Casselman, *Quadratic forms over finite fields*,
    Theorem 1.6). PARI's `coredisc` is the discriminant of `Q(sqrt(D))`.
    """
    assert rank % 2 == 0, "the character of the discriminant is stated for an even rank"
    assert determinant != 0, "the character requires a nonzero determinant"
    return int(_PARI.coredisc((-1) ** (rank // 2) * determinant))


SUBGROUP_BOUND = 100_000
"""`overlattice_count` decides a discriminant group with at most this number of subgroups.

Measured on 2026-10-01 with PARI 2.17: the count takes 0.06 s for `(Z/2)^7`
(29212 subgroups), 1.3 s for `(Z/2)^8` (417199) and 33 s for `(Z/2)^9`
(8283458), about 4 microseconds for each subgroup.
"""

# `forsubgroup` gives each subgroup `H` of `Z/c_1 + ... + Z/c_k` as a matrix whose columns generate it.
# The first loop counts the subgroups and stops above the bound; the second counts those on which the form vanishes.
_ISOTROPIC_SUBGROUPS = _PARI(
    "(cyc, N, e, bound) -> my(n = 0, c = 0); forsubgroup(H = cyc, , n++; if(n > bound, break)); if(n <= bound, forsubgroup(H = cyc, , if((H~ * N * H) % e == 0, c++))); [n, c]"
)


def overlattice_count(
    gram_tensor: GramTensor, bound: int = SUBGROUP_BOUND
) -> int | None:
    """Return the number of integral lattices `M` with `L <= M <= L^*`, or `None` when the discriminant group has more than `bound` subgroups.

    `b` must be integer valued with nonzero determinant. `L^*` is the set of
    `x` in `L (x) Q` with `b(x, L)` in `Z`, and `b` extends to it with rational
    values. The discriminant group is `A = L^* / L`, and
    `b_A(x + L, y + L) = b(x, y) + Z` is a symmetric bilinear form on `A` with
    values in `Q/Z`, defined because `b(L^*, L)` is in `Z`.

    A lattice `M` with `L <= M` of finite index is integral exactly when
    `b(M, M)` is in `Z`. Then `b(M, L)` is in `Z`, so `M <= L^*`. So the
    integral `M` are the subgroups `H = M / L` of `A` with `b_A(H, H) = 0`,
    and the function counts those subgroups. `H = 0` is `M = L`, which is
    counted: a unimodular lattice has the count 1. The count is of subgroups,
    not of their orbits under the isometries of `L`.

    `bound` is the budget of subgroups to enumerate. The count costs about 4
    microseconds for each subgroup, so `(Z/2)^8` (417199 subgroups) takes
    seconds and `(Z/2)^9` (8283458) minutes; a larger `bound` decides a larger
    group, at the cost of that time. The default `SUBGROUP_BOUND` leaves a
    value above it undecided (`None`).

    Computation. With `G` the matrix of the `b(e_i, e_j)`, `u -> G^-1 u` maps
    `Z^n` onto `L^*` (the columns of `G^-1` are the basis dual to the `e_i`)
    and `G Z^n` onto `L`, and `b(G^-1 u, G^-1 v) = u^T G^-1 v`. PARI's `matsnf`
    gives unimodular `U`, `V` with `U G V = D` diagonal, so `u -> U u` maps
    `Z^n / G Z^n` onto `Z^n / D Z^n`, and the generator `e_i` of the factor
    `Z / D_ii` is the class of `G^-1 U^-1 e_i`. On these generators `b_A` has
    the matrix `B = W^T G^-1 W` with `W = U^-1`. With `e` the largest `D_ii`,
    `N = e B` is an integer matrix, and `b_A` vanishes on the subgroup that the
    columns of `H` generate exactly when `H^T N H` is `0` modulo `e`, because
    `b_A` is bilinear.
    """
    assert is_integer_valued(gram_tensor), (
        "the dual lattice contains L only for an integer-valued form"
    )
    rank = len(gram_tensor)
    form = _PARI.matrix(
        rank, rank, [int(value) for row in gram_tensor for value in row]
    )
    left, _, smith = form.matsnf(1)
    diagonal = [abs(int(smith[index, index])) for index in range(rank)]
    assert all(factor != 0 for factor in diagonal), (
        "the discriminant group is finite only for a nonzero determinant"
    )
    cyclic_factors = [factor for factor in diagonal if factor > 1]
    assert diagonal[: len(cyclic_factors)] == cyclic_factors, (
        "matsnf puts the factors greater than 1 first"
    )
    if not cyclic_factors:
        return 1
    exponent = cyclic_factors[0]
    assert all(exponent % factor == 0 for factor in cyclic_factors), (
        "matsnf puts the largest factor first"
    )
    lift = left**-1
    scaled_form = exponent * (lift.mattranspose() * form**-1 * lift)
    size = len(cyclic_factors)
    form_on_generators = _PARI.matrix(
        size, size, [scaled_form[i, j] for i in range(size) for j in range(size)]
    )
    subgroups, isotropic = _ISOTROPIC_SUBGROUPS(
        cyclic_factors, form_on_generators, exponent, bound
    )
    return None if int(subgroups) > bound else int(isotropic)


def _integer_components(gram_tensor: GramTensor) -> tuple[int, tuple[Vector, ...]]:
    """Return `(k, components of k b)` for the least positive integer `k` such that `k b` is integer valued."""
    scale = lcm(*(value.denominator for row in gram_tensor for value in row))
    return scale, tuple(
        tuple(int(value * scale) for value in row) for row in gram_tensor
    )


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
    return (
        norm if norm != 0 and all(2 * value % norm == 0 for value in pairings) else None
    )


def is_root(gram_tensor: GramTensor, r: Vector) -> bool:
    """Whether `r` is a root of `L`. `L` and `L` with the form `k b`, `k != 0`, have the same roots."""
    return _root_norm(_integer_components(gram_tensor)[1], r) is not None


def _positive_integer_form(
    gram_tensor: GramTensor,
) -> tuple[int, tuple[Vector, ...], Gen]:
    """Return `(k, components of k b, PARI matrix of B)` for a definite `b`, where `B = k b` or `B = -k b` is positive definite and integer valued.

    `k` is the least positive integer for which `k b` is integer valued.

    The form must be definite: `B` is a positive definite integer matrix only
    then, and the algorithms that consume it decide an isometry or a minimal
    vector of a definite form.
    """
    assert is_definite(gram_tensor), (
        "this operation decides a definite form, and b is indefinite"
    )
    rank = len(gram_tensor)
    sign = 1 if gram_tensor[0][0] > 0 else -1
    scale, components = _integer_components(gram_tensor)
    return (
        scale,
        components,
        _PARI.matrix(rank, rank, [sign * value for row in components for value in row]),
    )


def minimum_and_kissing_number(gram_tensor: GramTensor) -> tuple[Fraction, int]:
    """Return the least value of `|b(x, x)|` over nonzero `x` and the number of `x` that attain it, for a definite `b`.

    PARI's `qfminim` enumerates the vectors of least norm of the positive
    definite integer form `B = k |b|` (Fincke and Pohst). The least value of
    `|b(x, x)|` is the least value of `B` divided by `k`, and the number of
    vectors counts both `x` and `-x`.
    """
    assert is_definite(gram_tensor), (
        "the minimum and kissing number decide a definite form, and b is indefinite"
    )
    scale, _, form = _positive_integer_form(gram_tensor)
    count, least, _ = form.qfminim(None, 0)
    return Fraction(int(least), scale), int(count)


def theta_coefficients(gram_tensor: GramTensor, bound: int) -> tuple[int, ...]:
    """Return `(a_0, ..., a_bound)`, `a_k` the number of `x` with `|b(x, x)| = k`, for a definite integer-valued `b`.

    PARI's `qfrep` counts, for `k = 1, ..., bound`, the pairs `x, -x` with `B(x, x) = k`.
    """
    assert is_definite(gram_tensor), (
        "the theta series decides a definite form, and b is indefinite"
    )
    assert is_integer_valued(gram_tensor), (
        "the coefficients of the theta series are indexed by integers only for an integer-valued form"
    )
    _, _, form = _positive_integer_form(gram_tensor)
    return (1, *(2 * int(pairs) for pairs in form.qfrep(bound)))


def is_isometric(gram_tensor: GramTensor, other: GramTensor) -> bool:
    """Whether the two definite lattices are isometric: whether some `g` in `GL_n(Z)` has `g^t b g = b'`.

    Isometric lattices have the same least `k` with `k b` integer valued, and
    are isometric exactly when the positive definite integer forms `k |b|`
    and `k |b'|` are. PARI's `qfisom` decides that by the algorithm of
    Plesken and Souvignier, and returns `0` when they are not.

    Both forms must be definite: `qfisom` decides the isometry of positive
    definite integer forms, and `_positive_integer_form` supplies it one only
    then. The isometry class of an indefinite lattice is decided instead by
    its genus invariants and spinor genus, not here.
    """
    assert is_definite(gram_tensor) and is_definite(other), (
        "isometry by `qfisom` is decided for definite forms; b or b' is indefinite"
    )
    assert len(gram_tensor) == len(other), "isometric lattices have the same rank"
    assert (gram_tensor[0][0] > 0) == (other[0][0] > 0), (
        "isometric lattices have the same sign"
    )
    scale, _, form = _positive_integer_form(gram_tensor)
    other_scale, _, other_form = _positive_integer_form(other)
    if scale != other_scale:
        return False
    return form.qfisom(other_form).type() != "t_INT"


def is_isotropic(gram_tensor: GramTensor) -> bool:
    """Whether `b(x, x) = 0` for some nonzero `x`, for a nondegenerate `b`.

    PARI's `qfsolve` returns a nonzero rational solution of `b(x, x) = 0`
    when one exists (a column), and an integer that names the obstruction
    when none does. A rational solution clears to an element of `L`.
    """
    rank = len(gram_tensor)
    assert determinant(gram_tensor) != 0, (
        "`qfsolve` decides isotropy of a nondegenerate form; a degenerate form is isotropic on its radical"
    )
    solution = _PARI.matrix(
        rank, rank, [str(value) for row in gram_tensor for value in row]
    ).qfsolve()
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
    assert is_definite(gram_tensor), (
        "the roots of a definite form are listed; b is indefinite"
    )
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
                roots[r if next(c for c in r if c) > 0 else tuple(-c for c in r)] = (
                    Fraction(norm, scale)
                )
    return roots


def generating_norms(roots: dict[Vector, Fraction], rank: int) -> tuple[Fraction, ...]:
    """Return a set `S` such that the given roots `r` with `b(r, r)` in `S` generate `L`. The given roots must generate `L`.

    Among the sets `S` of values `b(r, r)` of the given roots, the result has
    the fewest elements, and then the least absolute values.
    """
    norms = sorted(set(roots.values()), key=lambda norm: (abs(norm), norm))
    subsets = (
        subset
        for size in range(1, len(norms) + 1)
        for subset in combinations(norms, size)
    )
    from dzack_research.preamble.rings import session_ring_objects

    integers = session_ring_objects()["ZZ"]
    ambient = integers.free_module(rank)
    ambient_basis = tuple(ambient.module_generators())
    return next(
        subset
        for subset in subsets
        if all(
            generator
            in ambient.subobject_on(
                tuple(ambient(root) for root, norm in roots.items() if norm in subset)
            )
            for generator in ambient_basis
        )
    )
