from __future__ import annotations

from dzack_research.static_types import (
    BilinearForm,
    AlgebraElement,
    AlgebraMorphism,
    AlgebraParent,
    AlgebraRing,
    BaseChangedRelativeContext,
    Automorphism,
    CategoricalMorphism,
    CategoryFunctor,
    CategoryObject,
    Cochain,
    CochainComplex,
    CochainMorphism,
    CohomologyClass,
    CohomologyModule,
    CoefficientForm,
    Connection,
    Covector,
    DeRhamAlgebra,
    DeRhamClass,
    Degree,
    DifferentialGradedCarrier,
    Derivation,
    DifferentialForm,
    FractionFieldCovariantForm,
    LinearMap,
    Metric,
    MetricCovariantForm,
    ModuleElement,
    ModuleBaseChangeAdjunction,
    ModuleMorphism,
    ModuleParent,
    ModuleStructure,
    PerfectMetric,
    NondegenerateMetric,
    GradedMorphism,
    HomogeneousElement,
    KahlerClassifier,
    KahlerDifferentials,
    KahlerPForm,
    RelativeAlgebraMorphism,
    RelativeContext,
    RingMorphism,
    Scalar,
    Vector,
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
    category_object_view,
    class_of_cycle,
    classifier_from_derivation,
    cochain_complex_view,
    cochain_d,
    cochain_map,
    cochain_morphism_view,
    cochain_of,
    coefficient_form_view,
    categorical_isomorphism_view,
    compose_automorphisms,
    compose_module_morphisms,
    compose_morphisms,
    connection_view,
    correlation_isomorphism,
    covector_view,
    cohomology_map,
    cohomology_of,
    covariant_d,
    cup,
    de_rham_class_view,
    de_rham_algebra_view,
    d,
    degree_view,
    derive,
    derivation_from_classifier,
    derivation_view,
    dual_module,
    dualize_module_morphism,
    form_hodge_star,
    embed_function,
    embed_exterior_form,
    extend_algebra,
    extend_algebra_morphism,
    form_hodge_star_over_fraction_field,
    fraction_field_covariant_form_view,
    form_view,
    dga_d,
    kahler_one_form_view,
    kahler_differentials_view,
    functor_view,
    induced_aut,
    induced_hom,
    linear_map_view,
    metric_view,
    metric_covariant_form_view,
    nondegenerate_metric_view,
    module_element_view,
    module_base_change,
    module_base_change_counit,
    module_base_change_unit,
    module_action,
    map_cohomology_class,
    module_morphism_view,
    module_view,
    differential_graded_carrier_view,
    graded_map,
    graded_morphism_view,
    graded_multiply,
    homogeneous_element_view,
    module_structure_view,
    morphism_view,
    perfect_metric_view,
    precompose_covector,
    pullback_de_rham_class,
    pullback_bilinear_form,
    pullback_form,
    relative_algebra_morphism_view,
    relative_context_view,
    restrict_algebra,
    restrict_module,
    restrict_module_morphism,
    ring_morphism_view,
    extend_module,
    extend_module_morphism,
    exterior_component,
    exterior_one,
    scalar_view,
    vector_view,
    volume_view,
    wedge_exterior,
    wedge,
)


class R: ...
class U: ...
class V: ...
class W: ...
class S: ...


class G: ...
class H: ...


graded_g: HomogeneousElement[G, 2] = homogeneous_element_view(object())
graded_h: HomogeneousElement[H, 1] = homogeneous_element_view(object())
graded_morphism: GradedMorphism[G, H] = graded_morphism_view(object())
dga_g: DifferentialGradedCarrier[G] = differential_graded_carrier_view(object())
bad_graded_product = graded_multiply(graded_g, graded_h)
bad_graded_map = graded_map(graded_morphism, graded_h)
bad_dga_element = dga_d(dga_g, graded_h)


f: LinearMap[R, U, 2, V, 3] = linear_map_view(object())
wrong_vector: Vector[R, W, 2] = vector_view(object())
bad_application: Vector[R, V, 3] = apply(f, wrong_vector)
wrong_covector: Covector[R, W, 2] = covector_view(object())
wrong_form: BilinearForm[R, W, 2] = bilinear_form_view(object())
bad_precomposition = precompose_covector(wrong_covector, f)
bad_form_pullback = pullback_bilinear_form(wrong_form, f)

module_element_u: ModuleElement[R, U] = module_element_view(object())
module_element_w: ModuleElement[R, W] = module_element_view(object())
module_f: ModuleMorphism[R, U, V] = module_morphism_view(object())
module_bad_inner: ModuleMorphism[R, W, V] = module_morphism_view(object())
module_structure_u: ModuleStructure[R, U] = module_structure_view(object())
scalar_s: Scalar[S] = scalar_view(object())
bad_module_application = apply_module_morphism(module_f, module_element_w)
bad_module_composition = compose_module_morphisms(module_f, module_bad_inner)
bad_scalar_ring = module_action(module_structure_u, scalar_s, module_element_u)

class SBase: ...
class TBase: ...
class Phi: ...
class AlgA: ...
class AlgB: ...

ring_map: RingMorphism[R, SBase, Phi] = ring_morphism_view(object())
algebra_r: AlgebraParent[R, AlgA] = algebra_view(object())
algebra_s: AlgebraParent[SBase, AlgB] = algebra_view(object())
algebra_t: AlgebraParent[TBase, AlgB] = algebra_view(object())
algebra_map_s: AlgebraMorphism[SBase, AlgB, AlgB] = algebra_morphism_view(object())
algebra_adjunction = algebra_base_change(ring_map)

bad_extension_source = extend_algebra(ring_map, algebra_s)
bad_restriction_source = restrict_algebra(ring_map, algebra_r)
bad_extension_morphism = extend_algebra_morphism(ring_map, algebra_map_s)
bad_unit_source = algebra_base_change_unit(algebra_adjunction, algebra_s)
bad_counit_source = algebra_base_change_counit(algebra_adjunction, algebra_t)

module_r_u: ModuleParent[R, U] = module_view(object())
module_s_v: ModuleParent[SBase, V] = module_view(object())
module_t_v: ModuleParent[TBase, V] = module_view(object())
module_map_s: ModuleMorphism[SBase, V, V] = module_morphism_view(object())
module_map_r: ModuleMorphism[R, U, U] = module_morphism_view(object())
module_adjunction: ModuleBaseChangeAdjunction[R, SBase, Phi] = module_base_change(
    ring_map
)

bad_dual_nonfree = dual_module(module_r_u)
bad_dual_morphism = dualize_module_morphism(module_f)

bad_module_extension_source = extend_module(ring_map, module_s_v)
bad_module_restriction_source = restrict_module(ring_map, module_r_u)
bad_module_extension_morphism = extend_module_morphism(ring_map, module_map_s)
bad_module_restriction_morphism = restrict_module_morphism(ring_map, module_map_r)
bad_module_unit_source = module_base_change_unit(module_adjunction, module_s_v)
bad_module_counit_source = module_base_change_counit(module_adjunction, module_t_v)

class K: ...
class L: ...
class M: ...

cochain_degree_zero: Degree[0] = degree_view(0)
cochain_degree_one: Degree[1] = degree_view(1)
complex_k: CochainComplex[R, K] = cochain_complex_view(object())
chain_map: CochainMorphism[R, K, L] = cochain_morphism_view(object())
cochain_k_zero: Cochain[R, K, 0] = cochain_of(
    complex_k, cochain_degree_zero, object()
)
complex_m: CochainComplex[R, M] = cochain_complex_view(object())
cochain_m_zero: Cochain[R, M, 0] = cochain_of(
    complex_m, cochain_degree_zero, object()
)
h_k_zero: CohomologyModule[R, K, 0] = cohomology_of(
    complex_k, cochain_degree_zero
)
h_m_zero: CohomologyModule[R, M, 0] = cohomology_of(
    complex_m, cochain_degree_zero
)
h_m_class: CohomologyClass[R, M, 0] = class_of_cycle(
    h_m_zero, cochain_m_zero
)

bad_cochain_degree = cochain_d(complex_k, cochain_degree_one, cochain_k_zero)
bad_cochain_source = cochain_map(chain_map, cochain_degree_zero, cochain_m_zero)
bad_cycle_complex = class_of_cycle(h_k_zero, cochain_m_zero)
bad_cohomology_class = map_cohomology_class(
    chain_map, cochain_degree_zero, h_m_class
)
bad_cohomology_map_class = cohomology_map(chain_map, cochain_degree_zero)(h_m_class)

class C: ...
class X: ...
class Y: ...
class Z: ...
class D: ...
class FTag: ...

f_arrow: CategoricalMorphism[C, X, Y] = morphism_view(object())
g_bad_arrow: CategoricalMorphism[C, Z, Y] = morphism_view(object())
bad_arrow_composition = compose_morphisms(f_arrow, g_bad_arrow)
auto_x: Automorphism[C, X] = categorical_isomorphism_view(object())
auto_y: Automorphism[C, Y] = categorical_isomorphism_view(object())
bad_automorphism_composition = compose_automorphisms(auto_x, auto_y)

functor: CategoryFunctor[C, D, FTag] = functor_view(object())
x_object: CategoryObject[C, X] = category_object_view(object())
y_object: CategoryObject[C, Y] = category_object_view(object())
wrong_hom_arrow: CategoricalMorphism[C, X, Z] = morphism_view(object())
hom_transport = induced_hom(functor, x_object, y_object)
aut_transport = induced_aut(functor, x_object)
bad_hom_transport = hom_transport(wrong_hom_arrow)
bad_aut_transport = aut_transport(auto_y)


class Eta: ...
class OtherEta: ...
class A: ...
type Ctx = RelativeContext[Eta, R, A]
type OtherCtx = RelativeContext[OtherEta, R, A]
class TargetEta: ...
class B: ...
type TargetCtx = RelativeContext[TargetEta, R, B]
class E: ...
class F: ...

context_value: Ctx = relative_context_view(object())
wrong_base_changed_context: BaseChangedRelativeContext[R, TBase, Phi, Eta, A] = (
    base_changed_relative_context(ring_map, context_value)
)


algebra_element_other: AlgebraElement[OtherCtx] = algebra_element_view(object())
omega: KahlerDifferentials[Ctx] = kahler_differentials_view(object())
omega_other: KahlerDifferentials[OtherCtx] = kahler_differentials_view(object())
de_rham_algebra: DeRhamAlgebra[Ctx] = de_rham_algebra_view(object())
derivation_ctx: Derivation[Ctx, E] = derivation_view(object())
derivation_other: Derivation[OtherCtx, E] = derivation_view(object())
target_f: ModuleParent[AlgebraRing[Ctx], F] = module_view(object())
classifier_e: KahlerClassifier[Ctx, E] = classifier_from_derivation(
    omega, derivation_ctx
)
bad_derivation_argument = derive(derivation_ctx, algebra_element_other)
bad_function_embedding = embed_function(de_rham_algebra, algebra_element_other)
bad_classifier_context = classifier_from_derivation(omega, derivation_other)
bad_classifier_target = derivation_from_classifier(omega, target_f, classifier_e)

p: Degree[1] = degree_view(1)
degree_two: Degree[2] = degree_view(2)
one_form: DifferentialForm[Ctx, 1] = form_view(object())
other_form: DifferentialForm[OtherCtx, 1] = form_view(object())
one_kahler: KahlerPForm[Ctx, 1] = exterior_one(
    omega, kahler_one_form_view(object())
)
other_kahler: KahlerPForm[OtherCtx, 1] = exterior_one(
    omega_other, kahler_one_form_view(object())
)
bad_exterior_context = wedge_exterior(
    omega,
    p,
    one_kahler,
    p,
    other_kahler,
)
bad_exterior_embedding = embed_exterior_form(
    de_rham_algebra,
    degree_two,
    one_kahler,
)
bad_exterior_component = exterior_component(
    de_rham_algebra,
    degree_two,
    one_form,
)

bad_wedge: DifferentialForm[Ctx, 2] = wedge(one_form, other_form)
bad_d: DifferentialForm[Ctx, 4] = d(one_form)

metric: Metric[Ctx, 3] = metric_view(object())
nondegenerate_metric: NondegenerateMetric[Ctx, 3] = nondegenerate_metric_view(object())
perfect_metric: PerfectMetric[Ctx, 3] = perfect_metric_view(object())
volume: Volume[Ctx, 3] = volume_view(object())
metric_one_form: MetricCovariantForm[Ctx, 1] = metric_covariant_form_view(object())
fraction_metric_one_form: FractionFieldCovariantForm[Ctx, 1] = (
    fraction_field_covariant_form_view(object())
)

# A non-perfect metric cannot produce the integral covariant Hodge star.
bad_star = form_hodge_star(metric, volume, p, metric_one_form)
bad_correlation_isomorphism = correlation_isomorphism(metric)

# Even for a perfect metric, the output degree is forced to n-p = 2.
wrong_star_degree: MetricCovariantForm[Ctx, 1] = form_hodge_star(
    perfect_metric,
    volume,
    p,
    metric_one_form,
)

# Fraction-field Hodge star requires both nondegeneracy and an explicitly
# scalar-extended form context; it never accepts an integral-looking form.
bad_fraction_star_metric = form_hodge_star_over_fraction_field(
    metric,
    volume,
    p,
    fraction_metric_one_form,
)
bad_fraction_star_context = form_hodge_star_over_fraction_field(
    nondegenerate_metric,
    volume,
    p,
    metric_one_form,
)
nonflat: Connection[Ctx, E] = connection_view(object())
coefficient_form: CoefficientForm[Ctx, E, 1] = coefficient_form_view(object())
bad_covariant_d = covariant_d(nonflat, coefficient_form)

class_e: DeRhamClass[Ctx, 1] = de_rham_class_view(object())
class_other: DeRhamClass[OtherCtx, 1] = de_rham_class_view(object())
bad_cup = cup(class_e, class_other)

relative_map: RelativeAlgebraMorphism[R, Eta, A, TargetEta, B] = (
    relative_algebra_morphism_view(object())
)
bad_pullback_form = pullback_form(relative_map, other_form)
i1: Degree[1] = degree_view(1)
bad_pullback_class = pullback_de_rham_class(relative_map, i1, class_other)
