from sage.all import *

# ============================================================
# I. CATEGORY-STRUCTURE TESTS
# ============================================================
#
# These assert only:
#   - canonical named categories are the chained subcategories they represent
#   - the mathematical containment hierarchy is correct
#   - standard singleton categories sit in the right places
#
# Assume:
#   A <= B   means   A.is_subcategory_of(B)
# and equality of categories is literal object equality of the canonical category.
# ============================================================

# --- top-level named categories are the canonical chained subcategories they denote

assert Rings().CommutativeRings() == Rings().Commutative()
assert Rings().DivisionRings() == Rings().Division()
assert Rings().FiniteRings() == Rings().Finite()
assert Rings().TopologicalRings() == Rings().Topological()
assert Rings().ValuedRings() == Rings().WithValuation()

assert Rings().Fields() == Rings().Commutative().Fields()
assert Rings().IntegralDomains() == Rings().Commutative().IntegralDomains()
assert Rings().NoetherianRings() == Rings().Commutative().Noetherian()
assert Rings().LocalRings() == Rings().Commutative().Local()

assert Rings().GcdDomains() == Rings().IntegralDomains().Gcd()
assert Rings().UniqueFactorizationDomains() == Rings().IntegralDomains().UniqueFactorization()
assert Rings().PrincipalIdealDomains() == Rings().IntegralDomains().PrincipalIdeal()
assert Rings().EuclideanDomains() == Rings().IntegralDomains().Euclidean()
assert Rings().IntegrallyClosedDomains() == Rings().IntegralDomains().IntegrallyClosed()
assert Rings().DedekindDomains() == Rings().IntegralDomains().Dedekind()

assert Rings().FiniteFields() == Rings().Fields().Finite()
assert Rings().NumberFields() == Rings().Fields().NumberFields()
assert Rings().AlgebraicallyClosedFields() == Rings().Fields().AlgebraicallyClosed()
assert Rings().LocalFields() == Rings().Fields().LocalFields()
assert Rings().GlobalFields() == Rings().Fields().GlobalFields()
assert Rings().RealFields() == Rings().Fields().Real()
assert Rings().ComplexFields() == Rings().Fields().Complex()

assert Rings().ArchimedeanGlobalFields() == Rings().GlobalFields().Archimedean()
assert Rings().NonArchimedeanGlobalFields() == Rings().GlobalFields().NonArchimedean()

assert Rings().DiscretelyValuedRings() == Rings().ValuedRings().DiscretelyValued()
assert Rings().CompleteRings() == Rings().TopologicalRings().Complete()

# --- core mathematical containment hierarchy

assert Rings().Fields() <= Rings().CommutativeRings()
assert Rings().Fields() <= Rings().DivisionRings()
assert Rings().Fields() <= Rings().EuclideanDomains()
assert Rings().Fields() <= Rings().NoetherianRings()

assert Rings().IntegralDomains() <= Rings().CommutativeRings()

assert Rings().GcdDomains() <= Rings().IntegralDomains()
assert Rings().UniqueFactorizationDomains() <= Rings().GcdDomains()
assert Rings().PrincipalIdealDomains() <= Rings().UniqueFactorizationDomains()
assert Rings().EuclideanDomains() <= Rings().PrincipalIdealDomains()

assert Rings().DedekindDomains() <= Rings().IntegrallyClosedDomains()
assert Rings().DedekindDomains() <= Rings().NoetherianRings()
assert Rings().DedekindDomains() <= Rings().IntegralDomains()

assert Rings().FiniteFields() <= Rings().Fields()
assert Rings().NumberFields() <= Rings().Fields()
assert Rings().AlgebraicallyClosedFields() <= Rings().Fields()
assert Rings().LocalFields() <= Rings().Fields()
assert Rings().GlobalFields() <= Rings().Fields()

assert Rings().ArchimedeanGlobalFields() <= Rings().GlobalFields()
assert Rings().NonArchimedeanGlobalFields() <= Rings().GlobalFields()

assert Rings().DiscretelyValuedRings() <= Rings().ValuedRings()
assert Rings().CompleteRings() <= Rings().TopologicalRings()

# DVRs / local complete valued structure
assert Rings().DVRs() <= Rings().PrincipalIdealDomains()
assert Rings().DVRs() <= Rings().LocalRings()
assert Rings().DVRs() <= Rings().DiscretelyValuedRings()

# local fields are complete topological discretely valued fields
assert Rings().LocalFields() <= Rings().Fields()
assert Rings().LocalFields() <= Rings().TopologicalRings()
assert Rings().LocalFields() <= Rings().CompleteRings()
assert Rings().LocalFields() <= Rings().DiscretelyValuedRings()

# --- construction families: actual hierarchy, not flat naming

assert Rings().PolynomialRingsOver(ZZ) <= Rings().ObjectsUnder(ZZ)

assert Rings().PowerSeriesRingsOver(QQ) <= Rings().LaurentSeriesRingsOver(QQ)
assert Rings().LaurentSeriesRingsOver(QQ) <= Rings().PuiseuxSeriesRingsOver(QQ)

assert Rings().QuotientsOf(QQ['x']) <= Rings().ObjectsUnder(QQ['x'])
assert Rings().SubringsOf(QQ) <= Rings().ObjectsOver(QQ)

# --- named singleton categories live in the hierarchy

assert Rings().ZZ() <= Rings().EuclideanDomains()
assert Rings().ZZ() <= Rings().DedekindDomains()
assert Rings().ZZ() <= Rings().Characteristic(0)

assert Rings().QQ() <= Rings().NumberFields()
assert Rings().QQ() <= Rings().GlobalFields()
assert Rings().QQ() <= Rings().Characteristic(0)

assert Rings().QQbar() <= Rings().AlgebraicallyClosedFields()
assert Rings().QQbar() <= Rings().Characteristic(0)

assert Rings().Zp(5) <= Rings().DVRs()
assert Rings().Zp(5) <= Rings().CompleteRings()
assert Rings().Zp(5) <= Rings().ValuedRings()

assert Rings().Qp(5) <= Rings().LocalFields()
assert Rings().Qp(5) <= Rings().Fields()
assert Rings().Qp(5) <= Rings().CompleteRings()
assert Rings().Qp(5) <= Rings().ValuedRings()

assert Rings().RR() <= Rings().RealFields()
assert Rings().RR() <= Rings().Fields()
assert Rings().RR() <= Rings().CompleteRings()

assert Rings().CC() <= Rings().ComplexFields()
assert Rings().CC() <= Rings().Fields()
assert Rings().CC() <= Rings().CompleteRings()

assert Rings().SR() <= Rings()
assert Rings().SR() <= Rings().CommutativeRings()
assert not (Rings().SR() <= Rings().Fields())


# ============================================================
# II. INSTANCE TESTS
# ============================================================
#
# Each example is meant to witness a mathematically meaningful statement.
# No repeated "R in Rings(); R in Commutative(); ..." inflation.
# Instead: put R into the smallest/strongest interesting categories.
# ============================================================

# --- basic singleton rings and fields

assert ZZ in Rings().EuclideanDomains()
assert ZZ in Rings().DedekindDomains()
assert ZZ in Rings().ObjectsOver(QQ)          # ZZ -> QQ

assert QQ in Rings().NumberFields()
assert QQ in Rings().GlobalFields()
assert QQ in Rings().ObjectsUnder(ZZ)         # ZZ -> QQ

assert QQbar in Rings().AlgebraicallyClosedFields()
assert QQbar not in Rings().NumberFields()

assert RR in Rings().RealFields()
assert RR in Rings().CompleteRings()

assert CC in Rings().ComplexFields()
assert CC in Rings().AlgebraicallyClosedFields()
assert CC in Rings().CompleteRings()

assert SR in Rings().CommutativeRings()
assert SR not in Rings().Fields()

# --- finite quotients: prime quotient is a field, non-prime quotient is not

Fp = ZZ.quotient(3 * ZZ)
Z6 = ZZ.quotient(6 * ZZ)

assert Fp in Rings().FiniteFields()
assert Fp in Rings().Characteristic(3)
assert Fp in Rings().ObjectsUnder(ZZ)

assert Z6 in Rings().FiniteRings()
assert Z6 in Rings().Characteristic(6)
assert Z6 not in Rings().Fields()

# --- finite field constructors

F9 = GF(9)
assert F9 in Rings().FiniteFields()
assert F9 in Rings().Characteristic(3)
assert F9 in Rings().ObjectsUnder(ZZ)

# --- number fields and rings of integers

x = polygen(QQ, 'x')

K = QuadraticField(-5, 'a')
OK = K.ring_of_integers()

assert K in Rings().NumberFields()
assert K in Rings().GlobalFields()
assert K in Rings().ObjectsUnder(QQ)

# O_{Q(sqrt(-5))} is Dedekind but not PID
assert OK in Rings().DedekindDomains()
assert OK not in Rings().PrincipalIdealDomains()
assert OK in Rings().ObjectsOver(K)

C7 = CyclotomicField(7)
OC7 = C7.ring_of_integers()

assert C7 in Rings().CyclotomicFields()
assert C7 in Rings().GlobalFields()
assert OC7 in Rings().DedekindDomains()
assert OC7 in Rings().ObjectsOver(C7)

# --- p-adics

Z5 = Zp(5)
Q5 = Qp(5)

assert Z5 in Rings().DVRs()
assert Z5 in Rings().CompleteRings()
assert Z5 in Rings().ValuedRings().DiscretelyValued()
assert Z5 in Rings().ObjectsOver(Q5)          # Z5 -> Q5
assert Z5 in Rings().ObjectsUnder(ZZ)         # ZZ -> Z5

assert Q5 in Rings().LocalFields()
assert Q5 in Rings().CompleteRings()
assert Q5 in Rings().ValuedRings().DiscretelyValued()
assert Q5 in Rings().ObjectsUnder(QQ)         # QQ -> Q5
assert Q5 in Rings().ObjectsUnder(ZZ)         # ZZ -> Q5

# --- polynomial rings: univariate over a field is Euclidean; multivariate is not

Qx = PolynomialRing(QQ, 'x')
Qxy = PolynomialRing(QQ, ['x', 'y'])
Zx = PolynomialRing(ZZ, 'x')

assert Qx in Rings().EuclideanDomains()
assert Qx in Rings().PolynomialRingsOver(QQ)

assert Qxy in Rings().UniqueFactorizationDomains()
assert Qxy in Rings().PolynomialRingsOver(QQ)
assert Qxy not in Rings().PrincipalIdealDomains()

assert Zx in Rings().UniqueFactorizationDomains()
assert Zx in Rings().PolynomialRingsOver(ZZ)
assert Zx not in Rings().PrincipalIdealDomains()

# --- power / Laurent / Puiseux series: actual hierarchy

PS = PowerSeriesRing(QQ, 't')
LS = LaurentSeriesRing(QQ, 't')
PU = PuiseuxSeriesRing(QQ, 't')

# QQ[[t]] is a complete DVR
assert PS in Rings().DVRs()
assert PS in Rings().CompleteRings()
assert PS in Rings().ValuedRings().DiscretelyValued()
assert PS in Rings().PowerSeriesRingsOver(QQ)
assert PS in Rings().LaurentSeriesRingsOver(QQ)
assert PS in Rings().PuiseuxSeriesRingsOver(QQ)

# QQ((t)) is a complete discretely valued field
assert LS in Rings().Fields().WithValuation().DiscretelyValued()
assert LS in Rings().CompleteRings()
assert LS in Rings().LaurentSeriesRingsOver(QQ)
assert LS in Rings().PuiseuxSeriesRingsOver(QQ)

# Puiseux series over QQ form a field, and lie in the top family
assert PU in Rings().Fields()
assert PU in Rings().PuiseuxSeriesRingsOver(QQ)

# --- fraction fields and quotient fields

Frac_Zx = FractionField(Zx)
Frac_Qxy = FractionField(Qxy)

assert Frac_Zx in Rings().Fields().Quotients()
assert Frac_Zx in Rings().ObjectsUnder(Zx)

assert Frac_Qxy in Rings().Fields().Quotients()
assert Frac_Qxy in Rings().ObjectsUnder(Qxy)

# --- quotient field obtained as an actual quotient construction on a PID/UFD input
#     (use a field quotient, not a new axiom)

F25_alt = GF(5)['u'].quotient('u^2 + 2')
assert F25_alt in Rings().FiniteFields()

# --- products: finite product of fields is finite commutative ring but not a field/domain

P = cartesian_product([GF(2), GF(3)])
assert P in Rings().FiniteRings()
assert P in Rings().CommutativeRings()
assert P not in Rings().Fields()
assert P not in Rings().IntegralDomains()

# --- matrix rings: genuine rings, generally noncommutative

M2Q = MatrixSpace(QQ, 2)
assert M2Q in Rings()
assert not (M2Q in Rings().CommutativeRings())
assert not (M2Q in Rings().IntegralDomains())
assert not (M2Q in Rings().Fields())

# --- ideals as submodules; quotients/kernels/cokernels as module-theoretic tests

I = ZZ.ideal(6)
assert I in Modules(ZZ).Subobjects()

M = ZZ^2
N = M.submodule([(2, 0), (0, 3)])
Q = M.quotient(N)

assert N in Modules(ZZ).Subobjects()
assert Q in Modules(ZZ).Quotients()

A = matrix(ZZ, [[2, 4], [0, 6]])
K = A.right_kernel()
C = A.column_module()
Cok = (ZZ^2).quotient(C)

assert K in Modules(ZZ).Subobjects()
assert C in Modules(ZZ).Subobjects()
assert Cok in Modules(ZZ).Quotients()

# In a PID, finitely generated ideals are free rank-1 modules:
# use this only if your new module hierarchy has the corresponding named category.
# assert I in Modules(ZZ).FreeModules().FiniteRank(1)

# --- under / over workflow checks

assert QQ['x'] in Rings().ObjectsUnder(QQ)
assert QQ['x'] in Rings().ObjectsUnder(ZZ)
assert GF(5) in Rings().ObjectsUnder(ZZ)
assert OK in Rings().ObjectsOver(K)
assert ZZ in Rings().ObjectsOver(QQ)
assert Z5 in Rings().ObjectsOver(Q5)
