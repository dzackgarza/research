r"""Derivations of represented commutative algebras.

For an ``R``-algebra ``A`` and an ``A``-module ``M``, ``Derivations(A, M)``
is the ``A``-module of ``R``-derivations ``A -> M``.  On the live finite
polynomial-presentation backend a derivation is specified on the chosen
algebra generators and evaluated by the formal chain rule on a selected
presentation representative.
"""

from sage.categories.action import Action
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.categories.sets_cat import Sets
import operator

from dzack_research.preamble.categories.rings import OwnedRings as _OwnedRings
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.rings import engine_ring


def _commutative_presentation_data(algebra):
    r"""Return ``(P, labels, variables, relations, lift)`` for ``A = P/I``."""
    from dzack_research.preamble.categories.algebras import (
        AlgebrasWithChosenFinitePresentation,
        CommutativeAlgebras,
        SymmetricAlgebras,
    )

    base = algebra.base_ring()
    if algebra not in CommutativeAlgebras(base):
        raise TypeError("Kähler calculus requires a commutative algebra")

    if algebra in AlgebrasWithChosenFinitePresentation(base):
        presentation = algebra.presentation_ring()
        relations = tuple(algebra.relations())
        lift = algebra.lift_to_presentation
    elif algebra in SymmetricAlgebras(base):
        presentation = algebra
        relations = ()
        lift = lambda element: engine_ring(presentation)(element)
    else:
        raise NotImplementedError(
            "the live derivation backend requires a symmetric algebra or a chosen finite commutative polynomial presentation"
        )

    labels = tuple(presentation.algebra_generating_set())
    variables = tuple(
        engine_ring(presentation)(presentation.algebra_generator(label))
        for label in labels
    )
    return presentation, labels, variables, relations, lift


def _differentiate_representative(algebra, representative, variables):
    presentation, _labels, _variables, _relations, _lift = _commutative_presentation_data(
        algebra
    )
    source = engine_ring(presentation)(representative)
    target = engine_ring(algebra)
    return tuple(target(source.derivative(variable)) for variable in variables)


class Derivation(Morphism):
    r"""An actual ``R``-linear arrow ``A -> Res_R(M)`` satisfying Leibniz.

    The public codomain of a derivation remains the original ``A``-module
    ``M``.  :meth:`underlying_linear_morphism` is the corresponding element of
    the canonical ``Hom_R(A, Res_R(M))`` containing this derivation subobject.
    """

    def __init__(self, parent, generator_images) -> None:
        Morphism.__init__(self, parent)
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
        presentation, _labels, variables, relations, _lift = _commutative_presentation_data(
            algebra
        )
        for relation in relations:
            coefficients = _differentiate_representative(
                algebra,
                engine_ring(presentation)(relation),
                variables,
            )
            if self._evaluate_coefficients(coefficients) != self.codomain().zero():
                raise ValueError(
                    "the proposed generator images do not annihilate a defining algebra relation under the derivation rule"
                )

    def __call__(self, element):
        algebra = self.domain()
        presentation, _labels, variables, _relations, lift = _commutative_presentation_data(
            algebra
        )
        representative = engine_ring(presentation)(lift(element))
        coefficients = _differentiate_representative(
            algebra,
            representative,
            variables,
        )
        return self._evaluate_coefficients(coefficients)

    def _call_(self, element):
        return self.__call__(element)

    def underlying_linear_morphism(self):
        morphism = self.parent().ambient_hom().elementwise(
            lambda element: self.restricted_codomain()(self(element))
        )
        morphism._preamble_is_derivation = True
        morphism._preamble_derivation = self
        return morphism

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
        Action.__init__(self, engine_ring(algebra), derivations, is_left, operator.mul)

    def _act_(self, scalar, derivation):
        return self._derivations.algebra_multiple(scalar, derivation)


class DerivationSpace(Homset):
    r"""The ``A``-module ``Der_R(A,M)`` with its restricted Hom inclusion.

    The actual subobject of ``Hom_R(A,Res_R M)`` is
    ``Res_R Der_R(A,M)``.  Keeping these two scalar structures distinct is
    essential: the derivation module is canonically an ``A``-module, whereas
    its inclusion into the ambient Hom is only ``R``-linear.
    """

    Element = Derivation

    def __init__(self, algebra, target_module) -> None:
        if target_module.base_ring() is not algebra:
            raise TypeError("an R-derivation A -> M requires M to be an A-module")
        self._algebra = algebra
        self._target_module = target_module
        _presentation, labels, _variables, _relations, _lift = _commutative_presentation_data(
            algebra
        )
        self._generator_labels = labels
        from dzack_research.preamble.categories.modules import (
            ModuleSubobjects,
            Modules,
            module_embedding,
            restrict_scalars,
        )
        from dzack_research.preamble.refine import refine

        base = algebra.base_ring()
        structure_map = algebra.algebra_structure_morphism()
        self._restricted_target = restrict_scalars(
            target_module,
            structure_map,
        )
        Homset.__init__(self, algebra, target_module, category=Sets())
        self._preamble_base_ring = algebra
        refine(self, Modules(algebra))
        self.register_action(_DerivationAlgebraAction(algebra, self, True))
        self.register_action(_DerivationAlgebraAction(algebra, self, False))
        self._restricted_module = restrict_scalars(self, structure_map)
        self._ambient_hom = Modules(base).Hom(algebra, self._restricted_target)
        self._preamble_inclusion = module_embedding(
            self._restricted_module,
            self._ambient_hom,
            lambda restricted_derivation: (
                restricted_derivation.underlying_element().underlying_linear_morphism()
            ),
            verify_linearity=False,
        )
        self._restricted_module._preamble_inclusion = self._preamble_inclusion
        refine(self._restricted_module, ModuleSubobjects(base))

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

    def ambient_hom(self):
        return self._ambient_hom

    def inclusion(self):
        return self._preamble_inclusion

    def generator_labels(self):
        return self._generator_labels

    def _element_constructor_(self, generator_images):
        if isinstance(generator_images, Derivation) and generator_images.parent() is self:
            return generator_images
        if isinstance(generator_images, Morphism):
            if (
                generator_images.domain() is not self.algebra()
                or generator_images.codomain() is not self.restricted_target_module()
            ):
                raise ValueError("the linear map has the wrong derivation endpoints")
            if not getattr(generator_images, "_preamble_is_derivation", False):
                raise ValueError(
                    "an arbitrary R-linear map cannot be certified as a derivation by this backend"
                )
            generator_images = {
                label: generator_images(self.algebra().algebra_generator(label)).underlying_element()
                for label in self.generator_labels()
            }
        return self.element_class(self, generator_images)

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
        from dzack_research.preamble.categories.modules import Modules

        endomorphisms = Modules(self.algebra()).End(self)
        return SetMorphism(
            Hom(self.algebra(), endomorphisms, _OwnedRings()),
            lambda scalar: endomorphisms.elementwise(
                lambda derivation: self.algebra_multiple(scalar, derivation)
            ),
        )

    scalar_action = algebra_action

    def _repr_(self):
        return f"Der_{self.algebra().base_ring()}({self.algebra()}, {self.target_module()})"


_DERIVATION_SPACES = {}


def Derivations(algebra, target_module) -> DerivationSpace:
    key = (id(algebra), id(target_module))
    cached = _DERIVATION_SPACES.get(key)
    if (
        cached is not None
        and cached.algebra() is algebra
        and cached.target_module() is target_module
    ):
        return cached
    result = DerivationSpace(algebra, target_module)
    _DERIVATION_SPACES[key] = result
    return result


class GradedDerivation(ModuleMorphism):
    r"""A homogeneous graded derivation of a represented graded algebra.

    For shift ``r`` this represents a map ``D : A^p -> M^(p+r)`` satisfying
    ``D(ab) = D(a)b + (-1)^(r p) a D(b)`` on homogeneous ``a``.  It is an
    actual ``R``-linear morphism, lying in a represented submodule of
    ``Hom_R(A,M)``.
    """

    def __init__(self, parent, function) -> None:
        if not callable(function):
            raise TypeError("a graded derivation is specified by an element map")
        ModuleMorphism.__init__(
            self,
            parent,
            function,
            elementwise=True,
            verify_linearity=False,
        )
        if not self.check_on_generators():
            raise ValueError(
                f"the proposed map is not a degree-{self.degree_shift()} graded derivation"
            )

    def algebra(self):
        return self.parent().algebra()

    def target(self):
        return self.parent().target()

    def degree_shift(self):
        return self.parent().degree_shift()

    def underlying_linear_morphism(self):
        morphism = self.parent().ambient_hom().elementwise(
            lambda element: self(element),
            verify_linearity=False,
        )
        morphism._preamble_is_graded_derivation = True
        morphism._preamble_graded_derivation = self
        morphism._preamble_degree_shift = self.degree_shift()
        return morphism

    def check_on_generators(self) -> bool:
        r"""Check degree and graded Leibniz on a selected finite algebra framing."""
        labels = tuple(self.algebra().algebra_generating_set())
        generators = tuple(self.algebra().algebra_generator(label) for label in labels)
        for generator in generators:
            image = self(generator)
            if (
                generator.is_homogeneous()
                and image != self.target().zero()
                and (
                    not image.is_homogeneous()
                    or image.degree()
                    != (
                    generator.degree() + self.degree_shift()
                    )
                )
            ):
                return False
        for left in generators:
            if not left.is_homogeneous():
                return False
            for right in generators:
                signed_second = left * self(right)
                if (self.degree_shift() * left.degree()) % 2:
                    signed_second = -signed_second
                if self(left * right) != self(left) * right + signed_second:
                    return False
        return True


class GradedDerivationSpace(Homset):
    r"""The ``R``-submodule of degree-``r`` graded derivations in ``Hom_R``."""

    Element = GradedDerivation

    def __init__(self, algebra, target, shift) -> None:
        if algebra.base_ring() is not target.base_ring():
            raise ValueError("a graded derivation requires one coefficient ring")
        self._algebra = algebra
        self._target = target
        self._shift = int(shift)
        from dzack_research.preamble.categories.modules import (
            ModuleSubobjects,
            Modules,
            module_embedding,
        )
        from dzack_research.preamble.refine import refine

        ring = algebra.base_ring()
        self._ambient_hom = Modules(ring).Hom(algebra, target)
        Homset.__init__(self, algebra, target, category=Sets())
        self._preamble_base_ring = ring
        refine(self, [Modules(ring), ModuleSubobjects(ring)])
        self._preamble_inclusion = module_embedding(
            self,
            self._ambient_hom,
            lambda derivation: derivation.underlying_linear_morphism(),
            verify_linearity=False,
        )

    def base_ring(self):
        return self._preamble_base_ring

    def algebra(self):
        return self._algebra

    def target(self):
        return self._target

    def degree_shift(self):
        return self._shift

    def _element_constructor_(self, function):
        if isinstance(function, GradedDerivation) and function.parent() is self:
            return function
        if isinstance(function, Morphism):
            if function.domain() is not self.algebra() or function.codomain() is not self.target():
                raise ValueError("the linear map has the wrong graded-derivation endpoints")
            derivation = getattr(function, "_preamble_graded_derivation", None)
            if (
                derivation is None
                or getattr(function, "_preamble_degree_shift", None) != self.degree_shift()
            ):
                raise ValueError(
                    "an arbitrary R-linear map cannot be certified as a graded derivation by this backend"
                )
            return self.element_class(self, lambda element: derivation(element))
        return self.element_class(self, function)

    def ambient_hom(self):
        return self._ambient_hom

    def inclusion(self):
        return self._preamble_inclusion

    def zero(self):
        return self.elementwise(lambda _element: self.target().zero())

    def elementwise(self, function):
        if not callable(function):
            raise TypeError("a graded derivation is specified by an element map")
        return self.element_class(self, function)

    def scalar_multiple(self, scalar, derivation):
        if derivation.parent() is not self:
            derivation = self(derivation)
        scalar = self.base_ring()(scalar)
        target = self.target()
        return self.elementwise(
            lambda element: target.scalar_multiple(scalar, derivation(element))
        )

    def _repr_(self):
        return (
            f"Degree-{self.degree_shift()} graded derivations "
            f"{self.algebra()} -> {self.target()}"
        )


_GRADED_DERIVATION_SPACES = {}


def GradedDerivations(algebra, target=None, shift=0) -> GradedDerivationSpace:
    if target is None:
        target = algebra
    key = (id(algebra), id(target), int(shift))
    cached = _GRADED_DERIVATION_SPACES.get(key)
    if (
        cached is not None
        and cached.algebra() is algebra
        and cached.target() is target
        and cached.degree_shift() == int(shift)
    ):
        return cached
    result = GradedDerivationSpace(algebra, target, shift)
    _GRADED_DERIVATION_SPACES[key] = result
    return result


__all__ = [
    "Derivation",
    "DerivationSpace",
    "Derivations",
    "GradedDerivation",
    "GradedDerivationSpace",
    "GradedDerivations",
]
