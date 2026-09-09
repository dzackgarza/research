r"""Number-field Vinberg roots retain their actual maximal-order coefficients."""

from sage.rings.algebraic_real import AA as SageAA

from dzack_research.preamble.all import Lattices, QuadraticField
from dzack_research.preamble.categories.hyperbolic_lattices import (
    number_field_vinberg_lattice,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.engine_capabilities import engine_capabilities


def _belolipetsky_lattice():
    field = QuadraticField(5, "s")
    order = field.ring_of_integers()
    s = field.primitive_element()
    phi = (field.one() + s) / field(2)
    gram = (
        (order(2), order(-1), order(0), order(0)),
        (order(-1), order(2), order(-phi), order(0)),
        (order(0), order(-phi), order(2), order(-1)),
        (order(0), order(0), order(-1), order(2)),
    )
    lattice = Lattices(order)(gram)
    real_algebraics = _own_ring(SageAA)
    selected = next(
        embedding
        for embedding in field.embeddings(real_algebraics)
        if embedding(s) > 0
    )
    return lattice, selected


def test_belolipetsky_number_field_vinberg_roots_stay_over_the_maximal_order() -> None:
    r"""Archive engine seam: VinbergsAlgorithmNF raises exact maximal-order roots."""
    assert engine_capabilities.provider_names(
        "number_field_vinberg_root_enumeration"
    ) == ("VinbergsAlgorithmNF-via-sage-julia-bridge",)

    lattice, selected = _belolipetsky_lattice()
    vinberg = number_field_vinberg_lattice(lattice, selected)

    assert vinberg.lattice() is lattice
    assert vinberg.real_embedding() == selected
    assert vinberg.signature_at_selected_place() == (3, 1)
    assert all(signature == (4, 0) for signature in vinberg.other_signatures())

    complete, roots = vinberg.vinberg_simple_roots(count=4)
    assert complete
    assert len(roots) == 4
    assert all(root.parent() is lattice for root in roots)
    assert all(root.q() > 0 for root in roots)

    field = lattice.base_ring().fraction_field()
    s = field.primitive_element()
    expected = (
        lattice((-1, 0, 0, 0)),
        lattice((0, -1, 0, 0)),
        lattice((0, 0, -1, 0)),
        lattice(
            (
                lattice.base_ring()((s + 3) / 2),
                lattice.base_ring()(s + 3),
                lattice.base_ring()(3 * (s + 1) / 2),
                lattice.base_ring()((s - 1) / 2),
            )
        ),
    )
    assert roots == expected
