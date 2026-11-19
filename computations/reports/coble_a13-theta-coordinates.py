"""A13, item 1: the sign involution theta_Co of the Coble primitive embedding, in coordinates.

Self-contained: no sage, no sage-extensions.  Everything is exact integer / rational
arithmetic on 22x22 matrices with sympy.

The model, and where it comes from.  L = lkt = U^3 + E8^2 in the standard basis with the blocks
of @prop:coble-enriques-ambient-isometry:

    U_1 = <e_0, e_1>,  U_2 = <e_2, e_3>,  U_3 = <e_4, e_5>,
    E8_1 = <e_6..e_13>,  E8_2 = <e_14..e_21>,

the E8 summands negative definite with Gram -Cartan(E8), so that L is even, unimodular, of
signature (3, 19).  I_En is the Enriques involution of [@AEGS25, Def. 2.3, printed p. 586],

    I_En: (v, u, u', e, e') |-> (-v, u', u, e', e),

in the block form L = U_1 + U_2 + U_3 + E8_1 + E8_2 of the same source.  With alpha = e_0 - e_1
and w = s_alpha the reflection in alpha, J_Co = w I_En is the involution of
@prop:coble-enriques-ambient-isometry, whose invariant lattice is S_Co = ker(J_Co - 1).

The object computed here is theta_Co = -J_Co.  J_Co is +1 on S_Co and -1 on T_Co = S_Co^perp, so
theta_Co is -1 on S_Co and +1 on T_Co: that is the sign involution of @prop:theta-co-exists,
which that proposition defines as the isometry of lkt equal to -id on S_Co and id on T_Co.  The
covering involution of the Coble K3, the other involution of the same pair, is I_Co = J_Co = -theta_Co,
as @prop:coble-cover-marking records.

What this transcript certifies: the matrix, its integrality, its form preservation, its order, the
eigenspace bases with their Gram matrices and invariants, the index of S_Co + T_Co in lkt, the
Smith normal forms and coparities of both eigenspaces, the images of the marked classes, and the
impossibility of the reversed sign assignment and of one nearby perturbation.  What it does not
certify, and what is Nikulin's classification instead of a computation, is the identification of
the two eigenspace types with <2> + <-2>^10 and <2> + U(2) + E8(2).
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


def vec(entries):
    v = zeros(N, 1)
    for i, c in entries.items():
        v[i] = c
    return v


def is_integral(M):
    return all(Fraction(x).denominator == 1 for x in M)


def signature(Gm):
    """Exact inertia of a rational symmetric matrix, by congruence with 1x1 and 2x2 pivots."""
    A = [[Rational(Gm[i, j]) for j in range(Gm.cols)] for i in range(Gm.rows)]
    n = len(A)
    pos = neg = zer = 0
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
        # no 1x1 pivot: look for a hyperbolic 2x2 pivot
        j0 = None
        for j in range(i + 1, n):
            if A[i][j] != 0:
                j0 = j
                break
        if j0 is None:
            zer += 1
            i += 1
            continue
        c = A[i][j0]
        d = A[j0][j0]
        B = Matrix([[Rational(0), c], [c, d]])
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
    return pos, neg, zer


def is_even(Gm):
    return all(int(Gm[i, i]) % 2 == 0 for i in range(Gm.rows))


def snf_diag(Gm):
    D = smith_normal_form(Gm)
    return [abs(int(D[i, i])) for i in range(min(D.rows, D.cols)) if D[i, i] != 0]


def coparity(Gm):
    """delta = 0 iff q_S takes values in Z/2Z, i.e. iff every diagonal entry of G^{-1} is even."""
    Gi = Gm.inv()
    diag = [Rational(Gi[i, i]) for i in range(Gm.rows)]
    return 0 if all(d.denominator == 1 and int(d) % 2 == 0 for d in diag) else 1


def report(name, Gm):
    p, q, z = signature(Gm)
    if int(Gm.det()) == 0:
        print("     %-6s rank %d, det 0 -- DEGENERATE, signature (%d, %d, %d zero): no"
              " discriminant form, so not a candidate for either eigenspace"
              % (name, Gm.rows, p, q, z))
        return
    D = snf_diag(Gm)
    print("     %-6s rank %d, det %s, even %s, signature (%d, %d), SNF %s, coparity delta = %d"
          % (name, Gm.rows, int(Gm.det()), is_even(Gm), p, q,
             "[" + ", ".join(str(x) for x in D) + "]", coparity(Gm)))


print("provenance")
print("  sympy %s, exact integer and rational arithmetic, 22x22 matrices" % sympy_version)
print("  python %s" % sys.version.split()[0])
print("  no sage and no sage-extensions: every quantity below is an integer or a rational")
print("  model: writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md,")
print("         @prop:coble-enriques-ambient-isometry (blocks, J_Co, S_Co) and @prop:theta-co-exists")
print("")

G = build_G()
print("1. L = U^3 + E8(-1)^2 in the standard basis e_0, ..., e_21")
print("   blocks: U_1 = <e_0,e_1>, U_2 = <e_2,e_3>, U_3 = <e_4,e_5>,")
print("           E8_1 = <e_6..e_13>, E8_2 = <e_14..e_21>, Gram = -Cartan(E8) (Bourbaki numbering)")
report("L", G)
print("   the Gram matrix G:")
for i in range(N):
    print("    %2d: %s" % (i, " ".join("%2d" % int(G[i, j]) for j in range(N))))
print("")

print("2. the Enriques involution I_En of [@AEGS25, Def. 2.3, printed p. 586]")
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
print("   integral %s, I_En^2 = 1 %s, I_En^T G I_En = G %s, det %d"
      % (is_integral(IEn), (IEn * IEn) == eye(N), (IEn.T * G * IEn) == G, int(IEn.det())))
print("   eigenspace ranks: +1 -> %d, -1 -> %d  (S_En = U(2)+E8(2) has rank 10, T_En rank 12)"
      % (N - (IEn - eye(N)).rank(), N - (IEn + eye(N)).rank()))
print("")

print("3. alpha = e_0 - e_1, beta = e_0 + e_1, and the reflection w = s_alpha")
alpha = vec({0: 1, 1: -1})
beta = vec({0: 1, 1: 1})
Gab = Matrix([[ (alpha.T * G * alpha)[0, 0], (alpha.T * G * beta)[0, 0]],
              [ (beta.T * G * alpha)[0, 0], (beta.T * G * beta)[0, 0]]])
print("   alpha^2 = %d, beta^2 = %d, alpha.beta = %d, det of their Gram matrix %d,"
      % (int(Gab[0, 0]), int(Gab[1, 1]), int(Gab[0, 1]), int(Gab.det())))
print("   so <alpha,beta> = diag(-2,2) is a sublattice of index 2 in U_1; both are primitive in L")
q_alpha = (alpha.T * G * alpha)[0, 0]
w = eye(N) - Rational(2, 1) / q_alpha * alpha * (G * alpha).T
print("   w = 1 - (2/alpha^2) alpha (G alpha)^T, alpha^2 = %d: integral %s, w^2 = 1 %s, w^T G w = G %s, det %d"
      % (int(q_alpha), is_integral(w), (w * w) == eye(N), (w.T * G * w) == G, int(w.det())))
print("   w(alpha) = -alpha %s, w(beta) = beta %s"
      % (list(w * alpha) == [-x for x in alpha], (w * beta) == beta))
print("")

print("4. J_Co = w . I_En and theta_Co = -J_Co")
J = w * IEn
th = -J
for name, M in (("J_Co", J), ("theta_Co", th)):
    print("   %-8s integral %s, involution %s, isometry %s, det %d, trace %d"
          % (name, is_integral(M), (M * M) == eye(N), (M.T * G * M) == G,
             int(M.det()), int(M.trace())))
print("   theta_Co = -J_Co %s" % ((th + J) == zeros(N, N)))
print("   theta_Co is a signed permutation matrix %s"
      % all(sum(1 for x in th[:, j] if x != 0) == 1 for j in range(N)))
print("")

print("5. the matrix of theta_Co in the standard basis e_0, ..., e_21")
print("   entry (i,j) = coefficient of e_i in theta_Co(e_j)")
for i in range(N):
    print("    " + " ".join("%2d" % int(th[i, j]) for j in range(N)))
print("")

print("6. the two eigenspace bases")
plus = [beta, vec({2: 1, 4: -1}), vec({3: 1, 5: -1})] + [vec({6 + k: 1, 14 + k: -1}) for k in range(8)]
minus = [alpha, vec({2: 1, 4: 1}), vec({3: 1, 5: 1})] + [vec({6 + k: 1, 14 + k: 1}) for k in range(8)]
print("   (+1)-part: beta = e_0+e_1, e_2-e_4, e_3-e_5, e_{6+k}-e_{14+k} (k = 0..7)")
print("     each is fixed by theta_Co %s" % all((th * v) == v for v in plus))
print("   (-1)-part: alpha = e_0-e_1, e_2+e_4, e_3+e_5, e_{6+k}+e_{14+k} (k = 0..7)")
print("     each is negated by theta_Co %s"
      % all((th * v) == (-1) * v for v in minus))
print("   rank(theta_Co - 1) = %d and rank(theta_Co + 1) = %d, so both eigenspaces have rank 11"
      % ((th - eye(N)).rank(), (th + eye(N)).rank()))
full = Matrix.hstack(*(plus + minus))
print("   the 22 announced vectors are independent and span a sublattice of index %d in L"
      % abs(int(full.det())))
print("")


def gram(vs):
    k = len(vs)
    Gm = zeros(k, k)
    for i in range(k):
        for j in range(k):
            Gm[i, j] = (vs[i].T * G * vs[j])[0, 0]
    return Gm


GS = gram(minus)
GT = gram(plus)
print("7. the Gram matrices of the two eigenspaces")
print("   S_Co = ker(theta_Co + 1), basis alpha, e_2+e_4, e_3+e_5, e_{6+k}+e_{14+k}:")
print("     <alpha>    %s" % [[int(GS[0, 0])]])
print("     U(2)       %s" % [[int(GS[i, j]) for j in (1, 2)] for i in (1, 2)])
print("     E8(-1)(2)  diag %s" % [int(GS[3 + k, 3 + k]) for k in range(8)])
report("S_Co", GS)
print("     the three blocks are pairwise orthogonal %s"
      % all(GS[i, j] == 0 for i in range(11) for j in range(11)
            if ((i == 0) != (j == 0)) or ((i in (1, 2)) != (j in (1, 2)))))
print("   T_Co = ker(theta_Co - 1), basis beta, e_2-e_4, e_3-e_5, e_{6+k}-e_{14+k}:")
print("     <beta>     %s" % [[int(GT[0, 0])]])
print("     U(2)       %s" % [[int(GT[i, j]) for j in (1, 2)] for i in (1, 2)])
print("     E8(-1)(2)  diag %s" % [int(GT[3 + k, 3 + k]) for k in range(8)])
report("T_Co", GT)
print("     the three blocks are pairwise orthogonal %s"
      % all(GT[i, j] == 0 for i in range(11) for j in range(11)
            if ((i == 0) != (j == 0)) or ((i in (1, 2)) != (j in (1, 2)))))
print("")

print("8. the index, the gluing, and the two invariants that decide the types")
idx = abs(int(full.det()))
print("   [L : S_Co + T_Co] = %d = 2^%d" % (idx, idx.bit_length() - 1))
print("   |det S_Co| * |det T_Co| = %d = %d^2 %s"
      % (abs(int(GS.det())) * abs(int(GT.det())), idx,
         abs(int(GS.det())) * abs(int(GT.det())) == idx * idx))
print("   thus S_Co is (r,a,delta) = (11, 11, %d) of signature %s, and T_Co is (11, 11, %d)"
      " of signature %s:" % (coparity(GS), signature(GS)[:2], coparity(GT), signature(GT)[:2]))
print("   by [@Nik80, Thm. 3.6.2, printed p. 144] the first is <2> + <-2>^10 = I_{1,10}(2) and the")
print("   second is <2> + U(2) + E8(2), the two lattices of @prop:coble-invariant-lattice and")
print("   @prop:theta-co-exists.")
print("")

print("9. the marked classes of the Coble tuple in this marking")
H = vec({2: 1, 3: 1, 4: 1, 5: 1})
print("   H = e_2+e_3+e_4+e_5, the sum of the hyperbolic basis e = e_2+e_4, f = e_3+e_5 of")
print("   the summand Delta(U_2,U_3) = U(2) of S_Co:")
print("     H^2 = %d, alpha^2 = %d, H.alpha = %d"
      % (int((H.T * G * H)[0, 0]), int((alpha.T * G * alpha)[0, 0]),
         int((H.T * G * alpha)[0, 0])))
print("     theta_Co(H) = -H %s, theta_Co(alpha) = -alpha %s"
      % ((th * H) == (-1) * H, (th * alpha) == (-1) * alpha))
print("     theta_Co negates the summand Delta(U_2,U_3): theta_Co(e_2+e_4) = -(e_2+e_4) %s"
      % ((th * vec({2: 1, 4: 1})) == (-1) * vec({2: 1, 4: 1})))
print("")

print("10. the reversed sign assignment, and one nearby perturbation, both fail")
print("    J_Co = -theta_Co has the same two eigenspaces with the signs reversed; an isometry")
print("    g with g theta_Co g^-1 = J_Co would carry the (+1)-eigenspace of theta_Co, of")
print("    signature %s, to that of J_Co, of signature %s, and an isometry preserves"
      % (signature(GT)[:2], signature(GS)[:2]))
print("    signatures, so no such g exists: theta_Co and J_Co are not conjugate, and the sign")
print("    is not a choice of marking.")
print("    I_En alone has (+1)-rank %d, not 11." % (N - (IEn - eye(N)).rank()))
pert = th.copy()
pert[0, 0], pert[0, 1] = 0, -1
pert[1, 0], pert[1, 1] = -1, 0
print("    keep everything and change the U_1 block of theta_Co from the swap e_0<->e_1 to")
print("    its negative -swap (still an integral isometry of order two, still of rank 11 each):")
print("      integral %s, involution %s, isometry %s"
      % (is_integral(pert), (pert * pert) == eye(N), (pert.T * G * pert) == G))
print("      eigenspace ranks +1 -> %d, -1 -> %d"
      % (N - (pert - eye(N)).rank(), N - (pert + eye(N)).rank()))
print("      its (+1)-eigenspace is spanned by alpha, e_2-e_4, e_3-e_5, e_{6+k}-e_{14+k}:")
report("pert +", gram([alpha, vec({2: 1, 4: -1}), vec({3: 1, 5: -1})]
                     + [vec({6 + k: 1, 14 + k: -1}) for k in range(8)]))
print("      its (-1)-eigenspace is spanned by beta, e_2+e_4, e_3+e_5, e_{6+k}+e_{14+k}:")
report("pert -", gram([beta, vec({2: 1, 4: 1}), vec({3: 1, 5: 1})]
                     + [vec({6 + k: 1, 14 + k: 1}) for k in range(8)]))
print("      so the perturbation exchanges the two eigenspace types: its (+1)-eigenspace is")
print("      <alpha>+U(2)+E8(2), of signature (1,10), which is S_Co and not T_Co, and it")
print("      fixes alpha instead of negating it.  It fails the eigenspace claim.")
print("")

print("11. what is not computed here")
print("    the isometry classes of the two eigenspaces are decided by [@Nik80, Thm. 3.6.2,")
print("    printed p. 144] from the (r, a, delta) and the signature printed above, not by this")
print("    transcript; the polarization classes h_Co and h_En and the roots of the (18,0,0)_1")
print("    diagram in this basis are A13's second and third items and are not touched here.")
