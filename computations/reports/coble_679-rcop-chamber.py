"""The chamber and the cones at the 0-cusp of F_2, for the rational-curve divisor (research#679, A36).

    PYTHONPATH=/repo/.scratch/se-main/src \\
    <proot> -R <rootfs> -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo \\
        /sage/.venv/bin/python -u /repo/computations/reports/coble_679-rcop-chamber.py

The companion script `coble_679-rcop-split.py` asks for the split and records
that the stable limit of the pair over a cone is not an operation of the
library; it also showed that the Vinberg walk on the rank-19 cusp lattice does
not finish within 1800 s, so its cone inventory was never reached.  This script
is that walk alone, under a 2400 s alarm of its own so that a failure to finish
is written into the record rather than left to the invoking `timeout`: on
success it prints the walls, their pairings, the Coxeter diagram and the orbits
of elliptic and maximal parabolic subdiagrams, which are the cones of the
Coxeter semifan at that cusp.

The split I | J is not computed here either: it is a labelling of these cones by
the combinatorial type of the KSBA stable limit of (X, eps R_rc), and that
operation is absent from the library (see the companion record).
"""

import signal
import sys
import time

sys.path.insert(0, "/repo/.scratch/se-main/src")

from sage_extensions.all import ZZ, HyperbolicLattices, Lattices

T0 = time.time()


def stamp(message):
    print("[%7.1fs] %s" % (time.time() - T0, message), flush=True)


stamp("the 0-cusp lattice of F_2: N = U + E8(-1) + E8(-1) + A1(-1)")
N = Lattices(ZZ)("U") + Lattices(ZZ)("E8") + Lattices(ZZ)("E8") + Lattices(ZZ)("A1")
stamp("N = %s, rank %s, signature %s" % (N, N.rank(), N.signature()))

stamp("the fundamental chamber of N by Vinberg's algorithm")
BOUND_SECONDS = 2400


class _Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise _Timeout()


signal.signal(signal.SIGALRM, _alarm)
signal.alarm(BOUND_SECONDS)
try:
    chamber = HyperbolicLattices(ZZ)(N).fundamental_chamber()
except _Timeout:
    stamp("the Vinberg walk on N did not finish in %d s: timeout" % BOUND_SECONDS)
    stamp("done")
    raise SystemExit(0)
finally:
    signal.alarm(0)
walls = tuple(chamber.wall_roots())
stamp("walls: %d, complete wall set: %s" % (len(walls), chamber.is_complete_wall_set()))
stamp("wall squares: %s" % sorted(set(int(r * r) for r in walls)))
pairings = {}
for i in range(len(walls)):
    for j in range(i + 1, len(walls)):
        value = int(walls[i] * walls[j])
        pairings[value] = pairings.get(value, 0) + 1
stamp("pairings between walls: %s" % sorted(pairings.items()))
stamp("the walls:")
for index, root in enumerate(walls):
    stamp("  %2d  %s" % (index, root))

stamp("the cones: orbits of elliptic and maximal parabolic subdiagrams")
diagram = HyperbolicLattices(ZZ)(N).reflection_coxeter_diagram()
for name, operation in (
    ("maximal parabolic subdiagram orbits", "maximal_parabolic_subdiagram_orbits"),
    ("maximal elliptic subdiagram orbits", "maximal_elliptic_subdiagram_orbits"),
    ("all elliptic subdiagram orbits", "elliptic_subdiagram_orbits"),
    ("all parabolic subdiagram orbits", "parabolic_subdiagram_orbits"),
):
    try:
        value = getattr(diagram, operation)()
        stamp("  %s: %d" % (name, len(value)))
    except Exception as error:
        stamp("  %s: %s: %s" % (name, type(error).__name__, error))

stamp("done")
