r"""Owned toric weight complexes and their induced maps."""

from dzack_research.preamble.all import QQ, ZZ, RationalPolyhedralFans


def _projective_plane():
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    return fans.projective_space_fan().toric_variety(QQ)


def test_scalar_two_acts_on_the_actual_nonzero_weight_class() -> None:
    plane = _projective_plane()
    divisor = plane.canonical_divisor()
    weight = plane.character_lattice().zero()
    cohomology = plane.weight_cohomology(divisor, weight, 2)

    assert cohomology.dimension() == 1
    cycle_module = cohomology.cochain_complex().graded_piece(2)
    label = next(iter(cycle_module.module_generating_set()))
    cycle = cycle_module.module_generator(label)
    class_ = cohomology.class_of_cycle(cycle)
    assert class_.parent() is cohomology
    assert cohomology.cycle_representative(class_).parent() is cycle_module
    assert class_ != cohomology.zero()

    cochain_map = plane.weight_scalar_cochain_map(divisor, weight, QQ(2))
    induced = plane.weight_scalar_cohomology_map(divisor, weight, 2, QQ(2))

    assert cochain_map.component(2)(cycle) == QQ(2) * cycle
    scaled = QQ(2) * class_
    assert scaled.parent() is cohomology
    assert induced(class_) == scaled
    assert induced(class_).parent() is cohomology


def test_nonzero_weight_piece_includes_into_total_cohomology() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    total = plane.line_bundle_cohomology(divisor, 0)
    weight = next(iter(total.cohomology_weight_support()))
    piece = total.cohomology_weight_piece(weight)
    inclusion = total.cohomology_weight_inclusion(weight)
    projection = total.cohomology_weight_projection(weight)
    cycle_module = piece.cochain_complex().graded_piece(0)
    label = next(iter(cycle_module.module_generating_set()))
    class_ = piece.class_of_cycle(cycle_module.module_generator(label))
    included = inclusion(class_)
    doubled_in_total = QQ(2) * included
    projected = projection(included)
    projected_doubled = projection(doubled_in_total)

    assert class_.parent() is piece
    assert included.parent() is total
    assert doubled_in_total.parent() is total
    assert projected.parent() is piece
    assert projected_doubled.parent() is piece
    assert inclusion.domain() is piece
    assert inclusion.codomain() is total
    assert projection.domain() is total
    assert projection.codomain() is piece
    assert included != total.zero()
    assert projected == class_
    assert projected_doubled == QQ(2) * class_


def test_zero_support_and_boundary_degree_keep_the_geometric_complex() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    characters = plane.character_lattice()
    first = next(iter(characters.module_generating_set()))
    outside = ZZ(4) * characters.module_generator(first)
    zero_piece = plane.weight_cohomology(divisor, outside, 0)

    assert zero_piece.dimension() == 0
    complex_ = zero_piece.cochain_complex()
    assert complex_.cohomology_scheme() is plane
    assert complex_.toric_weight_cohomology_construction().scheme() is plane
    assert complex_.cohomology_divisor() == divisor
    assert complex_.cohomology_weight() == outside
    assert "_preamble_geometric_cohomology_scheme" not in complex_.__dict__
    assert "_preamble_geometric_cohomology_divisor" not in complex_.__dict__
    assert "_preamble_geometric_cohomology_weight" not in complex_.__dict__
