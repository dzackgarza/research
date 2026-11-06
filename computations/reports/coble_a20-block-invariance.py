"""A20 item 1: is the U(2)/E8(2) decomposition of A_{S_En} invariant under O(q_{S_En})?

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs   (checkout 281da26ffd)
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_a20-block-invariance.py

Runtime as adopted: Sage 11.0.beta5, GAP 4.16.1 (Sage-owned).  Provider: sage-extensions
15db925b.

Why this and not A_{S_Co}: the same test on A_{S_Co} (coble_gluing_discriminants.py) showed the
decomposition there is not O(q)-invariant, but the Heegner block condition of
prop:gamma-cong-eq-heegner(2) lives on the ENRIQUES side, in A_{S_En} = A_{U(2)} perp A_{E8(2)}
of order 1024.  If that decomposition is invariant under O(q_{S_En}), then every anti-isometry
is block-compatible and Gamma^Hdg_Co = Gamma^cong cap O^+ holds unconditionally; if it is not,
the condition is a real one and item 1 stays with #664.

Registered before the run: the group is O(q_{S_En}) (order 46 998 591 897 600); the set is the
1024 classes of A_{S_En}; the blocks are the images of the U(2) and E8(2) summands of
S_En = C(2) = U(2) + E8(2), of orders 4 and 256.  The calls: A.orbits() for the partition of
the whole module, and the U(2) block tested against it.
"""
import os
import shutil
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
RU_SHA = '281da26ffdce65f72203b75fe7c932684ce8fcff'

print('provenance')
print('  Sage: %s, checkout %s' % (SAGE_VERSION, RU_SHA[:12]))
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('  gap on PATH: %s' % shutil.which('gap'))
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8n = -CartanMatrix(['E', 8])
C = block_diagonal_matrix(U, E8n)
S = Lattices(ZZ)([list(r) for r in (2 * C).rows()])
A = S.discriminant_quadratic_form()
print('S_En = C(2): rank %d, signature %s, determinant %s'
      % (S.rank(), S.signature_pair(), S.determinant()))
print('A_{S_En}: %d classes' % int(A.cardinality()))
print('')


def cls(i):
    return S.discriminant_class(S.primitive_dual(S.basis_vector(i)))


def span(elements):
    zero = elements[0] - elements[0]
    out = {zero}
    frontier = [zero]
    while frontier:
        x = frontier.pop()
        for g in elements:
            y = x + g
            if y not in out:
                out.add(y)
                frontier.append(y)
    return frozenset(out)


blockU = span([cls(0), cls(1)])            # U(2) summand
blockE = span([cls(2 + i) for i in range(8)])   # E8(2) summand
print('the blocks')
print('  U(2) block  order %3d, q-values %s'
      % (len(blockU), sorted({str(A.q(x)) for x in blockU})))
print('  E8(2) block order %3d, q-values %s'
      % (len(blockE), sorted({str(A.q(x)) for x in blockE})))
assert len(blockU) == 4 and len(blockE) == 256
print('')

start = time.time()
orbits = [set(o) for o in A.orbits()]
print('the orbits of O(q_{S_En}) on the %d classes: %d, sizes %s   (%.0f s)'
      % (int(A.cardinality()), len(orbits), sorted(len(o) for o in orbits), time.time() - start))
print('')

meeting = [o for o in orbits if o & blockU]
invariant = all(o <= blockU for o in meeting)
print('orbits meeting the U(2) block: %d' % len(meeting))
for o in meeting:
    print('  orbit of size %d: %d of its classes inside the U(2) block'
          % (len(o), len(o & blockU)))
print('')
print('the decomposition A_{S_En} = A_{U(2)} perp A_{E8(2)} is O(q_{S_En})-invariant: %s'
      % invariant)
print('')
if invariant:
    inside = [o for o in meeting if o <= blockU][0]
    x = next(iter(inside))
    y = next(iter(blockU - {x, x - x}))
    print('  indeed the U(2) block is a union of orbits, so every isometry of q_{S_En}')
    print('  preserves it and every anti-isometry A_{S_En} -> A_{T_En}(-1) is block-compatible.')
    print('  CONSEQUENCE: rho(Gamma^Hdg_Co) = P without any hypothesis on the gluing, hence')
    print('  Gamma^Hdg_Co = Gamma^cong_{Co,2} cap O^+(T_Co) unconditionally.')
else:
    crossing = [o for o in meeting if not o <= blockU][0]
    x = next(iter(crossing & blockU))
    y = next(iter(crossing - blockU))
    print('  witness, in one orbit of size %d:' % len(crossing))
    print('    x = %s   (inside the U(2) block, q = %s)' % (x, A.q(x).lift()))
    print('    y = %s   (outside the U(2) block, q = %s)' % (y, A.q(y).lift()))
    print('  so some isometry of q_{S_En} moves a class of the U(2) block out of it: the')
    print('  decomposition is NOT invariant, block-compatibility is a property of the chosen')
    print('  anti-isometry, and item 1 stays with the labeled-embedding statement (#664).')
