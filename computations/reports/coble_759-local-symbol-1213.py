"""#759: the 2-adic genus symbol of the rank-8 complement.

The pair (12,13) is down to one datum: whether O(L) -> O(q_L) is surjective for the complement L,
which Nikulin, Integral symmetric bilinear forms and some of their applications, Theorem 1.14.2
supplies from a 2-adic condition.  Its case b) applies here, because rg T = 8 = l(A_2); the
condition asks the 2-adic lattice to be U^{(2)}(2^a) + T' or V^{(2)}(2^a) + T' with 0 <= a <= 1.

This record computes the 2-adic symbol, which is the datum that condition is stated in.
Sage's own route does it: IntegralLattice(G).genus() -- note the module, sage.modules.
free_quadratic_module_integer_symmetric; QuadraticForm has no genus in this build, and the
library's LocalGenusSymbol requires the Jordan blocks as input.

For both complements the answer is the same:

    Signature: (1, 7)
    Genus symbol at 2: [2^8]_2

one Jordan block, rank 8, level 2, oddity 2.  Nikulin's condition needs an orthogonal summand
U^{(2)}(2^a) or V^{(2)}(2^a) of rank 2 at level 2^a, a in {0,1}; comparing that with a single
rank-8 block at level 2 turns on the level and oddity dictionary, which this record prints but
does not interpret.  So the condition is not discharged here, and nothing is claimed either way.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
      computations/reports/coble_759-local-symbol-1213.py

Transcript: coble_759-local-symbol-1213-run.txt.  Sage in the shared runtime.
"""
import sys

sys.stdout.reconfigure(line_buffering=True)

from sage.all import QQ, ZZ, matrix, vector, block_diagonal_matrix, CartanMatrix
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

C = CartanMatrix(["E", 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C); N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(x) for x in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


delta = e - f
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j])); Gti = Gt.inverse()
abart = [vector(ZZ, [int(x) for x in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))]) for i in range(8)]
eta = 2 * e + 2 * f + abar[0]
ROOTS = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7], 2 * et - at[0],
          2 * et + (abart[1] - abart[2]), ft - et, et + ft + (abart[5] - abart[2]),
          et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]])
S = matrix(ZZ, [vector(ZZ, r) for r in ROOTS]).saturation()
GS = matrix(ZZ, 10, 10, lambda i, j: ip(S[i], S[j]))
Scols = matrix(QQ, S).transpose()


def complement_gram(r):
    rv, dv = vector(ZZ, r), vector(ZZ, delta)
    cP = Scols.solve_right(vector(QQ, rv)); cD = Scols.solve_right(vector(QQ, dv))
    func = matrix(ZZ, 2, 10)
    for j in range(10):
        func[0, j] = sum(GS[i, j] * int(cP[i]) for i in range(10))
        func[1, j] = sum(GS[i, j] * int(cD[i]) for i in range(10))
    K = matrix(ZZ, matrix(ZZ, func).right_kernel_matrix()).saturation()
    return matrix(ZZ, 8, 8, lambda i, j: sum(int(K[i][a]) * GS[a, b] * int(K[j][b])
                                             for a in range(10) for b in range(10)))


print("the 2-adic genus symbol of the rank-8 complement, for the two roots")
for lab, r in ((12, ROOTS[11]), (13, ROOTS[12])):
    GL = complement_gram(r)
    print()
    print("  label %d: det %d, all entries even: %s"
          % (lab, GL.det(), all(GL[i, j] % 2 == 0 for i in range(8) for j in range(8))))
    lat = IntegralLattice(GL)
    print("  %s" % (lat.genus(),).__str__().replace("\n", "\n  "))
print()
print("Both complements give the same symbol.  Nikulin 1.14.2 b) asks for an orthogonal summand")
print("U^(2)(2^a) or V^(2)(2^a) with 0 <= a <= 1; whether a single rank-8 block at level 2 with")
print("oddity 2 supplies one turns on the level and oddity dictionary, printed above and not")
print("interpreted here.")
print("PYEXIT=0")
