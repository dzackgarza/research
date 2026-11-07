#!/usr/bin/env python
"""Exact embedded-plane stabilizer images for #748, on A = T*/T with native finite parents.

T_En = U + U(2) + E_8(2), Gram G = block_diag(U,2U,2(-Cartan(E8))).
The discriminant module A = T*/T is identified explicitly with the F_2-submodule
K = ker(G mod 2) of T/2T: class [x/2] in A corresponds to the parity vector x mod 2.
Indeed [x/2] is in T* iff (x,T) is even, and [x/2] = [y/2] iff x-y is in 2T.
The printout checks |A| = |K| = 1024 and dim K = 10 (the scaled coordinates).

For every displayed matrix S, S is integral and S^T G S = G, and the integral span
of the primitive isotropic plane P is preserved (exact solve over QQ with an
integrality check).  The induced action is then projected to K, not to T/2T;
standalone GAP computes its finite group with coefficient Z(2).  No use is made
of the larger T/2L module or of a rational matrix group.

The two primitive planes are P_I = <e,e'> and P_II = <e',z> with
z = 2e + 2f + a_1 + a_2 for a pair of orthogonal E_8 roots.
"""
import os
import sys
import subprocess

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = "/sage/.venv/bin" + os.pathsep + os.environ.get("PATH", "")

import sage_extensions  # noqa: E402
import sage_indefinite_port  # noqa: E402
from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix, GF, vector, QQ  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

print("embedded-plane stabilizer images, on A = T*/T")
print("provenance")
print("  Sage: %s" % SAGE_VERSION)
print("  sage-indefinite-port: %s" % os.path.dirname(sage_indefinite_port.__file__))
print("  sage-extensions:      %s" % os.path.dirname(sage_extensions.__file__))

U = matrix(ZZ, [[0, 1], [1, 0]])
E8C = -CartanMatrix(['E', 8])
G = block_diagonal_matrix(U, 2 * U, 2 * E8C)
N = 12
E0, F0, E1, F1 = 0, 1, 2, 3
ROOTS = list(range(4, 12))
T = Lattices(ZZ)([list(r) for r in G.rows()])
A = T.discriminant_quadratic_form()
print("T_En: rank %d det %s signature %s" % (T.rank(), T.determinant(), T.signature_pair()))
F2 = GF(2)
K = G.change_ring(F2).right_kernel()
Kb = K.basis_matrix()
print("K = ker(G mod 2): dimension %d, cardinality %d, owned |A| = %d"
      % (K.dimension(), int(K.cardinality()), int(A.cardinality())))
assert K.dimension() == 10 and int(K.cardinality()) == int(A.cardinality()) == 1024
print("K basis (the discriminant submodule, not all of T/2T):")
print(Kb)
print("")


def vec(d):
    v = [0] * N
    for i, c in d.items():
        v[i] = c
    return v


def norm(x):
    return sum(x[i] * x[j] * int(G[i, j]) for i in range(N) if x[i]
               for j in range(N) if x[j])


def pairing(x, y):
    return sum(x[i] * y[j] * int(G[i, j]) for i in range(N) if x[i]
               for j in range(N) if y[j])


def parity(x):
    return tuple(1 if a % 2 else 0 for a in x)


def even_pairing(v):
    return all(pairing(v, vec({i: 1})) % 2 == 0 for i in range(N))


def trans_matrix(eta, w):
    """The established E(eta,w) = x + b(x,w)eta - b(x,eta)w - (w^2/2)b(x,eta)eta.

    The dual-basis parameter w may be fractional; every candidate is checked to be
    integral, Gram-preserving, and to preserve the embedded plane.  Parameters that
    fail integrality are reported rather than being silently discarded.
    """
    from fractions import Fraction as F
    hc = QQ(norm(w)) / 2
    M = matrix(QQ, 12, 12, lambda i, j:
               QQ(int(i == j)) + w[i] * sum(G[j][k] * eta[k] for k in range(N))
               - eta[i] * sum(G[j][k] * w[k] for k in range(N))
               - hc * eta[i] * sum(G[j][k] * eta[k] for k in range(N)))
    if not all(x in ZZ for row in M.rows() for x in row):
        raise ValueError("E(eta,w) is not integral for eta=%s, w=%s" % (eta, w))
    S = matrix(ZZ, M)
    assert (S.transpose() * G * S) == G
    return S


def preserves(P, S):
    assert (S.transpose() * G * S) == G, "candidate is not an integral isometry"
    PM = matrix(ZZ, 2, N, P).transpose()
    for p in P:
        im = vector(QQ, list(S * vector(ZZ, p)))
        try:
            coeffs = PM.solve_right(im)
        except Exception:
            return False
        if not all(c in ZZ for c in coeffs):
            return False
    return True


def induced_on_K(S):
    """Columns of the induced map on K's owned basis, with Z(2) coefficient."""
    out = []
    for i in range(Kb.nrows()):
        y = vector(F2, list(S * vector(ZZ, [int(a) for a in Kb.row(i)])))
        c = Kb.transpose().solve_right(y)
        out.append([int(a) for a in c])
    return out


def gap_mat(M):
    return "Z(2)*[" + ",".join("[" + ",".join(str(x) for x in row) + "]" for row in M) + "]"


def gap_order(mats):
    stmt = "Order(Group(" + ",".join(mats) + "));"
    r = subprocess.run(["/sage/.venv/bin/gap", "-q"], input=stmt + "\n",
                       text=True, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("standalone GAP failed: %s" % r.stderr[-500:])
    out = [x for x in r.stdout.strip().splitlines() if x.strip()]
    if not out or not out[-1].isdigit():
        raise RuntimeError("unexpected GAP answer: %s" % r.stdout[-500:])
    return int(out[-1])


def perp_quotient_gram(P):
    gv = list(G * vector(ZZ, P[0]))
    gw = list(G * vector(ZZ, P[1]))
    Kern = matrix(ZZ, 2, N, [gv, gw]).right_kernel().basis_matrix()
    Gp = Kern * G * Kern.transpose()
    C = matrix(ZZ, 2, 10)
    for i, p in enumerate(P):
        c = Kern.transpose().solve_right(vector(ZZ, p))
        assert all(x in ZZ for x in c)
        C.set_row(i, [int(a) for a in c])
    Dm, Um, Vm = C.smith_form()
    assert [x for x in Dm.diagonal() if x] == [1, 1]
    R = Vm.inverse().rows()[2:]
    assert abs(C.stack(matrix(ZZ, 8, 10, R)).determinant()) == 1
    return matrix(ZZ, 8, 8, [[sum(R[i][k] * Gp[k][l] * R[j][l]
                               for k in range(10) for l in range(10))
                             for j in range(8)] for i in range(8)])


def perp_classes(P):
    Mp = matrix(ZZ, 2, N, [list(G * vector(ZZ, P[0])),
                           list(G * vector(ZZ, P[1]))])
    Kern = Mp.right_kernel().basis_matrix()
    out = []
    for p in P:
        for bits in range(1 << Kern.nrows()):
            coeff = [(bits >> i) & 1 for i in range(Kern.nrows())]
            y = tuple(sum(coeff[i] * int(Kern[i, j]) for i in range(Kern.nrows()))
                      for j in range(N))
            out.append(y)
    return out


def discriminant_image(P):
    cls = [parity(p) for p in P if even_pairing(p)]
    elems = {tuple([0] * N)}
    for c in cls:
        elems |= {tuple((a + b) % 2 for a, b in zip(x, c)) for x in list(elems)}
    return elems


ORTHO = []
for i in range(8):
    if all(int(G[ROOTS[i], ROOTS[j]]) == 0 for j in ORTHO):
        ORTHO.append(i)
O1, O2 = (ROOTS[i] for i in ORTHO[:2])
P1 = [vec({E0: 1}), vec({E1: 1})]
P2 = [vec({E1: 1}), vec({E0: 2, F0: 2, O1: 1, O2: 1})]

for tag, P, target in (("I", P1, 89181388800), ("II", P2, 1981808640)):
    print("")
    print("type %s" % tag)
    print("  plane generators:", P)
    D = discriminant_image(P)
    print("  discriminant image D: order %d, nonzero classes %s" %
          (len(D), ["".join(str(a) for a in c) for c in sorted(D) if any(c)]))
    Qgram = perp_quotient_gram(P)
    print("  exact quotient Gram Q = P^perp/P: %s" % Qgram)
    if tag == "II":
        Dstar = -2 * CartanMatrix(['D', 8]).inverse()
        R = matrix(ZZ, [[1, 2, 3, 4, 5, 0, 0, 1],
                        [-1, 0, 1, 2, 3, -2, -1, 0],
                        [0, 0, 0, 0, 0, -1, 0, 0],
                        [0, -1, -2, -3, -4, -1, 0, -1],
                        [0, -1, -2, -3, -4, 0, 0, 0],
                        [0, -1, -2, -3, -3, 0, 0, 0],
                        [0, -1, -2, -2, -2, 0, 0, 0],
                        [0, -1, -1, -1, -1, 0, 0, 0]])
        print("  display the integral identification matrix R, certified"
              " R^T(-Qgram)R = 2 D_8^{-1}: %s" %
              ((R.transpose() * (-Qgram) * R) == 2 * CartanMatrix(['D', 8]).inverse()))
    images = {}
    accepted, skipped = 0, []
    half_root = QQ(1) / 2
    for eta in P:
        for i in ROOTS + [E1, F1]:
            w = [0] * N
            w[i] = half_root
            if pairing(eta, w) != 0:
                continue
            try:
                S = trans_matrix(eta, w)
            except ValueError as exc:
                skipped.append(str(exc))
                continue
            assert preserves(P, S), "displayed isometry does not stabilize its plane"
            M = induced_on_K(S)
            print("  accepted induced discriminant action (eta index %d, w index %d): %s"
                  % (list(P).index(eta), i, M))
            images[tuple(tuple(r) for r in M)] = S
            accepted += 1
    print("  dual-basis transvections accepted (integral, form-preserving, plane-preserving): %d"
          % accepted)
    print("  candidates rejected on integrality: %d" % len(skipped))
    Mats = [gap_mat(m) for m in images]
    answer = gap_order(Mats)
    print("  | generated discriminant image of these integral stabilizers | = %d" % answer)
    print("  stated finite target |Stab(D)| = %d" % target)
    print("  native GAP coefficient object is Z(2), with K dimension 10")
    if answer:
        print("  target / computed generated image = %s" %
              (target // answer if target % answer == 0 else "not integral")
    )
