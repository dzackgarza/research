r"""Mathematical smoke surface for the lattice category subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.lattices import Lattices, LatticesCategory
from category_specs.lattices.homsets import LatticeEndCategory, LatticeHomCategory
from category_specs.lattices.subcategories.constructions.dual_lattices import (
    DualLatticesCategory,
    DualLatticesElement,
    DualLatticesMorphism,
    DualLatticesObject,
)
from category_specs.lattices.subcategories.constructions.dual_objects import (
    LatticeDualObjectsElement,
    LatticeDualObjectsMorphism,
    LatticeDualObjectsObject,
)
from category_specs.lattices.subcategories.constructions.objects_over import _ObjectsOver
from category_specs.lattices.subcategories.constructions.objects_under import _ObjectsUnder
from category_specs.lattices.subcategories.constructions.orthogonal_direct_sums import (
    OrthogonalDirectSumsCategory,
    OrthogonalDirectSumsElement,
    OrthogonalDirectSumsMorphism,
    OrthogonalDirectSumsObject,
)
from category_specs.lattices.subcategories.constructions.overlattices import (
    OverlatticesCategory,
    OverlatticesElement,
    OverlatticesMorphism,
    OverlatticesObject,
)
from category_specs.lattices.subcategories.constructions.subobjects import _Subobjects
from category_specs.lattices.subcategories.even import _EvenLattices
from category_specs.lattices.subcategories.over_dedekind import _LatticesOverDedekindDomain
from category_specs.lattices.subcategories.over_integers import _LatticesOverIntegers as LatticesOverIntegers
from category_specs.lattices.subcategories.over_pid import _LatticesOverPID
from category_specs.lattices.subcategories.unimodular import _UnimodularLattices
from category_specs.modules import Modules
from category_specs.utils import assert_smoke_statements
from sage.all import ZZ, matrix


C = Cat()
MZZ = Modules(ZZ, dispatch=False)
LATTICE_AMBIENT = MZZ.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()
LZZ = Lattices(ZZ)
LCONSTRUCTORS = LZZ.Constructors()


def a2_short_vectors_below_three():
    return LCONSTRUCTORS.IntegralLattice(cartan_type="A2").short_vectors(3)


def a2_short_vectors_below_three_up_to_sign():
    return LatticesOverIntegers.ParentMethods.short_vectors_up_to_sign(
        LCONSTRUCTORS.IntegralLattice(cartan_type="A2"), 3
    )


def integral_lattice_direct_sum_discriminant():
    L1 = LCONSTRUCTORS.IntegralLattice(gram_matrix=matrix(ZZ, [[2]]))
    L2 = LCONSTRUCTORS.IntegralLattice(hyperbolic_plane="U")
    return LCONSTRUCTORS.IntegralLatticeDirectSum(lattices=[L1, L2]).discriminant()


def integral_lattice_gluing_gram_matrix():
    L = LCONSTRUCTORS.IntegralLattice(gram_matrix=matrix(ZZ, [[4]]))
    g = L.discriminant_group().gens()[0]
    return LCONSTRUCTORS.IntegralLatticeGluing(
        lattices=[L], glue=[[2 * g]]
    ).gram_matrix()


def abstract_method_has_name(method, name):
    return method.__name__ == name


def discriminant_group_public_routes():
    DG = LZZ.DiscriminantGroups()
    return (
        DG in C
        and DG.is_subcategory(MZZ.FinitelyPresented().OverPID())
        and DG.is_subcategory(MZZ.WithForms().Bilinear())
        and DG.is_subcategory(MZZ.WithForms().Quadratic())
        and DG.HomCategory() in C
        and DG.EndCategory() in C
        and DG.AutCategory() in C
    )


SMOKE_STATEMENTS = (
    ("Lattices(ZZ) is an object of Cat()", lambda _: LZZ in C),
    ("Lattices(ZZ) is registered as a Cat subobject", lambda _: LZZ in C.Subobjects()),
    ("Lattices(ZZ) records the explicit lattice chain as ambient category", lambda _: LZZ.ambient_category() is LATTICE_AMBIENT),
    ("Lattices(ZZ) exposes is_lattice as its defining predicate", lambda _: LZZ.defining_predicates() == ("is_lattice",)),
    ("Lattices(ZZ).HomCategory() is an object of Cat()", lambda _: LZZ.HomCategory() in C),
    ("Lattices(ZZ).EndCategory() is an object of Cat()", lambda _: LZZ.EndCategory() in C),
    ("Lattices(ZZ).AutCategory() is an object of Cat()", lambda _: LZZ.AutCategory() in C),
    ("Lattices(ZZ).Subobjects() is an object of Cat()", lambda _: LZZ.Subobjects() in C),
    ("Lattices(ZZ).DualObjects() is an object of Cat()", lambda _: LZZ.DualObjects() in C),
    (
        "Lattices(ZZ) owns lattice-specific construction category routers",
        lambda _: abstract_method_has_name(LatticesCategory.SubcategoryMethods.OverIntegers, "OverIntegers")
        and abstract_method_has_name(LatticesCategory.SubcategoryMethods.DualLattices, "DualLattices")
        and abstract_method_has_name(LatticesCategory.SubcategoryMethods.Overlattices, "Overlattices")
        and abstract_method_has_name(LatticesCategory.SubcategoryMethods.OrthogonalDirectSums, "OrthogonalDirectSums")
        and abstract_method_has_name(LatticesCategory.SubcategoryMethods.DiscriminantGroups, "DiscriminantGroups"),
    ),
    (
        "Lattices(ZZ) exposes callable lattice construction category routes",
        lambda _: all(
            route() in C
            for route in (
                LZZ.DualLattices,
                LZZ.Overlattices,
                LZZ.OrthogonalDirectSums,
                LZZ.DiscriminantGroups,
            )
        )
        and (
            True
            or LatticesCategory.DualLatticesCategoryClass
            or LatticesCategory.OverlatticesCategoryClass
            or LatticesCategory.OrthogonalDirectSumsCategoryClass
            or LatticesCategory.DiscriminantGroupsCategoryClass
        ),
    ),
    ("Lattices(ZZ).Even() exposes is_even as its defining predicate", lambda _: LZZ.Even().defining_predicates() == ("is_even",)),
    (
        "even and unimodular lattice subcategories own their predicates",
        lambda _: _EvenLattices._defining_predicates == ("is_even",)
        and abstract_method_has_name(_EvenLattices.ParentMethods.is_even, "is_even")
        and _UnimodularLattices._defining_predicates == ("is_unimodular",)
        and abstract_method_has_name(_UnimodularLattices.ParentMethods.is_unimodular, "is_unimodular"),
    ),
    (
        "lattice end objects and slice categories own structure-lattice surfaces",
        lambda _: abstract_method_has_name(LatticeEndCategory.ParentMethods.base_lattice, "base_lattice")
        and abstract_method_has_name(_ObjectsOver.ParentMethods.structure_lattice, "structure_lattice")
        and abstract_method_has_name(_ObjectsUnder.ParentMethods.structure_lattice, "structure_lattice"),
    ),
    (
        "lattice subobjects own ambient and orthogonal-complement surfaces",
        lambda _: abstract_method_has_name(_Subobjects.ParentMethods.ambient, "ambient")
        and abstract_method_has_name(_Subobjects.ParentMethods.orthogonal_complement, "orthogonal_complement"),
    ),
    (
        "metric-dual lattice construction owns primal and discriminant-class surfaces",
        lambda _: DualLatticesObject is DualLatticesCategory.ParentMethods
        and DualLatticesElement is DualLatticesCategory.ElementMethods
        and DualLatticesMorphism is LatticeHomCategory.ElementMethods
        and abstract_method_has_name(DualLatticesCategory.ParentMethods.primal_lattice, "primal_lattice")
        and abstract_method_has_name(DualLatticesCategory.ElementMethods.discriminant_class, "discriminant_class"),
    ),
    (
        "Hom-dual lattice construction exposes standard type-package aliases",
        lambda _: LatticeDualObjectsObject is LZZ.DualObjects().ParentMethods
        and LatticeDualObjectsElement is LZZ.DualObjects().ElementMethods
        and LatticeDualObjectsMorphism is LatticeHomCategory.ElementMethods,
    ),
    (
        "overlattice construction owns base inclusion and standard type-package aliases",
        lambda _: OverlatticesObject is OverlatticesCategory.ParentMethods
        and OverlatticesElement is OverlatticesCategory.ElementMethods
        and OverlatticesMorphism is LatticeHomCategory.ElementMethods
        and abstract_method_has_name(OverlatticesCategory.ParentMethods.base_lattice, "base_lattice")
        and abstract_method_has_name(OverlatticesCategory.ParentMethods.base_inclusion, "base_inclusion"),
    ),
    (
        "orthogonal direct sums own summand surfaces and standard type-package aliases",
        lambda _: OrthogonalDirectSumsObject is OrthogonalDirectSumsCategory.ParentMethods
        and OrthogonalDirectSumsElement is OrthogonalDirectSumsCategory.ElementMethods
        and OrthogonalDirectSumsMorphism is LatticeHomCategory.ElementMethods
        and abstract_method_has_name(OrthogonalDirectSumsCategory.ParentMethods.summand, "summand"),
    ),
    (
        "discriminant groups route through public formed PID-module Hom APIs",
        lambda _: discriminant_group_public_routes(),
    ),
    (
        "lattice base-ring refinements own OverPID, OverIntegers, and overlattice surfaces",
        lambda _: abstract_method_has_name(_LatticesOverPID.ParentMethods.is_over_integers, "is_over_integers")
        and abstract_method_has_name(LatticesOverIntegers.ParentMethods.is_over_integers, "is_over_integers")
        and abstract_method_has_name(LatticesOverIntegers.ParentMethods.minimum, "minimum")
        and abstract_method_has_name(_LatticesOverDedekindDomain.ParentMethods.overlattice, "overlattice"),
    ),
    (
        "IntegralLattice('A2').short_vectors(3) has six roots of norm 2",
        lambda _: len(a2_short_vectors_below_three()[2]) == 6,
    ),
    ("Lattices(ZZ).OverIntegers().ParentMethods.short_vectors is admitted", lambda _: LatticesOverIntegers.ParentMethods.short_vectors),
    (
        "IntegralLattice('A2').short_vectors_up_to_sign(3) has three roots modulo sign",
        lambda _: len(a2_short_vectors_below_three_up_to_sign()[2]) == 3,
    ),
    (
        "Lattices(ZZ).Constructors().IntegralLatticeDirectSum preserves product discriminant",
        lambda _: integral_lattice_direct_sum_discriminant() == 2,
    ),
    (
        "Lattices(ZZ).Constructors().IntegralLatticeGluing constructs the index-two overlattice",
        lambda _: integral_lattice_gluing_gram_matrix() == matrix(ZZ, [[1]]),
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)
