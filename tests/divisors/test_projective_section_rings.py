r"""Projective section rings retain actual graded pieces and multiplication maps."""

from dzack_research.preamble.all import QQ, ProjectiveSpaces, Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import NN


def test_veronese_section_ring_uses_actual_section_modules_and_component_maps() -> None:
    line = ProjectiveSpaces(QQ)(1)
    bundle = line.O(2)
    ring = bundle.section_ring()
    degree_one = ring.graded_piece(1)
    degree_two = ring.graded_piece(2)
    include_one = ring.homogeneous_component_map(1)
    include_two = ring.homogeneous_component_map(2)
    multiplication = ring.section_multiplication(1, 1)
    labels = tuple(degree_one.module_generating_set())
    left = degree_one.module_generator(labels[0])
    right = degree_one.module_generator(labels[1])
    polynomial_comparison = bundle.homogeneous_polynomial_comparison()
    polynomial_left = polynomial_comparison.forward()(left)
    polynomial_right = polynomial_comparison.forward()(right)

    product = multiplication(polynomial_left, polynomial_right)

    assert ring.section_scheme() is line
    assert ring.section_line_bundle() is bundle
    assert "_preamble_section_scheme" not in ring.__dict__
    assert "_preamble_section_line_bundle" not in ring.__dict__
    assert "_preamble_section_semigroup_generators" not in ring.__dict__
    assert "_preamble_degree_one_section_exponents" not in ring.__dict__
    assert "_preamble_section_line_bundle_degree" not in ring.__dict__
    assert "_preamble_section_block_widths" not in ring.__dict__
    assert degree_one is bundle.global_sections()
    assert degree_one.module_rank() == 3
    assert degree_two.module_rank() == 5
    assert multiplication.left_module() is degree_one
    assert multiplication.right_module() is degree_one
    assert multiplication.codomain() is degree_two
    left_in_ring = ring.homogeneous_component_element(1, polynomial_left)
    right_in_ring = ring.homogeneous_component_element(1, polynomial_right)
    product_in_ring = ring.homogeneous_component_element(2, product)
    assert include_one.codomain() is ring.underlying_module()
    assert include_two.codomain() is ring.underlying_module()
    assert product_in_ring == left_in_ring * right_in_ring
    assert ring.homogeneous_degree(left_in_ring) == NN(1)
    assert ring.homogeneous_degree(product_in_ring) == NN(2)


def test_multiprojective_section_ring_is_segre_veronese_with_exact_factor_roles() -> None:
    factor_labels = finite_ordered_set(("left", "right"))
    line = ProjectiveSpaces(QQ)(1)
    factors = indexed_family(factor_labels, lambda _label: line)
    quadric = Schemes(QQ).product(factors)
    bundle = quadric.O(1, 1)
    ring = bundle.section_ring()
    degree_one = ring.graded_piece(1)
    degree_two = ring.graded_piece(2)
    inclusion_one = ring.homogeneous_component_map(1)
    inclusion_two = ring.homogeneous_component_map(2)
    multiplication = ring.section_multiplication(1, 1)
    labels = tuple(degree_one.module_generating_set())
    first = degree_one.module_generator(labels[0])
    last = degree_one.module_generator(labels[-1])

    product = multiplication(first, last)

    assert ring.section_scheme() is quadric
    assert ring.section_line_bundle() is bundle
    assert tuple(bundle.multidegree()[label] for label in factor_labels) == (1, 1)
    assert degree_one.module_rank() == 4
    assert degree_two.module_rank() == 9
    first_in_ring = ring.homogeneous_component_element(1, first)
    last_in_ring = ring.homogeneous_component_element(1, last)
    product_in_ring = ring.homogeneous_component_element(2, product)
    assert inclusion_one.codomain() is ring.underlying_module()
    assert inclusion_two.codomain() is ring.underlying_module()
    assert product_in_ring == first_in_ring * last_in_ring
    assert ring.homogeneous_degree(product_in_ring) == NN(2)


