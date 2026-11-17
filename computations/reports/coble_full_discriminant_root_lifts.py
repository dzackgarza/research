"""Construct a complete integral reflection lift of O(q_{T_Co}).

The odd unimodular lattice B=T_Co(1/2) is isometric to I_{2,9}.
Use diagonal coordinates B=diag(1,1,-1,...,-1), nine minus signs.
Its even-norm subspace V in B/2B is 10-dimensional, and
q(x)=B(x,x)/2 mod 2 is a plus-type quadratic form on V.

Every nonsingular class in V has an explicit integral norm +/-2 lift.
The 496 integral root reflections induce all 496 nonsingular
symmetries on V. Their exact permutation action on the 527 nonzero
singular vectors is faithful and has order |O^+(10,2)|.

Run with Sage:
    sage -c 'exec(compile(open("computations/reports/coble_full_discriminant_root_lifts.py").read(), "coble_full_discriminant_root_lifts.py", "exec"))'
"""
from math import prod
from sage.all import ZZ, GF, PermutationGroup, diagonal_matrix, identity_matrix, matrix, vector

SIGNS = (1, 1) + (-1,) * 9
B = diagonal_matrix(ZZ, SIGNS)
PARITY = lambda n: n.bit_count() & 1
V = tuple(x for x in range(1 << 11) if not PARITY(x))


def bits(x):
    return tuple((x >> i) & 1 for i in range(11))


def norm(x):
    return sum(s * int(a)**2 for s, a in zip(SIGNS, x))


def q(x):
    return (norm(bits(x)) // 2) % 2


def root_lift(x):
    """A norm +/-2 root in the exact parity class x, for q(x)=1."""
    assert x in V and q(x) == 1
    v = list(bits(x))
    if norm(v) == -6:
        if 0 in v[:2]:
            v[v[:2].index(0)] = 2  # add 4 to the norm
        else:
            v[0] = 3  # add 8 to the norm
    assert norm(v) in (-2, 2) and all((a & 1) == b for a, b in zip(v, bits(x)))
    return vector(ZZ, v)


SINGULAR = tuple(x for x in V if x and q(x) == 0)
NONSINGULAR = tuple(x for x in V if q(x) == 1)
assert len(V) == 1024 and len(SINGULAR) == 527 and len(NONSINGULAR) == 496
assert matrix(GF(2), [bits(x) for x in SINGULAR]).rank() == 10
positions = {x: i + 1 for i, x in enumerate(SINGULAR)}
permutations = []

for x in NONSINGULAR:
    r = root_lift(x)
    n = norm(r)
    # The root reflection s_r(y) = y - 2(y,r)/n * r.
    reflection = identity_matrix(ZZ, 11) - (2 // n) * (r.column() * (r.row() * B))
    assert reflection.transpose() * B * reflection == B
    assert reflection.det() == -1
    # Its mod-two action is the nonsingular symmetry y -> y+(y,x)x.
    for i in range(11):
        e = vector(ZZ, [int(i == j) for j in range(11)])
        image = reflection * e
        image_mask = sum((int(image[j]) & 1) << j for j in range(11))
        assert image_mask == (1 << i) ^ (x if (x & (1 << i)) else 0)
    permutations.append([
        positions[y ^ (x if PARITY(y & x) else 0)] for y in SINGULAR
    ])

G = PermutationGroup(permutations)
order = int(G.order())
expected = 2 * 2**20 * (2**5 - 1) * prod(2**(2*i) - 1 for i in range(1, 5))
assert order == expected == 46998591897600
print('B=I_{2,9}: 496 integral norm +/-2 root reflections constructed and checked')
print('finite even-norm discriminant space: 527 nonzero singular, 496 nonsingular')
print('faithful finite permutation image order:', order)
print('full O^+(10,2) order:', expected)
