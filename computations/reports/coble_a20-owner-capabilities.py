"""#663 item 1: the two owner capabilities the issue records as blocking it, at the adopted runtime.

Transcript: coble_a20-owner-capabilities-run.txt.

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /bin/sh -c \\
        'PATH=/sage/.venv/bin:$PATH python /repo/computations/reports/coble_a20-owner-capabilities.py'

Part 1 decides #663 item 1(b) of the body -- "torsion forms have is_isometric_to but no explicit
isometry constructor ... expected operation: an explicit isometry constructor on torsion quadratic
forms, twisted variant included" -- by building that object and checking q_T o gamma = -q_S on
every class of the source.

Part 2 measures #663 item 1(a) of the body, L.discriminant_representation_is_surjective() on the
Coble coinvariant lattice T_Co, at the provider the image carries.  The method is
lattices.py:4226, and it calls discriminant_image(), i.e. the automorphism-generator route; a
budget is set below and, if it expires, the stack is dumped rather than guessed at.
"""
import faulthandler
import sys
import time
import traceback

sys.stdout.reconfigure(line_buffering=True)

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as SAGE_VERSION

import sage_extensions
from sage_extensions.all import Lattices

BUDGET = 900

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: %s' % sage_extensions.__file__)
print('  budget for the single surjectivity call below: %d s (faulthandler stack dump)' % BUDGET)
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8n = -CartanMatrix(['E', 8])

Tco = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8n).rows()])
Sco = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(matrix(ZZ, [[2]]), -2 * matrix.identity(ZZ, 10)).rows()])
Ten = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8n).rows()])
Sen = Lattices(ZZ)([list(r) for r in (2 * block_diagonal_matrix(U, E8n)).rows()])

print('the lattices')
for label, L, sig in (('T_Co = <2> + U(2) + E8(2)', Tco, (2, 9)),
                      ('S_Co = <2> + <-2>^10      ', Sco, (1, 10)),
                      ('T_En = U + U(2) + E8(2)  ', Ten, (2, 10)),
                      ('S_En = U(2) + E8(2)      ', Sen, (1, 9))):
    print('  %s rank %2d, determinant %6s, signature %s'
          % (label, L.rank(), L.determinant(), tuple(int(x) for x in L.signature_pair())))
    assert tuple(int(x) for x in L.signature_pair()) == sig
print('')

print('=== part 1: an explicit anti-isometry A_{S_En} -> A_{T_En} with q_T o gamma = -q_S')
A = Sen.discriminant_quadratic_form()
B = Ten.discriminant_quadratic_form()
Bm = B.twist(-1)
print('  A_{S_En}.is_isometric_to(A_{T_En})   = %s' % A.is_isometric_to(B))
print('  A_{S_En}.is_anti_isometric(A_{T_En}) = %s' % A.is_anti_isometric(B))
start = time.time()
gamma = A.isometry_to(Bm)
print('  A_{S_En}.isometry_to(A_{T_En}(-1))   = %s   (%.0f s)'
      % (type(gamma).__name__, time.time() - start))


def cls(lattice, form, i):
    return lattice.discriminant_class(lattice.primitive_dual(lattice.basis_vector(i)))


basis = [cls(Sen, A, i) for i in range(Sen.rank())]
classes = [basis[0] - basis[0]]
for g in basis:
    classes = classes + [x + g for x in classes]
print('  classes enumerated: %d = 2^%d' % (len(classes), len(basis)))
start = time.time()
ok = all(Bm.q(gamma(x)).lift() == A.q(x).lift() for x in classes)
print('  q_{T_En(-1)}(gamma x) = q_{S_En}(x) on all %d classes: %s   (%.0f s)'
      % (len(classes), ok, time.time() - start))
print('  distinct images: %d' % len({gamma(x) for x in classes}))
print('  So the object the body records as not existing exists here, twisted variant included.')
print('')

print('=== part 2: discriminant_representation_is_surjective() on T_Co (#663 item 1(a) of the body)')
print('  the method: sage_extensions/categories/lattices.py:4226, which calls discriminant_image()')
faulthandler.dump_traceback_later(BUDGET, repeat=False, file=sys.stdout)
start = time.time()
try:
    answer = Tco.discriminant_representation_is_surjective()
except Exception:
    print('  T_Co.discriminant_representation_is_surjective() RAISED; full traceback follows')
    print('-' * 78)
    traceback.print_exc(file=sys.stdout)
    print('-' * 78)
else:
    print('  T_Co.discriminant_representation_is_surjective() = %s   (%.0f s)'
          % (answer, time.time() - start))
finally:
    faulthandler.cancel_dump_traceback_later()
print('')
print('  controls, same call, same session')
for label, L in (('S_Co', Sco), ('T_En', Ten), ('S_En', Sen)):
    start = time.time()
    try:
        print('    %-5s -> %s   (%.0f s)' % (label, L.discriminant_representation_is_surjective(), time.time() - start))
    except Exception as exc:
        print('    %-5s -> raised %s   (%.0f s)' % (label, type(exc).__name__, time.time() - start))
print('')
print('What this decides: part 1 decides the capability the body records as missing; part 2 records')
print('whether the surjectivity route runs at this provider, which is the input #664 leans on for T_Co.')
print('Neither part says anything about the marked embedding (prob:coble-rigidity).')
