"""Exact arithmetic for all three recovered ten-nodal sextics.

See ex:explicit-ten-nodal-sextic in rational-sextic-calculations.md for
the properness and degree arguments; the arithmetic alone is not the theorem.
Run with Sage Python. Parametrization coefficients are in decreasing s-degree;
equation coefficients are in increasing z-degree, then increasing y-degree.
"""

from sage.all import GF, QQ, ZZ, PolynomialRing, gcd, matrix

samples = [
    (
        [[1,1,2,3,2,1,1], [2,3,1,2,3,1,2], [3,2,3,1,2,3,1]],
        [19783,-277523,1236290,-1155576,608968,-195808,26447,
         205052,-1702068,1686557,-1099558,366024,-45478,
         584140,-622975,609573,-130204,8334,
         3528,-73520,-118908,15408,-16747,89450,2144,-14520,-9276,2732],
    ),
    (
        [[1,2,-1,3,1,-2,1], [2,-1,3,2,-1,3,2], [3,1,2,-1,3,1,1]],
        [353242,854135,1639553,1474116,1573705,626953,431741,
         -905038,-3733093,-5037601,-6335498,-3180194,-2000606,
         1409317,4559311,7634496,5321744,3391388,
         -1294722,-3305929,-3762772,-2493799,586665,1160234,840085,
         -130140,-160216,11332],
    ),
    (
        [[1,3,2,-1,1,2,1], [2,1,3,2,-1,1,3], [1,-1,1,3,2,-1,2]],
        [1014125,-2621220,2005061,-92391,-372768,-33222,108463,
         1519685,-2102301,-74830,811610,217891,-408948,
         -1821,1121685,-907945,-514571,565902,
         -829658,327631,617343,-326533,363400,-314135,37488,
         -47192,27072,2017],
    ),
]

R = PolynomialRing(QQ, names=("s", "t"))
s, t = R.gens()
S = PolynomialRing(ZZ, names=("x", "y", "z"))
x, y, z = S.gens()
k = GF(101)
K = PolynomialRing(k, "u")
u = K.gen()
C = PolynomialRing(k, names=("a", "b"))
a, b = C.gens()
exponents = [(6 - j - h, j, h) for h in range(7) for j in range(7 - h)]

for n, (coeffs, equation) in enumerate(samples, 1):
    param = [sum(c * s**(6-i) * t**i for i, c in enumerate(cs)) for cs in coeffs]
    F = sum(c * x**i * y**j * z**h for c, (i, j, h) in zip(equation, exponents))
    assert F and F(*param) == 0
    ps = [K(sum(c * u**(6-i) for i, c in enumerate(cs))) for cs in coeffs]
    assert gcd(ps) == 1
    assert any(cs[0] % 101 for cs in coeffs)
    cols = [
        (ps[0]**i * ps[1]**j * ps[2]**(5-i-j)).list()
        for i in range(6) for j in range(6-i)
    ]
    A = matrix(k, 31, 21, lambda i, j: cols[j][i] if i < len(cols[j]) else 0)
    assert A.rank() == 21
    for chart in [(1, a, b), (a, 1, b), (a, b, 1)]:
        f = C(F(*chart))
        D = f.derivative(a, 2) * f.derivative(b, 2) - f.derivative(a).derivative(b)**2
        assert C.ideal([f, f.derivative(a), f.derivative(b), D]).groebner_basis() == [1]
    print(f"Example {n}: substitution zero, mod-101 gcd 1, rank 21, all three bad-locus bases [1]", flush=True)
