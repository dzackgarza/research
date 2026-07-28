"""Cross-module certificate composition checks."""

from sage.all import QQ, ProjectiveSpace


def test_picard_cycle_linking_linear_system_and_cyclic_cover():
    """A cycle through line bundles, sections, and cyclic covers is internally consistent."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    L = X.O(4, 4)
    M = X.O(2, 2)
    section_bundle = L.H(0)
    section = section_bundle.basis()[0] + section_bundle.basis()[1]
    system = L.complete_linear_system()
    cover = M.cyclic_cover(section, 2)

    assert section_bundle.dimension() == 25
    assert system.base_locus().defining_ideal().is_one()
    assert cover.domain().dimension() == X.dimension()
    assert cover.ramification_subscheme().dimension() == 1
