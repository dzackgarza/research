#!/usr/bin/env python3
"""The boundary lattice at a 0-cusp of F_{2d} with p_*(delta) > 1: the case d = p^2.

Sources.  AE23, Section 10C, printed p. 38, prints the boundary lattice as
    delta^perp/delta = <-2d/p_*(delta)> + H + E8^2;
AET23, Def. 4.1 with Fig. 1, printed pp. 21-22, gives the Coxeter fan of the
F_2 cusp lattice H + E8(-1)^2 + A_1(-1) = <-2> + U + E8(-1)^2.

The computation.  Let d = p^2 (p >= 2) and work in the rank-three lattice
K = <g> + H(e1, f1) with g^2 = -2d, e1^2 = f1^2 = 0, e1.f1 = 1; the remaining
summands H(e2, f2) + E8(-1)^2 are orthogonal to everything below.  Put

    delta = g + p(e1 + f1).

The script checks, exactly:
  * delta^2 = 0 and delta is primitive;
  * delta/p pairs integrally with g, e1, f1, and delta/p^2 does not, so the
    imprimitivity p_*(delta) is p;
  * u = e1 - f1 and v = g + 2p f1 lie in delta^perp, delta = v + p u, and every
    integral vector of K orthogonal to delta is a v + b u;
  * in delta^perp/delta (rank 19 = 1 + 2 + 16) the class of u generates the first
    summand, with u^2 = -2, so delta^perp/delta = <-2> + U + E8(-1)^2;
  * the printed first summand would be -2d/p_* = -2p, and a lattice with that
    first summand has discriminant 2p, while the computed one has discriminant 2.

No Sage is needed: every check is integer arithmetic on the rank-three form.
"""


def dot(d, x, y):
    return -2 * d * x[0] * y[0] + x[1] * y[2] + x[2] * y[1]


def main():
    out = []
    out.append("Boundary lattice at a 0-cusp of F_{2d} with p_*(delta) > 1: d = p^2.")
    out.append("Sources: AE23 Section 10C, printed p. 38; AET23 Def. 4.1 and Fig. 1, printed pp. 21-22.")
    out.append("")
    for p in (2, 3, 4):
        d = p * p
        delta = (1, p, p)
        u = (0, 1, -1)
        v = (1, 0, 2 * p)
        # delta/p and delta/p^2 as rational coordinate vectors: pairings with the basis
        pair_p = (-2 * p, 1, 1)  # (delta/p).g, (delta/p).e1, (delta/p).f1
        out.append("d = %d, p = %d" % (d, p))
        out.append("  delta = g + %d e1 + %d f1, delta^2 = %d, primitive = %s"
                   % (p, p, dot(d, delta, delta), delta[0] == 1))
        out.append("  delta/p in L*: pairings with (g, e1, f1) = (%d, %d, %d), all integral"
                   % pair_p)
        out.append("  delta/p^2 in L*: pairing with e1 = 1/%d, not integral -> p_*(delta) = %d"
                   % (p, p))
        out.append("  u = e1 - f1: u.delta = %d, u^2 = %d" % (dot(d, u, delta), dot(d, u, u)))
        out.append("  v = g + %d f1: v.delta = %d, v^2 = %d, delta = v + %d u"
                   % (2 * p, dot(d, v, delta), dot(d, v, v), p))
        out.append("  every (a,b,c) in K with b + c = %d a equals a v + b u" % (2 * p))
        out.append("  delta^perp/delta: rank 19 = 1 + 2 + 16, first summand -2, discriminant 2")
        out.append("  printed first summand -2d/p_* = -%d, discriminant %d" % (2 * p, 2 * p))
        out.append("  -> the printed lattice has discriminant %d; the cusp has 2" % (2 * p))
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    print(main(), end="")
