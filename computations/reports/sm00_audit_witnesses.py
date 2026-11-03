"""m3, swarm smw0b9kmo, direction d6: witness-membership audit.

Independent (sympy, exact rational arithmetic) certificate that each named witness of the
A21 chamber-obstruction is a member of the direct-projective one-node family, plus the
ruling-tangency data that the tracked lemmas silently assume.

Convention: coefficients a[(i,j)] are those of the affine chart centred at the tau-fixed
point which carries the node, with local coordinates (x,y) and the tau-action
(x,y) -> (-x,-y).  The invariant system is the 13 monomials x^i y^j with 0<=i,j<=4 and
i+j even.  The homogeneous bidegree-(4,4) form is
    F(X0,X1,Y0,Y1) = sum a[(i,j)] X0^i X1^(4-i) Y0^j Y1^(4-j).
"""
import sympy as sp

x, y = sp.symbols('x y')
MONS = [(i, j) for i in range(5) for j in range(5) if (i + j) % 2 == 0]


def poly(a):
    return sp.expand(sum(sp.Integer(a.get(m, 0)) * x ** m[0] * y ** m[1] for m in MONS))


def chart_form(a, sx, sy):
    """affine form in the chart x -> x (sx=1) or x -> 1/x (sx=-1), likewise y."""
    return sp.expand(sum(sp.Integer(a.get(m, 0))
                         * x ** (m[0] if sx == 1 else 4 - m[0])
                         * y ** (m[1] if sy == 1 else 4 - m[1]) for m in MONS))


def singular_points(a, sx, sy):
    g = chart_form(a, sx, sy)
    eqs = [g, sp.expand(sp.diff(g, x)), sp.expand(sp.diff(g, y))]
    gb = sp.groebner(eqs, x, y, order='grevlex')
    if list(gb.exprs) == [1]:
        return 'empty'
    sol = sp.solve_poly_system(eqs, x, y)
    if sol is None:
        return 'positive-dimensional'
    return [(sp.nsimplify(s[0]), sp.nsimplify(s[1])) for s in sol]


def audit(name, a):
    print('### %s' % name)
    f = poly(a)
    print('  f =', f)
    bad = [m for m in a if a[m] and ((m[0] + m[1]) % 2 or not (0 <= m[0] <= 4 and 0 <= m[1] <= 4))]
    print('  [1] tau-invariant section (all monomials i+j even, bidegree (4,4)):', not bad)
    print('  [2] f(p) = a00 =', a.get((0, 0), 0), '| node at p:', a.get((0, 0), 0) == 0)
    q = (a.get((2, 0), 0), a.get((1, 1), 0), a.get((0, 2), 0))
    d = sp.Integer(q[1]) ** 2 - 4 * sp.Integer(q[0]) * sp.Integer(q[2])
    print('  [3] quadratic part a20 x^2 + a11 xy + a02 y^2 =', q[0], ',', q[1], ',', q[2],
          '| disc =', d, '| ordinary node:', d != 0)
    print('  [4] tau-fixed values (a00, a04, a40, a44) =',
          (a.get((0, 0), 0), a.get((0, 4), 0), a.get((4, 0), 0), a.get((4, 4), 0)),
          '| no second node at a tau-fixed pt:',
          all(a.get(m, 0) != 0 for m in [(0, 4), (4, 0), (4, 4)]))
    for sx in (1, -1):
        for sy in (1, -1):
            lab = ('x' if sx == 1 else '1/x') + ',' + ('y' if sy == 1 else '1/y')
            s = singular_points(a, sx, sy)
            print('  [5] chart %-8s singular locus: %s' % (lab, s))
    print('  [6] ruling through the node tangent to B: a02 = 0 ?', q[2] == 0,
          '/ a20 = 0 ?', q[0] == 0, '| B transverse to both node rulings:', q[0] != 0 and q[2] != 0)
    print('  [7] f(0,y) factors:', sp.factor_list(sp.expand(f.subs(x, 0))))
    print('  [8] f(x,0) factors:', sp.factor_list(sp.expand(f.subs(y, 0))))
    Dy = sp.expand(sp.discriminant(sp.Poly(f, y), y))
    Dx = sp.expand(sp.discriminant(sp.Poly(f, x), x))
    for nm, D, v in (('disc_y(f)', Dy, x), ('disc_x(f)', Dx, y)):
        fac = sp.factor_list(D)
        print('  [9]', nm, '=', fac[0], '*', [(sp.factor(b), e) for b, e in fac[1]],
              ' | total degree', sp.degree(D, v))
        print('      squarefree part =', sp.factor(sp.sqf_part(D)))
    print()
    return f


W = {}
W['repo member A (corpus sec-explicit-curve)'] = {
    (4, 4): 29, (4, 2): 23, (4, 0): 19, (3, 3): 17, (3, 1): 13, (2, 4): 11, (2, 2): 7, (2, 0): 1,
    (1, 3): 5, (1, 1): 1, (0, 4): 3, (0, 2): 2, (0, 0): 0}
W['m5 b0'] = {(4, 4): 5, (4, 2): -2, (4, 0): 3, (3, 3): 1, (3, 1): -4, (2, 4): 2, (2, 2): 1,
              (2, 0): 2, (1, 3): -3, (1, 1): 7, (0, 4): -1, (0, 2): -5, (0, 0): 0}
W['m5 bstar (affine form of m5 sec-6)'] = {
    (4, 4): 8, (4, 2): 7, (4, 0): 6, (3, 3): 5, (3, 1): 4, (2, 4): 3, (2, 2): 2, (2, 0): 3,
    (1, 3): -13, (1, 1): -28, (0, 4): -10, (0, 2): 13, (0, 0): 0}
W['m6 member B (coefficient list of Thm 2.3)'] = {
    (0, 0): 0, (0, 2): -6, (0, 4): 8, (1, 1): -1, (1, 3): 4, (2, 0): -2, (2, 2): 1, (2, 4): -3,
    (3, 1): 1, (3, 3): -4, (4, 0): 3, (4, 2): 3, (4, 4): -4}
W["m8 F' (node-centred chart x1=y1=1)"] = {
    (4, 4): 1, (4, 0): 1, (3, 1): 1, (2, 2): 1, (2, 0): 1, (1, 3): 1, (1, 1): 1, (0, 4): 1, (0, 0): 0}

W["m3 checked: both node rulings tangent (a20 = a02 = 0)"] = {
    (1, 1): 1, (2, 2): 1, (4, 0): 1, (0, 4): 1, (4, 4): 1, (0, 0): 0}

F = {}
for name, a in W.items():
    F[name] = audit(name, a)

print('=== bitangency / split checks ===')
for name in list(W.keys()):
    f = F[name]
    print('--', name)
    for r in (1, -1):
        g = sp.Poly(sp.expand(f.subs(x, r)), y)
        print('   f(%d,y) =' % r, sp.factor(g.as_expr()), '| roots:', sp.roots(g))
