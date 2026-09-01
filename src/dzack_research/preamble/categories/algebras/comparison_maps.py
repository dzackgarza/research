r"""Canonical comparison morphisms among tensor, symmetric, exterior, and divided powers."""

from sage.arith.misc import factorial
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.framed_free_algebras import (
    AlternatingAlgebraOf,
    SymmetricAlgebraOf,
    TensorAlgebraOf,
)
from dzack_research.preamble.categories.algebras.power_algebras import (
    DividedPowerAlgebraOf,
    PowerAlgebraElement,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings import engine_ring


class ConstructionAlgebraMorphism(Morphism):
    r"""An algebra morphism whose action is determined by a construction map."""

    def __init__(self, parent, evaluator) -> None:
        Morphism.__init__(self, parent)
        self._evaluator = evaluator

    def _call_(self, element):
        return self._evaluator(element)

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return construction_algebra_homset(other.domain(), self.codomain())(
            lambda element: self(other(element))
        )


class ConstructionAlgebraHomset(Homset):
    Element = ConstructionAlgebraMorphism

    def __init__(self, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("construction algebra maps require one common base ring")
        Homset.__init__(
            self,
            domain,
            codomain,
            category=Algebras(domain.base_ring()),
        )

    def _element_constructor_(self, evaluator):
        return self.element_class(self, evaluator)


def construction_algebra_homset(domain, codomain):
    return ConstructionAlgebraHomset(domain, codomain)


def _presentation_representative(algebra, element):
    lift = getattr(algebra, "lift_to_presentation", None)
    if lift is None:
        return element
    return lift(element)


def _evaluate_tensor_representative(source, target, element):
    representative = _presentation_representative(source, element)
    presentation = (
        source.presentation_ring()
        if hasattr(source, "presentation_ring")
        else source
    )
    engine = engine_ring(presentation)
    labels = tuple(source.algebra_generating_set())
    monoid_labels = dict(zip(engine.monoid().gens(), labels, strict=True))
    result = target.zero()
    for monomial, coefficient in engine(representative).monomial_coefficients().items():
        value = target.one()
        for generator, exponent in monomial:
            target_generator = target.algebra_generator(monoid_labels[generator])
            for _ in range(int(exponent)):
                value *= target_generator
        result += coefficient * value
    return result


def _evaluate_symmetric_representative(source, target, element):
    representative = _presentation_representative(source, element)
    presentation = (
        source.presentation_ring()
        if hasattr(source, "presentation_ring")
        else source
    )
    engine = engine_ring(presentation)
    labels = tuple(source.algebra_generating_set())
    result = target.zero()
    for exponents, coefficient in engine(representative).dict().items():
        value = target.one()
        for label, exponent in zip(labels, exponents, strict=True):
            value *= target.algebra_generator(label) ** int(exponent)
        result += coefficient * value
    return result


def tensor_to_symmetric(module):
    r"""Return the quotient morphism ``T(M) -> Sym(M)``."""
    source = TensorAlgebraOf(module)
    target = SymmetricAlgebraOf(module)
    return construction_algebra_homset(source, target)(
        lambda element: _evaluate_tensor_representative(source, target, element)
    )


def tensor_to_alternating(module):
    r"""Return the quotient morphism ``T(M) -> Lambda(M)``."""
    source = TensorAlgebraOf(module)
    target = AlternatingAlgebraOf(module)
    return construction_algebra_homset(source, target)(
        lambda element: _evaluate_tensor_representative(source, target, element)
    )


def symmetric_to_divided(module):
    r"""Return ``Sym(M) -> Gamma(M)``, ``x^n |-> n! gamma_n(x)``."""
    source = SymmetricAlgebraOf(module)
    target = DividedPowerAlgebraOf(module)
    return construction_algebra_homset(source, target)(
        lambda element: _evaluate_symmetric_representative(source, target, element)
    )


def _divided_label_exponent(module, degree, label):
    labels = tuple(module.module_generating_set())
    if degree == 0:
        return tuple(0 for _ in labels)
    if degree == 1:
        exponent = [0] * len(labels)
        exponent[labels.index(label)] = 1
        return tuple(exponent)
    if degree == 2:
        exponent = [0] * len(labels)
        if label[0] == "gamma2":
            exponent[labels.index(label[1])] = 2
        else:
            exponent[labels.index(label[1])] = 1
            exponent[labels.index(label[2])] = 1
        return tuple(exponent)
    return tuple(int(value) for value in label)


def divided_to_symmetric(module):
    r"""Return ``Gamma(M) -> Sym(M)`` when every multi-factorial is invertible.

    On a divided monomial ``gamma_{a_1}(x_1)...gamma_{a_r}(x_r)`` this is
    ``x_1^{a_1}...x_r^{a_r}/(a_1!...a_r!)``.  Over a characteristic-zero
    field this is inverse to :func:`symmetric_to_divided`.
    """
    source = DividedPowerAlgebraOf(module)
    target = SymmetricAlgebraOf(module)
    ring = module.base_ring()
    engine = engine_ring(ring)
    labels = tuple(module.module_generating_set())

    def evaluate(element):
        if not isinstance(element, PowerAlgebraElement) or element.parent() is not source:
            element = source(element)
        result = target.zero()
        for degree, component in element.homogeneous_components().items():
            for label, coefficient in module_coefficients(
                component, source.graded_piece(degree)
            ).items():
                exponent = _divided_label_exponent(module, degree, label)
                denominator = 1
                monomial = target.one()
                for generator_label, power in zip(labels, exponent, strict=True):
                    denominator *= factorial(power)
                    monomial *= target.algebra_generator(generator_label) ** power
                try:
                    scalar = engine(coefficient) / engine(denominator)
                except (TypeError, ZeroDivisionError) as error:
                    raise ValueError(
                        "Gamma(M) -> Sym(M) requires all relevant factorials invertible"
                    ) from error
                if scalar * engine(denominator) != engine(coefficient):
                    raise ValueError(
                        "Gamma(M) -> Sym(M) requires all relevant factorials invertible"
                    )
                result += scalar * monomial
        return result

    return construction_algebra_homset(source, target)(evaluate)


__all__ = [
    "ConstructionAlgebraHomset",
    "ConstructionAlgebraMorphism",
    "construction_algebra_homset",
    "divided_to_symmetric",
    "symmetric_to_divided",
    "tensor_to_alternating",
    "tensor_to_symmetric",
]
