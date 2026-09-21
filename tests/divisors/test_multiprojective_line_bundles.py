r"""Multidegree line bundles retain factor roles and multihomogeneous sections."""

from dzack_research.preamble.all import QQ, ProjectiveSpaces, Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def _quadric_with_named_factors():
    labels = finite_ordered_set(("left", "right"))
    line = ProjectiveSpaces(QQ)(1)
    factors = indexed_family(labels, lambda _label: line)
    return labels, Schemes(QQ).product(factors)


def test_multiprojective_O_retains_exact_factor_multidegree_and_atlas() -> None:
    labels, quadric = _quadric_with_named_factors()
    bundle = quadric.O(1, 2)

    assert bundle.scheme() is quadric
    assert bundle.multidegree().index_set() is labels
    assert bundle.multidegree()["left"] == 1
    assert bundle.multidegree()["right"] == 2
    assert bundle.gluing_datum().scheme() is quadric
    assert bundle.global_sections().module_rank() == 6
    assert bundle.is_ample()
    assert bundle.is_basepoint_free()


def test_multiprojective_tensor_dual_and_canonical_degrees_are_componentwise() -> None:
    labels, quadric = _quadric_with_named_factors()
    bundle = quadric.O(1, 2)
    other = quadric.O(2, 1)
    tensor = bundle.tensor_product(other)
    dual = bundle.dual_sheaf()
    canonical = quadric.canonical_line_bundle()

    assert tuple(tensor.multidegree()[label] for label in labels) == (3, 3)
    assert tuple(dual.multidegree()[label] for label in labels) == (-1, -2)
    assert tuple(canonical.multidegree()[label] for label in labels) == (-2, -2)
    assert tuple(
        quadric.anticanonical_line_bundle().multidegree()[label]
        for label in labels
    ) == (2, 2)


def test_multihomogeneous_section_multiplication_lands_in_sum_multidegree() -> None:
    _labels, quadric = _quadric_with_named_factors()
    left = quadric.O(1, 0)
    right = quadric.O(0, 1)
    target = quadric.O(1, 1)
    multiplication = left.section_multiplication(right)
    left_label = next(iter(left.global_sections().module_generating_set()))
    right_label = next(iter(right.global_sections().module_generating_set()))

    product = multiplication(
        left.global_sections().module_generator(left_label),
        right.global_sections().module_generator(right_label),
    )

    assert multiplication.codomain().section_scheme() is quadric
    assert multiplication.codomain().module_rank() == target.global_sections().module_rank()
    assert product.parent() is multiplication.codomain()
    assert product != multiplication.codomain().zero()


def test_multiprojective_line_bundle_base_change_preserves_multidegree_and_sections() -> None:
    from dzack_research.preamble.all import QuadraticField

    field = QuadraticField(2, "s")
    ring_map = QQ.Mor(field)(lambda element: field(element))
    labels, quadric = _quadric_with_named_factors()
    bundle = quadric.O(1, 2)

    changed = bundle.base_change(ring_map)
    comparison = changed.section_base_change_comparison()

    assert changed.scheme().scheme_base_ring() is field
    assert changed.base_change_source_bundle() is bundle
    assert changed.base_change_projection().codomain() is quadric
    assert tuple(changed.multidegree()[label] for label in labels) == (1, 2)
    assert comparison.forward().domain().module_rank() == 6
    assert comparison.forward().codomain() is changed.global_sections()
    squared = changed.tensor_power(2)
    assert squared.base_change_source_bundle() is bundle.tensor_power(2)
    assert squared.base_change_projection() is squared.scheme().left_projection()
