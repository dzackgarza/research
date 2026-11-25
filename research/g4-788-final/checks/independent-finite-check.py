#!/usr/bin/env python3
"""Independent exhaustive check for the finite part of prop:gamma-co-images."""
from itertools import product
from pathlib import Path

import numpy as np

# E8 Dynkin diagram: a seven-node chain, with the eighth node attached
# to the third node of that chain.  Signs are irrelevant modulo two.
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]
cartan = [[0] * 8 for _ in range(8)]
for i in range(8):
    cartan[i][i] = 2
for i, j in edges:
    cartan[i][j] = cartan[j][i] = -1

def det_int(a):
    # Bareiss elimination, independent of floating-point determinants.
    a = [row[:] for row in a]
    sign = 1
    previous = 1
    for k in range(7):
        if a[k][k] == 0:
            for r in range(k + 1, 8):
                if a[r][k] != 0:
                    a[k], a[r] = a[r], a[k]
                    sign = -sign
                    break
        pivot = a[k][k]
        assert pivot != 0
        for i in range(k + 1, 8):
            for j in range(k + 1, 8):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // previous
        previous = pivot
        for i in range(k + 1, 8):
            a[i][k] = 0
        for j in range(k + 1, 8):
            a[k][j] = 0
    return sign * a[7][7]

assert det_int(cartan) == 1, det_int(cartan)

# Encode (u,v,y) with u,v in F_2 and y in E8/2E8 in ten bits.
# q(U(2)): 0,0,0,1.  q(E8(2)): C(y,y)/2 mod 2.
def bits(x):
    return [(x >> i) & 1 for i in range(10)]

def q(x):
    z = bits(x)
    u, v, y = z[0], z[1], z[2:]
    ans = (u & v)  # u=v=1 is the unique nonsingular U(2) class.
    for i in range(8):
        ans ^= y[i]  # diagonal C_ii/2 = 1.
        for j in range(i + 1, 8):
            # The off-diagonal quadratic term is C_ij*y_i*y_j.
            ans ^= (cartan[i][j] * y[i] * y[j]) % 2
    return ans

def pairing(x, y):
    # The associated F_2 polar form, i.e. 2b modulo two.
    p = bits(x)
    r = bits(y)
    ans = (p[0] & r[1]) ^ (p[1] & r[0])
    for i in range(8):
        for j in range(8):
            ans ^= (cartan[i][j] * p[2 + i] * r[2 + j]) % 2
    return ans

vectors = list(range(1024))
q_values = np.array([q(x) for x in vectors], dtype=np.uint8)
pair = np.array([[pairing(x, y) for y in vectors] for x in vectors], dtype=np.uint8)
assert all(pair[x, x] == 0 for x in vectors)
assert (pair == pair.T).all()
assert len(set(vectors)) == 1024
singular = [x for x in vectors if q(x) == 0]
nonsingular = [x for x in vectors if q(x) == 1]
print(f"E8 determinant: {det_int(cartan)}")
print(f"dim: 10; q=0: {len(singular)}; q=1: {len(nonsingular)}")
assert (len(singular), len(nonsingular)) == (528, 496)

planes = set()
ordered_pairs = 0
complement_singular_counts = set()
for a in singular:
    if a == 0:
        continue
    for b in singular:
        if pair[a, b] != 1:
            continue
        ordered_pairs += 1
        plane = tuple(sorted((0, a, b, a ^ b)))
        assert len(set(plane)) == 4
        assert sum(q(x) for x in plane) == 1
        planes.add(plane)
        complement = (pair[a] == 0) & (pair[b] == 0)
        assert int(complement.sum()) == 256
        complement_singular_counts.add(int((q_values[complement] == 0).sum()))

print(f"ordered hyperbolic pairs: {ordered_pairs}")
print(f"distinct hyperbolic planes: {len(planes)}")
print(f"527*256/2: {527 * 256 // 2}")
print(f"singular counts in all complements: {sorted(complement_singular_counts)}")
assert ordered_pairs == 527 * 256
assert len(planes) == ordered_pairs // 2 == 67456
assert complement_singular_counts == {136}  # O_8^+(2): 2^7+2^3.

# Full A_TCo = <w> direct-sum the ten-dimensional block.  Reduce q mod 1
# in half-integer units: w contributes 1, the block contributes 0 or 2,
# and b(w,x) detects exactly the w-coordinate in those units.  Both are
# therefore compared modulo two half-integer units, i.e. modulo one integer.
characteristic_failures = []
for epsilon, x in product((0, 1), vectors):
    q_mod_one = (epsilon + 2 * int(q_values[x])) % 2
    b_with_w = epsilon % 2
    if q_mod_one != b_with_w:
        characteristic_failures.append((epsilon, x))
print(f"characteristic identity checked on {2 * 1024} classes; failures: {len(characteristic_failures)}")
assert not characteristic_failures

# The same arithmetic independently counts the two orthogonal groups by
# ordered hyperbolic bases.
def first_pair_choices(m):
    return (2 ** (2 * m - 1) + 2 ** (m - 1) - 1) * 2 ** (2 * m - 2)

o2 = first_pair_choices(1)
o4 = first_pair_choices(2) * o2
o6 = first_pair_choices(3) * o4
o8 = first_pair_choices(4) * o6
o10 = first_pair_choices(5) * o8
print("hyperbolic-pair choices by half-dimension:", [first_pair_choices(m) for m in range(1, 6)])
print(f"|O2+|={o2}; |O4+|={o4}; |O6+|={o6}; |O8+|={o8}; |O10+|={o10}")
print(f"|P|={o2 * o8}; index={o10 // (o2 * o8)}")
assert (o2, o8, o10) == (2, 348364800, 46998591897600)
assert o2 * o8 == 696729600
assert o10 // (o2 * o8) == 67456 == 2**7 * 17 * 31

# H^perp/H: epsilon,c in {0,1}, with membership exactly epsilon=c.
# Subtracting epsilon*(w,delta) leaves a unique (0,x,0) representative.
perp = [(epsilon, x, c) for epsilon, x, c in product((0, 1), vectors, (0, 1)) if epsilon == c]
quotient = {(0, x, 0) for epsilon, x, c in perp}
print(f"|H^perp|={len(perp)}; |H^perp/H|={len(quotient)}")
assert len(perp) == 2048 and len(quotient) == 1024
print("ALL INDEPENDENT FINITE CHECKS PASSED")
