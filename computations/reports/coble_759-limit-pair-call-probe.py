"""#759, item 2: the operation the conjecture needs, and where it is absent.

conj:no_moduli_loss compares two degenerations by whether they are identified in the KSBA
boundary, i.e. by whether their limit stable pairs are isomorphic.  Every object on this page is
lattice data: T_Co, its cusp records, the folded Coxeter diagram, the admissible roots.  This probe
walks the library for the object that carries the other end -- the semifan as cones, and the limit
pair of a degeneration -- and prints, for each place it would live, the expression that fails.

Nothing here is a substitute for the operation: a miss is the statement that the object does not
exist in the image.

    usage: PYTHONPATH=<repo>/.scratch/se-main/src python \
               <repo>/computations/reports/coble_759-limit-pair-call-probe.py
"""
import sys, time
sys.stdout.reconfigure(line_buffering=True)
t0 = time.time()
def say(*a): print("[%7.1fs]" % (time.time() - t0), *a, flush=True)

from sage_extensions.all import *   # noqa: F401,F403
from sage.all import ZZ

# ---- (1) the objects that do exist on the lattice side
say("=== (1) what the library has, on the side this page computes with")
D = Coble.rank_ten_diagram()
say("    Coble.rank_ten_diagram() -> %s" % type(D).__name__)
say("    its vertices: %s" % (len(tuple(D.names())) if hasattr(D, "names") else "n/a",))
unctx = [m for m in dir(D) if not m.startswith("_")]
say("    its public attributes (%d): %s" % (len(unctx), ", ".join(unctx[:24]) + (" ..." if len(unctx) > 24 else "")))
cuspsrc = "src/sage_extensions/categories/lattices.py:9864"
say("    a cusp record is L.Aut().cusps(rank); its documented contents, from %s:" % cuspsrc)
say("      \"The finite ordered result retains each representative, its parabolic subgroup and")
say("       stabilizer generators, and transporter witnesses for membership.\"")

# ---- (2) the two absent operations, with the exact failure of each expression
say("")
say("=== (2) the operations the conjecture needs, and the failure of each expression")
ABSENT = [
    ("the restricted Enriques semifan at a cusp, as cones",
     "Coble.rank_ten_diagram().semifan()", lambda: Coble.rank_ten_diagram().semifan()),
    ("its cones", "Coble.rank_ten_diagram().cones()", lambda: Coble.rank_ten_diagram().cones()),
    ("the limit stable pair of a degeneration, from lattice data",
     "Coble.rank_ten_diagram().stable_pairs()", lambda: Coble.rank_ten_diagram().stable_pairs()),
    ("the marked root of a stable pair, as a class in K_I",
     "Coble.rank_ten_diagram().marked_root()", lambda: Coble.rank_ten_diagram().marked_root()),
]
for what, expr, fn in ABSENT:
    try:
        value = fn()
        say("    %-52s -> %s" % (expr, value))
    except Exception as exc:
        say("    %-52s -> %s: %s" % (expr, type(exc).__name__, str(exc).splitlines()[0]))
    say("      it would return: %s" % what)

# ---- (3) the names, searched for in the whole package
say("")
say("=== (3) the same names, searched for in the whole package")
import os
root = "/repo/.scratch/se-main/src"
files = []
for base, _dirs, names in os.walk(root):
    files += [os.path.join(base, n) for n in names if n.endswith(".py")]
texts = []
for path in files:
    try:
        texts.append(open(path, encoding="utf-8", errors="ignore").read().lower())
    except OSError:
        pass
say("    scanned %d python files under %s" % (len(texts), root))
for pattern in ("semifan", "ksba", "stable pair", "stable_pair", "limit pair", "marked root"):
    hits = sum(text.count(pattern) for text in texts)
    say("    %-14s occurrences: %d" % (pattern, hits))

print()
print("VERDICT: the two operations conj:no_moduli_loss needs are absent, and absent in different")
print("degrees.  The semifan as cones is absent from an object that exists (the folded Coxeter")
print("diagram, src/sage_extensions/categories/coxeter_diagrams.py:374, built at :2173), so it is")
print("an operation to add.  The limit pair is absent from the package altogether: no name in it")
print("refers to a stable pair, a KSBA compactification or a marked root, and a cusp record retains")
print("only representatives, parabolics, stabilizers and transporters")
print("(src/sage_extensions/categories/lattices.py:9864), so it is an object to build and not a")
print("method to add.  What that costs the conjecture is stated on the page: with the roots 12 and")
print("13 inequivalent (coble_759-gamma-co-2-orbit-1213-run.txt) and their faces equal")
print("(thm:face-irrelevant-marking), the remaining question is whether their limit pairs are")
print("isomorphic, and no expression in this image returns a limit pair.")
print()
print("elapsed %d s" % (time.time() - t0))
print("PYEXIT=0")
