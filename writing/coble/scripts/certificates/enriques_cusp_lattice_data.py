"""The lattice data quoted for the Enriques cusps, through the maintained two-elementary API.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/enriques_cusp_lattice_data.py

Cusp 1 quotes T-bar = (18,2,0)_1 = U(2) + E8^2 with invariant sublattice U(2) + E8(2); cusp 2
quotes (18,0,0)_1 = U + E8^2 with U + E8(2).  Both are checked here with
EvenTwoElementaryLattices(...).two_elementary_invariants(), together with their invariant
sublattices: (18,2,0) and (10,10,0) for cusp 1, (18,0,0) and (10,8,0) for cusp 2, all agreeing
with the text.

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

# cusp 2 of the Enriques chapter: (18,0,0)_1 = U + E8^2 with invariant sublattice U + E8(2)
U = Lattices(ZZ)([[0, 1], [1, 0]])
T2_ = U + E8 + E8
S2_ = U + E8_2
print("U+E8^2: rank", T2_.module_rank(), "det", T2_.determinant(), "sig", T2_.signature_pair(),
      "invariants", EvenTwoElementaryLattices(T2_.base_ring())(T2_).two_elementary_invariants())
print("U+E8(2): rank", S2_.module_rank(), "det", S2_.determinant(), "sig", S2_.signature_pair(),
      "invariants", EvenTwoElementaryLattices(S2_.base_ring())(S2_).two_elementary_invariants())
