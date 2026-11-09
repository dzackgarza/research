#!/usr/bin/env python
"""Exact embedded-plane stabilizer images for #748, on A = T*/T with native finite parents.

T_En = U + U(2) + E_8(2), Gram G = block_diag(U,2U,2(-Cartan(E8))).
The discriminant module A = T*/T is identified explicitly with the F_2-submodule
K = ker(G mod 2) of T/2T: class [x/2] in A corresponds to the parity vector x mod 2.
Indeed [x/2] is in T* iff (x,T) is even, and [x/2] = [y/2] iff x-y is in 2T.
The printout checks |A| = |K| = 1024 and dim K = 10 (the scaled coordinates).
The owner's norm-valued discriminant form is b([x/2],[y/2]) = (x,y)/4 mod Z
and q([x/2]) = x^2/4 mod 2Z.  Thus the finite polar form is (x,y)/2 mod 2.
The equivalent half-norm value is x^2/8 mod Z, not modulo 2Z.

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
from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix, GF, vector, QQ, identity_matrix  # noqa: E402
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


# Type II: actual integral Levi lifts, the natural gluing, and the full kernel.
# Every convention below is checked, including the dual (contragredient) action.
print("\n\ntype-II integral Levi lifts and the D^perp/D exact sequence")
P = P2
Mp = matrix(ZZ, 2, N, [list(G * vector(ZZ, P[0])), list(G * vector(ZZ, P[1]))])
Kern = Mp.right_kernel().basis_matrix()
Gp = Kern * G * Kern.transpose()
C = matrix(ZZ, 2, 10)
for i, p in enumerate(P):
    c = Kern.transpose().solve_right(vector(ZZ, p))
    C.set_row(i, [int(a) for a in c])
Dm, Um, Vm = C.smith_form()
B = Vm.inverse()
W = B * Kern
Rcoords = matrix(ZZ, B.rows()[2:])
Ractual = matrix(ZZ, W.rows()[2:])
Qgram = perp_quotient_gram(P)
assert Rcoords * Gp * Rcoords.transpose() == Qgram
assert Ractual == Rcoords * Kern
assert C * B.inverse() == matrix(ZZ, [[0, 1] + [0] * 8, [1, 0] + [0] * 8])
assert B[:2] * Gp * Rcoords.transpose() == 0
print("  the actual P^perp basis and Q basis are the ones used in the quotient certificate")


def canonical_classes(H):
    """Smith residuals r with dual class H^-1 U^-1 r, where D=U H V."""
    Dm, Um, Vm = H.smith_form()
    Uinv = Um.inverse()
    divisors = [int(d) for d in Dm.diagonal()]
    total = 1
    for d in divisors:
        total *= d
    reps = []
    for k in range(total):
        rr = k
        rep = []
        for d in divisors:
            rep.append(rr % d)
            rr //= d
        reps.append(tuple(rep))

    def canonical(m):
        rr = list(Um * vector(QQ, m))
        return tuple(int(rr[i]) % divisors[i] for i in range(len(divisors)))

    return reps, canonical, divisors, total, Uinv


reps, canonical, divisors, total, Uinv_Q = canonical_classes(Qgram)
assert total == 64 and divisors == [1, 1, 2, 2, 2, 2, 2, 2]


def dual_numerator(rep):
    ans = Uinv_Q * vector(QQ, rep)
    assert all(x in ZZ for x in ans)
    return vector(ZZ, ans)


def dual_action(X, rep):
    """A column isometry X acts on a dual numerator by X^(-T)."""
    return canonical(list(X.inverse().transpose() * dual_numerator(rep)))


def dual_permutation(X):
    perm = [reps.index(dual_action(X, rep)) + 1 for rep in reps]
    assert len(set(perm)) == total
    return perm


for rep in reps:
    numerator = dual_numerator(rep)
    dual_class = Qgram.inverse() * numerator
    assert Qgram * dual_class == numerator
    assert canonical(list(Qgram * dual_class)) == rep
assert all(dual_action(identity_matrix(ZZ, 8), rep) == rep for rep in reps)
print("  Smith dual convention proved on all 64 representatives: Q^-1 U^-1 r")

# The native definite group is included with the same corrected dual action.
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
OQ = IntegralLattice(Qgram).orthogonal_group(is_finite=True)
native_perms = []
for X in OQ.gens():
    X = matrix(ZZ, X)
    if X.transpose() * Qgram * X != Qgram:
        X = X.transpose()
    assert X.transpose() * Qgram * X == Qgram
    native_perms.append(dual_permutation(X))
X0, X1 = (matrix(ZZ, OQ.gens()[0]), matrix(ZZ, OQ.gens()[1]))
if X0.transpose() * Qgram * X0 != Qgram:
    X0 = X0.transpose()
if X1.transpose() * Qgram * X1 != Qgram:
    X1 = X1.transpose()
for rep in reps:
    assert dual_action(X1 * X0, rep) == dual_action(X1, dual_action(X0, rep))
for X in (X0, X1):
    XTinv = X.inverse().transpose()
    for rep in reps:
        numerator = dual_numerator(rep)
        expected = dual_action(X, rep)
        for j in range(8):
            shifted = numerator + vector(ZZ, Qgram.row(j))
            assert canonical(list(XTinv * shifted)) == expected
native_stmt = "Order(Group([" + ",".join("PermList(%s)" % p for p in native_perms) + "]));"
native_order = int(subprocess.run(
    ["/sage/.venv/bin/gap", "-q"], input=native_stmt + "\n", text=True,
    capture_output=True, check=True).stdout.strip().splitlines()[-1])
print("  | native O(Q) action on Q*/Q, using X^(-T)U^(-1) | = %d" % native_order)
assert native_order == 40320


def coordinates(element):
    underlying = element.to_vector()
    return [int(underlying(label)) for label in element.parent().module_generating_set()]


Qpositive = Lattices(ZZ)([list(r) for r in (-Qgram).rows()])
shell = Qpositive.vectors_of_square(4)
assert int(shell.cardinality()) == 368
reflection_lifts = []
nonreflective_shell_vectors = 0
for element in shell:
    coeff = coordinates(element)
    r = list(vector(ZZ, coeff) * Ractual)
    assert pairing(r, P[0]) == pairing(r, P[1]) == 0 and norm(r) == -4
    # An integral square-(-4) reflection needs even pairings with T. If a
    # P-translate supplies them, it has the same image in Q and fixes P.
    v = None
    for p in ([0] * N, P[0], P[1], list(vector(ZZ, P[0]) + vector(ZZ, P[1]))):
        trial = list(vector(ZZ, r) + vector(ZZ, p))
        if even_pairing(trial):
            v = trial
            break
    if v is None:
        nonreflective_shell_vectors += 1
        continue
    M = matrix(QQ, N, N, lambda i, j:
               QQ(int(i == j)) + QQ(v[i]) * sum(G[j][k] * v[k] for k in range(N)) / 2)
    assert all(x in ZZ for row in M.rows() for x in row)
    M = matrix(ZZ, M)
    assert M.transpose() * G * M == G and preserves(P, M)
    assert M * vector(ZZ, P[0]) == vector(ZZ, P[0])
    assert M * vector(ZZ, P[1]) == vector(ZZ, P[1])
    Y = W.transpose().solve_right(M * W.transpose())
    X = Y[2:, 2:]
    assert Y[:2, :2] == identity_matrix(ZZ, 2)
    assert Y[:2, 2:] == 0 and Y[2:, :2] == 0
    assert X.transpose() * Qgram * X == Qgram
    reflection_lifts.append((v, M, X))
print("  square-(-4) vectors of Q: 368; actual integral P-pointwise reflection lifts: %d"
      % len(reflection_lifts))
print("  shell vectors not used because no P-translate lies in 2T*: %d"
      % nonreflective_shell_vectors)
assert len(reflection_lifts) == 112 and nonreflective_shell_vectors == 256
reflection_perms = [dual_permutation(X) for _, _, X in reflection_lifts]
reflection_stmt = "Order(Group([" + ",".join("PermList(%s)" % p for p in reflection_perms) + "]));"
reflection_order = int(subprocess.run(
    ["/sage/.venv/bin/gap", "-q"], input=reflection_stmt + "\n", text=True,
    capture_output=True, check=True).stdout.strip().splitlines()[-1])
print("  | action of the integral reflection lifts on Q*/Q | = %d" % reflection_order)
assert reflection_order == 40320
for X in (reflection_lifts[0][2], reflection_lifts[1][2]):
    XTinv = X.inverse().transpose()
    for rep in reps:
        numerator = dual_numerator(rep)
        expected = dual_action(X, rep)
        for j in range(8):
            shifted = numerator + vector(ZZ, Qgram.row(j))
            assert canonical(list(XTinv * shifted)) == expected
print("  dual action certificates: identity, composition, and invariance modulo Q Z^8")

# The owner's norm-valued discriminant convention on K.
KbT = Kb.transpose()
KbZ = matrix(ZZ, [[int(a) for a in row] for row in Kb.rows()])


def k_coordinates(x):
    return vector(F2, list(KbT.solve_right(vector(F2, list(x)))))


def finite_q_from_parity(x):
    return QQ(norm(x)) / 4


def half_norm_q_from_parity(x):
    return QQ(norm(x)) / 8


d0 = k_coordinates(parity(P[0]))
d1 = k_coordinates(parity(P[1]))
Dspan = {tuple(vector(F2, [0] * 10)), tuple(d0), tuple(d1), tuple(d0 + d1)}


def in_D(x):
    return tuple(x) in Dspan


assert len(Dspan) == 4
pairing_on_K = KbZ * G * KbZ.transpose()
assert all(x % 2 == 0 for row in pairing_on_K.rows() for x in row)
BK = matrix(F2, [[int(pairing_on_K[i, j] // 2) for j in range(10)] for i in range(10)])
Dperp = []
for bits in range(1024):
    k = vector(F2, [(bits >> i) & 1 for i in range(10)])
    if all((k * BK * d) == 0 for d in (d0, d1)):
        Dperp.append(k)
assert len(Dperp) == 256
print("  |D| = 4, |D^perp| = 256, |D^perp/D| = 64; BK = (x,y)/2 mod 2 is nonzero")

# Representative independence: x/2 in T* makes (x,t) even. The norm value
# changes by (x,t)+t^2 in 2Z and the half-norm value by half that in Z.
for bits in range(1024):
    k = vector(F2, [(bits >> i) & 1 for i in range(10)])
    x = vector(ZZ, list(k * Kb))
    for j in range(N):
        t = vec({j: 1})
        delta = pairing(x, t) + norm(t)
        assert delta % 2 == 0
        xp = list(x + 2 * vector(ZZ, t))
        assert finite_q_from_parity(xp) - finite_q_from_parity(x) == delta
        assert half_norm_q_from_parity(xp) - half_norm_q_from_parity(x) == QQ(delta) / 2
        for ybits in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512):
            y = vector(ZZ, list(vector(F2, [(ybits >> i) & 1 for i in range(10)]) * Kb))
            beta_change = QQ(pairing(x + 2 * vector(ZZ, t), y) - pairing(x, y)) / 2
            assert beta_change % 2 == 0
print("  q=x^2/4 mod 2Z, half norm=x^2/8 mod Z, beta=(x,y)/2 mod 2: representative-independent")

# Natural gluing j: [q] -> [q+u]+D, with q in Q*, u orthogonal to P^perp,
# and q+u in T*. Explicit basis lifts are displayed, then all 64 values checked.
Uperp = matrix(QQ, Kern * G).right_kernel().basis_matrix()
Jcolumns = []
for i in range(2, 8):
    m = vector(ZZ, [int(j == i) for j in range(8)])
    qcoords = Qgram.inverse() * vector(QQ, dual_numerator(m))
    q0 = qcoords * matrix(QQ, Ractual)
    found = None
    for a in range(-4, 5):
        for b in range(-4, 5):
            coeff = vector(QQ, [QQ(a) / 2, QQ(b) / 2])
            candidate = q0 + coeff * Uperp
            if all(x in ZZ for x in G * candidate):
                found = candidate
                break
        if found is not None:
            break
    assert found is not None
    x = 2 * found
    assert all(a in ZZ for a in x)
    k = k_coordinates(x)
    assert k in Dperp
    Jcolumns.append(k)
    print("  gluing basis %d: q = %s; q+u = %s; K class = %s"
          % (i, q0, found, list(k)))
J = matrix(F2, 10, 6, lambda r, c: Jcolumns[c][r])
assert J.rank() == 6
JD = J.augment(matrix(F2, 10, 2, lambda r, c: (d0 if c == 0 else d1)[r]))
assert JD.rank() == 8
assert all(not in_D(J * vector(F2, [(bits >> i) & 1 for i in range(6)]))
           for bits in range(1, 64))
print("  explicit gluing matrix J; rank(J)=6 and rank([J|D])=8:")
print(J)
print("  quotient injectivity: every nonzero vector of im(J) lies outside D")
for m in reps:
    k = J * vector(F2, list(m[2:]))
    assert k in Dperp
    qcoords = Qgram.inverse() * vector(QQ, dual_numerator(m))
    q0 = qcoords * matrix(QQ, Ractual)
    qQ = q0.dot_product(G * q0)
    kx = vector(ZZ, list(k * Kb))
    qK = finite_q_from_parity(kx)
    assert QQ(qQ - qK) / 2 in ZZ, (m, qQ, qK)
print("  all 64 classes satisfy j(A_Q) inside D^perp and q_Q = q_T mod 2Z")


def action_matrix(S):
    return matrix(F2, induced_on_K(S)).transpose()


for v, M, X in reflection_lifts:
    SM = action_matrix(M)
    for i in range(2, 8):
        m = vector(ZZ, [int(j == i) for j in range(8)])
        out = vector(F2, dual_action(X, m)[2:])
        lhs = SM * (J * vector(F2, list(m[2:])))
        rhs = J * out
        assert in_D(lhs - rhs), (v, i, lhs, rhs)
print("  all 112 integral lifts agree with their dual Q*/Q actions transported by J")

# The fifteen integral transvections lie in the kernel on D^perp/D.
images = {}
half_root = QQ(1) / 2
for eta in P:
    for i in ROOTS + [E1, F1]:
        w = [0] * N
        w[i] = half_root
        if pairing(eta, w) != 0:
            continue
        S = trans_matrix(eta, w)
        assert preserves(P, S)
        images[tuple(tuple(r) for r in induced_on_K(S))] = S
assert len(images) == 15
plane_gens = []
for S in images.values():
    SM = action_matrix(S)
    assert in_D(SM * d0) and in_D(SM * d1)
    for k in Dperp:
        assert in_D(SM * k - k)
    cols = []
    for d in (d0, d1):
        y = SM * d
        match = None
        for a, b in ((0, 0), (1, 0), (0, 1), (1, 1)):
            if a * d0 + b * d1 == y:
                match = (a, b)
                break
        assert match is not None
        cols.append(match)
    plane_gens.append(matrix(F2, 2, 2, lambda r, c: cols[c][r]))
print("  every one of the fifteen Eichler matrices acts trivially on D^perp/D")


def gap_run(stmt):
    rr = subprocess.run(["/sage/.venv/bin/gap", "-q"], input=stmt + "\n",
                        text=True, capture_output=True)
    assert rr.returncode == 0, rr.stderr
    return rr.stdout.strip()


gap_all = ",".join(gap_mat([list(map(int, row)) for row in action_matrix(S).rows()])
                   for S in images.values())
gap_plane = ",".join(gap_mat([list(map(int, row)) for row in A2.rows()]) for A2 in plane_gens)
print("  | generated kernel group | =", gap_run("Print(Order(Group(" + gap_all + ")),\"\\n\");"))
print("  | generated action on D | =", gap_run("Print(Order(Group(" + gap_plane + ")),\"\\n\");"))
# GAP acts on row vectors from the right; transpose the column actions.
gap_all_right = ",".join(gap_mat([list(map(int, row)) for row in action_matrix(S).transpose().rows()])
                         for S in images.values())
gap_d0 = "Z(2)*[" + ",".join(str(int(x)) for x in d0) + "]"
gap_d1 = "Z(2)*[" + ",".join(str(int(x)) for x in d1) + "]"
kernel_stmt = ("G:=Group(" + gap_all_right + ");; K:=Stabilizer(G,[" + gap_d0 + "," + gap_d1
               + "],OnTuples);; Print(Order(K),\" \",Index(G,K),\"\\n\");")
print("  | pointwise-on-D subgroup | and its index =", gap_run(kernel_stmt))
assert gap_run("Print(Order(Group(" + gap_all + ")),\"\\n\");") == "49152"
assert gap_run("Print(Order(Group(" + gap_plane + ")),\"\\n\");") == "6"
assert gap_run(kernel_stmt) == "8192 6"

# Orientation: tau is in ker(rho), stabilizes both plane types, and has
# normalized real spinor norm -1 because -id on U(2) has positive index one.
tau = identity_matrix(ZZ, N)
tau[2, 2] = tau[3, 3] = -1
assert tau.transpose() * G * tau == G
assert induced_on_K(tau) == [list(r) for r in identity_matrix(ZZ, 10).rows()]
for plane in (P1, P2):
    assert preserves(plane, tau)
assert tau.determinant() == 1
print("  orientation witness tau=-id_U(2)+id: ker(rho), both plane stabilizers, det=1, spinor_R=-1")
print("TYPE-II CERTIFICATE COMPLETE: lifted Levi, exact gluing, kernel 8192 x GL_2, orientation")
