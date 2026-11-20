"""#789: the five remaining 1-cusps of F_En,2 and the (-2)-vectors in Pi^perp/Pi.

Sterk (Math. Z. 207 (1991), 4.3.17) lists five further
1-cusp types {2,4,5}, {4,5}, {3,5}, {3,4}, {5,5}.  For each, this script
takes the plane realised in computations/reports/coble_gammaEn2-planes-published.py
and computes Pi^perp/Pi, its 16 vectors of square -2, and the reflection orbits
on them.

Output: for each type, det(Pi^perp/Pi) = 64, 16 vectors of square -2, and the
orbit decomposition under the reflections in all of them: eight orbits of size
two, i.e. the sixteen vectors are eight mutually orthogonal antipodal pairs.

Inputs: AEGS, Nagoya Math. J. 259 (2025), Def. 2.3 (T_En);
Sterk, (4.2.3) (the cusp vectors), 4.3.17
(the five types); the plane realisations are those of
computations/reports/coble_gammaEn2-planes-published.py.
"""
from sage.all import matrix, vector, ZZ, QQ, block_diagonal_matrix, CartanMatrix
from sage.quadratic_forms.quadratic_form import QuadraticForm

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12

def perp_quotient(v, w):
    Mp = matrix(ZZ, 2, N, [list(G * vector(ZZ, v)), list(G * vector(ZZ, w))])
    Kern = Mp.right_kernel().basis_matrix()
    Gp = Kern * G * Kern.transpose()
    Cm = matrix(ZZ, 2, 10)
    for idx, u in enumerate((v, w)):
        c = Kern.transpose().solve_right(vector(ZZ, u))
        Cm.set_row(idx, [int(x) for x in c])
    Dm, Um, Vm = Cm.smith_form()
    Vi = Vm.inverse()
    R = Vi.rows()[2:]
    Gq = matrix(ZZ, 8, 8, [[sum(R[i][k] * Gp[k][l] * R[j][l]
                              for k in range(10) for l in range(10))
                            for j in range(8)] for i in range(8)])
    return Gq

PLANES = {
 (2, 4, 5): ([0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, 0, -2, -1, -1, 0, 0, 0, 0, 0, 0]),
 (4, 5):    ([0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, -2, 0, -1, 0, 0, 0, 1, 0, 0, 0]),
 (3, 5):    ([2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [-2, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0]),
 (3, 4):    ([0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, -1, -1, -1, 0, 1, 0, 0, 0, 0, 0]),
 (5, 5):    ([-2, 2, -2, -2, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]),
}
for lab, (uu, vv) in PLANES.items():
    Gq = perp_quotient(vector(ZZ, uu), vector(ZZ, vv))
    Q = QuadraticForm(ZZ, -Gq)
    vecs = [v for L in Q.short_vector_list_up_to_length(2) for v in L]
    roots = [vector(ZZ, list(v)) for v in vecs
             if any(v) and vector(ZZ, list(v)) * Gq * vector(ZZ, list(v)) == -2]
    rset = roots
    seen, orbits = set(), []
    for r in rset:
        if tuple(r) in seen:
            continue
        orb = {tuple(r)}
        stack = [r]
        while stack:
            x = stack.pop()
            for s in rset:
                b = x * Gq * s
                if b != 0:
                    y = vector(ZZ, x - 2 * QQ(b) / QQ(s * Gq * s) * s)
                    if tuple(y) not in orb:
                        orb.add(tuple(y))
                        stack.append(y)
        seen |= orb
        orbits.append(len(orb))
    print("type %s: det %d, %d vectors of square -2, reflection orbits %s"
          % (str(lab), Gq.det(), len(roots), orbits))
