from dzack_research.preamble.all import (
    BasedFreeModule,
    QQ,
    RationalPolyhedralFans,
    ToricFixedPointBlowup,
    ToricFixedPointBlowups,
    ZZ,
)


def _projective_plane():
    fans = RationalPolyhedralFans(BasedFreeModule(ZZ, 2))
    return fans.projective_space_fan().toric_variety(QQ)


def test_blowup_of_a_torus_fixed_point_of_p2_is_the_star_subdivision_with_blowdown() -> None:
    plane = _projective_plane()
    center = plane.fan().maximal_cones()[0]

    blowup = ToricFixedPointBlowup(plane, center)

    assert blowup in ToricFixedPointBlowups(QQ)
    assert blowup.blowup_source() is plane
    assert blowup.blowup_center_cone() is center
    assert blowup.blowup_morphism().domain() is blowup
    assert blowup.blowup_morphism().codomain() is plane
    assert blowup.fan().is_smooth()
    assert blowup.fan().is_complete()
    assert blowup.fan().cones(1).cardinality() == plane.fan().cones(1).cardinality() + 1


def test_exceptional_curve_has_self_intersection_minus_one_and_picard_rank_increases() -> None:
    plane = _projective_plane()
    blowup = ToricFixedPointBlowup(plane, plane.fan().maximal_cones()[0])

    exceptional = blowup.exceptional_divisor()

    assert blowup.exceptional_self_intersection() == -1
    assert blowup.weil_multiplicity(exceptional, blowup.exceptional_ray()) == 1
    assert int(blowup.picard_group().module_rank()) == int(plane.picard_group().module_rank()) + 1
