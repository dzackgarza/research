r"""The preamble's ``sage.all``: importing it is what makes a scope a session.

``from dzack_research.preamble.all import *`` enters the closed preamble
mathematical universe.  The module is not a superset of ``sage.all`` and does
not publish Sage's constructor namespace.  Sage is an implementation service
used by private adapters; every public name bound here is owned mathematics or
an ordinary Python support object deliberately selected by the preamble.
"""

import sys as _sys
from typing import cast as _cast

# The session's numeric vocabulary and its parser are one contract: decimal
# literals remain explicit MPFR approximations even though ``RealNumber`` now
# names an exact element of ``RR``.
import sageparse.preparser.research  # noqa: F401
from sage.misc.lazy_import import lazy_import as _lazy_import
from sage.repl.load import load as _sage_load

from dzack_research.preamble import language_runtime as _language_runtime
from sage_extensions.categories.abstract_categories import (  # noqa: F401
    Cat,
    CategoricalIsomorphism,
    CommutativeSquare,
    Coverage,
    CoveringFamilies,
    DescentData,
    DescentDataOnCover,
    DescentEqualizer,
    DescentEqualizerComparison,
    DirectedSystem,
    DirectSumObjects,
    FiniteOrdinalCategory,
    MorCategories,
    InverseSystem,
    NaturalTransformationMorphism,
    OppositeMorphism,
    PosetCategory,
    ProductMorphism,
    ResolutionMorphism,
    Resolutions,
    Sheaves,
    SubobjectMor,
    SubobjectMorphism,
    TrivialCoveringFamilies,
    trivial_coverage,
    OpenCoveringFamilies,
)
from sage_extensions.categories.abstract_categories.functors import (  # noqa: F401
    DiscreteCategories,
    DiscreteCategory,
    ObjectSetFunctor,
)
from sage_extensions.categories.algebras import (
    AlgebraMor,
    AlgebraMorphism,
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    AlternatingAlgebras,
    AugmentedAlgebras,
    CohomologyAlgebraElement,
    CohomologyAlgebraMor,
    CohomologyAlgebraMorphism,
    CohomologyAlgebras,
    CommutativeAlgebraCoproducts,
    CommutativeAlgebraPushouts,
    CommutatorLieAlgebras,
    CyclicCoverAlgebra,
    DegreewiseLinearMorphism,
    DeRhamAlgebras,
    Derivation,
    DerivationSpace,
    DGAMor,
    DGAMorphism,
    Differential,
    DifferentialComponentMorphism,
    DifferentialGradedAlgebras,
    DividedPowerAlgebras,
    FinitelyPresentedAlgebras,
    FreeAlgebras,
    GradedAlgebraMor,
    GradedAlgebraMorphism,
    GradedAlgebras,
    CommutativeGradedIntegralDomains,
    GradedAugmentedAlgebras,
    GradedCommutativeAlgebras,
    GradedDerivation,
    GradedDerivationSpace,
    GradedFreeAlgebras,
    GroupAlgebras,
    KahlerDifferentialModules,
    LieAlgebraMor,
    LieAlgebraMorphism,
    LieAlgebras,
    RestrictedGradedAlgebra,
    RestrictedGradedAlgebraElement,
    RestrictedScalarsAlgebras,
    StrictlyCommutativeDifferentialGradedAlgebras,
    StrictlyGradedCommutativeAlgebras,
    SymmetricAlgebras,
    TensorAlgebras,
)
from sage_extensions.categories.algebras.algebras import (
    MatrixAlgebras as MatrixAlgebras,
)
from sage_extensions.categories.coxeter_diagrams import (
    CoxeterDiagrams as CoxeterDiagrams,
)
from sage_extensions.categories.satake_diagrams import (
    SatakeDiagrams as SatakeDiagrams,
)
from sage_extensions.categories.chamber_systems import (  # noqa: F401
    ChamberSystems,
)
from sage_extensions.categories.graph_categories import (  # noqa: F401
    Digraphs,
    Graphs,
    LabelledDigraphs,
    LabelledGraphs,
)
from sage_extensions.categories.divisors import (  # noqa: F401
    AlgebraicCycleGroups,
    CartierDivisorGroups,
    ChowGroups,
    ClassGroups,
    CompleteLinearSystems,
    CoxRings,
    DivisorGroups,
    FormalDivisorGroups,
    HomogeneousPolynomialSectionSpaces,
    ImposedMultiplicityLinearSystems,
    LineBundleCohomologySpaces,
    PicardGroups,
    ProjectiveJetSpaces,
    ProjectiveLinearSystems,
    SectionRings,
    TorusInvariantCycleGroups,
    WeilDivisorGroups,
)
from sage_extensions.categories.forms import (
    BilinearFormMorphism,
    PairingMorphism,
    QuadraticFormMorphism,
)
from sage_extensions.categories.functions import (  # noqa: F401
    C,
    GradedLebesgueModule,
    GradedTensorProductModules,
    GradedTensorSquare,
    LebesgueGradedModules,
    LebesgueConvolution,
    LebesgueConvolutionModule,
    Lp,
    ell,
    graded_lebesgue_algebra,
    lebesgue_convolution_algebra,
    GradedLebesgueAlgebra,
    LebesgueConvolutionAlgebra,
)

# Explicit redundant aliases below are public session exports, not private imports.
from sage_extensions.categories.functors.core import (
    Adjunction as Adjunction,
)
from sage_extensions.categories.functors.core import (
    Functor as Functor,
)
from sage_extensions.categories.functors.core import (
    IdentityFunctor as IdentityFunctor,
)
from sage_extensions.categories.functors.core import (
    NaturalTransformation as NaturalTransformation,
)
from sage_extensions.groups import (
    FreeGroupQuotients,
    CoxeterGroups,
    AbelianGroups,
    AbsoluteDecompositionGroup,
    AbsoluteGaloisGroup,
    AbsoluteGaloisGroupElement,
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
    AbsoluteInertiaGroup,
    AdditiveGroups,
    CyclicGroups,
    CyclotomicCharacter,
    DecompositionGroupConjugacyClass,
    ElementConjugacyClass,
    FiniteAbelianGroups,
    FiniteElementConjugacyClass,
    FiniteGaloisAutomorphism,
    FiniteGaloisExtension,
    FiniteGaloisQuotient,
    FiniteGaloisSubgroup,
    FiniteGroups,
    FiniteGSets,
    FinitelyGeneratedGroups,
    FinitelyPresentedGroups,
    GeneralLinearGroups,
    FrobeniusConjugacyClass,
    FrobeniusElement,
    GObjectMor,
    GObjects,
    Grp,
    GroupAutomorphismGroup,
    GroupMor,
    Groups,
    GroupsWithChosenFinitePresentation,
    GSetMor,
    IndexedFreeGroupMorphism,
    IndexedFreeGroupMor,
    InertiaGroupConjugacyClass,
    InternalGroupActions,
    InternalGroupObjects,
    LiftCoset,
    OpenAbsoluteGaloisSubgroup,
    OpenAbsoluteGaloisSubgroups,
    OpenGaloisSubgroupConjugacyClass,
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
    SymmetricGroups,
    Torsors,
    groups,
)
from sage_extensions.categories.hyperbolic_lattices import (  # noqa: F401
    HyperbolicLattices,
)
from sage_extensions.categories.isotropic_orbits import (  # noqa: F401
    FlagType,
    IsotropicFlag,
)
from sage_extensions.categories.isotropic_parabolics import (  # noqa: F401
    PrimitiveIsotropicSubobjects,
)
from sage_extensions.categories.lattice_centralizers import (  # noqa: F401
    IsometryPrimitiveExtension,
)
from sage_extensions.categories.lattice_morphisms import (  # noqa: F401
    LatticeEmbedding,
    LatticeMor,
    LatticeIsometry,
    LatticeMorphism,
)
from sage_extensions.categories.lattices import (  # noqa: F401  # noqa: F401
    EvenLattices,
    EvenTwoElementaryLattices,
    DefiniteLattices,
    FiniteRankLattices,
    IsotropicReductions,
    Lattices,
    NotPrimitiveError,
    NoncrystallographicRootLattices,
    NondegenerateLattices,
    RootLattices,  # noqa: F401
    nikulin_invariants,
    signature_pair,
    signature_pairs,
)
from sage_extensions.categories.group.groups import (  # noqa: F401
    LieGroups,
    TopologicalGroups,
)
from sage_extensions.categories.hyperbolic_geometry import (  # noqa: F401
    HyperbolicPolyhedra,
    HyperbolicRationalPoints,
    HyperbolicSpaces,
    PositiveConeComponents,
)
from sage_extensions.categories.manifolds import (  # noqa: F401
    ComplexManifolds,
    DifferentiableManifolds,
    RiemannianManifolds,
    SmoothManifolds,
    TopologicalManifolds,
)
from sage_extensions.categories.integral_affine_manifolds import (  # noqa: F401
    IntegralAffineManifolds,
    IntegralAffineManifoldsWithBoundary,
    IntegralAffineManifoldsWithCorners,
    SingularIntegralAffineLocalModels,
    SingularIntegralAffineSpaces,
)
from sage_extensions.categories.integral_affine_atlases import (  # noqa: F401
    IntegralAffineAtlases,
)
from sage_extensions.categories.integral_affine_stratified_atlases import (  # noqa: F401
    IntegralAffineBoundaryAtlases,
    IntegralAffineCornerAtlases,
)
from sage_extensions.categories.integral_affine_collars import (  # noqa: F401
    IntegralAffineCollars,
)
from sage_extensions.categories.sets.finite_graded_posets import (  # noqa: F401
    FiniteGradedPosets,
)
from sage_extensions.categories.cell_complexes import (  # noqa: F401
    CellComplexes,
    DeltaComplexes,
    PolytopalComplexes,
    SimplicialComplexes,
    SimplicialSets,
)
from sage_extensions.categories.schemes.degeneration_central_fibers import (  # noqa: F401
    DegenerationCentralFibers,
)
from sage_extensions.categories.triangulations import (  # noqa: F401
    ChosenTriangulations,
)
from sage_extensions.categories.real_ck_manifolds import (  # noqa: F401
    RealCkManifolds,
)
from sage_extensions.categories.topological_atlases import (  # noqa: F401
    TopologicalAtlases,
)
from sage_extensions.categories.real_ck_atlases import (  # noqa: F401
    RealCkAtlases,
)
from sage_extensions.categories.stratified_atlases import (  # noqa: F401
    RealCkBoundaryAtlases,
    RealCkCornerAtlases,
    TopologicalBoundaryAtlases,
    TopologicalCornerAtlases,
)
from sage_extensions.categories.holomorphic_atlases import (  # noqa: F401
    HolomorphicAtlases,
)
from sage_extensions.categories.manifolds_with_boundary import (  # noqa: F401
    RealCkManifoldsWithBoundary,
    RealCkManifoldsWithCorners,
    SmoothManifoldsWithBoundary,
    SmoothManifoldsWithCorners,
    TopologicalManifoldsWithBoundary,
    TopologicalManifoldsWithCorners,
)
from sage_extensions.categories.manifold_dimension_strata import (  # noqa: F401
    ManifoldsOfDimensionAtMost,
    PureDimensionalManifolds,
)
from sage_extensions.categories.real_affine_spaces import (  # noqa: F401
    AffineSpacesWithLattice,
    RealAffineSpaces,
    RealVectorSpaces,
)
from sage_extensions.categories.complex_affine_spaces import (  # noqa: F401
    ComplexAffineSpaces,
    ComplexVectorSpaces,
)
from sage_extensions.categories.metric_affine_spaces import (  # noqa: F401
    EuclideanSpaces,
    SphericalSpaces,
)
from sage_extensions.categories.complex_analytic_spaces import (  # noqa: F401
    ComplexAnalyticSpaces,
)
from sage_extensions.categories.orbifolds import (  # noqa: F401
    ComplexOrbifolds,
    Orbifolds,
    RiemannianOrbifolds,
)
from sage_extensions.categories.modules import (
    BilinearFormModules,
    BilinearMap,
    BiproductModules,
    CochainComplexes,
    CochainDifferential,
    CochainMor,
    CochainMorphism,
    CohomologyModules,
    Connection,
    ConnectionDeRhamModule,
    ConnectionMor,
    ConnectionMorphism,
    ConnectionSpace,
    DifferentialGradedModules,
    DiscriminantBilinearModules,
    DiscriminantModules,
    DiscriminantQuadraticModules,
    DividedSquareModules,
    FiberedFormedModuleMor,
    FiberedFormedModuleMorphism,
    FinitelyGeneratedFreeModules,
    FinitelyGeneratedModules,
    FinitelyPresentedModules,
    FinitelyPresentedTorsionModules,
    FormedModuleMor,
    FormedModuleMorphism,
    FormEmbedding,
    FormModules,
    NondegenerateGenericFibreFormModules,
    FractionalIdeals,
    FractionFieldQuotients,
    FramedFreeModules,
    FreeFormModules,
    FreeModules,
    FreeResolution,
    GeneralModules,
    GradedAlgebraModules,
    GradedModules,
    IntegerGradedModules,
    GroupModuleMor,
    FiniteFreeGroupRepresentations,
    OrdinaryCharacterRepresentations,
    BrauerCharacterRepresentations,
    GroupModuleMorphism,
    InternalMorModules,
    LinearMorModules,
    LocalizedModules,
    ModuleBaseRingProjection,
    ModuleResolutions,
    Modules,
    ModulesOverIntegralDomains,
    ModulesOverCommutativeRings,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    ModulesWithConnection,
    ModulesWithFlatConnection,
    VectorBundlesWithConnection,
    PairingObjects,
    PairedModules,
    ProjectiveModules,
    QuadraticFormModules,
    RestrictedScalarsModules,
    SemilinearModuleMor,
    SemilinearModuleMorphism,
    SymmetricBilinearFormModules,
    TensorProductModules,
    TorsionBilinearFormModules,
    TorsionFormIsometry,
    TorsionModules,
    TorsionQuadraticFormModules,
    VectorSpaces,
    DerivedCategories,
    DerivedCategory,
    LinearCategories,
    TriangulatedCategories,
)
from sage_extensions.categories.modules.pure.modules import (  # noqa: F401
    MatrixEndomorphismSpaces,
    MatrixSpaces,
)
from sage_extensions.categories.modules.hodge_structures import (  # noqa: F401
    FilteredModules,
    HodgeStructures,
    MixedHodgeStructures,
    PolarizedHodgeStructures,
)
from sage_extensions.categories.rational_integral_stabilizers import (  # noqa: F401
    FiniteCommensurabilityQuotient,
    IntegralStructureAction,
)
_lazy_import(
    "sage_extensions.schemes",
    (
        "ADELogPairs",
        "AlgebraSheaves",
        "AffineGroupSchemeActions",
        "AffineGroupSchemes",
        "AffineGSchemes",
        "AffineInvariantQuotientBaseChangeComparison",
        "AffineSchemes",
        "AffineSpaces",
        "AbstractPolytopes",
        "ConvexPolytopesIn",
        "AnalyticDiscFamily",
        "Blowups",
        "ClosedEmbeddings",
        "ClosedSubschemes",
        "ConvexPolygons",
        "ConvexPolytopes",
        "EuclideanPolytopesIn",
        "HyperbolicGeodesicPolytopesIn",
        "LatticePolytopesIn",
        "CurveLocalDeltaContribution",
        "Curves",
        "CyclicCoverBaseChangeComparison",
        "DistinguishedAffineCoverRefinement",
        "DistinguishedAffineCovers",
        "EffectiveCartierDivisors",
        "FiberProductSchemes",
        "FiniteGluedInvariantQuotient",
        "HesseBertiniFamily",
        "HorikawaEnriquesSurface",
        "HorikawaK3Family",
        "IntegralSchemes",
        "IsolatedHypersurfaceSingularity",
        "LatticePolygons",
        "LatticePolytopes",
        "LegendreMonodromyFamily",
        "LocallyRingedSpaces",
        "LogPairs",
        "ModuleSheaves",
        "NodalCubic",
        "NodalCubicIntegralTopology",
        "NodalCubicNormalization",
        "NormalSchemes",
        "OpenImmersions",
        "DistinguishedOpenImmersions",
        "PGL2IntegralTopology",
        "PointedAnalyticFundamentalGroup",
        "ProductProjectiveSpaces",
        "ProductSchemes",
        "ProjectiveCompleteIntersections",
        "ProjectiveGeneralLinearGroup2",
        "ProjectivePointBlowups",
        "ProjectiveSchemes",
        "ProjectiveSpaces",
        "ProjectiveLines",
        "QuasiCoherentSheaves",
        "RationalPolyhedralFans",
        "RegularPolytopes",
        "SphericalGeodesicPolytopesIn",
        "RelativeCyclicCoverLift",
        "RelativeProjectivizations",
        "RingedSpaces",
        "SchemeMonomorphisms",
        "SchemeMorphism",
        "Schemes",
        "SchemesOverIntegralDomains",
        "SchemesOverLocalRings",
        "PresheafObjects",
        "SheafObjects",
        "SheafedSpaces",
        "SideDecoration",
        "SmoothSchemes",
        "Surfaces",
        "ToricFixedPointBlowups",
        "ToricGeometricLineBundleCohomologySpaces",
        "ToricLogPairs",
        "ToricSchemes",
        "ToricProjectiveSpaces",
        "GorensteinToricSchemes",
        "SmoothCompleteRationalToricSchemes",
        "ToricWeightCohomologyComplexes",
        "Varieties",
        "ZariskiCoveringFamilies",
        "distinguished_affine_coverage",
        "rational_quintic_with_nonrational_node_normalization",
        "rational_quintic_with_two_nodes_normalization",
        "zariski_coverage",
    ),
)
_lazy_import(
    "sage_extensions.categories.schemes.cyclic_covers",
    "CyclicCovers",
)
from sage_extensions.categories.sets import (  # noqa: F401
    AugmentedSimplexCategory,
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
    InfiniteSets,
    LaurentMonomials,
    ObjectSetsOfDiscreteCategories,
    Ord,
    Ordinals,
    PartiallyOrderedSets,
    PowerSets,
    Set,
    SetInjection,
    Sets,
    SetSurjection,
    SincTranslates,
    TotallyOrderedSets,
    UncountableSets,
    WellOrderedSets,
    aleph,
    aleph0,
    cardinal,
    continuum,
    finite_ordered_set,
    omega,
    omega0,
    ordinal,
)
from sage_extensions.categories.topological_spaces import (  # noqa: F401
    ContinuousMap,
    TopologicalSpaceMor,
    TopologicalSpaces,
)
from sage_extensions.categories.fundamental_groupoids import (  # noqa: F401
    FundamentalGroupoid,
    FundamentalGroupoids,
)
from sage_extensions.categories.pointed_topological_spaces import (  # noqa: F401
    TopologicalSpaceCoslices,
)
from sage_extensions.categories.algebras.graded_lie_algebras import (  # noqa: F401
    GradedLieAlgebras,
)
from sage_extensions.categories.algebras.graded_nonassociative_algebras import (  # noqa: F401
    GradedNonassociativeAlgebras,
)
from sage_extensions.categories.vector_orbits import (  # noqa: F401
    VectorPrimitiveExtension,
)
from sage_extensions.categories.rings.ring_foundation import (
    _OwnedRingParent,
)
from sage_extensions.categories.vinberg_invariants import (  # noqa: F401
    VinbergInvariantMatrices,
    reflection_cosines,
)
from sage_extensions.logic import Predicate, Propositions, Unknown, ask  # noqa: F401
from sage_extensions.validation import strict_checking  # noqa: F401
from sage_extensions.rings import (  # noqa: F401
    RR,
    CC,
    I,
    binomial,
    cos,
    cosh,
    e,
    exp,
    log,
    pi,
    sech,
    sgn,
    sin,
    sinh,
    sqrt,
    tan,
    tanh,
    zeta,
    AdicallyCompleteRings,
    AdicCompletions,
    ArtinianRings,
    CommutativeIdeals,
    CommutativeRings,
    CompleteLocalRings,
    DistinguishedOpenSubobjects,
    DivisionRings,
    ExactRealField,
    ExactRealNumber,
    ExactComplexField,
    ExactComplexNumber,
    Fields,
    FormalPowerSeriesRings,
    IntegralDomains,
    LocalRings,
    NoetherianRings,
    NonNegativeReals,
    NumberFieldsWithChosenPrimitiveElement,
    OrderedRings,
    Orders,
    OwnedCategoryOverBaseRing,
    OwnedDivisionRings,
    OwnedFields,
    OwnedNumberFields,
    OwnedOrders,
    OwnedRings,
    OwnedRngs,
    OwnedSemirings,
    PredicateSubrings,
    PrimeFields,
    PrimeSpectra,
    PrincipalIdealDomains,
    RealApproximation,
    Rings,
    UnitInterval,
    ZariskiClosedSubobjects,
    _restore_session_ring_bindings,  # noqa: F401
    session_ring_objects as _session_ring_objects,
)
from sage_extensions.tensors import Tensor, TensorModule, tensor  # noqa: F401
from sage_extensions.utilities import (
    lmap as lmap,
)
from sage_extensions.utilities import (
    lzip as lzip,
)
from sage_extensions.utilities import (
    to_var_names as to_var_names,
)
from sage_extensions.utilities import (
    zipsum as zipsum,
)

def load(filename: str, globals: dict | None = None, attach: bool = False) -> None:
    r"""Load a Sage file and restore this session's owned scalar vocabulary."""
    scope = _sys._getframe(1).f_globals if globals is None else globals
    _sage_load(filename, scope, attach)
    _restore_session_ring_bindings(scope)
    scope["GradedLebesgueAlgebra"] = GradedLebesgueAlgebra
    scope["LebesgueConvolutionAlgebra"] = LebesgueConvolutionAlgebra
    scope["load"] = load


# This is deliberately last.  Internal modules may import backend names while
# they load; the public session receives only owned scalar objects, owned
# constructors, and the owned runtime names emitted by the research dialect.
_restore_session_ring_bindings(globals())
_session_rings = _session_ring_objects()
ZZ: _OwnedRingParent = _cast(_OwnedRingParent, _session_rings["ZZ"])
QQ: _OwnedRingParent = _cast(_OwnedRingParent, _session_rings["QQ"])
Integer = _language_runtime.Integer
RealNumber = _language_runtime.RealNumber
ComplexNumber = _language_runtime.ComplexNumber
matrix = _language_runtime.matrix
factorial = _language_runtime.factorial
ellipsis_range = _language_runtime.ellipsis_range
ellipsis_iter = _language_runtime.ellipsis_iter


# The catalogue constructs named lattices at import time, so it is imported
# last, after every name it uses exists.
_lazy_import(
    "sage_extensions.catalogue",
    (
        "Embeddings",
        "Involutions",
        "NamedLattices",
        "NegativeDefTwoElementary",
        "TwoElementary",
        "signature_orthogonal_sums",
        "two_elementary_orthogonal_sums",
    ),
)
_lazy_import("sage_extensions.coble", "Coble")
_lazy_import("sage_extensions.sterk", "Sterk")


_language_runtime.install(globals())
