r"""Derivations of represented commutative algebras.

For an ``R``-algebra ``A`` and an ``A``-module ``M``, ``Derivations(A, M)``
is the ``A``-module of ``R``-derivations ``A -> M``.  On the live finite
polynomial-presentation backend a derivation is specified on the chosen
algebra generators and evaluated by the formal chain rule on a selected
presentation representative.
"""

from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

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


class Derivation(ModuleElement):
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

    def _add_(self, other):
        return self.parent()(
            {
                label: self.generator_image(label) + other.generator_image(label)
                for label in self.parent().generator_labels()
            }
        )

    def _neg_(self):
        return self.parent()(
            {
                label: -self.generator_image(label)
                for label in self.parent().generator_labels()
            }
        )

    def _lmul_(self, scalar):
        target = self.codomain()
        return self.parent()(
            {
                label: target.scalar_multiple(scalar, self.generator_image(label))
                for label in self.parent().generator_labels()
            }
        )

    _rmul_ = _lmul_

    def _repr_(self):
        return f"Derivation {self.domain()} -> {self.codomain()}"


class DerivationSpace(Parent):
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
        from dzack_research.preamble.categories.modules import Modules

        Parent.__init__(self, base=algebra, category=Modules(algebra))

    def algebra(self):
        return self._algebra

    def target_module(self):
        return self._target_module

    def generator_labels(self):
        return self._generator_labels

    def _element_constructor_(self, generator_images):
        if isinstance(generator_images, Derivation) and generator_images.parent() is self:
            return generator_images
        return self.element_class(self, generator_images)

    def zero(self):
        return self({label: self.target_module().zero() for label in self.generator_labels()})

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


class GradedDerivation(SageObject):
    r"""A homogeneous graded derivation of a represented graded algebra.

    For shift ``r`` this represents a map ``D : A^p -> M^(p+r)`` satisfying
    ``D(ab) = D(a)b + (-1)^(r p) a D(b)`` on homogeneous ``a``.  The live
    carrier is intentionally generic: concrete structured constructions may
    provide stronger finite checks through :meth:`check_on_generators`.
    """

    def __init__(self, algebra, target, shift, function) -> None:
        self._algebra = algebra
        self._target = target
        self._shift = int(shift)
        if not callable(function):
            raise TypeError("a graded derivation is specified by an element map")
        self._function = function

    def algebra(self):
        return self._algebra

    domain = algebra

    def target(self):
        return self._target

    codomain = target

    def degree_shift(self):
        return self._shift

    def __call__(self, element):
        if element.parent() is not self.algebra():
            element = self.algebra()(element)
        image = self._function(element)
        return image if image.parent() is self.target() else self.target()(image)

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


class GradedDerivationSpace(Parent):
    Element = GradedDerivation

    def __init__(self, algebra, target, shift) -> None:
        self._algebra = algebra
        self._target = target
        self._shift = int(shift)
        from sage.categories.sets_cat import Sets

        Parent.__init__(self, category=Sets())

    def algebra(self):
        return self._algebra

    def target(self):
        return self._target

    def degree_shift(self):
        return self._shift

    def _element_constructor_(self, function):
        return self.element_class(
            self.algebra(),
            self.target(),
            self.degree_shift(),
            function,
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
