r"""Derivations of represented commutative algebras.

For an ``R``-algebra ``A`` and an ``A``-module ``M``, ``A.derivations(M)``
is the ``A``-module of ``R``-derivations ``A -> M``.  On the live finite
polynomial-presentation backend a derivation is specified on the chosen
algebra generators and evaluated by the formal chain rule on a selected
presentation representative.
"""

import operator

from sage.categories.action import Action
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.unknown import Unknown
from sage.structure.element import ModuleElement

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    _RestrictedMorCategoryOf,
    RestrictedMorCategoryParent,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import AlgebrasWithChosenFinitePresentation
from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebras
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    _fix_selected_module_framing,
    _restricted_scalars_view,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _fix_selected_module_presentation,
    _presentation_from_relation_rows,
    _presentation_matrix,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)


def _commutative_presentation_data(algebra):
    r"""Return ``(P, labels, variables, relations, lift)`` for ``A = P/I``."""

    base = algebra.base_ring()
    if algebra not in Algebras(base).Associative().Unital().Commutative():
        raise TypeError("Kähler calculus requires a commutative algebra")
    assert (
        algebra in AlgebrasWithChosenFinitePresentation(base)
        or algebra in SymmetricAlgebras(base)
    ), (
        "the represented Kähler-calculus backend requires a symmetric algebra or a chosen finite commutative polynomial presentation"
    )

    if algebra in AlgebrasWithChosenFinitePresentation(base):
        presentation = algebra.presentation_ring()
        relations = algebra.relations()
        lift = algebra.lift_to_presentation
    elif algebra in SymmetricAlgebras(base):
        presentation = algebra
        relations = finite_ordered_set(())
        lift = presentation

    labels = presentation.algebra_generating_set()
    variables = FiniteOrderedSets().from_indexed(
        labels,
        presentation.algebra_generator,
    )
    return presentation, labels, variables, relations, lift


def _differentiate_representative(algebra, representative, variables):
    presentation, _labels, _variables, _relations, _lift = _commutative_presentation_data(
        algebra
    )
    source = _engine_element(presentation, presentation(representative))
    target = _engine_ring(algebra)

    def derivative(variable):
        engine_variable = _engine_element(presentation, variable)
        return _owned_engine_element(algebra,
            target(source.derivative(engine_variable))
        )

    return tuple(derivative(variable) for variable in variables)


class Derivation(ModuleElement):
    r"""An actual ``R``-linear arrow ``A -> Res_R(M)`` satisfying Leibniz.

    The public codomain of a derivation remains the original ``A``-module
    ``M``.  :meth:`underlying_linear_morphism` is the corresponding element of
    the canonical ``Hom_R(A, Res_R(M))`` containing this derivation subobject.
    """

    def __init__(self, parent, generator_images) -> None:
        ModuleElement.__init__(self, parent)
        labels = parent.generator_labels()
        if isinstance(generator_images, dict):
            missing = [label for label in labels if label not in generator_images]
            if missing:
                raise ValueError(f"derivation assignment omits {missing}")
            images = {label: generator_images[label] for label in labels}
        elif callable(generator_images):
            images = {label: generator_images(label) for label in labels}
        else:
            values = tuple(generator_images)
            if len(values) != len(labels):
                raise ValueError("a derivation needs one image for each algebra generator")
            images = dict(zip(labels, values, strict=True))
        target = parent.target_module()
        self._generator_images = {
            label: target(image) if image.parent() is not target else image
            for label, image in images.items()
        }
        self._check_relations()

    def domain(self):
        return self.parent().algebra()

    def codomain(self):
        return self.parent().target_module()

    def restricted_codomain(self):
        return self.parent().restricted_target_module()

    def generator_image(self, label):
        return self._generator_images[label]

    def _evaluate_coefficients(self, coefficients):
        target = self.codomain()
        return sum(
            (
                target.scalar_multiple(coefficient, self.generator_image(label))
                for label, coefficient in zip(
                    self.parent().generator_labels(), coefficients, strict=True
                )
                if coefficient
            ),
            target.zero(),
        )

    def _check_relations(self) -> None:
        algebra = self.domain()
        if algebra in LocalizationRings():
            source = algebra.localization_source()
            presentation, _labels, variables, relations, _lift = (
                _commutative_presentation_data(source)
            )
            localization_map = algebra.localization_map()
            for relation in relations:
                coefficients = _differentiate_representative(
                    source,
                    relation,
                    variables,
                )
                localized_coefficients = tuple(
                    localization_map(coefficient) for coefficient in coefficients
                )
                if self._evaluate_coefficients(localized_coefficients) != self.codomain().zero():
                    raise ValueError(
                        "the proposed generator images do not annihilate a defining source-algebra relation under the localized derivation rule"
                    )
            return

        presentation, _labels, variables, relations, _lift = _commutative_presentation_data(
            algebra
        )
        for relation in relations:
            coefficients = _differentiate_representative(
                algebra,
                relation,
                variables,
            )
            if self._evaluate_coefficients(coefficients) != self.codomain().zero():
                raise ValueError(
                    "the proposed generator images do not annihilate a defining algebra relation under the derivation rule"
                )

    def __call__(self, element):
        algebra = self.domain()
        if algebra in LocalizationRings():
            source = algebra.localization_source()
            _presentation, _labels, variables, _relations, lift = (
                _commutative_presentation_data(source)
            )
            localization_map = algebra.localization_map()

            def differentiate_source(value):
                representative = lift(source(value))
                coefficients = _differentiate_representative(
                    source,
                    representative,
                    variables,
                )
                return self._evaluate_coefficients(
                    tuple(localization_map(coefficient) for coefficient in coefficients)
                )

            numerator, denominator = algebra.localization_fraction_data(algebra(element))
            numerator_derivative = differentiate_source(numerator)
            denominator_derivative = differentiate_source(denominator)
            numerator_image = localization_map(numerator)
            denominator_inverse = algebra.fraction(
                source.one(),
                denominator,
            )
            target = self.codomain()
            first = target.scalar_multiple(
                denominator_inverse,
                numerator_derivative,
            )
            second = target.scalar_multiple(
                numerator_image * denominator_inverse * denominator_inverse,
                denominator_derivative,
            )
            return first + (-second)

        presentation, _labels, variables, _relations, lift = _commutative_presentation_data(
            algebra
        )
        representative = lift(algebra(element))
        coefficients = _differentiate_representative(
            algebra,
            representative,
            variables,
        )
        return self._evaluate_coefficients(coefficients)

    def _call_(self, element):
        return self.__call__(element)

    def lie_bracket(self, other):
        r"""Return the Lie bracket of two vector fields on one algebra."""
        from dzack_research.preamble.categories.algebras.cartan_calculus import (
            _lie_bracket,
        )

        return _lie_bracket(self, other)

    def interior_product(self):
        r"""Return contraction ``i_X`` on the algebraic de Rham complex."""
        from dzack_research.preamble.categories.algebras.cartan_calculus import (
            _interior_product,
        )

        return _interior_product(self)

    def lie_derivative(self):
        r"""Return the Lie derivative ``L_X=[d,i_X]`` on de Rham forms."""
        from dzack_research.preamble.categories.algebras.cartan_calculus import (
            _lie_derivative,
        )

        return _lie_derivative(self)

    @cached_method
    def underlying_linear_morphism(self):
        return DerivationUnderlyingLinearMorphism(
            self.parent().arrow_set(),
            self,
            lambda element: self.restricted_codomain()(self(element)),
        )

    as_morphism = underlying_linear_morphism

    def _lmul_(self, scalar):
        return self.parent().algebra_multiple(scalar, self)

    _rmul_ = _lmul_

    def __add__(self, other):
        if not isinstance(other, Derivation) or other.parent() is not self.parent():
            return NotImplemented
        return self.parent()(
            {
                label: self.generator_image(label) + other.generator_image(label)
                for label in self.parent().generator_labels()
            }
        )

    def __neg__(self):
        return self.parent()(
            {
                label: -self.generator_image(label)
                for label in self.parent().generator_labels()
            }
        )

    def __sub__(self, other):
        return self + (-other)

    def _richcmp_(self, other, op):
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, Derivation)
            and other.parent() is self.parent()
            and all(
                self.generator_image(label) == other.generator_image(label)
                for label in self.parent().generator_labels()
            )
        )
        return equal if op == op_EQ else not equal


class DerivationUnderlyingLinearMorphism(ModuleMorphism):
    r"""The selected underlying linear morphism of one algebra derivation."""

    def __init__(self, parent, derivation, function) -> None:
        self._derivation = derivation
        super().__init__(parent, function, elementwise=True)

    def derivation(self):
        return self._derivation

    def _elementwise_linearity_derivation(self):
        return True

    def __rmul__(self, scalar):
        return self.parent().algebra_multiple(scalar, self)

    def _acted_upon_(self, actor, self_on_left):
        try:
            return self.parent().algebra_multiple(actor, self)
        except (TypeError, ValueError):
            return None

    def _repr_(self):
        return f"Derivation {self.domain()} -> {self.codomain()}"


class _DerivationAlgebraAction(Action):
    def __init__(self, algebra, derivations, is_left) -> None:
        self._derivations = derivations
        Action.__init__(self, _engine_ring(algebra), derivations, is_left, operator.mul)

    def _act_(self, scalar, derivation):
        return self._derivations.algebra_multiple(scalar, derivation)


class DerivationSpace(RestrictedMorCategoryParent):
    r"""The ``A``-module ``Der_R(A,M)`` with its restricted Mor inclusion.

    The actual subobject of ``Hom_R(A,Res_R M)`` is
    ``Res_R Der_R(A,M)``.  Keeping these two scalar structures distinct is
    essential: the derivation module is canonically an ``A``-module, whereas
    its inclusion into the existing ``R``-linear Mor is only ``R``-linear.
    """

    Element = Derivation

    @staticmethod
    def __classcall__(cls, family_or_algebra, domain_or_target, codomain=None):
        if isinstance(family_or_algebra, DerivationCategoryConstruction):
            return typecall(
                cls,
                family_or_algebra,
                domain_or_target,
                codomain,
            )
        return family_or_algebra.derivations(domain_or_target)

    def __init__(self, family, algebra, restricted_target) -> None:
        target_module = restricted_target.module_over_extension()
        if target_module.base_ring() is not algebra:
            raise TypeError("an R-derivation A -> M requires M to be an A-module")
        self._algebra = algebra
        self._target_module = target_module
        presentation_algebra = (
            algebra.localization_source()
            if algebra in LocalizationRings()
            else algebra
        )
        _presentation, labels, _variables, _relations, _lift = _commutative_presentation_data(
            presentation_algebra
        )
        self._generator_labels = labels

        algebra.base_ring()
        structure_map = algebra.algebra_structure_morphism()
        self._restricted_target = restricted_target
        differentials = algebra.kahler_differentials()
        classifiers = differentials.module_category().Mor(differentials, target_module)
        self._preamble_kahler_classifier_module = classifiers
        category = Modules(algebra)
        if classifiers in ModulesWithChosenFinitePresentation(algebra):
            category = ModulesWithChosenFinitePresentation(algebra)
        # Der_R(A,M) is the subcategory of Hom_R(A,Res_R M) carved out by the
        # Leibniz rule, so the existing R-linear Mor category is the base.
        self._preamble_base_ring = algebra
        RestrictedMorCategoryParent.__init__(
            self,
            family,
            algebra,
            restricted_target,
            category=category,
        )
        if classifiers in ModulesWithChosenFinitePresentation(algebra):
            framing_labels = classifiers.module_generating_set()
            relation_matrix = _presentation_matrix(classifiers)
            classifier_presentation = classifiers.presentation()
            presentation = _presentation_from_relation_rows(
                algebra,
                framing_labels,
                classifier_presentation.domain().module_generating_set(),
                relation_matrix,
            )
            _fix_selected_module_framing(
                self,
                algebra,
                framing_labels,
                lambda label: self._from_kahler_classifier(
                    classifiers.module_generator(label)
                ),
                presentation.codomain(),
            )
            _fix_selected_module_presentation(
                self,
                algebra,
                relation_matrix,
                presentation,
            )
        self.register_action(_DerivationAlgebraAction(algebra, self, True))
        self.register_action(_DerivationAlgebraAction(algebra, self, False))

        def restricted_inclusion(restricted_module):
            return restricted_module.Mono(self.arrow_set())._subobject_inclusion(
                lambda restricted_derivation: (
                    restricted_derivation.underlying_element().underlying_linear_morphism()
                ),
            )

        self._restricted_module = _restricted_scalars_view(
            self,
            structure_map,
            _subobject_inclusion_factory=restricted_inclusion,
        )

    def base_ring(self):
        return self._preamble_base_ring

    def algebra(self):
        return self._algebra

    def target_module(self):
        return self._target_module

    def restricted_target_module(self):
        return self._restricted_target

    def restricted_module(self):
        return self._restricted_module

    def inclusion(self):
        return self.restricted_module().inclusion()

    def generator_labels(self):
        return self._generator_labels

    def _kahler_classifier_module(self):
        return self._preamble_kahler_classifier_module

    def _from_kahler_classifier(self, classifier):
        classifiers = self._kahler_classifier_module()
        classifier = classifiers(classifier)
        differentials = classifiers.domain()
        return self(
            {
                label: classifier(differentials.differential_generator(label))
                for label in self.generator_labels()
            }
        )

    def _to_kahler_classifier(self, derivation):
        derivation = self(derivation)
        return self._kahler_classifier_module().domain().from_derivation(derivation)

    def _selected_module_coefficients(self, derivation):
        classifiers = self._kahler_classifier_module()
        return classifiers.framing_coefficients(self._to_kahler_classifier(derivation))

    def __call__(self, generator_images):
        r"""Construct a derivation from its generator images, not an arrow object."""
        return self._element_constructor_(generator_images)

    def _element_constructor_(self, generator_images):
        if isinstance(generator_images, Derivation) and generator_images.parent() is self:
            return generator_images
        if isinstance(generator_images, Morphism):
            if (
                generator_images.domain() is not self.algebra()
                or generator_images.codomain() is not self.restricted_target_module()
            ):
                raise ValueError("the linear map has the wrong derivation endpoints")
            if not isinstance(generator_images, DerivationUnderlyingLinearMorphism):
                raise ValueError(
                    "an arbitrary R-linear map alone does not supply the Leibniz rule required of a derivation"
                )
            selected = generator_images.derivation()
            if selected.parent() is self:
                return selected
            generator_images = {
                label: selected.generator_image(label)
                for label in self.generator_labels()
            }
        return Derivation(self, generator_images)

    def zero(self):
        return self({label: self.target_module().zero() for label in self.generator_labels()})

    def algebra_multiple(self, scalar, derivation):
        if derivation.parent() is not self:
            derivation = self(derivation)
        scalar = self.algebra()(scalar)
        target = self.target_module()
        return self(
            {
                label: target.scalar_multiple(scalar, derivation.generator_image(label))
                for label in self.generator_labels()
            }
        )

    def scalar_multiple(self, scalar, derivation):
        return self.algebra_multiple(scalar, derivation)

    def algebra_action(self):

        endomorphisms = Modules(self.algebra()).End(self)
        return SetMorphism(
            self.algebra().Mor(endomorphisms),
            lambda scalar: endomorphisms.elementwise(
                lambda derivation: self.algebra_multiple(scalar, derivation)
            ),
        )

    scalar_action = algebra_action

    def _repr_(self):
        return f"Der_{self.algebra().base_ring()}({self.algebra()}, {self.target_module()})"


class DerivationCategoryConstruction(_RestrictedMorCategoryOf):
    _declaration_name = "_DerivationCategory"

    def fixed_category_class(self):
        return DerivationSpace

    def accepts(self, arrow) -> bool:
        return isinstance(arrow, DerivationUnderlyingLinearMorphism)


@cached_function(key=lambda algebra, target_module: (id(algebra), id(target_module)))
def _derivations(algebra, target_module) -> DerivationSpace:
    if target_module.base_ring() is not algebra:
        raise TypeError("an R-derivation A -> M requires M to be an A-module")
    base = algebra.base_ring()
    restricted_target = target_module.restrict_scalars(
        algebra.algebra_structure_morphism()
    )
    return DerivationCategoryConstruction(Modules(base)).Of(
        algebra,
        restricted_target,
    )


class GradedDerivation(ModuleElement):
    r"""A homogeneous graded derivation of a represented graded algebra.

    For shift ``r`` this represents a map ``D : A^p -> M^(p+r)`` satisfying
    ``D(ab) = D(a)b + (-1)^(r p) a D(b)`` on homogeneous ``a``.  It is an
    actual ``R``-linear morphism, lying in a represented submodule of
    ``Hom_R(A,M)``.
    """

    def __init__(self, parent, function) -> None:
        if not callable(function):
            raise TypeError("a graded derivation is specified by an element map")
        ModuleElement.__init__(self, parent)
        self._function = function
        observed = self.check_on_generators()
        match observed:
            case False:
                raise ValueError(
                    f"the proposed map is not a degree-{self.degree_shift()} graded derivation"
                )
            case _:
                pass
        derived = self._graded_derivation_derivation()
        match derived:
            case None:
                self._linearity_decision = Unknown
                self._degree_preservation_decision = Unknown
                self._graded_leibniz_decision = Unknown
            case decision if decision is True or decision is Unknown:
                self._linearity_decision = decision
                self._degree_preservation_decision = decision
                self._graded_leibniz_decision = decision
            case _:
                raise ValueError("a graded-derivation construction premise is True or Unknown")

    def _graded_derivation_derivation(self):
        r"""Return a construction-derived graded-derivation premise, or ``None`` for a stated map."""
        return None

    def linearity_decision(self):
        return self._linearity_decision

    def degree_preservation_decision(self):
        return self._degree_preservation_decision

    def graded_leibniz_decision(self):
        return self._graded_leibniz_decision

    def __call__(self, element):
        return self.target()(self._function(self.algebra()(element)))

    def _call_(self, element):
        return self.__call__(element)

    def algebra(self):
        return self.parent().algebra()

    def target(self):
        return self.parent().target()

    def degree_shift(self):
        return self.parent().degree_shift()

    def graded_commutator(self, other):
        r"""Return the graded commutator with another endo-derivation."""
        from dzack_research.preamble.categories.algebras.cartan_calculus import (
            _graded_commutator,
        )

        return _graded_commutator(self, other)

    @cached_method
    def underlying_linear_morphism(self):
        return GradedDerivationUnderlyingLinearMorphism(
            self.parent().arrow_set(),
            self,
            lambda element: self(element),
        )

    as_morphism = underlying_linear_morphism

    def __add__(self, other):
        if not isinstance(other, GradedDerivation) or other.parent() is not self.parent():
            return NotImplemented
        return self.parent()._from_derived_elementwise(
            lambda element: self(element) + other(element),
            self,
            other,
        )

    def __neg__(self):
        return self.parent()._from_derived_elementwise(
            lambda element: -self(element),
            self,
        )

    def __sub__(self, other):
        return self + (-other)

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    _rmul_ = _lmul_

    def __rmul__(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def check_on_generators(self):
        r"""Refute degree/Leibniz on finite selected generators when decidable.

        Passing this finite observation does not prove that an arbitrary
        element map is linear or satisfies Leibniz on all elements; those laws
        remain ``Unknown`` unless the construction supplies their theorem.
        """
        algebra = self.algebra()
        target = self.target()
        if not algebra.is_framed_algebra():
            return Unknown
        labels = algebra.algebra_generating_set()
        finite = labels.cardinality().is_finite()
        match finite:
            case True:
                pass
            case False:
                return Unknown
        for label in labels:
            generator = algebra.algebra_generator(label)
            match generator == algebra.zero():
                case True:
                    continue
                case answer if answer is Unknown:
                    return Unknown
                case False:
                    pass
            if not generator.is_homogeneous():
                return Unknown
            generator_degree = algebra.homogeneous_degree(generator)
            image = self(generator)
            match image == target.zero():
                case True:
                    continue
                case answer if answer is Unknown:
                    return Unknown
                case False:
                    pass
            if not image.is_homogeneous():
                return False
            image_degree = target.homogeneous_degree(image)
            match image_degree == generator_degree + self.degree_shift():
                case True:
                    pass
                case False:
                    return False
                case _:
                    return Unknown
        for left_label in labels:
            left = algebra.algebra_generator(left_label)
            match left == algebra.zero():
                case True:
                    continue
                case answer if answer is Unknown:
                    return Unknown
                case False:
                    pass
            if not left.is_homogeneous():
                return Unknown
            left_degree = algebra.homogeneous_degree(left)
            for right_label in labels:
                right = algebra.algebra_generator(right_label)
                signed_second = left * self(right)
                if (self.degree_shift() * left_degree) % 2:
                    signed_second = -signed_second
                match self(left * right) == self(left) * right + signed_second:
                    case True:
                        pass
                    case False:
                        return False
                    case _:
                        return Unknown
        return True


def _combined_graded_derivation_decision(derivations):
    r"""Transfer the graded-derivation theorem through an operation on actual derivations."""
    decisions = tuple(
        decision
        for derivation in derivations
        for decision in (
            derivation.linearity_decision(),
            derivation.degree_preservation_decision(),
            derivation.graded_leibniz_decision(),
        )
    )
    match all(decision is True for decision in decisions):
        case True:
            return True
        case False:
            return Unknown


class _DerivedGradedDerivation(GradedDerivation):
    r"""A graded derivation whose law premise is transferred from its operands."""

    def __init__(self, parent, function, premise) -> None:
        self._derived_graded_derivation_premise = premise
        super().__init__(parent, function)

    def _graded_derivation_derivation(self):
        return self._derived_graded_derivation_premise


class _ConstructedGradedDerivation(GradedDerivation):
    r"""A graded derivation whose defining construction proves its laws."""

    def _graded_derivation_derivation(self):
        return True


class GradedDerivationUnderlyingLinearMorphism(ModuleMorphism):
    r"""The selected underlying linear morphism of one graded derivation."""

    def __init__(self, parent, derivation, function) -> None:
        self._derivation = derivation
        super().__init__(
            parent,
            function,
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return self.derivation().linearity_decision()

    def derivation(self):
        return self._derivation

    def degree_shift(self):
        return self.derivation().degree_shift()


class GradedDerivationSpace(RestrictedMorCategoryParent):
    r"""The ``R``-submodule of degree-``r`` graded derivations in ``Hom_R``."""

    Element = GradedDerivation

    @staticmethod
    def __classcall__(cls, family_or_algebra, domain_or_target, codomain_or_shift=None):
        if isinstance(family_or_algebra, GradedDerivationCategoryConstruction):
            return typecall(
                cls,
                family_or_algebra,
                domain_or_target,
                codomain_or_shift,
            )
        return family_or_algebra.graded_derivations(
            domain_or_target,
            shift=codomain_or_shift,
        )

    def __init__(self, family, algebra, target) -> None:
        if algebra.base_ring() is not target.base_ring():
            raise ValueError("a graded derivation requires one coefficient ring")
        self._algebra = algebra
        self._target = target
        self._shift = family.degree_shift()

        ring = algebra.base_ring()
        self._preamble_base_ring = ring
        RestrictedMorCategoryParent.__init__(
            self,
            family,
            algebra,
            target,
            category=Cat().meet((Modules(ring), ModuleSubobjects(ring))),
        )

    @cached_method
    def inclusion(self):
        r"""Return the canonical inclusion into the underlying graded linear Mor."""
        return self.Mono(self.arrow_set())._subobject_inclusion(
            lambda derivation: derivation.underlying_linear_morphism(),
        )

    def base_ring(self):
        return self._preamble_base_ring

    def algebra(self):
        return self._algebra

    def target(self):
        return self._target

    def degree_shift(self):
        return self._shift

    def __call__(self, function):
        r"""Construct a graded derivation, not an arrow object."""
        return self._element_constructor_(function)

    def _element_constructor_(self, function):
        if isinstance(function, GradedDerivation) and function.parent() is self:
            return function
        if isinstance(function, Morphism):
            if function.domain() is not self.algebra() or function.codomain() is not self.target():
                raise ValueError("the linear map has the wrong graded-derivation endpoints")
            if (
                not isinstance(function, GradedDerivationUnderlyingLinearMorphism)
                or function.degree_shift() != self.degree_shift()
            ):
                raise ValueError(
                    "an arbitrary R-linear map alone does not supply the graded Leibniz rule required of a graded derivation"
                )
            derivation = function.derivation()
            if derivation.parent() is self:
                return derivation
            return self._from_derived_elementwise(
                lambda element: derivation(element),
                derivation,
            )
        return GradedDerivation(self, function)

    def zero(self):
        return self._from_constructed_elementwise(
            lambda _element: self.target().zero()
        )

    def elementwise(self, function):
        if not callable(function):
            raise TypeError("a graded derivation is specified by an element map")
        return GradedDerivation(self, function)

    def _from_constructed_elementwise(self, function):
        r"""Construct from a formula whose owner proves linearity, degree and Leibniz."""
        return _ConstructedGradedDerivation(self, function)

    def _from_derived_elementwise(self, function, *derivations):
        r"""Construct by a theorem-preserving operation on represented derivations."""
        return _DerivedGradedDerivation(
            self,
            function,
            _combined_graded_derivation_decision(derivations),
        )

    def scalar_multiple(self, scalar, derivation):
        if derivation.parent() is not self:
            derivation = self(derivation)
        scalar = self.base_ring()(scalar)
        target = self.target()
        return self._from_derived_elementwise(
            lambda element: target.scalar_multiple(scalar, derivation(element)),
            derivation,
        )

    def _repr_(self):
        return (
            f"Degree-{self.degree_shift()} graded derivations "
            f"{self.algebra()} -> {self.target()}"
        )


class GradedDerivationCategoryConstruction(_RestrictedMorCategoryOf):
    _declaration_name = "_GradedDerivationCategory"

    @staticmethod
    def __classcall__(cls, base_category, shift):
        return typecall(cls, base_category, int(shift))

    def __init__(self, base_category, shift) -> None:
        self._degree_shift = int(shift)
        super().__init__(base_category)

    def degree_shift(self):
        return self._degree_shift

    def fixed_category_class(self):
        return GradedDerivationSpace

    def accepts(self, arrow) -> bool:
        return (
            isinstance(arrow, GradedDerivationUnderlyingLinearMorphism)
            and arrow.degree_shift() == self.degree_shift()
        )


@cached_function(key=lambda algebra, target, shift=0: (id(algebra), id(target) if target is not None else None, int(shift)))
def _graded_derivations(algebra, target=None, shift=0) -> GradedDerivationSpace:
    if target is None:
        target = algebra
    ring = algebra.base_ring()
    if target not in Modules(ring):
        raise TypeError("a graded derivation target must be a module over the algebra's coefficient ring")
    graded_modules = algebra._graded_module_placement()
    if target not in graded_modules:
        raise TypeError(
            "a graded derivation target must carry the same declared grading as its algebra"
        )
    return GradedDerivationCategoryConstruction(Modules(ring), shift).Of(
        algebra,
        target,
    )


__all__ = [
    "Derivation",
    "DerivationSpace",
    "GradedDerivation",
    "GradedDerivationSpace",
]
