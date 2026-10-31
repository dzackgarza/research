"""The marked inclusion: the source's root generators inside the cusp quotient.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/cusp_label_inclusions.py

The question this answers is not which abstract overlattice of the label occurs -- both retained
candidates in a pair are isometric to the computed quotient, so no isometry invariant can
separate them -- but which inclusion is *marked*: the one cut out by the source's own root
generators.  So each label root r_i of the component is pushed through

    P -> Q = P/rad(P)        P.radical_quotient_projection()
    Q ->> K = v^perp/<v>     the isotropic reduction of I = <v>

and the subobject of K that the images span is recorded with its index and quotient.  The
retained maps are the library's own; no root is re-created as an abstract Cartan lattice here.
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
    "A~17":    (list(range(18)), ("A", 17)),
    "D~10":    ([18, 17] + list(range(8)) + [19], ("D", 10)),
    "E~8^(1)": ([13, 14, 15, 16, 17, 0, 1, 2, 18], ("E", 8)),
    "D~16":    ([19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 18], ("D", 16)),
}
LABEL_NODES = {          # the roots whose images are the label: the component plus its partners
    "A~17":    list(range(18)),
    "D~10":    [18, 17] + list(range(8)) + [19] + list(range(9, 16)) + [20],
    "E~8^(1)": [13, 14, 15, 16, 17, 0, 1, 2, 18] + [4, 5, 6, 7, 8, 9, 10, 11, 19] + [20, 23],
    "D~16":    [19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 18] + [3, 23],
}

for name, (chain, typ) in CUSPS.items():
    block = Matrix(ZZ, [[G24[a, b] for b in chain] for a in chain])
    basis = block.kernel().basis_matrix()
    a = [x for x in basis[0]]
    scale = min(abs(x) for x in a if x != 0)
    a = [x / scale for x in a]
    marks = {node: int(c) for node, c in zip(chain, a) if c}
    print(f"\n=== {name}: marks {marks}")
    w = P.linear_combination(marks)
    v = proj(w)
    I = Q.primitive_isotropic_subobject(v)
    K = I.isotropic_reduction()
    print("  K: rank", K.module_rank(), "det", K.determinant(), "sig", K.signature_pair())
    reduction = I.isotropic_quotient_projection()
    images = []
    for node in LABEL_NODES[name]:
        x = proj(P.basis_vector(node))
        try:
            images.append(reduction(x))
        except Exception as error:
            print(f"  root r_{node} did not descend:", type(error).__name__, str(error)[:120])
    print("  source root images in K:", len(images))
    try:
        S = K.subobject_on(tuple(images))
        print("  spanned subobject: rank", S.module_rank(), "primitive", S.is_primitive())
        detK, detS = abs(K.determinant()), abs(S.determinant())
        print("  det(K) =", detK, " det(S) =", detS, " -> index^2 =", detK // detS if detS else "?")
        inc = S.inclusion()
        print("  inclusion kept:", type(inc).__name__)
        cok = inc.cokernel()
        print("  quotient K/S:", type(cok).__name__, "order",
              cok.cardinality() if hasattr(cok, "cardinality") else "n/a")
        dm = S.discriminant_module()
        print("  S discriminant module: order", dm.cardinality(), "invariants",
              dm.invariant_factors())
        print("  S is primitive in K:", inc.is_primitive())
    except Exception as error:
        print("  subobject construction failed:", type(error).__name__)
        print("   full message:", error)
