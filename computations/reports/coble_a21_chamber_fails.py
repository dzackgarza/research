#!/usr/bin/env python3
"""A21, the chamber clause: the two one-node members of the counterexample, checked.

Run:  python3 computations/reports/coble_a21_chamber_fails.py
Dependencies: sympy only (no provider, no image).

Model (the direct projective construction, k = 1 node at p = (0,0)):
  Y = P^1 x P^1 with affine coordinates (x, y), tau(x,y) = (-x,-y),
  X^# = {z^2 = f(x,y)} over Y, f tau-invariant of bidegree (4,4) with an
  ordinary node at p and smooth elsewhere, X the minimal resolution,
  e_b = pi^*h_1, f_b = pi^*h_2, H = e_b + f_b, alpha = [D] = pi^*[e].

What is checked, for the two members b_0 and b_star:
  (1) tau-invariance, the node at p (value 0, nondegenerate quadratic part),
  (2) smoothness of the branch curve away from p (Groebner basis of the
      Jacobian ideal in each of the four affine charts of P^1 x P^1),
  (3) every ruling fibre of both rulings: the y-discriminant of f tells which
      rulings {x = x_0} fail to be transverse to the branch curve. A simple
      root is a nodal (irreducible) fibre, a double root is a bitangency whose
      fibre splits, the node's own ruling x = 0 is the I_2 fibre.
  (4) the leading coefficient in each variable, i.e. the fibres at infinity of both
      rulings.

Output: nu(b) = #{delta in Pic : delta^2 = -2, delta.H = 1}, which is the
number of H-degree-1 components of reducible ruling fibres:
  nu(b_0) = 0, nu(b_star) = 4.
"""

import sympy as sp

x, y = sp.symbols('x y')


def build(terms):
    return sp.expand(sum(c * x**i * y**j for (i, j), c in terms.items()))


# member b_0: no ruling fibre splits except the node's
f0 = build({(4, 4): 5, (4, 2): -2, (4, 0): 3, (3, 3): 1, (3, 1): -4,
            (2, 4): 2, (2, 2): 1, (2, 0): 2, (1, 3): -3, (1, 1): 7,
            (0, 4): -1, (0, 2): -5})

# member b_star: the rulings x = 1 and x = -1 are bitangent
fstar = build({(4, 4): 8, (4, 2): 7, (4, 0): 6, (3, 3): 5, (3, 1): 4,
               (2, 4): 3, (2, 2): 2, (2, 0): 3, (1, 3): -13, (1, 1): -28,
               (0, 4): -10, (0, 2): 13})


def ruling_discriminant(f, var):
    """disc of f, read as a polynomial in `var`; returns the discriminant
    divided by the forced square of the node's ruling coordinate."""
    d = sp.expand(sp.discriminant(sp.Poly(f, var).as_expr(), var))
    node = x if var is y else y
    q, r = sp.div(sp.Poly(d, node), sp.Poly(node**2, node))
    assert r.is_zero, 'the node ruling is not a double root'
    return sp.expand(q.as_expr())


def check(name, f):
    print('=' * 72)
    print('member', name)
    P = sp.Poly(f, x, y)
    print('  tau-invariant (i+j even for every monomial):',
          all((i + j) % 2 == 0 for i, j in P.monoms()))
    print('  bidegree:', max(i for i, _ in P.monoms()), max(j for _, j in P.monoms()))
    print('  f(p) =', f.subs({x: 0, y: 0}))
    quad = sp.expand(sum(c * x**i * y**j for (i, j), c in P.terms() if i + j == 2))
    print('  quadratic part at p:', quad,
          '  discriminant:', sp.expand(sp.discriminant(sp.Poly(quad, y).as_expr(), y)))

    # smoothness in the four affine charts of P^1 x P^1
    charts = {
        'x0/x1, y0/y1': f,
        'x0/x1, y1/y0': sp.expand(y**4 * f.subs(y, 1 / y)),
        'x1/x0, y0/y1': sp.expand(x**4 * f.subs(x, 1 / x)),
        'x1/x0, y1/y0': sp.expand(x**4 * y**4 * f.subs({x: 1 / x, y: 1 / y})),
    }
    u, v = sp.symbols('u v')
    for label, g in charts.items():
        G = sp.expand(g.subs({x: u, y: v}))
        ideal = [G, sp.expand(sp.diff(G, u)), sp.expand(sp.diff(G, v))]
        gb = sp.groebner(ideal, u, v, order='lex')
        print('  chart %-14s Groebner basis of (F, F_u, F_v): %s' % (label, list(gb.exprs)))

    # the two rulings
    for var, other, tag in ((y, x, 'x-fibres (e_b)'), (x, y, 'y-fibres (f_b)')):
        q = ruling_discriminant(f, var)
        g = sp.gcd(sp.Poly(q, other), sp.Poly(sp.diff(q, other), other)).as_expr()
        print('  %s: discriminant = %s^2 * q, deg q = %d, gcd(q, q\') = %s'
              % (tag, other, sp.degree(q, other), g))
        print('     q vanishes at the other node ruling?', sp.expand(q.subs(other, 0)) == 0)

    # the ruling restrictions that decide splitting
    for xv in (1, -1):
        print('  f(%s, y) = %s' % (xv, sp.factor(sp.expand(f.subs(x, xv)))))

    # the fibres at infinity of both rulings: the top coefficient in the other variable
    for var, rest, tag in ((x, y, 'x'), (y, x, 'y')):
        lead = sp.Poly(f, var).LC()
        print('  fibre at %s = infinity is {z^2 = %s}, degree %d, gcd(w,w\') = %s'
              % (tag, sp.expand(lead), sp.degree(lead, rest),
                 sp.gcd(sp.Poly(lead, rest), sp.Poly(sp.diff(lead, rest), rest)).as_expr()))


print(__doc__)
check('b_0', f0)
check('b_star', fstar)

print('=' * 72)
print('H-degree bookkeeping in <e_b, f_b, D> (Gram: e_b^2 = f_b^2 = 0,')
print('e_b.f_b = 2, D^2 = -2, D.e_b = D.f_b = 0, H = e_b + f_b):')
e, ff, D = sp.symbols('e_b f_b D')
G = sp.Matrix([[0, 2, 0], [2, 0, 0], [0, 0, -2]])


def dot(a, b):
    return sp.expand((sp.Matrix(1, 3, a) * G * sp.Matrix(3, 1, b))[0])


H = [1, 1, 0]
print('  H.e_b =', dot(H, [1, 0, 0]), ' H.f_b =', dot(H, [0, 1, 0]), ' H.D =', dot(H, [0, 0, 1]))
print('  node fibre D + (L_1 - D): (L_1-D)^2 =', dot([1, 0, -1], [1, 0, -1]),
      ' H.(L_1-D) =', dot(H, [1, 0, -1]))
print('  split fibre over x = 1: C_1 + C_2 = L_1 with C_i.L_1 = 0, C_1.C_2 = 2,')
print('     hence C_i^2 = -2 and C_i.H = C_i.L_2 = 1 (odd): two classes of H-degree 1.')
print()
print('VERDICT')
print('  b_0    : every ruling of both fibrations away from the node\'s has a squarefree')
print('           discriminant and the fibre at infinity is smooth, so no ruling fibre')
print('           splits; the node\'s fibre has H-degrees 0 and 2.  nu(b_0) = 0.')
print('  b_star : the rulings x = +1 and x = -1 are bitangent, splitting into two')
print('           components each of H-degree 1, and no other ruling splits.')
print('           nu(b_star) = 4.')
print('  Since an isometry carrying the chamber of one member to that of the other')
print('  must carry Pic of one onto Pic of the other, and H to H, it would have to')
print('  match these counts.  0 != 4, so no such isometry exists: the chamber clause')
print('  of A21 is false.')

print()
print('Integral classes of square -2 supported on a two-component fibre C_1 + C_2')
print('with C_1.C_2 = 2 (matrix [[-2,2],[2,-2]]): (aC_1+bC_2)^2 = -2(a-b)^2.')
for deg1, deg2, tag in ((1, 1, 'split ruling fibre (both components of H-degree 1)'),
                        (0, 2, 'node I_2 fibre (H-degrees 0 and 2)')):
    sols = []
    for a in range(-6, 7):
        for b in range(-6, 7):
            if a == 0 and b == 0:
                continue
            if -2 * (a - b) ** 2 == -2 and a * deg1 + b * deg2 == 1:
                sols.append((a, b))
    print('  %-52s square -2 and H-degree 1: %s' % (tag, sols if sols else 'none'))

