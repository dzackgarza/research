r"""The section ring of O(1) on P^2 has degree-one dimension three."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_hyperplane_section_ring_of_projective_plane() -> None:
    plane = RationalPolyhedralFans(ZZ.free_module(2)).projective_space_fan().toric_variety(QQ)
    divisor = plane.hyperplane_divisor()
    ring = plane.section_ring(divisor)

    assert ring in SectionRings(QQ)
    assert ring.section_scheme() is plane
    assert ring.section_divisor() == divisor
    assert ring.graded_piece(1).module_rank() == 3
    assert ring.graded_piece(2).module_rank() == 6
    labels = tuple(ring.algebra_generating_set())
    assert ring.section_semigroup_generators().cardinality() == cardinal(3)
    assert all(ring.generator_degree(label) == 1 for label in labels)
    assert ring.homogeneous_degree(ring.algebra_generator(labels[0]) ** 2) == 2


def test_line_bundle_section_ring_multiplication_and_component_maps() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    bundle = plane.O(1)
    ring = bundle.section_ring()
    degree_one = ring.graded_piece(1)
    degree_two = ring.graded_piece(2)
    first = degree_one.module_generator(next(iter(degree_one.module_generating_set())))
    second = degree_one.module_generator(tuple(degree_one.module_generating_set())[1])
    product = ring.section_multiplication(1, 1)(first, second)
    included_first = ring.homogeneous_component_element(1, first)
    included_second = ring.homogeneous_component_element(1, second)

    assert ring in SectionRings(QQ)
    assert ring.section_scheme() is plane
    assert ring.section_line_bundle() is bundle
    assert product in degree_two
    assert ring.homogeneous_component_map(1).domain() is degree_one
    assert ring.homogeneous_degree(included_first) == 1
    assert ring.homogeneous_degree(included_second) == 1
    assert ring.homogeneous_degree(included_first * included_second) == 2
