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
from dzack_research.preamble.categories.abstract_categories import (  # noqa: F401
    Cat,
    CategoricalIsomorphism,
    CategoryFunctorMorphism,
    CategoryObject,
    CommutativeSquare,
    Coverage,
    CoveringFamilies,
    DescentData,
    DescentDataOnCover,
    DescentEqualizer,
    DescentEqualizerComparison,
    DirectedSystem,
    DirectSumObjects,
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
)
from dzack_research.preamble.categories.abstract_categories.functors import (  # noqa: F401
    DiscreteCategories,
    DiscreteCategory,
    ObjectSetFunctor,
)
from dzack_research.preamble.categories.algebras import (
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
from dzack_research.preamble.categories.algebras.algebras import (
    MatrixAlgebras as MatrixAlgebras,
)
from dzack_research.preamble.categories.coxeter_diagrams import (
    CoxeterDiagrams as CoxeterDiagrams,
)
from dzack_research.preamble.categories.chamber_systems import (  # noqa: F401
    ChamberSystems,
)
from dzack_research.preamble.categories.graph_categories import (  # noqa: F401
    Digraphs,
    Graphs,
    LabelledDigraphs,
    LabelledGraphs,
)
from dzack_research.preamble.categories.divisors import (  # noqa: F401
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
from dzack_research.preamble.categories.functors.core import (
    Adjunction as Adjunction,
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
from dzack_research.preamble.groups import (
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
    EquivariantMorphism,
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
    GObjectMor,
    GObjects,
    Grp,
    GroupAutomorphismGroup,
    GroupMor,
    Groups,
    GroupsWithChosenFinitePresentation,
    GSetMor,
    GSetMorphism,
    IndexedFreeGroupMorphism,
    IndexedFreeGroupMor,
    InertiaGroupConjugacyClass,
    InternalGroupActions,
    InternalGroupObjects,
    LiftCoset,
    OpenAbsoluteGaloisSubgroup,
    OpenAbsoluteGaloisSubgroups,
    OpenGaloisSubgroupConjugacyClass,
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
    Torsors,
    groups,
)
from dzack_research.preamble.categories.hyperbolic_lattices import (  # noqa: F401
    HyperbolicLattices,
)
from dzack_research.preamble.categories.isotropic_orbits import (  # noqa: F401
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
    LatticeMor,
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
    nikulin_invariants,
    signature_pair,
    signature_pairs,
)
from dzack_research.preamble.categories.modules import (
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
    FractionalIdeals,
    FractionFieldQuotients,
    FramedFreeModules,
    FreeFormModules,
    FreeModules,
    FreeResolution,
    GeneralModules,
    GradedAlgebraModules,
    GradedModules,
    GroupModuleMor,
    GroupModuleMorphism,
    InternalMorModules,
    LinearMorModules,
    LocalizedModules,
    ModuleBaseRingProjection,
    ModuleEmbedding,
    ModuleResolutions,
    Modules,
    ModulesOverCommutativeRings,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    ModulesWithConnection,
    ModulesWithFlatConnection,
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
)
from dzack_research.preamble.categories.modules.pure.modules import (  # noqa: F401
    MatrixEndomorphismSpaces,
    MatrixSpaces,
)
from dzack_research.preamble.categories.rational_integral_stabilizers import (  # noqa: F401
    FiniteCommensurabilityQuotient,
    IntegralStructureAction,
)
from dzack_research.preamble.schemes import (
    ADELogPairs,
    AlgebraSheaves,
    AffineGroupSchemeActions,
    AffineGroupSchemes,
    AffineGSchemes,
    AffineInvariantQuotientBaseChangeComparison,
    AffineSchemes,
    AffineSpaces,
    AnalyticDiscFamily,
    ClosedEmbeddings,
    ClosedSubschemes,
    ConvexPolygons,
    ConvexPolytopes,
    DistinguishedAffineCoverRefinement,
    CurveLocalDeltaContribution,
    Curves,
    CyclicCoverBaseChangeComparison,
    DistinguishedAffineCovers,
    distinguished_affine_coverage,
    FiberProductSchemes,
    FiniteGluedInvariantQuotient,
    GeometricFundamentalGroups,
    HesseBertiniFamily,
    HorikawaEnriquesSurface,
    HorikawaK3Family,
    IntegralSchemes,
    IntegralSingularCohomologyGroups,
    IntegralTopologicalCohomologyGroups,
    IsolatedHypersurfaceSingularity,
    LatticePolygons,
    LatticePolytopes,
    LegendreMonodromyFamily,
    LocallyRingedSpaces,
    LogPairs,
    ModuleSheaves,
    NodalCubic,
    NodalCubicIntegralTopology,
    NodalCubicNormalization,
    NormalSchemes,
    OpenImmersions,
    PGL2IntegralTopology,
    PointedAnalyticFundamentalGroup,
    ProductProjectiveSpaces,
    ProductSchemes,
    ProjectiveCompleteIntersections,
    ProjectiveGeneralLinearGroup2,
    ProjectivePointBlowups,
    ProjectiveSchemes,
    ProjectiveSpaces,
    QuasiCoherentSheaves,
    RationalPolyhedralFans,
    RegularPolytopes,
    RelativeCyclicCoverLift,
    RelativeProjectivizations,
    ResolutionIntegralCohomologyGroups,
    RingedSpaces,
    SchemeMonomorphisms,
    SchemeMorphism,
    Schemes,
    ZariskiCoveringFamilies,
    zariski_coverage,
    SheafObjects,
    SheafedSpaces,
    SideDecoration,
    SmoothSchemes,
    Surfaces,
    ToricFixedPointBlowups,
    ToricFundamentalGroups,
    ToricGeometricLineBundleCohomologySpaces,
    ToricIntegralSingularCohomologyGroups,
    ToricLogPairs,
    ToricSchemes,
    ToricWeightCohomologyComplexes,
    Varieties,
    rational_quintic_with_nonrational_node_normalization,
    rational_quintic_with_two_nodes_normalization,
)
from dzack_research.preamble.categories.schemes.cyclic_covers import (  # noqa: F401
    CyclicCovers,
)
from dzack_research.preamble.categories.sets import (  # noqa: F401
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
    SetInclusion,
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
from dzack_research.preamble.categories.topological_spaces import (  # noqa: F401
    ContinuousMap,
    TopologicalSpaceMor,
    TopologicalSpaces,
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
from dzack_research.preamble.logic import Predicate, Propositions, Unknown, ask  # noqa: F401
from dzack_research.preamble.rings import (  # noqa: F401
    RR,
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
    ExactFieldMorphism,
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
    PrimeField,
    PrimeFields,
    PrimeSpectra,
    PrincipalIdealDomains,
    RealApproximation,
    Rings,
    UnitInterval,
    ZariskiClosedSubobjects,
    _restore_session_ring_bindings,  # noqa: F401
)
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
    scope["GradedLebesgueAlgebra"] = GradedLebesgueAlgebra
    scope["LebesgueConvolutionAlgebra"] = LebesgueConvolutionAlgebra
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


# The catalogue constructs named lattices at import time, so it is imported
# last, after every name it uses exists.
from dzack_research.preamble.catalogue import (  # noqa: E402,F401
    Embeddings,
    Involutions,
    NamedLattices,
    NegativeDefTwoElementary,
    TwoElementary,
    signature_orthogonal_sums,
    two_elementary_orthogonal_sums,
)
from dzack_research.preamble.coble import Coble  # noqa: E402,F401
from dzack_research.preamble.sterk import Sterk  # noqa: E402,F401
