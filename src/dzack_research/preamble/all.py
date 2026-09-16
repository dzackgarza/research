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
)
from dzack_research.preamble.categories.abstract_categories import (  # noqa: F401
    BiproductCategory,
    Cat,
    CategoricalIsomorphism,
    CategoryFunctorMorphism,
    CategoryObject,
    CommutativeSquare,
    DirectedSystem,
    DirectSumCategory,
    DirectSumObjects,
    HomCategories,
    InverseSystem,
    NaturalTransformationMorphism,
    OppositeMorphism,
    PosetCategory,
    ProductMorphism,
    SubobjectHomset,
    SubobjectMorphism,
    TensorProductCategory,
)
from dzack_research.preamble.categories.abstract_categories.functors import (  # noqa: F401
    DiscreteCategories,
    DiscreteCategory,
    ObjectSetFunctor,
)
from dzack_research.preamble.categories.algebras import (
    AlgebraHomset,
    AlgebraMorphism,
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    AlgebrasWithChosenMultiplication,
    AlternatingAlgebras,
    AssociativeAlgebrasWithChosenMultiplication,
    AugmentedAlgebras,
    CohomologyAlgebraElement,
    CohomologyAlgebraHomset,
    CohomologyAlgebraMorphism,
    CohomologyAlgebras,
    CommutativeAlgebraCoproducts,
    CommutativeAlgebraPushouts,
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
    DividedPowerAlgebras,
    FinitelyPresentedAlgebras,
    FramedAlgebras,
    FreeAlgebras,
    GradedAlgebraHomset,
    GradedAlgebraMorphism,
    GradedAlgebras,
    GradedAugmentedAlgebras,
    GradedCommutativeAlgebras,
    GradedDerivation,
    GradedDerivationSpace,
    GradedFreeAlgebras,
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
    SymmetricAlgebras,
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
    CartierDivisorGroups,
    ChowGroups,
    ClassGroups,
    CompleteLinearSystems,
    CoxRings,
    DivisorClassComparison,
    DivisorGroups,
    FiniteAtlasCartierDivisor,
    FiniteAtlasInvertibleSheaf,
    FormalDivisorGroups,
    HomogeneousPolynomialSectionSpaces,
    ImposedMultiplicityLinearSystems,
    InvertibleSheaf,
    LineBundleCohomologySpaces,
    PicardGroups,
    ProductProjectiveSubschemeLineBundle,
    ProjectiveJetSpaces,
    ProjectiveLinearSystems,
    ProjectiveSubschemeLineBundle,
    SectionRings,
    SerreIntersectionData,
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
    Lp,
    ell,
    graded_lebesgue_algebra,
    lebesgue_convolution_algebra,
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
    Torsors,
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
    nikulin_invariants,
    signature_pair,
    signature_pairs,
)
from dzack_research.preamble.categories.modules import (
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
    FinitelyPresentedModules,
    FinitelyPresentedQuadraticFormModules,
    FinitelyPresentedTorsionModules,
    FormedModuleHomset,
    FormedModuleMorphism,
    FormEmbedding,
    FormModules,
    FractionalIdeals,
    FractionFieldQuotients,
    FramedFreeModules,
    FramedModules,
    FreeFormModules,
    FreeModules,
    FreeResolution,
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
    ADELogPairs,
    AffineGroupSchemeActions,
    AffineGroupSchemes,
    AffineGSchemes,
    AffineInvariantQuotientBaseChangeComparison,
    AffineModuleSheaf,
    AffineSchemes,
    AffineSpaces,
    AnalyticDiscFamily,
    AT21ADEDoubleCover,
    AT21ToricADEPair,
    ClosedEmbeddings,
    ClosedSubschemes,
    ConvexPolygons,
    ConvexPolytopes,
    CoverRefinement,
    CurveLocalDeltaContribution,
    Curves,
    CyclicCoverBaseChangeComparison,
    DistinguishedAffineCover,
    FiberProductSchemes,
    FiniteGluedInvariantQuotient,
    FiniteTypeSchemes,
    GeometricFundamentalGroups,
    HesseBertiniFamily,
    HigherDirectImageSheaf,
    HorikawaEnriquesSurface,
    HorikawaK3DoubleCover,
    HorikawaK3Family,
    IntegralLocalSystem,
    IntegralSchemes,
    IntegralSingularCohomologyGroups,
    IntegralTopologicalCohomologyGroups,
    IsolatedHypersurfaceSingularity,
    LatticePolygons,
    LatticePolytopes,
    LegendreMonodromyFamily,
    LocallyRingedSpaces,
    LogPairs,
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
    ProjectiveCurveNormalizationData,
    ProjectiveGeneralLinearGroup2,
    ProjectivePointBlowups,
    ProjectiveSchemes,
    ProjectiveSpaces,
    QuasiAffineSchemes,
    QuasiCoherentSheaves,
    QuasiProjectiveSchemes,
    RationalPolyhedralFans,
    RegularPolytopes,
    RelativeAffineFamily,
    RelativeCyclicCoverLift,
    ResolutionIntegralCohomologyGroups,
    RingedSpaces,
    SchemeMonomorphisms,
    SchemeMorphism,
    Schemes,
    SchemeUnderlyingSpace,
    SeparatedSchemes,
    SideDecoration,
    SmoothSchemes,
    StructureSheaf,
    Surfaces,
    ToricFixedPointBlowups,
    ToricFundamentalGroups,
    ToricGeometricLineBundleCohomologySpaces,
    ToricIntegralSingularCohomologyGroups,
    ToricLogPairs,
    ToricSchemes,
    ToricWeightCohomologyComplexes,
    Varieties,
    hesse_bertini_family,
    legendre_monodromy_family,
    rational_quintic_with_nonrational_node_normalization,
    rational_quintic_with_two_nodes_normalization,
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
