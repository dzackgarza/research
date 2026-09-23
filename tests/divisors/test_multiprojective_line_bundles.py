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




