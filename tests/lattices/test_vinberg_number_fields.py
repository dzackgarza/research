r"""Number-field Vinberg roots retain their actual maximal-order coefficients."""

from sage.rings.qqbar import AA as SageAA

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
    selected = None
    for embedding in field.embeddings(real_algebraics):
        try:
            number_field_vinberg_lattice(lattice, embedding)
        except ValueError:
            continue
        assert selected is None, "the Vinberg signature conditions select one real place"
        selected = embedding
    assert selected is not None, "the Vinberg signature conditions select a real place"
    return lattice, selected


def test_belolipetsky_number_field_vinberg_roots_stay_over_the_maximal_order() -> None:
    r"""Archive engine seam: VinbergsAlgorithmNF raises exact maximal-order roots."""
    providers = engine_capabilities.provider_names("number_field_vinberg_root_enumeration")
    assert providers[0] == "VinbergsAlgorithmNF-via-sage-julia-bridge"
    assert not providers[1:]

    lattice, selected = _belolipetsky_lattice()
    vinberg = number_field_vinberg_lattice(lattice, selected)

    assert vinberg.lattice() is lattice
    assert vinberg.real_embedding() == selected
    selected_signature = vinberg.signature_at_selected_place()
    assert selected_signature.first() == 3
    assert selected_signature.second() == 1
    assert all(
        signature.first() == 4 and signature.second() == 0
        for signature in vinberg.other_signatures()
    )

    complete, roots = vinberg.vinberg_simple_roots(count=4)
    assert complete
    assert roots.cardinality() == 4
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
    assert all(root == expected[position] for position, root in enumerate(roots))
