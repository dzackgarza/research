from sage.all import *
from sage.rings.localization import Localization
from sage.combinat.free_module import CombinatorialFreeModule
from sage.algebras.tensor_algebra import TensorAlgebra

# --------------------------------------------------------------------
# Standard singleton rings and fields
# --------------------------------------------------------------------

assert ZZ in Rings()
assert ZZ in Rings().Commutative()
assert ZZ in Rings().Commutative().IntegralDomains()
assert ZZ in Rings().GcdDomains()
assert ZZ in Rings().UniqueFactorizationDomains()
assert ZZ in Rings().PrincipalIdealDomains()
assert ZZ in Rings().EuclideanDomains()
assert ZZ in Rings().DedekindDomains()
assert ZZ in Rings().NoetherianRings()
assert ZZ in Rings().Characteristic(0)
assert ZZ in Rings().Commutative().KrullDimension(1)
assert ZZ not in Rings().Fields()

assert QQ in Rings()
assert QQ in Rings().Commutative()
assert QQ in Rings().Fields()
assert QQ in Rings().Finite().Fields() is False  # only here to make intent explicit
assert QQ in Rings().NumberFields()
assert QQ in Rings().GlobalFields()
assert QQ in Rings().Characteristic(0)
assert QQ not in Rings().FiniteFields()

assert AA in Rings()
assert AA in Rings().Commutative()
assert AA in Rings().Fields()
assert AA in Rings().RealFields()
assert AA in Rings().Characteristic(0)
assert AA not in Rings().AlgebraicallyClosedFields()

assert QQbar in Rings()
assert QQbar in Rings().Commutative()
assert QQbar in Rings().Fields()
assert QQbar in Rings().AlgebraicallyClosedFields()
assert QQbar in Rings().Characteristic(0)
assert QQbar not in Rings().NumberFields()

assert RR in Rings()
assert RR in Rings().Commutative()
assert RR in Rings().Fields()
assert RR in Rings().RealFields()
assert RR in Rings().Topological().Complete()
assert RR in Rings().Fields().LocalFields()
assert RR in Rings().Fields().GlobalFields().Archimedean()
assert RR in Rings().Characteristic(0)

assert CC in Rings()
assert CC in Rings().Commutative()
assert CC in Rings().Fields()
assert CC in Rings().ComplexFields()
assert CC in Rings().AlgebraicallyClosedFields()
assert CC in Rings().Topological().Complete()
assert CC in Rings().Fields().LocalFields()
assert CC in Rings().Fields().GlobalFields().Archimedean()
assert CC in Rings().Characteristic(0)

assert RDF in Rings()
assert RDF in Rings().Commutative()
assert RDF in Rings().Fields()
assert RDF in Rings().RealFields()
assert RDF in Rings().Topological().Complete()
assert RDF in Rings().Characteristic(0)

assert CDF in Rings()
assert CDF in Rings().Commutative()
assert CDF in Rings().Fields()
assert CDF in Rings().ComplexFields()
assert CDF in Rings().Topological().Complete()
assert CDF in Rings().Characteristic(0)

assert SR in Rings()
assert SR in Rings().Commutative()
assert SR in Rings().Characteristic(0)
assert SR not in Rings().Fields()
assert SR not in Rings().IntegralDomains()

# --------------------------------------------------------------------
# Finite quotient rings and finite fields
# --------------------------------------------------------------------

F2 = ZZ.quotient(2 * ZZ)
F3 = ZZ.quotient(3 * ZZ)
Z6 = ZZ.quotient(6 * ZZ)

assert F2 in Rings()
assert F2 in Rings().Commutative()
assert F2 in Rings().Finite()
assert F2 in Rings().Fields()
assert F2 in Rings().FiniteFields()
assert F2 in Rings().Characteristic(2)

assert F3 in Rings()
assert F3 in Rings().Commutative()
assert F3 in Rings().Finite()
assert F3 in Rings().Fields()
assert F3 in Rings().FiniteFields()
assert F3 in Rings().Characteristic(3)

assert Z6 in Rings()
assert Z6 in Rings().Commutative()
assert Z6 in Rings().Finite()
assert Z6 in Rings().Characteristic(6)
assert Z6 not in Rings().Fields()
assert Z6 not in Rings().IntegralDomains()

K9 = GF(9)
K25 = GF(25)

assert K9 in Rings()
assert K9 in Rings().Commutative()
assert K9 in Rings().Finite()
assert K9 in Rings().Fields()
assert K9 in Rings().FiniteFields()
assert K9 in Rings().Characteristic(3)

assert K25 in Rings()
assert K25 in Rings().Commutative()
assert K25 in Rings().Finite()
assert K25 in Rings().Fields()
assert K25 in Rings().FiniteFields()
assert K25 in Rings().Characteristic(5)

# --------------------------------------------------------------------
# Number fields, quadratic fields, cyclotomic fields, orders
# --------------------------------------------------------------------

x = polygen(QQ, 'x')

K = NumberField(x^2 + 1, 'a')
L = QuadraticField(5, 'b')
C7 = CyclotomicField(7)

assert K in Rings()
assert K in Rings().Commutative()
assert K in Rings().Fields()
assert K in Rings().NumberFields()
assert K in Rings().GlobalFields()
assert K in Rings().Characteristic(0)

assert L in Rings()
assert L in Rings().Commutative()
assert L in Rings().Fields()
assert L in Rings().NumberFields()
assert L in Rings().QuadraticNumberFields()
assert L in Rings().GlobalFields()
assert L in Rings().Characteristic(0)

assert C7 in Rings()
assert C7 in Rings().Commutative()
assert C7 in Rings().Fields()
assert C7 in Rings().NumberFields()
assert C7 in Rings().CyclotomicFields()
assert C7 in Rings().GlobalFields()
assert C7 in Rings().Characteristic(0)

OK = K.ring_of_integers()
OL = L.ring_of_integers()
OC7 = C7.ring_of_integers()

assert OK in Rings()
assert OK in Rings().Commutative()
assert OK in Rings().IntegralDomains()
assert OK in Rings().NoetherianRings()
assert OK in Rings().IntegrallyClosedDomains()
assert OK in Rings().DedekindDomains()
assert OK in Rings().Commutative().KrullDimension(1)
assert OK not in Rings().Fields()

assert OL in Rings().DedekindDomains()
assert OL in Rings().Commutative().KrullDimension(1)
assert OL not in Rings().Fields()

assert OC7 in Rings().DedekindDomains()
assert OC7 in Rings().Commutative().KrullDimension(1)
assert OC7 not in Rings().Fields()

# --------------------------------------------------------------------
# Localizations and completions
# --------------------------------------------------------------------

Zloc2 = Localization(ZZ, (2,))
Zloc6 = Localization(ZZ, (2, 3))

assert Zloc2 in Rings()
assert Zloc2 in Rings().Commutative()
assert Zloc2 in Rings().IntegralDomains()
assert Zloc2 in Rings().NoetherianRings()
assert Zloc2 in Rings().PrincipalIdealDomains()
assert Zloc2 in Rings().Characteristic(0)
assert Zloc2 not in Rings().Fields()

assert Zloc6 in Rings()
assert Zloc6 in Rings().Commutative()
assert Zloc6 in Rings().IntegralDomains()
assert Zloc6 in Rings().NoetherianRings()
assert Zloc6 in Rings().PrincipalIdealDomains()
assert Zloc6 in Rings().Characteristic(0)
assert Zloc6 not in Rings().Fields()

Z5 = Zp(5)
Q5 = Qp(5)

assert Z5 in Rings()
assert Z5 in Rings().Commutative()
assert Z5 in Rings().Topological().Complete()
assert Z5 in Rings().WithValuation()
assert Z5 in Rings().WithValuation().DiscretelyValued()
assert Z5 in Rings().LocalRings()
assert Z5 in Rings().DVRs()
assert Z5 in Rings().Characteristic(0)
assert Z5 not in Rings().Fields()

assert Q5 in Rings()
assert Q5 in Rings().Commutative()
assert Q5 in Rings().Fields()
assert Q5 in Rings().Topological().Complete()
assert Q5 in Rings().WithValuation()
assert Q5 in Rings().WithValuation().DiscretelyValued()
assert Q5 in Rings().Fields().LocalFields()
assert Q5 in Rings().Fields().GlobalFields().NonArchimedean()
assert Q5 in Rings().Characteristic(0)

# --------------------------------------------------------------------
# Polynomial, Laurent polynomial, power series, Laurent series, Puiseux
# --------------------------------------------------------------------

R1 = PolynomialRing(QQ, 'x')
R2 = PolynomialRing(QQ, ['x', 'y'])
R3 = PolynomialRing(ZZ, 'x')
R4 = PolynomialRing(GF(5), 'x')
LP = LaurentPolynomialRing(QQ, 't')
PS = PowerSeriesRing(QQ, 't')
LS = LaurentSeriesRing(QQ, 'u')
PU = PuiseuxSeriesRing(QQ, 'v')

assert R1 in Rings()
assert R1 in Rings().Commutative()
assert R1 in Rings().IntegralDomains()
assert R1 in Rings().GcdDomains()
assert R1 in Rings().UniqueFactorizationDomains()
assert R1 in Rings().PrincipalIdealDomains()
assert R1 in Rings().EuclideanDomains()
assert R1 in Rings().NoetherianRings()
assert R1 in Rings().Characteristic(0)
assert R1 in Rings().Polynomial()

assert R2 in Rings()
assert R2 in Rings().Commutative()
assert R2 in Rings().IntegralDomains()
assert R2 in Rings().GcdDomains()
assert R2 in Rings().UniqueFactorizationDomains()
assert R2 in Rings().NoetherianRings()
assert R2 in Rings().Characteristic(0)
assert R2 in Rings().Polynomial()
assert R2 not in Rings().PrincipalIdealDomains()
assert R2 not in Rings().EuclideanDomains()

assert R3 in Rings()
assert R3 in Rings().Commutative()
assert R3 in Rings().IntegralDomains()
assert R3 in Rings().GcdDomains()
assert R3 in Rings().UniqueFactorizationDomains()
assert R3 in Rings().NoetherianRings()
assert R3 in Rings().Characteristic(0)
assert R3 in Rings().Polynomial()
assert R3 not in Rings().PrincipalIdealDomains()

assert R4 in Rings()
assert R4 in Rings().Commutative()
assert R4 in Rings().IntegralDomains()
assert R4 in Rings().GcdDomains()
assert R4 in Rings().UniqueFactorizationDomains()
assert R4 in Rings().PrincipalIdealDomains()
assert R4 in Rings().EuclideanDomains()
assert R4 in Rings().NoetherianRings()
assert R4 in Rings().Finite()
assert R4 in Rings().Characteristic(5)
assert R4 in Rings().Polynomial()

assert LP in Rings()
assert LP in Rings().Commutative()
assert LP in Rings().IntegralDomains()
assert LP in Rings().GcdDomains()
assert LP in Rings().UniqueFactorizationDomains()
assert LP in Rings().Characteristic(0)
assert LP in Rings().LaurentSeries()  # if Laurent polynomial is included in the Laurent branch
assert LP not in Rings().Fields()

assert PS in Rings()
assert PS in Rings().Commutative()
assert PS in Rings().IntegralDomains()
assert PS in Rings().LocalRings()
assert PS in Rings().Topological().Complete()
assert PS in Rings().WithValuation()
assert PS in Rings().WithValuation().DiscretelyValued()
assert PS in Rings().PrincipalIdealDomains()
assert PS in Rings().DVRs()
assert PS in Rings().Characteristic(0)
assert PS in Rings().PowerSeries()
assert PS in Rings().LaurentSeries()
assert PS in Rings().PuiseuxSeries()
assert PS not in Rings().Fields()

assert LS in Rings()
assert LS in Rings().Commutative()
assert LS in Rings().Fields()
assert LS in Rings().Topological().Complete()
assert LS in Rings().WithValuation()
assert LS in Rings().WithValuation().DiscretelyValued()
assert LS in Rings().Characteristic(0)
assert LS in Rings().LaurentSeries()
assert LS in Rings().PuiseuxSeries()

assert PU in Rings()
assert PU in Rings().Commutative()
assert PU in Rings().Fields()
assert PU in Rings().Characteristic(0)
assert PU in Rings().PuiseuxSeries()

# --------------------------------------------------------------------
# Fraction fields, quotients, function fields
# --------------------------------------------------------------------

Frac_Zx = FractionField(ZZ['x'])
Frac_Qxy = FractionField(QQ['x', 'y'])
FF = FunctionField(QQ, 't')

assert Frac_Zx in Rings()
assert Frac_Zx in Rings().Commutative()
assert Frac_Zx in Rings().Fields()
assert Frac_Zx in Rings().QuotientFields()
assert Frac_Zx in Rings().Characteristic(0)

assert Frac_Qxy in Rings()
assert Frac_Qxy in Rings().Commutative()
assert Frac_Qxy in Rings().Fields()
assert Frac_Qxy in Rings().QuotientFields()
assert Frac_Qxy in Rings().Characteristic(0)

assert FF in Rings()
assert FF in Rings().Commutative()
assert FF in Rings().Fields()
assert FF in Rings().QuotientFields()
assert FF in Rings().Characteristic(0)
assert FF not in Rings().NumberFields()

Qx = QQ['x']
x = Qx.gen()
Kmod = Qx.quotient(x^2 + 1, 'i')

assert Kmod in Rings()
assert Kmod in Rings().Commutative()
assert Kmod in Rings().Fields()
assert Kmod in Rings().NumberFields()
assert Kmod in Rings().GlobalFields()
assert Kmod in Rings().Characteristic(0)

F5x = GF(5)['x']
x = F5x.gen()
F25_alt = F5x.quotient(x^2 + 2, 'a')

assert F25_alt in Rings()
assert F25_alt in Rings().Commutative()
assert F25_alt in Rings().Finite()
assert F25_alt in Rings().Fields()
assert F25_alt in Rings().FiniteFields()
assert F25_alt in Rings().Characteristic(5)

# --------------------------------------------------------------------
# Products and square matrix rings
# --------------------------------------------------------------------

P1 = cartesian_product([ZZ, QQ])
P2 = cartesian_product([GF(2), GF(3)])
M2Q = MatrixSpace(QQ, 2)
M23Q = MatrixSpace(QQ, 2, 3)

assert P1 in Rings()
assert P1 in Rings().Commutative()
assert P1 in Rings().Characteristic(0)
assert P1 not in Rings().IntegralDomains()
assert P1 not in Rings().Fields()

assert P2 in Rings()
assert P2 in Rings().Commutative()
assert P2 in Rings().Finite()
assert P2 in Rings().Characteristic(6)
assert P2 not in Rings().IntegralDomains()
assert P2 not in Rings().Fields()

assert M2Q in Rings()
assert M2Q in Rings().Characteristic(0)
assert M2Q not in Rings().Commutative()
assert M2Q not in Rings().IntegralDomains()
assert M2Q not in Rings().Fields()

assert M23Q in Modules(QQ)
assert M23Q in Modules(QQ).FiniteDimensional()

# --------------------------------------------------------------------
# Ideals and quotients of rings
# --------------------------------------------------------------------

I6 = ZZ.ideal(6)
Ixy = QQ['x', 'y'].ideal(['x^2', 'x*y'])
I2 = QQ['x'].ideal('x^2 + 1')

assert I6 in RingIdeals(ZZ)
assert Ixy in RingIdeals(QQ['x', 'y'])
assert I2 in RingIdeals(QQ['x'])

Rquot = QQ['x', 'y'].quotient(QQ['x', 'y'].ideal('x'))
assert Rquot in Rings()
assert Rquot in Rings().Commutative()
assert Rquot in Rings().NoetherianRings()
assert Rquot in Rings().Characteristic(0)

# --------------------------------------------------------------------
# Free modules, vector spaces, submodules, quotients, kernels, cokernels
# --------------------------------------------------------------------

MZ = ZZ^3
VQ = QQ^3
CFM = CombinatorialFreeModule(QQ, ['a', 'b', 'c'])

assert MZ in Modules(ZZ)
assert MZ in Modules(ZZ).FinitelyPresented()

assert VQ in Modules(QQ)
assert VQ in Modules(QQ).FiniteDimensional()
assert VQ in Modules(QQ).FinitelyPresented()

assert CFM in Modules(QQ)

SZ = MZ.submodule([[1, 0, 0], [0, 2, 0]])
QZ = MZ.quotient(SZ)

assert SZ in Modules(ZZ)
assert SZ in Modules(ZZ).Subobjects()

assert QZ in Modules(ZZ)
assert QZ in Modules(ZZ).Quotients()

A = matrix(ZZ, [[1, 2, 3], [0, 1, 1]])
K = A.right_kernel()
C = A.column_module()
Cok = (ZZ^2).quotient(C)

assert K in Modules(ZZ)
assert K in Modules(ZZ).Subobjects()

assert C in Modules(ZZ)
assert C in Modules(ZZ).Subobjects()

assert Cok in Modules(ZZ)
assert Cok in Modules(ZZ).Quotients()

B = matrix(QQ, [[1, 2], [0, 0]])
KQ = B.right_kernel()
CQ = B.column_module()
CokQ = (QQ^2).quotient(CQ)

assert KQ in Modules(QQ)
assert KQ in Modules(QQ).Subobjects()
assert KQ in Modules(QQ).FiniteDimensional()

assert CQ in Modules(QQ)
assert CQ in Modules(QQ).Subobjects()
assert CQ in Modules(QQ).FiniteDimensional()

assert CokQ in Modules(QQ)
assert CokQ in Modules(QQ).Quotients()
assert CokQ in Modules(QQ).FiniteDimensional()

DS = (ZZ^2).direct_sum(ZZ^3)
assert DS in Modules(ZZ)
assert DS in Modules(ZZ).FinitelyPresented()

# --------------------------------------------------------------------
# Tensor / free / exterior / group / symmetric-function algebras
# --------------------------------------------------------------------

CFM2 = CombinatorialFreeModule(QQ, ['u', 'v'])
TA = TensorAlgebra(CFM2)
FA = FreeAlgebra(QQ, 2, names=('x', 'y'))
EA = ExteriorAlgebra(QQ, names=('e0', 'e1', 'e2'))
GA = GroupAlgebra(SymmetricGroup(3), QQ)
SF = SymmetricFunctions(QQ)

assert TA in Rings()
assert TA not in Rings().Commutative()

assert FA in Rings()
assert FA not in Rings().Commutative()

assert EA in Rings()
assert EA in Rings().Characteristic(0)

assert GA in Rings()
assert GA in Rings().Characteristic(0)

assert SF in Rings()
assert SF in Rings().Commutative()
assert SF in Rings().Characteristic(0)

# --------------------------------------------------------------------
# Slice / coslice style checks for the proposed ObjectsUnder / ObjectsOver
# --------------------------------------------------------------------

assert QQ['x'] in Rings().ObjectsUnder(QQ)
assert QQ['x'].fraction_field() in Rings().ObjectsUnder(QQ)
assert PowerSeriesRing(QQ, 't') in Rings().ObjectsUnder(QQ)
assert LaurentSeriesRing(QQ, 't') in Rings().ObjectsUnder(QQ)
assert PuiseuxSeriesRing(QQ, 't') in Rings().ObjectsUnder(QQ)

assert ZZ in Rings().ObjectsOver(QQ) is False
assert ZZ in Rings().ObjectsUnder(ZZ)
assert K.ring_of_integers() in Rings().ObjectsOver(K)
assert Zp(5) in Rings().ObjectsUnder(ZZ)
assert Qp(5) in Rings().ObjectsUnder(QQ)

# --------------------------------------------------------------------
# Explicit collapse / workflow checks across multiple category paths
# --------------------------------------------------------------------

assert ZZ in Rings().EuclideanDomains()
assert ZZ in Rings().Commutative().IntegralDomains().EuclideanDomains()

assert QQ in Rings().NumberFields()
assert QQ in Rings().Fields().NumberFields()

assert GF(5) in Rings().FiniteFields()
assert GF(5) in Rings().Fields().Finite()
assert GF(5) in Rings().Finite().Fields()

assert Qp(5) in Rings().Fields().LocalFields()
assert Qp(5) in Rings().Fields().GlobalFields().NonArchimedean()

assert RR in Rings().Fields().LocalFields()
assert RR in Rings().Fields().GlobalFields().Archimedean()

assert LaurentSeriesRing(QQ, 'u') in Rings().Fields().WithValuation().DiscretelyValued()
assert PowerSeriesRing(QQ, 'u') in Rings().WithValuation().DiscretelyValued()

assert QQ['x'] in Rings().Polynomial()
assert LaurentPolynomialRing(QQ, 'u') in Rings().LaurentSeries()
assert PowerSeriesRing(QQ, 'u') in Rings().PowerSeries()
assert PowerSeriesRing(QQ, 'u') in Rings().LaurentSeries()
assert PowerSeriesRing(QQ, 'u') in Rings().PuiseuxSeries()
