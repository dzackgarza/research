"""General divisor theory beyond torus-invariant presentations."""

import pytest

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    QuadraticField,
)
from dzack_research.preamble.categories.divisors.cartier_divisor_groups import (
    CartierDivisorGroups,
)
from dzack_research.preamble.categories.divisors.general_divisors import (
    DivisorClassComparison,
    FiniteAtlasCartierDivisor,
)
from dzack_research.preamble.categories.divisors.picard_groups import (
    PicardGroups,
)
from dzack_research.preamble.categories.divisors.weil_divisor_groups import WeilDivisorGroups


def _cyclic_module(order):
    generators = ZZ.free_module(1)
    relations = ZZ.free_module(1)
    return relations.Mor(generators)(
            {0: ZZ(order) * generators.module_generator(0)}
        ).cokernel()


def test_projective_space_over_a_field_has_the_hyperplane_picard_generator() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    base_picard = PicardGroups().trivial(plane.base_scheme())
    picard = plane.picard_group(base_picard)

    assert picard.picard_scheme() is plane
    assert picard.projective_base_picard_group() is base_picard
    assert picard.projective_hyperplane_factor().module_rank() == 1
    assert picard.module_rank() == 1
    assert picard.hyperplane_class() != picard.zero()


def test_projective_space_keeps_a_nontrivial_base_picard_factor() -> None:
    field = QuadraticField(-5, "a")
    assert field.class_number() == 2
    order = field.ring_of_integers()
    base = (order).affine_spectrum(base_ring=order)
    base_picard = PicardGroups()(_cyclic_module(2), scheme=base)
    relative_line = ProjectiveSpaces(order)(1)
    picard = relative_line.picard_group(base_picard)

    base_generator = base_picard.module_generator(0)
    pulled_base_class = picard.base_picard_inclusion()(base_generator)
    hyperplane = picard.hyperplane_class()

    assert pulled_base_class != picard.zero()
    assert pulled_base_class.additive_order() == 2
    assert hyperplane != picard.zero()
    assert picard.module_rank() == 2
    assert picard.projective_base_picard_group() is base_picard


def test_cartier_local_equations_produce_units_and_the_associated_line_bundle() -> None:
    line = ProjectiveSpaces(QQ)(1)
    datum = line.glued_from_standard_charts().gluing_datum()
    left_ring = datum.chart(0).coordinate_algebra()
    right_ring = datum.chart(1).coordinate_algebra()
    x0_over_x1 = right_ring.algebra_generator("x0_over_x1")

    point_at_infinity = FiniteAtlasCartierDivisor(
        datum,
        {0: left_ring.one(), 1: x0_over_x1},
    )
    transition = point_at_infinity.transition_unit(0, 1)
    bundle = point_at_infinity.associated_invertible_sheaf()

    assert transition.is_unit()
    assert transition != datum.overlap(0, 1).coordinate_algebra().one()
    assert bundle.scheme() is datum.scheme()
    assert bundle.associated_divisor() is point_at_infinity
    assert bundle.transition_unit(0, 1) == transition


def test_normal_a1_surface_has_a_weil_prime_that_is_not_cartier() -> None:
    polynomial = QQ.polynomial_ring("x,y,z")
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    z = polynomial.algebra_generator("z")
    ring = polynomial.quotient_ring(polynomial.ideal(x * y - z**2))
    x, y, z = ring(x), ring(y), ring(z)
    scheme = (ring).affine_spectrum(base_ring=QQ)

    assert ring.is_normal()
    prime_ideal = ring.ideal(x, z)
    prime = ring.spectrum()(prime_ideal)
    vertex = ring.spectrum()(ring.ideal(x, y, z))
    assert prime.height() == 1

    full_weil = scheme.full_weil_divisor_group()
    assert full_weil.divisor_scheme() is scheme
    assert full_weil.affine_divisor_coordinate_ring() is ring
    assert full_weil.prime_divisor_locus() is full_weil.module_generating_set()
    prime_divisor = full_weil.prime_divisor(prime)
    assert not full_weil.prime_is_cartier_at(prime, vertex)
    assert full_weil.prime_is_cartier_at(prime, prime)
    outside_prime = ring.spectrum()(ring.ideal(y, z))
    assert full_weil.prime_is_cartier_at(prime, outside_prime)

    # Since principal divisors are Cartier, a Weil divisor that fails to be
    # Cartier at one point cannot become Cartier after adding a principal
    # divisor.  Thus this is genuinely a non-Cartier Weil *class*, not merely
    # a selected nonprincipal equation.
    divisor_of_x = full_weil.principal_divisor(x)
    assert full_weil.multiplicity(divisor_of_x, prime) == 2
    assert divisor_of_x == 2 * prime_divisor

    principal = ZZ.free_module(1)
    cartier = CartierDivisorGroups()(ZZ.free_module(1), scheme=scheme)
    weil_presentation = WeilDivisorGroups()(ZZ.free_module(1), scheme=scheme)
    assert weil_presentation.divisor_scheme() is scheme
    with pytest.raises(TypeError, match="no represented full prime-divisor locus"):
        weil_presentation.prime_divisor_locus()
    with pytest.raises(TypeError, match="not an affine-normal divisor group"):
        weil_presentation.affine_divisor_coordinate_ring()
    principal_generator = principal.module_generator(0)
    cartier_generator = cartier.module_generator(0)
    weil_generator = weil_presentation.module_generator(0)

    principal_to_cartier = principal.module_category().Mor(principal, cartier)(
        {0: cartier_generator}
    )
    principal_to_weil = principal.module_category().Mor(principal, weil_presentation)(
        {0: 2 * weil_generator}
    )
    cartier_to_weil = cartier.module_category().Mor(cartier, weil_presentation)(
        {0: 2 * weil_generator}
    )
    classes = DivisorClassComparison(
        scheme,
        principal,
        cartier,
        weil_presentation,
        principal_to_cartier,
        principal_to_weil,
        cartier_to_weil,
    )

    presentation_into_full_weil = weil_presentation.module_category().Mor(weil_presentation, full_weil)(
        {0: prime_divisor}
    )
    assert presentation_into_full_weil(
        principal_to_weil(principal_generator)
    ) == divisor_of_x
    assert classes.picard_group().cardinality() == 1
    assert classes.class_group().cardinality() == 2
    noncartier_class = classes.weil_class_projection()(weil_generator)
    assert noncartier_class != classes.class_group().zero()
    assert noncartier_class.additive_order() == 2
    assert classes.picard_to_class_group_morphism().domain() is classes.picard_group()
    assert classes.picard_to_class_group_morphism().codomain() is classes.class_group()
