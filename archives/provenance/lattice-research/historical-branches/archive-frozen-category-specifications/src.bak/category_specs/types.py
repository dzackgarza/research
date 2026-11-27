"""Centralized type aliases for the category specification hierarchy.

Category modules publish their standard mathematical type packages locally.
This file imports those packages and chooses conventional aliases such as
``Ring = RingsObject`` or ``RModule = ModulesObject``.
"""

from collections.abc import Mapping, Sequence
from typing import TypeAlias
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
Category : TypeAlias = CatBaseCategory
CategoryObject : TypeAlias = SageParent
CategoryElement : TypeAlias = SageElement
Matrix : TypeAlias = SageMatrix
MatrixSpace : TypeAlias = SageMatrixSpace
DiGraph : TypeAlias = SageDiGraph
CartesianProductFunctor : TypeAlias = SageCartesianProductFunctor
CategoryOfHomCategories : TypeAlias = HomCategoriesCategory
CategoryOfEndCategories : TypeAlias = EndCategoriesCategory
CategoryOfAutCategories : TypeAlias = AutCategoriesCategory
Hom : TypeAlias = HomCategoriesObject
End : TypeAlias = EndCategoriesObject
Aut : TypeAlias = AutCategoriesObject
Morphism : TypeAlias = SageMorphism
Endomorphism : TypeAlias = SageMorphism
Automorphism : TypeAlias = SageMorphism
Ring : TypeAlias = RingsObject
Field : TypeAlias = _Fields.ParentMethods
NumberField : TypeAlias = _NumberFields.ParentMethods
RingElement : TypeAlias = RingsElement
RingMorphism : TypeAlias = RingsMorphism
RingHom : TypeAlias = RingsHom
RingEnd : TypeAlias = RingsEnd
RingAut : TypeAlias = RingsAut
RingEndomorphism : TypeAlias = RingsEndomorphism
RingAutomorphism : TypeAlias = RingsAutomorphism
ApproximateRing : TypeAlias = ApproximateRingsObject
ApproximateRingElement : TypeAlias = ApproximateRingsElement
ApproximateRingMorphism : TypeAlias = ApproximateRingsMorphism
ApproximateRingCategory : TypeAlias = ApproximateRingsCategory
Group : TypeAlias = SageGroup
AbelianGroup : TypeAlias = AbelianGroup_class
Magma : TypeAlias = CategoryObject
Semigroup : TypeAlias = CategoryObject
Monoid : TypeAlias = Monoid_class
AdditiveSemigroup : TypeAlias = CategoryObject
AdditiveMonoid : TypeAlias = CategoryObject
AdditiveGroup : TypeAlias = CategoryObject
Polynomial : TypeAlias = SagePolynomial
OrePolynomialRing : TypeAlias = SageOrePolynomialRing
AlgebraicPolynomial : TypeAlias = AlgebraicPolynomialTracker
TermOrder : TypeAlias = SageTermOrder
RealNumberInterval : TypeAlias = RealIntervalFieldElement
ComplexInterval : TypeAlias = ComplexIntervalFieldElement
Valuation : TypeAlias = DiscretePseudoValuation

LocalRing : TypeAlias = _LocalRings.ParentMethods
CompleteRing : TypeAlias = _CompleteRings.ParentMethods

Cardinality: TypeAlias = Integer | InfinityElement
FreeResolution : TypeAlias = SageFreeResolution

RMod : TypeAlias = ModulesCategory
RModule : TypeAlias = ModulesObject
RModuleElement : TypeAlias = ModulesElement
RModMorphism : TypeAlias = ModulesMorphism
RModuleMorphism : TypeAlias = RModMorphism
FreeModule : TypeAlias = _Free.ParentMethods
TorsionModule : TypeAlias = _Torsion.ParentMethods
ProjectiveModule : TypeAlias = _Projective.ParentMethods
SubModule : TypeAlias = ModuleSubobjects.ParentMethods
Submodule : TypeAlias = SubModule
QuotientModule : TypeAlias = ModuleQuotients.ParentMethods
TensorProductRModule : TypeAlias = ModuleTensorProducts.ParentMethods
TensorAlgebraComponent : TypeAlias = TensorAlgebraComponentsObject
Tensor : TypeAlias = TensorAlgebraComponentsElement

Ideal : TypeAlias = _RingIdealParentMethods
PrimeIdeal : TypeAlias = Ideal
MaximalIdeal : TypeAlias = PrimeIdeal

RModHom : TypeAlias = ModulesHom
RModEnd : TypeAlias = ModulesEnd
RModAut : TypeAlias = ModulesAut
RModuleEnd : TypeAlias = RModEnd
RModuleAut : TypeAlias = RModAut
RModEndomorphism : TypeAlias = ModulesEndomorphism
RModAutomorphism : TypeAlias = ModulesAutomorphism
RModuleEndomorphism : TypeAlias = RModEndomorphism
RModuleAutomorphism : TypeAlias = RModAutomorphism
DualModule : TypeAlias = ModuleDualObjects.ParentMethods
DualModuleElement : TypeAlias = ModuleDualObjects.ElementMethods
DualModuleMorphism : TypeAlias = RModMorphism
RModDual : TypeAlias = DualModule
RModuleDual : TypeAlias = DualModule
RModDualElement : TypeAlias = DualModuleElement
RModuleDualElement : TypeAlias = DualModuleElement
RModDualMorphism : TypeAlias = DualModuleMorphism
RModuleDualMorphism : TypeAlias = DualModuleMorphism
RModuleForm : TypeAlias = RModMorphism
ModuleStructure : TypeAlias = RModMorphism
ModuleBasis: TypeAlias = (
    AbstractFamily | Mapping[CategoryElement, RModuleElement] | Sequence[RModuleElement]
)
Polyhedron : TypeAlias = SageParent
FormedModuleCategory : TypeAlias = FormedModulesCategory
FormedModule : TypeAlias = FormedModulesObject
FormedModuleElement : TypeAlias = FormedModulesElement
FormedModuleMorphism : TypeAlias = FormedModulesMorphism
FormedModuleHom : TypeAlias = FormedModulesHom
FormedModuleEnd : TypeAlias = FormedModulesEnd
FormedModuleAut : TypeAlias = FormedModulesAut
FormedModuleHomCategory : TypeAlias = FormedModulesHomCategory
FormedModuleEndCategory : TypeAlias = FormedModulesEndCategory
FormedModuleAutCategory : TypeAlias = FormedModulesAutCategory
FormedModuleEndomorphism : TypeAlias = FormedModulesEndomorphism
FormedModuleAutomorphism : TypeAlias = FormedModulesAutomorphism
BilinearModuleCategory : TypeAlias = BilinearModulesCategory
BilinearModule : TypeAlias = BilinearModulesObject
BilinearModuleElement : TypeAlias = BilinearModulesElement
BilinearModuleMorphism : TypeAlias = BilinearModulesMorphism
BilinearModuleHom : TypeAlias = BilinearModulesHom
BilinearModuleEnd : TypeAlias = BilinearModulesEnd
BilinearModuleAut : TypeAlias = BilinearModulesAut
BilinearModuleHomCategory : TypeAlias = BilinearModulesHomCategory
BilinearModuleEndCategory : TypeAlias = BilinearModulesEndCategory
BilinearModuleAutCategory : TypeAlias = BilinearModulesAutCategory
BilinearModuleEndomorphism : TypeAlias = BilinearModulesEndomorphism
BilinearModuleAutomorphism : TypeAlias = BilinearModulesAutomorphism
QuadraticModuleCategory : TypeAlias = QuadraticModulesCategory
QuadraticModule : TypeAlias = QuadraticModulesObject
QuadraticModuleElement : TypeAlias = QuadraticModulesElement
QuadraticModuleMorphism : TypeAlias = QuadraticModulesMorphism
QuadraticModuleHom : TypeAlias = QuadraticModulesHom
QuadraticModuleEnd : TypeAlias = QuadraticModulesEnd
QuadraticModuleAut : TypeAlias = QuadraticModulesAut
QuadraticModuleHomCategory : TypeAlias = QuadraticModulesHomCategory
QuadraticModuleEndCategory : TypeAlias = QuadraticModulesEndCategory
QuadraticModuleAutCategory : TypeAlias = QuadraticModulesAutCategory
QuadraticModuleEndomorphism : TypeAlias = QuadraticModulesEndomorphism
QuadraticModuleAutomorphism : TypeAlias = QuadraticModulesAutomorphism
TorsionQuadraticModuleCategory : TypeAlias = TorsionQuadraticModulesCategory
TorsionQuadraticModule : TypeAlias = TorsionQuadraticModulesObject
TorsionQuadraticModuleElement : TypeAlias = TorsionQuadraticModulesElement
TorsionQuadraticModuleMorphism : TypeAlias = TorsionQuadraticModulesMorphism
TorsionQuadraticModuleHom : TypeAlias = TorsionQuadraticModulesHom
TorsionQuadraticModuleEnd : TypeAlias = TorsionQuadraticModulesEnd
TorsionQuadraticModuleAut : TypeAlias = TorsionQuadraticModulesAut
TorsionQuadraticModuleHomCategory : TypeAlias = TorsionQuadraticModulesHomCategory
TorsionQuadraticModuleEndCategory : TypeAlias = TorsionQuadraticModulesEndCategory
TorsionQuadraticModuleAutCategory : TypeAlias = TorsionQuadraticModulesAutCategory
TorsionQuadraticModuleEndomorphism : TypeAlias = TorsionQuadraticModulesEndomorphism
TorsionQuadraticModuleAutomorphism : TypeAlias = TorsionQuadraticModulesAutomorphism
BilinearFormsModule : TypeAlias = SageHomset
BilinearForm : TypeAlias = SageMorphism
QuadraticFormsModule : TypeAlias = SageHomset
QuadraticForm : TypeAlias = SageMorphism

RAlgebra : TypeAlias = AlgebrasCategory
Algebra : TypeAlias = AlgebrasObject
AlgebraElement : TypeAlias = AlgebrasElement
AlgebraMorphism : TypeAlias = AlgebrasMorphism
MagmaticAlgebraCategory : TypeAlias = MagmaticAlgebrasCategory
MagmaticAlgebra : TypeAlias = MagmaticAlgebrasObject
MagmaticAlgebraElement : TypeAlias = MagmaticAlgebrasElement
MagmaticAlgebraMorphism : TypeAlias = MagmaticAlgebrasMorphism
AssociativeAlgebraCategory : TypeAlias = AssociativeAlgebrasCategory
AssociativeAlgebra : TypeAlias = AssociativeAlgebrasObject
AssociativeAlgebraElement : TypeAlias = AssociativeAlgebrasElement
AssociativeAlgebraMorphism : TypeAlias = AssociativeAlgebrasMorphism
AlgebraBasis : TypeAlias = AbstractFamily
AlgebraIdeal : TypeAlias = AlgebraIdealsObject
HochschildChainComplex : TypeAlias = HochschildComplex

# Sets

Set : TypeAlias = SetsObject
FiniteSet : TypeAlias = _FiniteSets.ParentMethods
CountableSet : TypeAlias = _CountableSets.ParentMethods
InfiniteSet : TypeAlias = _InfiniteSets.ParentMethods
UncountableSet : TypeAlias = _UncountableSets.ParentMethods
GradedSet : TypeAlias = GradedSetsCategory.ParentMethods
GSet : TypeAlias = _GSets.ParentMethods
Subset : TypeAlias = SetSubobjects.ParentMethods
OpenSubset : TypeAlias = Subset
ClosedSubset : TypeAlias = Subset
SetSubquotient : TypeAlias = SetSubquotients.ParentMethods
QuotientSet : TypeAlias = SetQuotients.ParentMethods
IsomorphicSetObject : TypeAlias = SetIsomorphicObjects.ParentMethods
SetWithRealizations : TypeAlias = SetWithRealizationsCategory.ParentMethods
SetRealization : TypeAlias = SetRealizations.ParentMethods
SetElement : TypeAlias = SetsElement
SetMorphism : TypeAlias = SetsMorphism
SetHom : TypeAlias = SetsHom
SetEnd : TypeAlias = SetsEnd
SetAut : TypeAlias = SetsAut
SetEndomorphism : TypeAlias = SetsEndomorphism
SetAutomorphism : TypeAlias = SetsAutomorphism
FiniteSetMap : TypeAlias = FiniteSetMap_MN
SetFamily : TypeAlias = AbstractFamily
SetGeneratingSeries : TypeAlias = SageParent
IntegerPartition : TypeAlias = SageIntegerPartition
SetPartition : TypeAlias = SageSetPartition
SetPartitionsParent : TypeAlias = SageSetPartitions
PartitionedSet : TypeAlias = PartitionedSetsObject
PartitionedSetElement : TypeAlias = PartitionedSetsElement
PartitionedSetMorphism : TypeAlias = PartitionedSetsMorphism
PartitionedSetHom : TypeAlias = PartitionedSetsHom
PartitionedSetEnd : TypeAlias = PartitionedSetsEnd
PartitionedSetAut : TypeAlias = PartitionedSetsAut
PartitionedSetEndomorphism : TypeAlias = PartitionedSetsEndomorphism
PartitionedSetAutomorphism : TypeAlias = PartitionedSetsAutomorphism
PartitionedSetHomCategory : TypeAlias = PartitionedSetsHomCategory
PartitionedSetEndCategory : TypeAlias = PartitionedSetsEndCategory
PartitionedSetAutCategory : TypeAlias = PartitionedSetsAutCategory
PartitionedSetCategory : TypeAlias = PartitionedSetsCategory
SetPartitionSet : TypeAlias = PartitionedSet
EquivalenceRelation : TypeAlias = SetPartition
GroupElement : TypeAlias = SageElement
GroupAction : TypeAlias = SageMorphism

RealNumber : TypeAlias = SageRealNumber
TopologicalSpace : TypeAlias = TopologicalSpacesObject
MetricSpace : TypeAlias = MetricSpacesObject
TopologicalSpaceMorphism : TypeAlias = TopologicalSpacesMorphism
RealSubset : TypeAlias = _RealSets.ParentMethods
RealOpenSet : TypeAlias = RealSubset
RealInterval : TypeAlias = InternalRealInterval
MetricBall : TypeAlias = OpenSubset
PrimeSubset : TypeAlias = Subset
PrimesInArithmeticProgressions : TypeAlias = PrimeSubset
SympySet : TypeAlias = SageSympySet
Poset : TypeAlias = PosetsObject
PosetElement : TypeAlias = PosetsElement
PosetMorphism : TypeAlias = PosetsMorphism
PosetHom : TypeAlias = PosetsHom
PosetEnd : TypeAlias = PosetsEnd
PosetAut : TypeAlias = PosetsAut
PosetSubset : TypeAlias = Subset
MeetSemilatticePoset : TypeAlias = _MeetSemilatticePosets.ParentMethods
JoinSemilatticePoset : TypeAlias = _JoinSemilatticePosets.ParentMethods
LatticePoset : TypeAlias = _LatticePosets.ParentMethods
FiniteMeetSemilatticePoset : TypeAlias = _FiniteMeetSemilatticePosets.ParentMethods
FiniteJoinSemilatticePoset : TypeAlias = _FiniteJoinSemilatticePosets.ParentMethods
FiniteLatticePoset : TypeAlias = _FiniteLatticePosets.ParentMethods
SageFinitePoset : TypeAlias = SagePoset
LatticeCategory : TypeAlias = LatticesCategory
Lattice : TypeAlias = LatticesObject
LatticeElement : TypeAlias = LatticesElement
LatticeMorphism : TypeAlias = LatticesMorphism
LatticeHom : TypeAlias = LatticesHom
LatticeEnd : TypeAlias = LatticesEnd
LatticeAut : TypeAlias = LatticesAut
LatticeHomCategory : TypeAlias = LatticesHomCategory
LatticeEndCategory : TypeAlias = LatticesEndCategory
LatticeAutCategory : TypeAlias = LatticesAutCategory
LatticeEndomorphism : TypeAlias = LatticesEndomorphism
LatticeAutomorphism : TypeAlias = LatticesAutomorphism
DiscriminantGroupCategory : TypeAlias = LatticeDiscriminantGroupsCategory
DiscriminantGroup : TypeAlias = LatticeDiscriminantGroupsObject
DiscriminantGroupElement : TypeAlias = LatticeDiscriminantGroupsElement
DiscriminantGroupMorphism : TypeAlias = LatticeDiscriminantGroupsMorphism
DiscriminantGroupHom : TypeAlias = LatticeDiscriminantGroupsHom
DiscriminantGroupEnd : TypeAlias = LatticeDiscriminantGroupsEnd
DiscriminantGroupAut : TypeAlias = LatticeDiscriminantGroupsAut
DiscriminantGroupHomCategory : TypeAlias = LatticeDiscriminantGroupsHomCategory
DiscriminantGroupEndCategory : TypeAlias = LatticeDiscriminantGroupsEndCategory
DiscriminantGroupAutCategory : TypeAlias = LatticeDiscriminantGroupsAutCategory
DiscriminantGroupEndomorphism : TypeAlias = LatticeDiscriminantGroupsEndomorphism
DiscriminantGroupAutomorphism : TypeAlias = LatticeDiscriminantGroupsAutomorphism
OrthogonalGroup : TypeAlias = RModAut
OrthogonalAutomorphism : TypeAlias = RModAutomorphism
LatticeOrthogonalGroup : TypeAlias = LatticeAut
LatticeIsometry : TypeAlias = LatticeAutomorphism
SignaturePair = tuple[Integer, Integer]
IntegralRescaling = tuple[Integer, Lattice]


CatTypes = SimpleNamespace(Category=CatCategory,
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
Automorphism=CatAutomorphism,)

HomCategoryTypes = SimpleNamespace(Category=HomCategoriesCategory,
Object=HomCategoriesObject,
Element=HomCategoriesElement,
Morphism=HomCategoriesMorphism,)

EndCategoryTypes = SimpleNamespace(Category=EndCategoriesCategory,
Object=EndCategoriesObject,
Element=EndCategoriesElement,
Morphism=EndCategoriesMorphism,)

AutCategoryTypes = SimpleNamespace(Category=AutCategoriesCategory,
Object=AutCategoriesObject,
Element=AutCategoriesElement,
Morphism=AutCategoriesMorphism,)

SetTypes = SimpleNamespace(Category=SetsCategory,
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
Automorphism=SetsAutomorphism,)

RingTypes = SimpleNamespace(Category=RingsCategory,
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
Automorphism=RingsAutomorphism,)

RModuleTypes = SimpleNamespace(Category=ModulesCategory,
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
Automorphism=ModulesAutomorphism,)

FormedModuleTypes = SimpleNamespace(Category=FormedModulesCategory,
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
Automorphism=FormedModulesAutomorphism,)

BilinearModuleTypes = SimpleNamespace(Category=BilinearModulesCategory,
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
Automorphism=BilinearModulesAutomorphism,)

QuadraticModuleTypes = SimpleNamespace(Category=QuadraticModulesCategory,
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
Automorphism=QuadraticModulesAutomorphism,)

TorsionQuadraticModuleTypes = SimpleNamespace(Category=TorsionQuadraticModulesCategory,
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
Automorphism=TorsionQuadraticModulesAutomorphism,)

AlgebraTypes = SimpleNamespace(Category=AlgebrasCategory,
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
Automorphism=AlgebrasAutomorphism,)

MagmaticAlgebraTypes = SimpleNamespace(Category=MagmaticAlgebrasCategory,
Object=MagmaticAlgebrasObject,
Element=MagmaticAlgebrasElement,
Morphism=MagmaticAlgebrasMorphism,)

AssociativeAlgebraTypes = SimpleNamespace(Category=AssociativeAlgebrasCategory,
Object=AssociativeAlgebrasObject,
Element=AssociativeAlgebrasElement,
Morphism=AssociativeAlgebrasMorphism,)

PosetTypes = SimpleNamespace(Category=PosetsCategory,
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
Automorphism=PosetsAutomorphism,)

TopologicalSpaceTypes = SimpleNamespace(Category=TopologicalSpacesCategory,
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
Automorphism=TopologicalSpacesAutomorphism,)

MetricSpaceTypes = SimpleNamespace(Category=MetricSpacesCategory,
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
Automorphism=MetricSpacesAutomorphism,)

TensorAlgebraComponentTypes = SimpleNamespace(Category=TensorAlgebraComponentsCategory,
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
Automorphism=TensorAlgebraComponentsAutomorphism,)

LatticeTypes = SimpleNamespace(Category=LatticesCategory,
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
Automorphism=LatticesAutomorphism,)

DiscriminantGroupTypes = SimpleNamespace(Category=LatticeDiscriminantGroupsCategory,
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
Automorphism=LatticeDiscriminantGroupsAutomorphism,)
