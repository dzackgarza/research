r"""Finite-index splitting of the isotropic Tits building with live transporters."""

from dzack_research.preamble.all import NamedLattices, Sets


def _same_subobject(left, right) -> bool:
    try:
        left.inclusion().factor_through(right.inclusion())
        right.inclusion().factor_through(left.inclusion())
    except ValueError:
        return False
    return True


def _image_subobject(isometry, subobject):
    return (isometry * subobject.inclusion()).image()


def test_stable_orthogonal_group_has_owned_line_plane_and_flag_orbits() -> None:
    r"""The discriminant kernel splits the quotient building with Gamma-maps.

    ``U + U(2)`` has Witt index two and nontrivial discriminant module, so its
    stable orthogonal group is a genuine discriminant-preimage subgroup rather
    than the vacuous unimodular case.
    """
    lattice = NamedLattices.U + NamedLattices.U_2
    subgroup = lattice.stable_orthogonal_group()

    assert subgroup.character_data_is_complete()
    assert subgroup.contains_character_kernel()

    line_cusps = subgroup.cusps(1)
    plane_cusps = subgroup.cusps(2)
    incidences = subgroup.tits_building_incidence()

    assert line_cusps.cardinality() > 0
    assert plane_cusps.cardinality() > 0
    assert incidences.cardinality() > 0

    for cusp_family in (line_cusps, plane_cusps):
        for cusp in cusp_family:
            assert cusp in Sets()
            assert cusp.subgroup() is subgroup
            assert cusp.representative() in cusp
            stabilizer = cusp.stabilizer()
            assert stabilizer.supergroup() is subgroup
            assert stabilizer.one() in stabilizer

    for incidence in incidences:
        line = incidence.line()
        plane = incidence.plane()
        line.inclusion().factor_through(plane.inclusion())

        assert incidence.subgroup() is subgroup
        assert incidence.line_cusp().subgroup() is subgroup
        assert incidence.plane_cusp().subgroup() is subgroup
        assert line in incidence.line_cusp()
        assert plane in incidence.plane_cusp()

        line_transporter = incidence.line_transporter()
        plane_transporter = incidence.plane_transporter()
        assert line_transporter in subgroup
        assert plane_transporter in subgroup
        assert _same_subobject(
            _image_subobject(line_transporter, line),
            incidence.line_cusp().representative(),
        )
        assert _same_subobject(
            _image_subobject(plane_transporter, plane),
            incidence.plane_cusp().representative(),
        )

        stabilizer = incidence.stabilizer()
        assert stabilizer.supergroup() is subgroup
        assert stabilizer.one() in stabilizer
