from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.modules import Modules
from category_specs.modules.subcategories.constructions.quotients import _Quotients as ModuleQuotients
from category_specs.sets import Sets
from category_specs.utils import assert_smoke_statements, refine_category
from sage.modules.fp_graded.free_module import FreeGradedModule


R6 = IntegerModRing(6)
NM6 = Modules(R6).Constructors()
MR6 = Modules(R6)

PZ = PolynomialRing(ZZ, "x")
NMPZ = Modules(PZ).Constructors()
MPZ = Modules(PZ)

NMZZ = Modules(ZZ).Constructors()
NMQQ = Modules(QQ).Constructors()
MZZCat = Modules(ZZ)
MQQCat = Modules(QQ)

V = VectorSpace(QQ, 3)
W = V.subspace([V.gen(0), V.gen(1)])
Wb = V.subspace_with_basis([V.gen(0), V.gen(1)])
Q = V.quotient_module(W)

M = FreeModule(ZZ, 3)
S = M.submodule([2 * M.gen(0), 3 * M.gen(1)])
Sb = M.submodule_with_basis([2 * M.gen(0), 3 * M.gen(1)])
Qfree = M.quotient_module(S)

C = CombinatorialFreeModule(QQ, ["a", "b"])
a = C.monomial("a")
b = C.monomial("b")
CS = C.submodule([a + b])
CQ = C.quotient_module(CS)

Wfg = M.submodule([2 * M.gen(0), 4 * M.gen(1), M.gen(2)])
Mfg = M / Wfg

E = ExteriorAlgebra(QQ, names=("x", "y"))
xE, yE = E.gens()
NME = Modules(E).Constructors()

K = GF(5**3, "z")
z = K.gen()
Sore = OrePolynomialRing(K, K.frobenius_endomorphism(), names="X")
X = Sore.gen()
NMK = Modules(K).Constructors()


def fp_module_from_identity_cokernel():
    F = FreeGradedModule(E, [0, 1])
    return NME.FPModuleFromCokernelMap(Hom(F, F).identity())


def integer_lattice_from_cyclotomic_order_element():
    K5 = CyclotomicField(5)
    O5 = K5.ring_of_integers()
    return NMZZ.IntegerLatticeFromOrderElement(O5(K5.gen()))


def rational_quotient_split_methods_have_one_dimensional_outputs():
    V = VectorSpace(QQ, 3)
    W = V.subspace([V.gen(2)])
    Q = V.quotient_module(W)
    methods = ModuleQuotients.ParentMethods
    relation_matrix = matrix(QQ, [[1, 0]])
    quotient_by_submodule = methods.quotient_by_submodule(Q, Q.subspace([Q.gen(0)]))
    quotient_by_generators = methods.quotient_by_generators(Q, [Q.gen(0)])
    quotient_by_relation_matrix = methods.quotient_by_relation_matrix(Q, relation_matrix)
    quotient_by_relation_rows = methods.quotient_by_relation_rows(Q, [[1, 0]])
    assert quotient_by_submodule.dimension() == 1
    assert quotient_by_generators.dimension() == 1
    assert quotient_by_relation_matrix.dimension() == 1
    assert quotient_by_relation_rows.dimension() == 1
    return True


SMOKE_STATEMENTS = (
    (
        "Modules(Zmod(6)).Constructors().FreeModule(2) is finite-rank free",
        lambda _: NM6.FreeModule(2) in MR6.Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(2) is finite over finite base ring",
        lambda _: NM6.FreeModule(2) in MR6.Finite(),
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(2) has ordered basis",
        lambda _: NM6.FreeModule(2) in MR6.WithOrderedBasis(),
    ),
    ("Modules(Zmod(6)).Constructors().FreeModule(2) has base ring Zmod(6)", lambda _: NM6.FreeModule(2).base_ring() is R6),
    ("Modules(Zmod(6)).Constructors().FreeModule(2) has rank 2", lambda _: NM6.FreeModule(2).rank() == 2),
    (
        "Modules(QQ).Constructors().FreeModuleWithBasisKeys({a, b}) has two basis keys",
        lambda _: NMQQ.FreeModuleWithBasisKeys(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModuleWithoutBasis(2) has rank 2",
        lambda _: NM6.FreeModuleWithoutBasis(2).rank() == 2,
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModuleWithInnerProductRows(...) records the Gram matrix",
        lambda _: NM6.FreeModuleWithInnerProductRows(2, [[1, 0], [0, 1]]).inner_product_matrix()
        == matrix(R6, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModuleWithInnerProductEntries(...) records the Gram matrix",
        lambda _: NM6.FreeModuleWithInnerProductEntries(2, [1, 0, 0, 1]).inner_product_matrix()
        == matrix(R6, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(ZZ['x']).Constructors().FreeModule(2) is free over an integral domain",
        lambda _: NMPZ.FreeModule(2) in MPZ.Free().FiniteRank().WithOrderedBasis(),
    ),
    ("Modules(ZZ['x']).Constructors().FreeModule(2) has base ring ZZ['x']", lambda _: NMPZ.FreeModule(2).base_ring() is PZ),
    ("Modules(ZZ['x']).Constructors().FreeModule(2) has rank 2", lambda _: NMPZ.FreeModule(2).rank() == 2),
    (
        "Modules(ZZ).Constructors().FreeModule(2) is free over a PID",
        lambda _: NMZZ.FreeModule(2) in MZZCat.Free().FiniteRank().WithOrderedBasis(),
    ),
    ("Modules(ZZ).Constructors().FreeModule(2) has base ring ZZ", lambda _: NMZZ.FreeModule(2).base_ring() is ZZ),
    ("Modules(ZZ).Constructors().FreeModule(2) has rank 2", lambda _: NMZZ.FreeModule(2).rank() == 2),
    (
        "Modules(QQ).Constructors().VectorSpace(2) is finite-rank free",
        lambda _: NMQQ.VectorSpace(2) in MQQCat.Free().FiniteRank().WithOrderedBasis(),
    ),
    ("Modules(QQ).Constructors().VectorSpace(2) is over a field", lambda _: NMQQ.VectorSpace(2) in MQQCat.OverField()),
    ("Modules(QQ).Constructors().VectorSpace(2) has base ring QQ", lambda _: NMQQ.VectorSpace(2).base_ring() is QQ),
    ("Modules(QQ).Constructors().VectorSpace(2) has dimension 2", lambda _: NMQQ.VectorSpace(2).dimension() == 2),
    (
        "Modules(QQ).Constructors().VectorSpaceWithBasisKeys({a, b}) has two basis keys",
        lambda _: NMQQ.VectorSpaceWithBasisKeys(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(QQ).Constructors().VectorSpaceWithoutBasis(2) has dimension 2",
        lambda _: NMQQ.VectorSpaceWithoutBasis(2).dimension() == 2,
    ),
    (
        "Modules(QQ).Constructors().VectorSpaceWithInnerProductRows(...) records the Gram matrix",
        lambda _: NMQQ.VectorSpaceWithInnerProductRows(2, [[1, 0], [0, 1]]).inner_product_matrix()
        == matrix(QQ, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(QQ).Constructors().VectorSpaceWithInnerProductEntries(...) records the Gram matrix",
        lambda _: NMQQ.VectorSpaceWithInnerProductEntries(2, [1, 0, 0, 1]).inner_product_matrix()
        == matrix(QQ, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(RDF).Constructors().FreeModule(2) is finite-rank free",
        lambda _: Modules(RDF).Constructors().FreeModule(2) in Modules(RDF).Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "Modules(CDF).Constructors().FreeModule(2) is finite-rank free",
        lambda _: Modules(CDF).Constructors().FreeModule(2) in Modules(CDF).Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "refine_category(V.subspace(...), Subobjects()) is a module subobject",
        lambda _: refine_category(W, MQQCat.Subobjects()) in MQQCat.Subobjects(),
    ),
    ("refined V.subspace(...) has ambient vector space V", lambda _: refine_category(W, MQQCat.Subobjects()).ambient_vector_space() is V),
    (
        "refine_category(V.subspace_with_basis(...), Subobjects()+WithOrderedBasis() has ordered basis",
        lambda _: refine_category(Wb, MQQCat.WithOrderedBasis().Subobjects())
        in MQQCat.WithOrderedBasis().Subobjects(),
    ),
    (
        "refine_category(V.quotient_module(W), Quotients()) is a module quotient",
        lambda _: refine_category(Q, MQQCat.Quotients()) in MQQCat.Quotients(),
    ),
    (
        "Modules(QQ).Constructors().quotient_module(V, W) is a module quotient",
        lambda _: NMQQ.quotient_module(V, W) in MQQCat.Quotients(),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(...) is quadratic",
        lambda _: NMZZ.FreeQuadraticModule(2, matrix(ZZ, [[2, 1], [1, 2]])) in MZZCat.WithForms().Quadratic(),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(...) has rank 2",
        lambda _: NMZZ.FreeQuadraticModule(2, matrix(ZZ, [[2, 1], [1, 2]])).rank() == 2,
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModuleFromRows(...) records the form",
        lambda _: NMZZ.FreeQuadraticModuleFromRows(2, [[2, 1], [1, 2]]).inner_product_matrix()
        == matrix(ZZ, [[2, 1], [1, 2]]),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModuleFromEntries(...) records the form",
        lambda _: NMZZ.FreeQuadraticModuleFromEntries(2, [2, 1, 1, 2]).inner_product_matrix()
        == matrix(ZZ, [[2, 1], [1, 2]]),
    ),
    (
        "Modules(QQ).Constructors().CombinatorialFreeModule({a, b}) is free with ordered generators",
        lambda _: (
            NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])) in Modules(QQ).Free()
            and NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])) in Modules(QQ).WithBasis()
            and NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"]))
            in Modules(QQ).WithOrderedGeneratingSet()
        ),
    ),
    (
        "Modules(QQ).Constructors().CombinatorialFreeModule({a, b}) has two basis keys",
        lambda _: NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(QQ).Constructors().FiniteRankFreeModule(2) is finite-rank free",
        lambda _: NMQQ.FiniteRankFreeModule(2) in MQQCat.Free().FiniteRank(),
    ),
    ("Modules(QQ).Constructors().FiniteRankFreeModule(2) has rank 2", lambda _: NMQQ.FiniteRankFreeModule(2).rank() == 2),
    (
        "Modules(ZZ).Constructors().span(...) is a module subobject",
        lambda _: NMZZ.span([M.gen(0), M.gen(1)]) in MZZCat.Subobjects(),
    ),
    (
        "refine_category(M.submodule(...), Subobjects()) is a module subobject",
        lambda _: refine_category(S, MZZCat.Subobjects()) in MZZCat.Subobjects(),
    ),
    ("refined M.submodule(...) has ambient module M", lambda _: refine_category(S, MZZCat.Subobjects()).ambient_module() is M),
    (
        "refine_category(M.submodule_with_basis(...), Subobjects()+WithOrderedBasis()) has ordered basis",
        lambda _: refine_category(Sb, MZZCat.WithOrderedBasis().Subobjects())
        in MZZCat.WithOrderedBasis().Subobjects(),
    ),
    (
        "refine_category(M.quotient_module(S), Quotients()) is a module quotient",
        lambda _: refine_category(Qfree, MZZCat.Quotients()) in MZZCat.Quotients(),
    ),
    (
        "Modules(ZZ).Constructors().quotient_of_free_modules(M, S) is a module quotient",
        lambda _: NMZZ.quotient_of_free_modules(M, S) in MZZCat.Quotients(),
    ),
    (
        "Modules(QQ).Quotients().ParentMethods quotient_by_* split methods produce one-dimensional quotient vectorspaces",
        lambda _: rational_quotient_split_methods_have_one_dimensional_outputs(),
    ),
    (
        "refine_category(C.submodule([a + b]), Subobjects()+WithBasis()) has a basis",
        lambda _: refine_category(CS, MQQCat.WithBasis().Subobjects()) in MQQCat.WithBasis().Subobjects(),
    ),
    (
        "refine_category(C.quotient_module(CS), Quotients()+WithBasis()) has a basis",
        lambda _: refine_category(CQ, MQQCat.WithBasis().Quotients()) in MQQCat.WithBasis().Quotients(),
    ),
    (
        "refine_category(SymmetricGroup(3).regular_representation(QQ), RepresentationModules()) is a representation module",
        lambda _: refine_category(SymmetricGroup(3).regular_representation(QQ), MQQCat.RepresentationModules())
        in MQQCat.RepresentationModules(),
    ),
    (
        "refine_category(M / Wfg, FinitelyPresented().OverPID()) is finitely presented over a PID",
        lambda _: refine_category(Mfg, [MZZCat.FinitelyGenerated(), MZZCat.FinitelyPresented(), MZZCat.OverPID()])
        in MZZCat.FinitelyPresented().OverPID(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FreeGradedModule(E, (-1, 3)) is free graded",
        lambda _: NME.FreeGradedModule(E, (-1, 3)) in Modules(E).FreeGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(...) is finitely presented graded",
        lambda _: NME.FPModule(E, [0, 1], [[xE, E.one()]]) in Modules(E).FinitelyPresentedGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModuleFromPresentation(...) is finitely presented graded",
        lambda _: NME.FPModuleFromPresentation(E, generator_degrees=[0, 1], relations=[[xE, E.one()]])
        in Modules(E).FinitelyPresentedGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModuleFromFreeGradedModule(...) is finitely presented graded",
        lambda _: NME.FPModuleFromFreeGradedModule(NME.FreeGradedModule(E, [0, 1]))
        in Modules(E).FinitelyPresentedGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModuleFromCokernelMap(identity) is trivial",
        lambda _: fp_module_from_identity_cokernel().is_trivial(),
    ),
    (
        "Modules(GF(5^3)).Constructors().OreQuotientModule(S, X^2 + z) is an Ore module",
        lambda _: NMK.OreQuotientModule(Sore, X**2 + z) in Modules(K).OreModules(),
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(...) is an integer lattice",
        lambda _: NMZZ.IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]]) in MZZCat.IntegerLattices(),
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(...) has rank 3",
        lambda _: NMZZ.IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]]).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLatticeFromBasisMatrix(...) has rank 3",
        lambda _: NMZZ.IntegerLatticeFromBasisMatrix(matrix(ZZ, [[1, 0, 3], [0, 2, 1], [0, 2, 7]])).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLatticeFromBasisRows(...) has rank 3",
        lambda _: NMZZ.IntegerLatticeFromBasisRows([[1, 0, 3], [0, 2, 1], [0, 2, 7]]).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLatticeFromOrderElement(zeta_5) has rank 4",
        lambda _: integer_lattice_from_cyclotomic_order_element().rank() == 4,
    ),
    (
        "Modules(ZZ).Constructors().TorsionQuadraticForm(...) is a torsion quadratic module",
        lambda _: NMZZ.TorsionQuadraticForm(matrix(QQ, [[1, QQ(1) / 2], [QQ(1) / 2, 1]]))
        in MZZCat.TorsionQuadraticModules(),
    ),
    (
        "Modules(ZZ).Constructors().TorsionQuadraticFormFromRows(...) is a torsion quadratic module",
        lambda _: NMZZ.TorsionQuadraticFormFromRows([[1, QQ(1) / 2], [QQ(1) / 2, 1]])
        in MZZCat.TorsionQuadraticModules(),
    ),
    (
        "Modules(ZZ).Constructors().ring_as_rank_one_module() is rank-one free",
        lambda _: NMZZ.ring_as_rank_one_module() in MZZCat.Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "Modules(ZZ).Constructors().ideal_as_submodule((6)) is an ideal submodule",
        lambda _: NMZZ.ideal_as_submodule(ZZ.ideal(6)) in MZZCat.RIdeals(),
    ),
    (
        "Modules(ZZ).Constructors().invertible_ideal_as_projective_submodule((1)) is projective",
        lambda _: NMZZ.invertible_ideal_as_projective_submodule(ZZ.ideal(1)) in MZZCat.Projective(),
    ),
    (
        "Modules(ZZ).Constructors().polynomial_ring_as_module(name='t') is a ring object as a module",
        lambda _: NMZZ.polynomial_ring_as_module(name="t") in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().polynomial_ring_as_module(name='t') has base ring ZZ",
        lambda _: NMZZ.polynomial_ring_as_module(name="t").base_ring() is ZZ,
    ),
    (
        "Modules(ZZ).Constructors().power_series_ring_as_module('t') is a ring object as a module",
        lambda _: NMZZ.power_series_ring_as_module("t") in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().multivariate_power_series_ring_as_module(('x', 'y')) is a ring object as a module",
        lambda _: NMZZ.multivariate_power_series_ring_as_module(("x", "y")) in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().multivariate_power_series_ring_with_generator_prefix_as_module('x', 2) is a ring object as a module",
        lambda _: NMZZ.multivariate_power_series_ring_with_generator_prefix_as_module("x", 2)
        in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().laurent_series_ring_as_module('t') is a ring object as a module",
        lambda _: NMZZ.laurent_series_ring_as_module("t") in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().laurent_series_ring_from_power_series_as_module(...) is a ring object as a module",
        lambda _: NMZZ.laurent_series_ring_from_power_series_as_module(PowerSeriesRing(ZZ, "u"))
        in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().puiseux_series_ring_as_module('t') is a ring object as a module",
        lambda _: NMZZ.puiseux_series_ring_as_module("t") in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().puiseux_series_ring_from_laurent_series_as_module(...) is a ring object as a module",
        lambda _: NMZZ.puiseux_series_ring_from_laurent_series_as_module(LaurentSeriesRing(ZZ, "u"))
        in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().matrix_ring_as_module(2) is a ring object as a module",
        lambda _: NMZZ.matrix_ring_as_module(2) in MZZCat.RingObjectsAsModules(),
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)
