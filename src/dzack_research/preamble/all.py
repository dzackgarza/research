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
    ArrowCategory,
    AutCategoryConstruction,
    AutCategoryOf,
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
    CosliceCategory,
    DiagramCategory,
    DirectedSystem,
    DirectSumCategory,
    DirectSumDecomposition,
    DirectSumObjects,
    EndArrowCategory,
    EndCategoryConstruction,
    EndCategoryOf,
    EndofunctorAlgebras,
    EpiCategoryConstruction,
    EpiCategoryOf,
    EpimorphismArrowCategory,
    FunctorCategory,
    HomCategories,
    HomCategoryConstruction,
    HomCategoryOf,
    InverseSystem,
    IsoArrowCategory,
    IsoCategoryConstruction,
    IsoCategoryOf,
    Isomorphism,
    LimitsOfCategory,
    MonoCategoryConstruction,
    MonoCategoryOf,
    MonomorphismArrowCategory,
    NaturalTransformationMorphism,
    OppositeMorphism,
    PosetCategory,
    ProductConeCategory,
    ProductMorphism,
    ProductsOfCategory,
    SliceCategory,
    Span,
    SpanCategory,
    SubobjectCategory,
    SubobjectHomset,
    SubobjectMorphism,
    SuperobjectCategory,
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
    NaturalTransformations,
    ObjectSetFunctor,
    compose_functors,
)
from dzack_research.preamble.categories.algebras import (  # noqa: F401
    AlgebraHomset,
    AlgebraMorphism,
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    AlgebrasWithChosenMultiplication,
    AlternatingAlgebraOf,
    AlternatingAlgebraOn,
    AlternatingAlgebras,
    AssociativeAlgebras,
    AssociativeAlgebrasWithChosenMultiplication,
    AugmentedAlgebras,
    CohomologyAlgebra,
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
    DeRhamAlgebra,
    DeRhamAlgebras,
    Derivation,
    Derivations,
    DerivationSpace,
    DGAHomset,
    DGAMorphism,
    Differential,
    DifferentialComponentMorphism,
    DifferentialGradedAlgebras,
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
    GradedCommutator,
    GradedDerivation,
    GradedDerivations,
    GradedDerivationSpace,
    GradedFreeAlgebras,
    GroupAlgebra,
    GroupAlgebraFunctor,
    GroupAlgebras,
    InteriorProduct,
    KahlerDifferentialModules,
    KahlerDifferentials,
    LieAlgebraHomset,
    LieAlgebraMorphism,
    LieAlgebras,
    LieBracket,
    LieDerivative,
    OwnedAlgebras,
    RestrictedGradedAlgebra,
    RestrictedGradedAlgebraElement,
    RestrictedScalarsAlgebras,
    StrictlyCommutativeDifferentialGradedAlgebras,
    StrictlyGradedCommutativeAlgebras,
    SymmetricAlgebraOf,
    SymmetricAlgebraOn,
    SymmetricAlgebras,
    TensorAlgebraOf,
    TensorAlgebraOn,
    TensorAlgebras,
    VectorFields,
    algebra_from_multiplication,
    algebra_homset,
    augmented_algebra,
    cohomology_algebra_homset,
    commutative_algebra_coproduct,
    commutative_algebra_pushout,
    dga_homset,
    graded_algebra_homset,
    lie_algebra_homset,
    own_algebra,
    restrict_algebra_scalars,
    restrict_graded_algebra_scalars,
)
from dzack_research.preamble.categories.algebras.algebras import MatrixAlgebras  # noqa: F401
from dzack_research.preamble.categories.coxeter_diagrams import CoxeterDiagrams  # noqa: F401
from dzack_research.preamble.categories.divisors import (  # noqa: F401
    AffineCodimensionOneChowComparison,
    AffineCycleGroup,
    AffineWeilCycleIsomorphism,
    AlgebraicCycleGroups,
    CartierDivisorGroup,
    CartierDivisorGroups,
    ChowGroup,
    ChowGroups,
    ClosedImmersionCyclePushforward,
    ClassGroup,
    ClassGroups,
    CompleteLinearSystem,
    CompleteLinearSystems,
    CoordinateHyperplaneSectionRestriction,
    CoordinatePointJetEvaluation,
    CoxRing,
    CoxRings,
    DivisorClassComparison,
    DivisorGroup,
    DivisorGroups,
    DistinguishedOpenCyclePullback,
    FiniteAtlasCartierDivisor,
    FiniteAtlasInvertibleSheaf,
    FormalDivisor,
    FormalDivisorGroup,
    FormalDivisorGroups,
    FundamentalCycle,
    HomogeneousPolynomialSectionSpace,
    HomogeneousPolynomialSectionSpaces,
    ImposedPointMultiplicityLinearSystem,
    ImposedMultiplicityLinearSystem,
    ImposedMultiplicityLinearSystems,
    InvertibleSheaf,
    C2DiagonalProductProjectiveAction,
    C2ProductProjectiveLinearization,
    ProductProjectiveLineBundleLinearization,
    C2ProjectiveLineLinearization,
    ProjectiveLineBundleLinearization,
    ProjectiveLineBundleLinearizationIsomorphism,
    ProjectiveLineCoordinateSwapAction,
    LineBundleCohomologySpace,
    LineBundleCohomologySpaces,
    PicardGroup,
    PicardGroups,
    ProjectivePointJetEvaluation,
    ProjectiveSectionRestriction,
    ProductProjectiveSubschemeLineBundle,
    ProductProjectiveSubschemeLineBundleIsomorphism,
    ProjectiveSubschemeLineBundle,
    ProjectiveSubschemeLineBundleIsomorphism,
    ProjectiveJetSpaces,
    ProjectiveLinearSystem,
    ProjectiveLinearSystems,
    SerreIntersection,
    SerreIntersectionData,
    SectionRing,
    SectionRings,
    SectionsVanishingAtPoint,
    SectionsVanishingToOrder,
    TorusInvariantCycleGroups,
    TrivialInvertibleSheaf,
    WeilDivisorGroup,
    WeilDivisorGroups,
    affine_normal_weil_divisor_group,
    projective_space_picard_group,
    trivial_picard_group,
)
from dzack_research.preamble.categories.eichler_criterion import (  # noqa: F401
    are_in_one_stable_orbit,
    covering_discriminant_classes,
    eichler_criterion_applies,
    hyperbolic_plane_summand_count,
    splits_two_hyperbolic_planes,
)
from dzack_research.preamble.categories.forms import (  # noqa: F401
    BilinearForm,
    BilinearFormMorphism,
    BilinearForms,
    PairingMorphism,
    Pairings,
    QuadraticForm,
    QuadraticFormMorphism,
    QuadraticForms,
    gram_tensor_from_graph,
    gram_tensor_graph,
    tensor_connected_component_cuts,
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
from dzack_research.preamble.categories.functors.abelianization import (
    abelianization_adjunction as abelianization_adjunction,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    AlgebraUnderlyingModuleFunctor as AlgebraUnderlyingModuleFunctor,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    algebra_underlying_module_functor as algebra_underlying_module_functor,
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
from dzack_research.preamble.categories.functors.algebra_scalar_change import (
    algebra_base_change_adjunction as algebra_base_change_adjunction,
)
from dzack_research.preamble.categories.functors.cardinality import (
    CardinalityFunctor as CardinalityFunctor,
)
from dzack_research.preamble.categories.functors.cardinality import (
    cardinality_functor as cardinality_functor,
)
from dzack_research.preamble.categories.functors.cochain_complexes import (
    CochainUnderlyingGradedModuleFunctor as CochainUnderlyingGradedModuleFunctor,
)
from dzack_research.preamble.categories.functors.cochain_complexes import (
    cochain_underlying_graded_module_functor as cochain_underlying_graded_module_functor,
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
from dzack_research.preamble.categories.functors.cohomology import (
    cohomology_algebra_functor as cohomology_algebra_functor,
)
from dzack_research.preamble.categories.functors.cohomology import (
    cohomology_functor as cohomology_functor,
)
from dzack_research.preamble.categories.functors.cohomology import (
    de_rham_cohomology_algebra_functor as de_rham_cohomology_algebra_functor,
)
from dzack_research.preamble.categories.functors.cohomology import (
    de_rham_cohomology_functor as de_rham_cohomology_functor,
)
from dzack_research.preamble.categories.functors.core import (
    Adjunction as Adjunction,
)
from dzack_research.preamble.categories.functors.core import (
    CategoryInclusionFunctor as CategoryInclusionFunctor,
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
    category_inclusion as category_inclusion,
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
from dzack_research.preamble.categories.functors.de_rham import (
    de_rham_adjunction as de_rham_adjunction,
)
from dzack_research.preamble.categories.functors.de_rham import (
    de_rham_functor as de_rham_functor,
)
from dzack_research.preamble.categories.functors.de_rham import (
    degree_zero_dga_functor as degree_zero_dga_functor,
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
from dzack_research.preamble.categories.functors.free_algebras import (
    alternating_algebra_functor as alternating_algebra_functor,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    symmetric_algebra_adjunction as symmetric_algebra_adjunction,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    symmetric_algebra_functor as symmetric_algebra_functor,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    tensor_algebra_adjunction as tensor_algebra_adjunction,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    tensor_algebra_functor as tensor_algebra_functor,
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
from dzack_research.preamble.categories.functors.free_forgetful import (
    free_forgetful_adjunction as free_forgetful_adjunction,
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
from dzack_research.preamble.categories.functors.free_forms import (
    bilinear_free_form_adjunction as bilinear_free_form_adjunction,
)
from dzack_research.preamble.categories.functors.free_forms import (
    quadratic_free_form_adjunction as quadratic_free_form_adjunction,
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
from dzack_research.preamble.categories.functors.free_groups import (
    free_group_underlying_set_adjunction as free_group_underlying_set_adjunction,
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
from dzack_research.preamble.categories.functors.group_scalar_change import (
    group_module_base_change_adjunction as group_module_base_change_adjunction,
)
from dzack_research.preamble.categories.functors.hom_packets import (
    InducedAutFunctor as InducedAutFunctor,
)
from dzack_research.preamble.categories.functors.hom_packets import (
    InducedEndFunctor as InducedEndFunctor,
)
from dzack_research.preamble.categories.functors.hom_packets import (
    InducedHomFunctor as InducedHomFunctor,
)
from dzack_research.preamble.categories.functors.hom_packets import (
    induced_aut_functor as induced_aut_functor,
)
from dzack_research.preamble.categories.functors.hom_packets import (
    induced_end_functor as induced_end_functor,
)
from dzack_research.preamble.categories.functors.hom_packets import (
    induced_hom_functor as induced_hom_functor,
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
from dzack_research.preamble.categories.functors.module_localization import (
    module_localization_functor as module_localization_functor,
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
from dzack_research.preamble.categories.functors.orders_number_fields import (
    order_number_field_adjunction as order_number_field_adjunction,
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
from dzack_research.preamble.categories.functors.scalar_change import (
    base_change_adjunction as base_change_adjunction,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    restriction_coextension_adjunction as restriction_coextension_adjunction,
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
from dzack_research.preamble.categories.functors.set_constructions import (
    exponential_functor as exponential_functor,
)
from dzack_research.preamble.categories.functors.set_constructions import (
    finite_power_set_functor as finite_power_set_functor,
)
from dzack_research.preamble.categories.functors.set_constructions import (
    fixed_cardinality_subset_functor as fixed_cardinality_subset_functor,
)
from dzack_research.preamble.categories.functors.set_constructions import (
    inverse_image_power_set_functor as inverse_image_power_set_functor,
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
from dzack_research.preamble.categories.functors.subobject_images import (
    subobject_image_adjunction as subobject_image_adjunction,
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
from dzack_research.preamble.categories.functors.tensor_hom import (
    tensor_hom_adjunction as tensor_hom_adjunction,
)
from dzack_research.preamble.categories.group import (  # noqa: F401
    AbelianGroups,
    AbsoluteDecompositionGroup,
    AbsoluteGaloisGroup,
    AbsoluteGaloisGroupElement,
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
    AbsoluteGaloisSliceAutomorphism,
    AbsoluteInertiaGroup,
    AdditiveGroups,
    ContinuousGroupHomset,
    CyclicGroups,
    CyclotomicCharacter,
    DecompositionGroupConjugacyClass,
    ElementConjugacyClass,
    EquivariantMorphism,
    ExactFieldHomset,
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
    absolute_galois_group,
    absolute_galois_group_category,
    centralizer,
    continuous_group_homset,
    cyclic_subgroup,
    exact_embeddings,
    exact_field_homset,
    extensions_along,
    field_generators,
    finite_decomposition_group,
    finite_frobenius_class,
    finite_g_set,
    finite_inertia_group,
    first_exact_embedding,
    fixed_point_set,
    g_set_homset,
    generated_submonoid,
    group_homset,
    groups,
    open_absolute_galois_subgroup,
    predicate_subgroup,
    predicate_submonoid,
    restrict_along,
    trivial_g_set,
)
from dzack_research.preamble.categories.hyperbolic_lattices import (  # noqa: F401
    HyperbolicLattices,
)
from dzack_research.preamble.categories.isotropic_orbits import (  # noqa: F401
    Cusp,
    IsotropicFlag,
    cusps,
    primitive_isotropic_vectors,
    transport_isotropic_object,
)
from dzack_research.preamble.categories.isotropic_parabolics import (  # noqa: F401
    PrimitiveIsotropicSubobjects,
    primitive_isotropic,
)
from dzack_research.preamble.categories.lattice_centralizers import (  # noqa: F401
    IsometryPrimitiveExtension,
    cyclotomic_summand,
    isometry_primitive_extension,
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
    NondegenerateLattices,
    RootLattices,  # noqa: F401
    diagonal_gram,
    nikulin_invariants,
    signature_pair,
    signature_pairs,
)
from dzack_research.preamble.categories.modules import (  # noqa: F401
    AlgebraicCorrelationMorphism,
    BasedFreeModule,
    BilinearFormModules,
    BilinearMap,
    BiproductModules,
    Boundaries,
    CochainComplex,
    CochainComplexElement,
    CochainComplexes,
    CochainComplexObject,
    CochainDifferential,
    CochainHomset,
    CochainMorphism,
    Cohomology,
    CohomologyModules,
    Connection,
    ConnectionDeRhamDifferential,
    ConnectionDeRhamModule,
    ConnectionHomset,
    ConnectionMorphism,
    Connections,
    ConnectionSpace,
    CorrelationIsomorphism,
    Cycles,
    DeterminantLine,
    DifferentialGradedModules,
    DiscriminantBilinearModules,
    DiscriminantModule,
    DiscriminantModules,
    DiscriminantQuadraticModules,
    DividedSquare,
    DividedSquareModules,
    Ext,
    ExteriorForms,
    ExtMap,
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
    FramingVolumeTrivialization,
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
    HodgeDiscriminant,
    HodgeStar,
    HodgeStarOverFractionField,
    Ideals,
    InternalHom,
    InternalHomModules,
    LinearHomModules,
    LocalizedModules,
    ModuleEmbedding,
    Modules,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    ModulesWithConnection,
    ModulesWithFlatConnection,
    ModuleWithConnection,
    MultivectorHodgeStar,
    PairedModules,
    PoincareDuality,
    ProjectiveModules,
    QuadraticFormModules,
    QuadraticSquare,
    RestrictedScalarsModules,
    RestrictedScalarsModuleView,
    SymmetricBilinearFormModules,
    TensorProductModules,
    Tor,
    TorMap,
    TorsionBilinearFormModules,
    TorsionFormIsometry,
    TorsionModule,
    TorsionModules,
    TorsionQuadraticFormModules,
    VectorSpaces,
    VolumeTrivialization,
    biproduct_morphism,
    cochain_homset,
    connection_homset,
    divided_square_morphism,
    fibered_formed_module_homset,
    form_embedding,
    formed_module_homset,
    free_resolution,
    internal_hom_morphism,
    module_embedding,
    module_from_action,
    module_homset,
    regular_dg_module,
    restrict_scalars,
    ring_as_module,
    sub_framing_morphism,
    tensor_product_morphism,
    twist_scalar_action,
)
from dzack_research.preamble.categories.modules.pure.modules import (  # noqa: F401
    MatrixEndomorphismSpaces,
    MatrixSpaces,
)
from dzack_research.preamble.categories.rational_integral_stabilizers import (  # noqa: F401
    integral_double_cosets,
    integral_right_cosets,
    integral_stabilizer,
    integral_transporter,
)
from dzack_research.preamble.categories.rational_lattices import RationalLattices  # noqa: F401
from dzack_research.preamble.categories.reduction_complexes import (  # noqa: F401
    lorentzian_reduction_complex,
)
from dzack_research.preamble.categories.schemes import (  # noqa: F401
    AT21ADEPair,
    AT21ToricADEPair,
    EnriquesMarkedIntegralCohomology,
    HorikawaEnriquesBaseChangeComparison,
    HorikawaEnriquesSurface,
    horikawa_enriques_surface,
    ADELogPair,
    ADELogPairs,
    AffineGroupSchemeActions,
    AffineGroupSchemes,
    AffineGSchemes,
    AffineModuleSheaf,
    AffineSpaceAnalytificationFunctor,
    AnalyticDiscFamily,
    CyclicCoverBaseChangeComparison,
    RelativeCyclicCoverLift,
    cyclic_cover_base_change,
    relative_cyclic_cover_lift,
    HorikawaK3BaseChangeComparison,
    HorikawaK3DoubleCover,
    HorikawaK3Family,
    horikawa_k3_family,
    HigherDirectImageSheaf,
    IntegralLocalSystem,
    LegendreMonodromyFamily,
    PointedAnalyticFundamentalGroup,
    legendre_monodromy_family,
    analytic_disc_family,
    AffineInvariantQuotientBaseChangeComparison,
    reynolds_invariant_base_change_hypothesis,
    AffineSchemes,
    AffineSpace,
    AffineSpaces,
    AffineSpecFunctor,
    ClosedEmbeddings,
    ClosedSubschemes,
    ConvexPolygon,
    ConvexPolygons,
    ConvexPolytope,
    ConvexPolytopes,
    CoverRefinement,
    Curves,
    CurveGenusComparison,
    CurveLocalDeltaContribution,
    ProjectiveCurveNormalizationData,
    rational_quintic_with_nonrational_node_normalization,
    rational_quintic_with_two_nodes_normalization,
    DistinguishedAffineCover,
    FiberProductSchemes,
    FiniteGluedInvariantQuotient,
    FiniteTypeSchemes,
    IntegralSchemes,
    IsolatedHypersurfaceSingularity,
    LatticePolygon,
    LatticePolygons,
    LatticePolytope,
    LatticePolytopes,
    LocallyRingedSpaces,
    LogPair,
    LogPairs,
    NormalSchemes,
    OpenImmersions,
    ProductProjectiveSpaces,
    ProductSchemes,
    CompleteIntersectionAdjunctionComparison,
    ProjectivePointBlowup,
    ProjectivePointBlowupCanonicalComparison,
    ProjectivePointBlowups,
    ProjectiveCompleteIntersection,
    ProjectiveCompleteIntersections,
    ProjectiveSchemes,
    ProjectiveSpace,
    ProjectiveSpaces,
    QuasiAffineSchemes,
    QuasiCoherentSheaves,
    QuasiProjectiveSchemes,
    RationalPolyhedralFans,
    RelativeAffineFamily,
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
    SpecFunctor,
    StructureSheaf,
    Surfaces,
    GeometricFundamentalGroups,
    NodalCubicFundamentalGroup,
    PGL2FundamentalGroup,
    ProjectiveLineFundamentalGroup,
    IntegralTopologicalCohomologyGroups,
    ResolutionIntegralCohomologyGroups,
    NodalCubic,
    NodalCubicNormalization,
    NodalCubicIntegralTopology,
    IntegralSingularCohomologyGroups,
    PGL2IntegralCohomology,
    PGL2IntegralTopology,
    ProjectiveGeneralLinearGroup2,
    QuarticK3HodgeData,
    QuarticK3IntegralCohomology,
    QuarticK3IntegralTopology,
    ToricCycleClassIsomorphism,
    ToricFixedPointBlowup,
    ToricFixedPointBlowups,
    ToricFundamentalGroup,
    ToricFundamentalGroups,
    ToricGeometricLineBundleCohomologySpaces,
    ToricHodgeData,
    ToricHodgeStructure,
    ToricIntegralSingularCohomology,
    ToricIntegralSingularCohomologyGroups,
    ToricLineBundleCohomology,
    ToricLogPair,
    ToricLogPairs,
    ToricMiddleCohomologyForm,
    ToricPicardToChowIsomorphism,
    ToricSchemes,
    ToricVariety,
    ToricWeightCohomology,
    ToricWeightCohomologyComplex,
    ToricWeightCohomologyComplexes,
    Varieties,
    affine_equation_family,
    affine_spec_functor,
    glued_invariant_quotient,
    roots_of_unity_group_scheme,
    scheme_base_change_functor,
    scheme_fiber_product,
    scheme_product,
    slice_base_change_adjunction,
)
from dzack_research.preamble.categories.schemes.cyclic_covers import (  # noqa: F401
    CyclicCovers,
)
from dzack_research.preamble.categories.sets import (  # noqa: F401
    NN,
    CardinalComparison,
    Cardinalities,
    CartesianProductMorphism,
    CartesianProductOfFamily,
    CartesianProductOfSets,
    CartesianProductsOfSets,
    ConditionSet,
    CoproductMorphism,
    CoproductOfFamily,
    CoproductOfSets,
    CoproductsOfSets,
    CountableSets,
    CountablyInfiniteSets,
    DisjointUnionsOfSets,
    EnumeratedByIntegers,
    EnumeratedByNaturals,
    EnumeratedSets,
    ExponentialOfSets,
    FinitelySupportedFunctionSets,
    FinitePowerSets,
    FiniteSets,
    FiniteSubsets,
    FourierCharacters,
    FunctionEnumeratedSets,
    HermitePolynomials,
    ImageSet,
    InfiniteEnumeratedSets,
    InfiniteSets,
    LaurentMonomials,
    ObjectSetsOfDiscreteCategories,
    Ordinals,
    OrdinalSemirings,
    PartiallyOrderedSets,
    PowerSet,
    PowerSets,
    Set,
    SetInclusion,
    SetInjection,
    Sets,
    SetSurjection,
    SincTranslates,
    SubsetsOfSize,
    TotallyOrderedSets,
    UncountableSets,
    aleph,
    aleph0,
    cardinal,
    cartesian_product_of,
    continuum,
    omega,
    omega0,
    ordinal,
    set_injection,
    set_surjection,
)
from dzack_research.preamble.categories.vector_configurations import (  # noqa: F401
    VectorConfigurations,
    vector_configuration,
)
from dzack_research.preamble.categories.vector_orbits import (  # noqa: F401
    VectorPrimitiveExtension,
    definite_complement_extensions,
    gluing_route_discriminant_classes,
)
from dzack_research.preamble.categories.vinberg_invariants import (  # noqa: F401
    VinbergInvariantMatrices,
    reflection_cosines,
)
from dzack_research.preamble.coble import Coble  # noqa: F401
from dzack_research.preamble.logic import Predicate, Unknown, ask  # noqa: F401
from dzack_research.preamble.rings import (  # noqa: F401
    RR,
    ZZ,
    AdicallyCompleteRings,
    ArtinianRings,
    CommutativeIdeal,
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
    ResidueField,
    Rings,
    UnitInterval,
    ZariskiClosedSubobject,
    _restore_session_ring_bindings,  # noqa: F401
    predicate_subring,
)
from dzack_research.preamble.sterk import Sterk  # noqa: F401
from dzack_research.preamble.tensors import Tensor, TensorModule, tensor  # noqa: F401
from dzack_research.preamble.utilities import lmap, lzip, to_var_names, zipsum  # noqa: F401

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
    from dzack_research.preamble.categories.rings.ring_foundation import (
        OwnedCategoryOverBaseRing,
    )

    session = globals()
    for _name in sorted(session):
        _value = session[_name]
        if isinstance(_value, type) and issubclass(_value, OwnedCategoryOverBaseRing):
            _value(_ring)._cmp_key


for _initial_ring in (ZZ,):
    _realize_owned_categories_over(_initial_ring)
