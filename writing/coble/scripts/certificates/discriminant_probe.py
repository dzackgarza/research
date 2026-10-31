"""Smallest semantic example for the discriminant module of a lattice of determinant -2.

Run on the shared development image (Sage 11.0.beta5, Python 3.14.10) with
`sage_extensions` at the published revision 28407ef:

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/discriminant_probe.py

Question: a rank-one lattice < -2 > -- and the rank-17 quotient of a degree-two cusp, which
also has determinant -2 -- has discriminant group Z/2, of order 2.  Does the library's
`discriminant_module()` return that group, and what does `discriminant_projection()` carry?
`module_rank()` is not the answer to that question: Z/2 is a torsion module and has module
rank 0 while being of order 2, so a printed 0 says nothing about triviality.
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
    print(f"\nL with Gram {gram}: rank {L.module_rank()} det {L.determinant()}")
    print("  discriminant object:", type(A).__name__)
    print("  module_rank:", A.module_rank())
    try:
        print("  cardinality:", A.cardinality())
    except Exception as error:
        print("  cardinality raised:", type(error).__name__, error)
    for name in ("invariant_factors", "elementary_divisors", "gens", "generators",
                 "torsion_order", "order"):
        if hasattr(A, name):
            try:
                print(f"  {name}:", getattr(A, name)())
            except Exception as error:
                print(f"  {name} raised:", type(error).__name__, error)
    if hasattr(A, "torsion_submodule"):
        try:
            T = A.torsion_submodule()
            print("  torsion_submodule order:", T.cardinality() if hasattr(T, "cardinality") else T)
        except Exception as error:
            print("  torsion_submodule raised:", type(error).__name__, error)
    try:
        proj = L.discriminant_projection()
        print("  discriminant_projection:", type(proj).__name__, "->", proj.codomain())
        print("  projection is_surjective:", getattr(proj, "is_surjective", lambda: "n/a")())
    except Exception as error:
        print("  discriminant_projection raised:", type(error).__name__, error)
