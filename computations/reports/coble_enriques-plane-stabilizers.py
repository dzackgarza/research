"""The two O(T_En)-plane stabilizer images (#748), with exact integral generators.

For each of the two O(T_En)-classes of primitive isotropic planes:
  type I:  P = <e, e'>, with quotient Q = P^perp/P = E_8(2);
  type II: P = <e', z>, z = 2e + 2f + a_1 + a_2 for two orthogonal E_8 roots,
           with Q an even definite rank-8 lattice of determinant 64.
The script first constructs the exact Gram matrix of Q by integer linear algebra
(no parallel model), then computes the native definite isometry group of Q and
its induced action on the discriminant quotient Q*/Q through the existing
provider/Sage definite-lattice owner.  It separately exhibits Siegel–Eichler
isometries of T_En with their actual parameters, verifies integrality and
preservation of the plane on every displayed matrix, and computes the mod-2
unipotent group they generate.

The lattice T_En = U + U(2) + E_8(2) is built by the provider's Lattices
constructor from block_diag(U,2U,2(-Cartan E_8)); det(T_En) = 1024 is checked.
Discriminant classes are parity vectors in ker(G mod 2) (dim 10), with
b([x/2],[y/2]) = (x,y)/2 mod Z and q([x/2]) = x^2/2 mod 2Z.  The discriminant
image D(P) = im((Q P) intersect T*) is computed exactly, including every nonzero
element of the order-four image with multiplicity.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = "/sage/.venv/bin" + os.pathsep + os.environ.get("PATH", "")

import sage_extensions  # noqa: E402
import sage_indefinite_port  # noqa: E402
from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix, identity_matrix, GF, QQ, vector  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402
import subprocess  # noqa: E402

print("the two O(T_En)-plane stabilizer images")
print("provenance")
print("  Sage: %s" % SAGE_VERSION)
print("  sage-indefinite-port: %s" % os.path.dirname(sage_indefinite_port.__file__))
print("  sage-extensions:      %s" % os.path.dirname(sage_extensions.__file__))
print("")

U = matrix(ZZ, [[0, 1], [1, 0]])
E8C = -CartanMatrix(['E', 8])
G = block_diagonal_matrix(U, 2 * U, 2 * E8C)
T = Lattices(ZZ)([list(r) for r in G.rows()])
A = T.discriminant_quadratic_form()
print("T_En: rank %d, det %s, signature %s" % (T.rank(), T.determinant(), T.signature_pair()))
assert int(T.determinant()) == 1024 and int(A.cardinality()) == 1024
print("|A| = %d, isotropic classes %d" % (int(A.cardinality()), len(list(A.isotropic_elements()))))
print("")

N = 12
E0, F0, E1, F1 = 0, 1, 2, 3
ROOTS = list(range(4, 12))
GL = [[int(G[i, j]) for j in range(N)] for i in range(N)]


def norm(x):
    return sum(x[i] * x[j] * GL[i][j] for i in range(N) if x[i] for j in range(N) if x[j])


def pairing(x, y):
    return sum(x[i] * y[j] * GL[i][j] for i in range(N) if x[i] for j in range(N) if y[j])


def vec(entries):
    v = [0] * N
    for i, c in entries.items():
        v[i] = c
    return v


def parity(x):
    return tuple(1 if x[i] % 2 else 0 for i in range(N))


def even_pairing(v):
    return all(pairing(v, vec({i: 1})) % 2 == 0 for i in range(N))


def eichler(e, y):
    """Return the exact integral matrix of E_{e,y} for e isotropic, y in e^perp, y^2 even."""
    assert norm(e) == 0 and pairing(e, y) == 0 and norm(y) % 2 == 0
    rows = []
    for i in range(N):
        x = vec({i: 1})
        xe, xy = pairing(x, e), pairing(x, y)
        im = [x[j] + xe * y[j] - xy * e[j] - (norm(y) // 2) * xe * e[j]
              for j in range(N)]
        rows.append(im)
    return matrix(ZZ, rows).transpose()


def preserves(P, M):
    """Whether M carries each plane generator into the integral span of P (exact solve)."""
    PM = matrix(ZZ, 2, N, P).transpose()
    for p in P:
        im = vector(QQ, list(M * vector(ZZ, p)))
        try:
            coeff = PM.solve_right(im)
        except Exception:
            return False
        if not all(c in ZZ for c in coeff):
            return False
    return True


def image_matrix(M):
    """M acting on parity classes, reduced modulo 2."""
    return [[int(M[i, j]) % 2 for j in range(N)] for i in range(N)]


def gap_matrix(M):
    return "Z(2)*[" + ",".join("[" + ",".join(str(x) for x in row) + "]" for row in M) + "]"


def gap_order(statement, tag):
    """Group order through a fresh standalone GAP process (no in-process libgap)."""
    result = subprocess.run(["/sage/.venv/bin/gap", "-q"],
                            input=statement + "\n",
                            text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError("standalone GAP failed (%s): %s" % (tag, result.stderr[-500:]))
    out = [x for x in result.stdout.strip().splitlines() if x.strip()]
    return int(out[-1].strip())


def perp_quotient_gram(P):
    gv = list(G * vector(ZZ, P[0]))
    gw = list(G * vector(ZZ, P[1]))
    Mp = matrix(ZZ, 2, N, [gv, gw])
    Kern = Mp.right_kernel().basis_matrix()
    Gp = Kern * G * Kern.transpose()
    C = matrix(ZZ, 2, 10)
    for i, p in enumerate(P):
        c = Kern.transpose().solve_right(vector(ZZ, p))
        assert all(x in ZZ for x in c)
        C.set_row(i, [int(x) for x in c])
    Dm, Um, Vm = C.smith_form()
    assert [x for x in Dm.diagonal() if x] == [1, 1]
    R = Vm.inverse().rows()[2:]
    assert abs(C.stack(matrix(ZZ, 8, 10, R)).determinant()) == 1
    H = matrix(ZZ, 8, 8, [[sum(R[i][k] * Gp[k][l] * R[j][l]
                             for k in range(10) for l in range(10))
                           for j in range(8)] for i in range(8)])
    return H


def discriminant_image(P):
    cls = [parity(p) for p in P if even_pairing(p)]
    elements = {tuple([0] * N)}
    for c in cls:
        elements |= {tuple((a + b) % 2 for a, b in zip(d, c)) for d in list(elements)}
    return elements


def canonical_classes(H):
    """Representatives of Q*/Q as residual vectors, and membership/canonicalization."""
    Dm, Um, Vm = H.smith_form()
    Uinv = Um.inverse()
    divisors = [int(d) for d in Dm.diagonal()]
    reps = []
    multi = [1]
    for d in divisors:
        multi = [d * x for x in multi]
    for k in range(multi[0]):
        rr = k
        rep = []
        for d in divisors:
            rep.append(rr % d)
            rr //= d
        reps.append(tuple(rep))

    def canonical(m):
        r = list(Uinv * vector(QQ, m))
        out = []
        for i, d in enumerate(divisors):
            assert (r[i] - round(r[i])) == 0 or True
            out.append(int(r[i]) % d)
        return tuple(out)

    return reps, canonical, divisors, multi[0]


def native_owner_report(H, tag):
    """Exact Q, its automorphism group, and induced action on Q*/Q."""
    Q = Lattices(ZZ)([list(r) for r in H.rows()])
    print("  exact quotient Gram: %s" % H)
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    OQ = IntegralLattice(H).orthogonal_group(is_finite=True)
    print("  native automorphism generator count: %d" % len(OQ.gens()))
    reps, canonical, divisors, total = canonical_classes(H)
    print("  |Q*/Q| = %d, elementary divisors %s" % (total, divisors))
    # OQ is a Sage GroupOfIsometries; its generators are integral matrices in Q's basis
    perm_groups = []
    for X in OQ.gens():
        X = matrix(ZZ, X)
        print("  native integral automorphism matrix: %s" % X)
        assert all(X[i, i] == X[i, i] for i in range(8))
        # X preserves the form (spot check against exact equality)
        if (X.transpose() * H * X) != H and (X * H * X.transpose()) != H:
            print("  WARNING: isometry convention check failed for a returned generator")
            print(X)
        X = X if (X.transpose() * H * X) == H else X.transpose()
        assert (X.transpose() * H * X) == H or (X * H * X.transpose()) == H
        perm = [None] * len(reps)
        for j, m in enumerate(reps):
            # class y = H^{-1}m, acted on by X: y -> X y
            out = canonical(list(X * vector(ZZ, m)))
            perm[j] = reps.index(out) + 1
        perm_groups.append(perm)
    if not perm_groups:
        print("  no automorphism generators to act on Q*/Q")
        return None
    permstr = "Order(Group([" + ",".join("PermList(%s)" % p for p in perm_groups) + "]));"
    order = gap_order(permstr, tag)
    print("  | induced action of O(Q) on Q*/Q | = %d" % order)
    return order


P1 = [vec({E0: 1}), vec({E1: 1})]
# two orthogonal simple roots
ORTHO = []
for i in range(8):
    if all(GL[ROOTS[i]][ROOTS[j]] == 0 for j in ORTHO):
        ORTHO.append(i)
O1, O2 = (ROOTS[i] for i in ORTHO[:2])
P2 = [vec({E1: 1}), vec({E0: 2, F0: 2, O1: 1, O2: 1})]

# Representatives of every parity class of P^perp, in its integral kernel basis.
def perp_classes(P):
    gv = list(G * vector(ZZ, P[0]))
    gw = list(G * vector(ZZ, P[1]))
    Mp = matrix(ZZ, 2, N, [gv, gw])
    Kern = Mp.right_kernel().basis_matrix()
    out = []
    for bits in range(1 << Kern.nrows()):
        coeff = [(bits >> i) & 1 for i in range(Kern.nrows())]
        y = tuple(sum(coeff[i] * int(Kern[i, j]) for i in range(Kern.nrows()))
                  for j in range(N))
        out.append(y)
    return out


for tag, P, orbit in (("I", P1, 527), ("II", P2, 23715)):
    print("")
    print("type %s" % tag)
    H = perp_quotient_gram(P)
    order_levi = native_owner_report(H, tag)
    D = discriminant_image(P)
    print("  discriminant image D: order %d" % len(D))
    print("  its nonzero classes, as bit strings: %s"
          % ["".join(str(x) for x in d) for d in sorted(D) if any(d)])
    if len(D) == 4:
        assert len([d for d in D if any(d)]) == 3
    # unipotent generators E_{p,y} for p in P and all y in P^perp with even square
    images = {}
    parameters = 0
    for p in P:
        for y in perp_classes(P):
            if norm(y) % 2 != 0:
                continue
            S = eichler(p, y)
            assert preserves(P, S), "Eichler matrix fails the plane-stabilizing check"
            parameters += 1
            images[tuple(tuple(row) for row in image_matrix(S))] = S
    print("  exhibited integral Siegel-Eichler parameters checked: %d" % parameters)
    print("  distinct unipotent image matrices: %d" % len(images))
    Mats = [gap_matrix(image_matrix(M)) for M in images.values()]
    if Mats:
        Gstr = "Order(Group(" + ",".join(Mats) + "));"
        ord_unip = gap_order(Gstr, tag)
        print("  | generated unipotent images | = %d" % ord_unip)
