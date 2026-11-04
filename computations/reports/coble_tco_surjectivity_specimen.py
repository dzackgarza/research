"""Minimal specimen for the owner handoff: T_Co's discriminant surjectivity raises.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_tco_surjectivity_specimen.py

One construction and one call, no repair attempted:

    L = Lattices(ZZ)(Gram of <2> + U(2) + E8(2))     # T_Co, rank 11, det -2048, signature (2,9)
    L.discriminant_representation_is_surjective()

The first line succeeds and the second raises.  The same call returns True for S_Co = <2> + <-2>^10 and
for M = S_En + <delta>, both rank 11, det 2048, signature (1,10), so the failure is not about rank or
about the discriminant predicate in general.  The traceback is printed in full, and the run log
`coble_tco_surjectivity_specimen-run.txt` is the record handed to sage-extensions.

Provenance is printed first: provider pin, Sage version, image, and the two source roots that appear in
the traceback (the preamble checkout bound at /repo and the engine at /repos/...).
"""
import sys
import traceback

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'

print('provenance')
print('  sage-extensions provider pin: %s' % PIN)
print('  preamble source root: /repo/.scratch/se-provider-c546/src (bound read-only at /repo)')
print('  engine source root in the traceback: /repos/sage-indefinite-port/src (inside the image)')
print('  Sage: %s' % sage_version)
print('  image rootfs: $HOME/sage-image/rootfs, read-only; repository bound at /repo')
print('  sage_extensions package file: %s' % __import__('sage_extensions').__file__)
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
GRAM = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8)

L = Lattices(ZZ)([list(row) for row in GRAM.rows()])
print('construction: Lattices(ZZ)(Gram of <2> + U(2) + E8(2))')
print('  rank %d, determinant %s, signature %s, even %s'
      % (L.rank(), L.determinant(), L.signature_pair(), L.is_even()))
print('call: L.discriminant_representation_is_surjective()')
try:
    print('  returned %s' % L.discriminant_representation_is_surjective())
except Exception:
    print('  raised; full traceback follows')
    print('-' * 78)
    traceback.print_exc(file=sys.stdout)
    print('-' * 78)

print('')
print('control specimens, same call, same session:')
for name, gram in (('S_Co = <2> + <-2>^10', block_diagonal_matrix(matrix(ZZ, [[2]]), -2 * matrix.identity(ZZ, 10))),
                   ('M = S_En + <delta> = U(2) + E8(2) + <-2>', block_diagonal_matrix(matrix(ZZ, [[-2]]), 2 * U, 2 * E8))):
    control = Lattices(ZZ)([list(row) for row in gram.rows()])
    try:
        print('  %-42s -> %s' % (name, control.discriminant_representation_is_surjective()))
    except Exception as exc:
        print('  %-42s -> raised %s' % (name, type(exc).__name__))
print('')
print('handoff: expected semantic operation is discriminant_representation_is_surjective() for the')
print('2-elementary indefinite lattice T_Co, i.e. surjectivity of O(L) -> O(A_L) read off the')
print('discriminant reduction sequence; the mathematical content is thm:two-elementary-surjectivity,')
print('which the manuscript states as a theorem independently of this runtime failure.')
