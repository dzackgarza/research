"""The four degree-two cusps from the source presentation, through the maintained maps.

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/cusps_from_presentation.py

Construction, with no hand-rolled quotient:

    P = Lattices(ZZ)(G24)              the degenerate presentation: 24 generators, rank 19
    Q = P.radical_quotient()           N, as the quotient of P by its radical
    w = P.linear_combination(marks)     the source's mark combination, an element of P
    image = Q.presentation_projection()(w)

What runs, on the maintained baseline (Sage 11.0.beta5, sage_extensions at main 5a9d7024f7):
P is accepted as a degenerate lattice -- rank 24, determinant 0, radical of rank 5 -- Q is the
presented module of rank 19, every component's mark combination is isotropic in P, its image in
Q is found and isotropic.

Where it stops, and the exact minimal failing call:

    Q.primitive_isotropic_subobject(image)
    AttributeError: 'OwnedJoinCategory.parent_class[_PresentedModule].ObjectType' object has no
    attribute 'primitive_isotropic_subobject'

`radical_quotient()` returns a presented module that *does* carry the descended form -- a
presented module is not evidence that the form is missing, and the quotient object reports rank
19, signature (1, 18), nondegenerate and even.  What is missing is the lattice specialization:
the isotropic-subobject construction is owned by the lattice category and is not reached from
the presented module.  That dispatch gap is assigned to the sage-extensions project, and
`radical_ingress_probe.py` records the two exact entry points and their messages:

  P.radical_quotient_projection()                       ValueError, formed-module component
  IsotropicReductions(P.base_ring())(P.radical().inclusion())   constructs the rank-19 lattice
      with the descended form, but .isotropic_reduction() raises TypeError: the object is only
      in the isotropic-reductions category, not a represented subobject with an inclusion

No quotient is hand-rolled here and no private machinery is used.
"""
import sys

from sage.all import ZZ, Matrix
from sage.combinat.root_system.cartan_type import CartanType

from sage_extensions.all import Lattices  # noqa: F401

print("python", sys.version.split()[0])

# ------------------------------------------------------------------ the source Gram data
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
print("G24: rank", G24.rank(), "kernel", 24 - G24.rank())

# ------------------------------------------------------- the presentation and its quotient
P = Lattices(ZZ)([list(row) for row in G24.rows()])
print("P: rank", P.module_rank(), "| det", P.determinant(), "| radical rank",
      P.radical().module_rank(), "| degenerate:", not P.is_nondegenerate())
Q = P.radical_quotient()
print("Q = P/rad(P): a", type(Q).__name__, "of rank", Q.module_rank(),
      "(its form lives on the reduction, not on the presented module)")

# N = H + E8^2 + A1, for comparison only
def root_lattice(letter, rank):
    shape = CartanType([letter, rank])
    return Lattices(ZZ)([[-int(x) for x in row] for row in shape.cartan_matrix().rows()])


U = Lattices(ZZ)([[0, 1], [1, 0]])
E8 = root_lattice("E", 8)
A1 = root_lattice("A", 1)
N = U + E8 + E8 + A1
print("N: rank", N.module_rank(), "det", N.determinant(), "signature", N.signature_pair())
print("N: the model the reductions below should match; compared per cusp.")

# ------------------------------------------------------------ the four cusps, from the marks
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

# the solved integral null vectors, recomputed here so the marks used are the ones verified
def solved_null(chain):
    block = Matrix(ZZ, [[G24[a, b] for b in chain] for a in chain])
    basis = block.kernel().basis_matrix()
    a = [x for x in basis[0]]
    scale = min(abs(x) for x in a if x != 0)
    a = [x / scale for x in a]
    assert all(x in ZZ for x in a)
    return [int(x) for x in a]


for name, (chain, typ) in CHAINS.items():
    a = solved_null(chain)
    kac = sorted(CartanType([typ[0], typ[1], 1]).a().values())
    coeffs = {node: c for node, c in zip(chain, a) if c}
    print(f"\n{name}: marks on the source nodes {coeffs}")
    print(f"  multiset equals the Kac marks of the type: {sorted(a) == kac}")
    w = P.linear_combination(coeffs) if hasattr(P, "linear_combination") else None
    print("  P.linear_combination available:", w is not None)
    if w is None:
        continue
    print("  w is isotropic in P:", w.is_isotropic() if hasattr(w, "is_isotropic") else "?")
    proj = None
    for attribute in ("presentation_projection", "projection"):
        if hasattr(Q, attribute):
            proj = getattr(Q, attribute)()
            print(f"  projection taken as Q.{attribute}()")
            break
    image = proj(w) if proj is not None else None
    print("  image of w in Q:", "found" if image is not None else "NONE")
    try:
        print("  image is isotropic:", image.is_isotropic())
    except Exception as error:
        print("  image.is_isotropic failed:", type(error).__name__, str(error)[:120])
    try:
        I = Q.primitive_isotropic_subobject(image)
        print("  Q.primitive_isotropic_subobject: ok, rank", I.module_rank())
    except Exception as error:
        print("  Q.primitive_isotropic_subobject failed:", type(error).__name__,
              str(error)[:200])
        continue
    try:
        K = I.isotropic_reduction()
        print("  K = v^perp/Zv: rank", K.module_rank(), "det", K.determinant(),
              "signature", K.signature_pair())
    except Exception as error:
        print("  isotropic_reduction failed:", type(error).__name__, str(error)[:200])
        continue
    label = LABELS[name]
    print("  label: rank", label.module_rank(), "det", label.determinant())
    try:
        print("  K isometric to the label:", K.is_isometric(label))
    except Exception as error:
        print("  K.is_isometric failed:", type(error).__name__, str(error)[:160])
        continue
    inclusions = [inc for inc in label.even_overlattice_inclusions()
                  if inc.codomain().is_isometric(K)]
    print("  label's even overlattice inclusions with K as codomain:", len(inclusions))
