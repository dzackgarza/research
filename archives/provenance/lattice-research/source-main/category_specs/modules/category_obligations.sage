from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.modules import Modules, _RModObjects
from category_specs.modules.homsets import RModuleHomCategory, _Bilinear, _Forms, _Quadratic, _RModMorphisms
from category_specs.modules.subcategories.constructions.objects_over import _ObjectsOver
from category_specs.modules.subcategories.constructions.objects_under import _ObjectsUnder
from category_specs.modules.subcategories.constructions.quotients import _Quotients as ModuleQuotients
from category_specs.modules.subcategories.finitely_generated import _FinitelyGenerated
from category_specs.modules.subcategories.finitely_presented import _FinitelyPresented
from category_specs.modules.subcategories.finitely_presented_graded_modules import _FinitelyPresentedGradedModules
from category_specs.modules.subcategories.finitely_presented_over_pid import FinitelyPresentedModulesOverPID
from category_specs.modules.subcategories.ore_modules import _OreModules
from category_specs.modules.subcategories.over_commutative_ring import _OverCommutativeRing
from category_specs.modules.subcategories.over_complete_ring import _OverCompleteRing
from category_specs.modules.subcategories.over_dedekind_domain import _OverDedekindDomain
from category_specs.modules.subcategories.over_field import _OverField
from category_specs.modules.subcategories.over_integral_domain import _OverIntegralDomain
from category_specs.modules.subcategories.over_local_ring import _OverLocalRing
from category_specs.modules.subcategories.projective import _Projective
from category_specs.modules.subcategories.r_ideals import _RIdeals
from category_specs.modules.subcategories.torsion import _Torsion
from category_specs.modules.subcategories.torsionfree import _Torsionfree
from category_specs.modules.subcategories.with_ordered_generating_set import _WithOrderedGeneratingSet
from category_specs.modules.subcategories.with_basis import _WithBasis, _WithOrderedBasis
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.utils import assert_category_statements, refine_category
from sage.modules.fp_graded.free_module import FreeGradedModule


NR = Rings().Constructors()

R6 = NR.IntegerModRing(order=6)
NM6 = Modules(R6).Constructors()
MR6 = Modules(R6)

PZ = NR.PolynomialRing(base_ring=ZZ, name="x")
NMPZ = Modules(PZ).Constructors()
MPZ = Modules(PZ)

NMZZ = Modules(ZZ).Constructors()
NMQQ = Modules(QQ).Constructors()
MZZCat = Modules(ZZ)
MQQCat = Modules(QQ)

V = NMQQ.VectorSpace(dimension=3)
W = V.subspace([V.gen(0), V.gen(1)])
Wb = V.subspace_with_basis([V.gen(0), V.gen(1)])
Q = V.quotient_module(W)

M = NMZZ.FreeModule(rank=3)
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

K = NR.GF(order=5**3, name="z")
z = K.gen()
Sore = OrePolynomialRing(K, K.frobenius_endomorphism(), names="X")
X = Sore.gen()
NMK = Modules(K).Constructors()


def fp_module_from_identity_cokernel():
    F = FreeGradedModule(E, [0, 1])
    return NME.FPModule(defining_map=Hom(F, F).identity())


def integer_lattice_from_cyclotomic_order_element():
    K5 = NR.CyclotomicField(n=5, names="zeta")
    O5 = K5.ring_of_integers()
    return NMZZ.IntegerLattice(basis=O5(K5.gen()))


def rank_one_module_isomorphisms_are_inverse_witnesses():
    M1, from_M1, to_M1 = NM6.rank_one_module_with_ring_isomorphisms(basis=R6(5))
    x = R6(2)
    v = M1([x])
    return from_M1(to_M1(x)) == x and to_M1(from_M1(v)) == v


def rational_quotient_split_methods_have_one_dimensional_outputs():
    V = NMQQ.VectorSpace(dimension=3)
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


class _BaseModulePredicateWitness(_RModObjects):
    pass


def abstract_method_has_name(method, name):
    return method.__name__ == name


def base_module_surface_rejects_specialized_structure():
    witness = _BaseModulePredicateWitness()
    return (
        not witness.is_lattice()
        and not witness.is_representation_module()
        and not witness.is_free_graded_module()
        and not witness.is_finitely_presented_graded_module()
        and not witness.is_ore_module()
        and not witness.is_torsion_quadratic_module()
        and not witness.is_ring_object_as_module()
    )


def refine_for_membership(parent, categories):
    return refine_category(parent, categories, test=False)


CATEGORY_STATEMENTS = (
    (
        "Modules(Zmod(6)).Constructors().FreeModule(rank=2) is finite-rank free",
        lambda _: NM6.FreeModule(rank=2) in MR6.Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(rank=2) is finite over finite base ring",
        lambda _: NM6.FreeModule(rank=2) in MR6.Finite(),
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(rank=2) has ordered basis",
        lambda _: NM6.FreeModule(rank=2) in MR6.WithOrderedBasis(),
    ),
    ("Modules(Zmod(6)).Constructors().FreeModule(rank=2) has base ring Zmod(6)", lambda _: NM6.FreeModule(rank=2).base_ring() is R6),
    (
        "module Hom category owns scalar multiplication and form-refinement surfaces",
        lambda _: abstract_method_has_name(_RModMorphisms.scale, "scale")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ParentMethods.base_ring, "base_ring")
        and abstract_method_has_name(Modules(ZZ).EndCategory().ParentMethods.base_ring, "base_ring")
        and abstract_method_has_name(Modules(ZZ).AutCategory().ParentMethods.base_ring, "base_ring")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.kernel, "kernel")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.image, "image")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.direct_image, "direct_image")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.inverse_image, "inverse_image")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.restrict_domain, "restrict_domain")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.restrict_codomain, "restrict_codomain")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.restrict, "restrict")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.cokernel, "cokernel")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.coimage, "coimage")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.base_change, "base_change")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.lift, "lift")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.preimage_representative, "preimage_representative")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.is_injective, "is_injective")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.is_surjective, "is_surjective")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.is_bijective, "is_bijective")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.inverse, "inverse")
        and abstract_method_has_name(Modules(ZZ).HomCategory().ElementMethods.is_zero, "is_zero")
        and RModuleHomCategory.Forms is _Forms
        and abstract_method_has_name(_Forms.SubcategoryMethods.NonDegenerate, "NonDegenerate")
        and _Forms.Bilinear is _Bilinear
        and _Forms.Quadratic is _Quadratic,
    ),
    (
        "module axiom subcategory classes route through Modules",
        lambda _: Modules.FinitelyGenerated is _FinitelyGenerated
        and Modules.FinitelyPresented is _FinitelyPresented
        and Modules.OverCommutativeRing is _OverCommutativeRing
        and Modules.OverCompleteRing is _OverCompleteRing
        and Modules.OverDedekindDomain is _OverDedekindDomain
        and Modules.OverField is _OverField
        and Modules.OverIntegralDomain is _OverIntegralDomain
        and Modules.OverLocalRing is _OverLocalRing
        and Modules.Projective is _Projective
        and Modules.RIdeals is _RIdeals
        and Modules.Torsion is _Torsion
        and Modules.Torsionfree is _Torsionfree
        and Modules.WithOrderedGeneratingSet is _WithOrderedGeneratingSet,
    ),
    (
        "module slices own structure-module surfaces",
        lambda _: abstract_method_has_name(_ObjectsOver.ParentMethods.structure_module, "structure_module")
        and abstract_method_has_name(_ObjectsUnder.ParentMethods.structure_module, "structure_module"),
    ),
    (
        "ordered-generator module Hom owns generator-image construction routes",
        lambda _: abstract_method_has_name(_WithOrderedGeneratingSet.HomCategory.ParentMethods.from_images, "from_images")
        and abstract_method_has_name(_WithOrderedGeneratingSet.HomCategory.ParentMethods.from_function, "from_function")
        and abstract_method_has_name(_WithOrderedGeneratingSet.HomCategory.ElementMethods.generator_images, "generator_images"),
    ),
    (
        "finite-presentation module categories own presentation and Smith surfaces",
        lambda _: abstract_method_has_name(_FinitelyPresentedGradedModules.ParentMethods.presentation, "presentation")
        and abstract_method_has_name(FinitelyPresentedModulesOverPID.ParentMethods.invariants, "invariants")
        and abstract_method_has_name(FinitelyPresentedModulesOverPID.ParentMethods.invariant_factors, "invariant_factors")
        and abstract_method_has_name(FinitelyPresentedModulesOverPID.ParentMethods.smith_form_gens, "smith_form_gens")
        and abstract_method_has_name(FinitelyPresentedModulesOverPID.Torsion.ParentMethods.is_p_elementary, "is_p_elementary"),
    ),
    (
        "finite-presentation PID module Hom owns presentation-generator image witnesses",
        lambda _: abstract_method_has_name(FinitelyPresentedModulesOverPID.HomCategory.ElementMethods.im_gens, "im_gens"),
    ),
    (
        "Ore modules own companion-matrix surface",
        lambda _: abstract_method_has_name(_OreModules.ParentMethods.companion_matrix, "companion_matrix"),
    ),
    ("Modules(Zmod(6)).Constructors().FreeModule(rank=2) has rank 2", lambda _: NM6.FreeModule(rank=2).rank() == 2),
    (
        "Modules(QQ).Constructors().FreeModule(basis_keys={a, b}) has two basis keys",
        lambda _: NMQQ.FreeModule(basis_keys=Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(rank=2, with_basis=None) has rank 2",
        lambda _: NM6.FreeModule(rank=2, with_basis=None).rank() == 2,
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(inner_product_rows=...) records the Gram matrix",
        lambda _: NM6.FreeModule(rank=2, inner_product_rows=[[1, 0], [0, 1]]).inner_product_matrix()
        == matrix(R6, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(inner_product_entries=...) records the Gram matrix",
        lambda _: NM6.FreeModule(rank=2, inner_product_entries=[1, 0, 0, 1]).inner_product_matrix()
        == matrix(R6, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(ZZ['x']).Constructors().FreeModule(rank=2) is free over an integral domain",
        lambda _: NMPZ.FreeModule(rank=2) in MPZ.Free().FiniteRank().WithOrderedBasis(),
    ),
    ("Modules(ZZ['x']).Constructors().FreeModule(rank=2) has base ring ZZ['x']", lambda _: NMPZ.FreeModule(rank=2).base_ring() is PZ),
    ("Modules(ZZ['x']).Constructors().FreeModule(rank=2) has rank 2", lambda _: NMPZ.FreeModule(rank=2).rank() == 2),
    (
        "Modules(ZZ).Constructors().FreeModule(rank=2) is free over a PID",
        lambda _: NMZZ.FreeModule(rank=2) in MZZCat.Free().FiniteRank().WithOrderedBasis(),
    ),
    ("Modules(ZZ).Constructors().FreeModule(rank=2) has base ring ZZ", lambda _: NMZZ.FreeModule(rank=2).base_ring() is ZZ),
    ("Modules(ZZ).Constructors().FreeModule(rank=2) has rank 2", lambda _: NMZZ.FreeModule(rank=2).rank() == 2),
    (
        "Modules(QQ).Constructors().VectorSpace(dimension=2) is finite-rank free",
        lambda _: NMQQ.VectorSpace(dimension=2) in MQQCat.Free().FiniteRank().WithOrderedBasis(),
    ),
    ("Modules(QQ).Constructors().VectorSpace(dimension=2) is over a field", lambda _: NMQQ.VectorSpace(dimension=2) in MQQCat.OverField()),
    ("Modules(QQ).Constructors().VectorSpace(dimension=2) has base ring QQ", lambda _: NMQQ.VectorSpace(dimension=2).base_ring() is QQ),
    ("Modules(QQ).Constructors().VectorSpace(dimension=2) has dimension 2", lambda _: NMQQ.VectorSpace(dimension=2).dimension() == 2),
    (
        "Modules(QQ).Constructors().VectorSpace(basis_keys={a, b}) has two basis keys",
        lambda _: NMQQ.VectorSpace(basis_keys=Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(QQ).Constructors().VectorSpace(dimension=2, with_basis=None) has dimension 2",
        lambda _: NMQQ.VectorSpace(dimension=2, with_basis=None).dimension() == 2,
    ),
    (
        "Modules(QQ).Constructors().VectorSpace(inner_product_rows=...) records the Gram matrix",
        lambda _: NMQQ.VectorSpace(dimension=2, inner_product_rows=[[1, 0], [0, 1]]).inner_product_matrix()
        == matrix(QQ, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(QQ).Constructors().VectorSpace(inner_product_entries=...) records the Gram matrix",
        lambda _: NMQQ.VectorSpace(dimension=2, inner_product_entries=[1, 0, 0, 1]).inner_product_matrix()
        == matrix(QQ, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(RDF).Constructors().FreeModule(rank=2) is finite-rank free",
        lambda _: Modules(RDF).Constructors().FreeModule(rank=2) in Modules(RDF).Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "Modules(CDF).Constructors().FreeModule(rank=2) is finite-rank free",
        lambda _: Modules(CDF).Constructors().FreeModule(rank=2) in Modules(CDF).Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "refine_category(V.subspace(...), Subobjects()) is a module subobject",
        lambda _: refine_for_membership(W, MQQCat.Subobjects()) in MQQCat.Subobjects(),
    ),
    (
        "refined V.subspace(...) has ambient vector space V",
        lambda _: refine_for_membership(W, MQQCat.Subobjects()).ambient_vector_space() is V,
    ),
    (
        "refine_category(V.subspace_with_basis(...), Subobjects()+WithOrderedBasis() has ordered basis",
        lambda _: refine_for_membership(Wb, MQQCat.WithOrderedBasis().Subobjects())
        in MQQCat.WithOrderedBasis().Subobjects(),
    ),
    (
        "refine_category(V.quotient_module(W), Quotients()) is a module quotient",
        lambda _: refine_for_membership(Q, MQQCat.Quotients()) in MQQCat.Quotients(),
    ),
    (
        "Modules(QQ).Constructors().quotient_module(V, W) is a module quotient",
        lambda _: NMQQ.quotient_module(V, W) in MQQCat.Quotients(),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(...) is quadratic",
        lambda _: NMZZ.FreeQuadraticModule(rank=2, inner_product_matrix=matrix(ZZ, [[2, 1], [1, 2]])) in MZZCat.WithForms().Quadratic(),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(...) has rank 2",
        lambda _: NMZZ.FreeQuadraticModule(rank=2, inner_product_matrix=matrix(ZZ, [[2, 1], [1, 2]])).rank() == 2,
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(inner_product_rows=...) records the form",
        lambda _: NMZZ.FreeQuadraticModule(rank=2, inner_product_rows=[[2, 1], [1, 2]]).inner_product_matrix()
        == matrix(ZZ, [[2, 1], [1, 2]]),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(inner_product_entries=...) records the form",
        lambda _: NMZZ.FreeQuadraticModule(rank=2, inner_product_entries=[2, 1, 1, 2]).inner_product_matrix()
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
        "base Modules(R) object surface rejects specialized module subcategory predicates",
        lambda _: base_module_surface_rejects_specialized_structure(),
    ),
    (
        "Modules(ZZ).Constructors().span(...) is a module subobject",
        lambda _: NMZZ.span([M.gen(0), M.gen(1)]) in MZZCat.Subobjects(),
    ),
    (
        "refine_category(M.submodule(...), Subobjects()) is a module subobject",
        lambda _: refine_for_membership(S, MZZCat.Subobjects()) in MZZCat.Subobjects(),
    ),
    (
        "refined M.submodule(...) has ambient module M",
        lambda _: refine_for_membership(S, MZZCat.Subobjects()).ambient_module() is M,
    ),
    (
        "refine_category(M.submodule_with_basis(...), Subobjects()+WithOrderedBasis()) has ordered basis",
        lambda _: refine_for_membership(Sb, MZZCat.WithOrderedBasis().Subobjects())
        in MZZCat.WithOrderedBasis().Subobjects(),
    ),
    (
        "refine_category(M.quotient_module(S), Quotients()) is a module quotient",
        lambda _: refine_for_membership(Qfree, MZZCat.Quotients()) in MZZCat.Quotients(),
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
        lambda _: refine_for_membership(CS, MQQCat.WithBasis().Subobjects()) in MQQCat.WithBasis().Subobjects(),
    ),
    (
        "Modules(QQ).WithBasis() records the with-basis axiom owner",
        lambda _: _WithBasis._base_category_class_and_axiom == (Modules, "WithBasis"),
    ),
    (
        "CombinatorialFreeModule basis element surfaces expose terms and coefficients",
        lambda _: C.term("a", QQ(3)) == 3 * a
        and (2 * a + 5 * b).coefficient("a") == 2
        and (2 * a + 5 * b).monomials() == [a, b],
    ),
    (
        "category constructors expose basis index and ordered basis order through refined modules",
        lambda _: list(NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis_index_set())
        == ["a", "b"]
        and NMQQ.VectorSpace(dimension=2).basis_order() == (0, 1),
    ),
    (
        "with-basis category owns abstract reduction and morphism construction surfaces",
        lambda _: abstract_method_has_name(_WithBasis.ParentMethods.reduce, "reduce")
        and abstract_method_has_name(_WithBasis.HomCategory.ParentMethods.from_basis_map, "from_basis_map"),
    ),
    (
        "with-ordered-basis category owns coordinate and echelonized matrix surfaces",
        lambda _: abstract_method_has_name(_WithOrderedBasis.ParentMethods.echelonized_basis_matrix, "echelonized_basis_matrix")
        and abstract_method_has_name(_WithOrderedBasis.ParentMethods.coordinate_vector, "coordinate_vector")
        and abstract_method_has_name(_WithOrderedBasis.ParentMethods.coordinate_module, "coordinate_module"),
    ),
    (
        "ordered-basis module Hom owns matrix construction and presentation routes",
        lambda _: abstract_method_has_name(_WithOrderedBasis.HomCategory.ParentMethods.from_matrix, "from_matrix")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.to_matrix, "to_matrix")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.base_ring, "base_ring")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.rank, "rank")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.nullity, "nullity")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.determinant, "determinant")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.trace, "trace")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.characteristic_polynomial, "characteristic_polynomial")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.factorization_of_characteristic_polynomial, "factorization_of_characteristic_polynomial")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.fcp, "fcp")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.eigenvalues, "eigenvalues")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.eigenvectors, "eigenvectors")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.eigenspaces, "eigenspaces")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ElementMethods.decomposition, "decomposition"),
    ),
    (
        "ordered-basis module Hom owns matrix-unit basis witnesses",
        lambda _: abstract_method_has_name(_WithOrderedBasis.HomCategory.ParentMethods.basis, "basis")
        and abstract_method_has_name(_WithOrderedBasis.HomCategory.ParentMethods.basis_matrix_units, "basis_matrix_units"),
    ),
    (
        "refine_category(C.quotient_module(CS), Quotients()+WithBasis()) has a basis",
        lambda _: refine_for_membership(CQ, MQQCat.WithBasis().Quotients()) in MQQCat.WithBasis().Quotients(),
    ),
    (
        "refine_category(SymmetricGroup(3).regular_representation(QQ), RepresentationModules()) is a representation module",
        lambda _: refine_for_membership(SymmetricGroup(3).regular_representation(QQ), MQQCat.RepresentationModules())
        in MQQCat.RepresentationModules(),
    ),
    (
        "refine_category(M / Wfg, FinitelyPresented().OverPID()) is finitely presented over a PID",
        lambda _: refine_for_membership(Mfg, [MZZCat.FinitelyGenerated(), MZZCat.FinitelyPresented(), MZZCat.OverPID()])
        in MZZCat.FinitelyPresented().OverPID(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FreeGradedModule(E, (-1, 3)) is free graded",
        lambda _: NME.FreeGradedModule(E, (-1, 3)) in Modules(E).FreeGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(...) is finitely presented graded",
        lambda _: NME.FPModule(algebra=E, generator_degrees=[0, 0], relations=[[xE, yE]]) in Modules(E).FinitelyPresentedGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(algebra=...) is finitely presented graded",
        lambda _: NME.FPModule(algebra=E, generator_degrees=[0, 0], relations=[[xE, yE]])
        in Modules(E).FinitelyPresentedGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(module=...) is finitely presented graded",
        lambda _: NME.FPModule(module=NME.FreeGradedModule(E, [0, 1]))
        in Modules(E).FinitelyPresentedGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(defining_map=identity) is trivial",
        lambda _: fp_module_from_identity_cokernel().is_trivial(),
    ),
    (
        "Modules(NR.GF(order=5^3, name='z')).Constructors().OreQuotientModule(S, X^2 + z) is an Ore module",
        lambda _: NMK.OreQuotientModule(Sore, X**2 + z) in Modules(K).OreModules(),
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(...) is an integer lattice",
        lambda _: NMZZ.IntegerLattice(basis=[[1, 0, 3], [0, 2, 1], [0, 2, 7]]) in MZZCat.IntegerLattices(),
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(...) has rank 3",
        lambda _: NMZZ.IntegerLattice(basis=[[1, 0, 3], [0, 2, 1], [0, 2, 7]]).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(basis=matrix(...)) has rank 3",
        lambda _: NMZZ.IntegerLattice(basis=matrix(ZZ, [[1, 0, 3], [0, 2, 1], [0, 2, 7]])).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(basis=rows) has rank 3",
        lambda _: NMZZ.IntegerLattice(basis=[[1, 0, 3], [0, 2, 1], [0, 2, 7]]).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(basis=zeta_5) has rank 4",
        lambda _: integer_lattice_from_cyclotomic_order_element().rank() == 4,
    ),
    (
        "Modules(ZZ).Constructors().TorsionQuadraticForm(...) is a torsion quadratic module",
        lambda _: NMZZ.TorsionQuadraticForm(q=matrix(QQ, [[1, QQ(1) / 2], [QQ(1) / 2, 1]]))
        in MZZCat.TorsionQuadraticModules(),
    ),
    (
        "Modules(ZZ).Constructors().TorsionQuadraticForm(q=rows) is a torsion quadratic module",
        lambda _: NMZZ.TorsionQuadraticForm(q=[[1, QQ(1) / 2], [QQ(1) / 2, 1]])
        in MZZCat.TorsionQuadraticModules(),
    ),
    (
        "Modules(ZZ).Constructors().ring_as_rank_one_module() is rank-one free",
        lambda _: NMZZ.ring_as_rank_one_module() in MZZCat.Free().FiniteRank().WithOrderedBasis(),
    ),
    (
        "Modules(Zmod(6)).Constructors().rank_one_module_with_ring_isomorphisms(basis=5) gives inverse witnesses",
        lambda _: rank_one_module_isomorphisms_are_inverse_witnesses(),
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
        "Modules(ZZ).Constructors().laurent_series_ring_as_module(power_series_ring=...) is a ring object as a module",
        lambda _: NMZZ.laurent_series_ring_as_module(power_series_ring=NR.PowerSeriesRing(base_ring=ZZ, name="u"))
        in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().puiseux_series_ring_as_module('t') is a ring object as a module",
        lambda _: NMZZ.puiseux_series_ring_as_module("t") in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().puiseux_series_ring_as_module(laurent_series_ring=...) is a ring object as a module",
        lambda _: NMZZ.puiseux_series_ring_as_module(laurent_series_ring=NR.LaurentSeriesRing(base_ring=ZZ, name="u"))
        in MZZCat.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().matrix_ring_as_module(2) is a ring object as a module",
        lambda _: NMZZ.matrix_ring_as_module(2) in MZZCat.RingObjectsAsModules(),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
