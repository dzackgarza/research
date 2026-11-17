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
from math import gcd, prod
from collections import deque
import json
from pathlib import Path
from sage.all import (ZZ, GF, CartanMatrix, PermutationGroup, block_diagonal_matrix,
                      diagonal_matrix, identity_matrix, matrix, vector)

SIGNS = (1, 1) + (-1,) * 9
B = diagonal_matrix(ZZ, SIGNS)
# Rows of a unimodular change of basis from the standard
# <1> + U + E8(-1) presentation of T_Co(1/2) to diagonal I_{2,9}.
# The first row is the characteristic norm-one vector, the next two
# span U, and the remaining eight are an E8(-1) simple-root basis.
M = matrix(ZZ, [
    [3,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0],
    [-3,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1],
    [0,0,0,0,0,1,-1,0,0,0,0],
    [3,1,1,1,1,1,1,1,2,1,1],
    [-2,-1,-1,-1,-1,-1,0,-1,-1,0,-1],
    [2,1,1,1,1,1,1,1,0,0,1],
    [-1,0,0,0,0,-1,-1,-1,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,-1],
    [0,0,0,0,-1,0,0,0,0,0,1],
])
B_STANDARD = block_diagonal_matrix(matrix(ZZ, [[1]]),
                                   matrix(ZZ, [[0, 1], [1, 0]]),
                                   -CartanMatrix(['E', 8]))
assert abs(M.det()) == 1 and M * B * M.transpose() == B_STANDARD
TO_STANDARD = matrix(ZZ, M.transpose().inverse())
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
root_permutations = {}

for x in NONSINGULAR:
    r = root_lift(x)
    n = norm(r)
    # The root reflection s_r(y) = y - 2(y,r)/n * r.
    reflection = identity_matrix(ZZ, 11) - (2 // n) * (r.column() * (r.row() * B))
    assert reflection.transpose() * B * reflection == B
    assert reflection.det() == -1
    # An explicit integral root and reflection in the actual T_Co basis.
    standard_root = TO_STANDARD * r
    standard_reflection = TO_STANDARD * reflection * M.transpose()
    assert standard_root in ZZ**11 and standard_root * B_STANDARD * standard_root == n
    assert standard_reflection.base_ring() == ZZ
    assert standard_reflection.transpose() * B_STANDARD * standard_reflection == B_STANDARD
    # Its mod-two action is the nonsingular symmetry y -> y+(y,x)x.
    for i in range(11):
        e = vector(ZZ, [int(i == j) for j in range(11)])
        image = reflection * e
        image_mask = sum((int(image[j]) & 1) << j for j in range(11))
        assert image_mask == (1 << i) ^ (x if (x & (1 << i)) else 0)
    permutation = [
        positions[y ^ (x if PARITY(y & x) else 0)] for y in SINGULAR
    ]
    permutations.append(permutation)
    root_permutations[x] = permutation

G = PermutationGroup(permutations)
order = int(G.order())
expected = 2 * 2**20 * (2**5 - 1) * prod(2**(2*i) - 1 for i in range(1, 5))
assert order == expected == 46998591897600
# A deterministic ten-reflection certificate is enough for the *full*
# finite image, avoiding the 496-generator branching factor when carrying
# finite plane and flag classes. Each mask has its integral root lift above.
TEN_ROOTS = (1836, 269, 54, 418, 354, 390, 649, 562, 650, 957)
assert all(x in root_permutations for x in TEN_ROOTS)
assert int(PermutationGroup([root_permutations[x] for x in TEN_ROOTS]).order()) == expected
# For u=e_0+e_2, every nonsingular class orthogonal to u admits a
# norm +/-2 integral lift r with (r,u)=0, not merely (r,u)=0 mod 2.
# Hence its reflection fixes the primitive isotropic vector u exactly.
PARABOLIC_U = vector(ZZ, [1, 0, 1] + [0] * 8)
assert norm(PARABOLIC_U) == 0
parabolic_masks = tuple(x for x in NONSINGULAR if not PARITY(x & 5))
parabolic_roots = []
for x in parabolic_masks:
    r = list(bits(x))
    assert r[0] == r[2]
    if norm(r) == -6:
        r[1] = 2 if r[1] == 0 else 3
    root = vector(ZZ, r)
    assert norm(root) in (-2, 2) and root * B * PARABOLIC_U == 0
    assert all((int(a) & 1) == b for a, b in zip(root, bits(x)))
    parabolic_roots.append(root)
parabolic_image_order = int(PermutationGroup(
    [root_permutations[x] for x in parabolic_masks]
).order())
assert parabolic_image_order == expected // len(SINGULAR)
TEN_STANDARD_ROOTS = tuple(tuple(map(int, TO_STANDARD * root_lift(x))) for x in TEN_ROOTS)
assert len(set(TEN_STANDARD_ROOTS)) == 10
for coordinates in TEN_STANDARD_ROOTS:
    root = vector(ZZ, coordinates)
    n = int(root * B_STANDARD * root)
    assert abs(n) == 2
    s = identity_matrix(ZZ, 11) - (2 // n) * (
        root.column() * (root.row() * B_STANDARD)
    )
    assert s.transpose() * B_STANDARD * s == B_STANDARD and s.det() == -1

# Construct integral words carrying one singular discriminant class to
# every other one. This is a 527-vertex orbit traversal, not enumeration
# of the 46-trillion-element orthogonal group or its cosets.
base_integral = PARABOLIC_U
assert norm(base_integral) == 0 and gcd(*map(int, base_integral)) == 1
base_singular = sum((int(t) & 1) << i for i, t in enumerate(base_integral))
assert base_singular in SINGULAR
parent = {base_singular: None}
integral_vectors = {base_singular: base_integral}
queue = deque([base_singular])
while queue:
    y = queue.popleft()
    for i, x in enumerate(TEN_ROOTS):
        z = y ^ (x if PARITY(y & x) else 0)
        if z not in parent:
            parent[z] = (y, i)
            r = root_lift(x)
            n = norm(r)
            v = integral_vectors[y]
            integral_vectors[z] = v - (2 // n) * (v * B * r) * r
            queue.append(z)
assert set(parent) == set(SINGULAR)
assert all(norm(v) == 0 and gcd(*map(int, v)) == 1 and
           sum((int(t) & 1) << i for i, t in enumerate(v)) == y
           for y, v in integral_vectors.items())
target_singular = SINGULAR[-1]
path = []
y = target_singular
while y != base_singular:
    previous, i = parent[y]
    path.append(i)
    y = previous
path.reverse()
lift = identity_matrix(ZZ, 11)
for i in path:
    root = vector(ZZ, TEN_STANDARD_ROOTS[i])
    n = int(root * B_STANDARD * root)
    lift = (identity_matrix(ZZ, 11) - (2 // n) *
            (root.column() * (root.row() * B_STANDARD))) * lift
assert lift.transpose() * B_STANDARD * lift == B_STANDARD
base_vector = TO_STANDARD * base_integral
target_vector = TO_STANDARD * integral_vectors[target_singular]
assert lift * base_vector == target_vector
assert base_vector * B_STANDARD * base_vector == 0
assert target_vector * B_STANDARD * target_vector == 0
print('B=I_{2,9}: 496 integral norm +/-2 root reflections constructed and checked')
print('unimodular change to <1> + U + E8(-1): determinant', M.det())
print('all 496 integral reflection matrices verified in the standard T_Co basis')
print('finite even-norm discriminant space: 527 nonzero singular, 496 nonsingular')
print('faithful finite permutation image order:', order)
print('full O^+(10,2) order:', expected)
print('ten integral root reflections generate the full finite image:', TEN_ROOTS)
print('exact-vector stabilizer integral root image order:', parabolic_image_order)
print('integral norm-two vector-stabilizer roots:', len(parabolic_roots))
print('ten standard-basis integral roots:', TEN_STANDARD_ROOTS)
print('singular discriminant classes reached by integral root words:', len(parent))
print('primitive integral isotropic vector representatives certified:', len(integral_vectors))
print('sample integral transporter word (zero-based generator indices):', tuple(path))

# Persist the complete finite-to-integral vector section, rather than only its
# cardinality. All vectors are in the standard <1>+U+E8(-1) basis.
rows = []
for mask in sorted(integral_vectors):
    word = []
    y = mask
    while y != base_singular:
        y, i = parent[y]
        word.append(i)
    rows.append({
        'mask_diagonal': mask,
        'vector_standard': list(map(int, TO_STANDARD * integral_vectors[mask])),
        'word_from_base': list(reversed(word)),
    })
certificate = {
    'standard_gram': [list(map(int, row)) for row in B_STANDARD.rows()],
    'standard_to_diagonal': [list(map(int, row)) for row in M.transpose().rows()],
    'base_mask_diagonal': base_singular,
    'generator_roots_standard': [list(root) for root in TEN_STANDARD_ROOTS],
    'vector_stabilizer_roots_standard': [
        list(map(int, TO_STANDARD * root)) for root in parabolic_roots
    ],
    'vector_stabilizer_finite_order': parabolic_image_order,
    'representatives': rows,
}
output = Path('computations/reports/coble_singular_integral_representatives.json')
output.write_text(json.dumps(certificate, indent=2) + '\n')
assert len(rows) == 527 and len({r['mask_diagonal'] for r in rows}) == 527
print('published exact integral representatives:', output)
