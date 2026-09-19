r"""Codimension-one cycles use the existing divisor rational-equivalence quotient."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AffineCodimensionOneChowComparison,
)
from dzack_research.preamble.categories.divisors.general_divisors import (
    DivisorClassComparison,
)
from dzack_research.preamble.categories.divisors.weil_divisor_groups import (
    WeilDivisorGroups,
)


def _affine_plane_divisor_presentation():
    ring = QQ.polynomial_ring("x,y")
    x = ring.algebra_generator("x")
    scheme = (ring).affine_spectrum(base_ring=QQ)
    full_weil = scheme.full_weil_divisor_group()
    prime = ring.spectrum()(ring.ideal(x))
    prime_divisor = full_weil.prime_divisor(prime)

    principal = ZZ.free_module(1)
    cartier = ZZ.free_module(1)
    finite_weil = WeilDivisorGroups()(ZZ.free_module(1), scheme=scheme)
    principal_generator = principal.module_generator(0)
    cartier_generator = cartier.module_generator(0)
    weil_generator = finite_weil.module_generator(0)
    principal_to_cartier = principal.module_category().Mor(principal, cartier)(
        {0: cartier_generator}
    )
    principal_to_weil = principal.module_category().Mor(principal, finite_weil)(
        {0: weil_generator}
    )
    cartier_to_weil = cartier.module_category().Mor(cartier, finite_weil)(
        {0: weil_generator}
    )
    classes = DivisorClassComparison(
        scheme,
        principal,
        cartier,
        finite_weil,
        principal_to_cartier,
        principal_to_weil,
        cartier_to_weil,
    )
    into_full = finite_weil.module_category().Mor(finite_weil, full_weil)({0: prime_divisor})
    return scheme, ring, x, prime, full_weil, classes, into_full, principal_generator


def test_weil_divisor_cycle_isomorphism_preserves_prime_and_principal_multiplicity() -> None:
    scheme, _ring, x, prime, full_weil, _classes, _into_full, _principal = (
        _affine_plane_divisor_presentation()
    )
    comparison = scheme.weil_cycle_isomorphism()
    divisor = full_weil.principal_divisor(x)
    cycle = comparison.forward()(divisor)

    assert comparison.forward().domain() is full_weil
    assert comparison.forward().codomain().cycle_scheme() is scheme
    assert cycle == comparison.forward().codomain().prime_cycle(prime)
    assert comparison.inverse()(cycle) == divisor


def test_selected_principal_divisors_present_same_class_and_chow_quotient() -> None:
    scheme, _ring, _x, _prime, _full_weil, classes, into_full, principal = (
        _affine_plane_divisor_presentation()
    )
    comparison = AffineCodimensionOneChowComparison(classes, into_full)
    rational = comparison.rational_equivalence_morphism()
    class_to_chow = comparison.class_to_chow_isomorphism()

    assert comparison.scheme() is scheme
    assert rational.domain() is classes.principal_divisor_source()
    assert rational(principal) != comparison.cycle_presentation().zero()
    assert comparison.chow_group().cycle_codimension() == 1
    assert class_to_chow.forward().domain() is classes.class_group()
    assert class_to_chow.forward().codomain() is comparison.chow_group()
    assert classes.class_group().cardinality() == 1
    assert comparison.chow_group().cardinality() == 1
