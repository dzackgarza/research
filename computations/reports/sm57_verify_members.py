import sympy as sp, random
x, y = sp.symbols('x y')
MONS = [(i, j) for i in range(5) for j in range(5) if (i + j) % 2 == 0]


def charts(a):
    return [(sp.expand(sum(sp.Rational(a[m]) * x ** m[0] * y ** m[1] for m in MONS)), 'x,y'),
            (sp.expand(sum(sp.Rational(a[m]) * x ** (4 - m[0]) * y ** m[1] for m in MONS)), '1/x,y'),
            (sp.expand(sum(sp.Rational(a[m]) * x ** m[0] * y ** (4 - m[1]) for m in MONS)), 'x,1/y'),
            (sp.expand(sum(sp.Rational(a[m]) * x ** (4 - m[0]) * y ** (4 - m[1]) for m in MONS)), '1/x,1/y')]


def boundary(a):
    bad = []
    tests = [(all(a[(0, j)] == 0 for j in (0, 2, 4)), 'x=0 is a component of B'),
             (all(a[(4, j)] == 0 for j in (0, 2, 4)), 'x=inf is a component of B'),
             (all(a[(i, 0)] == 0 for i in (0, 2, 4)), 'y=0 is a component of B'),
             (all(a[(i, 4)] == 0 for i in (0, 2, 4)), 'y=inf is a component of B')]
    for cond, lab in tests:
        if cond:
            bad.append(lab)
    return bad


def sing(G):
    gens = [sp.expand(G), sp.expand(sp.diff(G, x)), sp.expand(sp.diff(G, y))]
    gb = sp.groebner(gens, x, y, order='lex')
    if list(gb.exprs) == [1]:
        return []
    s = sp.solve_poly_system(gens, x, y)
    if s is None:
        return 'posdim'
    return [(sp.simplify(t[0]), sp.simplify(t[1])) for t in s]


def fullcheck(a, name):
    print("### %s" % name)
    print("  ruling lines contained in B:", boundary(a) or "none")
    q = (a[(2, 0)], a[(1, 1)], a[(0, 2)])
    print("  quadratic part at p (a20,a11,a02):", q, " discriminant:", q[1] ** 2 - 4 * q[0] * q[2])
    tot = []
    for G, lab in charts(a):
        s = sing(G)
        print("   chart %-6s singular points: %s" % (lab, s))
        if s == 'posdim':
            print("   !! positive dimensional singular locus")
            return None
        tot += [(lab, p) for p in s]
    print("   TOTAL singular points:", len(tot), tot)
    print("   tau-invariant (all monomials i+j even):", all(a[m] == 0 for m in a if (m[0] + m[1]) % 2))
    f = sum(sp.Rational(a[m]) * x ** m[0] * y ** m[1] for m in MONS)
    print("   f =", f)
    print("   f(0,0) =", f.subs({x: 0, y: 0}))
    print("   roots of f(1,y):", sp.roots(sp.Poly(sp.expand(f.subs(x, 1)), y)))
    print("   roots of f(-1,y):", sp.roots(sp.Poly(sp.expand(f.subs(x, -1)), y)))
    print("   roots of f(0,y):", sp.roots(sp.Poly(sp.expand(f.subs(x, 0)), y)))
    dp = sp.Poly(sp.expand(sp.discriminant(f, y)), x)
    print("   disc_y(f): degree in x =", dp.degree())
    print("   roots of disc_y(f):", sp.roots(dp))
    print("   disc_y(f) factored:", sp.factor(dp.as_expr()))
    print()
    return tot


aA = {m: 0 for m in MONS}
aA.update({(4, 4): 29, (4, 2): 23, (4, 0): 19, (3, 3): 17, (3, 1): 13, (2, 4): 11, (2, 2): 7,
           (2, 0): 1, (1, 3): 5, (1, 1): 1, (0, 4): 3, (0, 2): 2})
fullcheck(aA, "member A = the repo's explicit polynomial")


def member(free, c=1):
    a11, a13, a20, a22, a42, a24, a44 = free
    a = {m: 0 for m in MONS}
    a[(2, 0)] = a20
    a[(4, 0)] = c - a20
    a[(1, 1)] = a11
    a[(3, 1)] = -a11
    a[(2, 2)] = a22
    a[(4, 2)] = a42
    a[(0, 2)] = -2 * c - a22 - a42
    a[(1, 3)] = a13
    a[(3, 3)] = -a13
    a[(2, 4)] = a24
    a[(4, 4)] = a44
    a[(0, 4)] = c - a24 - a44
    return a


random.seed(3)
good = None
for t in range(300):
    free = tuple(random.randint(-4, 4) for _ in range(7))
    a = member(free)
    if boundary(a):
        continue
    q = (a[(2, 0)], a[(1, 1)], a[(0, 2)])
    if q[0] == 0 or q[1] == 0 or q[2] == 0 or q[1] ** 2 - 4 * q[0] * q[2] == 0:
        continue
    tot = []
    ok = True
    for G, lab in charts(a):
        s = sing(G)
        if s == 'posdim':
            ok = False
            break
        tot += [(lab, p) for p in s]
    if ok and len(tot) == 1 and tot[0][0] == 'x,y' and tot[0][1] == (0, 0):
        good = (free, a)
        break
print("search: free =", good[0])
fullcheck(good[1], "member B: one node at p, bitangent to the ruling fibres {x=1} and {x=-1}")
print("coefficients of member B:", {str(m): good[1][m] for m in MONS})
