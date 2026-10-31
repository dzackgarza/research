"""The lattice data quoted for the Enriques cusps, through the maintained two-elementary API.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/enriques_cusp_lattice_data.py

Cusp 1 of the Enriques chapter quotes T-bar = (18,2,0)_1 = U(2) + E8^2 with invariant sublattice
U(2) + E8(2).  This checks both lattices with EvenTwoElementaryLattices(...).two_elementary_invariants()
and records the result: (18,2,0) for U(2) + E8^2 -- the quoted invariants -- and (10,10,0) for
U(2) + E8(2), which is the rank-10 invariant sublattice the 180-degree rotation leaves.

"""
from sage.all import ZZ, CartanType
from sage_extensions.all import EvenTwoElementaryLattices, Lattices
E8 = Lattices(ZZ)([[-int(x) for x in r] for r in CartanType(["E", 8]).cartan_matrix().rows()])
E8_2 = Lattices(ZZ)([[-2*int(x) for x in r] for r in CartanType(["E", 8]).cartan_matrix().rows()])
U2 = Lattices(ZZ)([[0, 2], [2, 0]])
T = U2 + E8 + E8
print("U(2)+E8^2: rank", T.module_rank(), "det", T.determinant(), "signature", T.signature_pair())
print("  even:", T.is_even(), "| two-elementary invariants:",
      EvenTwoElementaryLattices(T.base_ring())(T).two_elementary_invariants())
S = U2 + E8_2
print("U(2)+E8(2): rank", S.module_rank(), "det", S.determinant(), "signature", S.signature_pair())
print("  even:", S.is_even(), "| two-elementary invariants:",
      EvenTwoElementaryLattices(S.base_ring())(S).two_elementary_invariants())
