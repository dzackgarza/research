r"""A restricted Hom parent keeps both its arrow predicate and extra enrichment."""

from dzack_research.preamble.all import QQ, BasedFreeModule, Derivations, PolynomialRing
from dzack_research.preamble.categories.modules import Modules
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_derivation_space_is_an_enriched_restricted_hom_parent() -> None:
    algebra = PolynomialRing(QQ, "x")
    target = BasedFreeModule(algebra, finite_ordered_set(("e",)))
    derivations = Derivations(algebra, target)
    x = algebra.algebra_generator("x")
    e = target.module_generator("e")
    derivation = derivations({"x": e})

    assert derivation.parent() is derivations
    assert derivations.category().is_subcategory(Modules(algebra))
    assert derivations in Modules(algebra)
    assert derivations.domain_object() is algebra
    assert derivations.codomain_object() is derivations.restricted_target_module()
    assert derivation.as_morphism() in derivations.arrow_set()
    assert derivation in derivations
    assert derivation(x**2) == 2 * x * e
