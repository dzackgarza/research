r"""Canonical comparison morphisms among tensor, symmetric, exterior, and divided powers."""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
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
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
)


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


class ConstructionAlgebraHomset(OwnedHomset):
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


def _owned_backend_coefficient(target, coefficient):
    ring = target.base_ring()
    return ring._from_engine_element(_engine_ring(ring)(coefficient))


def _evaluate_tensor_representative(source, target, element):
    representative = _presentation_representative(source, element)
    presentation = (
        source.presentation_ring()
        if hasattr(source, "presentation_ring")
        else source
    )
    engine = _engine_ring(presentation)
    backend = _engine_element(presentation, presentation(representative))
    labels = source.algebra_generating_set()

    def source_label(generator):
        # Private finite backend serialization: Sage's free-monoid generator
        # object has no public position.  Search only the backend generator
        # array required to decode this finitely supported monomial.
        position = next(
            index
            for index, candidate in enumerate(engine.monoid().gens())
            if candidate == generator
        )
        return labels.unrank(position)

    result = target.zero()
    for monomial, coefficient in engine(backend).monomial_coefficients().items():
        value = target.one()
        for generator, exponent in monomial:
            target_generator = target.algebra_generator(source_label(generator))
            value *= target_generator ** int(exponent)
        result += _owned_backend_coefficient(target, coefficient) * value
    return result


def _evaluate_symmetric_representative(source, target, element):
    representative = _presentation_representative(source, element)
    presentation = (
        source.presentation_ring()
        if hasattr(source, "presentation_ring")
        else source
    )
    engine = _engine_ring(presentation)
    backend = _engine_element(presentation, presentation(representative))
    labels = source.algebra_generating_set()
    result = target.zero()
    for exponents, coefficient in engine(backend).dict().items():
        value = target.one()
        for position, exponent in enumerate(exponents):
            if exponent:
                value *= target.algebra_generator(labels.unrank(position)) ** int(exponent)
        result += _owned_backend_coefficient(target, coefficient) * value
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


def divided_to_symmetric(module):
    r"""Return ``Gamma(M) -> Sym(M)`` when every relevant factorial is invertible."""
    source = DividedPowerAlgebraOf(module)
    target = SymmetricAlgebraOf(module)
    ring = module.base_ring()

    def evaluate(element):
        if not isinstance(element, PowerAlgebraElement) or element.parent() is not source:
            element = source(element)
        result = target.zero()
        for degree, component in element.homogeneous_components().items():
            for label, coefficient in module_coefficients(
                component, source.graded_piece(degree)
            ).items():
                denominator = 1
                monomial = target.one()
                if degree == 1:
                    support = ((label, 1),)
                elif degree == 0:
                    support = ()
                else:
                    support = (
                        (generator_label, label.multiplicity(generator_label))
                        for generator_label in label.support()
                    )
                for generator_label, power in support:
                    denominator *= int(factorial(power))
                    monomial *= target.algebra_generator(generator_label) ** int(power)
                denominator_scalar = ring(denominator)
                try:
                    scalar = coefficient / denominator_scalar
                except (TypeError, ZeroDivisionError) as error:
                    raise ValueError(
                        "Gamma(M) -> Sym(M) requires all relevant factorials invertible"
                    ) from error
                if scalar * denominator_scalar != coefficient:
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
