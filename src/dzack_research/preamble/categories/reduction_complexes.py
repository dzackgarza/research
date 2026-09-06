r"""The reduction complex of an indefinite lattice, and what it would need.

A reduction complex is a ``G``-CW structure on the symmetric space of
``O(L)(R)``: for an indefinite form the cells are the perfect domains of
Opgenorth's reduction theory, each a rational polyhedral cone spanned by the
minimal vectors of an auxiliary positive form, and two cells are adjacent when
they share a facet.  Traversing the complex from one cell, taking the
stabilizer of each cell and the transporters along its facets, yields
generators of ``O(L)`` and decides isometry of two lattices in the same genus.
The *marked* variant carries with each cell a finite family of nonzero-norm
vectors, which is how a general Lorentzian vector orbit is computed: the
traversal then answers about the pair (cell, marked family) rather than about
the cell alone.

None of this is computed here.  The exact reduction is owned upstream by
polyhedral_common, whose indefinite reduction and perfect-domain traversal are
not among the entry points the repository's ``py_polyhedral.binaries`` bridge
exposes; that bridge currently offers the automorphism group, vector and
isotropic-subspace equivalence, their stabilizers, orbit representatives, the
Lorentzian reflective edgewalk, dual descriptions, face lattices and Delaunay
data.  Adding the perfect-domain entry point is work on that bridge.

What *is* owned, so that a caller does not reach here for it:

- generators of ``O(L)`` for an indefinite lattice, through
  ``L.O().group_generators()``, which already goes to polyhedral_common's
  automorphism group and so does not need the cell traversal;
- the ``O(L)``-orbits of vectors of a given square, their stabilizers and
  their equivalence witnesses, through the exact indefinite backend;
- the Lorentzian component character in signature ``(1, n)``, through
  ``L.positive_cone_subgroup()``, whose product with ``<-1>`` is ``O(L)``
  because ``-1`` exchanges the two components of the positive cone.
"""


def lorentzian_reduction_complex(lattice, marked_vectors=None):
    r"""Return the reduction complex of ``lattice``, optionally with marked vectors."""
    assert False, (
        f"the reduction complex of {lattice} is not computed: its cells are the "
        "perfect domains of Opgenorth's indefinite reduction, and no entry "
        "point of the repository's py_polyhedral bridge traverses them.  For "
        "generators of O(L) use L.O().group_generators(), for vector orbits "
        "use L.O().vector_orbit_representatives(square), and for the "
        f"Lorentzian component character use L.positive_cone_subgroup(); the "
        f"marked family {marked_vectors} would only be needed by the traversal "
        "this absence names"
    )


__all__ = ["lorentzian_reduction_complex"]
