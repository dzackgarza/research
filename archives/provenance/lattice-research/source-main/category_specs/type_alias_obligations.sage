r"""Category obligation examples for centralized category-spec type aliases."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.utils import assert_category_statements
from category_specs.types import (
    AlgebraTypes,
    ApproximateRing,
    ApproximateRingCategory,
    ApproximateRingElement,
    ApproximateRingMorphism,
    AssociativeAlgebra,
    AssociativeAlgebraCategory,
    AssociativeAlgebraElement,
    AssociativeAlgebraMorphism,
    AssociativeAlgebraTypes,
    AutCategoryTypes,
    BilinearModule,
    BilinearModuleAut,
    BilinearModuleAutCategory,
    BilinearModuleAutomorphism,
    BilinearModuleCategory,
    BilinearModuleElement,
    BilinearModuleEnd,
    BilinearModuleEndCategory,
    BilinearModuleEndomorphism,
    BilinearModuleHom,
    BilinearModuleHomCategory,
    BilinearModuleMorphism,
    BilinearModuleTypes,
    CatTypes,
    ClosedSubset,
    DiscriminantGroupAut,
    DiscriminantGroupAutCategory,
    DiscriminantGroupAutomorphism,
    DiscriminantGroupCategory,
    DiscriminantGroupEnd,
    DiscriminantGroupEndCategory,
    DiscriminantGroupEndomorphism,
    DiscriminantGroupHom,
    DiscriminantGroupHomCategory,
    DiscriminantGroupMorphism,
    DiscriminantGroupTypes,
    EndCategoryTypes,
    FormedModule,
    FormedModuleAut,
    FormedModuleAutCategory,
    FormedModuleAutomorphism,
    FormedModuleCategory,
    FormedModuleElement,
    FormedModuleEnd,
    FormedModuleEndCategory,
    FormedModuleEndomorphism,
    FormedModuleHom,
    FormedModuleHomCategory,
    FormedModuleMorphism,
    FormedModuleTypes,
    GSet,
    GradedSet,
    GroupAction,
    HomCategoryTypes,
    InfiniteSet,
    IsomorphicSetObject,
    JoinSemilatticePoset,
    LatticeAut,
    LatticeCategory,
    LatticeEnd,
    LatticeEndomorphism,
    LatticeHom,
    LatticeIsometry,
    LatticeTypes,
    MagmaticAlgebra,
    MagmaticAlgebraCategory,
    MagmaticAlgebraElement,
    MagmaticAlgebraMorphism,
    MagmaticAlgebraTypes,
    MeetSemilatticePoset,
    MetricSpace,
    MetricSpaceTypes,
    OrthogonalAutomorphism,
    PartitionedSetAut,
    PartitionedSetAutCategory,
    PartitionedSetAutomorphism,
    PartitionedSetCategory,
    PartitionedSetElement,
    PartitionedSetEnd,
    PartitionedSetEndCategory,
    PartitionedSetEndomorphism,
    PartitionedSetHom,
    PartitionedSetHomCategory,
    PartitionedSetMorphism,
    PosetAut,
    PosetEnd,
    PosetHom,
    PosetTypes,
    PrimesInArithmeticProgressions,
    QuadraticModule,
    QuadraticModuleAut,
    QuadraticModuleAutCategory,
    QuadraticModuleAutomorphism,
    QuadraticModuleCategory,
    QuadraticModuleElement,
    QuadraticModuleEnd,
    QuadraticModuleEndCategory,
    QuadraticModuleEndomorphism,
    QuadraticModuleHom,
    QuadraticModuleHomCategory,
    QuadraticModuleMorphism,
    QuadraticModuleTypes,
    RModAut,
    RModDual,
    RModDualElement,
    RModDualMorphism,
    RModEnd,
    RModHom,
    RModuleAut,
    RModuleAutomorphism,
    RModuleDual,
    RModuleDualElement,
    RModuleDualMorphism,
    RModuleEnd,
    RModuleEndomorphism,
    RModuleTypes,
    RealNumberInterval,
    RingAutomorphism,
    RingEndomorphism,
    RingTypes,
    SetAut,
    SetAutomorphism,
    SetEnd,
    SetEndomorphism,
    SetHom,
    SetPartitionsParent,
    SetSubquotient,
    SetTypes,
    SubModule,
    Submodule,
    TensorAlgebraComponentTypes,
    TopologicalSpaceMorphism,
    TopologicalSpaceTypes,
    TorsionQuadraticModule,
    TorsionQuadraticModuleAut,
    TorsionQuadraticModuleAutCategory,
    TorsionQuadraticModuleAutomorphism,
    TorsionQuadraticModuleCategory,
    TorsionQuadraticModuleElement,
    TorsionQuadraticModuleEnd,
    TorsionQuadraticModuleEndCategory,
    TorsionQuadraticModuleEndomorphism,
    TorsionQuadraticModuleHom,
    TorsionQuadraticModuleHomCategory,
    TorsionQuadraticModuleMorphism,
    TorsionQuadraticModuleTypes,
    UncountableSet,
)


def package_matches(types_package, expected):
    r"""Return whether ``types_package`` exposes the standard expected anchors."""
    return all(getattr(types_package, key) is value for key, value in expected.items())


CATEGORY_STATEMENTS = (
    (
        "module aliases preserve RMod/RModule spelling equivalences",
        lambda _: RModHom is RModuleTypes.Hom
        and RModEnd is RModuleEnd
        and RModAut is RModuleAut
        and RModuleEndomorphism is RModuleTypes.Endomorphism
        and RModuleAutomorphism is RModuleTypes.Automorphism
        and RModDual is RModuleDual
        and RModDualElement is RModuleDualElement
        and RModDualMorphism is RModuleDualMorphism,
    ),
    ("Submodule is the conventional spelling of SubModule", lambda _: Submodule is SubModule),
    (
        "ring aliases preserve endomorphism and automorphism names",
        lambda _: RingEndomorphism is RingTypes.Endomorphism and RingAutomorphism is RingTypes.Automorphism,
    ),
    (
        "approximate ring aliases expose the approximate ring package",
        lambda _: (ApproximateRingCategory, ApproximateRing, ApproximateRingElement, ApproximateRingMorphism)
        == (ApproximateRingCategory, ApproximateRing, ApproximateRingElement, ApproximateRingMorphism),
    ),
    (
        "formed module type package matches centralized aliases",
        lambda _: package_matches(
            FormedModuleTypes,
            {
                "Category": FormedModuleCategory,
                "Object": FormedModule,
                "Element": FormedModuleElement,
                "Morphism": FormedModuleMorphism,
                "HomCategory": FormedModuleHomCategory,
                "EndCategory": FormedModuleEndCategory,
                "AutCategory": FormedModuleAutCategory,
                "Hom": FormedModuleHom,
                "End": FormedModuleEnd,
                "Aut": FormedModuleAut,
                "Endomorphism": FormedModuleEndomorphism,
                "Automorphism": FormedModuleAutomorphism,
            },
        ),
    ),
    (
        "bilinear module type package matches centralized aliases",
        lambda _: package_matches(
            BilinearModuleTypes,
            {
                "Category": BilinearModuleCategory,
                "Object": BilinearModule,
                "Element": BilinearModuleElement,
                "Morphism": BilinearModuleMorphism,
                "HomCategory": BilinearModuleHomCategory,
                "EndCategory": BilinearModuleEndCategory,
                "AutCategory": BilinearModuleAutCategory,
                "Hom": BilinearModuleHom,
                "End": BilinearModuleEnd,
                "Aut": BilinearModuleAut,
                "Endomorphism": BilinearModuleEndomorphism,
                "Automorphism": BilinearModuleAutomorphism,
            },
        ),
    ),
    (
        "quadratic module type package matches centralized aliases",
        lambda _: package_matches(
            QuadraticModuleTypes,
            {
                "Category": QuadraticModuleCategory,
                "Object": QuadraticModule,
                "Element": QuadraticModuleElement,
                "Morphism": QuadraticModuleMorphism,
                "HomCategory": QuadraticModuleHomCategory,
                "EndCategory": QuadraticModuleEndCategory,
                "AutCategory": QuadraticModuleAutCategory,
                "Hom": QuadraticModuleHom,
                "End": QuadraticModuleEnd,
                "Aut": QuadraticModuleAut,
                "Endomorphism": QuadraticModuleEndomorphism,
                "Automorphism": QuadraticModuleAutomorphism,
            },
        ),
    ),
    (
        "torsion quadratic module type package matches centralized aliases",
        lambda _: package_matches(
            TorsionQuadraticModuleTypes,
            {
                "Category": TorsionQuadraticModuleCategory,
                "Object": TorsionQuadraticModule,
                "Element": TorsionQuadraticModuleElement,
                "Morphism": TorsionQuadraticModuleMorphism,
                "HomCategory": TorsionQuadraticModuleHomCategory,
                "EndCategory": TorsionQuadraticModuleEndCategory,
                "AutCategory": TorsionQuadraticModuleAutCategory,
                "Hom": TorsionQuadraticModuleHom,
                "End": TorsionQuadraticModuleEnd,
                "Aut": TorsionQuadraticModuleAut,
                "Endomorphism": TorsionQuadraticModuleEndomorphism,
                "Automorphism": TorsionQuadraticModuleAutomorphism,
            },
        ),
    ),
    (
        "algebra refinement packages expose magmatic and associative anchors",
        lambda _: package_matches(
            MagmaticAlgebraTypes,
            {
                "Category": MagmaticAlgebraCategory,
                "Object": MagmaticAlgebra,
                "Element": MagmaticAlgebraElement,
                "Morphism": MagmaticAlgebraMorphism,
            },
        )
        and package_matches(
            AssociativeAlgebraTypes,
            {
                "Category": AssociativeAlgebraCategory,
                "Object": AssociativeAlgebra,
                "Element": AssociativeAlgebraElement,
                "Morphism": AssociativeAlgebraMorphism,
            },
        )
        and AlgebraTypes.Category is not None,
    ),
    (
        "set aliases expose set refinements and Hom/End/Aut spellings",
        lambda _: InfiniteSet is SetTypes.Category.Infinite.ParentMethods
        and UncountableSet is SetTypes.Category.Uncountable.ParentMethods
        and GradedSet is not SetTypes.Object
        and SetHom is SetTypes.Hom
        and SetEnd is SetTypes.End
        and SetAut is SetTypes.Aut
        and SetEndomorphism is SetTypes.Endomorphism
        and SetAutomorphism is SetTypes.Automorphism,
    ),
    (
        "partitioned-set aliases expose the standard package",
        lambda _: PartitionedSetElement is not PartitionedSetMorphism
        and PartitionedSetHom is not PartitionedSetEnd
        and PartitionedSetAut is not PartitionedSetEnd
        and PartitionedSetEndomorphism is not PartitionedSetAutomorphism
        and PartitionedSetHomCategory is not PartitionedSetEndCategory
        and PartitionedSetAutCategory is not PartitionedSetEndCategory
        and PartitionedSetCategory is not None,
    ),
    (
        "set construction aliases preserve their mathematical names",
        lambda _: ClosedSubset is SetTypes.Category.Subobjects.ParentMethods
        and SetSubquotient is SetTypes.Category.Subquotients.ParentMethods
        and IsomorphicSetObject is not None
        and SetPartitionsParent is not None
        and GroupAction is not None
        and GSet is not None,
    ),
    (
        "topological aliases expose metric and morphism anchors",
        lambda _: MetricSpace is MetricSpaceTypes.Object
        and TopologicalSpaceMorphism is TopologicalSpaceTypes.Morphism
        and RealNumberInterval is not None
        and PrimesInArithmeticProgressions is not None,
    ),
    (
        "poset aliases expose Hom/End/Aut and semilattice anchors",
        lambda _: PosetHom is PosetTypes.Hom
        and PosetEnd is PosetTypes.End
        and PosetAut is PosetTypes.Aut
        and MeetSemilatticePoset is not None
        and JoinSemilatticePoset is not None,
    ),
    (
        "lattice aliases expose Hom/End/Aut and orthogonal spellings",
        lambda _: LatticeCategory is LatticeTypes.Category
        and LatticeHom is LatticeTypes.Hom
        and LatticeEnd is LatticeTypes.End
        and LatticeEndomorphism is LatticeTypes.Endomorphism
        and OrthogonalAutomorphism is RModuleTypes.Automorphism
        and LatticeIsometry is LatticeTypes.Automorphism,
    ),
    (
        "discriminant-group type package matches centralized aliases",
        lambda _: package_matches(
            DiscriminantGroupTypes,
            {
                "Category": DiscriminantGroupCategory,
                "Object": DiscriminantGroupTypes.Object,
                "Element": DiscriminantGroupTypes.Element,
                "Morphism": DiscriminantGroupMorphism,
                "HomCategory": DiscriminantGroupHomCategory,
                "EndCategory": DiscriminantGroupEndCategory,
                "AutCategory": DiscriminantGroupAutCategory,
                "Hom": DiscriminantGroupHom,
                "End": DiscriminantGroupEnd,
                "Aut": DiscriminantGroupAut,
                "Endomorphism": DiscriminantGroupEndomorphism,
                "Automorphism": DiscriminantGroupAutomorphism,
            },
        ),
    ),
    (
        "generic type packages expose Object anchors",
        lambda _: CatTypes.Object is not None
        and HomCategoryTypes.Object is not None
        and EndCategoryTypes.Object is not None
        and AutCategoryTypes.Object is not None
        and TensorAlgebraComponentTypes.Object is not None,
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
