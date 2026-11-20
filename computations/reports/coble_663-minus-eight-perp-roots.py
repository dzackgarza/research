"""research#663: does u^perp contain a (-2)-vector, and does that decide the dichotomy?  No.

@rmk:divisibility-of-the-difference-class leaves two cases: Pic = S_Co,b + <u> of determinant 2^14, or
an index-two overlattice of it of determinant 2^12.  The tempting argument for excluding the second is
that u^perp would then be entirely transcendental, and u^perp -- rank 10 and signature (2,8) -- seems
to contain vectors of square -2, which would then be algebraic in T_Co and contradict @prob:B24.

This script checks the first half (that u^perp does contain (-2)-vectors, for sampled classes of u of
square -8) and the record states why the argument fails anyway: in the second case such a vector is
transcendental, which is exactly what @prob:B24 permits.  The dichotomy is therefore NOT decided by
B24, and this file exists so that the route is not tried again.

Usage: python3 computations/reports/coble_663-minus-eight-perp-roots.py
"""
import random
from math import gcd

C = [[2, -1, 0, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0, 0], [0, -1, 2, -1, 0, 0, 0, -1],
     [0, 0, -1, 2, -1, 0, 0, 0], [0, 0, 0, -1, 2, -1, 0, 0], [0, 0, 0, 0, -1, 2, -1, 0],
     [0, 0, 0, 0, 0, -1, 2, 0], [0, 0, 0, -1, 0, 0, 0, 2]]
GT = [[0] * 11 for _ in range(11)]
GT[0][0] = 2
GT[1][2] = GT[2][1] = 2
for i in range(8):
    for j in range(8):
        GT[3 + i][3 + j] = -2 * C[i][j]

def q(v):
    return sum(v[i] * GT[i][j] * v[j] for i in range(11) for j in range(11))
def dot(v, w):
    return sum(v[i] * GT[i][j] * w[j] for i in range(11) for j in range(11))

random.seed(663)
us = []
while len(us) < 6:
    v = [random.randint(-3, 3) for _ in range(11)]
    if q(v) != -8:
        continue
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    if g != 1:
        continue
    if any(all(v[i] == u[i] for i in range(11)) or all(v[i] == -u[i] for i in range(11)) for u in us):
        continue
    us.append(v)

print("T_Co of determinant", -2048, "; sampled primitive vectors of square -8:", len(us))
hits = 0
for u in us:
    w = None
    for _ in range(200000):
        c = [random.randint(-2, 2) for _ in range(11)]
        if q(c) == -2 and dot(c, u) == 0:
            w = c
            break
    hits += w is not None
    print("  u =", u, "| perpendicular (-2)-vector:", w)
print("classes admitting one:", hits, "of", len(us))
print()
print("What this does NOT show: that the second case is excluded.  There, u^perp is the TRANSCENDENTAL")
print("lattice, so a (-2)-vector inside it is transcendental, not algebraic, and @prob:B24 -- which")
print("forbids only algebraic classes of square -2 in T_Co -- is satisfied.  The dichotomy stands open.")
