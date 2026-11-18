"""The same walk at the 0-cusp of F_2 with Sterk's kind of controlling vector (research#679, A36).

    PYTHONPATH=/repo/.scratch/se-main/src \\
    <proot> -R <rootfs> -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo \\
        /sage/.venv/bin/python -u /repo/computations/reports/coble_679-rcop-chamber-controlling-vector.py

`coble_679-rcop-chamber.py` shows that the Vinberg walk on N = U + E8(-1)^2 +
A1(-1) does not finish within 2400 s when the library picks its own controlling
vector.  Its docstring says what the choice decides: "the length of the
candidate list: a point lying on many of the walls presents them first", and it
records Sterk's choice at the first Enriques cusp, x = e' + f', of square 4 and
orthogonal to nine of his twelve roots.  The analogue here is x = e + f in the
U block: x^2 = 2, and x is orthogonal to all seventeen basis directions of the
E8(-1) + E8(-1) + A1(-1) part, so it lies on every wall carried by those blocks
and only the mixed walls remain to be found.

This script is that walk under a 1500 s alarm of its own.  It does not finish
either, so the controlling vector does not bring the chamber at this cusp within
reach; the measurement is recorded so that the optimisation is not attempted
again without new code.
"""

import signal
import sys
import time

sys.path.insert(0, "/repo/.scratch/se-main/src")

from sage_extensions.all import ZZ, HyperbolicLattices, Lattices

T0 = time.time()


def stamp(message):
    print("[%7.1fs] %s" % (time.time() - T0, message), flush=True)


class _Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise _Timeout()


BOUND_SECONDS = 1500

N = Lattices(ZZ)("U") + Lattices(ZZ)("E8") + Lattices(ZZ)("E8") + Lattices(ZZ)("A1")
rank = N.rank()


def basis(index):
    return N(tuple(1 if j == index else 0 for j in range(rank)))


control = basis(0) + basis(1)
stamp("N rank %s, controlling vector x = e+f with x^2 = %s" % (rank, control * control))

signal.signal(signal.SIGALRM, _alarm)
signal.alarm(BOUND_SECONDS)
try:
    chamber = HyperbolicLattices(ZZ)(N).fundamental_chamber(controlling_vector=control)
except _Timeout:
    stamp("the walk with the controlling vector did not finish in %d s" % BOUND_SECONDS)
    raise SystemExit(0)
finally:
    signal.alarm(0)

walls = tuple(chamber.wall_roots())
stamp("walls: %d, complete wall set: %s" % (len(walls), chamber.is_complete_wall_set()))
stamp("wall squares: %s" % sorted(set(int(w * w) for w in walls)))
pairings = {}
for i in range(len(walls)):
    for j in range(i + 1, len(walls)):
        value = int(walls[i] * walls[j])
        pairings[value] = pairings.get(value, 0) + 1
stamp("pairings between walls: %s" % sorted(pairings.items()))
diagram = HyperbolicLattices(ZZ)(N).reflection_coxeter_diagram(controlling_vector=control)
for name, operation in (
    ("maximal parabolic subdiagram orbits", "maximal_parabolic_subdiagram_orbits"),
    ("maximal elliptic subdiagram orbits", "maximal_elliptic_subdiagram_orbits"),
):
    try:
        stamp("  %s: %d" % (name, len(getattr(diagram, operation)())))
    except Exception as error:
        stamp("  %s: %s: %s" % (name, type(error).__name__, error))
stamp("done")
