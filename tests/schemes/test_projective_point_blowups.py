"""Regular-center projective blowups use their Rees graph and retained transforms."""

from dzack_research.preamble.all import QQ, ProjectiveSpaces


def _blowup_and_cusp():
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    point = plane.point_morphism((1, 1, 1))
    blowup = plane.point_blowup(point)
    ring = plane.O(3).global_sections().homogeneous_coordinate_ring()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    z = ring.algebra_generator("z")
    cusp = plane.closed_subscheme((y - z) ** 2 * z - (x - z) ** 3)
    return plane, point, blowup, cusp


def test_non_toric_point_blowup_retains_rees_graph_blowdown_and_exceptional_divisor() -> None:
    plane, point, blowup, _cusp = _blowup_and_cusp()
    exceptional = blowup.exceptional_divisor()

    assert blowup.blowup_source() is plane
    assert blowup.blowup_point() is point
    assert blowup.blowup_center().inclusion().codomain() is plane
    assert blowup.blowup_morphism().domain() is blowup
    assert blowup.blowup_morphism().codomain() is plane
    assert exceptional.inclusion().codomain() is blowup
    assert blowup.exceptional_line_bundle().scheme() is blowup
    source_picard = blowup.source_picard_group()
    pullback = blowup.picard_pullback_morphism()
    assert pullback(source_picard.hyperplane_class()) == blowup.hyperplane_picard_class()
    assert blowup.picard_intersection_pairing()(
        blowup.exceptional_picard_class(),
        blowup.exceptional_picard_class(),
    ) == -1
    assert tuple(
        blowup.exceptional_line_bundle().multidegree()[label]
        for label in blowup.exceptional_line_bundle().multidegree().index_set()
    ) == (1, -1)


def test_cusp_total_and_strict_transforms_retain_center_multiplicity_and_exceptional_contribution() -> None:
    _plane, _point, blowup, cusp = _blowup_and_cusp()
    inverse_image = blowup.scheme_theoretic_inverse_image(cusp)
    total = blowup.total_transform(cusp)
    strict = blowup.strict_transform(cusp)
    pairing = blowup.picard_intersection_pairing()
    strict_class = blowup.strict_transform_picard_class(cusp)
    exceptional = blowup.exceptional_picard_class()

    assert blowup.curve_multiplicity_at_center(cusp) == 2
    assert inverse_image.inclusion().codomain() is blowup
    assert total.inclusion().codomain() is blowup
    assert strict.inclusion().codomain() is blowup
    assert inverse_image is not total
    assert total is not strict
    assert blowup.total_transform_picard_class(cusp) != strict_class
    assert pairing(strict_class, exceptional) == 2
    assert pairing(strict_class, strict_class) == 5


def test_blowup_canonical_bundle_is_pullback_canonical_plus_exceptional() -> None:
    _plane, _point, blowup, _cusp = _blowup_and_cusp()
    comparison = blowup.canonical_comparison()
    canonical = comparison.domain()
    target = comparison.codomain()

    assert tuple(
        canonical.multidegree()[label] for label in canonical.multidegree().index_set()
    ) == (-2, -1)
    assert tuple(
        blowup.pulled_back_source_canonical_bundle().multidegree()[label]
        for label in blowup.pulled_back_source_canonical_bundle().multidegree().index_set()
    ) == (-3, 0)
    assert blowup.canonical_line_bundle() is canonical
    assert target == blowup.pulled_back_source_canonical_bundle().tensor_product(blowup.exceptional_line_bundle())
    assert blowup.anticanonical_line_bundle().is_ample()
    assert blowup.is_del_pezzo()
    assert blowup.del_pezzo_degree() == 8
