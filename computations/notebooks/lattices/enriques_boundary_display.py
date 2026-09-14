"""Research display: Enriques boundary cusps and their reduction diagrams.

This is deliberately a consumer of live mathematical objects.  It does not
install a display hook and it contains no Coxeter/TikZ implementation of its
own.  The research question is the incidence of rank-one and rank-two cusps of
the Enriques anti-invariant lattice and the reflection geometry of each
rank-one cusp reduction.

Execution is intentionally left to terminal/session verification.  The
reflection-diagram calls require the configured exact Vinberg/reflection
provider; bounded searches are not interpreted here as complete diagrams.
"""

from dzack_research.preamble.catalogue import NamedLattices
from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
from dzack_research.preamble.categories.isotropic_orbits import (
    cusps,
    tits_building_incidence,
)


def enriques_boundary_incidence():
    """Return the live rank-(1,2) quotient-building incidence records."""
    return tits_building_incidence(NamedLattices.TEn)


def enriques_line_cusp_diagrams():
    """Return the live Coxeter diagrams of the rank-one cusp reductions."""
    lattice = NamedLattices.TEn
    diagrams = []
    for cusp in cusps(lattice, 1):
        reduction = cusp.reduction_lattice()
        hyperbolic_reduction = HyperbolicLattices(reduction.base_ring())(reduction)
        diagrams.append((cusp, hyperbolic_reduction.reflection_coxeter_diagram()))
    return tuple(diagrams)


def enriques_line_cusp_tikz():
    """Return TikZ views supplied by the existing Coxeter-diagram owner."""
    return tuple(
        (cusp, diagram.tikz_picture())
        for cusp, diagram in enriques_line_cusp_diagrams()
    )


def display_enriques_boundary() -> None:
    """Print the incidence records and Coxeter TikZ source for notebook use."""
    print("Enriques line/plane cusp incidence:")
    for incidence in enriques_boundary_incidence():
        print(incidence)
    print("\nRank-one cusp reduction Coxeter diagrams:")
    for cusp, tikz in enriques_line_cusp_tikz():
        print(cusp)
        print(tikz)
        print()


if __name__ == "__main__":
    display_enriques_boundary()
