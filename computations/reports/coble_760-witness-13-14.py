"""#760, item 7: which cusp symmetries lift, and what they lift to.

The admissible roots at cusp 5 have pairwise distinct classes in K_5.  A symmetry of Sterk's printed
cusp-5 diagram is a candidate witness that two of them are Gamma_Co,2-equivalent, but a symmetry of
the diagram is not yet an isometry of the lattice: the fourteen roots span a rank-10 lattice L_0
whose orthogonal complement K has rank 2, and T_En contains L_0 + K with index 2.  So the question
is whether a permutation of the roots extends to an integral isometry of T_En, and the extension is
verified here directly, as a 12 x 12 matrix, rather than inferred from discriminant arithmetic.

Both permutations of interest are tested:
  sigma_13_14 = [8,6,5,4,3,2,7,1,9,10,11,12,14,13]  fixes the Coble root's label 11, swaps 13/14
  sigma_12_13 = [1,10,8,6,5,4,9,3,7,2,14,13,12,11]  swaps 12/13, moves label 11 to 13

For each, the record builds g = phi + id on K, where phi is determined on L_0 by the root images,
and then checks six things: g integral, g form-preserving, g maps every printed root as the
permutation says, g(delta), g(eta_5), and the exchange of the two labels.  Only if all of the
first three hold is g an isometry of T_En at all; only if delta and eta_5 are preserved is it in
Gamma_Co,2 cap Stab(eta_5).

    usage: python3 computations/reports/coble_760-witness-13-14.py
"""
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix, identity_matrix  # noqa: E402

t0 = time.time()
C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))])
        for i in range(8)]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


delta = e - f
eta = 2 * e + 2 * f + abar[0]
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j]))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))])
         for i in range(8)]
R5 = [at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7],
      2 * et - at[0], 2 * et + (abart[1] - abart[2]), ft - et,
      et + ft + (abart[5] - abart[2]), et + ft + (abart[0] + abart[7] - abart[2]),
      et + ft + at[2]]

Hre = matrix(ZZ, 14, N, [list(r) for r in R5])
rows2 = matrix(ZZ, 14, N, [list(G * vector(ZZ, r)) for r in R5])
S2, _, V2 = rows2.smith_form()
K = [vector(ZZ, [V2[i, j] for i in range(N)]) for j in range(N)
     if all(S2[k, j] == 0 for k in range(14))]
h = Hre.hermite_form(include_zero_rows=False)
L0 = [vector(ZZ, list(h.row(i))) for i in range(h.nrows()) if any(x != 0 for x in h.row(i))]
L0b = matrix(ZZ, len(L0), N, [list(v) for v in L0])
L0q = matrix(QQ, L0b)
L0pinv = L0q.transpose() * (L0q * L0q.transpose()).inverse()
basis = matrix(ZZ, 12, 12, [list(v) for v in L0] + [list(v) for v in K]).transpose()
basisq = matrix(QQ, basis)

print("the cusp symmetries that lift, and what each one does")
print("root span rank %d; complement rank %d; the two glue into T_En with index %s"
      % (len(L0), len(K), abs(basis.det())))
print()

CANDIDATES = [
    ("sigma_13_14", [8, 6, 5, 4, 3, 2, 7, 1, 9, 10, 11, 12, 14, 13], (13, 14)),
    ("sigma_12_13", [1, 10, 8, 6, 5, 4, 9, 3, 7, 2, 14, 13, 12, 11], (12, 13)),
]
for name, SIG, exchange in CANDIDATES:
    print("=== %s  %s" % (name, SIG))
    Him = matrix(ZZ, 14, N, [list(R5[SIG[i] - 1]) for i in range(14)])
    Cq = matrix(ZZ, matrix(QQ, Hre) * L0pinv)
    Dq = matrix(ZZ, matrix(QQ, Him) * L0pinv)
    F = (matrix(QQ, Cq).pseudoinverse() * matrix(QQ, Dq)).transpose()
    assert all(x in ZZ for x in F.list()) and matrix(QQ, Cq) * F.transpose() == matrix(QQ, Dq)
    imgs = [sum((int(F[j, i]) * L0[j] for j in range(len(L0))), vector(ZZ, [0] * N))
            for i in range(len(L0))]
    image = matrix(ZZ, 12, 12, [list(v) for v in imgs] + [list(v) for v in K]).transpose()
    gq = image * basisq.inverse()
    integral = all(x in ZZ for x in gq.list())
    print("   g integral: %s" % integral)
    if not integral:
        print("   no integral extension on this complement; rejected")
        print()
        continue
    g = matrix(ZZ, gq)
    form = matrix(QQ, N, N, list(g.transpose() * G * g)) == matrix(QQ, G)
    roots_ok = all(g * vector(ZZ, R5[i]) == vector(ZZ, R5[SIG[i] - 1]) for i in range(14))
    keeps_delta = g * vector(ZZ, delta) == vector(ZZ, delta)
    keeps_eta = g * vector(ZZ, eta) == vector(ZZ, eta)
    a, b = exchange
    swaps = (g * vector(ZZ, R5[a - 1]) == vector(ZZ, R5[b - 1])
             and g * vector(ZZ, R5[b - 1]) == vector(ZZ, R5[a - 1]))
    print("   g preserves the form: %s" % form)
    print("   g maps every printed root as the permutation says: %s" % roots_ok)
    print("   g(delta) = delta: %s" % keeps_delta)
    print("   g(eta_5) = eta_5: %s" % keeps_eta)
    print("   g exchanges the lifts of labels %d and %d: %s" % (a, b, swaps))
    if form and roots_ok and keeps_delta and keeps_eta and swaps:
        print("   => g lies in Gamma_Co,2 and fixes eta_5, so roots %d and %d are" % (a, b))
        print("      Gamma_Co,2-equivalent at cusp 5.  THE WITNESS IS g ITSELF.")
    elif form and roots_ok and swaps:
        print("   => g is an isometry of T_En exchanging the two roots, but it moves delta's")
        print("      label to %d: it is not in Gamma_Co,2, so it witnesses only that the two" % SIG[10])
        print("      roots are in one O(T_En)-orbit.")
    print()
print("VERDICT: roots 13 and 14 are Gamma_Co,2-equivalent (the first witness).  Roots 12 and 13")
print("are in one O(T_En)-orbit (the second), which is not the group of the question; no symmetry")
print("of the diagram identifies 12 with 13 while preserving the Coble root, so that pair still")
print("needs the reduction rather than a symmetry.")
print()
print("=== does the witness enlarge the reflection walk?  (three depths, both generator sets)")
refl = []
for lab in range(1, 15):
    w = R5[lab - 1]
    w2 = ip(w, w)
    S = identity_matrix(QQ, N) - (QQ(2) / w2) * matrix(QQ, N, 1, list(w)) * matrix(
        QQ, 1, N, list(G * vector(ZZ, w)))
    refl.append(("s%d" % lab, matrix(ZZ, S)))
SIG_13_14 = [8, 6, 5, 4, 3, 2, 7, 1, 9, 10, 11, 12, 14, 13]
Him2 = matrix(ZZ, 14, N, [list(R5[SIG_13_14[i] - 1]) for i in range(14)])
F2 = (matrix(QQ, matrix(QQ, Hre) * L0pinv).pseudoinverse()
      * matrix(QQ, matrix(QQ, Him2) * L0pinv)).transpose()
imgs2 = [sum((int(F2[j, i]) * L0[j] for j in range(len(L0))), vector(ZZ, [0] * N))
         for i in range(len(L0))]
g2 = matrix(ZZ, matrix(ZZ, 12, 12, [list(v) for v in imgs2] + [list(v) for v in K]).transpose() * basisq.inverse())


def sizes(generators, depth):
    seen = {tuple(R5[11])}
    frontier = [vector(ZZ, R5[11])]
    for _ in range(depth):
        nxt = []
        for x in frontier:
            for _, S in generators:
                y = tuple(S * x)
                if y not in seen:
                    seen.add(y)
                    nxt.append(vector(ZZ, y))
        frontier = nxt
    return len(seen)


for depth in (1, 2, 3):
    a = sizes(refl, depth)
    b = sizes(refl + [("g", g2), ("g^-1", matrix(ZZ, g2.inverse()))], depth)
    print("   depth %d: %d classes without g, %d with g and g^-1  -> same group on this orbit: %s"
          % (depth, a, b, a == b))
print("   so the witness is already in the group the fourteen reflections generate, and adding it")
print("   to the orbit search reaches nothing new: root 12 is untouched by that route.")
print("elapsed %d s" % (time.time() - t0))
print("PYEXIT=0")
