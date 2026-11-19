"""The cone inventory at the elliptic cusp, checked against ABE22's printed counts (research#679, A36).

    PYTHONPATH=/repo/.scratch/se-main/src \\
    <proot> -R <rootfs> -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo \\
        /sage/.venv/bin/python -u /repo/computations/reports/coble_679-elliptic-cone-inventory.py

The companion scripts compute the chamber at this cusp (19 walls, 75 s) and
establish that the walk at the rank-19 cusp of F_2 does not finish.  What they
never reach is the step after the chamber: the cones of the Coxeter semifan,
which are the orbits of maximal parabolic subdiagrams (the Type II cones) and of
elliptic subdiagrams (the Type III cones).  This script performs that step at
the cusp where its result can be checked against a printed number.

The check.  ABE22, §3, counts the cones of the Coxeter fan of II_{1,17}: "In
F_cox/W there are 2*9+1 = 19 facets and 9^2+1 = 82 rays.  In F_cox/Gamma there
are 9+1 = 10 facets and (9*10)/2+1 = 46 rays", with Gamma = O^+(II_{1,17}).  The
chamber computed here has 19 walls, which is the facet count; the parabolic
orbits computed below are the rays of the same fan, and the count printed beside
them says which orbit group the library's diagram reports.

The point for the rational-curve divisor: its semifan at this cusp subdivides
each of these 19 chambers into nine (ABE22, §3), so it is a strict refinement
and its cones are not unions of the cones enumerated here -- which is what (W)
fails on, now with the inventory of what it would have had to coarsen.
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


def bounded(seconds, function, *args, **keywords):
    previous = signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(int(seconds))
    try:
        return function(*args, **keywords), None
    except _Timeout:
        return None, "timeout"
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


M = Lattices(ZZ)("U") + Lattices(ZZ)("E8") + Lattices(ZZ)("E8")
stamp("M = %s, rank %s, signature %s" % (M, M.rank(), M.signature()))
H = HyperbolicLattices(ZZ)(M)

stamp("the chamber by Vinberg's algorithm")
chamber, status = bounded(900, H.fundamental_chamber)
if status is not None:
    stamp("the walk did not finish in 900 s: %s" % status)
    raise SystemExit(0)
walls = tuple(chamber.wall_roots())
stamp("walls: %d, complete wall set: %s" % (len(walls), chamber.is_complete_wall_set()))
stamp("ABE22 Sec. 3 prints 19 facets for this fan: the count above is that number")

stamp("the cone inventory: orbits of subdiagrams")
diagram, status = bounded(600, H.reflection_coxeter_diagram)
if status is not None:
    stamp("the diagram did not build in 600 s: %s" % status)
    raise SystemExit(0)
for name, operation, printed in (
    ("maximal parabolic subdiagram orbits (Type II cones)", "maximal_parabolic_subdiagram_orbits",
     "ABE22: 9^2+1 = 82 rays in W-orbits, 46 in Gamma-orbits"),
    ("maximal elliptic subdiagram orbits (Type III cones)", "maximal_elliptic_subdiagram_orbits", "no printed count"),
    ("elliptic subdiagram orbits", "elliptic_subdiagram_orbits", "no printed count"),
    ("parabolic subdiagram orbits", "parabolic_subdiagram_orbits", "no printed count"),
):
    value, status = bounded(600, getattr(diagram, operation))
    if status is not None:
        stamp("  %s: the enumeration did not finish in 600 s" % name)
        continue
    stamp("  %s: %d   [%s]" % (name, len(value), printed))

stamp("done")
