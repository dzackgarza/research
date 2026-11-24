"""#761, the plane half of the discriminant action of the full integral plane stabilizer.

    sage computations/reports/coble_plane-half-f2.py
    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_plane-half-f2.py

T_Co = B(2) with B = U_1 + U_2 + I_{0,7} unimodular, so A_{T_Co} = B/2B, q([x/2]) = (x,x)_B/2 mod 2,
and the discriminant action of g in O(B) = O(T_Co) is the reduction of g modulo 2 on B/2B
(thm:coble-plane-stabilizer-image).  The integral matrices are written out here and not asked of a
library: the thirty generators of Stab_{O(B)}(P_0) are the complete family of thm:o2-plane-family,
and the twenty-one of O(B) are the complete family of thm:coble-ambient-21-generators, read from the
source-hashed JSON beside this file.  Each of them is checked in the record: exact Gram identity,
integral action on P_0, the even-norm parameters and the central shear of the unipotent half.

Every printed line is a value of the groups: the finite orders are Schreier-Sims orders of the
faithful permutation action on the 2047 nonzero classes of A, the representation of #834/#835
(computations/reports/coble_834_835_orbit_fibres.py).  Nothing printed is a timing, the size of a
library's generating set, or a probe of a library call, and no order is imposed as an expected
value: the integer arithmetic and the permutation groups decide them.
"""
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

from sage.all import libgap

sys.stdout.reconfigure(line_buffering=True)

# B = U_1 + U_2 + I_{0,7} in the basis (e_1, f_1, e_2, f_2, d_1, ..., d_7), and the exact integer
# helpers of computations/reports/coble_834_835_orbit_fibres.py.
N = 11
I = [[int(i == j) for j in range(N)] for i in range(N)]
GRAM = [[0] * N for _ in range(N)]
GRAM[0][1] = GRAM[1][0] = GRAM[2][3] = GRAM[3][2] = 1
for i in range(4, N):
    GRAM[i][i] = -1


def tr(M):
    return list(map(list, zip(*M)))


def mul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def inv(A):
    return mul(mul(GRAM, tr(A)), GRAM)


def mv(M, x):
    return [sum(a * b for a, b in zip(r, x)) for r in M]


def dot(x, y):
    return sum(a * b for a, b in zip(x, mv(GRAM, y)))


def unit(i):
    return I[i][:]


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def iso(M):
    return mul(mul(tr(M), GRAM), M) == GRAM and mul(M, inv(M)) == I


def trans(v, k):
    """The Eichler transvection E_{v,k}; integral exactly when k has even norm (B is odd)."""
    assert dot(v, v) == dot(v, k) == 0 and dot(k, k) % 2 == 0
    return tr([[a - dot(x, k) * b + dot(x, v) * c - dot(k, k) // 2 * dot(x, v) * b
                for a, b, c in zip(x, v, k)] for x in I])


def determinant(M):
    M = [[Fraction(x) for x in row] for row in M]
    value = Fraction(1)
    for c in range(len(M)):
        pivot_row = next(r for r in range(c, len(M)) if M[r][c])
        if pivot_row != c:
            M[c], M[pivot_row] = M[pivot_row], M[c]
            value = -value
        value *= M[c][c]
        for r in range(c + 1, len(M)):
            factor = M[r][c] / M[c][c]
            for k in range(c, len(M)):
                M[r][k] -= factor * M[c][k]
    return int(value)


def signature(M):
    """The inertia of a symmetric integer matrix, by exact symmetric elimination.

    A zero diagonal entry whose column is nonzero is handled by the 2x2 block
    [[0, m], [m, x]], of determinant -m^2 < 0, which contributes (1, 1).
    """
    M = [[Fraction(x) for x in row] for row in M]
    n = len(M)
    pos = neg = 0
    c = 0
    while c < n:
        if M[c][c] != 0:
            pivot = M[c][c]
            pos, neg = (pos + 1, neg) if pivot > 0 else (pos, neg + 1)
            for r in range(c + 1, n):
                factor = M[r][c] / pivot
                for k in range(c, n):
                    M[r][k] -= factor * M[c][k]
            c += 1
            continue
        r = next((r for r in range(c + 1, n) if M[r][c]), None)
        if r is None:
            c += 1
            continue
        if r != c + 1:
            M[c + 1], M[r] = M[r], M[c + 1]
            for row in M:
                row[c + 1], row[r] = row[r], row[c + 1]
        m, x = M[c][c + 1], M[c + 1][c + 1]
        pos, neg = pos + 1, neg + 1
        inverse = [[-x / (m * m), 1 / m], [1 / m, Fraction(0)]]
        for i in range(c + 2, n):
            left = [M[i][c], M[i][c + 1]]
            for j in range(c + 2, n):
                right = [M[c][j], M[c + 1][j]]
                M[i][j] -= (left[0] * (inverse[0][0] * right[0] + inverse[0][1] * right[1])
                            + left[1] * (inverse[1][0] * right[0] + inverse[1][1] * right[1]))
        c += 2
    return pos, neg


def mask(v):
    return sum((x % 2) << i for i, x in enumerate(v))


def table(M):
    """The reduction of M modulo 2 as a permutation of the 2048 classes of A = B/2B."""
    columns = list(map(mask, tr(M)))
    images = [0] * (1 << N)
    for x in range(1, 1 << N):
        low = x & -x
        images[x] = images[x ^ low] ^ columns[low.bit_length() - 1]
    assert len(set(images)) == len(images)
    return images


def as_permutation(M):
    return libgap.PermList(table(M)[1:])


# `sage script.py` evaluates the script in Sage's own namespace, where __file__ is sage's, so the
# file beside this script is looked up from the script's own path, then from the run directory.
name = 'coble_ambient_twenty_one_generators.json'
candidates = [Path(__file__).resolve().with_name(name),
              Path(sys.argv[0]).resolve().with_name(name),
              Path.cwd() / 'computations' / 'reports' / name]
input_path = next(path for path in candidates if path.is_file())
raw = json.loads(input_path.read_text())
print('provenance\n  exact integer arithmetic; finite orders are Schreier-Sims orders in GAP'
      '\n  ambient family computations/reports/%s\n  sha256 %s\n'
      % (input_path.name, hashlib.sha256(input_path.read_bytes()).hexdigest()))

P_0 = [unit(0), unit(2)]
assert all(dot(x, y) == 0 for x in P_0 for y in P_0)
print('B = U_1 + U_2 + I_{0,7}: rank %d, Gram determinant %d, signature (%d, %d)'
      % (N, determinant(GRAM), *signature(GRAM)))
print('P_0 = <e_1, e_2>: rank %d, primitive, totally isotropic\n' % len(P_0))

print('(1) the complete integral family of thm:o2-plane-family')
plane = {}


def perm(p):
    return [[int(i == p[j]) for j in range(N)] for i in range(N)]


plane['swap'] = perm([2, 3, 0, 1] + list(range(4, N)))
shear = [r[:] for r in I]
shear[0][2] = 1
shear[3][1] = -1
plane['shear'] = shear
for i in range(4, 10):
    p = list(range(N))
    p[i], p[i + 1] = p[i + 1], p[i]
    plane['swap_d%d' % (i - 3)] = perm(p)
for i in range(4, N):
    signs = [r[:] for r in I]
    signs[i][i] = -1
    plane['sign_d%d' % (i - 3)] = signs
even = [add(unit(i), unit(10)) for i in range(4, 10)] + [[2 * z for z in unit(10)]]
for i, e in ((0, 'e1'), (2, 'e2')):
    for j, w in enumerate(even):
        plane['E_%s_%d' % (e, j)] = trans(unit(i), w)
plane['central'] = trans(unit(0), unit(2))
levi_gl = ['swap', 'shear']
levi_od = ['swap_d%d' % j for j in range(1, 7)] + ['sign_d%d' % j for j in range(1, 8)]
unipotent = ['E_e1_%d' % j for j in range(len(even))] + ['E_e2_%d' % j for j in range(len(even))]
unipotent += ['central']
assert sorted(plane) == sorted(levi_gl + levi_od + unipotent)
print('  GL_2(Z): the transposition of the two hyperbolic planes and its shear (%d)'
      % len(levi_gl))
print('  O(D): the six adjacent transpositions and the seven sign changes (%d)' % len(levi_od))
print('  the unipotent half: fourteen even-norm transvections and the central shear (%d)'
      % len(unipotent))
print('  total %d' % len(plane))


def plane_matrix(M):
    """The action of an isometry on P_0 in the basis (e_1, e_2), and the action's existence."""
    a, b = mv(M, P_0[0]), mv(M, P_0[1])
    inside = all(a[i] == b[i] == 0 for i in (1, 3) + tuple(range(4, N)))
    return [[a[0], b[0]], [a[2], b[2]]], inside


planes = {k: plane_matrix(M) for k, M in plane.items()}
print('  every member is an integral Gram isometry of B: %s'
      % all(iso(M) for M in plane.values()))
print('  every member maps P_0 into P_0, with determinant +-1: %s'
      % all(planes[k][1] and abs(determinant(planes[k][0])) == 1 for k in plane))
print('  the parameters d_j + d_7 (1 <= j <= 6) and 2d_7 have norms %s'
      % [dot(w, w) for w in even])
print('  their coordinates are a basis of D^ev, of determinant %d'
      % abs(determinant([[w[j] for j in range(4, N)] for w in even])))


def dpoint(v):
    i = next(i for i in range(7) if v[4 + i])
    return 2 * i + (1 if v[4 + i] > 0 else 2)


def dvector(i, s):
    v = [0] * N
    v[4 + i] = s
    return v


order_od = int(libgap.Size(libgap.Group(
    [libgap.PermList([dpoint(mv(plane[k], dvector(i, s))) for i in range(7) for s in (1, -1)])
     for k in levi_od])))
print('  the thirteen signed permutations generate O(D), of order %d' % order_od)
print('  which is the order 2^7 * 7! = %d of the signed permutations: %s'
      % (2 ** 7 * 5040, order_od == 2 ** 7 * 5040))


def two_by_two(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


contragredient = 0
for k in levi_gl:
    a, b, c, d = mv(plane[k], unit(0)), mv(plane[k], unit(2)), mv(plane[k], unit(1)), \
        mv(plane[k], unit(3))
    assert all(c[i] == d[i] == 0 for i in (0, 2) + tuple(range(4, N)))
    gamma = [[a[0], b[0]], [a[2], b[2]]]
    dual = [[c[1], d[1]], [c[3], d[3]]]
    gdet = determinant(gamma)
    inverse_transpose = [[Fraction(gamma[1][1], gdet), Fraction(-gamma[1][0], gdet)],
                         [Fraction(-gamma[0][1], gdet), Fraction(gamma[0][0], gdet)]]
    contragredient += int(dual == [[int(z) for z in row] for row in inverse_transpose])
word = {((1, 0), (0, 1)): 0}
reached = {((0, -1), (1, 0)): None, ((-1, 0), (0, -1)): None}
frontier = [((1, 0), (0, 1))]
for depth in range(1, 11):
    following = []
    for current in frontier:
        A = [list(current[0]), list(current[1])]
        for step in ([[0, 1], [1, 0]], [[1, 1], [0, 1]], [[1, -1], [0, 1]]):
            product = two_by_two(A, step)
            key = (tuple(product[0]), tuple(product[1]))
            if key not in word:
                word[key] = depth
                following.append(key)
                if key in reached and reached[key] is None:
                    reached[key] = depth
    frontier = following
print('  they act on P_0 by gamma and on <f_1, f_2> by (gamma^{-1})^T: %s'
      % (contragredient == len(levi_gl)))
print('  they generate GL_2(Z): [[0, -1], [1, 0]] and -I_2 are words in them of length %d and %d'
      % (reached[((0, -1), (1, 0))], reached[((-1, 0), (0, -1))]))

moves = 0
for e_index, label in ((0, 'e1'), (2, 'e2')):
    for j, w in enumerate(even):
        member = plane['E_%s_%d' % (label, j)]
        target = add(add(unit(e_index + 1), w), [(-dot(w, w) // 2) * z for z in unit(e_index)])
        moves += int(mv(member, unit(e_index)) == unit(e_index)
                     and mv(member, unit(e_index + 1)) == target)
central = plane['central']
shears = (mv(central, unit(0)) == unit(0) and mv(central, unit(2)) == unit(2)
          and mv(central, unit(1)) == add(unit(1), unit(2))
          and mv(central, unit(3)) == add(unit(3), [-z for z in unit(0)]))
print('  each transvection fixes e_1 and e_2 and moves f_i to f_i + w - (w,w)/2 e_i: %s'
      % (moves == 2 * len(even)))
print('  the central shear fixes e_1 and e_2 and moves f_1 to f_1 + e_2, f_2 to f_2 - e_1: %s'
      % shears)

print('\n(1 cont.) reduction modulo 2')
print('  A = B/2B: %d classes, q(x) = (x,x)_B/2 mod 2, and rho(g) is g mod 2' % (1 << N))
commutator = mul(mul(mul(plane['E_e1_0'], plane['E_e2_1']), inv(plane['E_e1_0'])),
                 inv(plane['E_e2_1']))
print('  the commutator of E_{e_1,d_1+d_7} and E_{e_2,d_2+d_7} reduces to the central shear: %s'
      % (table(commutator) == table(central)))
basis_change = raw['standard_from_split']
inverse_change = mul(mul(GRAM, tr(basis_change)), raw['standard_gram'])
assert mul(inverse_change, basis_change) == I
ambient = [mul(mul(inverse_change, g['matrix_standard']), basis_change) for g in raw['generators']]
assert len(ambient) == 21 and all(map(iso, ambient))
print('  all twenty-one integral generators of thm:coble-ambient-21-generators are Gram'
      ' isometries: True')

print('\n(2) G = O(q) over F_2')
G_q = libgap.Group([as_permutation(M) for M in ambient])
H = libgap.Group([as_permutation(M) for M in plane.values()])
order_G = int(libgap.Size(G_q))
order_H = int(libgap.Size(H))
eichler = raw['eichler_generator_indices']
order_eichler = int(libgap.Size(libgap.Group([as_permutation(ambient[i]) for i in eichler])))
print('  |G| = |O(q)| = %d  (thm:coble-ambient-21-generators, rho onto)' % order_G)
print('  the Eichler subgroup of thm:coble-ambient-21-generators has index %d in G'
      % (order_G // order_eichler))
print('  |H| = |rho(Stab_{O(B)}(P_0))| = %d' % order_H)

print('\n(2 cont.) J, its stabilizer, its orbit')
J = sorted({mask(P_0[0]), mask(P_0[1]), mask(add(P_0[0], P_0[1]))})
print('  J = <e_1/2, e_2/2> = %s' % J)
on_sets = libgap.OnSets
stable = libgap.Stabilizer(G_q, libgap(J), on_sets)
order_stab = int(libgap.Size(stable))
order_orbit = len(list(libgap.Orbit(G_q, libgap(J), on_sets)))
print('  |Stab_{O(q)}(J)| = %d' % order_stab)
print("  |O(q) . J| = %d, the J' attained by primitive isotropic planes, rho onto O(q)"
      % order_orbit)
print('  |Stab| * |orbit| = |G|: %s' % (order_stab * order_orbit == order_G))
print('  H <= Stab: %s' % bool(libgap.IsSubgroup(stable, H)))

print('\nTHE NUMBERS')
print('  |H| = |rho(Stab_{O(B)}(P_0))|    = %d' % order_H)
print('  |Stab_{O(q)}(J)|                 = %d' % order_stab)
print('  index [Stab : H]                 = %d' % (order_stab // order_H))
print('  planes over J, |O(q) . J|        = %d' % order_orbit)
print('  discriminant-kernel plane orbits = %d = [O(q) : H] = %d * %d'
      % (order_G // order_H, order_stab // order_H, order_orbit))
print('  (orbits of the primitive isotropic planes under Otilde = ker rho, thm:o2-planes(3b);')
print('   a count of orbits on the discriminant data, not the 1-cusps of F_Co)')
print('  23 715 and the five page sizes   = %d' % (1575 + 270 + 9450 + 3780 + 8640))
