r"""Canonical comparison morphisms among tensor, symmetric, exterior, and divided powers."""

from sage.arith.misc import factorial

from dzack_research.preamble.categories.algebras.algebras import Algebras


def _constructed_algebra_morphism(domain, codomain, evaluator):
    r"""Return a theorem-supplied map through the ordinary unital algebra Mor."""
    if domain.base_ring() is not codomain.base_ring():
        raise ValueError(
            f"a morphism of algebras {domain} -> {codomain} needs one base ring, but they are over "
            f"{domain.base_ring()} and {codomain.base_ring()}"
        )
    mor = Algebras(domain.base_ring()).Associative().Unital().Mor(
        domain,
        codomain,
    )
    return mor._from_constructed_element_map(evaluator)


def _tensor_to_symmetric(module):
    r"""Return the quotient morphism ``T(M) -> Sym(M)``."""
    source = module.tensor_algebra()
    target = module.symmetric_algebra()
    return source.Mor(target)(
        lambda label: target.algebra_generator(label)
    )


def _tensor_to_alternating(module):
    r"""Return the quotient morphism ``T(M) -> Lambda(M)``."""
    source = module.tensor_algebra()
    target = module.exterior_algebra()
    return source.Mor(target)(
        lambda label: target.from_component(
            1,
            target.generating_module().module_generator(label),
        )
    )


def _symmetric_to_divided(module):
    r"""Return ``Sym(M) -> Gamma(M)``, ``x^n |-> n! gamma_n(x)``."""
    source = module.symmetric_algebra()
    target = module.divided_power_algebra()
    return source.Mor(target)(
        lambda label: target.from_component(
            1,
            target.generating_module().module_generator(label),
        )
    )


def _divided_to_symmetric(module):
    r"""Return ``Gamma(M) -> Sym(M)`` when every relevant factorial is invertible."""
    source = module.divided_power_algebra()
    target = module.symmetric_algebra()
    ring = module.base_ring()

    def evaluate(element):
        element = source(element)
        result = target.zero()
        for degree, component in element.homogeneous_components().items():
            for label, coefficient in source.graded_piece(degree).framing_coefficients(component).items():
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
                if not denominator_scalar.is_unit():
                    raise ValueError(
                        f"the map Gamma(M) -> Sym(M) needs the factorial {denominator_scalar} to be invertible, but it "
                        f"does not divide {coefficient}"
                    )
                scalar = coefficient * denominator_scalar.inverse_of_unit()
                result += scalar * monomial
        return result

    return _constructed_algebra_morphism(source, target, evaluate)


__all__ = [
]
