r"""Archive reconciliation for the public hyperbolic reflection vocabulary."""

from dzack_research.preamble.all import ZZ, HyperbolicLattices, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage",
    "live_owner": "src/dzack_research/preamble/categories/hyperbolic_lattices.py",
    "disposition": "reconciled-live-owner",
}


def _u_plus_a1():
    return HyperbolicLattices(ZZ)(Lattices(ZZ)("U") + Lattices(ZZ)("A1"))


def test_archived_vinberg_algorithm_is_the_live_owned_root_family() -> None:
    lattice = _u_plus_a1()
    archived_name = lattice.vinberg_algorithm(max_decompositions=200)
    live_name = lattice.vinberg_simple_roots(max_decompositions=200)

    assert archived_name == live_name
    assert all(root.parent() is lattice for root in archived_name)


def test_archived_weyl_group_is_the_live_reflection_subgroup() -> None:
    lattice = _u_plus_a1()
    roots = lattice.vinberg_algorithm(max_decompositions=200)
    weyl = lattice.weyl_group(max_decompositions=200)
    reflection = lattice.reflection_group(max_decompositions=200)

    assert weyl.supergroup() is lattice.O()
    assert reflection.supergroup() is lattice.O()
    for root in roots:
        mirror = lattice.reflection(root)
        assert mirror in weyl
        assert mirror in reflection
