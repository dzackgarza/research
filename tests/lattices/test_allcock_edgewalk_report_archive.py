r"""Archive reconciliation for Allcock fundamental-domain report data."""

from dzack_research.preamble.all import HyperbolicLattices, Lattices, ZZ
from dzack_research.preamble.categories.hyperbolic_lattices import (
    AllcockEdgewalkReport,
)


def test_edgewalk_report_retains_vertices_walls_and_polyhedron_isometries(monkeypatch) -> None:
    lattice = HyperbolicLattices(ZZ)(Lattices(ZZ)([[1, 0, 0], [0, -1, 0], [0, 0, -1]]))
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    record = {
        "simple_root_rows": ((0, 1, -1),),
        "vertices": (((1, 1, 0), ((0, 1, -1),)),),
        "is_reflective": True,
        "isometry_generator_rows": (identity,),
    }

    def edgewalk_record(capability, _gram):
        assert capability == "lorentzian_edgewalk_fundamental_domain"
        return record

    monkeypatch.setattr(
        "dzack_research.preamble.categories.hyperbolic_lattices.engine_capabilities.compute",
        edgewalk_record,
    )

    report = lattice.allcock_edgewalk()

    assert isinstance(report, AllcockEdgewalkReport)
    assert report.lattice() is lattice
    assert report.is_reflective() is True
    assert report.simple_roots() is lattice.edgewalk_simple_roots()
    assert report.vertices().cardinality() == 1
    vertex = report.vertices()[0]
    assert vertex.lattice() is lattice
    assert vertex.square() == 0
    assert vertex.is_ideal()
    assert tuple(vertex.incident_roots()) == tuple(report.simple_roots())
    assert report.polyhedron_isometry_generators().cardinality() == 1
    assert report.polyhedron_isometry_group().supergroup() is lattice.O()
