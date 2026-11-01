"""The gluing subgroup cut out by the exhibited plane J = <v_1, v_2> of T_Co.

    python3 computations/reports/plane_gluing_subgroup.py

No Sage: the whole claim is integral linear algebra on the Gram matrix, done in Fractions, so the
certificate is independent of the maintained isotropic-quotient machinery that
`one_cusp_plane_quotient.py` exercises (that report supplies the *other* half of the plane data,
J^perp/J = I_{0,7}(2)).

T_Co = <2> + U(2) + E8(2), basis h; e', f'; a_1..a_8, exactly as in the manuscript and in
`one_cusp_plane_quotient.py` (which asserts div(v_1) = div(v_2) = 2 at the owner).  The plane is
v_1 = e', v_2 = 2h + a_1 + a_2.

What is checked:

  * J is totally isotropic and primitive, b(v_1,v_1) = b(v_1,v_2) = b(v_2,v_2) = 0;
  * div_{T_Co}(v_1) = div_{T_Co}(v_2) = 2, and every primitive vector of J has divisibility 2;
  * therefore (T_Co^vee cap J_Q)/J = (Z/2)^2, where T_Co^vee = {x in T_Co (x) Q : b(x,T_Co) <= Z};
    this is the subgroup of A_{T_Co} = T_Co^vee/T_Co cut out by J -- the plane's gluing datum;
  * its induced form is zero, i.e. the gluing is isotropic (as it must be, b being integral on T_Co);
  * |A_{T_Co}| = |det T_Co| = 2048, so the gluing subgroup is one of the order-4 isotropic subgroups.

Note what is *not* claimed: J^vee/J for the restricted form b|_J is infinite, since b|_J = 0 makes the
dual condition vacuous.  The finite invariant is the one above, cut out by J inside A_{T_Co}.
"""
from fractions import Fraction
from math import gcd
from functools import reduce

# E8 Cartan matrix from the Dynkin diagram: 1-3-4-5-6-7-8 with 2 attached to 3.
EDGES = [(1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
CARTAN = [[2 if i == j else 0 for j in range(1, 9)] for i in range(1, 9)]
for i, j in EDGES:
    CARTAN[i - 1][j - 1] = CARTAN[j - 1][i - 1] = -1

# GRAM = <2> perp U(2) perp E8(2); E8(2) = -2 * Cartan(E8) (negative definite, even).
n = 11
G = [[0] * n for _ in range(n)]
G[0][0] = 2                                    # <2>, h
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


def coord(v):
    """Coordinate vector of a lattice element given as {index: coefficient}."""
    c = [0] * n
    for i, k in v.items():
        c[i] += k
    return c


def b(c1, c2):
    return sum(c1[i] * G[i][j] * c2[j] for i in range(n) for j in range(n))


def pairing(c1, c2):
    """The entries of G c2 -- the values b(c1, .) on the ambient basis, which decide divisibility."""
    return [sum(G[i][j] * c2[j] for j in range(n)) for i in range(n)]


def divisibility(c):
    return reduce(gcd, (abs(x) for x in pairing([0] * n, c) if x != 0), 0)


DET = det_int(G)
print('T_Co: rank 11, even, |det| = %d' % abs(DET))
assert abs(DET) == 2048, 'this is not T_Co: |A_{T_Co}| should be 2048'

v1 = coord({1: 1})            # e'
v2 = coord({0: 2, 3: 1, 4: 1})  # 2h + a_1 + a_2

print('J = <v_1, v_2>, v_1 = e\', v_2 = 2h + a_1 + a_2')
print('  squares and product: v_1^2 = %d, v_1.v_2 = %d, v_2^2 = %d' % (b(v1, v1), b(v1, v2), b(v2, v2)))
assert (b(v1, v1), b(v1, v2), b(v2, v2)) == (0, 0, 0), 'the plane is not totally isotropic'
print('  divisibilities: div(v_1) = %d, div(v_2) = %d' % (divisibility(v1), divisibility(v2)))
assert (divisibility(v1), divisibility(v2)) == (2, 2)

# Every primitive vector of J has divisibility exactly 2: div(a v_1 + b v_2) is gcd of the two
# divisibility ideals scaled by a and b, so gcd(a,b) = 1 forces 2.  Checked on a range.
tested = 0
for a in range(-4, 5):
    for c in range(-4, 5):
        if gcd(abs(a), abs(c)) != 1:
            continue
        v = [a * v1[i] + c * v2[i] for i in range(n)]
        d = divisibility(v)
        assert d == 2, 'primitive %r v_1 + %r v_2 has divisibility %d' % (a, c, d)
        tested += 1
print('  all %d primitive vectors a v_1 + c v_2 with |a|, |c| <= 4 have divisibility 2' % tested)

# The lattice of (alpha, beta) with alpha v_1 + beta v_2 in T_Co^vee.
COL1 = pairing([0] * n, v1)
COL2 = pairing([0] * n, v2)


def in_dual(alpha, beta):
    """True iff alpha v_1 + beta v_2 pairs integrally with every basis vector of T_Co."""
    alpha, beta = Fraction(alpha), Fraction(beta)
    for i in range(n):
        if (alpha * COL1[i] + beta * COL2[i]).denominator != 1:
            return False
    return True


def dual_members(den):
    """The elements of T_Co^vee cap J_Q expressible with denominator den, as (alpha, beta) pairs."""
    out = []
    for p in range(-den, den + 1):
        for q in range(-den, den + 1):
            if in_dual(Fraction(p, den), Fraction(q, den)):
                out.append((Fraction(p, den) % 1, Fraction(q, den) % 1))
    return sorted(set(out))


assert in_dual(1, 0) and in_dual(0, 1), 'J is not contained in T_Co^vee'
print('  J <= T_Co^vee (b is integral on T_Co): confirmed')

HALF = dual_members(2)
QUARTER = dual_members(4)
print('  T_Co^vee cap (1/2)J, modulo J: %d elements %s' % (len(HALF), HALF))
print('  T_Co^vee cap (1/4)J, modulo J: %d elements %s' % (len(QUARTER), QUARTER))
assert len(HALF) == 4, 'expected the four half-integral classes'
assert set(HALF) == set(QUARTER), 'a quarter-integral class lies in the dual: index is not 4'
# Index 4 with every element of order 2 => (Z/2)^2, not Z/4.
assert all(2 * a % 1 == 0 and 2 * c % 1 == 0 for a, c in QUARTER)
print('the gluing subgroup (T_Co^vee cap J_Q)/J is (Z/2)^2, generated by v_1/2 and v_2/2, exponent 2')
print('  index [(T_Co^vee cap J_Q) : J] = %d, and |A_{T_Co}| = %d' % (len(QUARTER), abs(DET)))

# The induced form on the gluing subgroup, in Q/Z.
def class_pairing(a1, c1, a2, c2):
    """b(a1 v_1 + c1 v_2, a2 v_1 + c2 v_2) modulo 1, on half-integral classes."""
    va = [Fraction(a1) * v1[i] + Fraction(c1) * v2[i] for i in range(n)]
    vb = [Fraction(a2) * v1[i] + Fraction(c2) * v2[i] for i in range(n)]
    return b(va, vb) % 1


for p, q in QUARTER:
    for a, c in QUARTER:
        val = class_pairing(p, q, a, c)
        assert val == 0, 'gluing subgroup not isotropic at (%s, %s)-(%s, %s)' % (p, q, a, c)
print('the induced form on (Z/2)^2 is zero: the gluing is isotropic')

print('OK: J^perp/J = I_{0,7}(2) (one_cusp_plane_quotient.py) and the gluing subgroup'
      ' (Z/2)^2 <= A_{T_Co} are the plane\'s invariants')

# ---------------------------------------------------------------------------------------------------
# The other exhibited plane of the book: prop:tco-split-maximal takes T_Co = B(2) with
# B = U + U + I_{0,7} and J spanned by isotropic generators of the two hyperbolic summands, a plane in
# the presentation T_Co = U(2) + U(2) + A_1^7.  The two planes are different subspaces, but both are
# primitive isotropic planes of a lattice of signature (2,9), hence in one Orth^+ orbit by
# thm:plane-transitivity-tco; the gluing computed here is the check that the invariant agrees, and the
# reason it cannot be the thing that separates the two Gamma_Co orbits if they differ.
m = 11
G2 = [[0] * m for _ in range(m)]
for block in range(2):                          # U(2) + U(2)
    base = 2 * block
    G2[base][base + 1] = G2[base + 1][base] = 2
for k in range(7):                              # A_1^7 = I_{0,7}(2)
    G2[4 + k][4 + k] = -2
assert all(G2[i][j] == G2[j][i] for i in range(m) for j in range(m))
assert all(G2[i][i] % 2 == 0 for i in range(m))
assert abs(det_int(G2)) == 2048, 'the second presentation is not T_Co: |A| should be 2048'
print()
print('second presentation T_Co = U(2) + U(2) + A_1^7: rank 11, even, |det| = %d' % abs(det_int(G2)))


def pairing2(c):
    return [sum(G2[i][j] * c[j] for j in range(m)) for i in range(m)]


def divisibility2(c):
    return reduce(gcd, (abs(x) for x in pairing2(c) if x != 0), 0)


def b2(c1, c2):
    return sum(c1[i] * G2[i][j] * c2[j] for i in range(m) for j in range(m))


u1 = [1, 0] + [0] * 9   # isotropic generator of the first U(2)
u2 = [0, 0, 1, 0] + [0] * 7  # isotropic generator of the second U(2)
print('  J = <u_1, u_2>: squares %d, %d; product %d (isotropic)'
      % (b2(u1, u1), b2(u2, u2), b2(u1, u2)))
assert (b2(u1, u1), b2(u1, u2), b2(u2, u2)) == (0, 0, 0)
print('  divisibilities: div(u_1) = %d, div(u_2) = %d' % (divisibility2(u1), divisibility2(u2)))
assert (divisibility2(u1), divisibility2(u2)) == (2, 2)

COL1b, COL2b = pairing2(u1), pairing2(u2)


def in_dual2(alpha, beta):
    alpha, beta = Fraction(alpha), Fraction(beta)
    return all((alpha * COL1b[i] + beta * COL2b[i]).denominator == 1 for i in range(m))


members = sorted({(Fraction(p, 2) % 1, Fraction(q, 2) % 1)
                  for p in range(-2, 3) for q in range(-2, 3) if in_dual2(Fraction(p, 2), Fraction(q, 2))})
quarter = sorted({(Fraction(p, 4) % 1, Fraction(q, 4) % 1)
                  for p in range(-4, 5) for q in range(-4, 5) if in_dual2(Fraction(p, 4), Fraction(q, 4))})
print('  T_Co^vee cap (1/2)J, modulo J: %d elements; at (1/4): %d' % (len(members), len(quarter)))
assert len(members) == 4 and set(members) == set(quarter)
for p, q in quarter:
    for a, c in quarter:
        val = b2([Fraction(p) * u1[i] + Fraction(q) * u2[i] for i in range(m)],
                 [Fraction(a) * u1[i] + Fraction(c) * u2[i] for i in range(m)]) % 1
        assert val == 0, 'the second plane\'s gluing is not isotropic'
print('  the gluing subgroup is again (Z/2)^2 with zero pairing')
print('both planes exhibited in the book cut out (Z/2)^2 <= A_{T_Co}, each in the presentation the book')
print('  uses for it; so the invariant agrees on the two, and by thm:plane-transitivity-tco it must,')
print('  they being one Orth^+ orbit.  What it could separate is Gamma_Co-orbits, and for these two')
print('  planes it cannot witness a difference even if their Gamma_Co-orbits are distinct.')

