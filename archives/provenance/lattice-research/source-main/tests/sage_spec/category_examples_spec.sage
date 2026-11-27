from sage.all import *

# ============================================================
# 0. STANDARD BASE EXAMPLES
# ============================================================

# ZZ is the basic Euclidean/PID/UFD/Dedekind example of dimension 1.
assert ZZ in Rings().EuclideanDomains()
assert ZZ in Rings().DedekindDomains()
assert ZZ.krull_dimension() == 1
assert ZZ.class_number() == 1
assert not ZZ.is_field()
assert not ZZ.is_local()
assert not ZZ.is_artinian()

# QQ is the basic global field / number field / characteristic-0 field.
assert QQ in Rings().Fields().NumberFields()
assert QQ in Rings().Fields().GlobalFields()
assert QQ.characteristic() == 0

# QQbar is algebraically closed but not a number field.
assert QQbar in Rings().Fields().AlgebraicallyClosedFields()
assert QQbar.characteristic() == 0
assert QQbar not in Rings().Fields().NumberFields()

# RR and CC are local archimedean fields in the standard sense.
assert RR in Rings().Fields().LocalFields()
assert RR in Rings().Fields().RealFields()
assert RR.is_complete()

assert CC in Rings().Fields().LocalFields()
assert CC in Rings().Fields().ComplexFields()
assert CC in Rings().Fields().AlgebraicallyClosedFields()
assert CC.is_complete()


# ============================================================
# 1. STANDARD NUMBER-THEORETIC EXAMPLES
# ============================================================

# Gaussian integers: Euclidean, hence PID, hence UFD, hence Dedekind, class number 1.
Ki = QuadraticField(-1, 'i')
Oi = Ki.ring_of_integers()
assert Oi in Rings().EuclideanDomains()
assert Oi in Rings().DedekindDomains()
assert Oi.class_number() == 1

# Eisenstein integers: also Euclidean, class number 1.
Kw = QuadraticField(-3, 'w')
Ow = Kw.ring_of_integers()
assert Ow in Rings().EuclideanDomains()
assert Ow in Rings().DedekindDomains()
assert Ow.class_number() == 1

# O_{Q(sqrt(-5))}: standard Dedekind-not-PID, class number 2 example.
K5 = QuadraticField(-5, 'a')
O5 = K5.ring_of_integers()
assert O5 in Rings().DedekindDomains()
assert O5.krull_dimension() == 1
assert O5.class_number() == 2
assert O5 not in Rings().PrincipalIdealDomains()
assert O5 not in Rings().UniqueFactorizationDomains()

# Cyclotomic fields are number fields and global fields.
C7 = CyclotomicField(7)
assert C7 in Rings().Fields().NumberFields()
assert C7 in Rings().Fields().GlobalFields()
assert C7.ring_of_integers() in Rings().DedekindDomains()


# ============================================================
# 2. FINITE QUOTIENTS, ARTINIANITY, REDUCEDNESS
# ============================================================

# Prime quotient of ZZ is a field.
F3 = ZZ.quotient(3 * ZZ)
assert F3 in Rings().FiniteFields()
assert F3.characteristic() == 3

# Composite quotient need not be reduced or a field.
Z4 = ZZ.quotient(4 * ZZ)
assert Z4 in Rings().FiniteRings()
assert Z4.is_artinian()
assert not Z4.is_reduced()
assert not Z4.is_field()

# Squarefree finite quotient is reduced Artinian but not a field.
Z6 = ZZ.quotient(6 * ZZ)
assert Z6 in Rings().FiniteRings()
assert Z6.is_artinian()
assert Z6.is_reduced()
assert not Z6.is_field()

# CRT on integers.
assert ZZ.quotient(6 * ZZ) == cartesian_product([ZZ.quotient(2 * ZZ), ZZ.quotient(3 * ZZ)])
assert ZZ.quotient(12 * ZZ) == cartesian_product([ZZ.quotient(3 * ZZ), ZZ.quotient(4 * ZZ)])


# ============================================================
# 3. POLYNOMIAL RINGS: STANDARD THEOREMS
# ============================================================

x = polygen(QQ, 'x')
R1 = PolynomialRing(QQ, 'x')
R2 = PolynomialRing(QQ, ['x', 'y'])
R3 = PolynomialRing(ZZ, 'x')
R4 = PolynomialRing(ZZ, ['x', 'y'])

# k[x] over a field k is Euclidean by degree.
assert R1 in Rings().EuclideanDomains()
assert R1.krull_dimension() == 1

# k[x,y] is a UFD but not a PID; dimension 2.
assert R2 in Rings().UniqueFactorizationDomains()
assert R2.krull_dimension() == 2
assert R2 not in Rings().PrincipalIdealDomains()

# If R is a UFD, then R[x] is a UFD: test on R = ZZ.
assert R3 in Rings().UniqueFactorizationDomains()
assert R3.krull_dimension() == 2
assert R3 not in Rings().PrincipalIdealDomains()

# Hilbert basis theorem: if R is Noetherian, then R[x] is Noetherian.
assert R4.is_noetherian()
assert R4.krull_dimension() == 3

# Height computations in polynomial rings over fields.
S = PolynomialRing(QQ, ['x', 'y', 'z'])
x, y, z = S.gens()
assert S.ideal(x).height() == 1
assert S.ideal(x, y).height() == 2
assert S.ideal(x, y, z).height() == 3


# ============================================================
# 4. LOCALIZATION AND FRACTION FIELDS
# ============================================================

# Localization of a domain at all nonzero elements is its fraction field.
FracZ = FractionField(ZZ)
LocZ = LocalizationAtMultiplicativeSet(ZZ, ZZ - {0})
assert LocZ == FracZ
assert FracZ in Rings().Fields()

# Localization of a PID at a nonzero prime is a DVR.
Zloc3 = LocalizationAtPrime(ZZ, 3)
assert Zloc3 in Rings().DVRs()
assert Zloc3.krull_dimension() == 1
assert Zloc3.is_local()
assert Zloc3.maximal_ideal().height() == 1

# Localization of a Dedekind domain at a nonzero prime is a DVR.
p = O5.prime_above(2)
O5p = LocalizationAtPrime(O5, p)
assert O5p in Rings().DVRs()
assert O5p.is_local()
assert O5p.krull_dimension() == 1

# Localization preserves UFD in standard examples.
R = LocalizationAtPrime(PolynomialRing(ZZ, 'x'), 2)
assert R in Rings().UniqueFactorizationDomains()

# Localizing k[x,y] at (x,y) gives a 2-dimensional regular local ring.
A = LocalizationAtMaximalIdeal(PolynomialRing(QQ, ['x', 'y']), ('x', 'y'))
assert A.is_local()
assert A.krull_dimension() == 2
assert A.depth() == 2
assert A.is_regular_local()


# ============================================================
# 5. COMPLETIONS
# ============================================================

# Completion of ZZ_(p) at p is Z_p.
Zloc5 = LocalizationAtPrime(ZZ, 5)
Z5hat = CompleteAtIdeal(Zloc5, Zloc5.maximal_ideal())
assert Z5hat == Zp(5)
assert Z5hat in Rings().DVRs()
assert Z5hat.is_complete()

# Completion of k[x]_(x) at (x) is k[[x]].
A = LocalizationAtMaximalIdeal(PolynomialRing(QQ, 'x'), ('x',))
Ahat = CompleteAtIdeal(A, A.maximal_ideal())
assert Ahat == PowerSeriesRing(QQ, 'x')
assert Ahat in Rings().DVRs()

# k[[x,y]] is complete, local, Noetherian, regular, dimension 2.
PS2 = PowerSeriesRing(QQ, ['x', 'y'])
assert PS2.is_complete()
assert PS2.is_local()
assert PS2.is_noetherian()
assert PS2.krull_dimension() == 2
assert PS2.depth() == 2
assert PS2.is_regular_local()


# ============================================================
# 6. LAURENT / PUISEUX / VALUATION EXAMPLES
# ============================================================

# k[[t]] is a complete DVR.
PS = PowerSeriesRing(GF(5), 't')
assert PS in Rings().DVRs()
assert PS.is_complete()
assert PS.residue_field() == GF(5)

# k((t)) is a complete discretely valued field; if k is finite, it is a local field.
LS = LaurentSeriesRing(GF(5), 't')
assert LS in Rings().Fields().WithValuation().DiscretelyValued()
assert LS.is_complete()
assert LS.residue_field() == GF(5)
assert LS in Rings().Fields().LocalFields()

# Power series ⊂ Laurent series ⊂ Puiseux series, tested on actual instances.
PU = PuiseuxSeriesRing(GF(5), 't')
assert PS in Rings().PowerSeries()
assert PS in Rings().LaurentSeries()
assert PS in Rings().PuiseuxSeries()
assert LS in Rings().LaurentSeries()
assert LS in Rings().PuiseuxSeries()
assert PU in Rings().PuiseuxSeries()

# Q_p is a complete discretely valued local field.
Q5 = Qp(5)
assert Q5 in Rings().Fields().LocalFields()
assert Q5 in Rings().Fields().WithValuation().DiscretelyValued()
assert Q5.is_complete()
assert Q5.residue_field() == GF(5)


# ============================================================
# 7. REDUCED / IRREDUCIBLE / DOMAIN / REGULAR / DEPTH
# ============================================================

# k[x]/(x^2): local Artinian, nonreduced, irreducible, depth 0, not regular.
A = QQ['x'].quotient('x^2')
assert A.is_local()
assert A.is_artinian()
assert not A.is_reduced()
assert A.is_irreducible()
assert A.krull_dimension() == 0
assert A.depth() == 0
assert not A.is_regular_local()

# k[x,y]/(xy): reduced, not irreducible, not a domain, dimension 1.
B = QQ['x', 'y'].quotient('x*y')
assert B.is_reduced()
assert not B.is_irreducible()
assert not B in Rings().IntegralDomains()
assert B.krull_dimension() == 1

# Localize the node at the origin: 1-dimensional Cohen–Macaulay but not regular.
Bm = LocalizationAtMaximalIdeal(B, ('x', 'y'))
assert Bm.krull_dimension() == 1
assert Bm.depth() == 1
assert not Bm.is_regular_local()

# Regular local test case: k[x,y]_(x,y)
C = LocalizationAtMaximalIdeal(QQ['x', 'y'], ('x', 'y'))
assert C.krull_dimension() == 2
assert C.depth() == 2
assert C.is_regular_local()

# Non-Noetherian standard example.
Inf = InfinitePolynomialRing(QQ, 'x')
assert not Inf.is_noetherian()
assert not Inf.is_artinian()


# ============================================================
# 8. DIRECT PRODUCTS AND CHINESE REMAINDER
# ============================================================

# Product of reduced rings is reduced; product of domains need not be a domain.
P = cartesian_product([QQ, GF(5)])
assert P.is_reduced()
assert not (P in Rings().IntegralDomains())
assert P.is_artinian()
assert P.krull_dimension() == 0

# Product dimensions are max of component dimensions.
Q = cartesian_product([ZZ, QQ['x']])
assert Q.krull_dimension() == 1
assert Q.is_noetherian()
assert not Q.is_artinian()

# CRT in polynomial rings.
R = QQ['x']
x = R.gen()
CRT_ring = R.quotient((x * (x - 1)))
assert CRT_ring == cartesian_product([R.quotient(x), R.quotient(x - 1)])


# ============================================================
# 9. IDEALS AS MODULES; KERNELS AND COKERNELS
# ============================================================

# In a PID, every nonzero ideal is a free rank-1 module.
I = ZZ.ideal(6, 10)
assert I == ZZ.ideal(2)
assert I in Modules(ZZ).Subobjects()
assert I in Modules(ZZ).FreeModules().FiniteRank(1)

# In k[x,y], the maximal ideal (x,y) is not principal, hence not free rank 1 as an ideal module.
R = QQ['x', 'y']
x, y = R.gens()
m = R.ideal(x, y)
assert m in Modules(R).Subobjects()
assert not m.is_principal()

# Multiplication by 6 on ZZ has kernel 0 and cokernel ZZ/6.
f = module_morphism(ZZ, ZZ, lambda n: 6*n)
assert f.kernel().is_zero()
assert f.cokernel() == ZZ.quotient(6 * ZZ)

# Multiplication by x on k[x]/(x^2) is neither injective nor surjective.
A = QQ['x'].quotient('x^2')
xbar = A.gen()
mx = module_morphism(A, A, lambda a: xbar * a)
assert not mx.kernel().is_zero()
assert not mx.cokernel().is_zero()

# In a DVR, the maximal ideal is principal and the residue ring is a field.
R = Zp(5)
m = R.maximal_ideal()
assert m.is_principal()
assert R.quotient(m) in Rings().FiniteFields()


# ============================================================
# 10. MAPS: HOMOMORPHISMS VS NON-HOMOMORPHISMS
# ============================================================

# Evaluation at a point is a ring morphism.
R = QQ['x']
ev0 = ring_morphism(R, QQ, lambda f: f(0))
assert ev0.is_ring_morphism()

# Derivative is not a ring morphism.
d = additive_map(R, R, lambda f: f.derivative())
assert not d.is_ring_morphism()

# Frobenius is a ring morphism in characteristic p.
S = GF(5)['x']
Frob = ring_endomorphism(S, lambda f: f^5)
assert Frob.is_ring_morphism()

# The same formula is not a ring morphism in characteristic 0.
T = QQ['x']
bad_frob = map(T, T, lambda f: f^5)
assert not bad_frob.is_ring_morphism()

# n -> 2n on ZZ is additive but not a unital ring morphism.
double = map(ZZ, ZZ, lambda n: 2*n)
assert not double.is_ring_morphism()


# ============================================================
# 11. FURTHER STANDARD COMMUTATIVE-ALGEBRA EXAMPLES
# ============================================================

# A field is Artinian, Noetherian, reduced, and dimension 0.
assert QQ.is_artinian()
assert QQ.is_noetherian()
assert QQ.is_reduced()
assert QQ.krull_dimension() == 0

# Z[x] is not Dedekind because it has dimension 2.
assert ZZ['x'].krull_dimension() == 2
assert ZZ['x'] not in Rings().DedekindDomains()

# Finitely generated algebras over fields need not be fields:
A = QQ['x', 'y'].quotient('y^2 - x^3')
assert A.is_noetherian()
assert A.krull_dimension() == 1
assert A not in Rings().Fields()

# Height-one primes in a UFD are principal: test in ZZ[x].
R = ZZ['x']
x = R.gen()
P = R.ideal(x)
assert P.height() == 1
assert P.is_principal()

# Dedekind + class number 1 implies PID: test positive case.
assert Oi.class_number() == 1
assert Oi in Rings().PrincipalIdealDomains()

# Dedekind + class number > 1 implies not PID: test negative case.
assert O5.class_number() == 2
assert O5 not in Rings().PrincipalIdealDomains()
