"""#760, item 7: why the marked pair's invariant cannot be the complement of <delta, eta, r>.

The question is whether two of roots 12, 13, 14 at cusp 5 are Gamma_Co,2-equivalent, and the
obvious invariant to compare is the orthogonal complement in T_En of the triple they determine.
This record computes it and shows the invariant is empty: eta_5 is isotropic, so <delta, eta_5, r>
is a degenerate subspace, its orthogonal complement is degenerate too, and the isometry decision
on a degenerate Gram matrix is vacuous (it returns True for every pair).

What the invariant has to be is the *pair* (K_5, r) --- the boundary lattice with its marked root
--- whose isometry class is the O(K_5)-orbit invariant, and whose Gamma_Co,2-refinement needs the
subgroup.  The complement in K_5 of the root alone is the meaningful rank-9 object, and it was
computed in coble_760-isometry-decision-probe-run.txt (all three isometric).

    usage: PYTHONPATH=<repo>/.scratch/sage-extensions/src python \\
               <repo>/computations/reports/coble_760-marked-pair-invariant.py
"""
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

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

print("the marked pair's invariant, and why the triple's complement is not it")
print("delta^2 = %d, eta^2 = %d (isotropic), (delta,eta) = %d" % (ip(delta, delta), ip(eta, eta), ip(delta, eta)))
print()
lib = Lattices(ZZ)
for lab in (12, 13, 14):
    r = R5[lab - 1]
    rows = [list(G * vector(ZZ, v)) for v in (delta, eta, r)]
    S, _, V = matrix(ZZ, 3, N, rows).smith_form()
    ker = []
    for j in range(N):
        if all(S[i, j] == 0 for i in range(3)):
            ker.append(vector(ZZ, [V[i, j] for i in range(N)]))
    Gm = matrix(ZZ, 9, 9, lambda i, j: ip(ker[i], ker[j]))
    print("label %2d: complement of <delta, eta_5, r> has rank %d, determinant %d"
          % (lab, Gm.nrows(), Gm.det()))
print()
objs = {}
for lab in (12, 13, 14):
    r = R5[lab - 1]
    rows = [list(G * vector(ZZ, v)) for v in (delta, eta, r)]
    S, _, V = matrix(ZZ, 3, N, rows).smith_form()
    ker = [vector(ZZ, [V[i, j] for i in range(N)]) for j in range(N)
           if all(S[i, j] == 0 for i in range(3))]
    objs[lab] = lib([list(row) for row in
                     matrix(ZZ, 9, 9, lambda i, j: ip(ker[i], ker[j])).rows()])
for a, b in ((12, 13), (12, 14), (13, 14)):
    print("labels %d,%d: is_isometric_to on the degenerate complement -> %s"
          % (a, b, objs[a].is_isometric_to(objs[b])))
print()
print("a determinant of 0 says the subspace is degenerate, because eta_5 is isotropic: the")
print("decision above compares degenerate forms and carries no information.  The invariant that")
print("does carry information is the complement in K_5 of the root alone, or the pair (K_5, r)")
print("itself, and the pair's Gamma_Co,2-refinement is the reduction the library lacks.")
print("elapsed %d s" % (time.time() - t0))
print("PYEXIT=0")
