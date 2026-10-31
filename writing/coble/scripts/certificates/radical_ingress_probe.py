"""Public ingress check: IsotropicReductions over the radical's inclusion.

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/radical_ingress_probe.py

The point: `P.radical_quotient()` returns a presented module that already carries the descended
form -- a presented module is not evidence that the form is missing -- and the reason the cusp
construction stops there is a lattice specialization/dispatch gap, assigned to the
sage-extensions project.  The documented public ingress to the same quotient *as a lattice* is

    IsotropicReductions(P.base_ring())(P.radical().inclusion())

This script checks that ingress, and the documented projection name
`P.radical_quotient_projection()`, without reaching into private machinery or building any
quotient of its own.
"""
import sys

from sage.all import ZZ, Matrix
from sage.combinat.root_system.cartan_type import CartanType

from sage_extensions.all import IsotropicReductions, Lattices  # noqa: F401

print("python", sys.version.split()[0])

CAND = dict(
    one=[(i, (i + 1) % 18) for i in range(18)] + [(0, 18), (6, 19), (12, 20)],
    two=[(18, 21), (21, 9), (19, 22), (22, 15), (20, 23), (23, 3)],
    six=[(21, 22), (22, 23), (23, 21)],
)
G24 = [[0] * 24 for _ in range(24)]
for i in range(24):
    G24[i][i] = -2
for key, mult in (("one", 1), ("two", 2), ("six", 6)):
    for a, b in CAND[key]:
        G24[a][b] = G24[b][a] = mult

P = Lattices(ZZ)(G24)
print("P: rank", P.module_rank(), "det", P.determinant(), "radical rank",
      P.radical().module_rank())

print("\ndocumented projection name:")
print("  has radical_quotient_projection:", hasattr(P, "radical_quotient_projection"))
Q = P.radical_quotient()
try:
    proj = P.radical_quotient_projection()
    print("  P.radical_quotient_projection():", type(proj).__name__,
          "->", proj.codomain())
except Exception as error:
    print("  P.radical_quotient_projection failed:", type(error).__name__)
    print("   full message:", error)
    proj = None

print("\npublic ingress to the same quotient as a lattice:")
try:
    R = IsotropicReductions(P.base_ring())(P.radical().inclusion())
    print("  IsotropicReductions(P.base_ring())(P.radical().inclusion()):", type(R).__name__)
    K = R.isotropic_reduction()
    print("  isotropic_reduction:", type(K).__name__, "rank", K.module_rank(),
          "det", K.determinant(), "signature", K.signature_pair())
    N = (Lattices(ZZ)([[0, 1], [1, 0]])
         + Lattices(ZZ)([[-2]])
         + Lattices(ZZ)([[-2]]))          # a stand-in; replaced below by E8^2 + A1
except Exception as error:
    print("  ingress failed:", type(error).__name__)
    print("   full message:", error)
    K = None

if K is not None:
    print("\nthe descended quotient as a lattice is available; the cusp step from here is")
    print("  K.primitive_isotropic_subobject(image).isotropic_reduction()")
    print("with image the projection of a mark combination, which needs the transport from")
    print("the presented module to K -- the dispatch gap assigned to sage-extensions.")
