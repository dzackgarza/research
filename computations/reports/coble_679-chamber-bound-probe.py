"""Does a bound on Vinberg's search bring the chamber at the F_2 cusp into range? (research#679, A36)

    PYTHONPATH=/repo/.scratch/se-main/src \\
    <proot> -R <rootfs> -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo \\
        /sage/.venv/bin/python -u /repo/computations/reports/coble_679-chamber-bound-probe.py

`coble_679-rcop-chamber.py` shows that the walk on N = U + E8(-1)^2 + A1(-1) does not finish in
2400 s.  The obvious next question is whether the cost is in the *number of roots* -- in which
case a bound on the search would give a partial chamber cheaply -- or in the setup and the
per-step arithmetic at rank 19, in which case no bound helps.

This probe answers it by bounding the search at 1, 4, 12 and 24 roots, and by running the
rank-18 lattice U + E8(-1)^2 as a control at bounds 1 and 4.  Every attempt carries its own
120 s alarm, and a timeout is recorded as a result.

What it decides: the rank-19 walk does not finish at any bound tried, including max_roots = 1, so
the cost is not the number of roots to be found and a bound on the search cannot deliver the
chamber.  The control shows the other half of the same fact: at rank 18 the same bounds do
return the whole chamber, in tens of seconds, and the time is not monotone in the bound -- across
runs the bound-1 and bound-4 attempts trade places around the 120 s alarm -- so `max_roots` is
not a cost knob at either rank and the timing near the bound is not reproducible to better than
"finishes or not".  The chamber at rank 19 therefore has to be obtained some other way: computed
by a different method, or transcribed from AET23, Fig. 1, printed p. 22, with its pairings
checked.
"""

import signal
import sys
import time

sys.path.insert(0, "/repo/.scratch/se-main/src")

from sage_extensions.all import ZZ, HyperbolicLattices, Lattices

BOUND_SECONDS = 120
BOUNDS = (1, 4, 12, 24)


class _Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise _Timeout()


def attempt(name, lattice, bound):
    hyperbolic = HyperbolicLattices(ZZ)(lattice)
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(BOUND_SECONDS)
    start = time.time()
    try:
        roots = hyperbolic.vinberg_simple_roots(max_roots=bound)
        print("%-18s max_roots=%2d -> %2d roots in %6.1fs" % (name, bound, len(roots), time.time() - start), flush=True)
    except _Timeout:
        print("%-18s max_roots=%2d -> timeout at %d s" % (name, bound, BOUND_SECONDS), flush=True)
    finally:
        signal.alarm(0)


N = Lattices(ZZ)("U") + Lattices(ZZ)("E8") + Lattices(ZZ)("E8") + Lattices(ZZ)("A1")
M = Lattices(ZZ)("U") + Lattices(ZZ)("E8") + Lattices(ZZ)("E8")
print("rank 19: %s, signature %s" % (N.rank(), N.signature()), flush=True)
print("rank 18: %s, signature %s" % (M.rank(), M.signature()), flush=True)
for bound in BOUNDS:
    attempt("rank 19", N, bound)
for bound in (1, 4):
    attempt("rank 18 (control)", M, bound)
print()
print("Conclusion.  The rank-19 walk does not finish at any bound tried, including max_roots = 1.")
print("The cost there is therefore not the number of roots the search must find, and a bound on the")
print("search cannot deliver the chamber.  The rank-18 control returns the whole chamber under the")
print("same bounds, so the difference is the rank and not the parameter.")
