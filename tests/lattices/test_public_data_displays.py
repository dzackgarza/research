from dzack_research.preamble.categories.arithmetic_applications import LorentzianE10Application


def test_lorentzian_application_display_exposes_its_lattice_and_cusp() -> None:
    application = LorentzianE10Application()
    shown = repr(application)

    assert "Lorentzian E10 cusp application" in shown
    assert str(application.lattice()) in shown
    assert str(application.cusp()) in shown
    assert "object at 0x" not in shown
