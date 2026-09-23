"""Restricted multiprojective line bundles retain their exact multidegree."""

from dzack_research.preamble.all import QQ, ProjectiveSpaces
from dzack_research.preamble.categories.schemes.ringed_spaces import QuasiCoherentSheaves

def test_restricted_multiprojective_bundles_tensor_and_compare_by_multidegree() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    line = ProjectiveSpaces(QQ)(1)
    product = plane.scheme_category().product((plane, line))
    sections = product.O(1, 1).global_sections()
    ring = sections.homogeneous_coordinate_ring()
    labels = tuple(ring.algebra_generating_set())
    hypersurface = product.closed_subscheme(
        ring.algebra_generator(labels[0]) * ring.algebra_generator(labels[-1])
    )

    left = product.O(-3, 0).restrict_to(hypersurface)
    exceptional = product.O(1, -1).restrict_to(hypersurface)
    canonical = product.O(-2, -1).restrict_to(hypersurface)
    target = left.tensor_product(exceptional)
    comparison = canonical.canonical_isomorphism_to(target)
    sheaves = QuasiCoherentSheaves(hypersurface)

    assert canonical in QuasiCoherentSheaves(hypersurface).Invertible()
    assert tuple(canonical.multidegree()[label] for label in canonical.multidegree().index_set()) == (-2, -1)
    assert comparison.domain() is canonical
    assert comparison.codomain() is target
    assert comparison in sheaves.Core().Mor(canonical, target)
    assert comparison.forward() in sheaves.Mor(canonical, target)
