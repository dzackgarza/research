r"""Archived BKZ/HKZ reduction of definite lattice subobjects.

The archived definite-subobject API required reduction to reframe the same
embedded sublattice, not to return a detached lattice with a similar Gram
matrix.  The live reduction records retain the ambient lattice and an exact
isometry from the reduced framing back to the original subobject.
"""

from dzack_research.preamble.all import ZZ, Lattices


def _skew_subobject():
    ambient = Lattices(ZZ)(4)
    e = ambient.module_generators()
    return ambient.subobject_on(
        (
            9 * e[0] + 13 * e[1],
            4 * e[1] + 11 * e[2],
            7 * e[2] + 5 * e[3],
            6 * e[3],
        )
    )


def _assert_same_embedded_subobject(reduction, original) -> None:
    reduced = reduction.reduced
    assert reduced.ambient_lattice() is original.ambient_lattice()
    assert reduction.isometry.domain() is reduced
    assert reduction.isometry.codomain() is original
    reduced.inclusion().factor_through(original.inclusion())
    original.inclusion().factor_through(reduced.inclusion())
    assert reduced.index() == original.index()

    for generator in reduced.module_generators():
        assert reduced.inclusion()(generator) == original.inclusion()(
            reduction.isometry(generator)
        )


def test_archived_subobject_bkz_reframes_the_same_embedded_lattice() -> None:
    subobject = _skew_subobject()
    reduction = subobject.bkz_reduction(block_size=2)

    _assert_same_embedded_subobject(reduction, subobject)


def test_archived_subobject_hkz_reframes_the_same_embedded_lattice() -> None:
    subobject = _skew_subobject()
    reduction = subobject.hkz_reduction()

    _assert_same_embedded_subobject(reduction, subobject)
