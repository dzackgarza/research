"""Picard number of the member b_star of the Coble one-node family.

X_hat is the minimal resolution of the double cover z^2 = f_star(x, y) of
P^1 x P^1, f_star of bidegree (4, 4) as in coble_a21_chamber_fails.py, with
one ordinary node at p = (0, 0).  The Coble involution iota covers
tau(x, y) = (-x, -y).

Method (van Luijk 2007; Elsenhans-Jahnel 2011).  For an odd prime p of good
reduction and q = p^n:
  tr(F^n | H^2)       = #X_hat(F_q) - 1 - q^2,
  tr(F^n iota | H^2)  = #X_hat^iota(F_q) - 1 - q^2,
where X_hat^iota is the twist of X_hat by iota.  With s a square root of a
non-square n0 of F_q, the points fixed by Frob o iota are x = s a, y = s b,
and z in F_q or z in s F_q, according to the lift z -> eps z of tau.  So the
twist is z^2 = g(a, b) (eps = +1) or z^2 = n0 g(a, b) (eps = -1), with
g(a, b) = f_star(s a, s b) = sum c_ij n0^((i+j)/2) a^i b^j.  A double cover
w^2 = h of P^1 x P^1 with one ordinary node and smooth elsewhere has
#(resolution)(F_q) = sum_{P in P^1 x P^1 (F_q)} (1 + chi(h(P))) + q, the
exceptional curve being a smooth conic (q + 1 points) over the node.
The eps with H^2_+ algebraic is the Coble lift: tr(F^n | H^2_+) / q^n is
an integer for every n.  On H^2_- the class v = D_{1,+} - D_{-1,+} is defined
over Q (f_star(1, y) = ((y-1)(y-3))^2), so F v = p v, and the characteristic
polynomial on the 10-dimensional complement v^perp of H^2_- is computed from
the traces s_n = tr(F^n | H^2_-) - p^n by Newton's identities and the
functional equation.
"""
import os, sys, time
GP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'coble_766_a20_counts.gp')
from sage.all import (GF, pari, PolynomialRing, QQ, ZZ, Ideal, prod, factor,
                      cyclotomic_polynomial, Integer)

R = PolynomialRing(ZZ, ['x', 'y'])
x, y = R.gens()
COEFFS = {(4, 4): 8, (4, 2): 7, (4, 0): 6, (3, 3): 5, (3, 1): 4,
          (2, 4): 3, (2, 2): 2, (2, 0): 3, (1, 3): -13, (1, 1): -28,
          (0, 4): -10, (0, 2): 13}
FSTAR = sum(c * x**i * y**j for (i, j), c in COEFFS.items())


def good_reduction(p):
    """The branch curve mod p is smooth on P^1 x P^1 over F_p-bar except
    for an ordinary node at (0, 0)."""
    Fp = GF(p)
    S = PolynomialRing(Fp, ['u', 'v'])
    u, v = S.gens()
    f = FSTAR.change_ring(Fp)
    charts = [f(u, v), (v**4 * f(u, 1 / v)).numerator(),
              (u**4 * f(1 / u, v)).numerator(),
              (u**4 * v**4 * f(1 / u, 1 / v)).numerator()]
    ok = True
    for k, G in enumerate(charts):
        G = S(G)
        I = Ideal([G, G.derivative(u), G.derivative(v)])
        expected = Ideal([u, v]) if k == 0 else Ideal([S(1)])
        if k == 0:
            ok &= I.radical() == expected
        else:
            ok &= I == expected
    ok &= Fp(28**2 - 4 * 3 * 13) != 0
    return ok


def power_sums(coeffs, m):
    """Power sums p_1..p_m of the roots of t^d + coeffs[1] t^(d-1) + ..."""
    d = len(coeffs) - 1
    ps = []
    for k in range(1, m + 1):
        val = -k * coeffs[k] if k <= d else 0
        val -= sum(coeffs[i] * ps[k - i - 1] for i in range(1, min(k - 1, d) + 1))
        ps.append(val)
    return ps


def complement_poly(p, rows, idx):
    """Normalized char poly Q(t) of F/p on v^perp in H^2_- (degree 10), for
    each sign of the functional equation Q(t) = sign t^10 Q(1/t) that the
    traces n <= 5 allow, with the check against every computed n."""
    nmax = max(rows)
    P = [QQ((rows[n][0] - rows[n][idx]) / 2 - p**n) / p**n for n in range(1, nmax + 1)]
    a = [QQ(1)]
    for k in range(1, 6):
        a.append(-(P[k - 1] + sum(a[i] * P[k - i - 1] for i in range(1, k))) / k)
    t = PolynomialRing(QQ, 't').gen()
    cands = []
    for sign in (1, -1):
        if sign == -1 and a[5] != 0:
            continue
        c = a + [sign * a[10 - k] for k in range(6, 11)]
        Q = sum(c[k] * t**(10 - k) for k in range(11))
        cands.append((sign, Q, power_sums(c, nmax) == P))
    return cands


# Traces on H^2 of F^n and of F^n.iota (eps = -1), from coble_766_a20_counts.gp:
#   traces(p, n) for n <= 4, and for p = 13, n = 5 the sum of
#   half(13, 5, k0, k1) over [0,45000), [45000,75000), [75000,110000),
#   [110000,145000), [145000,185646), minus 1 + q^2.
TRACES = {
    11: {1: (52, 36), 2: (724, 244), 3: (10126, 8508), 4: (118584, 115672),
         5: (832072, 456336)},
    13: {1: (26, 52), 2: (1638, 52), 3: (25688, 676), 4: (199082, 86528),
         5: (2390336, -162578)},
}


if __name__ == '__main__':
    from sage.all import euler_phi
    for p, tr in TRACES.items():
        print('=' * 72)
        print('p = %d: good reduction: %s' % (p, good_reduction(p)))
        rows = {n: (a, None, b) for n, (a, b) in tr.items()}
        for n, (a, b) in tr.items():
            print('  n=%d  tr F^n|H^2 = %d  tr F^n.iota|H^2 = %d  tr F^n|H^2_+ = %s p^n'
                  '  tr F^n|H^2_- = %d' % (n, a, b, QQ((a + b) // 2) / p**n, (a - b) // 2))
        for sign, Q, ok in complement_poly(p, rows, 2):
            t = Q.parent().gen()
            print('  sign %+d of Q(t) = sign t^10 Q(1/t): consistent with n <= %d: %s'
                  % (sign, max(tr), ok))
            print('    p^10 Q(t/p) = %s' % factor(p**10 * Q(t / p)))
            cyc = [d for d in range(1, 400) if euler_phi(d) <= 10 and
                   Q % cyclotomic_polynomial(d, t) == 0]
            print('    cyclotomic factors Phi_d of Q: d in %s' % cyc)
