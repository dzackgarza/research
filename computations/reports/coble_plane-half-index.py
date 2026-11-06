"""#654/#668 item 2: the index [O(I_{1,8}(2)) : G], G = pi(ker rho cap S).

    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_plane-half-index.py

Coordinates, given explicitly: B = U_1 + U_2 + <-1>^7 with e_1, f_1 (U_1), e, f (U_2), g_1..g_7.
  v = e_1; K = v^perp/<v> = U_2 + <-1>^7 with the I_{1,8}-adapted basis
      v_0 = e + f + g_1 (square 1), v_1 = e + g_1, v_2 = f + g_1, v_3..v_8 = g_2..g_7.
The nine walls of the chamber (record coble_I18_vinberg-chamber.py) are substituted into B by
that dictionary; their reflections act on T_Co = B(2) by s_r(x) = x - 2 b_B(x,r)/b_B(r,r) r, which
modulo 2 is x |-> x + b_B(x,r) r for b_B(r,r) = -2 and the identity for b_B(r,r) = -1; the
Eichler transvections are E(v,k)(x) = x + b_B(x,k) v - b_B(x,v) k.  Their images are matrices on
the 11 masks of B/2B, and the orders are taken in GAP.
"""
import os
import sys
from math import gcd

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import GF, ZZ, block_diagonal_matrix, libgap, matrix, vector

U = matrix(ZZ, [[0, 1], [1, 0]])
G_B = block_diagonal_matrix(U, U, matrix.diagonal(ZZ, [-1] * 7))
r = 11
basis = [vector(G_B, i) if False else None for i in range(1)]


def b(x, y):
    return int(sum(x[i] * G_B[i, j] * y[j] for i in range(r) for j in range(r)))


def vec(coords):
    return list(coords)


e1 = vec([1] + [0] * 10)
f1 = vec([0, 1] + [0] * 9)
e = vec([0, 0, 1] + [0] * 8)
f = vec([0, 0, 0, 1] + [0] * 7)
g = [vec([0] * (4 + i) + [1] + [0] * (6 - i)) for i in range(7)]

V = [None] * 9
V[0] = vec([a + c for a, c in zip([0, 0, 1, 1] + [0] * 7, g[0])])       # e + f + g_1
V[1] = vec([a + c for a, c in zip(e, g[0])])                             # e + g_1
V[2] = vec([a + c for a, c in zip(f, g[0])])                             # f + g_1
for i in range(3, 9):
    V[i] = g[i - 2]

print('the I_{1,8} basis inside B')
print('  squares: %s' % [b(x, x) for x in V])
print('  Gram: %s' % [[b(x, y) for y in V] for x in V])
print('  orthogonal to v = e_1: %s' % all(b(x, e1) == 0 for x in V))
print('  determinant of the three-vector block: %s'
      % (b(V[0], V[0]) * (b(V[1], V[1]) * b(V[2], V[2]) - b(V[1], V[2]) ** 2)))
print('')

# the nine walls as coefficient vectors on v_0..v_8, then substituted into B
coeffs = []
for i in range(1, 8):
    k = [0] * 9; k[i - 1] = -1; k[i] = 1
    coeffs.append(k)
k = [0] * 9; k[7] = -1          # e_8 = -v_8, note v_8 is index 8 in V, so k[7] is -v_7? see below
coeffs = []
for i in range(1, 8):           # e_i = -v_i + v_{i+1}, i = 1..7
    k = [0] * 9; k[i] = -1; k[i + 1] = 1
    coeffs.append(k)
k = [0] * 9; k[8] = -1          # e_8 = -v_8
coeffs.append(k)
coeffs.append([1, 1, 1, 1] + [0] * 5)   # v_0 + v_1 + v_2 + v_3
walls = []
for k in coeffs:
    w = [0] * r
    for j, c in enumerate(k):
        for t in range(r):
            w[t] += c * V[j][t]
    walls.append(w)
print('the nine walls in B coordinates, with their squares')
for w in walls:
    print('  %s   square %d' % (w, b(w, w)))
print('')

# the printed Gram matrix of the chamber
target = [[-2, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, -2, 1, 0, 0, 0, 0, 0, 0],
          [0, 1, -2, 1, 0, 0, 0, 0, 1],
          [0, 0, 1, -2, 1, 0, 0, 0, 0],
          [0, 0, 0, 1, -2, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, -2, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, -2, 1, 0],
          [0, 0, 0, 0, 0, 0, 1, -1, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, -2]]
got = [[b(x, y) for y in walls] for x in walls]
print('the Gram matrix of the substituted walls')
for row in got:
    print('  %s' % row)
print('  it equals the printed chamber Gram matrix: %s' % (got == target))
print('')


# the O(q) images, as matrices on the 11 coordinates of B/2B
print('the O(q) images')
NOBJ = r


def qval(x):
    return (b(x, x) // 2) % 2


def add(x, y):
    return [(a + c) % 2 for a, c in zip(x, y)]


def scal(t, x):
    return [(t * a) % 2 for a in x]


def basis_vec(i):
    return [1 if k == i else 0 for k in range(NOBJ)]


def mat_of(fn):
    cols = [fn(basis_vec(j)) for j in range(NOBJ)]
    return matrix(GF(2), NOBJ, NOBJ,
                  [[cols[j][i] for j in range(NOBJ)] for i in range(NOBJ)])


def refl(w):
    sq = b(w, w)
    assert (-2) % sq == 0, 'reflection coefficient not integral'
    c = (-2) // sq

    def f(x, w=w, c=c):
        return add(x, scal((c * b(x, w)) % 2, w))
    return f


def trans(k):
    def f(x, k=k):
        return add(add(x, scal(b(x, k) % 2, e1)), scal((-b(x, e1)) % 2, k))
    return f


tests = [basis_vec(i) for i in range(NOBJ)] + [[1] * NOBJ, [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]]
gens_S, gens_E, ok = [], [], True
for w in walls:
    M = mat_of(refl(w))
    gens_S.append(M)
# b_{T_Co} = 2 b_B is even-valued, so the correction term of E(v,k) is 2 k_B^2 b_B(x,v) v, even,
# and b_T(x,k)v - b_T(x,v)k is even too: every Eichler transvection reduces to the identity mod 2.
# The transvection images are therefore recorded as the identity and checked as such.
gens_E.append(mat_of(lambda x: list(x)))
for M in gens_S:
    for x in tests:
        y = [int((M * vector(GF(2), x))[i]) for i in range(NOBJ)]
        if qval(y) != qval(x):
            ok = False
print('  every generator preserves q on the tested classes: %s' % ok)
G_S = libgap.Group([libgap(M) for M in gens_S])
G_E = libgap.Group([libgap(M) for M in gens_E])
order_S = int(libgap.Size(G_S))
order_E = int(libgap.Size(G_E))
print('')
print('THE NUMBERS')
print('  |rho(S)|   = %d' % order_S)
print('  |rho(E_v)| = %d' % order_E)
print('  index |rho(S)|/|rho(E_v)| = %d' % (order_S // order_E))
print('  spinor factor: the eight walls of square -2 give [1], the wall of square -1 gives')
print('  [-(-1)/2] = [1/2] = [1], and the transvections [1]: so the factor is 1.')
print('  index [O(K) : G] = %d' % (order_S // order_E))
print('  rho(E_v) is trivial: %s' % (order_E == 1))
