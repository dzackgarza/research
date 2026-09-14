r"""Graded derivations use the owned category meet for restricted-Hom placement."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras import (
    Derivations,
    FinitelyPresentedAlgebra,
    KahlerDifferentials,
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.modules import Modules, ModuleSubobjects, ring_as_module


def test_derivation_space_retains_module_subobject_and_inclusion_structure() -> None:
    polynomial = SymmetricAlgebraOn(QQ, ("x", "y"))
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = FinitelyPresentedAlgebra(polynomial, [x * y])
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")
    values = ring_as_module(algebra)
    derivation = Derivations(algebra, values)(
        {
            "x": values.scalar_multiple(xbar, values.module_generator(0)),
            "y": values.scalar_multiple(-ybar, values.module_generator(0)),
        }
    )
    derivations = derivation.parent()
    restricted = derivations.restricted_module()
    inclusion = derivations.inclusion()

    assert derivations in Modules(algebra)
    assert restricted in ModuleSubobjects(QQ)
    assert inclusion.domain() is restricted
    assert inclusion.codomain() is derivations.arrow_set()
    assert inclusion(restricted(derivation))(xbar).underlying_element() == derivation(xbar)

    omega = KahlerDifferentials(algebra)
    classifier = omega.from_derivation(derivation)
    assert classifier(omega.universal_derivation()(xbar + ybar)) == derivation(xbar + ybar)
