"""A21 chamber clause: explicit counterexample member and its verification.

Member b0 of the direct projective construction (X^sharp = {z^2 = f} -> Y = P^1 x P^1,
tau(x,y) = (-x,-y), L = O(2,2), f in H^0(L^2) = H^0(O(4,4))^tau).

Claims verified here:
 (V1) f is tau-invariant, of exact bidegree (4,4), irreducible;
 (V2) the branch curve B = {f = 0} has exactly one singular point, an ordinary node at
      the tau-fixed point p = (0,0)   [Groebner bases on the four affine charts];
 (V3) f(x,1) = (x^2+x+2)^2, so over the ruling line C = {y = 1} (p not in C, rational,
      O(1,1).C = 1) the double cover splits: pi^{-1}(C) = C' + C'' with C' = {z = q},
      C'' = {z = -q}, q = x^2+x+2;
 (V4) consequently C' is a smooth rational curve on the K3 X_b0 with C'^2 = -2
      (adjunction, K_X = 0), H.C' = 1, alpha.C' = 0;
 (V5) the class of C' is not in M_{b0} (x) Q, M = pi^*Pic(Bl_p Y) = <e1,e2,alpha>;
 (V6) every class of M has even H-degree, so C' has odd H-degree.
"""
import sympy as sp

x, y, u, v = sp.symbols('x y u v')

f = (17*x**4*y**4 - 14*x**4*y**2 - 2*x**4 + 5*x**3*y**3 - 3*x**3*y + 7*x**2*y**4
     - 3*x**2*y**2 + x**2 + 3*x*y**3 + x*y + 2*y**4 + 2*y**2)
q = x**2 + x + 2                       # f = q(x,y)^2 + (y^2-1)*h  with q = x^2+xy+2y^2, h = -x^2-xy-2y^2+3x^4+5x^3y+7x^2y^2+17x^4y^2
Q = x**2 + x*y + 2*y**2
h = (-x**2 - x*y - 2*y**2) + (3*x**4 + 5*x**3*y + 7*x**2*y**2) + 17*x**4*y**2

print("== (V1) tau-invariance, bidegree, irreducibility")
print("  f(-x,-y) - f(x,y) =", sp.simplify(f.subs({x: -x, y: -y}) - f))
print("  decomposition check f - (Q^2 + (y^2-1)h) =", sp.expand(f - (Q**2 + (y**2 - 1)*h)))
P = sp.Poly(f, x, y)
print("  monomials with i+j odd :", [m for m in P.monoms() if (m[0] + m[1]) % 2])
print("  degree in x, in y      :", sp.degree(f, x), sp.degree(f, y))
print("  factor                 :", sp.factor(f))

print("== (V2) singular locus of B on the four affine charts of P^1 x P^1")
charts = [("(x,y)",      sp.expand(f), x, y),
          ("(1/x,y)",    sp.expand(sp.simplify(f.subs(x, 1/u)*u**4)), u, y),
          ("(x,1/y)",    sp.expand(sp.simplify(f.subs(y, 1/v)*v**4)), x, v),
          ("(1/x,1/y)",  sp.expand(sp.simplify(f.subs({x: 1/u, y: 1/v})*u**4*v**4)), u, v)]
for nm, g, A, B in charts:
    G = sp.groebner([g, sp.diff(g, A), sp.diff(g, B)], A, B, order='lex')
    print("  chart %-9s  singular ideal Groebner basis: %s" % (nm, [sp.factor(e) for e in G.exprs]))
print("  quadratic part at p:", {m: c for m, c in P.terms() if m[0] + m[1] == 2},
      " discriminant of a*x^2+b*xy+c*y^2:", 1**2 - 4*1*2)
print("  coefficients (x^4, y^4, x^4y^4, 1) =", (P.coeff_monomial(x**4), P.coeff_monomial(y**4),
                                                P.coeff_monomial(x**4*y**4), P.coeff_monomial(1)))

print("== (V3) splitting over the ruling line C = {y = 1}")
print("  f(x,1) =", sp.expand(f.subs(y, 1)), "   q^2 - f(x,1) =", sp.expand(q**2 - f.subs(y, 1)))
print("  q =", q, "  roots of q:", sp.solve(q, x))
print("  C = {y=1} contains no tau-fixed point (tau-fixed points have y in {0,oo})")

print("== (V4) numerics of C' (C' maps isomorphically to C, so C'.pi^*D = C.D)")
print("  C.(1,1) = 1 = H.C' ;  p not in C  =>  C'.alpha = 0 ;  C' = P^1, K_X = 0 => C'^2 = -2")
print("  (pi^*C)^2 = 2*C^2 = 0 = C'^2 + 2 C'.C'' + C''^2 = -2 + 2*2 - 2, so C'.C'' = 2")

print("== (V5) the class of C' is not rational in M = <e1,e2,alpha>, e_i = pi^*h_i")
M = sp.Matrix([[0, 2, 0], [2, 0, 0], [0, 0, -2]])       # Gram of (e1,e2,alpha)
a, b, c = sp.symbols('a b c')
sol = M.solve(sp.Matrix([0, 1, 0]))                      # pairings (C'.e1, C'.e2, C'.alpha)
print("  unique v in M(x)Q with the same pairings: v =", list(sol.T), " v^2 =", sp.simplify((sol.T*M*sol)[0, 0]),
      "  but C'^2 = -2  =>  [C'] not in M(x)Q")
G4 = sp.Matrix([[0, 2, 0, 0], [2, 0, 0, 1], [0, 0, -2, 0], [0, 1, 0, -2]])   # (e1,e2,alpha,C')
print("  Gram of span(e1,e2,alpha,C'):", G4.tolist(), " det =", G4.det(),
      " charpoly =", sp.factor(G4.charpoly().as_expr()), " (Hodge index: signature (1,3))")

print("== (V6) H-degree parity")
print("  H = e1+e2, so (a e1 + b e2 + c alpha).H = 2(a+b) is even for every class of M")
print("  H.C' = 1 is odd")
print("  I_dP: z -> -z swaps C' and C'', so C'+C'' = pi^*h is invariant and [C'] is not in S_dP = M")
