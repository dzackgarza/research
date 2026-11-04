"""The marked inclusion: the source's root generators inside the cusp quotient.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/cusp_label_inclusions.py

The question is not which abstract overlattice of the label occurs -- the retained candidates in
a pair are isometric to the computed quotient by construction, so no isometry invariant can
separate them -- but which inclusion is *marked* by the source's own root generators.  Per node
of the labelled component, with the public contracts only:

    qroot   = proj(P.module_generator(node))              P ->> Q = P/rad(P)
    lifted  = K.orthogonal_complement().inclusion().preimage(qroot)
    image   = K.projection()(lifted)                      the image in K
    S       = K.sublattice_from(images, saturate=False)   the span
    j       = S.inclusion(),  j.gluing_subgroup()         the quotient inside A_S

The node -> image family is retained, so the marked inclusion is recorded with its index and its
glue rather than inferred from a determinant ratio.
"""
import sys

from sage.all import ZZ, Matrix
from sage.combinat.root_system.cartan_type import CartanType

from sage_extensions.all import Lattices  # noqa: F401

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
proj = P.radical_quotient_projection()
Q = P.radical_quotient()
print("P: rank", P.module_rank(), "det", P.determinant(), "| Q: rank", Q.module_rank(),
      "det", Q.determinant())

CUSPS = {
    "A~17":    (list(range(18)), ("A", 17), list(range(18))),
    "D~10":    ([18, 17] + list(range(8)) + [19], ("D", 10),
                [18, 17] + list(range(8)) + [19] + list(range(9, 16)) + [20]),
    "E~8^(1)": ([13, 14, 15, 16, 17, 0, 1, 2, 18], ("E", 8),
                [13, 14, 15, 16, 17, 0, 1, 2, 18] + list(range(4, 12)) + [19] + [20, 23]),
    "D~16":    ([19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 18], ("D", 16),
                [19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 18] + [3, 23]),
}

for name, (chain, typ, label_nodes) in CUSPS.items():
    block = Matrix(ZZ, [[G24[a, b] for b in chain] for a in chain])
    basis = block.kernel().basis_matrix()
    a = [x for x in basis[0]]
    scale = min(abs(x) for x in a if x != 0)
    a = [x / scale for x in a]
    marks = {node: int(c) for node, c in zip(chain, a) if c}
    print(f"\n=== {name}: marks on the source nodes {marks}")
    print("  multiset equals the Kac marks:",
          sorted(marks.values()) == sorted(CartanType([typ[0], typ[1], 1]).a().values()))
    v = proj(P.linear_combination(marks))
    I = Q.primitive_isotropic_subobject(v)
    K = I.isotropic_reduction()
    print("  K: rank", K.module_rank(), "det", K.determinant(), "sig", K.signature_pair())
    perp_inclusion = K.orthogonal_complement().inclusion()
    images = {}
    for node in label_nodes:
        qroot = proj(P.module_generator(node))
        lifted = perp_inclusion.preimage(qroot)
        images[node] = K.projection()(lifted)
    print("  node -> image family retained for", len(images), "roots")
    try:
        S = K.sublattice_from(tuple(images.values()), saturate=False)
        print("  S = sublattice_from(images, saturate=False): rank", S.module_rank(),
              "det", S.determinant())
        j = S.inclusion()
        print("  j = S.inclusion():", type(j).__name__, "| primitive:", j.is_primitive())
        detK, detS = abs(K.determinant()), abs(S.determinant())
        print("  [K : S]^2 = det(S)/det(K) =", detS, "/", detK, "=",
              detS // detK if detK else "?")
        try:
            g = j.gluing_subgroup()
            print("  j.gluing_subgroup():", type(g).__name__,
                  "order", g.cardinality() if hasattr(g, "cardinality") else g,
                  "invariants", g.invariant_factors() if hasattr(g, "invariant_factors") else "")
        except Exception as error:
            print("  gluing_subgroup raised:", type(error).__name__, str(error)[:200])
    except Exception as error:
        print("  sublattice_from failed:", type(error).__name__)
        print("   full message:", error)
