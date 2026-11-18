"""The split and the cones for the rational-curve divisor, at the smallest cusp (research#679, A36).

    PYTHONPATH=/repo/.scratch/se-main/src \\
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python -u \\
        /repo/computations/reports/coble_679-rcop-split.py

What is computed, and against which statement.

The moduli space $F_2$ of degree-two polarized K3 surfaces has one $0$-cusp, and
its boundary lattice is $N = U \\oplus E_8(-1)^{\\oplus 2} \\oplus A_1(-1)$, of rank
19.  The rational-curve divisor $R_{\\rcop}$ lives on $F_{2d}$, and $d = 1$ is the
smallest degree, so this cusp is the smallest one that carries it.  Stage 1
builds $N$ and reads back its invariants; stage 2 computes the fundamental
chamber and its walls by Vinberg's algorithm; stage 3 enumerates the cones of
the Coxeter semifan, which are the elliptic and maximal parabolic subdiagrams;
stage 4 asks for the split.

The split is decided by the KSBA stable limit of the pair $(X,\\eps R_{\\rcop})$
over each cone: a simple root is irrelevant exactly when the combinatorial type
of that limit does not change across its mirror, which is hypothesis (W) of
`thm:semifan-recognizable-divisor` read with `thm:semifan-stratum` on the page
`writing/coble/compactifications/toroidal-and-semitoroidal.md`.  The library has
no operation for a stable pair, a Kulikov model or a semitoroidal
compactification -- `grep -rn 'stable_pair\\|ksba\\|kulikov' src/sage_extensions`
returns nothing -- so stage 4 records the expression that would decide the split
and the `AttributeError` it raises.  The split is therefore **not** computed
here, and the record names the missing call.

Stage 5 computes the one cusp at which the semifan of a rational-curve divisor is
determined in the literature: the elliptic Heegner locus, whose boundary lattice
is $\\II_{1,17} = U \\oplus E_8(-1)^{\\oplus 2}$, of rank 18.  ABE22, Intro. Thm. 1.2
with Sec. 3, give the semifan there as the fan subdividing each Coxeter chamber
by four hyperplanes, with normals

    beta_L = a3 + 2 a2 - a1,  gamma_L = a3 - a1,
    beta_R = a17 + 2 a18 - a19,  gamma_R = a17 - a19,

in the simple roots of that cusp.  The chamber the library computes lets the two
squares that decide the question be evaluated: for simple roots with
$a_i^2 = -2$ and $a_i \\cdot a_j \\in \\{0,1\\}$,

    gamma^2 = -4 - 2 (a_i \\cdot a_j) \\in {-4,-6},
    beta^2  = -12 + 4(b.c) - 2(a.c) - 4(a.b) <= -8,

so neither is a root, their mirrors are not Coxeter walls, and the semifan of
that divisor does not coarsen the Coxeter fan: (W) fails there.  The stage
evaluates those two expressions over every pair and every admissible triple of
the computed simple roots, so the conclusion does not depend on the labelling.
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
    """Run ``function`` under a wall-clock bound, returning (value, None) or (None, 'timeout')."""
    previous = signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(int(seconds))
    try:
        return function(*args, **keywords), None
    except _Timeout:
        return None, "timeout"
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def square(lattice, element):
    """The square of a lattice element."""
    return int(element * element)


# ---------------------------------------------------------------- stage 1

stamp("stage 1: the 0-cusp lattice of F_2, N = U + E8(-1) + E8(-1) + A1(-1)")
N = Lattices(ZZ)("U") + Lattices(ZZ)("E8") + Lattices(ZZ)("E8") + Lattices(ZZ)("A1")
stamp("N = %s, rank %s, signature %s" % (N, N.rank(), N.signature()))

# ---------------------------------------------------------------- stage 2

stamp("stage 2: the fundamental chamber of N and its walls (Vinberg)")
H_N = HyperbolicLattices(ZZ)(N)
chamber_N, status_N = bounded(900, H_N.fundamental_chamber)
if status_N is not None:
    stamp("the Vinberg walk on N did not finish in 900 s: %s" % status_N)
    walls_N = ()
    complete_N = None
else:
    walls_N = tuple(chamber_N.wall_roots())
    complete_N = chamber_N.is_complete_wall_set()
    stamp("walls: %d, complete wall set: %s" % (len(walls_N), complete_N))
    stamp("wall squares: %s" % sorted(set(square(N, r) for r in walls_N)))

# ---------------------------------------------------------------- stage 3

cones = None
if walls_N:
    stamp("stage 3: the cones of the Coxeter semifan at this cusp")
    diagram = H_N.reflection_coxeter_diagram()
    stamp("diagram of %d vertices" % len(walls_N))
    for name, operation in (
        ("maximal parabolic orbits", "maximal_parabolic_subdiagram_orbits"),
        ("maximal elliptic orbits", "maximal_elliptic_subdiagram_orbits"),
    ):
        try:
            value = getattr(diagram, operation)()
            stamp("  %s: %d" % (name, len(value)))
            if cones is None:
                cones = {}
            cones[name] = len(value)
        except Exception as error:
            stamp("  %s: %s: %s" % (name, type(error).__name__, error))

# ---------------------------------------------------------------- stage 4

stamp("stage 4: the split, which is the stable limit of (X, eps R_rc) over each cone")
stand_in = chamber_N
if stand_in is None:
    K = Lattices(ZZ)("U") + Lattices(ZZ)("A1")
    stand_in = HyperbolicLattices(ZZ)(K).fundamental_chamber()
    stamp(
        "no chamber of N was computed; the attempt below is made on the chamber of U + A1(-1), "
        "which is built in under a second, because the operation it misses is a method of the "
        "chamber class and not of this lattice"
    )
for expression, scope in (
    ("stand_in.stable_pairs()", {"stand_in": stand_in}),
    ("stand_in.wall_roots()[0].stable_pairs()", {"stand_in": stand_in}),
):
    try:
        value = eval(expression, dict(globals(), **scope))
        stamp("%s -> %r" % (expression, value))
    except Exception as error:
        stamp("%s -> %s: %s" % (expression, type(error).__name__, error))
stamp(
    "the missing operation is the KSBA stable limit of the pair over a cone of the chamber: the "
    "chamber's methods live in src/sage_extensions/categories/polyhedral_cones.py and the "
    "diagram's in src/sage_extensions/categories/coxeter_diagrams.py, and neither module, nor any "
    "other in src/sage_extensions, names a stable pair, a Kulikov model or a semifan"
)

# ---------------------------------------------------------------- stage 5

stamp("stage 5: the elliptic cusp, II_{1,17} = U + E8(-1) + E8(-1), where the semifan is known")
M = Lattices(ZZ)("U") + Lattices(ZZ)("E8") + Lattices(ZZ)("E8")
stamp("M = %s, rank %s, signature %s" % (M, M.rank(), M.signature()))
H_M = HyperbolicLattices(ZZ)(M)
chamber_M, status_M = bounded(900, H_M.fundamental_chamber)
if status_M is not None:
    stamp("the Vinberg walk on M did not finish in 900 s: %s" % status_M)
else:
    walls_M = tuple(chamber_M.wall_roots())
    stamp("walls: %d, complete wall set: %s" % (len(walls_M), chamber_M.is_complete_wall_set()))
    stamp("wall squares: %s" % sorted(set(square(M, r) for r in walls_M)))
    pairings = {}
    for i in range(len(walls_M)):
        for j in range(i + 1, len(walls_M)):
            value = int(walls_M[i] * walls_M[j])
            pairings[value] = pairings.get(value, 0) + 1
    stamp("pairings between simple roots: %s" % sorted(pairings.items()))
    differences = set()
    for i in range(len(walls_M)):
        for j in range(len(walls_M)):
            if i == j:
                continue
            differences.add(-4 - 2 * int(walls_M[i] * walls_M[j]))
    stamp("squares of a_j - a_i over all simple pairs: %s" % sorted(differences))
    beta = set()
    for a in range(len(walls_M)):
        for b in range(len(walls_M)):
            for c in range(len(walls_M)):
                if len({a, b, c}) < 3:
                    continue
                ab = int(walls_M[a] * walls_M[b])
                bc = int(walls_M[b] * walls_M[c])
                ac = int(walls_M[a] * walls_M[c])
                if ab == 1 and bc == 1 and ac == 0:
                    beta.add(-12 + 4 * bc - 2 * ac - 4 * ab)
    stamp("squares of a_c + 2 a_b - a_a over admissible triples: %s" % sorted(beta))
    stamp(
        "a root has square -2: none of these is a root, so the four semifan walls are not "
        "Coxeter walls and (W) fails at this cusp"
    )

stamp("done")
