r"""Graded derivations use the owned category meet for restricted-Hom placement."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.modules import Modules, ModuleSubobjects


def test_derivation_space_retains_module_subobject_and_inclusion_structure() -> None:
    polynomial = QQ.free_module(("x", "y")).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = (polynomial).quotient_by_relations([x * y])
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")
    values = algebra.regular_module()
    derivation = algebra.derivations(values)(
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
    underlying = derivation.underlying_linear_morphism()
    assert underlying.derivation() is derivation
    assert derivations(underlying) is derivation

    omega = algebra.kahler_differentials()
    classifier = omega.from_derivation(derivation)
    assert classifier(omega.universal_derivation()(xbar + ybar)) == derivation(xbar + ybar)
