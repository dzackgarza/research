import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.algebras import Algebras, AssociativeAlgebras, MagmaticAlgebras
from category_specs.algebras.homsets import AlgebraEndCategory
from category_specs.algebras.subcategories.commutative import _CommutativeAlgebras
from category_specs.algebras.subcategories.constructions.ideals import (
    AlgebraIdealsCategory,
    AlgebraIdealsElement,
    AlgebraIdealsMorphism,
)
from category_specs.algebras.subcategories.constructions.objects_over import _ObjectsOver
from category_specs.algebras.subcategories.constructions.objects_under import _ObjectsUnder
from category_specs.algebras.subcategories.constructions.quotients import _Quotients
from category_specs.algebras.subcategories.finite_dimensional import _FiniteDimensionalAlgebras
from category_specs.algebras.subcategories.finite_dimensional_with_basis import _FiniteDimensionalAlgebrasWithBasis
from category_specs.algebras.subcategories.semisimple import _SemisimpleAlgebras
from category_specs.algebras.subcategories.with_basis import _AlgebrasWithBasis
from category_specs.cat import Cat
from category_specs.modules.homsets import RModuleHomCategory
from category_specs.sets import Sets
from category_specs.tensor_algebra_components import TensorAlgebraComponents
from category_specs.utils import assert_category_statements
from sage.all import GF, IntegerModRing, MatrixSpace, QQ, ZZ
from sage.categories.magmas import Magmas
from sage.categories.semigroups import Semigroups
from sage.groups.perm_gps.permgroup_named import CyclicPermutationGroup
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule


def A():
    return Algebras(ZZ)


def AQ():
    return Algebras(QQ)


def multiplicative_monoid_source():
    return IntegerModRing(3)


def multiplicative_group_source():
    return CyclicPermutationGroup(3)


def additive_source():
    return GF(3)


def multiplication_tensor(R):
    M = FiniteRankFreeModule(R, 2, name="M")
    e = M.basis("e")
    return TensorAlgebraComponents(R).Constructors().tensor(
        M,
        (1, 2),
        module_element_matrix=(
            (e[0], e[1]),
            (e[1], e[0]),
        ),
        basis=e,
        name="mu",
    )


def diagonal_matrix_subalgebra():
    M2 = MatrixSpace(QQ, 2)
    e00 = M2([[1, 0], [0, 0]])
    return M2.subalgebra([e00])


def matrix_space_split_ideals_route_to_sage_sides():
    M2 = MatrixSpace(QQ, 2)
    e00 = M2([[1, 0], [0, 0]])
    methods = AQ().ParentMethods
    assert methods.left_ideal(M2, [e00]).dimension() == 2
    assert methods.right_ideal(M2, [e00]).dimension() == 2
    assert methods.two_sided_ideal(M2, [e00]).dimension() == 4
    return True


def matrix_space_principal_split_ideals_route_to_sage_sides():
    M2 = MatrixSpace(QQ, 2)
    e00 = M2([[1, 0], [0, 0]])
    methods = AQ().ParentMethods
    assert methods.principal_left_ideal(M2, e00).dimension() == 2
    assert methods.principal_right_ideal(M2, e00).dimension() == 2
    assert methods.principal_two_sided_ideal(M2, e00).dimension() == 4
    return True


def abstract_method_has_name(method, name):
    return method.__name__ == name


def FreeAlgebra_records_generator_presentation():
    generators = Sets().Constructors().FiniteEnumeratedSet(["x", "y"])
    algebra = A().Constructors().FreeAlgebra(generators=generators)
    return (
        algebra in A().WithBasis()
        and algebra._category_specs_generator_set is generators
        and algebra._category_specs_generator_presentation == tuple(zip(tuple(generators), algebra.gens(), strict=True))
    )


def FreeAlgebra_recovers_sage_named_shapes():
    constructors = A().Constructors()
    by_names = constructors.FreeAlgebra(generator_names=("a", "b"), degrees=1)
    by_names_and_count = constructors.FreeAlgebra(
        generator_names=("u", "v"), generator_count=2
    )
    by_count_and_names = constructors.FreeAlgebra(
        generator_count=2, names=("p", "q")
    )
    by_count_and_name = constructors.FreeAlgebra(generator_count=2, name="z")
    return (
        by_names in A().WithBasis()
        and by_names.ngens() == 2
        and tuple(str(generator) for generator in by_names.gens()) == ("a", "b")
        and by_names_and_count in A().WithBasis()
        and by_names_and_count.ngens() == 2
        and by_count_and_names in A().WithBasis()
        and tuple(str(generator) for generator in by_count_and_names.gens())
        == ("p", "q")
        and by_count_and_name in A().WithBasis()
        and by_count_and_name.ngens() == 2
    )


CATEGORY_STATEMENTS = (
    ("Algebras(ZZ) is an object of Cat()", lambda _: A() in Cat()),
    ("Algebras(ZZ) has base ring ZZ", lambda _: A().base_ring() is ZZ),
    ("Algebras(ZZ).Commutative() is an object of Cat()", lambda _: A().Commutative() in Cat()),
    ("Algebras(ZZ).WithBasis() is an object of Cat()", lambda _: A().WithBasis() in Cat()),
    ("Algebras(ZZ).FiniteDimensional() is an object of Cat()", lambda _: A().FiniteDimensional() in Cat()),
    ("Algebras(ZZ).Semisimple() is an object of Cat()", lambda _: A().Semisimple() in Cat()),
    ("Algebras(ZZ).Commutative() is a subcategory of Algebras(ZZ)", lambda _: A().Commutative().is_subcategory(A())),
    ("Algebras(ZZ).WithBasis() is a subcategory of Algebras(ZZ)", lambda _: A().WithBasis().is_subcategory(A())),
    ("Algebras(ZZ).FiniteDimensional() is a subcategory of Algebras(ZZ)", lambda _: A().FiniteDimensional().is_subcategory(A())),
    ("Algebras(ZZ).Semisimple() is a subcategory of Algebras(ZZ)", lambda _: A().Semisimple().is_subcategory(A())),
    (
        "Algebras(ZZ) owns algebra generators and derivation surfaces",
        lambda _: abstract_method_has_name(A().ParentMethods.algebra_generators, "algebra_generators")
        and abstract_method_has_name(A().ParentMethods.derivations, "derivations"),
    ),
    (
        "algebra subcategory classes route through their canonical axiom owners",
        lambda _: Algebras.Commutative is _CommutativeAlgebras
        and Algebras.FiniteDimensional is _FiniteDimensionalAlgebras
        and Algebras.Semisimple is _SemisimpleAlgebras
        and MagmaticAlgebras.Associative is AssociativeAlgebras,
    ),
    (
        "algebras with basis own generator surface and finite-dimensional refinement",
        lambda _: Algebras.WithBasis is _AlgebrasWithBasis
        and _AlgebrasWithBasis.FiniteDimensional is _FiniteDimensionalAlgebrasWithBasis
        and abstract_method_has_name(_AlgebrasWithBasis.ParentMethods.algebra_generators, "algebra_generators"),
    ),
    (
        "semisimple algebras own their semisimplicity predicate",
        lambda _: abstract_method_has_name(_SemisimpleAlgebras.ParentMethods.is_semisimple, "is_semisimple"),
    ),
    ("Algebras(ZZ) is a subcategory of associative algebras", lambda _: A().is_subcategory(AssociativeAlgebras(ZZ))),
    (
        "AssociativeAlgebras(ZZ) is a subcategory of magmatic algebras",
        lambda _: AssociativeAlgebras(ZZ).is_subcategory(MagmaticAlgebras(ZZ)),
    ),
    ("Algebras(ZZ).Subobjects() is an object of Cat()", lambda _: A().Subobjects() in Cat()),
    ("Algebras(ZZ).Quotients() is an object of Cat()", lambda _: A().Quotients() in Cat()),
    ("Algebras(ZZ).Subquotients() is an object of Cat()", lambda _: A().Subquotients() in Cat()),
    ("Algebras(ZZ).CartesianProducts() is an object of Cat()", lambda _: A().CartesianProducts() in Cat()),
    ("Algebras(ZZ).TensorProducts() is an object of Cat()", lambda _: A().TensorProducts() in Cat()),
    ("Algebras(ZZ).DualObjects() is an object of Cat()", lambda _: A().DualObjects() in Cat()),
    ("Algebras(ZZ).HomCategory() is an object of Cat()", lambda _: A().HomCategory() in Cat()),
    (
        "algebra end categories own their base-algebra surface",
        lambda _: abstract_method_has_name(AlgebraEndCategory.ParentMethods.base_algebra, "base_algebra"),
    ),
    ("Algebras(ZZ).ParentMethods.subalgebra is admitted", lambda _: A().ParentMethods.subalgebra),
    (
        "algebra slices own structure-algebra surfaces",
        lambda _: abstract_method_has_name(_ObjectsOver.ParentMethods.structure_algebra, "structure_algebra")
        and abstract_method_has_name(_ObjectsUnder.ParentMethods.structure_algebra, "structure_algebra"),
    ),
    (
        "algebra quotients own quotient projection surface",
        lambda _: abstract_method_has_name(_Quotients.ParentMethods.quotient_projection, "quotient_projection"),
    ),
    (
        "algebra ideals own two-sided predicate and standard type package surfaces",
        lambda _: abstract_method_has_name(AlgebraIdealsCategory.ParentMethods.is_two_sided_ideal, "is_two_sided_ideal")
        and AlgebraIdealsElement is AlgebraIdealsCategory.ElementMethods
        and AlgebraIdealsMorphism is RModuleHomCategory.ElementMethods,
    ),
    (
        "MatrixSpace(QQ, 2).subalgebra([e00]) is the two-dimensional algebra generated by 1 and e00",
        lambda _: diagonal_matrix_subalgebra().dimension() == 2,
    ),
    (
        "Algebras(QQ).ParentMethods split ideals route to Sage side values on MatrixSpace(QQ, 2)",
        lambda _: matrix_space_split_ideals_route_to_sage_sides(),
    ),
    (
        "Algebras(QQ).ParentMethods principal split ideals route to Sage side values on MatrixSpace(QQ, 2)",
        lambda _: matrix_space_principal_split_ideals_route_to_sage_sides(),
    ),
    (
        "Algebras(ZZ).Constructors().FreeAlgebra(generators={x, y}) is an algebra with basis",
        lambda _: FreeAlgebra_records_generator_presentation(),
    ),
    (
        "Algebras(ZZ).Constructors().FreeAlgebra(...) recovers Sage name/count shapes",
        lambda _: FreeAlgebra_recovers_sage_named_shapes(),
    ),
    (
        "MagmaticAlgebras(ZZ).Constructors().algebra(magma=...) routes to project magmatic algebras",
        lambda _: MagmaticAlgebras(ZZ).Constructors().algebra(magma=Magmas().example()) in MagmaticAlgebras(ZZ),
    ),
    (
        "AssociativeAlgebras(ZZ).Constructors().algebra(semigroup=...) routes to project associative nonunital algebras",
        lambda _: AssociativeAlgebras(ZZ).Constructors().algebra(semigroup=Semigroups().example()) in AssociativeAlgebras(ZZ),
    ),
    (
        "Algebras(ZZ).Constructors().algebra(monoid=Z/3Z) executes the Sage monoid-algebra route",
        lambda _: A().Constructors().algebra(monoid=multiplicative_monoid_source()) in A().WithBasis(),
    ),
    (
        "Algebras(ZZ).Constructors().GroupAlgebra(group=C3) executes the Sage group-algebra route",
        lambda _: A().Constructors().GroupAlgebra(group=multiplicative_group_source()) in A().WithBasis(),
    ),
    (
        "AssociativeAlgebras(ZZ).Constructors().algebra(additive_semigroup=...) routes to project associative nonunital algebras",
        lambda _: AssociativeAlgebras(ZZ).Constructors().algebra(additive_semigroup=additive_source()) in AssociativeAlgebras(ZZ),
    ),
    (
        "Algebras(ZZ).Constructors().algebra(additive_monoid=GF(3), +) executes the Sage additive-monoid route",
        lambda _: A().Constructors().algebra(additive_monoid=additive_source()) in A().WithBasis(),
    ),
    (
        "Algebras(ZZ).Constructors().algebra(additive_group=GF(3), +) executes the Sage additive-group route",
        lambda _: A().Constructors().algebra(additive_group=additive_source()) in A().WithBasis(),
    ),
    (
        "MagmaticAlgebras(QQ).Constructors().FiniteDimensionalAlgebra(multiplication=...) builds a finite-dimensional algebra parent",
        lambda _: MagmaticAlgebras(QQ).Constructors().FiniteDimensionalAlgebra(multiplication=multiplication_tensor(QQ)) in AQ().WithBasis().FiniteDimensional(),
    ),
    (
        "MagmaticAlgebras(ZZ).Constructors().FiniteDimensionalAlgebra(multiplication=...) builds a finite-rank algebra parent",
        lambda _: MagmaticAlgebras(ZZ).Constructors().FiniteDimensionalAlgebra(multiplication=multiplication_tensor(ZZ)) in MagmaticAlgebras(ZZ),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
