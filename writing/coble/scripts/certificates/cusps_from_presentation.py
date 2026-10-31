"""The four degree-two cusps from the G24 source presentation, through the public contracts.

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/cusps_from_presentation.py

Environment: run inside the image's launcher environment, which includes
JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: .  Dropping that variable makes the Julia bridge
fail on a missing JSON package (the depot is in /opt/julia-depot, not on the default path), and
the overlattice calls below need the bridge.

Consumer for sage-extensions at main a0b8cdd2 ("an integral lattice's radical quotient is taken
at the lattice owner").  Construction, using only named public contracts:

    G24 = Matrix(ZZ, G24)
P = Lattices(ZZ)([list(row) for row in G24.rows()])                 24 generators of a rank-19 lattice
    proj = P.radical_quotient_projection()   P ->> P/rad(P), exact codomain
    Q = P.radical_quotient()               N = P/rad(P)
    w = P.linear_combination(source_marks)  the source's null vector, an element of P
    v = proj(w)                            its class in N
    K = Q.primitive_isotropic_subobject(v).isotropic_reduction()

K is the cusp's boundary lattice v^perp/Zv.  It is compared with the labelled root lattice only
through maintained constructions, never by invariants alone.
"""
import sys

from sage.all import ZZ, Matrix
from sage.combinat.root_system.cartan_type import CartanType

from sage_extensions.all import IsotropicReductions, Lattices  # noqa: F401

print("python", sys.version.split()[0])
import sage_extensions
print("sage_extensions", sage_extensions.__file__)

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

G24 = Matrix(ZZ, G24)
P = Lattices(ZZ)([list(row) for row in G24.rows()])
print("P: rank", P.module_rank(), "det", P.determinant(), "radical rank",
      P.radical().module_rank())
proj = P.radical_quotient_projection()
Q = P.radical_quotient()
print("proj:", type(proj).__name__, "| codomain:", type(proj.codomain()).__name__,
      "| codomain is Q:", proj.codomain() is Q)
print("Q: rank", Q.module_rank(), "| det", Q.determinant(), "| signature", Q.signature_pair())
print("Q has primitive_isotropic_subobject:", hasattr(Q, "primitive_isotropic_subobject"))

def root_lattice(letter, rank):
    shape = CartanType([letter, rank])
    return Lattices(ZZ)([[-int(x) for x in row] for row in shape.cartan_matrix().rows()])

U = Lattices(ZZ)([[0, 1], [1, 0]])
E8, A1 = root_lattice("E", 8), root_lattice("A", 1)
N = U + E8 + E8 + A1
print("N: rank", N.module_rank(), "det", N.determinant(), "signature", N.signature_pair())
print("Q is N:", Q.is_isometric(N))

CHAINS = {
    "A~17":    (list(range(18)), ("A", 17)),
    "D~10":    ([18, 17] + list(range(8)) + [19], ("D", 10)),
    "E~8^(1)": ([13, 14, 15, 16, 17, 0, 1, 2, 18], ("E", 8)),
    "D~16":    ([19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 18], ("D", 16)),
}
LABELS = {
    "A~17":    root_lattice("A", 17),
    "D~10":    root_lattice("D", 10) + root_lattice("E", 7),
    "E~8^(1)": E8 + E8 + A1,
    "D~16":    root_lattice("D", 16) + A1,
}

for name, (chain, typ) in CHAINS.items():
    block = Matrix(ZZ, [[G24[a, b] for b in chain] for a in chain])
    basis = block.kernel().basis_matrix()
    a = [x for x in basis[0]]
    scale = min(abs(x) for x in a if x != 0)
    a = [x / scale for x in a]
    assert all(x in ZZ for x in a)
    coeffs = {node: int(c) for node, c in zip(chain, a) if c}
    kac = sorted(CartanType([typ[0], typ[1], 1]).a().values())
    print(f"\n{name}: marks {coeffs}")
    print("  multiset equals the Kac marks:", sorted(int(x) for x in a if x) == kac
          or sorted(int(x) for x in a) == kac)
    w = P.linear_combination(coeffs)
    print("  w isotropic in P:", w.is_isotropic())
    v = proj(w)
    print("  v = proj(w) in Q: isotropic", v.is_isotropic())
    try:
        I = Q.primitive_isotropic_subobject(v)
        K = I.isotropic_reduction()
        print("  K = v^perp/Zv: rank", K.module_rank(), "det", K.determinant(),
              "signature", K.signature_pair(), "even", K.is_even())
        label = LABELS[name]
        dm = K.discriminant_module()
        print("  discriminant module: order", dm.cardinality(), "invariants",
              dm.invariant_factors())
        det_label, det_K = abs(label.determinant()), abs(K.determinant())
        print("  label: rank", label.module_rank(), "det", label.determinant(),
              "-> index^2 = det(label)/det(K) =", det_label, "/", det_K, "=",
              det_label // det_K if det_K else "?")
        try:
            print("  K isometric to the label:", K.is_isometric(label))
        except Exception as error:
            print("  K.is_isometric raised:", type(error).__name__, str(error)[:120])
        try:
            inclusions = [inc for inc in label.even_overlattice_inclusions()
                          if inc.codomain().is_isometric(K)]
            print("  label's even overlattice inclusions with K as codomain:", len(inclusions))
        except Exception as error:
            print("  even_overlattice_inclusions raised:", type(error).__name__,
                  str(error)[:200])
    except Exception as error:
        print("  FAILED:", type(error).__name__)
        print("   full message:", error)
