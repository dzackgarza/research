"""Primitive totally isotropic planes in T' = U(1) + U(2), and the size of Pi^*/Pi.

Pi* = {z in span_Q(Pi): (z, T') inside Z} = the elements of the Q-span pairing integrally.
With B the 2 x 4 basis matrix and G the Gram matrix, M = B G, and
  Pi*/Pi  =  (row space of B G in Z^4) saturated / (row space of B G),
whose order is the product of the two Smith-invariant factors d1*d2.  Pi primitive in T' means
the same product computed for B itself is 1.  So one function answers both questions.
"""
import math
from itertools import combinations, product

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def saturation_index(B):
    """Order of R_sat / R for the row lattice R of the 2 x 4 integer matrix B."""
    D = smith_normal_form(Matrix(B), domain=ZZ)
    return abs(D[0, 0] * D[1, 1])


G = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 2], [0, 0, 2, 0]]


def dot(x, y):
    a, b, c, d = x
    a2, b2, c2, d2 = y
    return a * b2 + b * a2 + 2 * c * d2 + 2 * d * c2


def qform(x):
    return dot(x, x)


LIMIT = 3
vectors = []
for a, b, c, d in product(range(-LIMIT, LIMIT + 1), repeat=4):
    if (a, b, c, d) == (0, 0, 0, 0):
        continue
    if math.gcd(math.gcd(a, b), math.gcd(c, d)) != 1:
        continue
    if qform((a, b, c, d)) == 0:
        vectors.append((a, b, c, d))

print('isotropic primitive vectors in the box: %d' % len(vectors))
found = {1: [], 2: [], 4: []}
others = {}
checked = 0
for x, y in combinations(vectors, 2):
    if dot(x, y) != 0:
        continue
    checked += 1
    B = [list(x), list(y)]
    if saturation_index(B) != 1:
        continue  # not a primitive sublattice
    M = [[sum(r[k] * G[k][j] for k in range(4)) for j in range(4)] for r in B]
    idx = saturation_index(M)
    if idx in (1, 2, 4):
        found[idx].append((x, y))
    else:
        others[idx] = others.get(idx, 0) + 1

print('primitive planes checked: %d' % checked)
for idx in (1, 2, 4):
    print('  |Pi*/Pi| = %d : %d planes found' % (idx, len(found[idx])))
    for x, y in found[idx][:4]:
        print('      x = %s, y = %s' % (x, y))
if others:
    print('  other indices: %s' % others)
