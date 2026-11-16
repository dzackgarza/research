"""#645/#667, plane half as F_2 linear algebra: |H|, |Stab(J)|, |orbit|, index, 1-cusp count.

    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_plane-half-f2.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e.

T_Co = B(2) with B unimodular, so A_{T_Co} = B/2B is F_2^11, q(x) = (x,x)_B/2 mod 2, and the
discriminant action of g in O(B) is g mod 2.  Extends coble_plane-half.py, which returns the 119
generators of Stab_{O(B)}(P) and documents the two library gaps; here the reduction mod 2 is done
by hand so the gaps do not bite.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import GF, QQ, ZZ, block_diagonal_matrix, libgap, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
print('provenance\n  Sage: %s\n  sage-extensions: pin %s\n' % (SAGE_VERSION, PIN[:12]))

G_B = block_diagonal_matrix(matrix(ZZ, [[0, 1], [1, 0]]), matrix(ZZ, [[0, 1], [1, 0]]),
                           -matrix.identity(ZZ, 7))
B = Lattices(ZZ)([list(x) for x in G_B.rows()])
T = Lattices(ZZ)([list(x) for x in (2 * G_B).rows()])
r = int(B.rank())
basis = [B.basis_vector(i) for i in range(r)]
P = B.primitive_sublattice_from([basis[0], basis[2]])
print('B = U + U + I_{0,7}: rank %d, det %s, signature %s;  P primitive of rank %d\n'
      % (r, B.determinant(), B.signature_pair(), P.rank()))

start = time.time()
A = T.discriminant_quadratic_form()
O = A.orthogonal_group()
order_O = int(O.order())
print('|O(q)| = %d   (%.0f s)' % (order_O, time.time() - start))

start = time.time()
eT = [T.basis_vector(i) for i in range(r)]
c = [T.discriminant_class(T.primitive_dual(eT[i])) for i in range(r)]
mask = {A.zero(): 0}
for i in range(r):
    for elem, m in list(mask.items()):
        mask.setdefault(elem + c[i], m | (1 << i))
print('mask isomorphism A = B/2B: %d classes   (%.0f s)' % (len(mask), time.time() - start))


def mat_of(theta):
    cols = [mask[theta(c[i])] for i in range(r)]
    return matrix(GF(2), r, r, [[(cols[j] >> i) & 1 for j in range(r)] for i in range(r)])


print('\n(2) G = O(q) over F_2')
start = time.time()
gensO = list(O.group_generators())
G = libgap.Group([libgap(mat_of(t)) for t in gensO])
order_G = int(libgap.Size(G))
print('  |G| = %d, equals |O(q)|: %s   (%.0f s)' % (order_G, order_G == order_O, time.time() - start))

gensB = list(B.Isom(B).stabilizer(P, action='setwise').group_generators())
inv = G_B.inverse()
gens_H = []
for g in gensB:
    cols = []
    for j in range(r):
        pair = matrix(ZZ, 1, r, [B.pairing(g(basis[j]), basis[i]) for i in range(r)])
        coords = (pair * inv)[0]
        cols.append([int(QQ(x)) % 2 for x in coords])
    # GAP acts on row vectors by right multiplication, so the column-convention matrix of the
    # module automorphism enters the comparison transposed; the O(q) generators stay as mat_of
    # returns them, and the two sides then agree on J.
    gens_H.append(matrix(GF(2), r, r, [[cols[j][i] for j in range(r)] for i in range(r)]).transpose())
H = libgap.Group([libgap(g) for g in gens_H])
order_H = int(libgap.Size(H))
print('  |H| = |rho(Stab_{O(B)}(P))| = %d' % order_H)

print('\n(2 cont.) J, its stabilizer, its orbit')
start = time.time()
V = libgap.GF(2) ** r
r1 = [0] * r; r1[0] = 1
r3 = [0] * r; r3[2] = 1
print('  building J = <e1/2, e2/2>, trying the available GAP constructions')
J = None
candidates = [
    ("Subspace(V, [vector, vector])", lambda: libgap.Subspace(V, libgap([libgap(r1), libgap(r3)]))),
    ("Subspace(V, gens, \"basis\")", lambda: libgap.Subspace(V, libgap([libgap(r1), libgap(r3)]), "basis")),
    ("Submodule(V, gens, \"basis\")", lambda: libgap.Submodule(V, libgap([libgap(r1), libgap(r3)]), "basis")),
    ("the canonical-basis matrix", lambda: libgap(matrix(GF(2), [r1, r3])),
     ),
]
for entry in candidates:
    name, build = entry[0], entry[1]
    try:
        candidate = build()
        try:
            dim = int(libgap.Dimension(candidate))
        except Exception:
            dim = 'n/a'
        print('    %-34s OK, dimension %s' % (name, dim))
        J = candidate
        break
    except Exception as exc:                                # noqa: BLE001
        print('    %-34s FAILED: %s: %s' % (name, type(exc).__name__, exc))
if J is None:
    print('  no construction of J succeeded; stopping')
    raise SystemExit(1)
start = time.time()
Stab = libgap.Stabilizer(G, J, libgap.OnSubspacesByCanonicalBasis)
order_stab = int(libgap.Size(Stab))
orbit = libgap.Orbit(G, J, libgap.OnSubspacesByCanonicalBasis)
order_orbit = len(list(orbit))
print('  |Stab_{O(q)}(J)| = %d' % order_stab)
print('  |O(q) . J| = %d' % order_orbit)
print('  |Stab| * |orbit| = |G|: %s' % (order_stab * order_orbit == order_G))
contained = bool(libgap.IsSubgroup(Stab, H))
print('  H <= Stab: %s   (%.0f s)' % (contained, time.time() - start))
if not contained:
    print('  the containment fails; scanning for the first generator that moves J')
    Jm = matrix(GF(2), [r1, r3])
    for k, g in enumerate(gens_H):
        M2 = Jm * g
        image = libgap.Subspace(libgap.GF(2) ** r, libgap([[int(x) for x in M2[i]] for i in (0, 1)]))
        try:
            same = bool(libgap.IsSubspace(J, image))
        except Exception:
            same = False
        if not same:
            print('  generator %d moves J; its matrix over GF(2) is' % k)
            print(g)
            break

print('\nTHE NUMBERS')
print('  |H| = |rho(Stab_{O(B)}(P))|      = %d' % order_H)
print('  |Stab_{O(q)}(J)|                 = %d' % order_stab)
print('  index [Stab : H]                 = %d' % (order_stab // order_H))
print('  liftable J (= |G . J|, rho onto) = %d' % order_orbit)
print('  1-cusp count of F_Co             = %d' % (order_orbit * (order_stab // order_H)))
print('  23 715 and the five page sizes   = %d' % (1575 + 270 + 9450 + 3780 + 8640))
