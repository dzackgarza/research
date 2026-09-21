r"""Archive reconciliation for the integral-lattice mathematical surface.

The archived monolith is now split among the common lattice, lattice-morphism,
definite-lattice, discriminant-form, and group-action owners.  The central
metric-dual/discriminant chain remains one live construction rather than a
parallel archive API.
"""

from dzack_research.preamble.all import ZZ, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/integrallattice/integral_lattices.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattices.py",
    "owner_overrides": {
        "IntegralLattices.ParentMethods.minimum": "src/dzack_research/preamble/categories/definite_lattices.py",
        "IntegralLattices.ParentMethods.enumerate_short_vectors": "src/dzack_research/preamble/categories/definite_lattices.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_metric_dual_discriminant_chain_is_the_live_owned_chain() -> None:
    lattice = Lattices(ZZ)("A2")
    dual = lattice.dual_lattice()
    correlation = lattice.correlation_morphism()
    discriminant = lattice.discriminant_module()
    projection = lattice.discriminant_projection()
    generator = lattice.basis_vector(0)
    dual_image = correlation(generator)
    discriminant_class = projection(dual_image)

    assert correlation.domain() is lattice
    assert correlation.codomain() is dual
    assert dual_image.parent() is dual
    assert projection.domain() is dual
    assert projection.codomain() is discriminant
    assert discriminant_class.parent() is discriminant
    assert discriminant_class == lattice.discriminant_class(generator)
    assert discriminant.cardinality() == abs(lattice.gram_matrix().determinant())
