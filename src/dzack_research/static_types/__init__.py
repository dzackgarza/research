"""Runtime-neutral entry points for the Pyrefly semantic typing facade.

The classes in this module are annotation markers only.  Their precise
generic signatures live in the adjacent ``__init__.pyi``; at runtime they do
not wrap or replace the authoritative Sage objects.
"""


from typing import Any


class _StaticMarker:
    @classmethod
    def __class_getitem__(cls, _parameters):
        return cls


class RelativeContext(_StaticMarker):
    pass


class FractionFieldContext(_StaticMarker):
    pass


class Dual(_StaticMarker):
    pass


class Scalar(_StaticMarker):
    pass


class Degree(_StaticMarker):
    pass


class AlgebraRing(_StaticMarker):
    pass


class AlgebraElement(_StaticMarker):
    pass


class RingMorphism(_StaticMarker):
    pass


class AlgebraCategory(_StaticMarker):
    pass


class AlgebraParent(_StaticMarker):
    pass


class AlgebraMorphism(_StaticMarker):
    pass


class ScalarExtendedAlgebra(_StaticMarker):
    pass


class RestrictedAlgebra(_StaticMarker):
    pass


class BaseChangedStructure(_StaticMarker):
    pass


BaseChangedRelativeContext = RelativeContext


class AlgebraScalarExtensionFunctor(_StaticMarker):
    pass


class AlgebraRestrictionFunctor(_StaticMarker):
    pass


class AlgebraBaseChangeAdjunction(_StaticMarker):
    pass


class ModuleCategory(_StaticMarker):
    pass


class HomTag(_StaticMarker):
    pass


class CategoryObject(_StaticMarker):
    pass


class FunctorImage(_StaticMarker):
    pass


class CategoryFunctor(_StaticMarker):
    pass


class CategoricalMorphism(_StaticMarker):
    pass


class CategoricalIsomorphism(CategoricalMorphism):
    pass


class HomObject(_StaticMarker):
    pass


class IsoObject(HomObject):
    pass


class ModuleParent(CategoryObject):
    pass


class FiniteFreeModule(ModuleParent):
    pass


class ModuleElement(_StaticMarker):
    pass


class ModuleMorphism(CategoricalMorphism, ModuleElement):
    pass


class FreeModuleMorphism(ModuleMorphism):
    pass


class FreeModuleIsomorphism(CategoricalIsomorphism):
    pass


class ModuleHom(HomObject, ModuleParent):
    pass


class ModuleStructure(_StaticMarker):
    pass


class ScalarExtendedModule(_StaticMarker):
    pass


class RestrictedModule(_StaticMarker):
    pass


class ModuleScalarExtensionFunctor(_StaticMarker):
    pass


class ModuleRestrictionFunctor(_StaticMarker):
    pass


class ModuleBaseChangeAdjunction(_StaticMarker):
    pass


class KahlerTag(_StaticMarker):
    pass


class DerivationTag(_StaticMarker):
    pass


class AlgebraModuleTag(_StaticMarker):
    pass


KahlerDifferentials = ModuleParent
KahlerOneForm = ModuleElement
KahlerClassifier = ModuleMorphism
KahlerClassifierIsomorphism = CategoricalIsomorphism


class Derivation(ModuleElement):
    pass


class DerivationSpace(ModuleParent):
    pass


class UniversalDerivation(Derivation):
    pass


class ExteriorPowerTag(_StaticMarker):
    pass


ExteriorPower = ModuleParent
ExteriorElement = ModuleElement
KahlerPForm = ModuleElement
PoincareDualityIsomorphism = CategoricalIsomorphism
HodgeStarIsomorphism = CategoricalIsomorphism


class CochainPieceTag(_StaticMarker):
    pass


class CohomologyTag(_StaticMarker):
    pass


class CochainComplex(_StaticMarker):
    pass


class CochainMorphism(_StaticMarker):
    pass


CochainPiece = ModuleParent
Cochain = ModuleElement
CohomologyModule = ModuleParent
CohomologyClass = ModuleElement
CochainCohomologyMorphism = ModuleMorphism


class InducedHomFunctor(_StaticMarker):
    pass


class InducedEndFunctor(_StaticMarker):
    pass


class InducedAutFunctor(_StaticMarker):
    pass


EndObject = HomObject
AutObject = IsoObject
EndomorphismArrow = CategoricalMorphism
Automorphism = CategoricalIsomorphism
ModuleEnd = ModuleHom
ModuleEndomorphism = ModuleMorphism


class Up(_StaticMarker):
    pass


class Down(_StaticMarker):
    pass


class Tensor(_StaticMarker):
    pass


class Vector(Tensor):
    pass


class Covector(Tensor):
    pass


class LinearMap(Tensor):
    pass


class Endomorphism(LinearMap):
    pass


class Isomorphism(LinearMap):
    pass


class BilinearForm(Tensor):
    pass


class DualBilinearForm(Tensor):
    pass


class GradedObject(_StaticMarker):
    pass


class HomogeneousElement(_StaticMarker):
    pass


class GradedMorphism(_StaticMarker):
    pass


class DifferentialGradedObject(GradedObject):
    pass


class DifferentialGradedMorphism(GradedMorphism):
    pass


DifferentialForm = HomogeneousElement
DeRhamAlgebra = DifferentialGradedObject


class DeRhamGradedTag(_StaticMarker):
    pass


class RelativeBaseRing(_StaticMarker):
    pass


class DeRhamComplexTag(_StaticMarker):
    pass


Multivector = ExteriorElement


MetricCovariantForm = ExteriorElement
FractionFieldCovariantForm = ExteriorElement


class FractionFieldMetricRing(_StaticMarker):
    pass


class FractionFieldMetricModule(_StaticMarker):
    pass


class DifferentialGradedModule(_StaticMarker):
    pass


class DGModuleElement(_StaticMarker):
    pass


class DGModuleMorphism(_StaticMarker):
    pass


class ConnectionModuleTag(_StaticMarker):
    pass


CoefficientDeRhamModule = DifferentialGradedModule
CoefficientForm = DGModuleElement


VectorField = Derivation


class FormOperator(_StaticMarker):
    pass


class GradedDerivationOperator(FormOperator):
    pass


class DifferentialOperator(GradedDerivationOperator):
    pass


class InteriorOperator(GradedDerivationOperator):
    pass


class LieDerivativeOperator(GradedDerivationOperator):
    pass


class Metric(_StaticMarker):
    pass


class MetricScalarRing(_StaticMarker):
    pass


class NondegenerateMetric(Metric):
    pass


class PerfectMetric(NondegenerateMetric):
    pass


class Volume(_StaticMarker):
    pass


class Connection(_StaticMarker):
    pass


class FlatConnection(Connection):
    pass


class CoefficientOperator(_StaticMarker):
    pass


class CovariantDifferential(CoefficientOperator):
    pass


DeRhamCohomology = CohomologyModule
DeRhamClass = CohomologyClass


class DeRhamCohomologyAlgebra(_StaticMarker):
    pass


class RelativeAlgebraMorphism(_StaticMarker):
    pass


DGAMorphism = DifferentialGradedMorphism


class CohomologyMorphism(_StaticMarker):
    pass


class HodgeCohomology(_StaticMarker):
    pass


class HodgeToDeRham(_StaticMarker):
    pass


class SpectralTerm(_StaticMarker):
    pass


def _view(*values):
    return values[-1]


vector_view = _view
covector_view = _view
linear_map_view = _view
endomorphism_view = _view
isomorphism_view = _view
bilinear_form_view = _view
dual_bilinear_form_view = _view
form_view = _view
de_rham_algebra_view = _view
graded_object_view = _view
homogeneous_element_view = _view
graded_morphism_view = _view
differential_graded_object_view = _view
differential_graded_morphism_view = _view
multivector_view = _view
metric_covariant_form_view = _view
fraction_field_covariant_form_view = _view
coefficient_form_view = _view
dg_module_view = _view
dg_module_element_view = _view
dg_module_morphism_view = _view
vector_field_view = _view
operator_view = _view
graded_derivation_operator_view = _view
metric_view = _view
nondegenerate_metric_view = _view
perfect_metric_view = _view
volume_view = _view
connection_view = _view
flat_connection_view = _view
cohomology_view = _view
de_rham_class_view = _view
cohomology_algebra_view = _view
category_object_view = _view
morphism_view = _view
categorical_isomorphism_view = _view
hom_object_view = _view
iso_object_view = _view
module_view = _view
finite_free_module_view = _view
module_element_view = _view
module_morphism_view = _view
free_module_morphism_view = _view
free_module_isomorphism_view = _view
module_hom_view = _view
module_structure_view = _view
module_base_change_adjunction_view = _view
scalar_view = _view
degree_view = _view
algebra_element_view = _view
ring_morphism_view = _view
algebra_view = _view
algebra_morphism_view = _view
algebra_base_change_adjunction_view = _view
kahler_differentials_view = _view
kahler_one_form_view = _view
exterior_power_view = _view
exterior_element_view = _view
derivation_view = _view
derivation_space_view = _view
universal_derivation_view = _view
cochain_complex_view = _view
cochain_morphism_view = _view
cochain_piece_view = _view
cochain_view = _view
cohomology_module_view = _view
cohomology_class_view = _view
relative_algebra_morphism_view = _view
dga_morphism_view = _view
cohomology_morphism_view = _view
relative_context_view = _view
functor_view = _view


def fraction_field_context(context):
    """Static context change corresponding to scalar extension to ``Frac(R)``."""
    return context


def base_changed_relative_context(ring_map, context):
    """Return the static relative context after scalar extension along ``ring_map``."""
    return context


def algebra_base_change(ring_map):
    """Return the live algebra scalar-extension/restriction adjunction."""
    from dzack_research.preamble.categories.functors.algebra_scalar_change import algebra_base_change_adjunction

    return algebra_base_change_adjunction(ring_map)


def extend_algebra(ring_map, algebra):
    """Apply live algebra scalar extension along ``ring_map``."""
    return algebra_base_change(ring_map).left_adjoint()(algebra)


def restrict_algebra(ring_map, algebra):
    """Apply live algebra restriction of scalars along ``ring_map``."""
    return algebra_base_change(ring_map).right_adjoint()(algebra)


def extend_algebra_morphism(ring_map, morphism):
    """Transport an algebra morphism by live scalar extension."""
    return algebra_base_change(ring_map).left_adjoint()(morphism)


def restrict_algebra_morphism(ring_map, morphism):
    """Transport an algebra morphism by live scalar restriction."""
    return algebra_base_change(ring_map).right_adjoint()(morphism)


def algebra_base_change_unit(adjunction, algebra):
    """Return the live unit ``A -> Res(S tensor_R A)``."""
    return adjunction.unit(algebra)


def algebra_base_change_counit(adjunction, algebra):
    """Return the live counit ``S tensor_R Res(B) -> B``."""
    return adjunction.counit(algebra)


def functor_object_image(functor, obj):
    """Return the live image of an object under an authoritative functor."""
    return functor.on_object(obj)


def functor_morphism_image(functor, morphism):
    """Return the live image of a morphism under an authoritative functor."""
    return functor.on_morphism(morphism)


def induced_hom(functor, source, target):
    """Return the represented Hom functor induced by ``functor``."""
    from dzack_research.preamble.categories.functors.hom_packets import induced_hom_functor

    return induced_hom_functor(functor, source, target)


def induced_end(functor, obj):
    """Return the represented End functor induced by ``functor``."""
    from dzack_research.preamble.categories.functors.hom_packets import induced_end_functor

    return induced_end_functor(functor, obj)


def induced_aut(functor, obj):
    """Return the represented Aut functor induced by ``functor``."""
    from dzack_research.preamble.categories.functors.hom_packets import induced_aut_functor

    return induced_aut_functor(functor, obj)


def module_element_of(module, value):
    """Typed identity view anchored by one already-typed module parent."""
    return value


def module_morphism_of(source, target, value):
    """Typed identity view anchored by its source and target module parents."""
    return value


def free_module_morphism_of(source, source_rank, target, target_rank, value):
    """Typed identity view of a framed map with explicit symbolic ranks."""
    return value


def vector_of(module, rank, value):
    """Typed identity view of a vector anchored by module and rank."""
    return value


def covector_of(module, rank, value):
    """Typed identity view of a covector anchored by module and rank."""
    return value


def linear_map_of(source, source_rank, target, target_rank, value):
    """Typed identity view of a linear map anchored by endpoint modules and ranks."""
    return value


def form_of(context, degree, value):
    """Typed identity view of a differential form anchored by context and degree."""
    return value


def multivector_of(context, degree, value):
    """Typed identity view of a multivector anchored by context and degree."""
    return value


def coefficient_form_of(context, coefficient_module, degree, value):
    """Typed identity view of a coefficient form with explicit relative context."""
    return value


def differential_operator_of(context, value):
    """Typed identity view of a degree-``+1`` form operator."""
    return value


def interior_operator_of(context, value):
    """Typed identity view of a degree-``-1`` contraction operator."""
    return value


def lie_derivative_operator_of(context, value):
    """Typed identity view of a degree-zero Lie derivative operator."""
    return value


def compose_morphisms(outer, inner):
    """Compose authoritative categorical morphisms in mathematical order."""
    return outer * inner


def identity_endomorphism(end_object):
    """Return the identity element of a represented ``End_C(A)`` object."""
    return end_object.one()


def compose_endomorphisms(outer, inner):
    """Compose two endomorphisms of the same represented object."""
    return outer * inner


def identity_automorphism(aut_object):
    """Return the identity element of a represented ``Aut_C(A)`` object."""
    return aut_object.one()


def compose_automorphisms(outer, inner):
    """Compose automorphisms of one represented object."""
    return outer * inner


def inverse_automorphism(automorphism):
    """Return the inverse automorphism without changing its endpoint object."""
    from dzack_research.preamble.categories.abstract_categories import Isomorphism

    return Isomorphism(automorphism.inverse(), automorphism.forward())


def apply_module_morphism(morphism, element):
    """Apply an authoritative module morphism."""
    return morphism(element)


def compose_module_morphisms(outer, inner):
    """Compose authoritative module morphisms."""
    return outer * inner


def module_morphism_tensor(morphism):
    """Return the live type-``(1,1)`` coordinate tensor of a framed module map."""
    from dzack_research.preamble.tensors import tensor

    return tensor.from_morphism(morphism)


def dual_module(module):
    """Return the live finite-free dual module."""
    return module.dual_module()


def dualize_module_morphism(morphism):
    """Apply the live contravariant finite-free dualization functor."""
    from dzack_research.preamble.categories.functors.linear_constructions import DualizationFunctor

    return DualizationFunctor(morphism.domain().base_ring())(morphism)


def double_dual_morphism(module):
    """Return the live finite-free biduality morphism ``M -> M**``."""
    from dzack_research.preamble.categories.functors.linear_constructions import DualizationFunctor

    return DualizationFunctor(module.base_ring()).double_dual_morphism(module)


def module_action(structure, scalar, element):
    """Apply a scalar through the represented structure map ``R -> End_R(M)``."""
    return structure(scalar)(element)


def module_base_change(ring_map):
    """Return the live module scalar-extension/restriction adjunction."""
    from dzack_research.preamble.categories.functors.scalar_change import base_change_adjunction

    return base_change_adjunction(ring_map)


def extend_module(ring_map, module):
    """Apply live module scalar extension along ``ring_map``."""
    return module_base_change(ring_map).left_adjoint()(module)


def restrict_module(ring_map, module):
    """Apply live module restriction of scalars along ``ring_map``."""
    return module_base_change(ring_map).right_adjoint()(module)


def extend_module_morphism(ring_map, morphism):
    """Transport a module morphism by live scalar extension."""
    return module_base_change(ring_map).left_adjoint()(morphism)


def restrict_module_morphism(ring_map, morphism):
    """Transport a module morphism by live scalar restriction."""
    return module_base_change(ring_map).right_adjoint()(morphism)


def module_base_change_unit(adjunction, module):
    """Return the live unit ``M -> Res(S tensor_R M)``."""
    return adjunction.unit(module)


def module_base_change_counit(adjunction, module):
    """Return the live counit ``S tensor_R Res(N) -> N``."""
    return adjunction.counit(module)


def universal_derivation(omega):
    """Return the live universal derivation attached to ``omega``."""
    return omega.universal_derivation()


def derive(derivation, element):
    """Apply a represented derivation to an algebra element."""
    return derivation(element)


def embed_function(de_rham, element):
    """Embed a coefficient-algebra element as a de Rham degree-zero form."""
    return de_rham.from_degree_zero(element)


def embed_kahler_one_form(de_rham, one_form):
    """Embed a Kähler one-form into exterior degree one of the de Rham DGA."""
    exterior = de_rham.extension_algebra()
    return de_rham.from_realization(exterior(one_form))


def classifier_from_derivation(omega, derivation):
    """Return the unique linear classifier through the Kähler module."""
    return omega.from_derivation(derivation)


def derivation_from_classifier(omega, target_module, classifier):
    """Transport a classifier through the represented Kähler isomorphism."""
    return omega.derivation_classifier_isomorphism(target_module).forward()(classifier)


def kahler_classifier_isomorphism(omega, target_module):
    """Return the represented Kähler classifier isomorphism."""
    return omega.derivation_classifier_isomorphism(target_module)


def exterior_power(module, degree):
    """Return the live exterior power ``Lambda^degree(module)``."""
    from dzack_research.preamble.categories.modules import AlternatingPower

    return AlternatingPower(module, int(degree))


def exterior_one(module, element):
    """Read ``Lambda^1(module)=module`` without constructing a second module."""
    return element


def wedge_exterior(module, left_degree, left, right_degree, right):
    """Multiply two live exterior-power elements."""
    from dzack_research.preamble.categories.modules import alternating_power_product

    return alternating_power_product(
        module,
        int(left_degree),
        left,
        int(right_degree),
        right,
    )


def exterior_power_morphism(morphism, degree):
    """Apply the live exterior-power functor to a module morphism."""
    from dzack_research.preamble.categories.modules import alternating_power_morphism

    return alternating_power_morphism(morphism, int(degree))


def embed_exterior_form(de_rham, degree, exterior_element):
    """Embed one exterior-power component into the live de Rham algebra."""
    exterior = de_rham.extension_algebra()
    realized = exterior._from_component(int(degree), exterior_element)
    return de_rham.from_realization(realized)


def exterior_component(de_rham, degree, form):
    """Return the live exterior-power component underlying a homogeneous form."""
    return de_rham.realize(form).homogeneous_component(int(degree))


def cochain_piece(complex_, degree):
    """Return the represented degree-``degree`` module of a cochain complex."""
    return complex_.graded_piece(int(degree))


def cochain_of(complex_, degree, value):
    """Typed identity view of a homogeneous cochain anchored by complex and degree."""
    return value


def cochain_d(complex_, degree, cochain):
    """Apply the selected component ``d^i : C^i -> C^(i+1)``."""
    return complex_.differential_component(int(degree))(cochain)


def cochain_map(morphism, degree, cochain):
    """Apply the degree-``degree`` component of a cochain morphism."""
    return morphism.component(int(degree))(cochain)


def cohomology_of(complex_, degree):
    """Return the represented degree-``degree`` cohomology module."""
    return complex_.cohomology(int(degree))


def class_of_cycle(cohomology_module, cycle):
    """Return the cohomology class of a closed homogeneous cochain."""
    return cohomology_module.class_of_cycle(cycle)


def cycle_representative(cohomology_module, cohomology_class):
    """Return the selected cycle representative of a cohomology class."""
    return cohomology_module.cycle_representative(cohomology_class)


def cohomology_map(morphism, degree):
    """Return the map induced by a cochain morphism on degree-``degree`` cohomology."""
    from dzack_research.preamble.categories.functors.cohomology import cohomology_functor

    return cohomology_functor(morphism.domain().base_ring(), int(degree))(morphism)


def map_cohomology_class(morphism, degree, cohomology_class):
    """Apply the induced cohomology map to a represented class."""
    return cohomology_map(morphism, degree)(cohomology_class)


def apply(linear_map, vector):
    """Contract a type-``(1,1)`` tensor with a vector."""
    return linear_map * vector


def graded_multiply(left, right):
    """Multiply homogeneous elements of one represented additive graded object."""
    return left * right


def graded_map(morphism, element):
    """Apply a degree-zero graded morphism to a homogeneous element."""
    return morphism(element)


def dga_d(algebra, element):
    """Apply the degree-one differential of a represented DGA."""
    return algebra.d(element)


def compose(outer, inner):
    """Contract the adjacent covariant/contravariant slots of two tensors."""
    return outer * inner


def lower_index(form, vector):
    """Contract a covariant bilinear tensor with a vector."""
    return form * vector


def raise_index(dual_form, covector):
    """Contract a contravariant dual form with a covector."""
    return dual_form * covector


def pair(covector, vector):
    """Evaluate the natural covector-vector pairing."""
    return covector * vector


def precompose_covector(covector, linear_map):
    """Contract a covector with the first contravariant slot of a tensor."""
    return covector * linear_map


def pullback_bilinear_form(form, morphism):
    """Pull back a covariant bilinear tensor along an owned module morphism."""
    return form.pullback(morphism)


def dual_tensor(value):
    """Dualize a nondegenerate pairing or copairing tensor."""
    return value.dual_tensor()


def wedge(left, right):
    """Multiply homogeneous elements in the represented exterior algebra."""
    return left * right


def d(form):
    """Apply the differential of the represented DGA containing ``form``."""
    return form.parent().d(form)


def graded_commutator(left, right):
    from dzack_research.preamble.categories.algebras import GradedCommutator

    return GradedCommutator(left, right)


def interior_operator(vector_field):
    from dzack_research.preamble.categories.algebras import InteriorProduct

    return InteriorProduct(vector_field)


def interior(vector_field, form):
    return interior_operator(vector_field)(form)


def lie_derivative_operator(vector_field):
    from dzack_research.preamble.categories.algebras import LieDerivative

    return LieDerivative(vector_field)


def lie_derivative(vector_field, form):
    return lie_derivative_operator(vector_field)(form)


def lie_bracket(left, right):
    from dzack_research.preamble.categories.algebras import LieBracket

    return LieBracket(left, right)


def form_hodge_star(metric, volume, degree, form):
    from dzack_research.preamble.categories.modules import HodgeStar

    return HodgeStar(metric, volume, degree)(form)


def metric_tensor(metric):
    """Return the live covariant Gram tensor of a represented metric."""
    return metric.gram_tensor()


def correlation_morphism(metric):
    """Return the live correlation morphism ``g^flat : M -> M^vee``."""
    from dzack_research.preamble.categories.modules import AlgebraicCorrelationMorphism

    return AlgebraicCorrelationMorphism(metric)


def correlation_isomorphism(metric):
    """Return the live perfect correlation isomorphism ``M ~= M^vee``."""
    from dzack_research.preamble.categories.modules import CorrelationIsomorphism

    return CorrelationIsomorphism(metric)


def poincare_duality(metric, volume, degree):
    """Return the live Poincaré-duality isomorphism in exterior degree ``degree``."""
    from dzack_research.preamble.categories.modules import PoincareDuality

    return PoincareDuality(metric, volume, int(degree))


def hodge_star_isomorphism(metric, volume, degree):
    """Return the live covariant Hodge-star isomorphism on exterior forms."""
    from dzack_research.preamble.categories.modules import HodgeStar

    return HodgeStar(metric, volume, int(degree))


def form_hodge_star_over_fraction_field(metric, volume, degree, form):
    """Apply the live covariant Hodge star after explicit fraction-field extension."""
    from dzack_research.preamble.categories.modules import HodgeStarOverFractionField

    return HodgeStarOverFractionField(metric, volume, degree)(form)


def multivector_hodge_star(metric, volume, degree, multivector):
    from dzack_research.preamble.categories.modules import MultivectorHodgeStar

    return MultivectorHodgeStar(metric, volume, degree)(multivector)


def covariant_d(connection, coefficient_form):
    """Apply the live coefficient de Rham differential for one flat connection."""
    module = coefficient_form.parent()
    if not hasattr(module, "connection") or module.connection() is not connection:
        raise ValueError("the coefficient form does not belong to this connection's de Rham module")
    return module.d(coefficient_form)


def connection_de_rham_module(connection):
    """Return the live DG module attached to a flat connection."""
    return connection.de_rham_module()


def coefficient_zero_form(dg_module, coefficient):
    """Embed a coefficient-module element in DG-module degree zero."""
    return dg_module.from_coefficient(coefficient)


def dg_module_act(dg_module, module_element, algebra_element):
    """Apply the live graded DGA action on a homogeneous DG-module element."""
    return dg_module.act(module_element, algebra_element)


def dg_module_d(dg_module, module_element):
    """Apply the degree-one differential of a represented DG module."""
    return dg_module.d(module_element)


def cup(left, right):
    """Multiply homogeneous classes in the represented de Rham cohomology algebra."""
    return left * right


def de_rham_map(morphism):
    """Apply the live affine de Rham functor to one relative algebra morphism."""
    from dzack_research.preamble.categories.functors.de_rham import de_rham_functor

    return de_rham_functor(morphism.domain().base_ring())(morphism)


def pullback_form(morphism, form):
    """Transport a differential form along the represented affine algebra map."""
    return de_rham_map(morphism)(form)


def de_rham_cohomology_map(morphism, degree):
    """Return the map induced on degree-``degree`` algebraic de Rham cohomology."""
    from dzack_research.preamble.categories.functors.cohomology import de_rham_cohomology_functor

    return de_rham_cohomology_functor(
        morphism.domain().base_ring(), int(degree)
    )(morphism)


def pullback_de_rham_class(morphism, degree, cohomology_class):
    """Transport a de Rham class along the represented affine algebra map."""
    return de_rham_cohomology_map(morphism, degree)(cohomology_class)


# A point $(n_1, \ldots, n_k)$ of the product monoid $\mathbb N^k$: an element
# of `Sets().product` of the constant family $\mathbb N$ over a finite index
# set.  The parent is built at runtime, so the referent has no static name yet
# and this aliases `Any` under `LEX-15`.  It checks nothing and is not intended
# to; it names the codomain so a reader can audit a signature against the
# operation's definition, and it is the single point at which a sharper
# refinement will later apply to every consumer at once (`LEX-17`, `LEX-18`).
ProductOfNaturalNumbers = Any


__all__ = [
    "ProductOfNaturalNumbers",
    "AutObject",
    "AlgebraBaseChangeAdjunction",
    "AlgebraCategory",
    "AlgebraElement",
    "AlgebraMorphism",
    "AlgebraModuleTag",
    "AlgebraParent",
    "AlgebraRestrictionFunctor",
    "AlgebraRing",
    "AlgebraScalarExtensionFunctor",
    "Automorphism",
    "BilinearForm",
    "BaseChangedRelativeContext",
    "BaseChangedStructure",
    "CategoricalIsomorphism",
    "CategoricalMorphism",
    "CategoryFunctor",
    "CategoryObject",
    "Cochain",
    "CochainCohomologyMorphism",
    "CochainComplex",
    "CochainMorphism",
    "CochainPiece",
    "CochainPieceTag",
    "CohomologyClass",
    "CohomologyModule",
    "CohomologyMorphism",
    "CohomologyTag",
    "CoefficientForm",
    "CoefficientOperator",
    "Connection",
    "Covector",
    "CovariantDifferential",
    "DGAMorphism",
    "DeRhamClass",
    "DeRhamAlgebra",
    "DeRhamCohomology",
    "DeRhamCohomologyAlgebra",
    "DeRhamComplexTag",
    "DeRhamGradedTag",
    "Degree",
    "Derivation",
    "DerivationSpace",
    "DerivationTag",
    "DifferentialForm",
    "DifferentialGradedObject",
    "DifferentialGradedMorphism",
    "DifferentialOperator",
    "Down",
    "Dual",
    "DualBilinearForm",
    "EndObject",
    "EndomorphismArrow",
    "ExteriorElement",
    "ExteriorPower",
    "ExteriorPowerTag",
    "Endomorphism",
    "FlatConnection",
    "FreeModuleMorphism",
    "FormOperator",
    "FractionFieldContext",
    "FunctorImage",
    "GradedObject",
    "GradedMorphism",
    "HomObject",
    "HomTag",
    "HomogeneousElement",
    "HodgeCohomology",
    "HodgeToDeRham",
    "InducedAutFunctor",
    "InducedEndFunctor",
    "InducedHomFunctor",
    "InteriorOperator",
    "IsoObject",
    "Isomorphism",
    "KahlerClassifier",
    "KahlerClassifierIsomorphism",
    "KahlerDifferentials",
    "KahlerOneForm",
    "KahlerPForm",
    "KahlerTag",
    "LieDerivativeOperator",
    "LinearMap",
    "Metric",
    "NondegenerateMetric",
    "ModuleCategory",
    "ModuleElement",
    "ModuleEnd",
    "ModuleEndomorphism",
    "ModuleHom",
    "ModuleBaseChangeAdjunction",
    "ModuleMorphism",
    "ModuleParent",
    "ModuleRestrictionFunctor",
    "ModuleScalarExtensionFunctor",
    "ModuleStructure",
    "Multivector",
    "PerfectMetric",
    "RelativeContext",
    "RelativeAlgebraMorphism",
    "RelativeBaseRing",
    "RestrictedAlgebra",
    "RestrictedModule",
    "RingMorphism",
    "Scalar",
    "ScalarExtendedAlgebra",
    "ScalarExtendedModule",
    "SpectralTerm",
    "Tensor",
    "Up",
    "UniversalDerivation",
    "Vector",
    "VectorField",
    "Volume",
    "apply",
    "apply_module_morphism",
    "algebra_base_change",
    "algebra_base_change_adjunction_view",
    "algebra_base_change_counit",
    "algebra_base_change_unit",
    "algebra_element_view",
    "algebra_morphism_view",
    "algebra_view",
    "base_changed_relative_context",
    "bilinear_form_view",
    "categorical_isomorphism_view",
    "category_object_view",
    "class_of_cycle",
    "classifier_from_derivation",
    "cochain_complex_view",
    "cochain_d",
    "cochain_map",
    "cochain_morphism_view",
    "cochain_of",
    "cochain_piece",
    "cochain_piece_view",
    "cochain_view",
    "coefficient_form_view",
    "cohomology_algebra_view",
    "cohomology_class_view",
    "cohomology_map",
    "cohomology_module_view",
    "cohomology_morphism_view",
    "cohomology_of",
    "cohomology_view",
    "compose",
    "compose_automorphisms",
    "compose_endomorphisms",
    "compose_module_morphisms",
    "compose_morphisms",
    "connection_view",
    "covector_view",
    "covariant_d",
    "cup",
    "cycle_representative",
    "d",
    "degree_view",
    "derive",
    "derivation_from_classifier",
    "derivation_space_view",
    "derivation_view",
    "de_rham_cohomology_map",
    "de_rham_class_view",
    "de_rham_algebra_view",
    "de_rham_map",
    "dga_d",
    "dga_morphism_view",
    "differential_graded_object_view",
    "differential_graded_morphism_view",
    "dual_bilinear_form_view",
    "dual_tensor",
    "endomorphism_view",
    "embed_function",
    "embed_exterior_form",
    "embed_kahler_one_form",
    "extend_algebra",
    "extend_algebra_morphism",
    "extend_module",
    "extend_module_morphism",
    "exterior_component",
    "exterior_element_view",
    "exterior_one",
    "exterior_power",
    "exterior_power_view",
    "flat_connection_view",
    "form_of",
    "free_module_morphism_view",
    "free_module_morphism_of",
    "form_hodge_star",
    "form_hodge_star_over_fraction_field",
    "form_view",
    "fraction_field_context",
    "functor_morphism_image",
    "functor_object_image",
    "functor_view",
    "graded_object_view",
    "graded_commutator",
    "graded_derivation_operator_view",
    "graded_map",
    "graded_morphism_view",
    "graded_multiply",
    "homogeneous_element_view",
    "hom_object_view",
    "interior",
    "interior_operator",
    "identity_automorphism",
    "identity_endomorphism",
    "induced_aut",
    "induced_end",
    "induced_hom",
    "inverse_automorphism",
    "iso_object_view",
    "isomorphism_view",
    "kahler_classifier_isomorphism",
    "kahler_differentials_view",
    "kahler_one_form_view",
    "lie_bracket",
    "lie_derivative",
    "lie_derivative_operator",
    "linear_map_view",
    "linear_map_of",
    "lower_index",
    "metric_view",
    "nondegenerate_metric_view",
    "module_element_view",
    "module_element_of",
    "module_hom_view",
    "module_structure_view",
    "module_action",
    "module_base_change",
    "module_base_change_adjunction_view",
    "module_base_change_counit",
    "module_base_change_unit",
    "map_cohomology_class",
    "module_morphism_tensor",
    "module_morphism_view",
    "module_morphism_of",
    "module_view",
    "morphism_view",
    "multivector_hodge_star",
    "multivector_view",
    "multivector_of",
    "operator_view",
    "differential_operator_of",
    "interior_operator_of",
    "lie_derivative_operator_of",
    "pair",
    "precompose_covector",
    "perfect_metric_view",
    "pullback_de_rham_class",
    "pullback_bilinear_form",
    "pullback_form",
    "raise_index",
    "relative_algebra_morphism_view",
    "relative_context_view",
    "restrict_algebra",
    "restrict_algebra_morphism",
    "restrict_module",
    "restrict_module_morphism",
    "ring_morphism_view",
    "scalar_view",
    "vector_field_view",
    "vector_view",
    "vector_of",
    "volume_view",
    "universal_derivation",
    "universal_derivation_view",
    "wedge",
    "wedge_exterior",
    "coefficient_form_of",
    "covector_of",
]
