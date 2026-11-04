"""Minimal reproducer for a sage-extensions defect: presented-module `torsion_submodule()`.

Kept separate from the discriminant probe on purpose: this is a library defect to hand to the
sage-extensions project, not a fact about any lattice in the Coble manuscript.

Runtime it was observed on: the shared development image, Sage 11.0.beta5 / Python 3.14.10,
sage_extensions at published revision 28407ef.

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/sage_extensions_repro_torsion_submodule.py

Defect. `L.discriminant_module().torsion_submodule()` raises

    TypeError: CategoricalIsomorphism.__init__() missing 1 required positional argument:
    'inverse_computation'

for the rank-one lattices < -2 >, < -4 >, < -8 > and < 2 >, whose discriminant modules are
Z/2, Z/4, Z/8 and Z/2 -- all torsion, so the torsion submodule is the whole module and the
answer is known independently.  The same call succeeds on diag(-2, -1), whose discriminant
module is also Z/2, so the failure is not about the group: it is in the construction of the
isomorphism, which is handed over without its inverse computation.

Expectation (from the discriminant module itself, not from any computation here): the torsion
submodule of a torsion module is that module, so for < -2 > the answer is an isomorphism from
the module of order 2 to itself.
"""
import sys

from sage.all import ZZ

from sage_extensions.all import Lattices  # noqa: F401

print("python", sys.version.split()[0])
import sage_extensions
print("sage_extensions", sage_extensions.__file__)

for gram in ([[-2]], [[-4]], [[-8]], [[2]], [[-2, 0], [0, -1]]):
    L = Lattices(ZZ)(gram)
    A = L.discriminant_module()
    print(f"\nL = {gram}: det {L.determinant()}, discriminant module of order {A.cardinality()},"
          f" invariant factors {A.invariant_factors()}")
    try:
        T = A.torsion_submodule()
        print("  torsion_submodule ->", T)
    except Exception as error:
        print("  torsion_submodule raised:", type(error).__name__ + ":", error)
