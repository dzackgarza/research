"""Realize the remaining degree-two cusps in N and identify them by their quotient.

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/cusps_in_N.py

With I = <f_1> the 0-cusp line, N = I^perp/I is H + E8^2 + A1, and a primitive isotropic v in N
gives a 1-cusp J = I + <v~> with boundary lattice v^perp/Zv.  Writing H = <e, f>, an isotropic v
with e-coefficient 1 is v = e + n f + w with w in E8^2 + A1 and n = -w^2/2; for w a root of one
of the three summands, w^2 = -2 and v = e + f + w.

Each candidate is judged by whether v^perp/Zv is isometric to one of the four labels of AET
Sec. 3B, the labels built from their Cartan matrices rather than keyed in by invariants.
"""
import sys

from sage.all import ZZ
from sage.combinat.root_system.cartan_type import CartanType
from sage.combinat.root_system.root_system import RootSystem
from sage.matrix.constructor import Matrix

from sage_extensions.all import Lattices  # noqa: F401

print("python", sys.version.split()[0])


def root_lattice(letter, rank):
    shape = CartanType([letter, rank])
    gram = [[-int(x) for x in row] for row in shape.cartan_matrix().rows()]
    return Lattices(ZZ)(gram)


E8, A1 = root_lattice("E", 8), root_lattice("A", 1)
LABELS = {
    "A17":       root_lattice("A", 17),
    "D10 + E7":  root_lattice("D", 10) + root_lattice("E", 7),
    "E8^2 + A1": E8 + E8 + A1,
    "D16 + A1":  root_lattice("D", 16) + A1,
}

U = Lattices(ZZ)([[0, 1], [1, 0]])          # the named constructor routes through Julia
N = U + E8 + E8 + A1
print("N: rank", N.module_rank(), "det", N.determinant(), "signature", N.signature_pair())


def roots_in(letter, rank, offset):
    """Roots of a summand, as coordinate vectors of N (simple-root coordinates)."""
    space = RootSystem([letter, rank]).ambient_space()
    simple = list(space.simple_roots())
    cartan = Matrix(ZZ, CartanType([letter, rank]).cartan_matrix().rows())
    inverse = cartan.inverse()
    out = []
    for root in space.roots():
        inner = [sum(root[k] * simple[j][k] for k in range(space.dimension()))
                 for j in range(rank)]
        coords = vector(ZZ, inner) * inverse
        vec = [0] * 19
        for k in range(rank):
            vec[offset + k] = int(coords[k])
        out.append(tuple(vec))
    return out


def make(vec):
    total = N.basis_vector(0) + N.basis_vector(1)          # e + f
    for i, c in enumerate(vec):
        if c:
            total = total + c * N.basis_vector(i)
    return total


seen = {}
for offset, letter, rank in [(2, "E", 8), (10, "E", 8), (18, "A", 1)]:
    roots = roots_in(letter, rank, offset)
    print("\nsummand %s%d at %d: %d roots" % (letter, rank, offset, len(roots)))
    for w in roots:
        v = make(w)
        if not (v.is_isotropic() and v.is_primitive()):
            continue
        K = v.isotropic_reduction()
        key = (K.module_rank(), K.determinant(), tuple(int(x) for x in K.signature_pair()))
        if key in seen:
            continue
        hits = [name for name, L in LABELS.items() if K.is_isometric(L)]
        seen[key] = hits
        print("  v = e + f + w: v^perp/Zv rank %d det %d sig %s -> %s"
              % (key[0], key[1], key[2], hits if hits else "none of the four labels"))

print("\ndistinct quotient lattices found:", len(seen))
for key, hits in seen.items():
    print("  ", key, "->", hits)
