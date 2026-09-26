r"""Structured fixed-Mor arrow implementations follow the semantic Mor graph."""

from dzack_research.preamble.all import *


def test_lattice_mor_arrow_type_inherits_module_mor_arrow_type() -> None:
    lattice = NamedLattices.U
    lattice_mor = lattice.Mor(lattice)
    module_mor = lattice.module_category().Mor(lattice, lattice)

    assert issubclass(lattice_mor.ElementType, module_mor.ElementType)
    assert lattice_mor.element_class is lattice_mor.ElementType
