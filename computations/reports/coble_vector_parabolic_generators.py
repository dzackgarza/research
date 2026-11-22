"""Explicit generating family of the stabilizer of a primitive isotropic vector.

For B = U_1 + U_2 + <-1>^7 (basis e_1, f_1, e_2, f_2, d_1, ..., d_7) and
v = e_1, this certifies the structure Stab_{O(B)}(v) = O(K) x| K_ev of
lem:cusp-vector-stabilizer-image, K = U_2 + <-1>^7 = v^perp / Z v:

* the nine integral Eichler transvections E(v, k_i) for the Z-basis
  e_2, f_2, d_1 + d_7, ..., d_6 + d_7, 2 d_7 of K_ev = {k in K : k^2 even},
  each an exact integer matrix preserving the Gram matrix and fixing v;
  their reductions modulo 2 generate a group of order 2^8 on K/2K;
* the integral reflections of K in vectors w with w^2 = -2 or w^2 = 2,
  transported by the identity on U_1, which fix v; their reductions generate
  a group of order 348364800 = |O(q_{K(2)})| = |GO^+_8(2)| on K/2K;
* the two families together generate a group of order 89181388800 =
  |O(q)| / 527 = |Stab_{O(q)}([v/2])| on the 2048 classes of B/2B.

No floating point. Group orders are computed by Schreier-Sims (sympy) on the
faithful permutation action. Run: python3 coble_vector_parabolic_generators.py
"""
import itertools

N = 11
# index 0 = e_1, 1 = f_1, 2 = e_2, 3 = f_2, 4..10 = d_1..d_7
GRAB = [[0] * N for _ in range(N)]
GRAB[0][1] = GRAB[1][0] = 1
GRAB[2][3] = GRAB[3][2] = 1
for i in range(4, N):
    GRAB[i][i] = -1

KIDX = list(range(2, N))


def ip(x, y):
    return sum(x[i] * GRAB[i][j] * y[j] for i in range(N) for j in range(N))


def sq(x):
    return ip(x, x)


def unit(i):
    x = [0] * N
    x[i] = 1
    return x


V = unit(0)


def columns_to_matrix(cols):
    return [[cols[j][i] for j in range(N)] for i in range(N)]


def eichler(vv, k):
    """E(vv,k)(x) = x + (vv,x)k - ((k,x) + k^2/2 (vv,x)) vv, integral for k^2 even."""
    assert sq(k) % 2 == 0
    cols = []
    for j in range(N):
        x = unit(j)
        a = ip(vv, x)
        b = ip(k, x)
        cols.append([x[i] + a * k[i] - (b + (sq(k) // 2) * a) * vv[i]
                     for i in range(N)])
    return columns_to_matrix(cols)


def reflection(w):
    q = sq(w)
    assert q in (-2, 2), q
    cols = []
    for j in range(N):
        x = unit(j)
        c = 2 * ip(x, w) // q
        cols.append([x[i] - c * w[i] for i in range(N)])
    return columns_to_matrix(cols)


def preserves_gram(m):
    return all(sum(m[a][i] * GRAB[a][b] * m[b][j]
                   for a in range(N) for b in range(N)) == GRAB[i][j]
               for i in range(N) for j in range(N))


def apply(m, x):
    return [sum(m[i][j] * x[j] for j in range(N)) for i in range(N)]


KEV = [unit(2), unit(3)]
KEV += [[a + b for a, b in zip(unit(3 + i), unit(10))] for i in range(1, 7)]
KEV += [[2 * a for a in unit(10)]]
assert len(KEV) == 9 and all(sq(k) % 2 == 0 for k in KEV)
# integral basis of K_ev of index 2 in K: determinant of the coefficient matrix
COEFF = [[k[i] for i in KIDX] for k in KEV]


def det_int(m):
    """exact determinant by fraction-free elimination"""
    from fractions import Fraction
    a = [[Fraction(x) for x in row] for row in m]
    n = len(a)
    d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if a[r][c] != 0), None)
        assert p is not None
        if p != c:
            a[c], a[p] = a[p], a[c]
            d = -d
        d *= a[c][c]
        for r in range(c + 1, n):
            f = a[r][c] / a[c][c]
            for cc in range(c, n):
                a[r][cc] -= f * a[c][cc]
    return int(d)


print("K_ev basis squares:", [sq(k) for k in KEV])
print("index of K_ev in K:", det_int(COEFF))

TRANS = [eichler(V, k) for k in KEV]
print("nine transvections integral and Gram-preserving:",
      all(preserves_gram(m) for m in TRANS))
print("nine transvections fix v:", all(apply(m, V) == V for m in TRANS))
print("nine transvections act trivially on v^perp/Zv:",
      all(all(d == 0 for d in [a - b for a, b in zip(apply(m, x), x)][1:])
          for x in [unit(0)] + [unit(i) for i in KIDX] for m in TRANS))

REFS = {}
for coeffs in itertools.product([-1, 0, 1], repeat=9):
    w = [0] * N
    for c, i in zip(coeffs, KIDX):
        w[i] = c
    if sq(w) in (-2, 2):
        m = reflection(w)
        assert preserves_gram(m) and apply(m, V) == V
        REFS.setdefault(tuple(map(tuple, m)), m)
print("distinct integral reflections of K in vectors of square +-2:", len(REFS))

from sympy.combinatorics import Permutation, PermutationGroup

A = list(itertools.product([0, 1], repeat=N))
AIDX = {a: i for i, a in enumerate(A)}


def perm_a(m):
    return tuple(AIDX[tuple(y % 2 for y in apply(m, a))] for a in A)


KK = list(itertools.product([0, 1], repeat=9))
KID = {a: i for i, a in enumerate(KK)}


def perm_k(m):
    out = []
    for a in KK:
        x = [0] * N
        for c, j in zip(a, KIDX):
            x[j] = c
        y = apply(m, x)
        out.append(KID[tuple(y[j] % 2 for j in KIDX)])
    return tuple(out)


GU = PermutationGroup([Permutation(perm_a(m)) for m in TRANS])
GR = PermutationGroup([Permutation(perm_a(m)) for m in REFS.values()])
GF = PermutationGroup([Permutation(perm_a(m)) for m in TRANS + list(REFS.values())])
print("order of the transvection images on B/2B:", GU.order())
print("order of the reflection images on B/2B:", GR.order())
print("order of the full family on B/2B:", GF.order())
assert GU.order() == 2 ** 8
assert GR.order() == 348364800
assert GF.order() == 89181388800
