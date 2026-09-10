r"""Archived lattice decomposition semantics on represented orthogonal sums.

The archived integral-lattice parent exposed its chosen direct-sum decomposition
and returned summands as actual embedded lattice subobjects.  The live owner
keeps that representation-sensitive contract: it does not run an unrelated
indecomposability algorithm on an arbitrary Gram matrix.
"""

from dzack_research.preamble.all import Lattices, ZZ


def test_archived_orthogonal_sum_decomposition_retains_actual_summand_embeddings() -> None:
    hyperbolic = Lattices(ZZ)("U")
    root = Lattices(ZZ)("A2")
    lattice = hyperbolic + root

    decomposition = lattice.decomposition()
    summands = tuple(lattice.summands())

    assert decomposition is not None
    assert lattice.is_decomposable()
    assert len(summands) == 2
    assert tuple(decomposition.summands()) == summands

    for summand in summands:
        assert summand.ambient_lattice() is lattice
        assert summand.inclusion().codomain() is lattice
        for generator in summand.module_generators():
            assert summand.inclusion()(generator).parent() is lattice

    assert summands[0].is_isometric(hyperbolic) is True
    assert summands[1].is_isometric(root) is True
    for left in summands[0].embedded_module_generators():
        for right in summands[1].embedded_module_generators():
            assert lattice.b(left, right) == 0


def test_archived_indecomposable_catalogue_lattice_has_no_chosen_decomposition() -> None:
    lattice = Lattices(ZZ)("A2")

    assert lattice.decomposition() is None
    assert not lattice.is_decomposable()
