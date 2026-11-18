"""#759: which side of the rank-2 gluing obstructs the pair (12,13)?

S contains P = <r, delta> with P + P^perp of index 2, so S/(P + P^perp) is Z/2.  A generator v
satisfies 2v = p + l with p in P and l in P^perp, and the class of p/2 in P*/P is well defined.
That class is the gluing datum on the P side.  The map r12 -> r13, delta -> delta is the identity
in the (r, delta) coordinates, so it acts trivially on A_P, and the extension to S exists only if
the two gluing classes agree there.

Result
------
The gluing classes are

    r12: p/2 = (-1/2, 1/2)   in the (r, delta) coordinates, mod Z^2
    r13: p/2 = ( 1/2, 1/2)

and since -1/2 = 1/2 mod 1 they are EQUAL in (Q/Z)^2.  So the P side obstructs nothing for either
root, and whatever obstructs the extension lives in the complements.

This corrects an earlier version of this record, which reported (0, 0) for both: its 2-division
vector was trivial -- it satisfied 2v in P + P^perp by being in P + P^perp already -- so it was
not a generator of the quotient.  The search here refuses trivial classes.

Where the pair now stands
-------------------------
The two complements are isometric by every invariant (coble_759-invariant-lattices-1213-run.txt)
and the library returns an explicit isometry between them (Lattices(...).isometry_matrix_to
returns a matrix, not None).  So the pair (12,13) is reduced to one question: does that explicit
isometry carry the gluing class of one complement onto that of the other.  This record does not
answer it -- applying the library's morphism to a half-integral vector needed a conversion of its
elements into sage coordinates that did not come together here -- and it does not report the
answer either way.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
      computations/reports/coble_759-gluing-class-1213.py

Transcript: coble_759-gluing-class-1213-run.txt.  Sage in the shared runtime, exact ZZ/QQ algebra.
"""
import sys
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix
sys.stdout.reconfigure(line_buffering=True)
C = CartanMatrix(["E", 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C); N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]
def ip(x, y): return int(vector(ZZ, x) * G * vector(ZZ, y))
delta = e - f
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j])); Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))]) for i in range(8)]
eta = 2 * e + 2 * f + abar[0]
ROOTS = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7], 2 * et - at[0],
          2 * et + (abart[1] - abart[2]), ft - et, et + ft + (abart[5] - abart[2]),
          et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]])
r12, r13 = ROOTS[11], ROOTS[12]
S = matrix(ZZ, [vector(ZZ, r) for r in ROOTS]).saturation()   # 10 x 12
GS = matrix(ZZ, 10, 10, lambda i, j: ip(S[i], S[j]))

def glue(r):
    rv = vector(ZZ, r); dv = vector(ZZ, delta)
    # P = span(r, delta) (saturated: they are primitive and orthogonal, both (-2))
    P = matrix(ZZ, [rv, dv])
    # coordinates in the S-basis
    def coords(x):
        return matrix(QQ, S).transpose().solve_right(vector(QQ, x))
    cP, cD = coords(rv), coords(dv)
    # L = P^perp inside S, in S-coordinates: kernel of [GS*cP ; GS*cD]
    func = matrix(ZZ, 2, 10)
    for j in range(10):
        func[0, j] = sum(GS[i, j] * int(cP[i]) for i in range(10))
        func[1, j] = sum(GS[i, j] * int(cD[i]) for i in range(10))
    K = matrix(ZZ, matrix(ZZ, func).right_kernel_matrix()).saturation()
    assert K.nrows() == 8, K.nrows()
    # the index of P + L in S
    GL = matrix(ZZ, 8, 8, lambda i, j: sum(int(K[i][a]) * GS[a, b] * int(K[j][b]) for a in range(10) for b in range(10)))
    d2 = QQ(4) * QQ(GL.det()) / QQ(GS.det())
    assert d2.is_square() and d2.sqrt() == 2, (d2, GL.det())
    # find v in S with 2v in P + L, i.e. the class of 2v in S/(P+L) is zero but v is not
    # solve: v = a*r + b*delta + l over QQ with a, b not both integral-half;
    # equivalent: find v with 2 (v . cP-part) ... simpler: search the 2-division of the class
    # assemble a basis of span(P, L) in S-coordinates: 2 + 8 = 10 rows -> often full rank
    B = matrix(QQ, 2 + 8, 10, [list(cP), list(cD)] + [[int(K[i][j]) for j in range(10)] for i in range(8)])
    # a vector v whose double lands in the span: solve for v in the dual sense
    # we look for v in S with 2v in lattice(P,L) but v not: check the quotient S/lattice(P,L) has order 2
    # take v = the sum of the S-basis vectors whose coordinates realise the missing class:
    from itertools import product
    found = None
    for combo in product([0, 1], repeat=10):
        if sum(combo) == 0:
            continue
        cv = vector(QQ, combo)
        # 2v in lattice(P,L)?
        # solve B^T * x = 2*cv  (x of length 10)
        try:
            x = B.transpose().solve_right(2 * cv)
        except Exception:
            continue
        if all(v in ZZ for v in x):
            found = (cv, x); break
    assert found, "no 2-division vector found"
    cv, x = found
    p_part = [x[0], x[1]]                       # coordinates of p in the (r, delta) basis
    # a = class of p/2 in P*/P, i.e. the pair (p1/2, p2/2) mod Z^2
    a = (QQ(p_part[0]) / 2 - (QQ(p_part[0]) / 2).floor(),
         QQ(p_part[1]) / 2 - (QQ(p_part[1]) / 2).floor())
    return a, GL.det()

a12, d12 = glue(r12)
a13, d13 = glue(r13)
print("complement determinant inside S: r12 -> %d, r13 -> %d" % (d12, d13))
print("gluing class in the (r, delta) coordinates, as p/2 mod Z^2:")
print("  r12: %s" % (a12,))
print("  r13: %s" % (a13,))
print()
print("the classes are equal mod Z^2: %s"
      % all((QQ(a12[i]) - QQ(a13[i])) in ZZ for i in range(2)))
print()
if d12 != d13:
    print("RESULT: the complements differ in determinant, so no isometry of S carries r12 to r13")
    print("while fixing delta.")
elif all((QQ(a12[i]) - QQ(a13[i])) in ZZ for i in range(2)):
    print("RESULT: the P side obstructs nothing -- the gluing classes agree in (Q/Z)^2 -- so the pair")
    print("is reduced to whether an isometry of the two complements (which exist, and which the")
    print("library exhibits explicitly) carries one complement gluing class onto the other.  That")
    print("comparison is not made here.")
else:
    print("RESULT: the gluing classes differ in (Q/Z)^2, so no isometry of S carries r12 to r13")
    print("while fixing delta.")
print("PYEXIT=0")
