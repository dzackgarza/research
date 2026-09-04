from __future__ import annotations

from shape_extensions import Int
from typing import assert_type

from dzack_research.static_types import (
    AutObject,
    AlgebraBaseChangeAdjunction,
    AlgebraElement,
    AlgebraMorphism,
    AlgebraModuleTag,
    AlgebraParent,
    AlgebraRestrictionFunctor,
    AlgebraRing,
    AlgebraScalarExtensionFunctor,
    BaseChangedRelativeContext,
    BaseChangedStructure,
    Automorphism,
    BilinearForm,
    CategoricalMorphism,
    CategoryFunctor,
    CategoryObject,
    Cochain,
    CochainCohomologyMorphism,
    CochainComplex,
    CochainMorphism,
    CochainPiece,
    CochainPieceTag,
    CohomologyClass,
    CohomologyModule,
    CohomologyMorphism,
    CoefficientForm,
    Covector,
    DGAMorphism,
    DeRhamAlgebra,
    DeRhamClass,
    Degree,
    Derivation,
    DerivationSpace,
    DifferentialForm,
    DifferentialOperator,
    Dual,
    DualBilinearForm,
    EndObject,
    EndomorphismArrow,
    ExteriorElement,
    ExteriorPower,
    ExteriorPowerTag,
    FiniteFreeModule,
    FlatConnection,
    FractionFieldCovariantForm,
    FreeModuleIsomorphism,
    FreeModuleMorphism,
    FunctorImage,
    DifferentialGradedCarrier,
    GradedMorphism,
    GradedDerivationOperator,
    HomogeneousElement,
    HomObject,
    InducedAutFunctor,
    InducedEndFunctor,
    InducedHomFunctor,
    InteriorOperator,
    IsoObject,
    KahlerClassifier,
    KahlerClassifierIsomorphism,
    KahlerDifferentials,
    KahlerOneForm,
    KahlerPForm,
    KahlerTag,
    LieDerivativeOperator,
    LinearMap,
    Metric,
    MetricCovariantForm,
    MetricScalarRing,
    ModuleElement,
    ModuleBaseChangeAdjunction,
    ModuleEnd,
    ModuleEndomorphism,
    ModuleHom,
    ModuleMorphism,
    ModuleParent,
    ModuleRestrictionFunctor,
    ModuleScalarExtensionFunctor,
    ModuleStructure,
    Multivector,
    NondegenerateMetric,
    PerfectMetric,
    RelativeAlgebraMorphism,
    RelativeContext,
    RestrictedModule,
    RestrictedAlgebra,
    RingMorphism,
    Scalar,
    ScalarExtendedAlgebra,
    ScalarExtendedModule,
    UniversalDerivation,
    Vector,
    VectorField,
    Volume,
    apply,
    apply_module_morphism,
    algebra_base_change,
    algebra_base_change_counit,
    algebra_base_change_unit,
    algebra_element_view,
    algebra_morphism_view,
    algebra_view,
    base_changed_relative_context,
    bilinear_form_view,
    categorical_isomorphism_view,
    category_object_view,
    class_of_cycle,
    classifier_from_derivation,
    cochain_complex_view,
    cochain_d,
    cochain_map,
    cochain_morphism_view,
    cochain_of,
    cochain_piece,
    coefficient_form_view,
    compose,
    compose_automorphisms,
    compose_endomorphisms,
    compose_module_morphisms,
    compose_morphisms,
    correlation_isomorphism,
    correlation_morphism,
    covariant_d,
    covector_of,
    cup,
    cycle_representative,
    d,
    dga_d,
    degree_view,
    derive,
    derivation_from_classifier,
    derivation_space_view,
    derivation_view,
    de_rham_cohomology_map,
    de_rham_algebra_view,
    de_rham_class_view,
    de_rham_map,
    differential_operator_of,
    dual_tensor,
    dual_module,
    dualize_module_morphism,
    embed_function,
    embed_exterior_form,
    embed_kahler_one_form,
    extend_algebra,
    extend_algebra_morphism,
    flat_connection_view,
    finite_free_module_view,
    form_hodge_star_over_fraction_field,
    form_of,
    form_hodge_star,
    form_view,
    free_module_morphism_view,
    free_module_morphism_of,
    fraction_field_covariant_form_view,
    functor_morphism_image,
    functor_object_image,
    functor_view,
    graded_commutator,
    graded_derivation_operator_view,
    graded_map,
    graded_morphism_view,
    graded_multiply,
    homogeneous_element_view,
    differential_graded_carrier_view,
    hom_object_view,
    identity_automorphism,
    identity_endomorphism,
    induced_aut,
    induced_end,
    induced_hom,
    interior,
    interior_operator_of,
    inverse_automorphism,
    iso_object_view,
    kahler_classifier_isomorphism,
    kahler_differentials_view,
    kahler_one_form_view,
    lie_bracket,
    lie_derivative,
    lie_derivative_operator_of,
    linear_map_view,
    linear_map_of,
    lower_index,
    metric_view,
    metric_tensor,
    metric_covariant_form_view,
    nondegenerate_metric_view,
    module_element_view,
    module_element_of,
    module_hom_view,
    module_base_change,
    module_base_change_counit,
    module_base_change_unit,
    module_action,
    map_cohomology_class,
    module_morphism_tensor,
    module_morphism_view,
    module_base_change_adjunction_view,
    module_view,
    module_morphism_of,
    module_structure_view,
    morphism_view,
    multivector_hodge_star,
    double_dual_morphism,
    multivector_view,
    multivector_of,
    pair,
    precompose_covector,
    perfect_metric_view,
    pullback_de_rham_class,
    pullback_bilinear_form,
    pullback_form,
    raise_index,
    covector_view,
    relative_algebra_morphism_view,
    relative_context_view,
    restrict_module,
    restrict_module_morphism,
    restrict_algebra,
    restrict_algebra_morphism,
    ring_morphism_view,
    scalar_view,
    extend_module,
    extend_module_morphism,
    exterior_component,
    exterior_one,
    exterior_power,
    exterior_element_view,
    cohomology_map,
    cohomology_of,
    universal_derivation,
    universal_derivation_view,
    vector_field_view,
    vector_view,
    vector_of,
    volume_view,
    wedge_exterior,
    wedge,
)


class R: ...
class U: ...
class V: ...
class W: ...


class G: ...
class H: ...


graded_two: HomogeneousElement[G, 2] = homogeneous_element_view(object())
graded_three: HomogeneousElement[G, 3] = homogeneous_element_view(object())
graded_morphism: GradedMorphism[G, H] = graded_morphism_view(object())
dga_g: DifferentialGradedCarrier[G] = differential_graded_carrier_view(object())

assert_type(graded_multiply(graded_two, graded_three), HomogeneousElement[G, 5])
assert_type(graded_map(graded_morphism, graded_two), HomogeneousElement[H, 2])
assert_type(dga_d(dga_g, graded_two), HomogeneousElement[G, 3])


module_element: ModuleElement[R, U] = module_element_view(object())
module_f: ModuleMorphism[R, U, V] = module_morphism_view(object())
module_g: ModuleMorphism[R, V, W] = module_morphism_view(object())
free_module_f: FreeModuleMorphism[R, U, 2, V, 3] = free_module_morphism_view(object())
module_hom: ModuleHom[R, U, V] = module_hom_view(object())
module_end: ModuleEnd[R, U] = module_hom_view(object())
module_u: ModuleParent[R, U] = module_view(object())
module_v: ModuleParent[R, V] = module_view(object())
module_structure: ModuleStructure[R, U] = module_structure_view(object())
scalar_r: Scalar[R] = scalar_view(object())
rank_u: Int[2] = 2
rank_v: Int[3] = 3
finite_u: FiniteFreeModule[R, U, 2] = finite_free_module_view(object())
finite_v: FiniteFreeModule[R, V, 3] = finite_free_module_view(object())

anchored_u = module_element_of(module_u, object())
anchored_module_f = module_morphism_of(module_u, module_v, object())
anchored_free_f = free_module_morphism_of(
    module_u, rank_u, module_v, rank_v, object()
)
anchored_vector = vector_of(module_u, rank_u, object())
anchored_covector = covector_of(module_u, rank_u, object())
anchored_linear = linear_map_of(module_u, rank_u, module_v, rank_v, object())

assert_type(anchored_u, ModuleElement[R, U])
assert_type(anchored_module_f, ModuleMorphism[R, U, V])
assert_type(anchored_free_f, FreeModuleMorphism[R, U, 2, V, 3])
assert_type(anchored_vector, Vector[R, U, 2])
assert_type(anchored_covector, Covector[R, U, 2])
assert_type(anchored_linear, LinearMap[R, U, 2, V, 3])

assert_type(apply_module_morphism(module_f, module_element), ModuleElement[R, V])
assert_type(
    compose_module_morphisms(module_g, module_f),
    ModuleMorphism[R, U, W],
)
assert_type(module_morphism_tensor(free_module_f), LinearMap[R, U, 2, V, 3])
dual_f = dualize_module_morphism(free_module_f)
assert_type(dual_module(finite_u), FiniteFreeModule[R, Dual[U], 2])
assert_type(
    dual_f,
    FreeModuleMorphism[R, Dual[V], 3, Dual[U], 2],
)
assert_type(
    module_morphism_tensor(dual_f),
    LinearMap[R, Dual[V], 3, Dual[U], 2],
)
assert_type(
    double_dual_morphism(finite_u),
    FreeModuleMorphism[R, U, 2, Dual[Dual[U]], 2],
)
assert_type(module_hom, ModuleHom[R, U, V])
assert_type(module_end, ModuleHom[R, U, U])
assert_type(module_structure(scalar_r), ModuleEndomorphism[R, U])
assert_type(module_action(module_structure, scalar_r, anchored_u), ModuleElement[R, U])


class SBase: ...
class Phi: ...
class AlgA: ...
class AlgB: ...
class AlgC: ...


ring_map: RingMorphism[R, SBase, Phi] = ring_morphism_view(object())
algebra_a: AlgebraParent[R, AlgA] = algebra_view(object())
algebra_b: AlgebraParent[SBase, AlgB] = algebra_view(object())
algebra_c: AlgebraParent[R, AlgC] = algebra_view(object())
algebra_map: AlgebraMorphism[R, AlgA, AlgC] = algebra_morphism_view(object())
algebra_map_b: AlgebraMorphism[SBase, AlgB, AlgB] = algebra_morphism_view(object())

algebra_adjunction = algebra_base_change(ring_map)
extended_a = extend_algebra(ring_map, algebra_a)
restricted_b = restrict_algebra(ring_map, algebra_b)
extended_map = extend_algebra_morphism(ring_map, algebra_map)
restricted_map = restrict_algebra_morphism(ring_map, algebra_map_b)

assert_type(algebra_adjunction, AlgebraBaseChangeAdjunction[R, SBase, Phi])
assert_type(
    algebra_adjunction.left_adjoint(),
    AlgebraScalarExtensionFunctor[R, SBase, Phi],
)
assert_type(
    algebra_adjunction.right_adjoint(),
    AlgebraRestrictionFunctor[R, SBase, Phi],
)
assert_type(extended_a, AlgebraParent[SBase, ScalarExtendedAlgebra[Phi, AlgA]])
assert_type(restricted_b, AlgebraParent[R, RestrictedAlgebra[Phi, AlgB]])
assert_type(
    extended_map,
    AlgebraMorphism[
        SBase,
        ScalarExtendedAlgebra[Phi, AlgA],
        ScalarExtendedAlgebra[Phi, AlgC],
    ],
)
assert_type(
    restricted_map,
    AlgebraMorphism[
        R,
        RestrictedAlgebra[Phi, AlgB],
        RestrictedAlgebra[Phi, AlgB],
    ],
)
assert_type(
    algebra_base_change_unit(algebra_adjunction, algebra_a),
    AlgebraMorphism[
        R,
        AlgA,
        RestrictedAlgebra[Phi, ScalarExtendedAlgebra[Phi, AlgA]],
    ],
)
assert_type(
    algebra_base_change_counit(algebra_adjunction, algebra_b),
    AlgebraMorphism[
        SBase,
        ScalarExtendedAlgebra[Phi, RestrictedAlgebra[Phi, AlgB]],
        AlgB,
    ],
)


module_s_w: ModuleParent[SBase, W] = module_view(object())
module_map_s: ModuleMorphism[SBase, W, W] = module_morphism_view(object())
module_adjunction = module_base_change(ring_map)
module_adjunction_viewed: ModuleBaseChangeAdjunction[R, SBase, Phi] = (
    module_base_change_adjunction_view(object())
)
extended_u = extend_module(ring_map, module_u)
restricted_w = restrict_module(ring_map, module_s_w)
extended_module_map = extend_module_morphism(ring_map, module_f)
restricted_module_map = restrict_module_morphism(ring_map, module_map_s)

assert_type(module_adjunction, ModuleBaseChangeAdjunction[R, SBase, Phi])
assert_type(module_adjunction_viewed, ModuleBaseChangeAdjunction[R, SBase, Phi])
assert_type(
    module_adjunction.left_adjoint(),
    ModuleScalarExtensionFunctor[R, SBase, Phi],
)
assert_type(
    module_adjunction.right_adjoint(),
    ModuleRestrictionFunctor[R, SBase, Phi],
)
assert_type(extended_u, ModuleParent[SBase, ScalarExtendedModule[Phi, U]])
assert_type(restricted_w, ModuleParent[R, RestrictedModule[Phi, W]])
assert_type(
    extended_module_map,
    ModuleMorphism[
        SBase,
        ScalarExtendedModule[Phi, U],
        ScalarExtendedModule[Phi, V],
    ],
)
assert_type(
    restricted_module_map,
    ModuleMorphism[
        R,
        RestrictedModule[Phi, W],
        RestrictedModule[Phi, W],
    ],
)
assert_type(
    module_base_change_unit(module_adjunction, module_u),
    ModuleMorphism[
        R,
        U,
        RestrictedModule[Phi, ScalarExtendedModule[Phi, U]],
    ],
)
assert_type(
    module_base_change_counit(module_adjunction, module_s_w),
    ModuleMorphism[
        SBase,
        ScalarExtendedModule[Phi, RestrictedModule[Phi, W]],
        W,
    ],
)


class K: ...
class L: ...


cochain_degree_zero: Degree[0] = degree_view(0)
cochain_degree_one: Degree[1] = degree_view(1)
complex_k: CochainComplex[R, K] = cochain_complex_view(object())
complex_l: CochainComplex[R, L] = cochain_complex_view(object())
chain_map: CochainMorphism[R, K, L] = cochain_morphism_view(object())

piece_zero = cochain_piece(complex_k, cochain_degree_zero)
cochain_zero = cochain_of(complex_k, cochain_degree_zero, object())
cochain_one = cochain_d(complex_k, cochain_degree_zero, cochain_zero)
mapped_zero = cochain_map(chain_map, cochain_degree_zero, cochain_zero)
h_zero = cohomology_of(complex_k, cochain_degree_zero)
h_class = class_of_cycle(h_zero, cochain_zero)
h_representative = cycle_representative(h_zero, h_class)
h_map = cohomology_map(chain_map, cochain_degree_zero)

assert_type(piece_zero, CochainPiece[R, K, 0])
assert_type(cochain_zero, Cochain[R, K, 0])
assert_type(cochain_one, Cochain[R, K, 1])
assert_type(mapped_zero, Cochain[R, L, 0])
assert_type(h_zero, CohomologyModule[R, K, 0])
assert_type(h_class, CohomologyClass[R, K, 0])
assert_type(h_representative, Cochain[R, K, 0])
assert_type(h_map, CochainCohomologyMorphism[R, K, L, 0])
assert_type(
    map_cohomology_class(chain_map, cochain_degree_zero, h_class),
    CohomologyClass[R, L, 0],
)
assert_type(
    chain_map.component(cochain_degree_one),
    ModuleMorphism[R, CochainPieceTag[K, 1], CochainPieceTag[L, 1]],
)


class C: ...
class X: ...
class Y: ...
class Z: ...
class D: ...
class FTag: ...


x_object: CategoryObject[C, X] = category_object_view(object())
y_object: CategoryObject[C, Y] = category_object_view(object())
f_arrow: CategoricalMorphism[C, X, Y] = morphism_view(object())
g_arrow: CategoricalMorphism[C, Y, Z] = morphism_view(object())
end_x: EndObject[C, X] = hom_object_view(object())
aut_x: AutObject[C, X] = iso_object_view(object())
endomorphism_x: EndomorphismArrow[C, X] = morphism_view(object())
automorphism_x: Automorphism[C, X] = categorical_isomorphism_view(object())
assert_type(x_object, CategoryObject[C, X])
assert_type(
    compose_morphisms(g_arrow, f_arrow),
    CategoricalMorphism[C, X, Z],
)
assert_type(end_x, HomObject[C, X, X])
assert_type(aut_x, IsoObject[C, X, X])
assert_type(identity_endomorphism(end_x), EndomorphismArrow[C, X])
assert_type(
    compose_endomorphisms(endomorphism_x, endomorphism_x),
    EndomorphismArrow[C, X],
)
assert_type(identity_automorphism(aut_x), Automorphism[C, X])
assert_type(
    compose_automorphisms(automorphism_x, automorphism_x),
    Automorphism[C, X],
)
assert_type(inverse_automorphism(automorphism_x), Automorphism[C, X])

functor: CategoryFunctor[C, D, FTag] = functor_view(object())
image_x = functor_object_image(functor, x_object)
image_f = functor_morphism_image(functor, f_arrow)
hom_transport = induced_hom(functor, x_object, y_object)
end_transport = induced_end(functor, x_object)
aut_transport = induced_aut(functor, x_object)

assert_type(image_x, CategoryObject[D, FunctorImage[FTag, X]])
assert_type(
    image_f,
    CategoricalMorphism[D, FunctorImage[FTag, X], FunctorImage[FTag, Y]],
)
assert_type(hom_transport, InducedHomFunctor[FTag, C, D, X, Y])
assert_type(end_transport, InducedEndFunctor[FTag, C, D, X])
assert_type(aut_transport, InducedAutFunctor[FTag, C, D, X])
assert_type(hom_transport.domain(), HomObject[C, X, Y])
assert_type(
    hom_transport.codomain(),
    HomObject[D, FunctorImage[FTag, X], FunctorImage[FTag, Y]],
)
assert_type(end_transport.domain(), EndObject[C, X])
assert_type(end_transport.codomain(), EndObject[D, FunctorImage[FTag, X]])
assert_type(aut_transport.domain(), AutObject[C, X])
assert_type(aut_transport.codomain(), AutObject[D, FunctorImage[FTag, X]])
assert_type(
    hom_transport(f_arrow),
    CategoricalMorphism[D, FunctorImage[FTag, X], FunctorImage[FTag, Y]],
)
assert_type(
    end_transport(endomorphism_x),
    EndomorphismArrow[D, FunctorImage[FTag, X]],
)
assert_type(
    aut_transport(automorphism_x),
    Automorphism[D, FunctorImage[FTag, X]],
)


u: Vector[R, U, 2] = vector_view(object())
v: Vector[R, V, 3] = vector_view(object())
f: LinearMap[R, U, 2, V, 3] = linear_map_view(object())
g: LinearMap[R, V, 3, W, 4] = linear_map_view(object())
b: BilinearForm[R, V, 3] = bilinear_form_view(object())
alpha: Covector[R, V, 3] = covector_view(object())

assert_type(apply(f, u), Vector[R, V, 3])
assert_type(compose(g, f), LinearMap[R, U, 2, W, 4])
assert_type(lower_index(b, v), Covector[R, V, 3])
assert_type(pair(alpha, v), Scalar[R])
assert_type(precompose_covector(alpha, f), Covector[R, U, 2])
assert_type(pullback_bilinear_form(b, free_module_f), BilinearForm[R, U, 2])
dual_b = dual_tensor(b)
assert_type(dual_b, DualBilinearForm[R, V, 3])
assert_type(raise_index(dual_b, alpha), Vector[R, V, 3])


class Eta: ...
class A: ...
type Ctx = RelativeContext[Eta, R, A]
class TargetEta: ...
class B: ...
type TargetCtx = RelativeContext[TargetEta, R, B]
context_value: Ctx = relative_context_view(object())
degree_one: Degree[1] = degree_view(1)
degree_two: Degree[2] = degree_view(2)
base_changed_context = base_changed_relative_context(ring_map, context_value)
assert_type(
    base_changed_context,
    BaseChangedRelativeContext[R, SBase, Phi, Eta, A],
)
assert_type(
    base_changed_context,
    RelativeContext[
        BaseChangedStructure[Phi, Eta],
        SBase,
        ScalarExtendedAlgebra[Phi, A],
    ],
)

anchored_one_form = form_of(context_value, degree_one, object())
anchored_one_vector = multivector_of(context_value, degree_one, object())
anchored_d_operator = differential_operator_of(context_value, object())
anchored_i_operator = interior_operator_of(context_value, object())
anchored_lie_operator = lie_derivative_operator_of(context_value, object())
assert_type(anchored_one_form, DifferentialForm[Ctx, 1])
assert_type(anchored_one_vector, Multivector[Ctx, 1])
assert_type(anchored_d_operator, DifferentialOperator[Ctx])
assert_type(anchored_i_operator, InteriorOperator[Ctx])
assert_type(anchored_lie_operator, LieDerivativeOperator[Ctx])
d_as_derivation: GradedDerivationOperator[Ctx, 1] = graded_derivation_operator_view(
    anchored_d_operator
)
i_as_derivation: GradedDerivationOperator[Ctx, -1] = graded_derivation_operator_view(
    anchored_i_operator
)
lie_as_derivation: GradedDerivationOperator[Ctx, 0] = graded_derivation_operator_view(
    anchored_lie_operator
)


class E: ...


algebra_element: AlgebraElement[Ctx] = algebra_element_view(object())
omega: KahlerDifferentials[Ctx] = kahler_differentials_view(object())
kahler_one_form: KahlerOneForm[Ctx] = kahler_one_form_view(object())
target_a_module: ModuleParent[AlgebraRing[Ctx], E] = module_view(object())
derivation_space: DerivationSpace[Ctx, E] = derivation_space_view(object())
derivation: Derivation[Ctx, E] = derivation_view(object())
universal_view: UniversalDerivation[Ctx] = universal_derivation_view(object())

universal = universal_derivation(omega)
classifier = classifier_from_derivation(omega, derivation)
classifier_iso = kahler_classifier_isomorphism(omega, target_a_module)
de_rham_algebra: DeRhamAlgebra[Ctx] = de_rham_algebra_view(object())

assert_type(kahler_one_form, KahlerOneForm[Ctx])
assert_type(derivation_space, DerivationSpace[Ctx, E])
assert_type(universal, UniversalDerivation[Ctx])
assert_type(derive(universal, algebra_element), KahlerOneForm[Ctx])
assert_type(derive(universal_view, algebra_element), KahlerOneForm[Ctx])
assert_type(classifier, KahlerClassifier[Ctx, E])
assert_type(
    derivation_from_classifier(omega, target_a_module, classifier),
    Derivation[Ctx, E],
)
assert_type(classifier_iso, KahlerClassifierIsomorphism[Ctx, E])
assert_type(embed_function(de_rham_algebra, algebra_element), DifferentialForm[Ctx, 0])
assert_type(
    embed_kahler_one_form(de_rham_algebra, kahler_one_form),
    DifferentialForm[Ctx, 1],
)

omega_two = exterior_power(omega, degree_two)
omega_one_element = exterior_one(omega, kahler_one_form)
omega_two_element = wedge_exterior(
    omega,
    degree_one,
    omega_one_element,
    degree_one,
    omega_one_element,
)
synthetic_two: KahlerPForm[Ctx, 2] = exterior_element_view(object())

assert_type(
    omega_two,
    ExteriorPower[AlgebraRing[Ctx], KahlerTag[Ctx], 2],
)
assert_type(
    omega_one_element,
    ExteriorElement[AlgebraRing[Ctx], KahlerTag[Ctx], 1],
)
assert_type(omega_two_element, KahlerPForm[Ctx, 2])
assert_type(synthetic_two, KahlerPForm[Ctx, 2])
embedded_two = embed_exterior_form(de_rham_algebra, degree_two, omega_two_element)
assert_type(embedded_two, DifferentialForm[Ctx, 2])
assert_type(
    exterior_component(de_rham_algebra, degree_two, embedded_two),
    KahlerPForm[Ctx, 2],
)


one_form: DifferentialForm[Ctx, 1] = form_view(object())
two_form: DifferentialForm[Ctx, 2] = form_view(object())
vector_field: VectorField[Ctx] = vector_field_view(object())
assert_type(wedge(one_form, two_form), DifferentialForm[Ctx, 3])
assert_type(d(two_form), DifferentialForm[Ctx, 3])
assert_type(interior(vector_field, two_form), DifferentialForm[Ctx, 1])
assert_type(lie_derivative(vector_field, two_form), DifferentialForm[Ctx, 2])
assert_type(lie_bracket(vector_field, vector_field), VectorField[Ctx])
assert_type(
    derive(vector_field, algebra_element),
    ModuleElement[AlgebraRing[Ctx], AlgebraModuleTag[Ctx]],
)
assert_type(
    graded_commutator(d_as_derivation, i_as_derivation),
    GradedDerivationOperator[Ctx, 0],
)
assert_type(
    graded_commutator(lie_as_derivation, i_as_derivation),
    GradedDerivationOperator[Ctx, -1],
)

metric: Metric[Ctx, 3] = metric_view(object())
nondegenerate_metric: NondegenerateMetric[Ctx, 3] = nondegenerate_metric_view(object())
perfect_metric: PerfectMetric[Ctx, 3] = perfect_metric_view(object())
volume: Volume[Ctx, 3] = volume_view(object())
p: Degree[1] = degree_view(1)
one_vector: Multivector[Ctx, 1] = multivector_view(object())
metric_one_form: MetricCovariantForm[Ctx, 1] = metric_covariant_form_view(object())
fraction_one_form: FractionFieldCovariantForm[Ctx, 1] = (
    fraction_field_covariant_form_view(object())
)

assert_type(
    metric_tensor(metric),
    BilinearForm[MetricScalarRing[Ctx], Ctx, 3],
)
assert_type(
    correlation_morphism(metric),
    FreeModuleMorphism[MetricScalarRing[Ctx], Ctx, 3, Dual[Ctx], 3],
)
correlation = correlation_isomorphism(perfect_metric)
assert_type(
    correlation,
    FreeModuleIsomorphism[MetricScalarRing[Ctx], Ctx, 3, Dual[Ctx], 3],
)
assert_type(
    correlation.forward(),
    FreeModuleMorphism[MetricScalarRing[Ctx], Ctx, 3, Dual[Ctx], 3],
)
assert_type(
    correlation.inverse(),
    FreeModuleMorphism[MetricScalarRing[Ctx], Dual[Ctx], 3, Ctx, 3],
)

correlation_inverse_exterior = exterior_power_morphism(
    correlation.inverse(),
    degree_one,
)
poincare = poincare_duality(metric, volume, degree_one)
star_isomorphism = hodge_star_isomorphism(perfect_metric, volume, degree_one)
hodge_composite = compose_module_morphisms(
    poincare.forward(),
    correlation_inverse_exterior,
)

assert_type(
    correlation_inverse_exterior,
    ModuleMorphism[
        MetricScalarRing[Ctx],
        ExteriorPowerTag[Dual[Ctx], 1],
        ExteriorPowerTag[Ctx, 1],
    ],
)
assert_type(poincare, PoincareDualityIsomorphism[Ctx, 3, 1])
assert_type(star_isomorphism, HodgeStarIsomorphism[Ctx, 3, 1])
assert_type(
    hodge_composite,
    ModuleMorphism[
        MetricScalarRing[Ctx],
        ExteriorPowerTag[Dual[Ctx], 1],
        ExteriorPowerTag[Dual[Ctx], 2],
    ],
)
assert_type(
    star_isomorphism.forward(),
    ModuleMorphism[
        MetricScalarRing[Ctx],
        ExteriorPowerTag[Dual[Ctx], 1],
        ExteriorPowerTag[Dual[Ctx], 2],
    ],
)

assert_type(
    form_hodge_star(perfect_metric, volume, p, metric_one_form),
    MetricCovariantForm[Ctx, 2],
)
assert_type(
    multivector_hodge_star(metric, volume, p, one_vector),
    Multivector[Ctx, 2],
)

assert_type(
    form_hodge_star_over_fraction_field(
        nondegenerate_metric,
        volume,
        p,
        fraction_one_form,
    ),
    FractionFieldCovariantForm[Ctx, 2],
)
flat_connection: FlatConnection[Ctx, E] = flat_connection_view(object())
coefficient_two_form: CoefficientForm[Ctx, E, 2] = coefficient_form_view(object())
assert_type(
    covariant_d(flat_connection, coefficient_two_form),
    CoefficientForm[Ctx, E, 3],
)

class_one: DeRhamClass[Ctx, 1] = de_rham_class_view(object())
class_two: DeRhamClass[Ctx, 2] = de_rham_class_view(object())
assert_type(cup(class_one, class_two), DeRhamClass[Ctx, 3])

relative_map: RelativeAlgebraMorphism[R, Eta, A, TargetEta, B] = (
    relative_algebra_morphism_view(object())
)
assert_type(de_rham_map(relative_map), DGAMorphism[Ctx, TargetCtx])
assert_type(
    pullback_form(relative_map, two_form),
    DifferentialForm[TargetCtx, 2],
)
i1: Degree[1] = degree_view(1)
assert_type(
    de_rham_cohomology_map(relative_map, i1),
    CohomologyMorphism[Ctx, TargetCtx, 1],
)
assert_type(
    pullback_de_rham_class(relative_map, i1, class_one),
    DeRhamClass[TargetCtx, 1],
)
