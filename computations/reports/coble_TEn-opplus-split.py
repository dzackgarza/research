"""#654 step (iii): the O~^+ split for the two T_En classes.

T_En = U + U(2) + E8(2), slots 0-1 (U), 2-3 (U(2)), 4-11 (E8(2)).  For each eta an explicit element
of ker rho cap Stab(eta) whose orientation character is -1 is exhibited: identity on the summand
containing eta, -1 on the rest.  Its mask action is trivial because -1 is the identity mod 2, and
its determinant on the positive 2-plane is (+1)(-1) = -1, so it lies outside O^+(T_En) by
spinor-norm.md's definition for signature (2,n).
"""
import os
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix  # noqa: E402

C = [[int(x) for x in row] for row in CartanMatrix(['E', 8])]
G = [[0] * 12 for _ in range(12)]
G[0][1] = G[1][0] = 1
G[2][3] = G[3][2] = 2
for i in range(8):
    for j in range(8):
        G[4 + i][4 + j] = -2 * C[i][j]
N = 12


def b(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


def isometry(signs):
    return [[signs[i] * G[i][j] * signs[j] * 0 + (signs[i] if i == j else 0) for j in range(N)]
            for i in range(N)]


def check(M, eta, label, keep):
    for i in range(N):
        for j in range(N):
            assert sum(M[k][i] * G[k][l] * M[l][j] for k in range(N) for l in range(N)) == G[i][j], 'not an isometry'
    fixed = [sum(M[i][j] * eta[j] for j in range(N)) for i in range(N)] == list(eta)
    # mask action on slots 2-11, mod 2
    trivial = True
    for m in range(1 << 10):
        v = [0, 0] + [(m >> k) & 1 for k in range(10)]
        w = [sum(M[i][j] * v[j] for j in range(N)) for i in range(N)]
        if [(int(w[2 + k]) % 2) for k in range(10)] != [(m >> k) & 1 for k in range(10)]:
            trivial = False
            break
    # orientation: the two positive directions are e1 + f1 (slots 0-1) and e3 + f3 (slots 2-3)
    v1 = [1, 1] + [0] * 10
    v2 = [0, 0, 1, 1] + [0] * 8
    assert b(v1, v1) > 0 and b(v2, v2) > 0 and b(v1, v2) == 0
    Mv1 = [sum(M[i][j] * v1[j] for j in range(N)) for i in range(N)]
    Mv2 = [sum(M[i][j] * v2[j] for j in range(N)) for i in range(N)]
    # g(v1) = s1 v1, g(v2) = s2 v2 for a diagonal summand-wise g
    s1 = Mv1[0] // v1[0] if v1[0] else None
    s2 = Mv2[2] // v2[2] if v2[2] else None
    print('%s' % label)
    print('  fixes verbose eta: %s' % fixed)
    print('  acts trivially on A_{T_En} (all 1024 masks): %s' % trivial)
    print('  scaling on the two positive directions: %s and %s, determinant %s'
          % (s1, s2, (s1 or 1) * (s2 or 1)))
    print('  lies in O^+(T_En): %s' % ((s1 or 1) * (s2 or 1) > 0))
    print('')


s_eta1 = [1, 1] + [-1] * 10          # identity on U (slots 0-1), -1 on U(2) + E8(2)
s_eta3 = [-1, -1, 1, 1] + [-1] * 8   # identity on U(2) (slots 2-3), -1 on U + E8(2)
check(isometry(s_eta1), [1] + [0] * 11, 'eta = e_1 (div 1): g = id_U (+) (-id on U(2)+E8(2))', None)
check(isometry(s_eta3), [0, 0, 1] + [0] * 9, 'eta = e_3 (div 2): g = id_U(2) (+) (-id on U+E8(2))', None)
