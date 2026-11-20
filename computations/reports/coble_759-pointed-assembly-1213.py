"""#759: the pointed lattices (S; r12, delta) and (S; r13, delta) -- every test but the assembly.

What is computed
----------------
1. The gluing classes of <r, delta> in S agree in (Q/Z)^2 for the two roots (coble_759-gluing-class
   1213-run.txt).
2. The two complements are isometric, and the library exhibits an explicit isometry Phi between
   them: Lattices(...).isometry_matrix_to returns a morphism, and its images of the generators,
   read off as the integer combinations they print as, give a matrix satisfying
   Phi^T G1 Phi = G2.
3. A direct comparison of the two complement gluing classes under Phi reports agreement in both
   directions.  THAT COMPARISON IS NOT THE DECIDING TEST and must not be read as matching; see the
   correction below.

So every datum that a pointed-lattice isometry needs is present and matches.  What the record does
NOT do is assemble them: writing tau as "identity on <r, delta>, Phi on the complement" gives a
map that is not integral on S, in either direction of Phi, so that naive gluing correction fails
and the equivalence of 12 and 13 is not certified here.

Correction: the deciding test, and it fails
------------------------------------------
Since [S : P + P^perp] = 2, an isometry of S inducing the identity on P and Phi on P^perp must send
x to (sigma(p) + phi(l))/2, where 2x = p + l.  Running that on a basis of S gives, at the very
first basis vector,

    image of S_0 is not integral: [-5/2, 2, 0, 0, 1/2, 2, 2, 0, -1, 4]

so identity-on-P glued with this Phi is not an isometry of S, and the direct comparison of the two
gluing classes above does not imply that it is.  The pair is therefore NOT certified equivalent by
this Phi, and the earlier reading of that comparison is withdrawn here.

What that means for the pair
----------------------------
The pair is not decided.  What is decided is that the obstruction is not in the invariants, not in
the P-side gluing, and not in the complement isometry -- it is in the gluing correction that
assembles them into an isometry of S, or equivalently in a pointed-isometry decision the library
does not expose.

The citation route, and why it is closed
----------------------------------------
The uniqueness statement one would want is Nikulin, Integral symmetric bilinear forms and some of
their applications, Proposition 1.14.1 (the copy in tmp/sources, subsection 1.14): two primitive
embeddings are equivalent when the complement has one class in its genus and O(K) is onto O(q_K).
That proposition is stated for an even lattice embedded in an even UNIMODULAR lattice, and its
companion Theorem 1.14.2 supplies the two complement conditions (its case b applies here, the
complement having rank 8 = l(A_2)).  But S is not unimodular -- det S = -256 -- so Proposition
1.14.1 does not apply to embeddings into S, and the route through it is closed for that reason,
not for want of a page reference.  Theorem 1.14.2 remains usable on the complement alone; it says
nothing about embeddings into S.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /bin/sh -c \\
      'PATH=/sage/.venv/bin:$PATH PYTHONPATH=/repo/.scratch/se-main/src \\
       /sage/.venv/bin/python /repo/computations/reports/coble_759-pointed-assembly-1213.py'

Transcript: coble_759-pointed-assembly-1213-run.txt.  Library pin .scratch/se-main (cf6ba0b2).
"""
import sys, re
sys.stdout.reconfigure(line_buffering=True)
from sage_extensions.all import Lattices, tensor, ZZ as LZZ
from sage.all import QQ, ZZ, matrix, vector, block_diagonal_matrix, CartanMatrix
C = CartanMatrix(["E", 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C); N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(x) for x in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]
def ip(x, y): return int(vector(ZZ, x) * G * vector(ZZ, y))
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

def setup(r):
    rv, dv = vector(ZZ, r), vector(ZZ, delta)
    cP = matrix(QQ, S).transpose().solve_right(vector(QQ, rv))
    cD = matrix(QQ, S).transpose().solve_right(vector(QQ, dv))
    func = matrix(ZZ, 2, 10)
    for j in range(10):
        func[0, j] = sum(GS[i, j] * int(cP[i]) for i in range(10))
        func[1, j] = sum(GS[i, j] * int(cD[i]) for i in range(10))
    K = matrix(ZZ, matrix(ZZ, func).right_kernel_matrix()).saturation()
    GL = matrix(ZZ, 8, 8, lambda i, j: sum(int(K[i][a]) * GS[a, b] * int(K[j][b])
                                           for a in range(10) for b in range(10)))
    B = matrix(QQ, 10, 10, [list(cP), list(cD)] + [[int(K[i][j]) for j in range(10)] for i in range(8)])
    def in_lattice(cv):
        try:
            y = B.transpose().solve_right(vector(QQ, cv))
        except Exception:
            return False
        return all(v in ZZ for v in y)
    from itertools import product
    for combo in product([0, 1], repeat=10):
        if sum(combo) == 0:
            continue
        cv = vector(QQ, combo)
        if in_lattice(cv) or not in_lattice(2 * cv):
            continue
        x = B.transpose().solve_right(2 * cv)
        if not all(v in ZZ for v in x):
            continue
        p = vector(QQ, [x[0], x[1]])
        l_coords = sum(x[2 + i] * vector(QQ, K[i]) for i in range(8))
        cL = matrix(QQ, K).transpose().solve_right(vector(QQ, l_coords))
        a = tuple(QQ(p[i]) / 2 - (QQ(p[i]) / 2).floor() for i in range(2))
        return a, GL, vector(QQ, cL)
    raise RuntimeError("no 2-division")

a1, GL1, c1 = setup(ROOTS[11])
a2, GL2, c2 = setup(ROOTS[12])
print("P-side classes: %s and %s; equal mod Z^2: %s"
      % (a1, a2, all((QQ(a1[i]) - QQ(a2[i])) in ZZ for i in range(2))))
L1 = Lattices(LZZ)(tensor(LZZ, (), (8, 8), [[LZZ(int(GL1[i, j])) for j in range(8)] for i in range(8)]))
L2 = Lattices(LZZ)(tensor(LZZ, (), (8, 8), [[LZZ(int(GL2[i, j])) for j in range(8)] for i in range(8)]))
M = L1.isometry_matrix_to(L2)
print("isometry_matrix_to: %s" % ("morphism" if M is not None else "None"))
if M is not None:
    strings = [str(M(L2.module_generator(i))) for i in range(8)]
    print("images of the generators of L2, in L1's basis:")
    for i, t in enumerate(strings):
        print("  %d -> %s" % (i, t))
    term = re.compile(r"(\d*)\*?\[(\d+)\]")
    cols = []
    for t in strings:
        col = [0] * 8
        expr = t.replace(" ", "").replace("-", "+-")
        for piece in expr.split("+"):
            if not piece:
                continue
            neg = piece.startswith("-")
            body = piece[1:] if neg else piece
            m = term.fullmatch(body)
            assert m, ("unparsed term", piece, t)
            coeff = int(m.group(1)) if m.group(1) else 1
            idx = int(m.group(2))
            col[idx] += -coeff if neg else coeff
        cols.append(col)
    mono = False
    print()
    if True:
        Mmat = matrix(ZZ, 8, 8, cols).transpose()
        print("  M^T G1 M == G2: %s" % (Mmat.transpose() * GL1 * Mmat == GL2))
        for name, Mt, src, dst in (("L2 -> L1", Mmat, c2, c1), ("L1 -> L2", Mmat.inverse(), c1, c2)):
            img = Mt * vector(QQ, src)
            ok = all((QQ(img[i]) - QQ(dst[i])) / 2 in ZZ for i in range(8))
            print("  %-8s carries the complement gluing class onto the other: %s" % (name, ok))
print("PYEXIT=0")
