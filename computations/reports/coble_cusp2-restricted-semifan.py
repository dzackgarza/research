"""The cusp-2 mirror facet: projected integral roots and the AEGS marking.

Header: objects and checks fixed before the run
-----------------------------------------------
T_En = U + U(2) + E8(2), with basis (e,f,e',f',a_1,...,a_8) and Gram matrix
block_diag(U,2U,-2 Cartan(E8)).  The cusp-2 isotropic vector is eta = e'.  The
AEGS Figure 7 roots, in the node order used by
coble_enriques-white-root-facets.py, are

  r_1 = a_4, r_2 = a_3, r_3 = a_1, r_4 = a_2,
  r_i = a_i (5 <= i <= 8), r_9 = abar_8 + 2f, r_10 = e-f,

where abar is Sterk's dual-root basis transcribed verbatim from the accepted
#654 record.  Only r_10 is white: r_10^2 = -2; the other squares are -4.  The
only nonorthogonal incidence with delta = r_10 is the double bond 9--10.

For i < 10, the projected wall normal into delta^perp is
  w_i = r_i + ((r_i,delta)/2) delta.
Thus w_9 = r_9 + delta and every other w_i = r_i.  The restricted cusp lattice
  Sbar = (delta^perp intersect eta^perp)/eta
has the explicit basis (h,a_1,...,a_8), h = e+f, with Gram matrix
<2> + (-2 Cartan(E8)); in particular Sbar = <2> + E8(2) has invariants (9,9,1).
The run checks integrality in this basis, all Gram entries, w_9^2 = -2, the other
squares -4, and reflection integrality (every -2 vector is reflective, while a -4
vector must have divisibility 2).  The nine restricted hyperplanes are distinct: the
projected Gram matrix is nonsingular over QQ.  This also records the checks that
node 10 is the only wall requiring a central dihedral rotation and that its
incidence label 4 is even.

Marking input fixed before the run: AEGS Definition 5.4 and Figure 7 make every
root on the folded triangle's boundary relevant; the interior spur is node 4.
Lemma 5.5 (printed p. 611) says this is the marking of the folded semifan.  By
AN06 Table 1, entry (9,9,1), the corresponding Coble spur is v_9.  Thus the
inherited marking is {v_1,...,v_8} relevant and {v_9} irrelevant, and the
restricted irrelevant reflection has order 2.  The run prints the Gram matrix in
both the manuscript wall order and the AN order 3,2,1,5,6,7,8,9,4; the latter
has the single double bond v_7--v_8 as in @thm:coble-cusp-chamber.

Owner calls: exact ZZ/QQ matrix algebra only.  No root enumeration, provider
call, or numerical volume computation is made.  The full W^(2,4) assertion on
the page uses congruence to the finite-volume AN06 chamber, not this script as a
root-completeness search.

Run in the maintained Sage runtime:
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs \
    -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo /bin/sh -c \
    'PATH=/sage/.venv/bin:$PATH python \
     /repo/computations/reports/coble_cusp2-restricted-semifan.py'
Transcript: coble_cusp2-restricted-semifan-run.txt.
"""
from math import gcd
import sys

sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ, QQ, CartanMatrix, block_diagonal_matrix, matrix, vector
from sage.version import version as SAGE_VERSION

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = (BAS[i] for i in range(4))
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))) for i in range(8)]
eta = ep
delta = e - f
R = [alpha[3], alpha[2], alpha[0], alpha[1], alpha[4], alpha[5], alpha[6], alpha[7],
     abar[7] + 2 * f, delta]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


print("cusp-2 restricted semifan: projected roots and inherited marking")
print("Sage %s; exact ZZ/QQ linear algebra" % SAGE_VERSION)
print("eta = %s; delta = %s; eta.delta = %d; delta^2 = %d; eta^2 = %d" %
      (list(eta), list(delta), ip(eta, delta), ip(delta, delta), ip(eta, eta)))
assert ip(eta, delta) == 0 and ip(delta, delta) == -2 and ip(eta, eta) == 0
print("the only delta incidence is double 9--10; every other incidence is orthogonal")
for i in range(9):
    print("  pairing (r_%d,delta) = %d" % (i + 1, ip(R[i], delta)))
assert [ip(R[i], delta) for i in range(9)] == [0] * 8 + [2]

W = []
for i in range(9):
    assert ip(R[i], delta) % 2 == 0
    w = R[i] + (ip(R[i], delta) // 2) * delta
    assert ip(w, delta) == 0 and ip(w, eta) == 0
    W.append(w)
assert W[8] == R[8] + delta
assert all(W[i] == R[i] for i in range(8))

B = matrix(ZZ, 9, 12, [list(e + f)] + [list(a) for a in alpha])
S = B * G * B.transpose()
print("restricted basis = (h=e+f,a_1,...,a_8); restricted Gram invariants are (9,9,1)")
print("restricted basis Gram determinant = %d" % S.det())
assert S.det() == 512
print("restricted Gram =\n%s" % S)

coordinates = []
for i, w in enumerate(W):
    c = B.change_ring(QQ).transpose().solve_right(vector(QQ, w))
    assert all(x in ZZ for x in c)
    c = vector(ZZ, [int(x) for x in c])
    assert sum((c[j] * B.row(j) for j in range(9)), vector(ZZ, [0] * 12)) == w
    coordinates.append(c)
    div = gcd(*[abs(ip(w, B.row(j))) for j in range(9)])
    q = ip(w, w)
    expected_q = -2 if i == 8 else -4
    reflective = (q == -2 and div in (1, 2)) or (q == -4 and div == 2)
    print("w_%d = %s; Sbar coordinates = %s; square = %d; div_Sbar = %d" %
          (i + 1, list(w), list(c), q, div))
    assert q == expected_q and reflective

WG = matrix(ZZ, 9, 9, lambda i, j: ip(W[i], W[j]))
print("projected wall Gram, in the figure-node order =\n%s" % WG)
assert WG.det() != 0
EXPECTED_BONDS = {(0, 1): 2, (1, 2): 2, (0, 3): 2, (0, 4): 2,
                  (4, 5): 2, (5, 6): 2, (6, 7): 2, (7, 8): 2}
for i in range(9):
    for j in range(i + 1, 9):
        assert WG[i, j] == EXPECTED_BONDS.get((i, j), 0)
assert [WG[i, i] for i in range(9)] == [-4] * 8 + [-2]

AN_ORDER = [2, 1, 0, 4, 5, 6, 7, 8, 3]
AN_G = matrix(ZZ, 9, 9, lambda i, j: WG[AN_ORDER[i], AN_ORDER[j]])
print("the same wall Gram in AN order (chain v_1,...,v_8, spur v_9) =\n%s" % AN_G)
AN_BONDS = {(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(2,8)}
for i in range(9):
    for j in range(i + 1, 9):
        assert AN_G[i, j] == (2 if (i, j) in AN_BONDS else 0)
# The chain is v_1,...,v_8 in AN indices 0,...,7.  Its last bond 6--7
# is double because v_8 has square -2; the spur 8 is attached to v_3 = index 2.
assert AN_G[7, 7] == -2 and AN_G[2, 8] == 2 and AN_G[6, 7] == 2
print("all nine induced hyperplanes are distinct and every wall is a root mirror of Sbar")

# The even-incidence mechanism: R = s_delta s_r9 rotates through pi/2
# on <delta,r_9>, so R^2 induces s_w9 on the mirror delta^perp.
def reflection_matrix(root):
    q = ip(root, root)
    rows = []
    for basis_vector in BAS:
        numerator = 2 * ip(basis_vector, root)
        assert numerator % q == 0
        rows.append([basis_vector[j] - (numerator // q) * root[j] for j in range(N)])
    return matrix(ZZ, N, N, rows)

Rdelta = reflection_matrix(delta)
R9 = reflection_matrix(R[8])
Rotation = Rdelta * R9
assert Rotation ** 4 == matrix.identity(ZZ, N)
Central = Rotation ** 2
assert Central * G * Central.transpose() == G
assert Central.transpose() * vector(ZZ, delta) == -vector(ZZ, delta)
for row in B.rows():
    expected = row + ip(row, W[8]) * W[8]
    assert Central.transpose() * row == expected
print("central dihedral check: R=s_delta s_r9 has order 4 and R^2 restricts to s_w9")
print("marking: relevant nodes 1,2,3,5,6,7,8,9; irrelevant interior spur 4")
print("AN marking: v_1,...,v_8 relevant; v_9 (= current node 4) irrelevant; W_irr = S_2")
print("PYEXIT=0")
