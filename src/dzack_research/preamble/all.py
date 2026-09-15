r"""The preamble's ``sage.all``: importing it is what makes a scope a session.

``from dzack_research.preamble.all import *`` enters the closed preamble
mathematical universe.  The module is not a superset of ``sage.all`` and does
not publish Sage's constructor namespace.  Sage is an implementation service
used by private adapters; every public name bound here is owned mathematics or
an ordinary Python support object deliberately selected by the preamble.
"""

import sys as _sys

# The session's numeric vocabulary and its parser are one contract: decimal
# literals remain explicit MPFR approximations even though ``RealNumber`` now
# names an exact element of ``RR``.
import sageparse.preparser.research  # noqa: F401
from sage.repl.load import load as _sage_load

from dzack_research.preamble import language_runtime as _language_runtime
from dzack_research.preamble.catalogue import (  # noqa: F401
    Embeddings,
    Involutions,
    NamedLattices,
    NegativeDefTwoElementary,
    TwoElementary,
    signature_orthogonal_sums,
    two_elementary_orthogonal_sums,
    validate_negative_def_two_elementary_table,
    validate_two_elementary_table,
)
from dzack_research.preamble.categories.abstract_categories import (  # noqa: F401
    AutCategoryConstruction,
    AutomorphismArrowCategory,
    BiproductCategory,
    Cat,
    CategoricalIsomorphism,
    CategoryFunctorMorphism,
    CategoryObject,
    CategoryPacket,
    Cocone,
    CoconeCategory,
    ColimitsOfCategory,
    CommutativeSquare,
    Cone,
    ConeCategory,
    CoproductCoconeCategory,
    CoproductsOfCategory,
    CoreCategory,
    DiagramCategory,
    DirectedSystem,
    DirectSumCategory,
    DirectSumDecomposition,
    DirectSumObjects,
    EndArrowCategory,
    EndCategoryConstruction,
    EndofunctorAlgebras,
    EpiCategoryConstruction,
    EpimorphismArrowCategory,
    HomCategories,
    HomCategoryConstruction,
    InverseSystem,
    IsoArrowCategory,
    IsoCategoryConstruction,
    Isomorphism,
    LimitsOfCategory,
    MonoCategoryConstruction,
    MonomorphismArrowCategory,
    NaturalTransformationMorphism,
    OppositeMorphism,
    PosetCategory,
    ProductConeCategory,
    ProductMorphism,
    ProductsOfCategory,
    Span,
    SpanCategory,
    SubobjectHomset,
    SubobjectMorphism,
    TensorProductCategory,
    WideSubcategory,
    category_packet,
    common_category,
    coproduct_cocone_category,
    product_cone_category,
)
from dzack_research.preamble.categories.abstract_categories.functors import (  # noqa: F401
    Bifunctor,
    CodomainFunctor,
    ComposedFunctor,
    ConstantDiagram,
    ContravariantFunctor,
    DiscreteCategories,
    DiscreteCategory,
    DiscreteDiagram,
    DiscreteFunctor,
    DomainFunctor,
    ObjectSetFunctor,
)
from dzack_research.preamble.categories.algebras import (  # noqa: F401
    AlgebraHomset,
    AlgebraMorphism,
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    AlgebrasWithChosenMultiplication,
    AlternatingAlgebraOn,
    AlternatingAlgebras,
    AssociativeAlgebras,
    AssociativeAlgebrasWithChosenMultiplication,
    AugmentedAlgebras,
    CohomologyAlgebraElement,
    CohomologyAlgebraHomset,
    CohomologyAlgebraMorphism,
    CohomologyAlgebras,
    CommutativeAlgebraCoproducts,
    CommutativeAlgebraPushouts,
    CommutativeAlgebras,
    CommutativeDifferentialGradedAlgebras,
    CommutatorLieAlgebras,
    CyclicCoverAlgebra,
    DegreewiseLinearMorphism,
    DeRhamAlgebras,
    Derivation,
    DerivationSpace,
    DGAHomset,
    DGAMorphism,
    Differential,
    DifferentialComponentMorphism,
    DifferentialGradedAlgebras,
    DividedPowerAlgebraOn,
    DividedPowerAlgebras,
    FinitelyPresentedAlgebra,
    FinitelyPresentedAlgebraOn,
    FinitelyPresentedAlgebras,
    FramedAlgebras,
    FreeAlgebraOn,
    FreeAlgebras,
    GradedAlgebraHomset,
    GradedAlgebraMorphism,
    GradedAlgebras,
    GradedAugmentedAlgebras,
    GradedCommutativeAlgebras,
    GradedDerivation,
    GradedDerivationSpace,
    GradedFreeAlgebras,
    GroupAlgebra,
    GroupAlgebraFunctor,
    GroupAlgebras,
    KahlerDifferentialModules,
    LieAlgebraHomset,
    LieAlgebraMorphism,
    LieAlgebras,
    OwnedAlgebras,
    RestrictedGradedAlgebra,
    RestrictedGradedAlgebraElement,
    RestrictedScalarsAlgebras,
    StrictlyCommutativeDifferentialGradedAlgebras,
    StrictlyGradedCommutativeAlgebras,
    SymmetricAlgebraOn,
    SymmetricAlgebras,
    TensorAlgebraOn,
    TensorAlgebras,
)
from dzack_research.preamble.categories.algebras.algebras import (
    MatrixAlgebras as MatrixAlgebras,
)
from dzack_research.preamble.categories.coxeter_diagrams import (
    CoxeterDiagrams as CoxeterDiagrams,
)
from dzack_research.preamble.categories.divisors import (  # noqa: F401
    AffineCodimensionOneChowComparison,
    AlgebraicCycleGroups,
    C2DiagonalProductProjectiveAction,
    C2ProductProjectiveLinearization,
    C2ProjectiveLineLinearization,
    CartierDivisorGroup,
    CartierDivisorGroups,
    ChowGroup,
    ChowGroups,
    ClassGroup,
    ClassGroups,
    CompleteLinearSystems,
    CoxRings,
    DivisorClassComparison,
    DivisorGroup,
    DivisorGroups,
    FiniteAtlasCartierDivisor,
    FiniteAtlasInvertibleSheaf,
    FormalDivisor,
    FormalDivisorGroup,
    FormalDivisorGroups,
    HomogeneousPolynomialSectionSpaces,
    ImposedMultiplicityLinearSystems,
    InvertibleSheaf,
    LineBundleCohomologySpaces,
    PicardGroup,
    PicardGroups,
    ProductProjectiveLineBundleLinearization,
    ProductProjectiveSubschemeLineBundle,
    ProductProjectiveSubschemeLineBundleIsomorphism,
    ProjectiveJetSpaces,
    ProjectiveLinearSystems,
    ProjectiveLineBundleLinearization,
    ProjectiveLineBundleLinearizationIsomorphism,
    ProjectiveLineCoordinateSwapAction,
    ProjectiveSubschemeLineBundle,
    ProjectiveSubschemeLineBundleIsomorphism,
    SectionRings,
    SerreIntersectionData,
    TorusInvariantCycleGroups,
    WeilDivisorGroup,
    WeilDivisorGroups,
)
from dzack_research.preamble.categories.forms import (
    BilinearFormMorphism,
    PairingMorphism,
    QuadraticFormMorphism,
)
from dzack_research.preamble.categories.functions import (  # noqa: F401
    C,
    GradedLebesgueModule,
    GradedTensorProductModules,
    GradedTensorSquare,
    LebesgueGradedModules,
    Lp,
    ell,
    graded_lebesgue_algebra,
    lebesgue_convolution_algebra,
)

# Explicit redundant aliases below are public session exports, not private imports.
from dzack_research.preamble.categories.functors.abelianization import (
    AbelianGroupInclusionFunctor as AbelianGroupInclusionFunctor,
)
from dzack_research.preamble.categories.functors.abelianization import (
    AbelianizationAdjunction as AbelianizationAdjunction,
)
from dzack_research.preamble.categories.functors.abelianization import (
    AbelianizationFunctor as AbelianizationFunctor,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    AlgebraUnderlyingModuleFunctor as AlgebraUnderlyingModuleFunctor,
)
from dzack_research.preamble.categories.functors.algebra_scalar_change import (
    AlgebraBaseChangeAdjunction as AlgebraBaseChangeAdjunction,
)
from dzack_research.preamble.categories.functors.algebra_scalar_change import (
    AlgebraRestrictionOfScalarsFunctor as AlgebraRestrictionOfScalarsFunctor,
)
from dzack_research.preamble.categories.functors.algebra_scalar_change import (
    AlgebraScalarExtensionFunctor as AlgebraScalarExtensionFunctor,
)
from dzack_research.preamble.categories.functors.cardinality import (
    CardinalityFunctor as CardinalityFunctor,
)
from dzack_research.preamble.categories.functors.cochain_complexes import (
    CochainUnderlyingGradedModuleFunctor as CochainUnderlyingGradedModuleFunctor,
)
from dzack_research.preamble.categories.functors.cohomology import (
    CohomologyAlgebraFunctor as CohomologyAlgebraFunctor,
)
from dzack_research.preamble.categories.functors.cohomology import (
    CohomologyFunctor as CohomologyFunctor,
)
from dzack_research.preamble.categories.functors.cohomology import (
    DeRhamCohomologyAlgebraFunctor as DeRhamCohomologyAlgebraFunctor,
)
from dzack_research.preamble.categories.functors.cohomology import (
    DeRhamCohomologyFunctor as DeRhamCohomologyFunctor,
)
from dzack_research.preamble.categories.functors.core import (
    Adjunction as Adjunction,
)
from dzack_research.preamble.categories.functors.core import (
    CompositeAdjunction as CompositeAdjunction,
)
from dzack_research.preamble.categories.functors.core import (
    CompositeFunctor as CompositeFunctor,
)
from dzack_research.preamble.categories.functors.core import (
    Functor as Functor,
)
from dzack_research.preamble.categories.functors.core import (
    IdentityFunctor as IdentityFunctor,
)
from dzack_research.preamble.categories.functors.core import (
    NaturalTransformation as NaturalTransformation,
)
from dzack_research.preamble.categories.functors.core import (
    compose_adjunctions as compose_adjunctions,
)
from dzack_research.preamble.categories.functors.de_rham import (
    DegreeZeroDGAFunctor as DegreeZeroDGAFunctor,
)
from dzack_research.preamble.categories.functors.de_rham import (
    DeRhamAdjunction as DeRhamAdjunction,
)
from dzack_research.preamble.categories.functors.de_rham import (
    DeRhamFunctor as DeRhamFunctor,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    AlternatingAlgebraFunctor as AlternatingAlgebraFunctor,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    SymmetricAlgebraAdjunction as SymmetricAlgebraAdjunction,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    SymmetricAlgebraFunctor as SymmetricAlgebraFunctor,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    TensorAlgebraAdjunction as TensorAlgebraAdjunction,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    TensorAlgebraFunctor as TensorAlgebraFunctor,
)
from dzack_research.preamble.categories.functors.free_forgetful import (
    FreeForgetfulAdjunction as FreeForgetfulAdjunction,
)
from dzack_research.preamble.categories.functors.free_forgetful import (
    FreeModuleFunctor as FreeModuleFunctor,
)
from dzack_research.preamble.categories.functors.free_forgetful import (
    UnderlyingSetFunctor as UnderlyingSetFunctor,
)
from dzack_research.preamble.categories.functors.free_forms import (
    BilinearFreeFormAdjunction as BilinearFreeFormAdjunction,
)
from dzack_research.preamble.categories.functors.free_forms import (
    BilinearUnderlyingModuleFunctor as BilinearUnderlyingModuleFunctor,
)
from dzack_research.preamble.categories.functors.free_forms import (
    FreeBilinearFormFunctor as FreeBilinearFormFunctor,
)
from dzack_research.preamble.categories.functors.free_forms import (
    FreeQuadraticFormFunctor as FreeQuadraticFormFunctor,
)
from dzack_research.preamble.categories.functors.free_forms import (
    QuadraticFreeFormAdjunction as QuadraticFreeFormAdjunction,
)
from dzack_research.preamble.categories.functors.free_forms import (
    QuadraticUnderlyingModuleFunctor as QuadraticUnderlyingModuleFunctor,
)
from dzack_research.preamble.categories.functors.free_groups import (
    FreeGroupFunctor as FreeGroupFunctor,
)
from dzack_research.preamble.categories.functors.free_groups import (
    FreeGroupUnderlyingSetAdjunction as FreeGroupUnderlyingSetAdjunction,
)
from dzack_research.preamble.categories.functors.free_groups import (
    GroupUnderlyingSetFunctor as GroupUnderlyingSetFunctor,
)
from dzack_research.preamble.categories.functors.group_actions import (
    CoinvariantsFunctor as CoinvariantsFunctor,
)
from dzack_research.preamble.categories.functors.group_actions import (
    CoinvariantsTrivialAdjunction as CoinvariantsTrivialAdjunction,
)
from dzack_research.preamble.categories.functors.group_actions import (
    InvariantsFunctor as InvariantsFunctor,
)
from dzack_research.preamble.categories.functors.group_actions import (
    TrivialActionFunctor as TrivialActionFunctor,
)
from dzack_research.preamble.categories.functors.group_actions import (
    TrivialInvariantsAdjunction as TrivialInvariantsAdjunction,
)
from dzack_research.preamble.categories.functors.group_induction import (
    CoinductionFunctor as CoinductionFunctor,
)
from dzack_research.preamble.categories.functors.group_induction import (
    InductionFunctor as InductionFunctor,
)
from dzack_research.preamble.categories.functors.group_induction import (
    InductionRestrictionAdjunction as InductionRestrictionAdjunction,
)
from dzack_research.preamble.categories.functors.group_induction import (
    RestrictionCoinductionAdjunction as RestrictionCoinductionAdjunction,
)
from dzack_research.preamble.categories.functors.group_induction import (
    RestrictionOfActingGroupFunctor as RestrictionOfActingGroupFunctor,
)
from dzack_research.preamble.categories.functors.group_scalar_change import (
    GroupModuleBaseChangeAdjunction as GroupModuleBaseChangeAdjunction,
)
from dzack_research.preamble.categories.functors.group_scalar_change import (
    GroupModuleRestrictionOfScalarsFunctor as GroupModuleRestrictionOfScalarsFunctor,
)
from dzack_research.preamble.categories.functors.group_scalar_change import (
    GroupModuleScalarExtensionFunctor as GroupModuleScalarExtensionFunctor,
)
from dzack_research.preamble.categories.functors.linear_constructions import (
    BiproductBifunctor as BiproductBifunctor,
)
from dzack_research.preamble.categories.functors.linear_constructions import (
    CokernelArrowFunctor as CokernelArrowFunctor,
)
from dzack_research.preamble.categories.functors.linear_constructions import (
    DualizationFunctor as DualizationFunctor,
)
from dzack_research.preamble.categories.functors.linear_constructions import (
    KernelArrowFunctor as KernelArrowFunctor,
)
from dzack_research.preamble.categories.functors.linear_constructions import (
    OrthogonalDirectSumBifunctor as OrthogonalDirectSumBifunctor,
)
from dzack_research.preamble.categories.functors.orders_number_fields import (
    FractionFieldFunctor as FractionFieldFunctor,
)
from dzack_research.preamble.categories.functors.orders_number_fields import (
    OrderNumberFieldAdjunction as OrderNumberFieldAdjunction,
)
from dzack_research.preamble.categories.functors.orders_number_fields import (
    RingOfIntegersFunctor as RingOfIntegersFunctor,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    BaseChangeAdjunction as BaseChangeAdjunction,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    CoextensionOfScalarsFunctor as CoextensionOfScalarsFunctor,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    RestrictionCoextensionAdjunction as RestrictionCoextensionAdjunction,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    RestrictionOfScalarsFunctor as RestrictionOfScalarsFunctor,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    ScalarExtensionFunctor as ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.functors.set_constructions import (
    ExponentialFunctor as ExponentialFunctor,
)
from dzack_research.preamble.categories.functors.set_constructions import (
    FinitePowerSetFunctor as FinitePowerSetFunctor,
)
from dzack_research.preamble.categories.functors.set_constructions import (
    FixedCardinalitySubsetFunctor as FixedCardinalitySubsetFunctor,
)
from dzack_research.preamble.categories.functors.set_constructions import (
    InverseImagePowerSetFunctor as InverseImagePowerSetFunctor,
)
from dzack_research.preamble.categories.functors.subobject_images import (
    DirectImageSubobjectFunctor as DirectImageSubobjectFunctor,
)
from dzack_research.preamble.categories.functors.subobject_images import (
    InverseImageSubobjectFunctor as InverseImageSubobjectFunctor,
)
from dzack_research.preamble.categories.functors.subobject_images import (
    SubobjectImageAdjunction as SubobjectImageAdjunction,
)
from dzack_research.preamble.categories.functors.tensor_hom import (
    InternalHomFromFunctor as InternalHomFromFunctor,
)
from dzack_research.preamble.categories.functors.tensor_hom import (
    TensorByFunctor as TensorByFunctor,
)
from dzack_research.preamble.categories.functors.tensor_hom import (
    TensorHomAdjunction as TensorHomAdjunction,
)
from dzack_research.preamble.categories.group import (
    AbelianGroups,
    AbsoluteDecompositionGroup,
    AbsoluteGaloisGroup,
    AbsoluteGaloisGroupElement,
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
    AbsoluteGaloisSliceAutomorphism,
    AbsoluteInertiaGroup,
    AdditiveGroups,
    CyclicGroups,
    CyclotomicCharacter,
    DecompositionGroupConjugacyClass,
    ElementConjugacyClass,
    EquivariantMorphism,
    ExactFieldMorphism,
    FiniteAbelianGroups,
    FiniteElementConjugacyClass,
    FiniteGaloisAutomorphism,
    FiniteGaloisExtension,
    FiniteGaloisQuotient,
    FiniteGaloisSubgroup,
    FiniteGroupClassFunction,
    FiniteGroups,
    FiniteGSets,
    FinitelyGeneratedGroups,
    FinitelyPresentedGroups,
    FrobeniusConjugacyClass,
    FrobeniusElement,
    GaloisRestrictionMap,
    GObjectHomset,
    GObjects,
    GroupAutomorphismGroup,
    GroupHomset,
    Groups,
    GroupsWithChosenFiniteGeneratingSet,
    GroupsWithChosenFinitePresentation,
    GSetHomset,
    GSetMorphism,
    GSets,
    IndexedFreeGroupHomomorphism,
    IndexedFreeGroupHomset,
    InertiaGroupConjugacyClass,
    LiftCoset,
    OpenAbsoluteGaloisSubgroup,
    OpenAbsoluteGaloisSubgroups,
    OpenGaloisSubgroupConjugacyClass,
    OpenSubgroupInclusion,
    OrbitSets,
    OwnedAbelianGroups,
    OwnedFiniteAbelianGroups,
    OwnedFiniteGroups,
    OwnedFinitelyGeneratedGroups,
    OwnedFinitelyPresentedGroups,
    OwnedGroups,
    PredicateSubgroups,
    PrimeProlongation,
    ProfiniteCharacter,
    ProfiniteGroups,
    QuadraticCharacter,
    RestrictedProfiniteCharacter,
    Subgroups,
    Submonoids,
    Torsors,
    absolute_galois_group_category,
    groups,
)
from dzack_research.preamble.categories.hyperbolic_lattices import (  # noqa: F401
    HyperbolicLattices,
)
from dzack_research.preamble.categories.isotropic_orbits import (  # noqa: F401
    Cusp,
    IsotropicFlag,
)
from dzack_research.preamble.categories.isotropic_parabolics import (  # noqa: F401
    PrimitiveIsotropicSubobjects,
)
from dzack_research.preamble.categories.lattice_centralizers import (  # noqa: F401
    IsometryPrimitiveExtension,
)
from dzack_research.preamble.categories.lattice_morphisms import (  # noqa: F401
    LatticeEmbedding,
    LatticeHomset,
    LatticeIsometry,
    LatticeMorphism,
)
from dzack_research.preamble.categories.lattices import (  # noqa: F401  # noqa: F401
    EvenLattices,
    FiniteRankLattices,
    Genus,
    IsotropicReductions,
    Lattices,
    NoncrystallographicRootLattices,
    NondegenerateLattices,
    RootLattices,  # noqa: F401
    diagonal_gram,
    nikulin_invariants,
    signature_pair,
    signature_pairs,
)
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    BilinearFormModules,
    BilinearMap,
    BiproductModules,
    CochainComplexElement,
    CochainComplexes,
    CochainComplexObject,
    CochainDifferential,
    CochainHomset,
    CochainMorphism,
    CohomologyModules,
    Connection,
    ConnectionDeRhamDifferential,
    ConnectionDeRhamModule,
    ConnectionHomset,
    ConnectionMorphism,
    ConnectionSpace,
    DifferentialGradedModules,
    DiscriminantBilinearModules,
    DiscriminantModules,
    DiscriminantQuadraticModules,
    DividedSquareModules,
    FiberedFormedModuleHomset,
    FiberedFormedModuleMorphism,
    FinitelyGeneratedFormModules,
    FinitelyGeneratedFreeFormModules,
    FinitelyGeneratedFreeModules,
    FinitelyGeneratedModules,
    FinitelyPresentedBilinearFormModules,
    FinitelyPresentedFormModules,
    FinitelyPresentedModule,
    FinitelyPresentedModules,
    FinitelyPresentedQuadraticFormModules,
    FinitelyPresentedTorsionModules,
    FormedModuleHomset,
    FormedModuleMorphism,
    FormedModules,
    FormEmbedding,
    FormModule,
    FormModules,
    FractionalIdeal,
    FractionalIdeals,
    FractionFieldQuotient,
    FractionFieldQuotients,
    FramedFreeModules,
    FramedModules,
    FreeFormModules,
    FreeModule,
    FreeModuleOn,
    FreeModules,
    FreeResolution,
    GeneralModule,
    GeneralModules,
    GradedAlgebraModules,
    GradedModules,
    GroupModuleHomset,
    GroupModuleMorphism,
    Ideals,
    InternalHomModules,
    LinearHomModules,
    LocalizedModules,
    ModuleEmbedding,
    Modules,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    ModulesWithConnection,
    ModulesWithFlatConnection,
    PairedModules,
    ProjectiveModules,
    QuadraticFormModules,
    RestrictedScalarsModules,
    RestrictedScalarsModuleView,
    SymmetricBilinearFormModules,
    TensorProductModules,
    TorsionBilinearFormModules,
    TorsionFormIsometry,
    TorsionModule,
    TorsionModules,
    TorsionQuadraticFormModules,
    VectorSpaces,
)
from dzack_research.preamble.categories.modules.pure.modules import (  # noqa: F401
    MatrixEndomorphismSpaces,
    MatrixSpaces,
)
from dzack_research.preamble.categories.rational_integral_stabilizers import (  # noqa: F401
    FiniteCommensurabilityQuotient,
    IntegralStructureAction,
)
from dzack_research.preamble.categories.rational_lattices import (
    RationalLattices as RationalLattices,
)
from dzack_research.preamble.categories.schemes import (
    ADELogPair,
    ADELogPairs,
    AffineGroupSchemeActions,
    AffineGroupSchemes,
    AffineGSchemes,
    AffineInvariantQuotientBaseChangeComparison,
    AffineModuleSheaf,
    AffineSchemes,
    AffineSpace,
    AffineSpaceAnalytificationFunctor,
    AffineSpaces,
    AffineSpecFunctor,
    AnalyticDiscFamily,
    AT21ADEDoubleCover,
    AT21ADEPair,
    AT21ToricADEPair,
    ClosedEmbeddings,
    ClosedSubschemes,
    CompleteIntersectionAdjunctionComparison,
    ConvexPolygon,
    ConvexPolygons,
    ConvexPolytope,
    ConvexPolytopes,
    CoverRefinement,
    CurveGenusComparison,
    CurveLocalDeltaContribution,
    Curves,
    CyclicCoverBaseChangeComparison,
    DistinguishedAffineCover,
    EnriquesMarkedIntegralCohomology,
    FiberProductSchemes,
    FiniteGluedInvariantQuotient,
    FiniteTypeSchemes,
    GeometricFundamentalGroups,
    HesseBertiniFamily,
    HigherDirectImageSheaf,
    HorikawaEnriquesBaseChangeComparison,
    HorikawaEnriquesSurface,
    HorikawaK3BaseChangeComparison,
    HorikawaK3DoubleCover,
    HorikawaK3Family,
    IntegralLocalSystem,
    IntegralSchemes,
    IntegralSingularCohomologyGroups,
    IntegralTopologicalCohomologyGroups,
    IsolatedHypersurfaceSingularity,
    LatticePolygon,
    LatticePolygons,
    LatticePolytope,
    LatticePolytopes,
    LegendreMonodromyFamily,
    LocallyRingedSpaces,
    LogPairs,
    NodalCubic,
    NodalCubicFundamentalGroup,
    NodalCubicIntegralTopology,
    NodalCubicNormalization,
    NormalSchemes,
    OpenImmersions,
    PGL2FundamentalGroup,
    PGL2IntegralCohomology,
    PGL2IntegralTopology,
    PointedAnalyticFundamentalGroup,
    ProductProjectiveSpaces,
    ProductSchemes,
    ProjectiveCompleteIntersections,
    ProjectiveCurveNormalizationData,
    ProjectiveGeneralLinearGroup2,
    ProjectiveLineFundamentalGroup,
    ProjectivePointBlowups,
    ProjectiveSchemes,
    ProjectiveSpace,
    ProjectiveSpaces,
    QuarticK3HodgeData,
    QuarticK3IntegralTopology,
    QuasiAffineSchemes,
    QuasiCoherentSheaves,
    QuasiProjectiveSchemes,
    RationalPolyhedralFans,
    RegularPolytopes,
    RelativeAffineFamily,
    RelativeCyclicCoverLift,
    ResolutionIntegralCohomologyGroups,
    RingedSpaces,
    SchemeBaseChangeFunctor,
    SchemeMonomorphisms,
    SchemeMorphism,
    Schemes,
    SchemeUnderlyingSpace,
    SeparatedSchemes,
    SideDecoration,
    SliceBaseChangeAdjunction,
    SliceCompositionFunctor,
    SlicePullbackFunctor,
    SmoothSchemes,
    Spec,
    StructureSheaf,
    Surfaces,
    ToricFixedPointBlowups,
    ToricFundamentalGroups,
    ToricGeometricLineBundleCohomologySpaces,
    ToricHodgeData,
    ToricIntegralSingularCohomologyGroups,
    ToricLogPairs,
    ToricSchemes,
    ToricWeightCohomologyComplexes,
    Varieties,
    affine_equation_family,
    analytic_disc_family,
    glued_invariant_quotient,
    hesse_bertini_family,
    horikawa_enriques_surface,
    horikawa_k3_family,
    legendre_monodromy_family,
    rational_quintic_with_nonrational_node_normalization,
    rational_quintic_with_two_nodes_normalization,
    reynolds_invariant_base_change_hypothesis,
    roots_of_unity_group_scheme,
)
from dzack_research.preamble.categories.schemes.cyclic_covers import (  # noqa: F401
    CyclicCovers,
)
from dzack_research.preamble.categories.sets import (  # noqa: F401
    NN,
    CardinalComparison,
    Cardinalities,
    CartesianProductsOfSets,
    CoproductsOfSets,
    CountableSets,
    CountablyInfiniteSets,
    DisjointUnionsOfSets,
    EnumeratedByIntegers,
    EnumeratedByNaturals,
    EnumeratedSets,
    FinitelySupportedFunctionSets,
    FinitePowerSets,
    FiniteSets,
    FourierCharacters,
    FunctionEnumeratedSets,
    HermitePolynomials,
    InfiniteEnumeratedSets,
    InfiniteSets,
    LaurentMonomials,
    ObjectSetsOfDiscreteCategories,
    Ordinals,
    OrdinalSemirings,
    PartiallyOrderedSets,
    PowerSets,
    Set,
    SetInclusion,
    SetInjection,
    Sets,
    SetSurjection,
    SincTranslates,
    TotallyOrderedSets,
    UncountableSets,
    aleph,
    aleph0,
    cardinal,
    continuum,
    finite_ordered_set,
    omega,
    omega0,
    ordinal,
)
from dzack_research.preamble.categories.vector_configurations import (  # noqa: F401
    VectorConfigurations,
)
from dzack_research.preamble.categories.vector_orbits import (  # noqa: F401
    VectorPrimitiveExtension,
)
from dzack_research.preamble.categories.vinberg_invariants import (  # noqa: F401
    VinbergInvariantMatrices,
    reflection_cosines,
)
from dzack_research.preamble.coble import Coble  # noqa: F401
from dzack_research.preamble.logic import Predicate, Unknown, ask  # noqa: F401
from dzack_research.preamble.rings import (  # noqa: F401
    RR,
    AdicallyCompleteRings,
    AdicCompletions,
    ArtinianRings,
    CommutativeIdeals,
    CommutativeRings,
    CompleteLocalRings,
    DistinguishedOpenSubobject,
    DivisionRings,
    DualNumbers,
    ExactRealField,
    ExactRealNumber,
    Fields,
    FormalPowerSeriesRings,
    IntegralDomains,
    LocalRings,
    NoetherianRings,
    NonNegativeReals,
    NumberFieldsWithChosenPrimitiveElement,
    OrderedRings,
    OwnedCategoryOverBaseRing,
    OwnedDivisionRings,
    OwnedFields,
    OwnedNumberFields,
    OwnedOrders,
    OwnedRings,
    OwnedRngs,
    OwnedSemirings,
    PredicateSubrings,
    PrimeField,
    PrimeFields,
    PrimeSpectra,
    PrincipalIdealDomains,
    RealApproximation,
    Rings,
    UnitInterval,
    ZariskiClosedSubobject,
    _restore_session_ring_bindings,  # noqa: F401
)
from dzack_research.preamble.sterk import Sterk  # noqa: F401
from dzack_research.preamble.tensors import Tensor, TensorModule, tensor  # noqa: F401
from dzack_research.preamble.utilities import (
    lmap as lmap,
)
from dzack_research.preamble.utilities import (
    lzip as lzip,
)
from dzack_research.preamble.utilities import (
    to_var_names as to_var_names,
)
from dzack_research.preamble.utilities import (
    zipsum as zipsum,
)

_language_runtime.install()


def load(filename: str, globals: dict | None = None, attach: bool = False) -> None:
    r"""Load a Sage file and restore this session's owned scalar vocabulary."""
    scope = _sys._getframe(1).f_globals if globals is None else globals
    _sage_load(filename, scope, attach)
    _restore_session_ring_bindings(scope)
    scope["GradedLebesgueAlgebra"] = graded_lebesgue_algebra()
    scope["LebesgueConvolutionAlgebra"] = lebesgue_convolution_algebra()
    scope["load"] = load


# This is deliberately last.  Internal modules may import backend names while
# they load; the public session receives only owned scalar objects, owned
# constructors, and the owned runtime names emitted by the research dialect.
_restore_session_ring_bindings(globals())
Integer = _language_runtime.Integer
RealNumber = _language_runtime.RealNumber
ComplexNumber = _language_runtime.ComplexNumber
matrix = _language_runtime.matrix
factorial = _language_runtime.factorial
ellipsis_range = _language_runtime.ellipsis_range
ellipsis_iter = _language_runtime.ellipsis_iter
var = _language_runtime.var
symbolic_expression = _language_runtime.symbolic_expression
GradedLebesgueAlgebra = graded_lebesgue_algebra()
LebesgueConvolutionAlgebra = lebesgue_convolution_algebra()


def _realize_owned_categories_over(_ring) -> None:
    r"""Create every owned category over ``_ring``, in one fixed order.

    Sage orders a category's supercategories for class construction by
    ``_cmp_key``, which is ``(flag, counter)`` with a global counter assigned
    the first time a category is touched.  Sage's own graph is created while
    ``sage.categories.all`` imports, so that order is the same every run.  The
    owned graph is created lazily as a session reaches into it, so the counters
    -- and with them the bases of every parent class -- depend on what the
    session happened to build first.  Two sibling categories then linearize
    their shared supercategories in opposite orders and a category above both
    cannot be built at all: ``Lattices(ZZ)("A2").discriminant_group()`` raised
    in a fresh session and succeeded after ``E8``'s.

    Creating them here fixes the counters before a session can. Sorting by name
    is what makes the order a property of the source rather than of the run.

    ``ZZ`` alone, because the counter belongs to the category object and not to
    its class, so this settles the categories over the initial ring and leaves a
    category over any other ring to be created when a session first reaches it.
    Extending the tuple below is how another ring joins them.
    """
    session = globals()
    for _name in sorted(session):
        _value = session[_name]
        if isinstance(_value, type) and _value is not OwnedCategoryOverBaseRing and issubclass(_value, OwnedCategoryOverBaseRing):
            _value(_ring)._cmp_key


for _initial_ring in (globals()["ZZ"],):
    _realize_owned_categories_over(_initial_ring)
