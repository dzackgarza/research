r"""Reduced normalization, total quotients, and finite local lengths."""

from dzack_research.preamble.all import QQ, IsolatedHypersurfaceSingularity


def test_reducible_node_normalizes_componentwise_and_retains_the_map() -> None:
    polynomial = QQ.polynomial_ring("x", "y")
    x, y = tuple(polynomial.algebra_generators())
    node = polynomial.quotient_ring(polynomial.ideal(x * y))

    assert node.is_reduced()
    assert node.minimal_primes().cardinality() == 2
    assert node.irreducible_components().cardinality() == 2
    components = node.normalization_components()
    assert components.cardinality() == 2
    for minimal_prime, component, component_map in components:
        assert minimal_prime.ring() is node
        assert component_map.domain() is node
        assert component_map.codomain() is component
    normalization = node.normalization()
    normalization_map = node.normalization_map()
    assert normalization_map.domain() is node
    assert normalization_map.codomain() is normalization
    assert node.conductor_ideal().ring() is node
    assert node.delta_invariant() == 1


def test_total_quotient_ring_of_reduced_node_is_product_of_component_fields() -> None:
    polynomial = QQ.polynomial_ring("x", "y")
    x, y = tuple(polynomial.algebra_generators())
    node = polynomial.quotient_ring(polynomial.ideal(x * y))

    total = node.total_quotient_ring()
    total_map = node.total_quotient_map()
    assert total_map.domain() is node
    assert total_map.codomain() is total
    assert total_map(node(x + y)).is_unit()
    assert not total_map(node(x)).is_unit()


def test_local_length_divides_out_nonrational_residue_degree() -> None:
    polynomial = QQ.polynomial_ring("x")
    x = polynomial.algebra_generator("x")
    prime = polynomial.ideal(x**2 + 1)
    point = polynomial.spectrum()(prime)

    assert point.residue_degree() == 2
    assert point.local_length(prime) == 1
    assert point.local_length(prime.power(2)) == 2


def test_plane_curve_conductor_lives_in_the_curve_local_ring() -> None:
    polynomial = QQ.polynomial_ring("x", "y")
    x, y = tuple(polynomial.algebra_generators())
    cusp = IsolatedHypersurfaceSingularity(polynomial, y**2 - x**3)

    conductor = cusp.conductor_ideal_at_origin()
    local_curve = conductor.ring()
    curve = local_curve.localization_source()
    assert curve.defining_ideal().contains_ambient_element(y**2 - x**3)
    assert local_curve.localization_map()(curve(x)) in conductor
    assert local_curve.localization_map()(curve(y)) in conductor
