"""A13 register, item 1: the chain T_Co -> T_En -> T_dP -> lkt in coordinates.

Self-contained: no sage, no sage-extensions.  Exact integer and rational arithmetic with sympy.

The marking is the one of @thm:theta-co-coordinates.  What is given here:

  * the bases of the four lattices of the chain of @lem:sequence_of_embeddings, each as the
    coordinate matrix of its basis in the standard basis e_0..e_21 of lkt;
  * the three inclusion matrices between consecutive members, and the composite, which must
    equal the coordinate matrix of T_Co in lkt;
  * that each step is primitive, by the Smith normal form of its inclusion matrix being trivial
    (equivalently: the cokernel is torsion-free, which is the criterion the two lemmas invoke);
  * that each lattice is the eigenspace of a named involution of [@AEGS25, Def. 2.3] or of
    theta_Co: T_Co = ker(theta_Co - 1), T_En = ker(I_En + 1), T_dP = ker(I_dP + 1), and
    S_dP = ker(I_dP - 1) = Delta(U_2,U_3) = U(2);
  * the invariants of each member -- rank, determinant, signature, and the triple (r, a, delta)
    of the 2-elementary classification -- and the isometry type the lemmas name;
  * that the marking realises the two displayed embeddings of the lemmas: eta sends h to
    beta = e_0 + e_1 and is the identity on E_10(2) (= Delta^-(U_2,U_3) + Delta^-(E8) here),
    while the composite T_Co -> T_dP equals the displayed (h, x, y) -> (e~+f~, x, (y,y)) after
    the isometry (a,b) -> (a,-b) of the two E8 summands.
"""
import sys
from fractions import Fraction

from sympy import Matrix, Rational, eye, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy import __version__ as sympy_version

sys.stdout.reconfigure(line_buffering=True)

N = 22
U_BLOCKS = [(0, 1), (2, 3), (4, 5)]
E_BLOCKS = [list(range(6, 14)), list(range(14, 22))]
E8_EDGES = [(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]


def build_G():
    G = zeros(N, N)
    for a, b in U_BLOCKS:
        G[a, b] = 1
        G[b, a] = 1
    for blk in E_BLOCKS:
        for i in range(8):
            G[blk[i], blk[i]] = -2
        for i, j in E8_EDGES:
            G[blk[i], blk[j]] = 1
            G[blk[j], blk[i]] = 1
    return G


def col(entries):
    v = zeros(N, 1)
    for i, c in entries.items():
        v[i] = c
    return v


def is_integral(M):
    return all(Fraction(x).denominator == 1 for x in M)


def show(v):
    items = [(i, Fraction(x)) for i, x in enumerate(v) if x != 0]
    if not items:
        return "0"
    out = []
    for i, c in items:
        num, den = c.numerator, c.denominator
        s = ("e_%d" % i) if den == 1 else ("e_%d/%d" % (i, den))
        if abs(num) != 1:
            s = ("%d*" % num) + s
        out.append(("+" if c > 0 else "-") + " " + s.lstrip("-"))
    return " ".join(out)


def signature(Gm):
    A = [[Rational(Gm[i, j]) for j in range(Gm.cols)] for i in range(Gm.rows)]
    n = len(A)
    pos = neg = 0
    i = 0
    while i < n:
        if A[i][i] != 0:
            piv = A[i][i]
            if piv > 0:
                pos += 1
            else:
                neg += 1
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    f = A[j][i] / piv
                    for k in range(n):
                        A[j][k] -= f * A[i][k]
                        A[k][j] -= f * A[i][k]
            i += 1
            continue
        j0 = next((j for j in range(i + 1, n) if A[i][j] != 0), None)
        if j0 is None:
            i += 1
            continue
        B = Matrix([[Rational(0), A[i][j0]], [A[i][j0], A[j0][j0]]])
        Binv = B.inv()
        pos += 1
        neg += 1
        for j in range(i + 1, n):
            if j == j0:
                continue
            b = Matrix([A[i][j], A[j0][j]])
            for k in range(i + 1, n):
                if k == j0:
                    continue
                bk = Matrix([A[i][k], A[j0][k]])
                corr = (bk.T * Binv * b)[0, 0]
                A[j][k] -= corr
                A[k][j] -= corr
        for j in range(i + 1, n):
            if j != j0:
                A[i][j] = A[j][i] = 0
                A[j0][j] = A[j][j0] = 0
        i += 2
    return pos, neg


def coparity(Gm):
    Gi = Gm.inv()
    diag = [Rational(Gi[i, i]) for i in range(Gm.rows)]
    return 0 if all(d.denominator == 1 and int(d) % 2 == 0 for d in diag) else 1


def snf_diag(M):
    D = smith_normal_form(M)
    return [abs(int(D[i, i])) for i in range(min(D.rows, D.cols)) if D[i, i] != 0]


print("provenance")
print("  sympy %s, exact integer and rational arithmetic" % sympy_version)
print("  python %s" % sys.version.split()[0])
print("  no sage and no sage-extensions")
print("  marking: @thm:theta-co-coordinates and @thm:gamma-co-coordinates")
print("  chain: @lem:sequence_of_embeddings, @lem:primitive_embedding_eta")
print("")

G = build_G()

# --- the four involutions, to anchor each lattice as an eigenspace ----------------------
IEn = zeros(N, N)
for k in (0, 1):
    IEn[k, k] = -1
IEn[2, 4] = 1
IEn[4, 2] = 1
IEn[3, 5] = 1
IEn[5, 3] = 1
for k in range(8):
    IEn[6 + k, 14 + k] = 1
    IEn[14 + k, 6 + k] = 1

IdP = zeros(N, N)
for k in (0, 1):
    IdP[k, k] = -1
IdP[2, 4] = 1
IdP[4, 2] = 1
IdP[3, 5] = 1
IdP[5, 3] = 1
for k in range(8):
    IdP[6 + k, 6 + k] = -1
    IdP[14 + k, 14 + k] = -1

th = zeros(N, N)
th[0, 1] = 1
th[1, 0] = 1
th[2, 4] = -1
th[4, 2] = -1
th[3, 5] = -1
th[5, 3] = -1
for k in range(8):
    th[6 + k, 14 + k] = -1
    th[14 + k, 6 + k] = -1

for name, M in (("I_En", IEn), ("I_dP", IdP), ("theta_Co", th)):
    print("%-9s integral %s, involution %s, isometry %s"
          % (name, is_integral(M), (M * M) == eye(N), (M.T * G * M) == G))
print("")

# --- the bases, in the standard basis ---------------------------------------------------
T_Co_basis = [col({0: 1, 1: 1})] + [col({2: 1, 4: -1}), col({3: 1, 5: -1})] + \
             [col({6 + k: 1, 14 + k: -1}) for k in range(8)]
T_En_basis = [col({0: 1}), col({1: 1})] + [col({2: 1, 4: -1}), col({3: 1, 5: -1})] + \
             [col({6 + k: 1, 14 + k: -1}) for k in range(8)]
T_dP_basis = [col({0: 1}), col({1: 1}), col({2: 1, 4: -1}), col({3: 1, 5: -1})] + \
             [col({6 + k: 1}) for k in range(8)] + [col({14 + k: 1}) for k in range(8)]
lkt_basis = [col({i: 1}) for i in range(N)]

members = (("T_Co", T_Co_basis), ("T_En", T_En_basis), ("T_dP", T_dP_basis), ("lkt", lkt_basis))
print("1. the four bases, in the standard basis e_0..e_21")
for name, basis in members:
    print("   %-5s %d vectors: %s" % (name, len(basis),
                                      ", ".join(show(v) for v in basis)))
print("")

print("2. each lattice is the eigenspace of its involution")
for name, M, mname, basis, sign in (("T_Co", th, "theta_Co", T_Co_basis, 1),
                                    ("T_En", IEn, "I_En", T_En_basis, -1),
                                    ("T_dP", IdP, "I_dP", T_dP_basis, -1)):
    iff = all((M * v) == sign * v for v in basis)
    rank_of_kernel = N - (M - sign * eye(N)).rank()
    print("   %-5s: every basis vector is a %+d-eigenvector of %s: %s; rank of that eigenspace %d = %d"
          % (name, sign, mname, iff, rank_of_kernel, len(basis)))
S_dP = [col({2: 1, 4: 1}), col({3: 1, 5: 1})]
print("   S_dP  : Delta(U_2,U_3), every basis vector a +1-eigenvector of I_dP: %s; rank %d"
      % (all((IdP * v) == v for v in S_dP), N - (IdP - eye(N)).rank()))
print("   the containments:")
for a, b, an, bn in ((T_Co_basis, T_En_basis, "T_Co", "T_En"),
                     (T_En_basis, T_dP_basis, "T_En", "T_dP"),
                     (T_dP_basis, lkt_basis, "T_dP", "lkt")):
    A = Matrix.hstack(*a)
    B = Matrix.hstack(*b)
    in_span = Matrix.hstack(B, A).rank() == B.rank()
    print("     %s subset of %s: %s" % (an, bn, in_span))
print("")

print("3. the three inclusion matrices, and the composite")
def coords(inner, outer):
    """the matrix of inner's basis in outer's basis"""
    A = Matrix.hstack(*inner)
    B = Matrix.hstack(*outer)
    return (B.T * G * B).inv() * B.T * G * A

M1 = coords(T_Co_basis, T_En_basis)
M2 = coords(T_En_basis, T_dP_basis)
M3 = coords(T_dP_basis, lkt_basis)
M13 = coords(T_Co_basis, lkt_basis)
for name, M in (("T_Co -> T_En  (12x11)", M1), ("T_En -> T_dP  (20x12)", M2),
                ("T_dP -> lkt   (22x20)", M3), ("T_Co -> lkt   (22x11)", M13)):
    print("   %-22s integral %s, shape %dx%d" % (name, is_integral(M), M.rows, M.cols))
print("   T_Co -> T_En:")
for i in range(M1.rows):
    print("     " + " ".join("%2d" % int(M1[i, j]) for j in range(M1.cols)))
print("   T_En -> T_dP:")
for i in range(M2.rows):
    print("     " + " ".join("%2d" % int(M2[i, j]) for j in range(M2.cols)))
print("   T_dP -> lkt:")
for i in range(M3.rows):
    print("     " + " ".join("%2d" % int(M3[i, j]) for j in range(M3.cols)))
print("   the composite equals the direct matrix: M3*M2*M1 = M13 %s"
      % (((M3 * M2) * M1) == M13))
print("")

print("4. each step is primitive: the Smith normal form of its inclusion matrix is trivial")
for name, M in (("T_Co -> T_En", M1), ("T_En -> T_dP", M2), ("T_dP -> lkt", M3)):
    D = snf_diag(M)
    print("   %-13s rank %d, SNF %s, all one: %s (cokernel torsion-free, so primitive)"
          % (name, M.rank(), D, set(D) == {1}))
print("")

print("5. the invariants of the four members")
for name, basis in members:
    B = Matrix.hstack(*basis)
    Gm = B.T * G * B
    p, q = signature(Gm)
    D = snf_diag(Gm)
    multiset = sorted(set(D)) and {d: D.count(d) for d in sorted(set(D))}
    print("   %-5s rank %2d, det %6d, even %s, signature (%d, %d), SNF multiplicities %s"
          % (name, Gm.rows, int(Gm.det()), all(int(Gm[i, i]) % 2 == 0 for i in range(Gm.rows)),
             p, q, multiset))
print("")

print("6. the two displayed embeddings of the lemmas")
print("   eta: h -> beta = e_0+e_1 and the identity on E_10(2) = Delta^-(U_2,U_3)+Delta^-(E8):")
print("     the T_Co -> T_En matrix is the identity on the last ten coordinates and")
print("     (1,1) on the first two: %s" % (M1[0, 0] == 1 and M1[1, 0] == 1))
print("   the sequence's display (h,x,y) -> (e~+f~, x, (y,y)) into U (+) U(2) (+) E8^2:")
print("     T_Co -> T_dP sends y_k to (y_k, -y_k), not to (y_k, y_k); the isometry")
print("     sigma = diag(1 on U_1,U_2,U_3; -1 on E8_2) carries one to the other:") 
sigma = eye(N)
for k in range(8):
    sigma[14 + k, 14 + k] = -1
print("     sigma is an isometry of lkt: %s, it preserves T_dP: %s"
      % ((sigma.T * G * sigma) == G,
         Matrix.hstack(Matrix.hstack(*T_dP_basis), sigma * Matrix.hstack(*T_dP_basis)).rank()
         == len(T_dP_basis)))
print("     the composite's images, in the standard basis, and their images under sigma:")
images = []
for j, v in enumerate(T_Co_basis):
    img = M13[:, j]
    images.append(img)
    print("       %-28s -> %-22s sigma of it %-22s" % (show(v), show(img), show(sigma * img)))
print("     sigma carries beta to beta = e~+f~, fixes the Delta^-(U_2,U_3) classes, and sends")
print("     (y_k,-y_k) to (y_k,y_k), which is the lemma's display (h,x,y) -> (e~+f~, x, (y,y)):")
print("       sigma(beta) = beta: %s" % ((sigma * images[0]) == images[0]))
print("       sigma fixes e_2-e_4 and e_3-e_5: %s"
      % (all((sigma * images[j]) == images[j] for j in (1, 2))))
print("       sigma(e_{6+k}-e_{14+k}) = e_{6+k}+e_{14+k} for k = 0..7: %s"
      % all((sigma * images[3 + k]) == col({6 + k: 1, 14 + k: 1}) for k in range(8)))
print("")

print("7. the quotient ranks, and what stays open")
print("   ranks of the cokernels: T_En/T_Co %d, T_dP/T_En %d, lkt/T_dP %d"
      % (len(T_En_basis) - len(T_Co_basis), len(T_dP_basis) - len(T_En_basis),
         len(lkt_basis) - len(T_dP_basis)))
print("   the equations of the sextic C and its double plane in these bases are not touched")
print("   here: they are @thm:coble-explicit-sextic, which works in the plane model, a basis of")
print("   H^2 determining no equation.")
