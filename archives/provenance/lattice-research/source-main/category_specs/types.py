"""Centralized type aliases for the category specification hierarchy.

Category modules publish their standard mathematical type packages locally.
This file imports those packages and chooses conventional aliases such as
``Ring = RingsObject`` or ``RModule = ModulesObject``.
"""

from collections.abc import Mapping, Sequence
from types import SimpleNamespace

from sage.categories.cartesian_product import (
    CartesianProductFunctor as SageCartesianProductFunctor,
)
from sage.categories.homset import Homset as SageHomset
from sage.categories.morphism import Morphism as SageMorphism
from sage.combinat.partition import Partition as SageIntegerPartition
from sage.combinat.posets.posets import FinitePoset as SagePoset
from sage.combinat.set_partition import SetPartition as SageSetPartition
from sage.combinat.set_partition import SetPartitions as SageSetPartitions
from sage.graphs.digraph import DiGraph as SageDiGraph
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.group import Group as SageGroup
from sage.homology.free_resolution import FreeResolution as SageFreeResolution
from sage.homology.hochschild_complex import HochschildComplex
from sage.matrix.matrix2 import Matrix as SageMatrix
from sage.matrix.matrix_space import MatrixSpace as SageMatrixSpace
from sage.monoids.monoid import Monoid_class
from sage.rings.complex_interval import ComplexIntervalFieldElement
from sage.rings.infinity import InfinityElement
from sage.rings.integer import Integer
from sage.rings.polynomial.ore_polynomial_ring import (
    OrePolynomialRing as SageOrePolynomialRing,
)
from sage.rings.polynomial.polynomial_element import Polynomial as SagePolynomial
from sage.rings.polynomial.term_order import TermOrder as SageTermOrder
from sage.rings.qqbar import AlgebraicPolynomialTracker
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.real_mpfr import RealNumber as SageRealNumber
from sage.rings.valuation.valuation import DiscretePseudoValuation
from sage.sets.family import AbstractFamily
from sage.sets.finite_set_map_cy import FiniteSetMap_MN
from sage.sets.real_set import InternalRealInterval
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent as SageParent
from sympy.sets.sets import Set as SageSympySet

from .algebras import (
    AlgebrasAut,
    AlgebrasAutCategory,
    AlgebrasAutomorphism,
    AlgebrasCategory,
    AlgebrasElement,
    AlgebrasEnd,
    AlgebrasEndCategory,
    AlgebrasEndomorphism,
    AlgebrasHom,
    AlgebrasHomCategory,
    AlgebrasMorphism,
    AlgebrasObject,
    AssociativeAlgebrasCategory,
    AssociativeAlgebrasElement,
    AssociativeAlgebrasMorphism,
    AssociativeAlgebrasObject,
    MagmaticAlgebrasCategory,
    MagmaticAlgebrasElement,
    MagmaticAlgebrasMorphism,
    MagmaticAlgebrasObject,
)
from .algebras.subcategories.constructions.ideals import AlgebraIdealsObject
from .cat import (
    CatAut,
    CatAutCategory,
    CatAutomorphism,
    CatCategory,
    CatElement,
    CatEnd,
    CatEndCategory,
    CatEndomorphism,
    CatHom,
    CatHomCategory,
    CatMorphism,
    CatObject,
)
from .cat import (
    Category as CatBaseCategory,
)
from .forms import (
    BilinearModulesAut,
    BilinearModulesAutCategory,
    BilinearModulesAutomorphism,
    BilinearModulesCategory,
    BilinearModulesElement,
    BilinearModulesEnd,
    BilinearModulesEndCategory,
    BilinearModulesEndomorphism,
    BilinearModulesHom,
    BilinearModulesHomCategory,
    BilinearModulesMorphism,
    BilinearModulesObject,
    FormedModulesAut,
    FormedModulesAutCategory,
    FormedModulesAutomorphism,
    FormedModulesCategory,
    FormedModulesElement,
    FormedModulesEnd,
    FormedModulesEndCategory,
    FormedModulesEndomorphism,
    FormedModulesHom,
    FormedModulesHomCategory,
    FormedModulesMorphism,
    FormedModulesObject,
    QuadraticModulesAut,
    QuadraticModulesAutCategory,
    QuadraticModulesAutomorphism,
    QuadraticModulesCategory,
    QuadraticModulesElement,
    QuadraticModulesEnd,
    QuadraticModulesEndCategory,
    QuadraticModulesEndomorphism,
    QuadraticModulesHom,
    QuadraticModulesHomCategory,
    QuadraticModulesMorphism,
    QuadraticModulesObject,
    TorsionQuadraticModulesAut,
    TorsionQuadraticModulesAutCategory,
    TorsionQuadraticModulesAutomorphism,
    TorsionQuadraticModulesCategory,
    TorsionQuadraticModulesElement,
    TorsionQuadraticModulesEnd,
    TorsionQuadraticModulesEndCategory,
    TorsionQuadraticModulesEndomorphism,
    TorsionQuadraticModulesHom,
    TorsionQuadraticModulesHomCategory,
    TorsionQuadraticModulesMorphism,
    TorsionQuadraticModulesObject,
)
from .homsets import (
    AutCategoriesCategory,
    AutCategoriesElement,
    AutCategoriesMorphism,
    AutCategoriesObject,
    EndCategoriesCategory,
    EndCategoriesElement,
    EndCategoriesMorphism,
    EndCategoriesObject,
    HomCategoriesCategory,
    HomCategoriesElement,
    HomCategoriesMorphism,
    HomCategoriesObject,
)
from .lattices import (
    LatticesAut,
    LatticesAutCategory,
    LatticesAutomorphism,
    LatticesCategory,
    LatticesElement,
    LatticesEnd,
    LatticesEndCategory,
    LatticesEndomorphism,
    LatticesHom,
    LatticesHomCategory,
    LatticesMorphism,
    LatticesObject,
)
from .lattices.subcategories.constructions.discriminant_groups import (
    LatticeDiscriminantGroupsAut,
    LatticeDiscriminantGroupsAutCategory,
    LatticeDiscriminantGroupsAutomorphism,
    LatticeDiscriminantGroupsCategory,
    LatticeDiscriminantGroupsElement,
    LatticeDiscriminantGroupsEnd,
    LatticeDiscriminantGroupsEndCategory,
    LatticeDiscriminantGroupsEndomorphism,
    LatticeDiscriminantGroupsHom,
    LatticeDiscriminantGroupsHomCategory,
    LatticeDiscriminantGroupsMorphism,
    LatticeDiscriminantGroupsObject,
)
from .modules import (
    ModulesAut,
    ModulesAutCategory,
    ModulesAutomorphism,
    ModulesCategory,
    ModulesElement,
    ModulesEnd,
    ModulesEndCategory,
    ModulesEndomorphism,
    ModulesHom,
    ModulesHomCategory,
    ModulesMorphism,
    ModulesObject,
)
from .modules.subcategories.constructions.dual_objects import (
    _DualObjects as ModuleDualObjects,
)
from .modules.subcategories.constructions.quotients import (
    _Quotients as ModuleQuotients,
)
from .modules.subcategories.constructions.subobjects import (
    _Subobjects as ModuleSubobjects,
)
from .modules.subcategories.constructions.tensor_products import (
    _TensorProducts as ModuleTensorProducts,
)
from .modules.subcategories.free import _Free
from .modules.subcategories.projective import _Projective
from .modules.subcategories.torsion import _Torsion
from .posets import (
    PosetsAut,
    PosetsAutCategory,
    PosetsAutomorphism,
    PosetsCategory,
    PosetsElement,
    PosetsEnd,
    PosetsEndCategory,
    PosetsEndomorphism,
    PosetsHom,
    PosetsHomCategory,
    PosetsMorphism,
    PosetsObject,
)
from .posets.subcategories.finite_join_semilattice import _FiniteJoinSemilatticePosets
from .posets.subcategories.finite_lattice import _FiniteLatticePosets
from .posets.subcategories.finite_meet_semilattice import _FiniteMeetSemilatticePosets
from .posets.subcategories.join_semilattice import _JoinSemilatticePosets
from .posets.subcategories.lattice import _LatticePosets
from .posets.subcategories.meet_semilattice import _MeetSemilatticePosets
from .rings import (
    RingsAut,
    RingsAutCategory,
    RingsAutomorphism,
    RingsCategory,
    RingsElement,
    RingsEnd,
    RingsEndCategory,
    RingsEndomorphism,
    RingsHom,
    RingsHomCategory,
    RingsMorphism,
    RingsObject,
    _RingIdealParentMethods,
)
from .rings.subcategories.approximate import (
    ApproximateRingsCategory,
    ApproximateRingsElement,
    ApproximateRingsMorphism,
    ApproximateRingsObject,
)
from .rings.subcategories.complete import _CompleteRings
from .rings.subcategories.field import _Fields
from .rings.subcategories.local import _LocalRings
from .rings.subcategories.number_field import _NumberFields
from .sets import (
    SetsAut,
    SetsAutCategory,
    SetsAutomorphism,
    SetsCategory,
    SetsElement,
    SetsEnd,
    SetsEndCategory,
    SetsEndomorphism,
    SetsHom,
    SetsHomCategory,
    SetsMorphism,
    SetsObject,
)
from .sets.subcategories.constructions.isomorphic_objects import (
    _IsomorphicObjects as SetIsomorphicObjects,
)
from .sets.subcategories.constructions.quotients import _Quotients as SetQuotients
from .sets.subcategories.constructions.realizations import (
    _Realizations as SetRealizations,
)
from .sets.subcategories.constructions.subobjects import Subsets as SetSubobjects
from .sets.subcategories.constructions.subquotients import (
    _Subquotients as SetSubquotients,
)
from .sets.subcategories.constructions.with_realizations import (
    SetsWithRealizations as SetWithRealizationsCategory,
)
from .sets.subcategories.countable import _CountableSets
from .sets.subcategories.finite import _FiniteSets
from .sets.subcategories.graded import GradedSetsCategory
from .sets.subcategories.group_actions import _GSets
from .sets.subcategories.infinite import _InfiniteSets
from .sets.subcategories.partitioned import (
    PartitionedSetsAut,
    PartitionedSetsAutCategory,
    PartitionedSetsAutomorphism,
    PartitionedSetsCategory,
    PartitionedSetsElement,
    PartitionedSetsEnd,
    PartitionedSetsEndCategory,
    PartitionedSetsEndomorphism,
    PartitionedSetsHom,
    PartitionedSetsHomCategory,
    PartitionedSetsMorphism,
    PartitionedSetsObject,
)
from .sets.subcategories.real_set import _RealSets
from .sets.subcategories.uncountable import _UncountableSets
from .tensor_algebra_components import (
    TensorAlgebraComponentsAut,
    TensorAlgebraComponentsAutCategory,
    TensorAlgebraComponentsAutomorphism,
    TensorAlgebraComponentsCategory,
    TensorAlgebraComponentsElement,
    TensorAlgebraComponentsEnd,
    TensorAlgebraComponentsEndCategory,
    TensorAlgebraComponentsEndomorphism,
    TensorAlgebraComponentsHom,
    TensorAlgebraComponentsHomCategory,
    TensorAlgebraComponentsMorphism,
    TensorAlgebraComponentsObject,
)
from .topological_spaces import (
    MetricSpacesAut,
    MetricSpacesAutCategory,
    MetricSpacesAutomorphism,
    MetricSpacesCategory,
    MetricSpacesElement,
    MetricSpacesEnd,
    MetricSpacesEndCategory,
    MetricSpacesEndomorphism,
    MetricSpacesHom,
    MetricSpacesHomCategory,
    MetricSpacesMorphism,
    MetricSpacesObject,
    TopologicalSpacesAut,
    TopologicalSpacesAutCategory,
    TopologicalSpacesAutomorphism,
    TopologicalSpacesCategory,
    TopologicalSpacesElement,
    TopologicalSpacesEnd,
    TopologicalSpacesEndCategory,
    TopologicalSpacesEndomorphism,
    TopologicalSpacesHom,
    TopologicalSpacesHomCategory,
    TopologicalSpacesMorphism,
    TopologicalSpacesObject,
)

# Generic / Support
Category = CatBaseCategory
type CategoryObject = SageParent
type CategoryElement = SageElement
type Matrix = SageMatrix
type MatrixSpace = SageMatrixSpace
type DiGraph = SageDiGraph
type CartesianProductFunctor = SageCartesianProductFunctor
CategoryOfHomCategories = HomCategoriesCategory
CategoryOfEndCategories = EndCategoriesCategory
CategoryOfAutCategories = AutCategoriesCategory
Hom = HomCategoriesObject
End = EndCategoriesObject
Aut = AutCategoriesObject
type Morphism = SageMorphism
type Endomorphism = SageMorphism
type Automorphism = SageMorphism
Ring = RingsObject
Field = _Fields.ParentMethods
NumberField = _NumberFields.ParentMethods
RingElement = RingsElement
RingMorphism = RingsMorphism
RingHom = RingsHom
RingEnd = RingsEnd
RingAut = RingsAut
RingEndomorphism = RingsEndomorphism
RingAutomorphism = RingsAutomorphism
ApproximateRing = ApproximateRingsObject
ApproximateRingElement = ApproximateRingsElement
ApproximateRingMorphism = ApproximateRingsMorphism
ApproximateRingCategory = ApproximateRingsCategory
type Group = SageGroup
type AbelianGroup = AbelianGroup_class
type Magma = CategoryObject
type Semigroup = CategoryObject
type Monoid = Monoid_class
type AdditiveSemigroup = CategoryObject
type AdditiveMonoid = CategoryObject
type AdditiveGroup = CategoryObject
type Polynomial = SagePolynomial
type OrePolynomialRing = SageOrePolynomialRing
AlgebraicPolynomial = AlgebraicPolynomialTracker
type TermOrder = SageTermOrder
RealNumberInterval = RealIntervalFieldElement
ComplexInterval = ComplexIntervalFieldElement
Valuation = DiscretePseudoValuation

LocalRing = _LocalRings.ParentMethods
CompleteRing = _CompleteRings.ParentMethods

type Cardinality = Integer | InfinityElement
FreeResolution = SageFreeResolution

RMod = ModulesCategory
type RModule = ModulesObject
type RModuleElement = ModulesElement
RModMorphism = ModulesMorphism
RModuleMorphism = RModMorphism
FreeModule = _Free.ParentMethods
TorsionModule = _Torsion.ParentMethods
ProjectiveModule = _Projective.ParentMethods
SubModule = ModuleSubobjects.ParentMethods
Submodule = SubModule
QuotientModule = ModuleQuotients.ParentMethods
TensorProductRModule = ModuleTensorProducts.ParentMethods
type TensorAlgebraComponent = TensorAlgebraComponentsObject
type Tensor = TensorAlgebraComponentsElement

Ideal = _RingIdealParentMethods
PrimeIdeal = Ideal
MaximalIdeal = PrimeIdeal

RModHom = ModulesHom
RModEnd = ModulesEnd
RModAut = ModulesAut
RModuleEnd = RModEnd
RModuleAut = RModAut
RModEndomorphism = ModulesEndomorphism
RModAutomorphism = ModulesAutomorphism
RModuleEndomorphism = RModEndomorphism
RModuleAutomorphism = RModAutomorphism
DualModule = ModuleDualObjects.ParentMethods
DualModuleElement = ModuleDualObjects.ElementMethods
DualModuleMorphism = RModMorphism
RModDual = DualModule
RModuleDual = DualModule
RModDualElement = DualModuleElement
RModuleDualElement = DualModuleElement
RModDualMorphism = DualModuleMorphism
RModuleDualMorphism = DualModuleMorphism
RModuleForm = RModMorphism
ModuleStructure = RModMorphism
type ModuleBasis = (
    AbstractFamily | Mapping[CategoryElement, RModuleElement] | Sequence[RModuleElement]
)
Polyhedron = SageParent
FormedModuleCategory = FormedModulesCategory
FormedModule = FormedModulesObject
FormedModuleElement = FormedModulesElement
FormedModuleMorphism = FormedModulesMorphism
FormedModuleHom = FormedModulesHom
FormedModuleEnd = FormedModulesEnd
FormedModuleAut = FormedModulesAut
FormedModuleHomCategory = FormedModulesHomCategory
FormedModuleEndCategory = FormedModulesEndCategory
FormedModuleAutCategory = FormedModulesAutCategory
FormedModuleEndomorphism = FormedModulesEndomorphism
FormedModuleAutomorphism = FormedModulesAutomorphism
BilinearModuleCategory = BilinearModulesCategory
BilinearModule = BilinearModulesObject
BilinearModuleElement = BilinearModulesElement
BilinearModuleMorphism = BilinearModulesMorphism
BilinearModuleHom = BilinearModulesHom
BilinearModuleEnd = BilinearModulesEnd
BilinearModuleAut = BilinearModulesAut
BilinearModuleHomCategory = BilinearModulesHomCategory
BilinearModuleEndCategory = BilinearModulesEndCategory
BilinearModuleAutCategory = BilinearModulesAutCategory
BilinearModuleEndomorphism = BilinearModulesEndomorphism
BilinearModuleAutomorphism = BilinearModulesAutomorphism
QuadraticModuleCategory = QuadraticModulesCategory
QuadraticModule = QuadraticModulesObject
QuadraticModuleElement = QuadraticModulesElement
QuadraticModuleMorphism = QuadraticModulesMorphism
QuadraticModuleHom = QuadraticModulesHom
QuadraticModuleEnd = QuadraticModulesEnd
QuadraticModuleAut = QuadraticModulesAut
QuadraticModuleHomCategory = QuadraticModulesHomCategory
QuadraticModuleEndCategory = QuadraticModulesEndCategory
QuadraticModuleAutCategory = QuadraticModulesAutCategory
QuadraticModuleEndomorphism = QuadraticModulesEndomorphism
QuadraticModuleAutomorphism = QuadraticModulesAutomorphism
TorsionQuadraticModuleCategory = TorsionQuadraticModulesCategory
TorsionQuadraticModule = TorsionQuadraticModulesObject
TorsionQuadraticModuleElement = TorsionQuadraticModulesElement
TorsionQuadraticModuleMorphism = TorsionQuadraticModulesMorphism
TorsionQuadraticModuleHom = TorsionQuadraticModulesHom
TorsionQuadraticModuleEnd = TorsionQuadraticModulesEnd
TorsionQuadraticModuleAut = TorsionQuadraticModulesAut
TorsionQuadraticModuleHomCategory = TorsionQuadraticModulesHomCategory
TorsionQuadraticModuleEndCategory = TorsionQuadraticModulesEndCategory
TorsionQuadraticModuleAutCategory = TorsionQuadraticModulesAutCategory
TorsionQuadraticModuleEndomorphism = TorsionQuadraticModulesEndomorphism
TorsionQuadraticModuleAutomorphism = TorsionQuadraticModulesAutomorphism
type BilinearFormsModule = SageHomset
type BilinearForm = SageMorphism
type QuadraticFormsModule = SageHomset
type QuadraticForm = SageMorphism

RAlgebra = AlgebrasCategory
type Algebra = AlgebrasObject
type AlgebraElement = AlgebrasElement
type AlgebraMorphism = AlgebrasMorphism
MagmaticAlgebraCategory = MagmaticAlgebrasCategory
type MagmaticAlgebra = MagmaticAlgebrasObject
MagmaticAlgebraElement = MagmaticAlgebrasElement
MagmaticAlgebraMorphism = MagmaticAlgebrasMorphism
AssociativeAlgebraCategory = AssociativeAlgebrasCategory
AssociativeAlgebra = AssociativeAlgebrasObject
AssociativeAlgebraElement = AssociativeAlgebrasElement
AssociativeAlgebraMorphism = AssociativeAlgebrasMorphism
AlgebraBasis = AbstractFamily
AlgebraIdeal = AlgebraIdealsObject
type HochschildChainComplex = HochschildComplex

# Sets

Set = SetsObject
FiniteSet = _FiniteSets.ParentMethods
CountableSet = _CountableSets.ParentMethods
InfiniteSet = _InfiniteSets.ParentMethods
UncountableSet = _UncountableSets.ParentMethods
GradedSet = GradedSetsCategory.ParentMethods
GSet = _GSets.ParentMethods
Subset = SetSubobjects.ParentMethods
OpenSubset = Subset
ClosedSubset = Subset
SetSubquotient = SetSubquotients.ParentMethods
QuotientSet = SetQuotients.ParentMethods
IsomorphicSetObject = SetIsomorphicObjects.ParentMethods
SetWithRealizations = SetWithRealizationsCategory.ParentMethods
SetRealization = SetRealizations.ParentMethods
SetElement = SetsElement
SetMorphism = SetsMorphism
SetHom = SetsHom
SetEnd = SetsEnd
SetAut = SetsAut
SetEndomorphism = SetsEndomorphism
SetAutomorphism = SetsAutomorphism
type FiniteSetMap = FiniteSetMap_MN
type SetFamily = AbstractFamily
type SetGeneratingSeries = SageParent
type IntegerPartition = SageIntegerPartition
type SetPartition = SageSetPartition
SetPartitionsParent = SageSetPartitions
PartitionedSet = PartitionedSetsObject
PartitionedSetElement = PartitionedSetsElement
PartitionedSetMorphism = PartitionedSetsMorphism
PartitionedSetHom = PartitionedSetsHom
PartitionedSetEnd = PartitionedSetsEnd
PartitionedSetAut = PartitionedSetsAut
PartitionedSetEndomorphism = PartitionedSetsEndomorphism
PartitionedSetAutomorphism = PartitionedSetsAutomorphism
PartitionedSetHomCategory = PartitionedSetsHomCategory
PartitionedSetEndCategory = PartitionedSetsEndCategory
PartitionedSetAutCategory = PartitionedSetsAutCategory
PartitionedSetCategory = PartitionedSetsCategory
SetPartitionSet = PartitionedSet
type EquivalenceRelation = SetPartition
type GroupElement = SageElement
GroupAction = SageMorphism

type RealNumber = SageRealNumber
type TopologicalSpace = TopologicalSpacesObject
MetricSpace = MetricSpacesObject
TopologicalSpaceMorphism = TopologicalSpacesMorphism
RealSubset = _RealSets.ParentMethods
RealOpenSet = RealSubset
type RealInterval = InternalRealInterval
MetricBall = OpenSubset
PrimeSubset = Subset
PrimesInArithmeticProgressions = PrimeSubset
type SympySet = SageSympySet
type Poset = PosetsObject
type PosetElement = PosetsElement
type PosetMorphism = PosetsMorphism
PosetHom = PosetsHom
PosetEnd = PosetsEnd
PosetAut = PosetsAut
PosetSubset = Subset
MeetSemilatticePoset = _MeetSemilatticePosets.ParentMethods
JoinSemilatticePoset = _JoinSemilatticePosets.ParentMethods
LatticePoset = _LatticePosets.ParentMethods
FiniteMeetSemilatticePoset = _FiniteMeetSemilatticePosets.ParentMethods
FiniteJoinSemilatticePoset = _FiniteJoinSemilatticePosets.ParentMethods
FiniteLatticePoset = _FiniteLatticePosets.ParentMethods
type SageFinitePoset = SagePoset
LatticeCategory = LatticesCategory
Lattice = LatticesObject
LatticeElement = LatticesElement
type LatticeMorphism = LatticesMorphism
LatticeHom = LatticesHom
LatticeEnd = LatticesEnd
LatticeAut = LatticesAut
LatticeHomCategory = LatticesHomCategory
LatticeEndCategory = LatticesEndCategory
LatticeAutCategory = LatticesAutCategory
LatticeEndomorphism = LatticesEndomorphism
LatticeAutomorphism = LatticesAutomorphism
DiscriminantGroupCategory = LatticeDiscriminantGroupsCategory
DiscriminantGroup = LatticeDiscriminantGroupsObject
DiscriminantGroupElement = LatticeDiscriminantGroupsElement
DiscriminantGroupMorphism = LatticeDiscriminantGroupsMorphism
DiscriminantGroupHom = LatticeDiscriminantGroupsHom
DiscriminantGroupEnd = LatticeDiscriminantGroupsEnd
DiscriminantGroupAut = LatticeDiscriminantGroupsAut
DiscriminantGroupHomCategory = LatticeDiscriminantGroupsHomCategory
DiscriminantGroupEndCategory = LatticeDiscriminantGroupsEndCategory
DiscriminantGroupAutCategory = LatticeDiscriminantGroupsAutCategory
DiscriminantGroupEndomorphism = LatticeDiscriminantGroupsEndomorphism
DiscriminantGroupAutomorphism = LatticeDiscriminantGroupsAutomorphism
OrthogonalGroup = RModAut
OrthogonalAutomorphism = RModAutomorphism
LatticeOrthogonalGroup = LatticeAut
LatticeIsometry = LatticeAutomorphism
SignaturePair = tuple[Integer, Integer]
IntegralRescaling = tuple[Integer, Lattice]


CatTypes = SimpleNamespace(
    Category=CatCategory,
    Object=CatObject,
    Element=CatElement,
    Morphism=CatMorphism,
    HomCategory=CatHomCategory,
    EndCategory=CatEndCategory,
    AutCategory=CatAutCategory,
    Hom=CatHom,
    End=CatEnd,
    Aut=CatAut,
    Endomorphism=CatEndomorphism,
    Automorphism=CatAutomorphism,
)

HomCategoryTypes = SimpleNamespace(
    Category=HomCategoriesCategory,
    Object=HomCategoriesObject,
    Element=HomCategoriesElement,
    Morphism=HomCategoriesMorphism,
)

EndCategoryTypes = SimpleNamespace(
    Category=EndCategoriesCategory,
    Object=EndCategoriesObject,
    Element=EndCategoriesElement,
    Morphism=EndCategoriesMorphism,
)

AutCategoryTypes = SimpleNamespace(
    Category=AutCategoriesCategory,
    Object=AutCategoriesObject,
    Element=AutCategoriesElement,
    Morphism=AutCategoriesMorphism,
)

SetTypes = SimpleNamespace(
    Category=SetsCategory,
    Object=SetsObject,
    Element=SetsElement,
    Morphism=SetsMorphism,
    HomCategory=SetsHomCategory,
    EndCategory=SetsEndCategory,
    AutCategory=SetsAutCategory,
    Hom=SetsHom,
    End=SetsEnd,
    Aut=SetsAut,
    Endomorphism=SetsEndomorphism,
    Automorphism=SetsAutomorphism,
)

RingTypes = SimpleNamespace(
    Category=RingsCategory,
    Object=RingsObject,
    Element=RingsElement,
    Morphism=RingsMorphism,
    HomCategory=RingsHomCategory,
    EndCategory=RingsEndCategory,
    AutCategory=RingsAutCategory,
    Hom=RingsHom,
    End=RingsEnd,
    Aut=RingsAut,
    Endomorphism=RingsEndomorphism,
    Automorphism=RingsAutomorphism,
)

RModuleTypes = SimpleNamespace(
    Category=ModulesCategory,
    Object=ModulesObject,
    Element=ModulesElement,
    Morphism=ModulesMorphism,
    HomCategory=ModulesHomCategory,
    EndCategory=ModulesEndCategory,
    AutCategory=ModulesAutCategory,
    Hom=ModulesHom,
    End=ModulesEnd,
    Aut=ModulesAut,
    Endomorphism=ModulesEndomorphism,
    Automorphism=ModulesAutomorphism,
)

FormedModuleTypes = SimpleNamespace(
    Category=FormedModulesCategory,
    Object=FormedModulesObject,
    Element=FormedModulesElement,
    Morphism=FormedModulesMorphism,
    HomCategory=FormedModulesHomCategory,
    EndCategory=FormedModulesEndCategory,
    AutCategory=FormedModulesAutCategory,
    Hom=FormedModulesHom,
    End=FormedModulesEnd,
    Aut=FormedModulesAut,
    Endomorphism=FormedModulesEndomorphism,
    Automorphism=FormedModulesAutomorphism,
)

BilinearModuleTypes = SimpleNamespace(
    Category=BilinearModulesCategory,
    Object=BilinearModulesObject,
    Element=BilinearModulesElement,
    Morphism=BilinearModulesMorphism,
    HomCategory=BilinearModulesHomCategory,
    EndCategory=BilinearModulesEndCategory,
    AutCategory=BilinearModulesAutCategory,
    Hom=BilinearModulesHom,
    End=BilinearModulesEnd,
    Aut=BilinearModulesAut,
    Endomorphism=BilinearModulesEndomorphism,
    Automorphism=BilinearModulesAutomorphism,
)

QuadraticModuleTypes = SimpleNamespace(
    Category=QuadraticModulesCategory,
    Object=QuadraticModulesObject,
    Element=QuadraticModulesElement,
    Morphism=QuadraticModulesMorphism,
    HomCategory=QuadraticModulesHomCategory,
    EndCategory=QuadraticModulesEndCategory,
    AutCategory=QuadraticModulesAutCategory,
    Hom=QuadraticModulesHom,
    End=QuadraticModulesEnd,
    Aut=QuadraticModulesAut,
    Endomorphism=QuadraticModulesEndomorphism,
    Automorphism=QuadraticModulesAutomorphism,
)

TorsionQuadraticModuleTypes = SimpleNamespace(
    Category=TorsionQuadraticModulesCategory,
    Object=TorsionQuadraticModulesObject,
    Element=TorsionQuadraticModulesElement,
    Morphism=TorsionQuadraticModulesMorphism,
    HomCategory=TorsionQuadraticModulesHomCategory,
    EndCategory=TorsionQuadraticModulesEndCategory,
    AutCategory=TorsionQuadraticModulesAutCategory,
    Hom=TorsionQuadraticModulesHom,
    End=TorsionQuadraticModulesEnd,
    Aut=TorsionQuadraticModulesAut,
    Endomorphism=TorsionQuadraticModulesEndomorphism,
    Automorphism=TorsionQuadraticModulesAutomorphism,
)

AlgebraTypes = SimpleNamespace(
    Category=AlgebrasCategory,
    Object=AlgebrasObject,
    Element=AlgebrasElement,
    Morphism=AlgebrasMorphism,
    HomCategory=AlgebrasHomCategory,
    EndCategory=AlgebrasEndCategory,
    AutCategory=AlgebrasAutCategory,
    Hom=AlgebrasHom,
    End=AlgebrasEnd,
    Aut=AlgebrasAut,
    Endomorphism=AlgebrasEndomorphism,
    Automorphism=AlgebrasAutomorphism,
)

MagmaticAlgebraTypes = SimpleNamespace(
    Category=MagmaticAlgebrasCategory,
    Object=MagmaticAlgebrasObject,
    Element=MagmaticAlgebrasElement,
    Morphism=MagmaticAlgebrasMorphism,
)

AssociativeAlgebraTypes = SimpleNamespace(
    Category=AssociativeAlgebrasCategory,
    Object=AssociativeAlgebrasObject,
    Element=AssociativeAlgebrasElement,
    Morphism=AssociativeAlgebrasMorphism,
)

PosetTypes = SimpleNamespace(
    Category=PosetsCategory,
    Object=PosetsObject,
    Element=PosetsElement,
    Morphism=PosetsMorphism,
    HomCategory=PosetsHomCategory,
    EndCategory=PosetsEndCategory,
    AutCategory=PosetsAutCategory,
    Hom=PosetsHom,
    End=PosetsEnd,
    Aut=PosetsAut,
    Endomorphism=PosetsEndomorphism,
    Automorphism=PosetsAutomorphism,
)

TopologicalSpaceTypes = SimpleNamespace(
    Category=TopologicalSpacesCategory,
    Object=TopologicalSpacesObject,
    Element=TopologicalSpacesElement,
    Morphism=TopologicalSpacesMorphism,
    HomCategory=TopologicalSpacesHomCategory,
    EndCategory=TopologicalSpacesEndCategory,
    AutCategory=TopologicalSpacesAutCategory,
    Hom=TopologicalSpacesHom,
    End=TopologicalSpacesEnd,
    Aut=TopologicalSpacesAut,
    Endomorphism=TopologicalSpacesEndomorphism,
    Automorphism=TopologicalSpacesAutomorphism,
)

MetricSpaceTypes = SimpleNamespace(
    Category=MetricSpacesCategory,
    Object=MetricSpacesObject,
    Element=MetricSpacesElement,
    Morphism=MetricSpacesMorphism,
    HomCategory=MetricSpacesHomCategory,
    EndCategory=MetricSpacesEndCategory,
    AutCategory=MetricSpacesAutCategory,
    Hom=MetricSpacesHom,
    End=MetricSpacesEnd,
    Aut=MetricSpacesAut,
    Endomorphism=MetricSpacesEndomorphism,
    Automorphism=MetricSpacesAutomorphism,
)

TensorAlgebraComponentTypes = SimpleNamespace(
    Category=TensorAlgebraComponentsCategory,
    Object=TensorAlgebraComponentsObject,
    Element=TensorAlgebraComponentsElement,
    Morphism=TensorAlgebraComponentsMorphism,
    HomCategory=TensorAlgebraComponentsHomCategory,
    EndCategory=TensorAlgebraComponentsEndCategory,
    AutCategory=TensorAlgebraComponentsAutCategory,
    Hom=TensorAlgebraComponentsHom,
    End=TensorAlgebraComponentsEnd,
    Aut=TensorAlgebraComponentsAut,
    Endomorphism=TensorAlgebraComponentsEndomorphism,
    Automorphism=TensorAlgebraComponentsAutomorphism,
)

LatticeTypes = SimpleNamespace(
    Category=LatticesCategory,
    Object=LatticesObject,
    Element=LatticesElement,
    Morphism=LatticesMorphism,
    HomCategory=LatticesHomCategory,
    EndCategory=LatticesEndCategory,
    AutCategory=LatticesAutCategory,
    Hom=LatticesHom,
    End=LatticesEnd,
    Aut=LatticesAut,
    Endomorphism=LatticesEndomorphism,
    Automorphism=LatticesAutomorphism,
)

DiscriminantGroupTypes = SimpleNamespace(
    Category=LatticeDiscriminantGroupsCategory,
    Object=LatticeDiscriminantGroupsObject,
    Element=LatticeDiscriminantGroupsElement,
    Morphism=LatticeDiscriminantGroupsMorphism,
    HomCategory=LatticeDiscriminantGroupsHomCategory,
    EndCategory=LatticeDiscriminantGroupsEndCategory,
    AutCategory=LatticeDiscriminantGroupsAutCategory,
    Hom=LatticeDiscriminantGroupsHom,
    End=LatticeDiscriminantGroupsEnd,
    Aut=LatticeDiscriminantGroupsAut,
    Endomorphism=LatticeDiscriminantGroupsEndomorphism,
    Automorphism=LatticeDiscriminantGroupsAutomorphism,
)
