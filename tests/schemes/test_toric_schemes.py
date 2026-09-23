r"""Toric varieties of fans and of lattice polytopes.

Values are Cox--Little--Schenck, *Toric Varieties*: the smoothness and
completeness criteria are Thm. 3.1.19 and Thm. 3.4.1, the orbit-cone
correspondence is Thm. 3.2.6, the affine chart of a cone is Prop. 1.3.9, the
three generators of the ``A_1`` chart are Example 1.2.22, and the face
localization is Prop. 1.3.16.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AffineSchemes,
    IntegralSchemes,
    LatticePolygons,
    NormalSchemes,
    OpenImmersions,
    RationalPolyhedralFans,
    Schemes,
    SmoothSchemes,
    Surfaces,
    ToricSchemes,
    Varieties,
)

# One rank-two cocharacter lattice for the whole file: a free module is a
# fresh object on every construction, so building it twice would give two
# unrelated categories of fans.
_PLANE_FANS = RationalPolyhedralFans(ZZ.free_module(2))


def _plane_fans():
    return _PLANE_FANS


def test_the_projective_plane_of_its_fan_is_a_smooth_complete_toric_surface() -> None:
    plane = _plane_fans().projective_space_fan().toric_variety(QQ)

    assert plane in Schemes(QQ)
    assert plane in ToricSchemes(QQ)
    assert plane in Varieties(QQ)
    assert plane in Surfaces(QQ)
    assert plane in NormalSchemes(QQ)
    assert plane in SmoothSchemes(QQ)
    assert plane in IntegralSchemes(QQ)
    assert plane.dimension() == 2
    assert plane.is_smooth()
    assert plane.is_complete()
    assert plane.is_normal()


def test_a_toric_variety_carries_its_fan_and_the_two_torus_lattices() -> None:
    fans = _plane_fans()
    plane = fans.projective_space_fan().toric_variety(QQ)

    assert plane.fan() is fans.projective_space_fan()
    assert plane.cocharacter_lattice() is fans.cocharacter_lattice()
    assert plane.character_lattice() is fans.character_lattice()
    assert plane.character_cocharacter_pairing() is fans.character_cocharacter_pairing()


def test_the_dense_torus_is_the_toric_variety_of_the_zero_cone() -> None:
    plane = _plane_fans().projective_space_fan().toric_variety(QQ)
    torus = plane.torus()

    assert torus in ToricSchemes(QQ)
    assert torus.dimension() == 2
    assert not torus.is_complete()
    assert torus.fan().cardinality() == 1


def test_the_orbit_cone_correspondence_counts_the_orbits_of_each_dimension() -> None:
    r"""CLS Thm. 3.2.6: cones of dimension ``k`` index orbits of dimension
    ``n - k``, so ``P^2`` has one dense orbit, three one-dimensional orbits and
    three fixed points."""
    plane = _plane_fans().projective_space_fan().toric_variety(QQ)

    assert plane.torus_orbits(2).cardinality() == 1
    assert plane.torus_orbits(1).cardinality() == 3
    assert plane.torus_orbits(0).cardinality() == 3


def test_the_chart_of_a_smooth_cone_is_the_affine_plane() -> None:
    fans = _plane_fans()
    variety = fans((((1, 0), (0, 1)), ((1, 0), (0, -1)))).toric_variety(QQ)
    cone = variety.fan().maximal_cones()[0]
    chart = variety.affine_chart(cone)

    assert chart in AffineSchemes(QQ)
    assert chart.coordinate_algebra().algebra_generating_set().cardinality() == 2


def test_the_chart_of_the_a_one_cone_is_the_quadric_cone() -> None:
    r"""CLS Example 1.2.22: ``S_sigma`` needs three characters with one
    relation, so the chart is a hypersurface in three variables rather than an
    affine plane."""
    fans = _plane_fans()
    variety = fans((((0, 1), (2, -1)),)).toric_variety(QQ)
    cone = variety.fan().maximal_cones()[0]
    chart = variety.affine_chart(cone)

    assert chart in AffineSchemes(QQ)
    assert chart.coordinate_algebra().algebra_generating_set().cardinality() == 3
    assert not variety.is_smooth()


def test_a_face_of_a_cone_localizes_the_chart_at_one_monomial() -> None:
    r"""CLS Prop. 1.3.16: for ``tau`` a face of ``sigma`` the chart of ``tau``
    is the distinguished open of the chart of ``sigma`` where the supporting
    character is invertible."""
    variety = _plane_fans().projective_space_fan().toric_variety(QQ)
    cone = variety.fan().maximal_cones()[0]
    face = cone.faces(1)[0]
    chart = variety.affine_chart(cone)
    localized = variety.face_localization(face, cone)

    assert localized in OpenImmersions(chart)
    assert localized in AffineSchemes(QQ)


def test_a_general_hypersurface_of_a_toric_chart_is_only_an_ordinary_closed_subscheme() -> None:
    variety = _plane_fans().projective_space_fan().toric_variety(QQ)
    cone = variety.fan().maximal_cones()[0]
    chart = variety.affine_chart(cone)
    algebra = chart.coordinate_algebra()
    first, second = tuple(algebra.algebra_generating_set())
    hypersurface = chart.closed_subscheme(
        algebra.algebra_generator(first) + algebra.algebra_generator(second)
    )

    assert hypersurface in Schemes(QQ)
    assert hypersurface not in ToricSchemes(QQ)


def test_the_standard_identifications_are_decided_by_fan_isomorphism() -> None:
    fans = _plane_fans()
    plane = fans.projective_space_fan().toric_variety(QQ)
    first_hirzebruch = fans.hirzebruch_surface_fan(1).toric_variety(QQ)

    assert plane.is_projective_space()
    assert plane.is_weighted_projective_space((1, 1, 1))
    assert not plane.is_hirzebruch_surface(1)
    assert first_hirzebruch.is_hirzebruch_surface(1)
    assert not first_hirzebruch.is_projective_space()
    assert not plane.is_isomorphic_to(first_hirzebruch)
    assert plane.is_isomorphic_to(fans.projective_space_fan().toric_variety(QQ))


def test_the_normal_fan_of_a_polytope_uses_inner_normals() -> None:
    r"""The facet ``x + 2y = 2`` of ``conv{(0,0),(2,0),(0,1)}`` has inner
    normal ``-e_1 - 2 e_2``; the outer normal ``e_1 + 2 e_2`` is not a ray of
    the normal fan."""
    lattice = ZZ.free_module(2)
    polygon = LatticePolygons(lattice)(((0, 0), (2, 0), (0, 1)))
    fan = polygon.normal_fan()
    cocharacters = fan.cocharacter_lattice()
    first, second = tuple(cocharacters.module_generating_set())
    inner = cocharacters.linear_combination({first: ZZ(-1), second: ZZ(-2)})
    outer = cocharacters.linear_combination({first: ZZ(1), second: ZZ(2)})

    assert fan.rays().cardinality() == 3
    assert inner in fan.rays()
    assert outer not in fan.rays()


def test_the_toric_variety_of_the_standard_triangle_is_the_projective_plane() -> None:
    r"""The normal fan of ``conv{(0,0),(1,0),(0,1)}`` has rays ``e_1``, ``e_2``
    and ``-e_1-e_2``, which is the fan of ``P^2``."""
    lattice = ZZ.free_module(2)
    triangle = LatticePolygons(lattice)(((0, 0), (1, 0), (0, 1)))
    variety = triangle.toric_variety(QQ)

    assert variety in ToricSchemes(QQ)
    assert variety.is_projective_space()
    assert variety.is_polarized()
    assert variety.polarizing_polytope() is triangle


def test_a_variety_built_from_a_bare_fan_carries_no_polarizing_polytope() -> None:
    variety = _plane_fans().projective_space_fan().toric_variety(QQ)

    assert not variety.is_polarized()


def test_a_fan_compatible_lattice_map_induces_a_toric_morphism() -> None:
    r"""CLS Thm. 3.3.4: the identity of ``N`` is compatible with any fan and
    with itself, and doubling every cocharacter carries the fan of ``P^2``
    into itself."""

    fans = _plane_fans()
    fan = fans.projective_space_fan()
    cocharacters = fans.cocharacter_lattice()
    identity = cocharacters.module_category().Mor(cocharacters, cocharacters).identity()

    assert fan.is_compatible_with(identity, fan)

    variety = fan.toric_variety(QQ)
    morphism = variety.toric_morphism(identity, variety)
    assert morphism.domain() is variety
    assert morphism.codomain() is variety


def test_a_nonidentity_toric_morphism_retains_its_chart_pullback() -> None:
    r"""On ``P^1``, doubling ``N`` induces ``chi^m |-> chi^(2m)`` on a chart."""

    fans = RationalPolyhedralFans(ZZ.free_module(1))
    fan = fans.projective_space_fan()
    cocharacters = fans.cocharacter_lattice()
    label = next(iter(cocharacters.module_generating_set()))
    doubling = cocharacters.module_category().Mor(cocharacters, cocharacters)(
        {
            label: ZZ(2) * cocharacters.module_generator(label),
        }
    )
    variety = fan.toric_variety(QQ)
    morphism = variety.toric_morphism(doubling, variety)
    source_cone = fan.maximal_cones()[0]
    target_cone = morphism.chart_target(source_cone)
    source_algebra = variety.affine_chart(source_cone).coordinate_algebra()
    target_algebra = variety.affine_chart(target_cone).coordinate_algebra()
    source_generator = source_algebra.algebra_generator(
        next(iter(source_algebra.algebra_generating_set()))
    )
    target_generator = target_algebra.algebra_generator(
        next(iter(target_algebra.algebra_generating_set()))
    )

    assert morphism.lattice_morphism() is doubling
    assert morphism.chart_pullback(source_cone)(target_generator) == source_generator**2
    assert morphism.chart_morphism(source_cone).domain() is variety.affine_chart(source_cone)
    assert morphism.chart_morphism(source_cone).codomain() is variety.affine_chart(target_cone)


def test_an_incompatible_lattice_map_is_refused_rather_than_forced() -> None:
    r"""The fan of ``P^1`` in a rank-one lattice is not carried into the fan of
    the affine line by the identity: the ray ``-e_1`` lies in no cone."""
    line_fans = RationalPolyhedralFans(ZZ.free_module(1))

    projective_line = line_fans.projective_space_fan()
    affine_line = line_fans((((1,),),))
    cocharacters = line_fans.cocharacter_lattice()
    identity = cocharacters.module_category().Mor(cocharacters, cocharacters).identity()

    assert not projective_line.is_compatible_with(identity, affine_line)
    assert affine_line.is_compatible_with(identity, projective_line)
