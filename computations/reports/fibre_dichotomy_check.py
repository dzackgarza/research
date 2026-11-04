"""Adjudication of the I_2 / IV dichotomy for the node-ruling fibre, at the maintained
Sage level (pin c546077d). For each member: the strict transform at the node in the
blow-up chart (x,y) = (X Y, Y); the branch divisor of pi^*C~ -> C~ is the zero divisor
of ftwiddle(0,Y) = a02 + a04 Y^2. Output per member: a02, a04, the polynomial, and
whether it has two distinct roots (-> I_2, degrees 0 and 2) or is a double point
(-> Kodaira IV, degrees 1,1,0). Exact rational arithmetic throughout."""
from sage.all import PolynomialRing, QQ, factor

# coefficients from the tracked audits, node-centred chart per member's own audit file.
# each entry: (name, a20, a11, a02, a04)
MEMBERS = [
    ("corpus   (sec-explicit-curve)", 1, 1, 2, 3),
    ("m5 b0",                          2, 7, -5, -1),
    ("m5 bstar",                       3, -28, 13, -10),
    ("m6 member B (coeff list)",       -2, -1, -6, 8),
    ("m8 F' (corner x1=y1=1)",         1, 1, 0, 1),
    ("m3 check both tangent",          0, 1, 0, 1),
]
R = PolynomialRing(QQ, 'Y'); Y = R.gen()
for name, a20, a11, a02, a04 in MEMBERS:
    node_ok = a11**2 - 4*a20*a02 != 0
    g = a02 + a04*Y**2
    d = disc(g) if g != 0 else 0
    ftype = "I_2 (two distinct geometric roots -> D+(L_1-D), degrees 0,2)" if d != 0 else ("IV (double point -> C1+C2+D, degrees 1,1,0)" if g != 0 else "DEGENERATE")
    print(f"{name}: a02={a02}, a04={a04}, node condition ok: {node_ok}, ftwiddle(0,Y) = {g}, disc = {d} -> {ftype}")
