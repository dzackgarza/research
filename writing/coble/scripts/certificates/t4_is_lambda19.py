"""T_{2d} at 2d = 4 is Laza--O'Grady's Lambda_19, hence their D_17 classification applies.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/t4_is_lambda19.py

The manuscript's transcendental lattice is T_{2d} = <-2d> + U^2 + E8^2 of rank 21, so the degree-4
case is 2d = 4 and T_4 = <-4> + U^2 + E8^2, not T_8.  Laza--O'Grady (arXiv:1801.04845) set
Lambda_N = U^2 + D_{N-2}, so n = 17 in their Theorem A.6 is N = 19 and Lambda_19 = U^2 + D_17, of
rank 21 and determinant -4.  This script checks that the two lattices are the same one:
is_isometric returns True, with equal rank, determinant, signature, parity and discriminant module.

"""
from sage.all import ZZ, CartanType
from sage_extensions.all import Lattices
E8 = Lattices(ZZ)([[-int(x) for x in r] for r in CartanType(["E", 8]).cartan_matrix().rows()])
D17 = Lattices(ZZ)([[-int(x) for x in r] for r in CartanType(["D", 17]).cartan_matrix().rows()])
U = Lattices(ZZ)([[0, 1], [1, 0]])
A4 = Lattices(ZZ)([[-4]])
T4 = A4 + U + U + E8 + E8                      # the manuscript's T_{2d} at 2d = 4
L19 = U + U + D17                              # Laza-O'Grady's Lambda_19, n = 17
for name, L in (("T_4 = <-4>+U^2+E8^2", T4), ("Lambda_19 = U^2+D_17", L19)):
    dm = L.discriminant_module()
    print(name, ": rank", L.module_rank(), "det", L.determinant(), "sig", L.signature_pair(),
          "even", L.is_even(), "| A order", dm.cardinality(), "invariants", dm.invariant_factors())
print("isometric:", T4.is_isometric(L19))
