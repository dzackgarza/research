#!/usr/bin/env python3
"""research#787: an irreducible ten-nodal sextic invariant under a projectivity of
order 3 that permutes its nodes.  Witness that S_10 does not act freely on the
labelled base B = V/PGL_3.

Exact rational arithmetic (sympy).  Run from the repository root:
    python3 computations/reports/coble_787-s10-symmetric-sextic.py

Construction.  R = [[0,-1,0],[1,-1,0],[0,0,1]] has order 3.  Take the two triangles
A=(1,0,1), B=RA, C=R^2 A and A'=(1,0,2), B'=RA', C'=R^2 A', in perspective from
O=(0,0,1), and X=BC cap B'C', Y=CA cap C'A', Z=AB cap A'B'.  The ten points are
R-invariant; the sextic through them with multiplicity two at each is unique and
turns out to be R-invariant and irreducible, with the ten points ordinary double.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
VARS = (x, y, z)


def main():
    R = sp.Matrix([[0, -1, 0], [1, -1, 0], [0, 0, 1]])
    assert R**3 == sp.eye(3)

    def act(p):
        return tuple(R * sp.Matrix(p))

    def line(p, q):
        return sp.Matrix([p[1]*q[2] - p[2]*q[1], p[2]*q[0] - p[0]*q[2], p[0]*q[1] - p[1]*q[0]])

    def meet(l, m):
        return (l[1]*m[2] - l[2]*m[1], l[2]*m[0] - l[0]*m[2], l[0]*m[1] - l[1]*m[0])

    O = (0, 0, 1)
    A = (1, 0, 1); B = act(A); C = act(B)
    Ap = (1, 0, 2); Bp = act(Ap); Cp = act(Bp)
    X = meet(line(B, C), line(Bp, Cp))
    Y = meet(line(C, A), line(Cp, Ap))
    Z = meet(line(A, B), line(Ap, Bp))
    pts = [O, A, B, C, Ap, Bp, Cp, X, Y, Z]
    print("ten points:", pts)
    assert len(set(pts)) == 10, "the ten points are not distinct"
    perm = [pts.index(act(p)) for p in pts]
    print("permutation of the ten points by R:", perm)
    assert perm != list(range(10)), "the permutation is trivial"

    mons = [(i, j, 6 - i - j) for i in range(7) for j in range(7 - i)]
    mon = [x**i * y**j * z**k for (i, j, k) in mons]
    rows = []
    for p in pts:
        for v in range(3):
            rows.append([sp.diff(m, VARS[v]).subs({x: p[0], y: p[1], z: p[2]}) for m in mon])
    M = sp.Matrix(rows)
    print("matrix of the thirty node conditions:", M.shape, "rank:", M.rank())
    ns = M.nullspace()
    print("dimension of the space of sextics with a double point at all ten:", len(ns))
    assert len(ns) == 1
    F = sp.expand(sum(ns[0][i] * mon[i] for i in range(28)))
    G = sp.expand(4 * F)
    print("the sextic (normalised to integral coefficients):")
    print(" G =", G)
    factors = sp.factor_list(G)[1]
    print("factorisation over Q:", [(sp.factor(f), e) for f, e in factors])
    assert len(factors) == 1 and factors[0][1] == 1, "the sextic is not irreducible"

    def hess2(p):
        i = [k for k in range(3) if p[k] != 0][0]
        others = [k for k in range(3) if k != i]
        f = sp.expand(G.subs({VARS[i]: 1}))
        sub = {VARS[k]: sp.Rational(p[k], p[i]) for k in others}
        return sp.simplify(sp.hessian(f, [VARS[k] for k in others]).subs(sub).det())

    for p in pts:
        grad = [sp.simplify(sp.diff(G, q).subs({x: p[0], y: p[1], z: p[2]})) for q in VARS]
        assert grad == [0, 0, 0], (p, grad)
        d = hess2(p)
        assert d != 0, (p, d)
        print("ordinary double point at", p, " 2x2 Hessian determinant:", d)

    FR = sp.expand(G.subs({x: (R.inv() * sp.Matrix(VARS))[0],
                           y: (R.inv() * sp.Matrix(VARS))[1],
                           z: (R.inv() * sp.Matrix(VARS))[2]}, simultaneous=True))
    print("R^* G - G =", sp.expand(FR - G))
    assert sp.expand(FR - G) == 0, "the sextic is not invariant"
    # an irreducible sextic with ten ordinary double points has no other singularity:
    # p_a = 10 and each node contributes delta = 1, so the genus is 0.
    print("genus check: p_a = 10, sum of delta = 10, geometric genus 0, no other singularity")
    print("CONCLUSION: S_10 does not act freely on B; the stabiliser of the class of")
    print("(G; p_1..p_10) contains the 3-cycle", perm, "!= e.")


if __name__ == '__main__':
    main()
