"""Multiprojective homogeneous coordinates preserve exact factor roles."""

from dzack_research.preamble.all import ProjectiveSpace, QQ, scheme_product


def test_factor_coordinate_embeddings_keep_repeated_projective_factors_distinct() -> None:
    line = ProjectiveSpace(1, QQ, names=("u", "v"))
    product = scheme_product(line, line)
    sections = product.O(1, 1).global_sections()
    ring = sections.homogeneous_coordinate_ring()
    left = sections.factor_coordinate_embedding(0)
    right = sections.factor_coordinate_embedding(1)
    factor_ring = line.O(1).global_sections().homogeneous_coordinate_ring()
    u = factor_ring.algebra_generator("u")

    assert left.domain() is factor_ring
    assert right.domain() is factor_ring
    assert left.codomain() is ring
    assert right.codomain() is ring
    assert left(u) != right(u)
