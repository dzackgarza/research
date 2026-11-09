"""#667/#645, plane half, part 1: the Levi obstruction to lifting planes.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := /sage/.venv/bin:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_plane-half-levi.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e.

The question, in the page's own words: is rho(Stab_{O(B)}(P)) = Stab_{O(q)}(J) for a primitive
isotropic plane P in B = U + U + I_{0,7} and J = [P/2] in A_{T_Co} = B/2B?  Nikulin's
surjectivity does not apply, because the Levi quotient is Orth(I_{0,7}), which is definite.

What this run decides.  The Levi part of the parabolic Stab_{O(B)}(P) = (GL(P) x O(K_P)) |x N is
O(K_P) = O(I_{0,7}) = {+-1}^7 |x S_7, and GL(P) and the unipotent radical N both act trivially on
K_P.  Hence the action of the whole parabolic on K_P, and therefore on K_P/2K_P, factors through
O(I_{0,7}); the sign changes of {+-1}^7 are trivial modulo 2, so the image is S_7.  If
S_7 is a proper subgroup of O(q_{K_P(2)}) then no element of Stab_{O(q)}(J) whose image on
K_P/2K_P lies outside S_7 can lift, and the lifting theorem fails.

What it computes: (1) B and the plane P, with K_P = P^perp/P identified as I_{0,7};
(2) K_P(2) = <-2>^7 and the order of O(q_{-1/2}^7) on its 128 classes;
(3) |S_7| and the index |O(q)|/|S_7|, which is a lower bound for [Stab_{O(q)}(J) : rho(P_P)].
What it does NOT compute: the order of Stab_{O(q)}(J) itself, hence not the exact fibre index,
and not the number of plane classes.  Those are the remaining steps named in the run's last line.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
G_B = block_diagonal_matrix(U, U, -matrix.identity(ZZ, 7))
B = Lattices(ZZ)([list(r) for r in G_B.rows()])
print('(1) B = U + U + I_{0,7}')
print('  rank %d, determinant %s, signature %s, even %s'
      % (B.rank(), B.determinant(), B.signature_pair(), B.is_even()))
basis = [B.basis_vector(i) for i in range(B.rank())]
e1, e2 = basis[0], basis[2]              # the isotropic generators of the two hyperbolic planes
print('  P = <e1, e2> = <%s, %s>: squares %s, %s, pairing %s'
      % (tuple(e1), tuple(e2), e1.q(), e2.q(), B.pairing(e1, e2)))
print('  e1, e2 primitive together (the submodule generated is saturated): %s'
      % (B.primitive_sublattice_from([e1, e2]).rank() == 2))
print('')

# K_P = P^perp/P: spanned by the I_{0,7} coordinates, since P^perp = <e1,e2> + I_{0,7}
K_basis = [basis[4 + i] for i in range(7)]
G_K = matrix(ZZ, [[B.pairing(a, b) for b in K_basis] for a in K_basis])
K = Lattices(ZZ)([list(r) for r in G_K.rows()])
print('  P^perp has rank %d, spanned by e1, e2 and the seven I_{0,7} coordinates: %s'
      % (2 + 7, all(B.pairing(e, k) == 0 for e in (e1, e2) for k in K_basis)))
print('  K_P = P^perp/P: rank %d, determinant %s, signature %s, odd %s'
      % (K.rank(), K.determinant(), K.signature_pair(), not K.is_even()))
print('  its Gram matrix is minus the identity: %s' % (G_K == -matrix.identity(ZZ, 7)))
print('')

start = time.time()
K2 = Lattices(ZZ)([list(r) for r in (2 * G_K).rows()])       # K_P(2) = <-2>^7
A_K = K2.discriminant_quadratic_form()
n_K = int(A_K.cardinality())
print('(2) K_P(2) = <-2>^7 and its discriminant form   (%.0f s)' % (time.time() - start))
print('  |A_{K_P(2)}| = %d, i.e. (Z/2)^7' % n_K)
values = sorted({str(A_K.q(x)) for x in A_K.elements()})
print('  the values of q, as classes: %d distinct' % len(values))
start = time.time()
O_K = A_K.orthogonal_group()
order_K = int(O_K.order())
print('  |O(q_{-1/2^7})| = %d   (%.0f s)' % (order_K, time.time() - start))
print('')

fact = 1
for i in range(1, 8):
    fact *= i
print('(3) the image of the Levi part and the index')
print('  O(I_{0,7}) = {+-1}^7 |x S_7 has order 2^7 * 7! = %d' % ((2 ** 7) * fact))
print('  the sign changes act trivially modulo 2, so the image in O(q_{K_P(2)}) is S_7, of order %d'
      % fact)
print('  |O(q)| / |S_7| = %d / %d = %d' % (order_K, fact, order_K // fact))
print('  and that is a lower bound for [Stab_{O(q)}(J) : rho(P_P)], since the action of the whole')
print('  parabolic on K_P/2K_P factors through O(I_{0,7}).')
print('')
print('CONCLUSION')
print('  The Levi image is S_7 of order %d inside O(q_{K_P(2)}) of order %d, an index of %d.'
      % (fact, order_K, order_K // fact))
print('  No element of the parabolic acts on K_P/2K_P outside S_7, so any element of')
print('  Stab_{O(q)}(J) whose action there does is not in the image; the lifting theorem for planes')
print('  therefore fails, and the fibre index per plane class is at least %d.'
      % (order_K // fact))
print('  Remaining, and not computed here: (i) |Stab_{O(q)}(J)|, hence the exact fibre index;')
print('  (ii) the plane classes and their number; (iii) the incidence of each plane orbit with the')
print('  527 0-cusp classes.')
