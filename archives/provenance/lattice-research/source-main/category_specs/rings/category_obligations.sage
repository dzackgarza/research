from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.rings import Rings, _RingIdealParentMethods
from category_specs.rings.homsets import RingEndCategory, RingHomCategory
from category_specs.rings.matrix_algebras import _MatrixAlgebras
from category_specs.rings.subcategories.algebraically_closed_field import _AlgebraicallyClosedFields
from category_specs.rings.subcategories.approximate import ApproximateRingsCategory
from category_specs.rings.subcategories.archimedean_global_field import _ArchimedeanGlobalFields
from category_specs.rings.subcategories.commutative import _CommutativeRings
from category_specs.rings.subcategories.complex_precision_field import _ComplexPrecisionFields
from category_specs.rings.subcategories.field import _Fields
from category_specs.rings.subcategories.integral_domain import _IntegralDomains
from category_specs.rings.subcategories.nonarchimedean_global_field import _NonArchimedeanGlobalFields
from category_specs.rings.subcategories.number_field import _NumberFields
from category_specs.rings.subcategories.p_adic_ring import _PAdicRings
from category_specs.rings.subcategories.rational_field import _QQ
from category_specs.rings.subcategories.real_precision_field import _RealPrecisionFields
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_category_statements


NR = Rings().Constructors()
PQ = NR.PolynomialRing(base_ring=QQ, name="x")
x = PQ.gen()


def abstract_method_has_name(method, name):
    return method.__name__ == name


CATEGORY_STATEMENTS = (
    ("Constructors().ZZ() is a ring", lambda _: NR.ZZ() in Rings()),
    ("Constructors().ZZ() has characteristic 0", lambda _: NR.ZZ().characteristic() == 0),
    ("Constructors().ZZ() is not finite", lambda _: not NR.ZZ().is_finite()),
    (
        "Rings() owns ideal-monoid, approximate, and algebra-over surfaces",
        lambda _: abstract_method_has_name(Rings.ParentMethods.ideal_monoid, "ideal_monoid")
        and Rings().Approximate() is ApproximateRingsCategory()
        and Rings().AlgebrasOver(ZZ).base_ring() is ZZ,
    ),
    (
        "ring elements expose divisibility through Sage-compatible elements",
        lambda _: ZZ(2).divides(ZZ(4)) and abstract_method_has_name(_RingIdealParentMethods.divides, "divides"),
    ),
    (
        "ring Hom and End categories own Sage refinement constructors",
        lambda _: abstract_method_has_name(RingHomCategory.from_sage_hom, "from_sage_hom")
        and abstract_method_has_name(RingEndCategory.from_sage_end, "from_sage_end"),
    ),
    (
        "ring field/global-field category classes route through their canonical owners",
        lambda _: _Fields.AlgebraicallyClosed is _AlgebraicallyClosedFields
        and _NumberFields.ParentMethods.ring_of_integers_at_prime.__name__ == "ring_of_integers_at_prime"
        and _NumberFields.ParentMethods.ring_of_integers_at_primes.__name__ == "ring_of_integers_at_primes"
        and _QQ.ParentMethods.algebraic_closure.__name__ == "algebraic_closure"
        and _QQ.ParentMethods.ring_of_integers_at_primes.__name__ == "ring_of_integers_at_primes"
        and _ArchimedeanGlobalFields._base_category_class_and_axiom[1] == "Archimedean"
        and _NonArchimedeanGlobalFields._base_category_class_and_axiom[1] == "NonArchimedean",
    ),
    (
        "commutative and integral-domain ring subcategories own reduced, localization, and divisibility surfaces",
        lambda _: _CommutativeRings.Reduced.__name__ == "_ReducedRings"
        and abstract_method_has_name(_CommutativeRings.SubcategoryMethods.Reduced, "Reduced")
        and abstract_method_has_name(_IntegralDomains.ParentMethods.localization, "localization")
        and abstract_method_has_name(_IntegralDomains.ElementMethods.divides, "divides"),
    ),
    ("Constructors().QQ() is a field", lambda _: NR.QQ() in Rings().Commutative().Field()),
    ("Constructors().QQ() has characteristic 0", lambda _: NR.QQ().characteristic() == 0),
    ("Constructors().QQ() is a number field", lambda _: NR.QQ().is_number_field()),
    ("Constructors().QQ().trace_pairing_discriminant([1]) is 1", lambda _: NR.QQ().trace_pairing_discriminant([QQ(1)]) == 1),
    ("Constructors().QQ().integral_basis_at_prime(2) is [1]", lambda _: tuple(NR.QQ().integral_basis_at_prime(2)) == (QQ(1),)),
    ("Constructors().QQ().integral_basis_at_primes([2, 3]) is [1]", lambda _: tuple(NR.QQ().integral_basis_at_primes([2, 3])) == (QQ(1),)),
    ("Constructors().QQ().maximal_order_at_prime(2) is ZZ", lambda _: NR.QQ().maximal_order_at_prime(2) is ZZ),
    ("Constructors().QQ().maximal_order_at_primes([2, 3]) is ZZ", lambda _: NR.QQ().maximal_order_at_primes([2, 3]) is ZZ),
    ("Constructors().QQbar() is a field", lambda _: NR.QQbar() in Rings().Commutative().Field()),
    ("Constructors().QQbar() has characteristic 0", lambda _: NR.QQbar().characteristic() == 0),
    ("Constructors().QQbar() is algebraically closed", lambda _: NR.QQbar().is_algebraically_closed()),
    ("Constructors().AA() is a field", lambda _: NR.AA() in Rings().Commutative().Field()),
    ("Constructors().AA() has characteristic 0", lambda _: NR.AA().characteristic() == 0),
    ("Constructors().RR() is a field", lambda _: NR.RR() in Rings().Commutative().Field()),
    ("Constructors().RR() is a topological ring", lambda _: NR.RR() in Rings().Topological()),
    ("Constructors().RR() is a topological space", lambda _: NR.RR() in TopologicalSpaces()),
    ("Constructors().RR() has characteristic 0", lambda _: NR.RR().characteristic() == 0),
    ("Constructors().RR() has precision 53", lambda _: NR.RR().precision() == 53),
    (
        "real precision fields change precision through the default Sage route",
        lambda _: abstract_method_has_name(_RealPrecisionFields.ParentMethods.change_precision, "change_precision"),
    ),
    ("Constructors().CC() is a field", lambda _: NR.CC() in Rings().Commutative().Field()),
    ("Constructors().CC() has characteristic 0", lambda _: NR.CC().characteristic() == 0),
    ("Constructors().CC() has precision 53", lambda _: NR.CC().precision() == 53),
    (
        "complex precision fields change precision through the default Sage route",
        lambda _: abstract_method_has_name(_ComplexPrecisionFields.ParentMethods.change_precision, "change_precision")
        and abstract_method_has_name(ApproximateRingsCategory.ParentMethods.change_precision, "change_precision"),
    ),
    ("Constructors().RDF() is a field", lambda _: NR.RDF() in Rings().Commutative().Field()),
    ("Constructors().RDF() has characteristic 0", lambda _: NR.RDF().characteristic() == 0),
    ("Constructors().RDF() has precision 53", lambda _: NR.RDF().precision() == 53),
    ("Constructors().CDF() is a field", lambda _: NR.CDF() in Rings().Commutative().Field()),
    ("Constructors().CDF() has characteristic 0", lambda _: NR.CDF().characteristic() == 0),
    ("Constructors().CDF() has precision 53", lambda _: NR.CDF().precision() == 53),
    ("Constructors().RIF() is a field", lambda _: NR.RIF() in Rings().Commutative().Field()),
    ("Constructors().RIF() has characteristic 0", lambda _: NR.RIF().characteristic() == 0),
    ("Constructors().CIF() is a field", lambda _: NR.CIF() in Rings().Commutative().Field()),
    ("Constructors().CIF() has characteristic 0", lambda _: NR.CIF().characteristic() == 0),
    ("Constructors().RealField(prec=100) is a field", lambda _: NR.RealField(prec=100) in Rings().Commutative().Field()),
    ("Constructors().RealField(prec=100) has precision 100", lambda _: NR.RealField(prec=100).precision() == 100),
    ("Constructors().ComplexField(prec=100) is a field", lambda _: NR.ComplexField(prec=100) in Rings().Commutative().Field()),
    ("Constructors().ComplexField(prec=100) has precision 100", lambda _: NR.ComplexField(prec=100).precision() == 100),
    ("Constructors().RealBallField(prec=100) is a field", lambda _: NR.RealBallField(prec=100) in Rings().Commutative().Field()),
    ("Constructors().RealBallField(prec=100) has precision 100", lambda _: NR.RealBallField(prec=100).precision() == 100),
    ("Constructors().ComplexBallField(prec=100) is a field", lambda _: NR.ComplexBallField(prec=100) in Rings().Commutative().Field()),
    ("Constructors().ComplexBallField(prec=100) has precision 100", lambda _: NR.ComplexBallField(prec=100).precision() == 100),
    ("Constructors().IntegerModRing(order=6) is finite", lambda _: NR.IntegerModRing(order=6) in Rings().Finite()),
    ("Constructors().IntegerModRing(order=6) has order 6", lambda _: NR.IntegerModRing(order=6).order() == 6),
    ("Constructors().IntegerModRing(order=6) has characteristic 6", lambda _: NR.IntegerModRing(order=6).characteristic() == 6),
    ("Constructors().Zmod(order=6) is finite", lambda _: NR.Zmod(order=6) in Rings().Finite()),
    ("Constructors().Zmod(order=6) has order 6", lambda _: NR.Zmod(order=6).order() == 6),
    ("Constructors().Integers(order=6) is finite", lambda _: NR.Integers(order=6) in Rings().Finite()),
    ("Constructors().Integers(order=6) has order 6", lambda _: NR.Integers(order=6).order() == 6),
    ("Constructors().GF(order=5) is a finite field", lambda _: NR.GF(order=5) in Rings().Commutative().Field().Finite()),
    ("Constructors().GF(order=5) has cardinality 5", lambda _: NR.GF(order=5).cardinality() == 5),
    ("Constructors().GF(order=5) has characteristic 5", lambda _: NR.GF(order=5).characteristic() == 5),
    ("Constructors().FiniteField(order=5) is a finite field", lambda _: NR.FiniteField(order=5) in Rings().Commutative().Field().Finite()),
    ("Constructors().FiniteField(order=5) has cardinality 5", lambda _: NR.FiniteField(order=5).cardinality() == 5),
    ("Constructors().NumberField(polynomial=x^3 - 2, name='a') is a number field", lambda _: NR.NumberField(polynomial=x**3 - 2, name="a") in Rings().Commutative().Field().NumberFields()),
    ("Constructors().NumberField(polynomial=x^3 - 2, name='a') has degree 3", lambda _: NR.NumberField(polynomial=x**3 - 2, name="a").degree() == 3),
    (
        "Constructors().NumberFieldTower([x^2 + 1, x^2 + 2], ['a', 'b']) is a number field",
        lambda _: NR.NumberFieldTower(polynomials=[x**2 + 1, x**2 + 2], names=["a", "b"])
        in Rings().Commutative().Field().NumberFields(),
    ),
    (
        "Constructors().NumberFieldTower([x^2 + 1, x^2 + 2], ['a', 'b']) has absolute degree 4",
        lambda _: NR.NumberFieldTower(polynomials=[x**2 + 1, x**2 + 2], names=["a", "b"]).absolute_degree() == 4,
    ),
    ("Constructors().QuadraticField(D=5, name='a') is quadratic", lambda _: NR.QuadraticField(D=5, name="a") in Rings().Commutative().Field().NumberFields().Quadratic()),
    ("Constructors().QuadraticField(D=5, name='a') has degree 2", lambda _: NR.QuadraticField(D=5, name="a").degree() == 2),
    ("Constructors().CyclotomicField(n=5) is cyclotomic", lambda _: NR.CyclotomicField(n=5) in Rings().Commutative().Field().NumberFields().Cyclotomic()),
    ("Constructors().CyclotomicField(n=5) has degree 4", lambda _: NR.CyclotomicField(n=5).degree() == 4),
    ("Constructors().Zp(p=5) is a commutative ring", lambda _: NR.Zp(p=5) in Rings().Commutative()),
    ("Constructors().Zp(p=5) has prime 5", lambda _: NR.Zp(p=5).prime() == 5),
    (
        "p-adic rings own precision, prime-change, and print-mode mutation surfaces",
        lambda _: abstract_method_has_name(_PAdicRings.ParentMethods.change_precision, "change_precision")
        and abstract_method_has_name(_PAdicRings.ParentMethods.change_prime, "change_prime")
        and abstract_method_has_name(_PAdicRings.ParentMethods._change_print_mode, "_change_print_mode"),
    ),
    ("Constructors().Zp(p=5, relative_cap=4, absolute_cap=8, type='lattice-cap') has prime 5", lambda _: NR.Zp(p=5, relative_cap=4, absolute_cap=8, type="lattice-cap").prime() == 5),
    ("Constructors().Zp(p=5, default_prec=4, halting_prec=8, type='relaxed') has prime 5", lambda _: NR.Zp(p=5, default_prec=4, halting_prec=8, type="relaxed").prime() == 5),
    ("Constructors().Qp(p=5) is a field", lambda _: NR.Qp(p=5) in Rings().Commutative().Field()),
    ("Constructors().Qp(p=5) has prime 5", lambda _: NR.Qp(p=5).prime() == 5),
    ("Constructors().Qp(p=5, relative_cap=4, absolute_cap=8, type='lattice-cap') has prime 5", lambda _: NR.Qp(p=5, relative_cap=4, absolute_cap=8, type="lattice-cap").prime() == 5),
    ("Constructors().Qp(p=5, default_prec=4, halting_prec=8, type='relaxed') has prime 5", lambda _: NR.Qp(p=5, default_prec=4, halting_prec=8, type="relaxed").prime() == 5),
    ("Constructors().Zq(q=25, names='a') is a commutative ring", lambda _: NR.Zq(q=25, names="a") in Rings().Commutative()),
    ("Constructors().Zq(p=5, degree=2, names='a') has prime 5", lambda _: NR.Zq(p=5, degree=2, names="a").prime() == 5),
    (
        "Constructors().Zq(factorization=[(5, 2)], names='a') has prime 5",
        lambda _: NR.Zq(factorization=[(5, 2)], names="a").prime() == 5,
    ),
    ("Constructors().Qq(q=25, names='a') is a field", lambda _: NR.Qq(q=25, names="a") in Rings().Commutative().Field()),
    ("Constructors().Qq(p=5, degree=2, names='a') has prime 5", lambda _: NR.Qq(p=5, degree=2, names="a").prime() == 5),
    (
        "Constructors().Qq(factorization=[(5, 2)], names='a') has prime 5",
        lambda _: NR.Qq(factorization=[(5, 2)], names="a").prime() == 5,
    ),
    (
        "Constructors().PolynomialRing(ZZ, name='t') is a polynomial ring over ZZ",
        lambda _: NR.PolynomialRing(base_ring=ZZ, name="t") in Rings().PolynomialRingsOver(ZZ),
    ),
    ("Constructors().PolynomialRing(ZZ, name='t') has base ring ZZ", lambda _: NR.PolynomialRing(base_ring=ZZ, name="t").base_ring() is ZZ),
    ("Constructors().PolynomialRing(ZZ, name='t') has one generator", lambda _: NR.PolynomialRing(base_ring=ZZ, name="t").ngens() == 1),
    (
        "Constructors().PowerSeriesRing(ZZ, 't') is a power-series ring over ZZ",
        lambda _: NR.PowerSeriesRing(base_ring=ZZ, name="t") in Rings().PowerSeriesRingsOver(ZZ),
    ),
    ("Constructors().PowerSeriesRing(ZZ, 't') has base ring ZZ", lambda _: NR.PowerSeriesRing(base_ring=ZZ, name="t").base_ring() is ZZ),
    (
        "Constructors().MultivariatePowerSeriesRing(ZZ, names=('x', 'y')) has two generators",
        lambda _: NR.MultivariatePowerSeriesRing(base_ring=ZZ, names=("x", "y")).ngens() == 2,
    ),
    (
        "Constructors().MultivariatePowerSeriesRingWithGeneratorPrefix(ZZ, prefix='x', num_gens=2) has two generators",
        lambda _: NR.MultivariatePowerSeriesRingWithGeneratorPrefix(base_ring=ZZ, prefix="x", num_gens=2).ngens() == 2,
    ),
    (
        "Constructors().LaurentSeriesRing(ZZ, 't') is a Laurent-series ring over ZZ",
        lambda _: NR.LaurentSeriesRing(base_ring=ZZ, name="t") in Rings().LaurentSeriesRingsOver(ZZ),
    ),
    ("Constructors().LaurentSeriesRing(ZZ, 't') has base ring ZZ", lambda _: NR.LaurentSeriesRing(base_ring=ZZ, name="t").base_ring() is ZZ),
    (
        "Constructors().LaurentSeriesRing(power_series_ring=...) has base ring ZZ",
        lambda _: NR.LaurentSeriesRing(power_series_ring=NR.PowerSeriesRing(base_ring=ZZ, name="u")).base_ring() is ZZ,
    ),
    (
        "Constructors().PuiseuxSeriesRing(QQ, 't') is a Puiseux-series ring over QQ",
        lambda _: NR.PuiseuxSeriesRing(base_ring=QQ, name="t") in Rings().PuiseuxSeriesRingsOver(QQ),
    ),
    ("Constructors().PuiseuxSeriesRing(QQ, 't') has base ring QQ", lambda _: NR.PuiseuxSeriesRing(base_ring=QQ, name="t").base_ring() is QQ),
    (
        "Constructors().PuiseuxSeriesRing(laurent_series_ring=...) has base ring QQ",
        lambda _: NR.PuiseuxSeriesRing(laurent_series_ring=NR.LaurentSeriesRing(base_ring=QQ, name="u")).base_ring() is QQ,
    ),
    ("Constructors().MatrixRing(base_ring=ZZ, n=2) is a matrix algebra over ZZ", lambda _: NR.MatrixRing(base_ring=ZZ, n=2) in Rings().MatrixAlgebras(ZZ, 2, 2)),
    ("Constructors().MatrixRing(base_ring=ZZ, n=2) has 2 rows", lambda _: NR.MatrixRing(base_ring=ZZ, n=2).nrows() == 2),
    ("Constructors().MatrixRing(base_ring=ZZ, n=2) has 2 columns", lambda _: NR.MatrixRing(base_ring=ZZ, n=2).ncols() == 2),
    ("Constructors().MatrixRing(base_ring=ZZ, n=2) has base ring ZZ", lambda _: NR.MatrixRing(base_ring=ZZ, n=2).base_ring() is ZZ),
    (
        "Constructors().MatrixRing(ZZ, 2) exposes zero matrix and sparse predicate",
        lambda _: abstract_method_has_name(_MatrixAlgebras.ParentMethods.zero_matrix, "zero_matrix")
        and abstract_method_has_name(_MatrixAlgebras.ParentMethods.is_sparse, "is_sparse"),
    ),
    (
        "Constructors().MatrixRing(ZZ, 2).matrix_from_matrix(...) returns the same matrix",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).matrix_from_matrix(matrix(ZZ, [[1, 2], [3, 4]]))
        == matrix(ZZ, [[1, 2], [3, 4]]),
    ),
    (
        "Constructors().MatrixRing(ZZ, 2).matrix_from_entries(...) uses row-major entries",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).matrix_from_entries([1, 2, 3, 4]) == matrix(ZZ, [[1, 2], [3, 4]]),
    ),
    (
        "Constructors().MatrixRing(ZZ, 2).matrix_from_rows(...) uses row data",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).matrix_from_rows([[1, 2], [3, 4]]) == matrix(ZZ, [[1, 2], [3, 4]]),
    ),
    (
        "Constructors().MatrixRing(ZZ, 2).scalar_matrix(3) is 3 times the identity",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).scalar_matrix(3) == 3 * identity_matrix(ZZ, 2),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
