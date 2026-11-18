"""research#663: the level set of A_{T_Co} and the orbits of P on it, exactly.

A20/#720 (D1) asks that the family's discriminant meet every Gamma^dir-orbit of walls.  Its
(-2) half is a corollary of the period image (the page, cor:d1-minus-two-half).  Its (-4) half is a
statement about the 496 classes of {q_{T_Co} = 1} in A_{T_Co}: whether the 121 classes the gluing
carries there meet every orbit.  This script does two things and nothing else.

1. It rebuilds (A_{T_Co}, q) from the Gram matrix of T_Co = <2> + U(2) + E8(2) and reproduces the
   level counts of coble_671-discriminant-levels (528, 528, 496, 496), which is a check on the
   lattice and on the normalization at once.
2. It computes the orbits of P = (the involution swapping the two isotropic generators of U(2)) x
   (the orthogonal transvections of the E8(2) block) on the level set: 4 orbits, of sizes
   240, 135, 120, 1.

The group generated here is contained in the P of prop:direct-eq-heegner (it fixes [h/2], and it
acts by orthogonal transvections on the E8(2) block), so its orbits refine P's; the orbit count it
prints is therefore an upper bound for P's, and the subset sum printed at the end is a check of
consistency, not the argument.  The argument of thm:d1-minus-four-half is only that 121 < 496 and
that the 121 classes are stable under P.

Usage: python3 computations/reports/coble_663-d1-level-orbits.py
"""
from fractions import Fraction
from collections import deque, Counter
from itertools import combinations
import sympy

# --- the lattice -------------------------------------------------------------------------------
# E8 Dynkin diagram: arms of lengths 2, 4 and 1 from the branch node (so E8, not the affine diagram)
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]
C = sympy.zeros(8)
for i in range(8):
    C[i, i] = 2
for i, j in edges:
    C[i, j] = C[j, i] = -1
M = sympy.zeros(11)
M[0, 0] = 2                        # <h>, h^2 = 2
M[1, 2] = M[2, 1] = 2              # U(2)
M[3:11, 3:11] = -2 * C             # E8(2) = 2 E8(-1), negative definite
G = [[int(M[i, j]) for j in range(11)] for i in range(11)]

n = 11
def bits(x):
    return tuple((x >> i) & 1 for i in range(n))
def idx(t):
    v = 0
    for i in range(n):
        v |= (t[i] & 1) << i
    return v

print("T_Co: rank 11, det =", M.det(), "(want -2048)")
print("       diagonal blocks: <2> gives +1, U(2) gives (1,1), E8(2) = 2 E8(-1) gives (0,8);")
print("       so signature (2,9) and det 2 * (-4) * 2^8 = -2048")

# --- A = T/2T and q(t) = t^T G t / 4 mod 2Z -----------------------------------------------------
Q = [None] * 2048
for x in range(2048):
    t = bits(x)
    s = sum(t[i] * G[i][j] * t[j] for i in range(n) for j in range(n))
    q = Fraction(s, 4)
    Q[x] = q - 2 * (q // 2)
hist = Counter(Q)
print("q histogram mod 2Z:", {str(k): hist[k] for k in sorted(hist)})
assert hist[Fraction(0)] == 528 and hist[Fraction(1, 2)] == 528
assert hist[Fraction(1)] == 496 and hist[Fraction(3, 2)] == 496
level = [x for x in range(2048) if Q[x] == Fraction(1)]
print("level set {q = 1}:", len(level), "classes")

# --- P: the swap on the U(2) block, and the orthogonal transvections of the E8(2) block ---------
def beta(x, y):
    t, u = bits(x), bits(y)
    s = sum(t[i] * G[i][j] * u[j] for i in range(n) for j in range(n))
    return (s // 2) % 2          # 2 b(x,y) mod 2

def swapU(y):
    t = list(bits(y))
    t[1], t[2] = t[2], t[1]
    return idx(t)

def transvection(e):
    eb = bits(e)
    def f(y):
        t = list(bits(y))
        if beta(y, e):
            for i in range(3, 11):
                t[i] ^= eb[i]
        return idx(t)
    return f

def is_isometry(f):
    if len({f(x) for x in range(2048)}) != 2048:
        return False
    return all(Q[f(x)] == Q[x] for x in range(2048))

gens = [("swap", swapU)]
assert is_isometry(swapU)
kept = 0
for e in [x for x in range(2048) if (x >> 3) != 0 and (x & 7) == 0]:
    f = transvection(e)
    if is_isometry(f):
        gens.append(("tau", f)); kept += 1
print("generators: the swap plus", kept, "orthogonal transvections of the E8(2) block")

# --- orbits on the level set --------------------------------------------------------------------
pts = set(level); seen = set(); orbits = []
for p in sorted(pts):
    if p in seen:
        continue
    comp = []; dq = deque([p]); seen.add(p)
    while dq:
        y = dq.popleft(); comp.append(y)
        for _, g in gens:
            z = g(y)
            if z in pts and z not in seen:
                seen.add(z); dq.append(z)
    orbits.append(comp)
print("orbits on the level set:", len(orbits), "sizes:", sorted((len(o) for o in orbits), reverse=True))

sizes = sorted((len(o) for o in orbits), reverse=True)
subs = [s for r in range(1, len(sizes) + 1) for s in combinations(sizes, r) if sum(s) == 121]
print("subsets of those sizes summing to 121:", subs)
print()
print("For (D1): 121 < 496, and the 121 classes are the image under the gluing of the level set of")
print("q_{S_Co} that carries a vector of square -4, so they are stable under P.  A stable subset of")
print("a finite set with a stable complement leaves orbits of the complement untouched, and the")
print("walls of such an orbit are met by the image: (D1)'s (-4) half fails on 496 - 121 = 375 classes.")
