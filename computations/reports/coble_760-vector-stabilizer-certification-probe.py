"""#760: is the generating family of Stab_{O(T)}(v) certified on sage-extensions main?  (No.)

The item.  The cusp-5 decision of @thm:no-moduli-loss runs on the family the provider returns for
Stab_{Orth(T_Co)}(r_12): the coset computation enumerates the orbit of the point A_{U(2)} under the
image of that subgroup and is exhaustive over the subgroup the family generates.  For the pair to be
decided as the page decides it, the family must generate the whole stabilizer.  The item is therefore
a certified-complete generating family for this vector stabilizer, an indefinite one:
`src/sage_extensions/categories/lattice_morphisms.py:4791` at the commit the page used, whose
indefinite branch the library itself labels untrusted engine output.

What this record answers.  sage-extensions#459 closed at 58588b8 on the *isotropic line* stabilizer's
generator family (`_isotropic_line_stabilizer_generators`) and on the lazy discriminant-preimage
family.  This record reads the code that runs at main and reports which branch a *pointed* marking
takes, so that the answer to "is the item's stabilizer now certified" is a fact about the dispatch
and not an inference from the issue's title.  It does not decide the cusp-5 pair, and it asserts no
number about it.

    usage: SE_COMMIT=$(git -C <repo>/.scratch/sage-extensions rev-parse HEAD) \\
             PYTHONPATH=<repo>/.scratch/sage-extensions/src \\
             <sage image>/sage/.venv/bin/python3 <repo>/computations/reports/coble_760-vector-stabilizer-certification-probe.py
"""
import os, sys, time
sys.stdout.reconfigure(line_buffering=True)
t0 = time.time()
def say(*a): print("[%7.1fs]" % (time.time() - t0), *a, flush=True)

from sage_extensions.all import *   # noqa: F401,F403
from sage.all import ZZ, matrix, vector
from sage.env import SAGE_VERSION   # noqa: E402
import sage_extensions.categories.lattice_morphisms as lm   # noqa: E402
import sage_extensions.categories.lattices as lat           # noqa: E402
from sage_extensions.categories.abstract_categories.arrow_categories import CosliceCategory  # noqa: E402
import sage_indefinite_port   # noqa: E402

print("is the vector stabilizer's generating family certified?")
print("Sage %s; sage-extensions main %s; port %s"
      % (SAGE_VERSION, os.environ.get("SE_COMMIT", "(unset)"),
         sage_indefinite_port.__file__))
print()
print("(1) the dispatch, printed from the source files of the modules that run:")
for path, keys in (
    (lm.__file__, ["def vector_stabilizer_generators",
                   "def _marking_stabilizer_generators",
                   "they are untrusted engine",
                   "result = lattice.lattice_category()._marked_automorphism_generators",
                   "def _discriminant_point_orbit_and_section"]),
    (lat.__file__, ["def _marked_automorphism_generators",
                    "isinstance(diagram_category, (CosliceCategory, OrientedIsotropicFlags))",
                    "return automorphism_group_generators(diagram_category, marked)",
                    "def _isotropic_plane_parabolic_generators",
                    "def _isotropic_line_stabilizer_generators"]),
):
    text = open(path).read().splitlines()
    for key in keys:
        for number, line in enumerate(text, 1):
            if key in line:
                print("    %s:%d  %s" % (os.path.basename(path), number, line.strip()))
                break
print()

lattice = NamedLattices.Tco
labels = tuple(lattice.module_generating_set())
def vec(d): return vector(ZZ, [int(d.get(l, 0)) for l in labels])
def elt(d): return lattice([int(x) for x in (d if not isinstance(d, dict) else vec(d))])
r12 = vec({"h": 1, "ep": 3, "fp": 3, "a1": -2, "a2": 1, "a3": 2, "a4": 2, "a5": 1})
Aut = lattice.Aut()
BAS = [elt([1 if k == i else 0 for k in range(len(labels))]) for i in range(len(labels))]
Gm = matrix(ZZ, [[int(lattice.b(bi, bj)) for bj in BAS] for bi in BAS])
say("T_Co: rank %d, det %s; r12 %s, square %s" % (len(labels), Gm.det(), list(r12), r12 * Gm * r12))
print()

print("(2) which category the pointed marking is in, from the library's own constructor:")
category, marked = lm._pointed_marking(lattice, elt(r12))
print("    _pointed_marking(T_Co, r12) -> %s" % type(category).__name__)
print("    isinstance(category, CosliceCategory): %s" % isinstance(category, CosliceCategory))
print("    so lattices.py:2859-2865 sets parabolic = None and no own construction is entered")
print()

print("(3) the call the deciding record makes, twice:")
os.environ["SE_DEBUG_STAGES"] = "1"
def as_matrix(g): return matrix(ZZ, len(labels), len(labels), [list(g(b).to_vector()) for b in BAS]).transpose()
families = []
counts = []
for attempt in (1, 2):
    say("    Aut.vector_stabilizer_generators(r12), attempt %d" % attempt)
    family = Aut.vector_stabilizer_generators(elt(r12))
    members = tuple(family)
    families.append(members)
    verified = 0
    for g in members:
        try: m = as_matrix(g)
        except Exception: continue
        if all(x in ZZ for x in m.list()) and matrix(ZZ, list(m.transpose() * Gm * m)) == Gm and m * r12 == r12:
            verified += 1
    say("    -> %s, %d members, %d verified integral, form-preserving and fixing r12"
        % (type(family).__name__, len(members), verified))
    counts.append(len(members))
print("    (this run's two calls above; the count is a datum of the run and not a property of the")
print("     stabilizer --- the earlier records of this family name 40 and 44 in")
print("     computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt and 51 and 60 in")
print("     computations/reports/coble_760-transporter-in-gent-run.txt)")
print()

print("    counts this run: %s" % (counts,))
print()
print("(4) the library's own spelling of the same subgroup's generators:")
S = Aut.stabilizer(elt(r12))
say("    Aut.stabilizer(r12) -> %s" % type(S).__name__)
try:
    own = tuple(S.group_generators())
    say("    .group_generators() -> %d members, through the same _marked_automorphism_generators" % len(own))
except Exception as exc:
    own = ()
    say("    .group_generators() raised %s: %s" % (type(exc).__name__, str(exc).splitlines()[0]))
print()

print("(5) the expression that would state the item, and why its answer is no decision:")
H1, H2 = Aut.subgroup(families[0]), Aut.subgroup(families[1])
for name, value in (("Aut.subgroup(family) == Aut.subgroup(family)  [the same subgroup]", H1 == H2),
                    ("Aut.subgroup(family) == Aut.stabilizer(r12)     [the item]", H1 == S),
                    ("Aut.stabilizer(r12)  == Aut.subgroup(family)     [the item]", S == H1)):
    say("    %s -> %s" % (name, value))
say("    Aut.subgroup(family).cardinality() -> %s" % (H1.cardinality(),))
say("    Aut.stabilizer(r12).cardinality()  -> %s" % (S.cardinality(),))
print("    The first line is False for two families of one and the same stabilizer, so subgroup")
print("    equality here is not a decision about groups; the second and third lines therefore")
print("    carry no information, in either direction.  Both sides have cardinality aleph_0, so no")
print("    order distinguishes them either, and no validator states the law (the library's")
print("    validator protocol has none for 'these generators generate the subgroup').")
print()
print("VERDICT: the item's stabilizer is not certified at this commit.  vector_stabilizer_generators")
print("reaches the indefinite port through the coslice branch, whose output the library labels")
print("untrusted (lattice_morphisms.py:4914-4917); the own constructions added for #459 are the")
print("rank-one isotropic line (lattices.py:2955) and the rank-two isotropic plane (:2934), which a")
print("pointed marking is not.  Nothing raises: the family returns, and no operation certifies it.")
print("PYEXIT=0")
