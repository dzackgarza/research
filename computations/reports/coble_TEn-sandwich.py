"""#654 step (iii): the sandwich on T_En, for the two O(T_En)-orbits of primitive isotropic vectors.

T_En = U + M with M = N(2), N = U + E8 unimodular, on slots 2-11.  Then T_En* = U + (1/2)M and
A_{T_En} = (1/2)M/M = N/2N, the ten masks on slots 2-11, with q([n]) = n^2_N / 2 = b_T(n,n)/4 mod 2.
An integral isometry g acts on [n] by reading the slots 2-11 part of g.(0,0,n) mod 2.
Generators: the ten lifted wall reflections of each cusp chamber, and the Eichler transvections
E(eta, w)(x) = x + b(x,w) eta - b(x,eta) w for w in a basis of the even sublattice of eta^perp.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, GF, libgap, matrix, vector  # noqa: E402

C = [[int(x) for x in row] for row in CartanMatrix(['E', 8])]
E8n = [[-2 * C[i][j] for j in range(8)] for i in range(8)]   # E8(2) = -2C, negative definite
G = [[0] * 12 for _ in range(12)]
G[0][1] = G[1][0] = 1                       # U on slots 0-1
G[2][3] = G[3][2] = 1                       # M = N(2): the U part of N doubled is [[0,2],[2,0]]/2
for i in range(2):
    pass
# T_En = U + U(2) + E8(2): slots 2-3 carry U(2) = 2*U, slots 4-11 carry E8(2) = 2*E8(-1)
G[2][3] = G[3][2] = 2
for i in range(8):
    for j in range(8):
        G[4 + i][4 + j] = E8n[i][j]
N = 12


def b(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


def qval(mask):
    """q on the class [n] with n = the mask on slots 2-11: b_T(n,n)/4 mod 2."""
    v = [0, 0] + list(mask)
    return (b(v, v) // 4) % 2


def apply_g(M, mask):
    v = [0, 0] + list(mask)
    w = [sum(M[i][j] * v[j] for j in range(N)) for i in range(N)]
    return [int(w[2 + i]) % 2 for i in range(10)]


def mat_of(fn):
    cols = [fn([1 if k == i else 0 for k in range(10)]) for i in range(10)]
    return matrix(GF(2), 10, 10, [[cols[j][i] for j in range(10)] for i in range(10)])


def refl_matrix(r):
    sq = b(r, r)
    # integrality is not 'r^2 divides 2': for a 2-elementary lattice a wall of norm -4 can still
    # reflect integrally, because b(x,r) is even for every x.  Build the matrix over QQ and check
    # that it is integral and Gram-preserving.
    from fractions import Fraction
    c = Fraction(-2, sq)
    M = [[Fraction(1 if i == j else 0)
          + c * r[i] * sum(G[j][k] * r[k] for k in range(N)) for j in range(N)] for i in range(N)]
    assert all(x.denominator == 1 for row in M for x in row), 'reflection not integral'
    M = [[int(x) for x in row] for row in M]
    for i in range(N):
        for j in range(N):
            lhs = sum(M[k][i] * G[k][l] * M[l][j] for k in range(N) for l in range(N))
            assert lhs == G[i][j], 'reflection does not preserve the form'
    return M


def trans_matrix(eta, w):
    return [[(1 if i == j else 0) + w[i] * sum(G[j][k] * eta[k] for k in range(N))
             - eta[i] * sum(G[j][k] * w[k] for k in range(N))
             for j in range(N)] for i in range(N)]


walls1 = ([[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -2, -3, -4, -6, -5, -4, -3, -2]])
walls2 = ([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, -2, -2, -3, -4, -6, -5, -4, -3, -2]])
cases = (('eta = e_1 (div 1), K(L_1) = U(2) + E8(2)', [1] + [0] * 11, walls1, 1,
          [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
         ('eta = e_3 (div 2), K(L_2) = U + E8(2)', [0, 0, 1] + [0] * 9, walls2, 527,
          [0, 1, 4, 5, 6, 7, 8, 9, 10, 11]))
OQ = 46998591897600
tests = [[1 if k == i else 0 for k in range(10)] for i in range(10)] + [[1] * 10]
for name, eta, walls, orbit, slots in cases:
    lifted = []
    for w in walls:
        v = [0] * 12
        for a, i in zip(w, slots):
            v[i] = a
        lifted.append(v)
    gens, ok = [], True
    for r in lifted:
        M = refl_matrix(r)
        gens.append(mat_of(lambda m, M=M: apply_g(M, m)))
    for i in slots:
        w = [1 if k == i else 0 for k in range(12)]
        M = trans_matrix(eta, w)
        gens.append(mat_of(lambda m, M=M: apply_g(M, m)))
    for M in gens:
        for x in tests:
            y = [int((M * vector(GF(2), x))[i]) for i in range(10)]
            if qval(y) != qval(x):
                ok = False
    start = time.time()
    order = int(libgap.Size(libgap.Group([libgap(M) for M in gens])))
    stab = OQ // orbit
    print(name)
    print('  %d generators, every one q-preserving: %s' % (len(gens), ok))
    print('  |rho(S_eta)| = %d' % order)
    print('  |O(q)| / (orbit size %d) = |Stab_{O(q)}([eta/2])| = %d' % (orbit, stab))
    print('  index |Stab| / |rho(S_eta)| = %d   (published: %d)'
          % (stab // order if order else -1, orbit))
    print('  (%.0f s)' % (time.time() - start))
    print('')
