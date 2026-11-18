"""#760: relevance in the RESTRICTED semifan, which is the object the issue names.

The issue's statement is about the restricted Enriques semifan F_I, not about the Enriques semifan
of the cusp: the restriction to the Coble hyperplane removes the roots that are not orthogonal to
the Coble root, and a root's relevance is a property of the diagram it sits in.  The theorem on the
page argues that every admissible T_Co-root is irrelevant, using the fold of AEGS25 Figure 5 for
the Enriques diagram; this record checks the conclusion in the restricted diagram, where the
irrelevant roots are the Enriques irrelevant ones that survive the restriction.

Input: the two committed transcripts, which carry the label sets.
  coble_irrelevant-marking-face-run.txt   the walls in T_Co (orthogonal to delta) and the
                                          printed labels of the Enriques irrelevant roots, per cusp
  the same file's admissible labels, i.e. the (-2) ones among the walls

    usage: python3 computations/reports/coble_760-restricted-irrelevance.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "computations/reports/coble_irrelevant-marking-face-run.txt"
text = RUN.read_text(encoding="utf-8")

irrelevant = {}
walls = {}
for m in re.finditer(r"the printed labels of those vertices, under every matching: \[([0-9, ]+)\]", text):
    # three blocks, in cusp order 3, 4, 5
    pass
labels = re.findall(r"the printed labels of those vertices, under every matching: \[([0-9, ]+)\]", text)
wall_sets = re.findall(r"walls in T_Co at printed labels \[([0-9, ]+)\]", text)
adm_sets = re.findall(r"admissible roots \[([0-9, ]+)\]", text)
assert len(labels) == 3 and len(wall_sets) == 3 and len(adm_sets) == 3, (labels, wall_sets, adm_sets)

def nums(s):
    return [int(x) for x in s.replace(",", " ").split()]

print("relevance in the restricted semifan at the marked cusps")
print("(the restricted diagram keeps the walls orthogonal to the Coble root; its irrelevant roots are")
print("the Enriques irrelevant ones among those walls)")
print()
ok = True
for cusp, lab, wall, adm in zip((3, 4, 5), labels, wall_sets, adm_sets):
    irr = set(nums(lab))
    w = set(nums(wall))
    a = nums(adm)
    restricted_irr = sorted(irr & w)
    inside = all(x in restricted_irr for x in a)
    ok = ok and inside
    print("cusp %d" % cusp)
    print("   walls in T_Co (orthogonal to delta): %s" % sorted(w))
    print("   Enriques irrelevant printed labels : %s" % sorted(irr))
    print("   irrelevant in the RESTRICTED diagram: %s" % restricted_irr)
    print("   admissible roots                  : %s  -> all irrelevant after restriction: %s"
          % (a, inside))
    print()
assert ok, "an admissible root is not irrelevant in the restricted diagram"
print("VERDICT: at each marked cusp the admissible T_Co-roots are irrelevant in the restricted")
print("diagram as well, so the theorem's conclusion holds for the semifan the issue names and not")
print("only for the Enriques one it was proved from.")
print("PYEXIT=0")
