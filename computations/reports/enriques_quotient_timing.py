"""Where v^perp/Zv spends its time for L_- = H + H(2) + E8(-2), step by step.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/enriques_quotient_timing.py

Library: sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee.  Lattice: the Enriques period
lattice L_- = H + H(2) + E8(-2), Gram block_diagonal(H, [[0,2],[2,0]], -2*Cartan(E8)), whose
components are the ones computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage fixes.
Representative: v = e, the first basis vector, primitive isotropic.

Each step is timed and cut off by an alarm, so the stalling call is identified rather than the
whole script being killed.  The public route used is the vector-level one the API exposes --
v.orthogonal_complement() for the inclusion v^perp -> L, and v.isotropic_reduction() for the
quotient -- and nothing is reimplemented: no Gram complement, no hand-built quotient.
"""
import signal
import time

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage_extensions.all import Lattices

LIMIT = 60          # seconds per step


class Timeout(Exception):
    pass


def on_alarm(signum, frame):
    raise Timeout()


signal.signal(signal.SIGALRM, on_alarm)


def step(label, function, limit=LIMIT):
    start = time.time()
    signal.alarm(limit)
    try:
        value = function()
    except Timeout:
        print('%-46s TIMEOUT after %ds' % (label, limit), flush=True)
        return None
    except Exception as error:
        print('%-46s raised %s: %s' % (label, type(error).__name__, str(error)[:90]), flush=True)
        return None
    finally:
        signal.alarm(0)
    print('%-46s %6.2fs' % (label, time.time() - start), flush=True)
    return value


C = CartanMatrix(['E', 8])
H = matrix(ZZ, [[0, 1], [1, 0]])
H2 = matrix(ZZ, [[0, 2], [2, 0]])
GRAM = block_diagonal_matrix(H, H2, -2 * C)
print('L_-: rank %s, determinant %s, signature %s'
      % (GRAM.nrows(), GRAM.det(), 'computed below'), flush=True)

L = step('Lattices(ZZ)(L_- Gram)', lambda: Lattices(ZZ)([list(row) for row in GRAM.rows()]))
if L is None:
    raise SystemExit('the lattice itself does not build')
print('   rank %s, determinant %s, signature %s'
      % (L.module_rank(), L.determinant(), L.signature_pair()), flush=True)

ring = L.base_ring()
v = step('the representative v = e as a lattice element',
         lambda: L.linear_combination({0: ring(1)}))
print('   q(v) = %s (isotropic), primitive: %s'
      % (v.q(), step('v.is_primitive()', v.is_primitive)), flush=True)

line = step('v.sublattice()', v.sublattice)
perpendicular = step('v.orthogonal_complement()', v.orthogonal_complement)
if perpendicular is not None:
    print('   v^perp: rank %s' % step('v^perp module_rank', perpendicular.module_rank), flush=True)
reduction = step('v.isotropic_reduction()  [lattice quotient]', v.isotropic_reduction, limit=120)
if reduction is not None:
    print('   v^perp/Zv: rank %s, determinant %s, signature %s'
          % (reduction.module_rank(), reduction.determinant(), reduction.signature_pair()), flush=True)
else:
    quotient = step('v.isotropic_quotient()  [formed module, retains torsion]',
                    v.isotropic_quotient, limit=120)
    if quotient is not None:
        print('   formed quotient: %s' % quotient, flush=True)
