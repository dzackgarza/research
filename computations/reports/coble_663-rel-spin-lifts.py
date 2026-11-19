"""research#663 / #766 (REL): the rational spin lifts of thm:coble-block-sign-in-w, checked in the Clifford algebra.

Claims checked, each by exact arithmetic over QQ in sage's CliffordAlgebra (v^2 = Q(v), Q(v) = b(v, v)):

1. Model B0 = <1> + U + E8(-1), E8 = D8^+ in the coordinates of QQ^8.  The eight roots
   r = f1 +- f2, f3 +- f4, f5 +- f6, f7 +- f8 of E8(-1) are pairwise orthogonal of square -2.
   x_delta = r1 ... r8 / 16 has x x^t = 1 (so it lies in Spin(B0 tensor QQ)), x v x^{-1} = delta_E8(v)
   for every v in a basis of B0 (delta_E8 = +1 on <1> + U, -1 on E8(-1)), hence x stabilizes B0.
   The script also reports whether x_delta lies in the integral Clifford algebra C(B0), computed in the
   Clifford algebra of the lattice Gram matrix, whose monomials in the lattice basis span C(B0) over ZZ.
2. Conjugation by a single vector u of nonzero square is -s_u, not s_u (checked on u = r1).
3. Diagonal model D = diag(1, 1, -1 x 9) with basis E1..E11 and v = E3 (square -1):
   x_v = E1 ... E11 E3 has x x^t = 1 and x b x^{-1} = -s_v(b) for every basis vector b.
4. In B0, with f1, f2, f3 the first three E8 coordinate vectors (square -1, pairwise orthogonal),
   a = f1 f2 and b = f2 f3 lie in Spin, stabilize B0, and a b a^{-1} b^{-1} = -1.

Usage:  sage-docker-python computations/reports/coble_663-rel-spin-lifts.py
"""
import hashlib
from pathlib import Path

from sage.all import QQ, ZZ, CliffordAlgebra, QuadraticForm, block_diagonal_matrix, identity_matrix, matrix, vector

REPORT = Path(__file__).resolve().parent
lines = ["research#663 / #766 (REL): rational spin lifts in the Clifford algebra", "=" * 72,
         "script sha256: " + hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), ""]


def clifford(gram):
    return CliffordAlgebra(QuadraticForm(QQ, 2 * gram))


def as_clifford(cl, coords):
    gens = cl.gens()
    return sum(QQ(c) * g for c, g in zip(coords, gens))


def vector_coords(cl, y):
    n = cl.ngens()
    coeffs = y.monomial_coefficients()
    vec = [QQ(0)] * n
    for key, c in coeffs.items():
        support = tuple(key)
        assert len(support) == 1, ("not a vector", y)
        vec[support[0]] = c
    return vector(QQ, vec)


# --- model B0 = <1> + U + E8(-1)
G0 = block_diagonal_matrix([matrix(QQ, [[1]]), matrix(QQ, [[0, 1], [1, 0]]), -identity_matrix(QQ, 8)])
C0 = clifford(G0)
half = QQ(1) / 2
e8_basis = [[half, -half, -half, -half, -half, -half, -half, half], [1, 1, 0, 0, 0, 0, 0, 0]]
for i in range(6):
    v = [0] * 8; v[i + 1] = 1; v[i] = -1; e8_basis.append(v)
basis_B0 = [[1] + [0] * 10, [0, 1] + [0] * 9, [0, 0, 1] + [0] * 8] + [[0, 0, 0] + v for v in e8_basis]
LB = matrix(QQ, basis_B0)
assert LB.det() != 0
gram_B0 = LB * G0 * LB.transpose()
assert gram_B0.denominator() == 1 and abs(gram_B0.det()) == 1
roots = []
for i in (0, 2, 4, 6):
    for s in (1, -1):
        v = [0] * 11; v[3 + i] = 1; v[4 + i] = s; roots.append(v)
for r in roots:
    assert (matrix(QQ, [r]) * G0 * matrix(QQ, [r]).transpose())[0, 0] == -2
    assert all(c in ZZ for c in vector(QQ, r) * LB.inverse())
for i, r in enumerate(roots):
    for s in roots[i + 1:]:
        assert (matrix(QQ, [r]) * G0 * matrix(QQ, [s]).transpose())[0, 0] == 0
x = C0.one()
for r in roots:
    x = x * as_clifford(C0, r)
x = x / 16
assert x * x.transpose() == C0.one()
delta = block_diagonal_matrix([identity_matrix(QQ, 3), -identity_matrix(QQ, 8)])
for b in basis_B0:
    image = vector_coords(C0, x * as_clifford(C0, b) * x.transpose())
    assert image == delta * vector(QQ, b), b
# integrality in the integral Clifford algebra C(B0): the Clifford algebra on the lattice Gram matrix,
# whose generators are the lattice basis; C(B0) is the ZZ-span of the monomials in them.
CL = clifford(gram_B0)
root_coords = [vector(QQ, r) * LB.inverse() for r in roots]
xl = CL.one()
for rc in root_coords:
    xl = xl * as_clifford(CL, rc)
xl = xl / 16
assert xl * xl.transpose() == CL.one()
lattice_denominators = sorted({QQ(c).denominator() for c in xl.monomial_coefficients().values()})
in_integral_clifford = lattice_denominators == [1]
f_product = C0.one()
for k in range(8):
    f_product = f_product * as_clifford(C0, [0] * (3 + k) + [1] + [0] * (7 - k))
lines += ["1. x_delta = r1...r8/16 in B0 = <1>+U+E8(-1):",
          "   x x^t = 1: True;  x b x^{-1} = delta_E8(b) on all 11 basis vectors of B0: True",
          f"   x_delta == f1 f2 ... f8 (product of the D8 coordinate vectors): {x == f_product}",
          f"   denominators of x_delta in the basis of C(B0) derived from the lattice basis: {lattice_denominators}",
          f"   x_delta lies in the integral Clifford algebra C(B0): {in_integral_clifford}", ""]

u = as_clifford(C0, roots[0])
uinv = u / QQ(-2)
for b in basis_B0:
    bv = vector(QQ, b)
    rv = vector(QQ, roots[0])
    s_u = bv - 2 * (bv * G0 * rv) / (rv * G0 * rv) * rv
    assert vector_coords(C0, u * as_clifford(C0, b) * uinv) == -s_u
lines += ["2. u b u^{-1} = -s_u(b) for u = r1 and every basis vector b: True", ""]

# --- diagonal model D = diag(1,1,-1^9), v = E3
GD = block_diagonal_matrix([identity_matrix(QQ, 2), -identity_matrix(QQ, 9)])
CD = clifford(GD)
E = CD.gens()
xv = CD.one()
for g in E:
    xv = xv * g
xv = xv * E[2]
assert xv * xv.transpose() == CD.one()
for i in range(11):
    b = vector(QQ, [1 if j == i else 0 for j in range(11)])
    v = vector(QQ, [1 if j == 2 else 0 for j in range(11)])
    s_v = b - 2 * (b * GD * v) / (v * GD * v) * v
    assert vector_coords(CD, xv * as_clifford(CD, b) * xv.transpose()) == -s_v
lines += ["3. x_v = E1...E11 E3 in diag(1,1,-1^9): x x^t = 1 and x b x^{-1} = -s_v(b) on all basis vectors: True", ""]

f = [as_clifford(C0, [0] * (3 + k) + [1] + [0] * (7 - k)) for k in range(3)]
a = f[0] * f[1]
bb = f[1] * f[2]
assert a * a.transpose() == C0.one() and bb * bb.transpose() == C0.one()
for y in (a, bb):
    for b in basis_B0:
        img = vector_coords(C0, y * as_clifford(C0, b) * y.transpose()) * LB.inverse()
        assert all(c in ZZ for c in img)
commutator = a * bb * a.transpose() * bb.transpose()
assert commutator == -C0.one()
lines += ["4. a = f1 f2, b = f2 f3 in Spin, both stabilize B0, and [a, b] = a b a^{-1} b^{-1} = -1: True", ""]

(REPORT / "coble_663-rel-spin-lifts-run.txt").write_text("\n".join(lines))
print("\n".join(lines))
