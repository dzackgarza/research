"""#759 item 1: the certified stabilizer of a vector is absent from the provider, at a named commit.

Item 1 of research#759 asks for the operation that decides the cusp-5 pair (12,13), and the
decision recorded on the page runs on the family that
``O(T_Co).vector_stabilizer_generators`` returns for ``Stab(r_12)``.  The provider's own
docstring says what that family is and what it is not: for an indefinite lattice the apex
stabilizer "is not constructed" and the generators are the marked-diagram decision's own,
from ``sage-indefinite-port``, which ``_computed_group_generators`` labels "untrusted engine
output".  So the family is not a certified generating set, and the page's coset computation
is exhaustive only over the subgroup that family generates.

This record checks the three claims of that paragraph against the provider sources at the
commit it names, so that "the operation is absent" is a printed fact and not a repetition:

  1. the isotropic marking dispatch has slots for a line and a plane and no slot for a vector;
  2. ``vector_stabilizer_generators`` documents the discarded apex stabilizer for an indefinite
     lattice, and routes through the untrusted engine family;
  3. ``_computed_group_generators`` says in its docstring that all its answers are untrusted
     engine output.

It does not run the provider, does not need Sage, and makes no claim about the mathematics:
the mathematics is `ksba.md` @rmk:coble-root-orbits-cusp-five and @thm:no-moduli-loss, whose
cusp-5 step stays modulo the family until sage-extensions#603 delivers the certified one.

    usage: python3 computations/reports/coble_759-vector-stabilizer-absence.py [provider-root]

The provider root defaults to $SE_ROOT, then to .scratch/sage-extensions beside this checkout.
"""
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parents[2]


def provider_root():
    for candidate in (sys.argv[1] if len(sys.argv) > 1 else None,
                      os.environ.get("SE_ROOT"),
                      str(REPO / ".scratch/sage-extensions"),
                      str(REPO.parent / ".scratch/sage-extensions"),
                      str(REPO.parent.parent / ".scratch/sage-extensions")):
        if candidate and (pathlib.Path(candidate) / "src/sage_extensions/categories/lattices.py").is_file():
            return pathlib.Path(candidate)
    return None


root = provider_root()
if root is None:
    print("no provider checkout found; pass its root as argv[1] or set SE_ROOT")
    print("PROBE_EXIT=2")
    raise SystemExit(2)

try:
    commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                            capture_output=True, text=True, timeout=60).stdout.strip()
except Exception as exc:                      # pragma: no cover - git absent
    commit = "unknown (%s)" % exc
print("provider: %s" % root)
print("provider commit: %s" % (commit or "unknown"))
print()

lattices = (root / "src/sage_extensions/categories/lattices.py").read_text().splitlines()
morphisms = (root / "src/sage_extensions/categories/lattice_morphisms.py").read_text().splitlines()


def find(lines, needle, start=0):
    for i in range(start, len(lines)):
        if needle in lines[i]:
            return i
    return None


def defline(lines, name):
    return find(lines, "    def %s(" % name)


def body(lines, name):
    """The def line and docstring of one method, as (line-number, text) pairs."""
    start = defline(lines, name)
    if start is None:
        return []
    out = []
    depth = 0
    for i in range(start, min(len(lines), start + 200)):
        out.append((i + 1, lines[i]))
        depth += lines[i].count('"""')
        if i > start and depth >= 2:
            break
    return out


print("=== 1. the isotropic marking dispatch: which markings have a library-owned slot")
i = find(lattices, "def _isotropic_parabolic_generators(")
print("lattices.py:%d" % (i + 1))
for j in range(i, min(len(lattices), i + 60)):
    line = lattices[j]
    if ("_isotropic_plane_parabolic_generators" in line or
            "_isotropic_line_stabilizer_generators" in line or
            "return None" in line or "plane = " in line):
        print("  :%-6d %s" % (j + 1, line.strip()))
plane_def = defline(lattices, "_isotropic_plane_parabolic_generators")
line_def = defline(lattices, "_isotropic_line_stabilizer_generators")
print("  the two slots are defined at :%d (plane) and :%d (line)" % (plane_def + 1, line_def + 1))
vector_slot = find(lattices, "_pointed", i) is not None or find(lattices, "vector_stabilizer", i) is not None
print("  a slot for a primitive vector (a pointed marking) in this dispatch: %s" % vector_slot)
print()

print("=== 2. the call item 1 uses, and what its docstring says for an indefinite lattice")
for number, text in body(morphisms, "vector_stabilizer_generators"):
    if ("not constructed" in text or "untrusted" in text or "marked-diagram" in text
            or "def vector_stabilizer_generators" in text or "indefinite" in text
            or "apex stabilizer is discarded" in text):
        print("  :%-6d %s" % (number, text.strip()))
print()

print("=== 3. the family behind it, and the provider's own word for it")
for number, text in body(morphisms, "_computed_group_generators"):
    if "untrusted" in text or "sage_indefinite_port" in text:
        print("  :%-6d %s" % (number, text.strip()))
print()

print("=== verdict")
absent = (not vector_slot) and plane_def is not None and line_def is not None
print("a library-owned stabilizer of a primitive vector in an indefinite lattice, as for lines "
      "and planes: %s" % ("ABSENT at this commit" if absent else "present -- re-check this record"))
print("the operation is owned by sage-extensions#603 (Certified generators of the stabilizer of a")
print("vector in an indefinite lattice), open at the time of this record.")
print("consumer: writing/coble/stable-limits/ksba.md @rmk:coble-root-orbits-cusp-five and")
print("@thm:no-moduli-loss, whose cusp-5 step is exhaustive only over the family this call returns")
print("(`computations/reports/coble_760-vector-stabilizer-certification-run.txt`).")
print("PROBE_EXIT=0" if absent else "PROBE_EXIT=3")
raise SystemExit(0 if absent else 3)
