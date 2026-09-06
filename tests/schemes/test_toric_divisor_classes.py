r"""Class group, Cartier divisors and divisor polytopes of a toric variety.

Values are Cox--Little--Schenck, *Toric Varieties*: the exact sequence
``M -> Div_T(X) -> Cl(X) -> 0`` is Thm. 4.1.3, the Cartier criterion is
Thm. 4.2.8, ``Pic = Cl`` on a smooth fan is Prop. 4.2.6, the polytope of a
divisor is (4.3.2) and its lattice points are a basis of the global sections
by Prop. 4.3.3.
"""

import pytest

from dzack_research.preamble.all import (
    BasedFreeModule,
    ClassGroups,
    PicardGroups,
    QQ,
    RationalPolyhedralFans,
    ZZ,
)

# One rank-two cocharacter lattice for the whole file: a free module is a
# fresh object on every construction, so building it twice would give two
# unrelated categories of fans.
_PLANE_FANS = RationalPolyhedralFans(BasedFreeModule(ZZ, 2))


def _projective_plane():
    return _PLANE_FANS.projective_space_fan().toric_variety(QQ)


def _quadric_cone():
    r"""``U_sigma`` for ``sigma = Cone((1,0),(1,2))``: the ``A_1`` surface singularity."""
    return _PLANE_FANS((((1, 0), (1, 2)),)).toric_variety(QQ)


def _prime_divisors(variety):
    return tuple(
        variety.torus_invariant_prime_divisor(ray) for ray in variety.fan().cones(1)
    )


def test_the_three_lines_of_the_projective_plane_share_one_divisor_class() -> None:
    r"""``div(chi^{e_1^*}) = D_1 - D_0`` on the fan of ``P^2``, so the three
    torus-invariant lines are linearly equivalent and generate ``Cl(P^2)``."""
    plane = _projective_plane()
    classes = plane.class_group()
    first, second, third = (plane.divisor_class(D) for D in _prime_divisors(plane))

    assert classes in ClassGroups()
    assert first == second
    assert second == third
    assert first != classes.zero()


def test_the_principal_divisor_of_every_character_is_trivial_in_the_class_group() -> None:
    plane = _projective_plane()
    characters = plane.character_lattice()
    principal = plane.character_divisor_morphism()
    classes = plane.class_group()

    for label in characters.module_generating_set():
        character = characters.module_generator(label)
        assert plane.divisor_class(principal(character)) == classes.zero()


def test_the_anticanonical_class_of_the_projective_plane_is_three_times_a_line() -> None:
    plane = _projective_plane()
    line = plane.divisor_class(_prime_divisors(plane)[0])

    assert plane.divisor_class(plane.toric_boundary_divisor()) == ZZ(3) * line
    assert plane.divisor_class(plane.canonical_divisor()) == ZZ(-3) * line


def test_only_a_fan_whose_rays_span_the_lattice_is_free_of_a_torus_factor() -> None:
    r"""``A^1 x k^*`` is the toric variety of the single ray ``e_1`` in ``ZZ^2``."""
    plane = _projective_plane()
    half_plane = _PLANE_FANS((((1, 0),),)).toric_variety(QQ)

    assert not plane.has_torus_factor()
    assert half_plane.has_torus_factor()


def test_a_ruling_of_the_quadric_cone_is_weil_but_not_cartier() -> None:
    r"""On ``sigma = Cone((1,0),(1,2))`` a character with ``<m,u_1> = -1`` and
    ``<m,u_2> = 0`` would need second coordinate ``1/2``, so ``D_1`` is not
    Cartier while ``2 D_1`` is."""
    cone_surface = _quadric_cone()
    ruling = _prime_divisors(cone_surface)[0]

    assert not cone_surface.is_cartier(ruling)
    assert cone_surface.is_cartier(ZZ(2) * ruling)
    assert cone_surface.is_cartier(cone_surface.toric_boundary_divisor())


def test_every_torus_invariant_divisor_on_a_smooth_toric_surface_is_cartier() -> None:
    plane = _projective_plane()

    for divisor in _prime_divisors(plane):
        assert plane.is_cartier(divisor)
    assert plane.is_cartier(plane.canonical_divisor())


def test_the_picard_group_is_constructed_on_a_smooth_fan_and_refused_otherwise() -> None:
    assert _projective_plane().picard_group() in PicardGroups()

    with pytest.raises(AssertionError):
        _quadric_cone().picard_group()


def test_the_sections_of_a_line_on_the_projective_plane_are_the_three_linear_forms() -> None:
    r"""``h^0(P^2, O(1)) = 3`` and ``h^0(P^2, O(3)) = 10``: the polytope of a
    single torus-invariant line is a unimodular triangle and the polytope of
    the boundary is its third dilate."""
    plane = _projective_plane()
    characters = plane.character_lattice()

    for divisor in _prime_divisors(plane):
        assert plane.divisor_polytope(divisor).n_integral_points() == 3
        assert plane.divisor_section_characters(divisor).cardinality() == 3

    boundary = plane.toric_boundary_divisor()
    assert plane.divisor_polytope(boundary).n_integral_points() == 10
    assert characters.zero() in plane.divisor_section_characters(boundary)


def test_the_polytope_of_an_ample_divisor_has_the_fan_as_its_normal_fan() -> None:
    r"""``O(1)`` on ``P^2`` is ample, and by CLS Thm. 6.2.1 the normal fan of the
    polytope of an ample divisor on a complete toric variety is the fan itself.
    Each torus-invariant line of ``P^2`` is a unimodular triangle's divisor."""
    plane = _projective_plane()

    for divisor in _prime_divisors(plane):
        polytope = plane.divisor_polytope(divisor)
        assert polytope.n_vertices() == 3
        assert polytope.normal_fan().is_isomorphic(plane.fan())
