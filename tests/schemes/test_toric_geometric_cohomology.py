r"""Owned toric weight complexes and their induced maps."""

from dzack_research.preamble.all import BasedFreeModule, QQ, RationalPolyhedralFans, ZZ
from dzack_research.preamble.categories.schemes.geometric_cohomology import (
    ToricLineBundleCohomology,
    ToricWeightCohomology,
    ToricWeightScalarCochainMap,
    ToricWeightScalarCohomologyMap,
)


def _projective_plane():
    fans = RationalPolyhedralFans(BasedFreeModule(ZZ, 2))
    return fans.projective_space_fan().toric_variety(QQ)


def test_scalar_two_acts_on_the_actual_nonzero_weight_class() -> None:
    plane = _projective_plane()
    divisor = plane.canonical_divisor()
    weight = plane.character_lattice().zero()
    cohomology = ToricWeightCohomology(plane, divisor, weight, 2)

    assert cohomology.dimension() == 1
    cycle_module = cohomology.cochain_complex().graded_piece(2)
    label = next(iter(cycle_module.module_generating_set()))
    cycle = cycle_module.module_generator(label)
    class_ = cohomology.class_of_cycle(cycle)
    assert class_ != cohomology.zero()

    cochain_map = ToricWeightScalarCochainMap(plane, divisor, weight, QQ(2))
    induced = ToricWeightScalarCohomologyMap(plane, divisor, weight, 2, QQ(2))

    assert cochain_map.component(2)(cycle) == QQ(2) * cycle
    assert induced(class_) == QQ(2) * class_


def test_nonzero_weight_piece_includes_into_total_cohomology() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    total = ToricLineBundleCohomology(plane, divisor, 0)
    weight = next(iter(total.cohomology_weight_support()))
    piece = total.cohomology_weight_piece(weight)
    inclusion = total.cohomology_weight_inclusion(weight)
    projection = total.cohomology_weight_projection(weight)
    cycle_module = piece.cochain_complex().graded_piece(0)
    label = next(iter(cycle_module.module_generating_set()))
    class_ = piece.class_of_cycle(cycle_module.module_generator(label))

    assert inclusion.domain() is piece
    assert inclusion.codomain() is total
    assert projection.domain() is total
    assert projection.codomain() is piece
    assert inclusion(class_) != total.zero()
    assert projection(inclusion(class_)) == class_


def test_zero_support_and_boundary_degree_keep_the_geometric_complex() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    characters = plane.character_lattice()
    first = next(iter(characters.module_generating_set()))
    outside = ZZ(4) * characters.module_generator(first)
    zero_piece = ToricWeightCohomology(plane, divisor, outside, 0)

    assert zero_piece.dimension() == 0
    assert zero_piece.cochain_complex().cohomology_scheme() is plane
    assert zero_piece.cochain_complex().cohomology_divisor() == divisor
    assert zero_piece.cochain_complex().cohomology_weight() == outside
