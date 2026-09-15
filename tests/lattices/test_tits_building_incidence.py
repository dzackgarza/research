r"""Exact line/plane incidence in the Enriques lattice quotient building."""

from dzack_research.preamble.all import NamedLattices


def _same_subobject(left, right) -> bool:
    try:
        left.inclusion().factor_through(right.inclusion())
        right.inclusion().factor_through(left.inclusion())
    except ValueError:
        return False
    return True


def test_enriques_line_plane_incidence_retains_flags_and_transporters() -> None:
    lattice = NamedLattices.TEn
    incidences = lattice.tits_building_incidence()

    assert incidences.cardinality() > 0
    for incidence in incidences:
        line = incidence.line()
        plane = incidence.plane()
        assert line.module_rank() == 1
        assert plane.module_rank() == 2
        line.inclusion().factor_through(plane.inclusion())
        assert line in incidence.line_cusp()
        assert plane in incidence.plane_cusp()

        moved_line = incidence.line_transporter().transport_isotropic_object(line)
        moved_plane = incidence.plane_transporter().transport_isotropic_object(plane)
        assert _same_subobject(moved_line, incidence.line_cusp().representative())
        assert _same_subobject(moved_plane, incidence.plane_cusp().representative())


def test_incidence_stabilizers_fix_both_terms_of_the_flag() -> None:
    for incidence in NamedLattices.TEn.tits_building_incidence():
        assert incidence.stabilizer_generators().cardinality() > 0
        for isometry in incidence.stabilizer_generators():
            moved_line = isometry.transport_isotropic_object(incidence.line())
            moved_plane = isometry.transport_isotropic_object(incidence.plane())
            assert _same_subobject(moved_line, incidence.line())
            assert _same_subobject(moved_plane, incidence.plane())
