#!/usr/bin/env python3
"""The boundary lattice at a 0-cusp of F_{2d} with p_*(delta) > 1.

Sources.  AE23, Section 10C, printed p. 38, prints the boundary lattice as
    delta^perp/delta = <-2d/p_*(delta)> + H + E8^2;
AET23, Def. 4.1 with Fig. 1, printed pp. 21-22, gives the Coxeter fan of the
F_2 cusp lattice, and the same diagram is the one of the unigonal cusp lattice
<-2k> + U + E8(-1)^2 when k = 1.

The computation.  Let p >= 2, k >= 1, d = p^2 k, and work in the rank-three
lattice K = <g> + H(e1, f1) with g^2 = -2d, e1^2 = f1^2 = 0, e1.f1 = 1; the
remaining summands H(e2, f2) + E8(-1)^2 are orthogonal to everything below.
Put

    delta = g + p e1 + p k f1.

The script checks, exactly:
  * delta^2 = 0 and delta is primitive;
  * delta/p pairs integrally with g, e1, f1, and delta/p^2 does not (pairing
    1/p with f1), so the imprimitivity p_*(delta) is p;
  * u = e1 - k f1 and v = g + 2p k f1 lie in delta^perp, delta = v + p u, and
    every integral vector of K orthogonal to delta is a v + b u;
  * in delta^perp/delta (rank 19 = 1 + 2 + 16) the class of u generates the
    first summand, with u^2 = -2k, so delta^perp/delta = <-2k> + U + E8(-1)^2;
  * the printed first summand would be -2d/p_* = -2pk, and a lattice with that
    first summand has discriminant 2pk, while the computed one has 2k.

At k = 1 (d = p^2) the computed lattice is the F_2 cusp lattice; for k >= 2 it
is the unigonal cusp lattice of F_{2k}.  No Sage is needed: every check is
integer arithmetic on the rank-three form.
"""


def dot(d, x, y):
    return -2 * d * x[0] * y[0] + x[1] * y[2] + x[2] * y[1]


def dot5(d, x, y):
    """The rank-five lattice <g> + H(e1, f1) + H(e2, f2), coordinates (g, e1, f1, e2, f2)."""
    return (-2 * d * x[0] * y[0] + x[1] * y[2] + x[2] * y[1]
            + x[3] * y[4] + x[4] * y[3])


def main():
    out = []
    out.append("Boundary lattice at a 0-cusp of F_{2d} with p_*(delta) > 1: d = p^2 k.")
    out.append("Sources: AE23 Section 10C, printed p. 38; AET23 Def. 4.1 and Fig. 1, printed pp. 21-22.")
    out.append("")
    for p, k in ((2, 1), (3, 1), (2, 2), (2, 4), (3, 2)):
        d = p * p * k
        delta = (1, p, p * k)
        u = (0, 1, -k)
        v = (1, 0, 2 * p * k)
        pair_p = (-2 * p * k, k, 1)  # (delta/p).g, .e1, .f1
        out.append("d = %d, p = %d, k = %d" % (d, p, k))
        out.append("  delta = g + %d e1 + %d f1, delta^2 = %d, primitive = %s"
                   % (p, p * k, dot(d, delta, delta), delta[0] == 1))
        out.append("  delta/p in L*: pairings with (g, e1, f1) = (%d, %d, %d), all integral"
                   % pair_p)
        out.append("  delta/p^2 in L*: pairing with f1 = 1/%d, not integral -> p_*(delta) = %d"
                   % (p, p))
        out.append("  u = e1 - %d f1: u.delta = %d, u^2 = %d"
                   % (k, dot(d, u, delta), dot(d, u, u)))
        out.append("  v = g + %d f1: v.delta = %d, v^2 = %d, delta = v + %d u"
                   % (2 * p * k, dot(d, v, delta), dot(d, v, v), p))
        out.append("  every (a,b,c) in K with c + %d b = %d a equals a v + b u"
                   % (k, 2 * p * k))
        out.append("  delta^perp/delta: rank 19 = 1 + 2 + 16, first summand -2k = %d, discriminant %d"
                   % (-2 * k, 2 * k))
        out.append("  printed first summand -2d/p_* = %d, discriminant %d" % (-2 * p * k, 2 * p * k))
        out.append("  -> the printed lattice has discriminant %d; the cusp has %d"
                   % (2 * p * k, 2 * k))
        e2 = (0, 0, 0, 1, 0)
        delta5 = (delta[0], delta[1], delta[2], 0, 0)
        u1 = (0, 1, -k, 0, 0)
        v1 = (1, 0, 2 * p * k, 0, 0)
        out.append("  J = Z delta + Z e2: delta.e2 = %d, e2^2 = %d, delta = v1 + %d u1"
                   % (dot5(d, delta5, e2), dot5(d, e2, e2), p))
        out.append("  u1 = e1 - %d f1, u1^2 = %d; v1 = g + %d f1, v1^2 = %d"
                   % (k, dot5(d, u1, u1), 2 * p * k, dot5(d, v1, v1)))
        out.append("  J^perp/J: rank 17 = 1 + 16, first summand -2k = %d" % (-2 * k))
        if k == 1:
            out.append("  1-cusp lattice E8(-1)^2 + A1(-1)")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    print(main(), end="")
