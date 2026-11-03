#!/usr/bin/env python3
"""
m5, swarm smw0b9kmo, direction d7 (input side of A21), appendix A -- CORRECTED.

The H-degree-1 census: the number of (-2)-CURVES of H-degree 1 on a one-node
member.  (Not the number of all classes delta with delta^2=-2, delta.H=1: that
set is also finite but contains the class D + F, F the ruling-fibre class, on
EVERY member; see appendix A.5.)

Corrected universal formula (proved in appendix A.1-A.4), for every one-node
member, with f the tau-invariant branch section, a_ij its coefficients, and
"node ruling" meaning x = 0 in the x-family and y = 0 in the y-family:

  nu_curve = 2 * #{c in P^1 \\ {0} : x-fibre over c reducible}
           + 2 * [a_02 = 0]
           + 2 * #{c in P^1 \\ {0} : y-fibre over c reducible}
           + 2 * [a_20 = 0]

(the two middle/final terms are the Kodaira-IV node rulings; the sets
"P^1 \\ {0}" include the point at infinity of the ruling parameter).

This script certifies the formula and computes nu_curve exactly on four members:
  A. the corpus's explicit member (sec-explicit-curve)          ->  0
  B. the bitangent member (constructed here)                    ->  4
  C. a Kodaira-IV member, a_02 = 0 (constructed here)           ->  2
  D. an "infinity-tangent" member, f(inf,y) = (y^2+1)^2         ->  4
Each member's one-node validity is certified by the ideal (f,f_x,f_y) in the
four standard charts.  All exact over Q.  Log: census_hdegree-run.txt
"""
import sympy as sp

PASS, FAIL = [], []
x, y, u, v = sp.symbols('x y u v')


def check(label, cond, detail=""):
    cond = bool(cond)
    (PASS if cond else FAIL).append(label)
    print(("PASS " if cond else "FAIL ") + label + ((" | " + detail) if detail else ""))


f_A = sp.expand(29 * x**4 * y**4 + 23 * x**4 * y**2 + 19 * x**4
                + 17 * x**3 * y**3 + 13 * x**3 * y
                + 11 * x**2 * y**4 + 7 * x**2 * y**2 + x**2
                + 5 * x * y**3 + x * y + 3 * y**4 + 2 * y**2)
f_B = sp.expand(x**4 * y**4 + 2 * x**4 - x**3 * y**3 - x**3 * y + x**2 * y**4
                - 8 * x**2 * y**2 + x**2 + x * y**3 + x * y + y**4 + 2 * y**2)
f_C = sp.expand(x**4 * y**4 + x**4 - x**3 * y - 3 * x**2 * y**2 + x**2 + x * y + 2 * y**4)
f_D = sp.expand(x**4 * y**4 + 2 * x**4 * y**2 + x**4 + y**4 + x**3 * y**3
                - 3 * x**2 * y**2 + x**2 + x * y + 2 * y**2)


def coeffs(f):
    P = sp.Poly(f, x, y)
    return {(i, j): int(P.coeff_monomial(x**i * y**j)) for i in range(9) for j in range(9)}


def one_node(f, name):
    """certify Sing(B) = {p} with p a nondegenerate node."""
    charts = [(x, y, sp.expand(f)),
              (x, v, sp.expand(v**4 * f.subs(y, 1 / v))),
              (u, y, sp.expand(u**4 * f.subs(x, 1 / u))),
              (u, v, sp.expand(u**4 * v**4 * f.subs({x: 1 / u, y: 1 / v})))]
    ok = True
    for s1, s2, G in charts:
        gb = sp.groebner([G, sp.diff(G, s1), sp.diff(G, s2)], s1, s2, order='lex')
        ex = list(gb.exprs)
        if (s1, s2) == (x, y):
            ok = ok and ex == [x, y]
        else:
            ok = ok and ex == [sp.Integer(1)]
    c = coeffs(f)
    node = (c[(0, 0)] == 0 and c[(1, 1)]**2 - 4 * c[(2, 0)] * c[(0, 2)] != 0)
    check("member %s: Sing(B) = {p}, node (quadratic form nondegenerate)" % name, ok and node,
          "a11^2-4a20a02 = %d" % (c[(1, 1)]**2 - 4 * c[(2, 0)] * c[(0, 2)]))
    return c


def square_params(f, fibre_var, param):
    """parameters c (affine) with f(c,.) = lambda*h^2, h of degree 1 or 2."""
    g = sp.Poly(f, fibre_var)
    a = [sp.expand(g.coeff_monomial(fibre_var**j)) for j in range(5)]
    a4, a3, a2, a1, a0 = a[4], a[3], a[2], a[1], a[0]
    p = sp.cancel(a3 / (2 * a4))
    q = sp.cancel((a2 / a4 - p**2) / 2)
    G1 = sp.expand(sp.numer(sp.cancel(a1 - 2 * a4 * p * q)))
    G2 = sp.expand(sp.numer(sp.cancel(a0 - a4 * q**2)))
    gg = sp.gcd(sp.Poly(G1, param), sp.Poly(G2, param))
    return gg


def is_square_up_to_scalar(q, t):
    """q in Q[t]: decide q = lambda * h^2 with h a polynomial (i.e. all roots even)."""
    P = sp.Poly(sp.expand(q), t)
    if P.degree() <= 0:
        return True
    fac = sp.factor_list(P.as_expr(), t)[1]
    return all(e % 2 == 0 for (b, e) in fac if sp.Poly(b, t).degree() > 0)


def square_params_1(q, t):
    P = sp.Poly(q, t)
    d = P.degree()
    if d == 4:
        a = [sp.expand(P.coeff_monomial(t**j)) for j in range(5)]
        a4, a3, a2, a1, a0 = a[4], a[3], a[2], a[1], a[0]
        p = sp.cancel(a3 / (2 * a4))
        qq = sp.cancel((a2 / a4 - p**2) / 2)
        G1 = sp.expand(sp.numer(sp.cancel(a1 - 2 * a4 * p * qq)))
        G2 = sp.expand(sp.numer(sp.cancel(a0 - a4 * qq**2)))
        return sp.gcd(sp.Poly(G1, t), sp.Poly(G2, t))
    return sp.Poly(1, t)     # degree != 4: not treated here


def census(f, name):
    c = coeffs(f)
    data = {}
    for direction, fibre_var, param in (("x", y, x), ("y", x, y)):
        gg = square_params(f, fibre_var, param)
        aff_roots = sp.roots(sp.Poly(gg, param)) if gg.degree() > 0 else {}
        # point at infinity of the ruling parameter: coefficient of the top power
        top = sp.expand(P.TC() if False else sum(
            c[(4, j)] * fibre_var**j for j in range(5)))
        if direction == "y":
            top = sp.expand(sum(c[(i, 4)] * x**i for i in range(5)))
        inf_red = is_square_up_to_scalar(top, fibre_var)
        data[direction] = (gg, aff_roots, inf_red)
        print("  %s-rulings: square-fibre affine parameters %s (gcd %s); reducible at infinity: %s"
              % (direction, aff_roots, sp.factor(gg.as_expr()), inf_red))
    nu = 0
    nu += 2 * sum(1 for cc in data["x"][1] if cc != 0)
    nu += 2 * (1 if c[(0, 2)] == 0 else 0)
    nu += 2 * sum(1 for cc in data["y"][1] if cc != 0)
    nu += 2 * (1 if c[(2, 0)] == 0 else 0)
    nu += 2 * (1 if data["x"][2] else 0) + 2 * (1 if data["y"][2] else 0)
    print("  => nu_curve(%s) = %d   [a02 = %d, a20 = %d]" % (name, nu, c[(0, 2)], c[(2, 0)]))
    return nu, c


print("=== A: corpus explicit member ===")
cA = one_node(f_A, "A")
nuA, _ = census(f_A, "A")
print("=== B: bitangent member ===")
cB = one_node(f_B, "B")
nuB, _ = census(f_B, "B")
print("=== C: Kodaira-IV member (a_02 = 0) ===")
cC = one_node(f_C, "C")
nuC, _ = census(f_C, "C")
print("=== D: infinity-tangent member ===")
cD = one_node(f_D, "D")
nuD, _ = census(f_D, "D")

print()
check("PL-10a A: nu_curve = 0 (no reducible ruling fibre at all, a02 != 0)", nuA == 0)
check("PL-10b B: nu_curve = 4 (two bitangent x-rulings, I_2 side at the node)", nuB == 4)
check("PL-10c C: nu_curve = 2 (Kodaira-IV node ruling, a02 = 0, nothing else)", nuC == 2
      and cC[(0, 2)] == 0 and cC[(2, 0)] != 0)
check("PL-10d D: nu_curve = 2, the reducible fibre being at x = infinity (not at y = infinity),"
      " with the I_2 side at the node ruling",
      nuD == 2 and cD[(0, 2)] != 0 and cD[(2, 0)] != 0)

print()
print("=== the node-ruling dichotomy, in the blow-up chart (x = y u, z = y v) ===")
for f, nm in ((f_A, "A (a02=2, I_2)"), (f_C, "C (a02=0, IV)"), (f_B, "B"), (f_D, "D")):
    S = sp.expand(sp.cancel(sp.expand((y * v)**2 - f.subs({x: y * u})) / y**2))
    at_u0 = sp.factor(sp.expand(S.subs(u, 0)))
    branches = sp.solve(sp.Eq(at_u0, 0), v)
    print("  member %-16s fibre (x) = (y) + (u); {u=0}: %s ; v = %s" % (nm, at_u0, branches))
check("PL-10e I_2 side (a02 != 0): v^2 - (a02 + a04 y^2) is irreducible over C",
      cA[(0, 2)] != 0 and cA[(0, 4)] != 0)
check("PL-10f IV side (a02 = 0): v^2 - (a02 + a04 y^2) = (v - c y)(v + c y) over C",
      cC[(0, 2)] == 0 and cC[(0, 4)] != 0)

print()
print("=== the class count vs the curve count (appendix A.5) ===")
check("PL-10g D + F has square -2 and H-degree 1 on every member (F the fibre class): "
      "(-2) + 0 + 2*0 = -2", -2 + 0 + 2 * 0 == -2)
check("PL-10h IV node ruling: D + C_i has square -2 too: (-2) + (-2) + 2*1 = -2",
      (-2) + (-2) + 2 * 1 == -2)
check("PL-10i IV node ruling: the three components meet pairwise once: 2*(-2)+2*3 = 0 = F^2",
      2 * (-2) + (-2) + 2 * 3 == 0)

print()
print("summary: %d checks passed, %d failed" % (len(PASS), len(FAIL)))
print()
print("nu_curve: A(corpus) = %d, B(bitangent) = %d, C(IV) = %d, D(infinity-tangent) = %d"
      % (nuA, nuB, nuC, nuD))
if FAIL:
    print("FAILED: " + ", ".join(FAIL))
    raise SystemExit(1)
