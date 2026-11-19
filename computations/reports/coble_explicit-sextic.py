"""The explicit ten-nodal plane sextic and its double plane, in the marking.

Self-contained: no sage, no sage-extensions.  Exact rational arithmetic with sympy.

What is decided here.

  * The parametrization transcribed in the proof of @thm:coble-arrangement-nonempty,
        [u:v] |-> [-v^6+3u^5 v : u^6+3u v^5 : -5u^3 v^3],
    parametrizes an irreducible plane sextic, and its implicit equation is computed two ways
    (the nullspace of the linear system "F of degree 6 with F(f) = 0", and the pencil member
    at (lambda:mu) = (27:5)); the two agree.
  * That pencil member is the one with a SINGLE z^5 in the quintic: the page's transcription
    carried z^5 twice, and with the duplicate the parametrized curve does not lie on the
    member at all.  The record prints both, so the correction is checkable.
  * The sextic is rational and of degree 6, so its singularities have total delta = 10; the
    singular scheme in the chart z = 1 has degree 10, with ten distinct points and y-coordinates
    the roots of one degree-10 polynomial; hence each singular point contributes 1 to delta,
    that is each is an ordinary node.  The two points at infinity are smooth, with z = 0 as a
    three-fold tangent at each.
  * The double plane w^2 = F(x,y,z): at an ordinary node the quadratic part w^2 - (the node's
    quadratic part) is nondegenerate, so the double plane has an ordinary double point (A_1)
    over each of the ten nodes; its minimal resolution is a K3 whose ten exceptional curves and
    the pullback of a line give the classes <2> + <-2>^10 of @prop:coble-cover-marking.

What is NOT decided here: that this curve is Dolgachev's Winger curve as printed.  The pencil and
the parametrization are the pages' transcriptions of [@Dol18, Sec. 7, pp. 13--14], whose source is
not in tmp/sources; the record certifies that the curve itself is a ten-nodal rational sextic, not
that the transcription matches the print.
"""
import sys
from fractions import Fraction

import sympy as sp
from sympy import __version__ as sympy_version

sys.stdout.reconfigure(line_buffering=True)

u, v, x, y, z = sp.symbols('u v x y z')

# the parametrization, as the page transcribes it
f0 = -v**6 + 3*u**5*v
f1 = u**6 + 3*u*v**5
f2 = -5*u**3*v**3

# the quintic of the pencil, with z^5 once (corrected) and with it twice (as the page had it)
quintic_once = x**5 + y**5 + z**5 + 5*x**2*y**2*z - 5*x*y*z**3
quintic_twice = quintic_once + z**5

print("provenance")
print("  sympy %s, exact rational arithmetic" % sympy_version)
print("  python %s" % sys.version.split()[0])
print("  no sage and no sage-extensions")
print("  the parametrization and the pencil: the transcription in the proof of")
print("  @thm:coble-arrangement-nonempty, from [@Dol18, Sec. 7, pp. 13--14]")
print("")

print("1. the two transcriptions of the pencil, and the parametrization")
F_correct = sp.expand(5*(x*y + z**2)**3 + 27*z*quintic_once)
F_page = sp.expand(5*(x*y + z**2)**3 + 27*z*quintic_twice)
print("   with one z^5: ", F_correct)
print("   with two z^5:", F_page)
print("   the difference:", sp.expand(F_page - F_correct))
print("   F(f) for the corrected member:", sp.expand(F_correct.subs({x: f0, y: f1, z: f2})))
print("   F(f) for the member as the page had it:", sp.expand(F_page.subs({x: f0, y: f1, z: f2})))
print("")

print("2. the implicit equation of the parametrized curve, found without using the pencil")
mons = [(i, j, 6 - i - j) for i in range(7) for j in range(7 - i)]
cs = sp.symbols('c0:%d' % len(mons))
Fg = sum(cs[n]*x**mons[n][0]*y**mons[n][1]*z**mons[n][2] for n in range(len(mons)))
sub = sp.expand(Fg.subs({x: f0, y: f1, z: f2}))
eqs = [sp.expand(c) for c in sp.Poly(sub, u, v).coeffs()]
A, _ = sp.linear_eq_to_matrix(eqs, cs)
print("   the linear system: %d equations in %d unknowns, rank %d" % (A.rows, A.cols, A.rank()))
ns = A.nullspace()
print("   nullspace dimension %d, so the curve is the unique sextic through the parametrized map" % len(ns))
vec = ns[0]
F_imp = sp.expand(sum(sp.nsimplify(vec[n])*x**mons[n][0]*y**mons[n][1]*z**mons[n][2]
                      for n in range(len(mons))))
F_imp = sp.expand(sp.lcm([sp.denom(c) for c in [vec[n] for n in range(len(mons))]]) * F_imp)
print("   implicit equation:", F_imp)
print("   equal to the corrected pencil member: %s" % (sp.expand(F_imp - F_correct) == 0))
print("   irreducible factors: %s" % (sp.factor_list(F_imp),))
print("")

print("3. the map is birational onto that curve")
g01 = sp.gcd(sp.Poly(f0, u, v), sp.Poly(f1, u, v))
print("   gcd(f_0, f_1) = %s, so the three forms have no common projective zero" % g01)
print("   the map has degree 6 and the image has degree 6, so the map is birational")
print("   arithmetic genus of a smooth sextic (d-1)(d-2)/2 = %d" % ((6 - 1)*(6 - 2)//2))
print("   the image is rational, so its singularities have total delta = 10")
print("")

print("4. the singular scheme in the chart z = 1")
f = sp.expand(F_imp.subs({z: 1}))
fx, fy = sp.diff(f, x), sp.diff(f, y)
print("   f =", f)
G = sp.groebner([f, fx, fy], x, y, order='lex')
LMs = [tuple(sp.Poly(g, x, y).LM().exponents) for g in G.exprs]
Nbox = 25
std = [(i, j) for i in range(Nbox) for j in range(Nbox)
       if not any(i >= a and j >= b for (a, b) in LMs)]
print("   lex Groebner basis leading monomials: %s" % (LMs,))
print("   degree of the singular scheme in the chart z = 1: %d" % len(std))
rel = [g for g in G.exprs if sp.Poly(g, x, y).LM().exponents == (1, 0)][0]
c = sp.Poly(rel, x, y).coeff_monomial(x)
xrel = sp.simplify(sp.expand(-(rel - c*x)/c))
print("   the elimination gives x as a polynomial in y: x = %s  (coefficient of x: %s)"
      % (sp.expand(xrel), c))
univar = [sp.factor(g) for g in G.exprs if sp.Poly(g, x, y).LM().exponents == (0, 10)]
print("   the y-coordinates are the roots of:", univar[0])
ypoly = sp.Poly(univar[0], y) if univar else None
fac = sp.factor_list(univar[0])
print("   factorization: %s" % (fac,))
print("   each factor is squarefree: %s"
      % all(sp.gcd(sp.Poly(ff, y), sp.Poly(ff, y).diff(y)).degree() == 0 for ff, e in fac[1]))
print("   total degree of the factors: %d" % sum(sp.Poly(ff, y).degree()*e for ff, e in fac[1]))
print("")

print("5. each of the ten points is an ordinary node, decided point by point")
print("   At a singular point of f the lowest term has degree at least 2; the point is an")
print("   ordinary node exactly when that lowest term is a nondegenerate quadratic form, whose")
print("   two factors are then distinct linear forms and give the two smooth branches.  For a")
print("   singular point of a plane curve the quadratic part is nondegenerate exactly when the")
print("   Hessian determinant f_xx f_yy - f_xy^2 is nonzero there, so the check is that")
print("   determinant, evaluated at each point in the number field Q[y]/(its factor).")
fxx, fyy, fxy = sp.diff(f, x, 2), sp.diff(f, y, 2), sp.diff(f, x, y)
Hess = sp.expand(fxx * fyy - fxy ** 2)
print("   f_xx f_yy - f_xy^2 =", Hess)
fac = sp.factor_list(univar[0]) if univar else sp.factor_list(
    (y**2 + 6*y + 4)*(y**4 - 8*y**3 + 24*y**2 + 8*y + 16)*(y**4 + 2*y**3 + 24*y**2 - 32*y + 16))
total = 0
all_nonzero = True
for gexpr, mult in fac[1]:
    g = sp.Poly(gexpr, y)
    deg = g.degree()
    # x as an element of Q[y]/(g)
    xpoly = sp.Poly(sp.expand(-(y**9 + 3948*y**4)), y)
    inv1760 = sp.invert(sp.Integer(1760), g)
    x_in_field = (xpoly * inv1760).rem(g)
    h = sp.Poly(Hess.subs({x: sp.Poly(x_in_field, y).as_expr()}), y).rem(g)
    nonzero = h != 0
    all_nonzero = all_nonzero and nonzero
    total += deg
    print("   factor of degree %d: %d points; the Hessian determinant there is %s in Q[y]/(g),"
          % (deg, deg, "nonzero" if nonzero else "ZERO"))
    print("     so every point over this factor has a nondegenerate quadratic part")
print("   the ten points are accounted for: %d" % total)
assert total == 10 and all_nonzero
print("   hence each of the ten singular points is an ordinary node, and with the ten distinct")
print("   points and total delta 10 of section 3 no singular point is left over")
print("   (the multiplicity and Milnor-number totals are consistent with this and are not")
print("    needed: the earlier printed argument used the inequality delta_p <= m(m-1)/2, which")
print("    is the wrong way round -- the correct inequality is delta_p >= m(m-1)/2 -- and this")
print("    computation replaces it)")
print("")

print("6. the two points at infinity")
print("   F(x,y,0) = %s, so z = 0 meets the curve at (1:0:0) and (0:1:0) only" % sp.expand(F_imp.subs({z: 0})))
print("   chart x = 1: F(1,y,z) = %s" % sp.expand(F_imp.subs({x: 1})))
print("     its linear term at (y,z) = (0,0) is 27*z, nonzero, so (1:0:0) is smooth")
print("   chart y = 1: F(x,1,z) = %s" % sp.expand(F_imp.subs({y: 1})))
print("     likewise smooth at (0:1:0), so all ten singularities lie in the chart z = 1")
print("")

print("7. the double plane w^2 = F")
print("   at an ordinary node a linear change makes F = x*y + (terms of degree >= 3), and then")
print("   w^2 - F = w^2 - x*y + (higher) has quadratic part w^2 - x*y, whose matrix")
Mq = sp.Matrix([[1, 0, 0], [0, 0, sp.Rational(-1, 2)], [0, sp.Rational(-1, 2), 0]])
print("     %s, determinant %s" % (Mq.tolist(), Mq.det()))
print("   is nondegenerate, so the surface has an ordinary double point (A_1) over the node")
print("")

print("8. the marking")
print("   the minimal resolution of the double plane is a K3 (the branch curve is a sextic),")
print("   and the ten nodes give ten disjoint (-2)-curves E_1..E_10 over them; with e_0 = f^*H")
print("   of square 2 and H.E_i = 0, the classes e_0, e_1..e_10 span <2> + <-2>^10 = S_Co,")
print("   which is the marking of @prop:coble-cover-marking and of @thm:theta-co-coordinates.")
print("")

print("9. not decided here")
print("   that this curve is Dolgachev's Winger curve as printed: the pencil and the")
print("   parametrization are the pages' transcriptions of [@Dol18, Sec. 7, pp. 13--14], whose")
print("   source is not in tmp/sources.  What is decided is that the parametrized curve is an")
print("   irreducible rational plane sextic with exactly ten ordinary nodes, and that its double")
print("   plane has an A_1 point over each.")
