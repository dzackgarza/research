"""The integral isometry behind the congruence group: sigma = s_{e'-f'} on T_Co.

    python3 computations/reports/coble_swap_isometry.py

No Sage: everything below is exact integer and Fraction arithmetic on the Gram matrix, so the
certificate does not depend on the maintained lattice machinery (the same reason
`plane_gluing_subgroup.py` is written this way).

T_Co = <2> + U(2) + E8(2), basis zeta; e', f'; a_1..a_8, exactly as in the manuscript (the <2>
generator is zeta in lem:coble-heegner-vector and h in plane_gluing_subgroup.py, which is where this
Gram matrix is taken from).  The isometry is

    sigma : e' <-> f',     h and a_1..a_8 fixed,

which is the transposition of the two isotropic generators of the U(2) summand.  What is checked:

  * sigma is an integral isometry of T_Co: M G M^T = G with M integral, M^2 = 1, M != 1, det M = -1;
  * sigma is the reflection s_v in v = e' - f', of square v^2 = -4: s_v applied to every basis
    vector agrees with M.  Since the spinor norm of a reflection is [-b(w,w)/2] by the book's
    `def:spinor-norm`, s_v has spinor norm [2] = 1 in R^x/(R^x)^2, so sigma lies in Theta_R(T_Co) =
    Orth^+(T_Co);
  * A_{T_Co} = T_Co^vee/T_Co has exponent 2 and order 2048 = |det T_Co|, so it is (Z/2)^11, which is
    the book's description; the classes are the halves of the 2048 parity vectors mod 2T_Co;
  * the action of sigma on A_{T_Co} transposes the two isotropic classes e'/2 and f'/2, fixes the
    class h/2, and fixes every class of the E8(2) block.  So rho(sigma) lies in
    O(q_{U(2)}) x O(q_{E8(2)}) and is not the identity, whereas Gamma_Co = Orth^+(T_Co) cap ker(rho);
  * the isometry group of the four-element space A_{U(2)} = <e'/2, f'/2> is exactly {id, swap}, so
    rho(sigma) generates the U(2) factor of that product.

Consequence, and the only one asserted: sigma is an *integral* witness that the congruence preimage
rho^{-1}(P) is strictly larger than the stable group, in the component-preserving half.  Nontriviality
of P alone would not give that: a preimage of a nontrivial subgroup of Orth(A,q) is larger than the
kernel only if some element of the subgroup is realised by an isometry of the lattice, and sigma is
that realisation for the swap.

What is *not* claimed here: nothing about Gamma^Hdg.  Deciding whether the Heegner group strictly
contains Gamma_Co needs an element of Gamma_{En,2} that fixes the Heegner line and acts nontrivially
on A_{T_Co}; this script exhibits no such element, so that strictness stays open.
"""
from fractions import Fraction
from itertools import product, permutations

# E8 Cartan matrix from the Dynkin diagram: 1-3-4-5-6-7-8 with 2 attached to 3.
EDGES = [(1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
CARTAN = [[2 if i == j else 0 for j in range(1, 9)] for i in range(1, 9)]
for i, j in EDGES:
    CARTAN[i - 1][j - 1] = CARTAN[j - 1][i - 1] = -1

# GRAM = <2> perp U(2) perp E8(2); E8(2) = -2 * Cartan(E8) (negative definite, even).
n = 11
G = [[0] * n for _ in range(n)]
G[0][0] = 2                                    # <2>, zeta
G[1][2] = G[2][1] = 2                          # U(2), e', f'
for i in range(8):
    for j in range(8):
        G[3 + i][3 + j] = -2 * CARTAN[i][j]    # E8(2), a_1..a_8
assert all(G[i][j] == G[j][i] for i in range(n) for j in range(n)), 'GRAM not symmetric'
assert all(G[i][i] % 2 == 0 for i in range(n)), 'GRAM not even'


def det_int(M):
    """Exact determinant of an integer matrix, by fraction-free elimination on Fractions."""
    M = [[Fraction(x) for x in row] for row in M]
    m = len(M)
    d = Fraction(1)
    for c in range(m):
        p = next((r for r in range(c, m) if M[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, m):
            f = M[r][c] / M[c][c]
            for k in range(c, m):
                M[r][k] -= f * M[c][k]
    return d


def b(c1, c2):
    return sum(c1[i] * G[i][j] * c2[j] for i in range(n) for j in range(n))


def pad(v):
    return [Fraction(x) for x in v]


def integral(c):
    return all(Fraction(x).denominator == 1 for x in c)


def mod_lattice(c):
    """Class of c in Q^n / Z^n, i.e. coordinates mod 1."""
    return tuple(Fraction(x) % 1 for x in c)


# ---------------------------------------------------------------- sigma as a matrix
# Column j is the image of basis vector j: e' -> f', f' -> e', everything else fixed.
M = [[0] * n for _ in range(n)]
for j in range(n):
    M[j][j] = 1
M[1][1] = M[2][2] = 0
M[1][2] = M[2][1] = 1

print('T_Co = <2> + U(2) + E8(2);  sigma: e\' <-> f\', zeta and a_1..a_8 fixed')
print('  |det T_Co| = %d' % abs(det_int(G)))
assert abs(det_int(G)) == 2048, 'this is not T_Co: |A_{T_Co}| should be 2048'


def apply(v):
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def mat_mul(P, Q):
    return [[sum(P[i][k] * Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


M2 = mat_mul(M, M)
assert all(M2[i][j] == (1 if i == j else 0) for i in range(n) for j in range(n)), 'sigma^2 != 1'
assert any(M[i][j] != (1 if i == j else 0) for i in range(n) for j in range(n)), 'sigma = 1'
print('  sigma integral, sigma^2 = 1, sigma != 1, det sigma = %d' % det_int(M))

MGM = mat_mul(mat_mul(M, G), [[M[j][i] for j in range(n)] for i in range(n)])
assert all(MGM[i][j] == G[i][j] for i in range(n) for j in range(n)), 'sigma is not an isometry'
print('  M G M^T = G: sigma is an integral isometry of T_Co')

# ---------------------------------------------------------------- sigma is s_{e'-f'}
v = [0] * n
v[1], v[2] = 1, -1                              # e' - f'
vv = b(v, v)
print('  v = e\' - f\', v^2 = %d' % vv)
assert vv == -4
for j in range(n):
    x = [0] * n
    x[j] = 1
    # s_v(x) = x - 2 b(x,v)/b(v,v) * v
    s = [Fraction(x[i]) - Fraction(2 * b(x, v), vv) * v[i] for i in range(n)]
    assert [Fraction(t) for t in apply(x)] == s, 'sigma is not the reflection in e\' - f\''
print('  sigma = s_v, the reflection in v, on every basis vector')
# Spinor norm of a reflection is [-b(w,w)/2] by def:spinor-norm; for w = v that is [4/2] = [2].
print('  sn(sigma) = [-v^2/2] = [%s] = 1 in R^x/(R^x)^2, so sigma lies in Theta_R(T_Co) = Orth^+(T_Co)'
      % Fraction(-vv, 2))
assert Fraction(-vv, 2) > 0, 'the reflection would not lie in the spinor kernel'

# ---------------------------------------------------------------- A_{T_Co} = (Z/2)^11
# x in T_Co^vee iff b(x, basis_i) is integral for every i, i.e. G x is integral.
parity = list(product([0, 1], repeat=n))
assert len(parity) == 2048
halves = {}
for k in parity:
    x = [Fraction(ki, 2) for ki in k]
    pairing = [sum(G[i][j] * x[j] for j in range(n)) for i in range(n)]
    assert integral(pairing), 'half of a parity vector %r is not in T_Co^vee' % (k,)
    halves[k] = mod_lattice(x)
print('  all %d halves of parity vectors lie in T_Co^vee' % len(parity))
assert len(set(halves.values())) == 2048, 'the classes of the halves are not distinct'
print('  T_Co^vee/T_Co has order 2048 = |det T_Co| and exponent 2, i.e. (Z/2)^11')

ZERO = (Fraction(0),) * n


def key(k):
    return halves[k]


def cls_half(k):
    return halves[k]


H = [0] * n
H[0] = 1
E1 = [0] * n
E1[1] = 1
F1 = [0] * n
F1[2] = 1


def parity_of(vec):
    """The parity vector k with vec = k/2 mod T_Co, or None if vec is not of that shape."""
    out = []
    for x in vec:
        y = Fraction(x) * 2
        if y.denominator != 1 or y % 2 not in (0, 1):
            return None
        out.append(int(y % 2))
    return tuple(out)


# The class of v/2 is the half of the parity vector (coordinates of v mod 2).
def kof(vec):
    return tuple(int(x) % 2 for x in vec)


kH, kE, kF = kof(H), kof(E1), kof(F1)
print('  classes [h/2], [e\'/2], [f\'/2] are nonzero: h, e\', f\' are primitive in T_Co')
assert key(kE) == mod_lattice([Fraction(x, 2) for x in E1])
assert key(kE) != ZERO and key(kF) != ZERO
assert b([Fraction(x, 2) for x in E1], [Fraction(x, 2) for x in E1]) == 0
assert b([Fraction(x, 2) for x in F1], [Fraction(x, 2) for x in F1]) == 0
print('  both are isotropic: b(e\'/2, e\'/2) = b(f\'/2, f\'/2) = 0')

# ---------------------------------------------------------------- the induced action
def act_class(k):
    """sigma on the class k/2: apply M to k and read off the class."""
    img = apply([Fraction(x, 2) for x in k])
    kk = parity_of(img)
    assert kk is not None
    return kk


assert act_class(kE) == kF, 'sigma does not carry [e\'/2] to [f\'/2]'
assert act_class(kF) == kE, 'sigma does not carry [f\'/2] to [e\'/2]'
assert act_class(kH) == kH, 'sigma does not fix [h/2]'
print('  sigma transposes [e\'/2] and [f\'/2] and fixes [h/2]')

roots_fixed = True
for i in range(8):
    k = [0] * n
    k[3 + i] = 1
    if act_class(tuple(k)) != tuple(k):
        roots_fixed = False
assert roots_fixed, 'sigma moves a class of the E8(2) block'
print('  sigma fixes all 8 classes [a_i/2]: it acts only on the U(2) block')


def fixed_by_sigma(k):
    return act_class(k) == k


nontrivial = [k for k in parity if not fixed_by_sigma(k)]
print('  sigma moves %d of the 2048 classes, so rho(sigma) != 1 and sigma is not in Gamma_Co'
      % len(nontrivial))
assert len(nontrivial) > 0

# ---------------------------------------------------------------- the U(2) block
block = [(0, 0), (1, 0), (0, 1), (1, 1)]        # coefficients of (e', f')
elems = []
for a, c in block:
    vec = [Fraction(0)] * n
    vec[1] = Fraction(a, 2)
    vec[2] = Fraction(c, 2)
    elems.append(vec)
pair = [[b(x, y) for y in elems] for x in elems]
quad = [b(x, x) / 2 for x in elems]


def isometry(p):
    return all(pair[i][j] == pair[p[i]][p[j]] for i in range(4) for j in range(4)) and \
           all(quad[i] == quad[p[i]] for i in range(4))


isons = [p for p in permutations(range(4)) if isometry(p)]
swap = (0, 2, 1, 3)                              # 0 -> 0, e' <-> f', e'+f' fixed
assert swap in isons
print('  A_{U(2)}: b and q are %s and %s' % (pair, quad))
print('  isometry group of the four-element space A_{U(2)}: %d elements, {id, swap}; '
      'the swap is in it' % len(isons))
assert len(isons) == 2, 'O(q_{U(2)}) is not of order 2'

print('')
print('CONCLUSION')
print('  sigma in Orth^+(T_Co) cap rho^{-1}(O(q_{U(2)}) x O(q_{E8(2)})) with rho(sigma) != 1,')
print('  i.e. an integral isometry realising the swap, so Gamma_Co = Orth^+(T_Co) cap ker(rho) is a')
print('  proper subgroup of the congruence preimage rho^{-1}(P) and [rho^{-1}(P) : Gamma_Co] >= 2.')
print('  Not claimed: strictness for the Heegner group Gamma^Hdg, which no element here witnesses.')
print('OK: the congruence group strictly contains the stable group, by an exhibited integral isometry')
