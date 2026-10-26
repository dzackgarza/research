r"""The preamble's ``sage.all``: importing it is what makes a scope a session.

``from dzack_research.preamble.all import *`` enters the closed preamble
mathematical universe.  The module is not a superset of ``sage.all`` and does
not publish Sage's constructor namespace.  Sage is an implementation service
used by private adapters; every public name bound here is owned mathematics or
an ordinary Python support object deliberately selected by the preamble.
"""

import sys as _sys
from importlib import import_module as _import_module
from importlib.util import find_spec as _find_spec
from pathlib import Path as _Path
from typing import cast as _cast

# The session's numeric vocabulary and its parser are one contract: decimal
# literals remain explicit MPFR approximations even though ``RealNumber`` now
# names an exact element of ``RR``.
import sageparse.preparser.research  # noqa: F401
from sage.misc.lazy_import import lazy_import as _lazy_import
from sage.repl.load import load as _sage_load

_canonical_attached_modules: dict[str, str] = {}
_sage_attach_reload_wrapped = False


def _canonical_attach_code(filename: str) -> str | None:
    r"""Return a reload expression only for sources owned by canonical imports."""
    source = str(_Path(filename).expanduser().resolve())
    module_name = _canonical_attached_modules.get(source)
    if module_name is None:
        return None
    return (
        "import importlib as __preamble_importlib, sys as __preamble_sys\n"
        f"__preamble_module = __preamble_importlib.reload(__preamble_sys.modules[{module_name!r}])\n"
        "globals().update({name: value for name, value in vars(__preamble_module).items() "
        "if not (name.startswith('__') and name.endswith('__'))})\n"
    )


def _install_canonical_attach_reload() -> None:
    r"""Route Sage's existing attach/reload callbacks through module identity."""
    global _sage_attach_reload_wrapped
    if _sage_attach_reload_wrapped:
        return
    from sage.repl import attach as _sage_attach

    original_load = _sage_attach.load
    original_load_wrap = _sage_attach.load_wrap

    def load(filename, scope, attach=False):
        code = _canonical_attach_code(str(filename))
        if code is None:
            return original_load(filename, scope, attach=attach)
        exec(compile(code, str(filename), "exec"), scope)

    def load_wrap(filename, attach=False):
        code = _canonical_attach_code(str(filename))
        if code is None:
            return original_load_wrap(filename, attach=attach)
        return code

    _sage_attach.load = load
    _sage_attach.load_wrap = load_wrap
    _sage_attach_reload_wrapped = True

from dzack_research.preamble import language_runtime as _language_runtime
from dzack_research.preamble.categories.abstract_categories import (  # noqa: F401
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
from dzack_research.preamble.categories.algebras.algebras import (
    MatrixAlgebras as MatrixAlgebras,
)
from dzack_research.preamble.categories.coxeter_diagrams import (
    CoxeterDiagrams as CoxeterDiagrams,
)
from dzack_research.preamble.categories.satake_diagrams import (
    SatakeDiagrams as SatakeDiagrams,
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
from dzack_research.preamble.categories.hyperbolic_lattices import (  # noqa: F401
    HyperbolicLattices,
)
from dzack_research.preamble.categories.isotropic_orbits import (  # noqa: F401
    FlagType,
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
from dzack_research.preamble.categories.group.groups import (  # noqa: F401
    LieGroups,
    TopologicalGroups,
)
from dzack_research.preamble.categories.hyperbolic_geometry import (  # noqa: F401
    HyperbolicPolyhedra,
    HyperbolicRationalPoints,
    HyperbolicSpaces,
    PositiveConeComponents,
)
from dzack_research.preamble.categories.manifolds import (  # noqa: F401
    ComplexManifolds,
    DifferentiableManifolds,
    RiemannianManifolds,
    SmoothManifolds,
    TopologicalManifolds,
)
from dzack_research.preamble.categories.integral_affine_manifolds import (  # noqa: F401
    IntegralAffineManifolds,
    IntegralAffineManifoldsWithBoundary,
    IntegralAffineManifoldsWithCorners,
    SingularIntegralAffineLocalModels,
    SingularIntegralAffineSpaces,
)
from dzack_research.preamble.categories.integral_affine_atlases import (  # noqa: F401
    IntegralAffineAtlases,
)
from dzack_research.preamble.categories.integral_affine_stratified_atlases import (  # noqa: F401
    IntegralAffineBoundaryAtlases,
    IntegralAffineCornerAtlases,
)
from dzack_research.preamble.categories.integral_affine_collars import (  # noqa: F401
    IntegralAffineCollars,
)
from dzack_research.preamble.categories.sets.finite_graded_posets import (  # noqa: F401
    FiniteGradedPosets,
)
from dzack_research.preamble.categories.cell_complexes import (  # noqa: F401
    CellComplexes,
    DeltaComplexes,
    PolytopalComplexes,
    SimplicialComplexes,
    SimplicialSets,
)
from dzack_research.preamble.categories.schemes.degeneration_central_fibers import (  # noqa: F401
    DegenerationCentralFibers,
)
from dzack_research.preamble.categories.triangulations import (  # noqa: F401
    ChosenTriangulations,
)
from dzack_research.preamble.categories.real_ck_manifolds import (  # noqa: F401
    RealCkManifolds,
)
from dzack_research.preamble.categories.topological_atlases import (  # noqa: F401
    TopologicalAtlases,
)
from dzack_research.preamble.categories.real_ck_atlases import (  # noqa: F401
    RealCkAtlases,
)
from dzack_research.preamble.categories.stratified_atlases import (  # noqa: F401
    RealCkBoundaryAtlases,
    RealCkCornerAtlases,
    TopologicalBoundaryAtlases,
    TopologicalCornerAtlases,
)
from dzack_research.preamble.categories.holomorphic_atlases import (  # noqa: F401
    HolomorphicAtlases,
)
from dzack_research.preamble.categories.manifolds_with_boundary import (  # noqa: F401
    RealCkManifoldsWithBoundary,
    RealCkManifoldsWithCorners,
    SmoothManifoldsWithBoundary,
    SmoothManifoldsWithCorners,
    TopologicalManifoldsWithBoundary,
    TopologicalManifoldsWithCorners,
)
from dzack_research.preamble.categories.manifold_dimension_strata import (  # noqa: F401
    ManifoldsOfDimensionAtMost,
    PureDimensionalManifolds,
)
from dzack_research.preamble.categories.real_affine_spaces import (  # noqa: F401
    AffineSpacesWithLattice,
    RealAffineSpaces,
    RealVectorSpaces,
)
from dzack_research.preamble.categories.complex_affine_spaces import (  # noqa: F401
    ComplexAffineSpaces,
    ComplexVectorSpaces,
)
from dzack_research.preamble.categories.metric_affine_spaces import (  # noqa: F401
    EuclideanSpaces,
    SphericalSpaces,
)
from dzack_research.preamble.categories.complex_analytic_spaces import (  # noqa: F401
    ComplexAnalyticSpaces,
)
from dzack_research.preamble.categories.orbifolds import (  # noqa: F401
    ComplexOrbifolds,
    Orbifolds,
    RiemannianOrbifolds,
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
from dzack_research.preamble.categories.modules.pure.modules import (  # noqa: F401
    MatrixEndomorphismSpaces,
    MatrixSpaces,
)
from dzack_research.preamble.categories.modules.hodge_structures import (  # noqa: F401
    FilteredModules,
    HodgeStructures,
    MixedHodgeStructures,
    PolarizedHodgeStructures,
)
from dzack_research.preamble.categories.rational_integral_stabilizers import (  # noqa: F401
    FiniteCommensurabilityQuotient,
    IntegralStructureAction,
)
_lazy_import(
    "dzack_research.preamble.schemes",
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
    "dzack_research.preamble.categories.schemes.cyclic_covers",
    "CyclicCovers",
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
from dzack_research.preamble.categories.fundamental_groupoids import (  # noqa: F401
    FundamentalGroupoid,
    FundamentalGroupoids,
)
from dzack_research.preamble.categories.pointed_topological_spaces import (  # noqa: F401
    TopologicalSpaceCoslices,
)
from dzack_research.preamble.categories.algebras.graded_lie_algebras import (  # noqa: F401
    GradedLieAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_nonassociative_algebras import (  # noqa: F401
    GradedNonassociativeAlgebras,
)
from dzack_research.preamble.categories.vector_orbits import (  # noqa: F401
    VectorPrimitiveExtension,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _OwnedRingParent,
)
from dzack_research.preamble.categories.vinberg_invariants import (  # noqa: F401
    VinbergInvariantMatrices,
    reflection_cosines,
)
from dzack_research.preamble.logic import Predicate, Propositions, Unknown, ask  # noqa: F401
from dzack_research.preamble.validation import strict_checking  # noqa: F401
from dzack_research.preamble.rings import (  # noqa: F401
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

def load(filename: str, globals: dict | None = None, attach: bool = False) -> None:
    r"""Load a Sage file through its canonical module when it is importable.

    Package sources must not be executed into an ad-hoc namespace: that creates
    a second population of category and module classes beside the ordinary
    import population.  Resolve an importable source path to its dotted module
    name and let the installed ``sageparse`` finder own compilation and module
    identity.  Arbitrary session scripts, which have no importable module name,
    retain Sage's traditional namespace-loading behavior.
    """
    scope = _sys._getframe(1).f_globals if globals is None else globals
    source = _Path(filename).expanduser().resolve()
    module_name = None
    conflicting_candidate = None
    for entry in _sys.path:
        root = _Path(entry or ".").resolve()
        try:
            relative = source.relative_to(root)
        except ValueError:
            continue
        # Canonicalize package sources in either source format.  An ordinary
        # standalone script still falls through unless normal import resolution
        # identifies this exact file as a module.
        if relative.suffix not in (".py", ".sage"):
            continue
        # A path merely lying under sys.path does not make a session script a
        # package module: test and notebook scripts commonly live there too.
        # Canonicalize only sources inside a package tree (or the package
        # initializer itself); otherwise preserve Sage's execute-into-scope
        # semantics even if a namespace-package finder could import the file.
        ancestors = []
        directory = root
        for part in relative.parts[:-1]:
            directory = directory / part
            ancestors.append(directory)
        if relative.name not in ("__init__.py", "__init__.sage") and not any(
            (directory / "__init__.py").is_file()
            or (directory / "__init__.sage").is_file()
            for directory in ancestors
        ):
            continue
        parts = list(relative.with_suffix("").parts)
        if parts and parts[-1] == "__init__":
            parts.pop()
        if not parts or not all(part.isidentifier() for part in parts):
            continue
        candidate = ".".join(parts)
        # Only delegate when the installed sageparse finder chooses this exact
        # source; package directories may have their own loader.
        try:
            spec = _find_spec(candidate)
        except (ImportError, ModuleNotFoundError, ValueError):
            continue
        if spec is None or spec.origin is None:
            # This sys.path entry did not make the source importable under the
            # candidate name (a nested path entry may be only a partial name).
            # It is not evidence of a competing canonical module.
            continue
        if _Path(spec.origin).resolve() == source:
            imported = _import_module(candidate)
            module_name = candidate
            break
        conflicting_candidate = candidate
    if module_name is None and conflicting_candidate is not None:
        # Normal import resolution selected a different source for a module
        # name that this path would otherwise claim. Falling back to
        # exec-into-scope here would create a second class population.
        # Falling back to exec-into-scope for either .py or .sage package
        # source is precisely the second loading route that duplicates
        # category/module classes.  Keep legacy loading only for genuinely
        # non-importable session scripts.
        raise ImportError(
            f"{source} is under an import root but is not the canonical source "
            f"for {conflicting_candidate!r}; import the module selected by sageparse instead"
        )
    if module_name is not None:
        imported = _sys.modules[module_name]
        if attach:
            _canonical_attached_modules[str(source)] = module_name
            _install_canonical_attach_reload()
            from sage.repl.attach import add_attached_file as _add_attached_file

            _add_attached_file(source)
        scope.update(
            (name, value)
            for name, value in vars(imported).items()
            if not (name.startswith("__") and name.endswith("__"))
        )
    else:
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
    "dzack_research.preamble.catalogue",
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
_lazy_import("dzack_research.preamble.coble", "Coble")
_lazy_import("dzack_research.preamble.sterk", "Sterk")


_language_runtime.install(globals())
