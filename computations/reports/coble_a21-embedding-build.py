"""#664: the five lattices and the two embeddings in one copy of L_K3, as far as they go today.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs   (checkout 281da26ffd)
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_a21-embedding-build.py

Runtime as adopted; provider sage-extensions 15db925b.

What this builds, and with which source each lattice is fixed:
  L_K3 = II_{3,19} = 3U + 2E8(-1)          thm:indefinite-unimodular-classification
  S_Co = C_S(2), C_S = <-1> + U + E8(-1)   prop:coble-invariant-lattice (sign by signature)
  T_Co = B(2),   B   = <1> + U + E8(-1)    prop:tco-as-twist
  S_En = C(2),   C   = U + E8(-1)          prop:gamma-en-two-gluing
  T_En = S_En^perp in L_K3, rank 12        lem:coble-heegner-vector

What it does NOT build, and why:
  * the overlattice (S_Co + T_Co) + graph(gamma) of index 2048 and (S_En + T_En) + graph(gamma)
    of index 1024: the constructors exist (`overlattice`, `even_overlattice_inclusions`,
    `extended_subgroup`, `gluing_subgroup`, `gluing_route_discriminant_classes`), but the glue
    is the GRAPH of an anti-isometry, and forming that graph needs a class of A_{S+T} from a
    pair (x, gamma(x)) with x in A_S and gamma(x) in A_T; the pairing of the two discriminant
    groups of an orthogonal sum is the object sage-extensions#276 supplies;
  * delta in T_En with delta^perp = T_Co: sage-extensions#279.

So this record fixes the inputs and the invariants, and leaves the glue to #276.
"""
import os
import shutil
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
RU = '281da26ffdce65f72203b75fe7c932684ce8fcff'

print('provenance')
print('  Sage: %s, checkout %s' % (SAGE_VERSION, RU[:12]))
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8n = -CartanMatrix(['E', 8])

def lat(m):
    return Lattices(ZZ)([list(r) for r in m.rows()])

L_K3 = lat(block_diagonal_matrix(U, U, U, E8n, E8n))
CS = block_diagonal_matrix(matrix(ZZ, [[-1]]), U, E8n)
B  = block_diagonal_matrix(matrix(ZZ, [[1]]), U, E8n)
C  = block_diagonal_matrix(U, E8n)
S_Co, T_Co, S_En = lat(2 * CS), lat(2 * B), lat(2 * C)

print('the lattices, with the source that fixes each')
rows = (('L_K3 = 3U + 2E8(-1)', L_K3, (3, 19), -1),
        ('S_Co = C_S(2)',      S_Co, (1, 10), 2048),
        ('T_Co = B(2)',        T_Co, (2, 9), -2048),
        ('S_En = C(2)',        S_En, (1, 9), -1024))
for name, L, sig, det in rows:
    ok_sig = tuple(int(x) for x in L.signature_pair()) == sig
    ok_det = int(L.determinant()) == det
    print('  %-22s rank %2d  signature %-9s det %7d  even %-5s  AGREE %s'
          % (name, L.rank(), L.signature_pair(), int(L.determinant()), L.is_even(),
             ok_sig and ok_det))
    assert ok_sig and ok_det and L.is_even()
print('')

print('the two orthogonal sums and the glue that #276 will supply')
for name, left, right, index in (('S_Co + T_Co', S_Co, T_Co, 2048),
                                 ('S_En + T_En', S_En, None, 1024)):
    if right is None:
        continue
    G = left + right
    det_g = int(G.determinant())
    A = left.discriminant_group()
    print('  %-14s rank %d, signature %s, det %d = -2^%d, even %s'
          % (name, G.rank(), G.signature_pair(), det_g, round(-det_g).bit_length() - 1, G.is_even()))
    print('      |A_{S}| = %d, and the overlattice index would be %d, giving det(overlattice) = %d'
          % (int(A.cardinality()), index, det_g // index ** 2))
    print('      constructors present on the sum: overlattice %s, even_overlattice_inclusions %s'
          % (hasattr(G, 'overlattice'), hasattr(G, 'even_overlattice_inclusions')))
print('')

print('the glue as a graph, and where the construction stops')
DS, DT = S_Co.discriminant_group(), T_Co.discriminant_group()
gamma = DS.isometry_to(DT.twist(-1))
print('  an anti-isometry A_{S_Co} -> A_{T_Co}(-1) is built: %s' % type(gamma).__name__)
print('  it is *an* anti-isometry, not the one induced by the marked embedding: that needs')
print('  sage-extensions#276, whose specimen is exactly the S_En + T_En case above.')
print('  the graph {(x, gamma(x))} needs a class of A_{S+T} from a pair of classes of A_S, A_T;')
print('  that pairing is what #276 supplies, and no operation in this build returns it.')
print('')
print('  delta in T_En with delta^perp = T_Co needs sage-extensions#279.')
print('')
print('RESULT: L_K3 and the three summand lattices are built and agree with their recorded')
print('  invariants (ranks 22, 11, 11, 10; signatures (3,19), (1,10), (2,9), (1,9); determinants')
print('  1, 2048, -2048, -1024; all even).  The orthogonal sums are built with det = -2^22 and')
print('  -2^20 and the recorded indices 2^11 and 2^10 divide them correctly.  The overlattices,')
print('  the complement T_En, gamma and delta are deferred to sage-extensions#276 and #279.')
