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

None of this is computed here, and no registered provider of the capability
layer supplies it.  The exact reduction is owned upstream by
polyhedral_common, which reaches the Lorentzian perfect domain only as the
``h = 1`` branch inside its combined indefinite algorithm and exposes no
entry point that traverses the complex; what the layer currently offers is
the automorphism group, the vector and isotropic-subspace equivalence
witnesses, their stabilizers and orbit representatives.  The port that would
supply the traversal is ``sage-indefinite-port``, whose capability manifest
records that dispatch, and it would arrive here as one further capability
name rather than as an implementation in this file.

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
        "perfect domains of Opgenorth's indefinite reduction, and no provider "
        "registered in the capability layer traverses them; the port that "
        "would supply one is sage-indefinite-port.  For "
        "generators of O(L) use L.O().group_generators(), for vector orbits "
        "use L.O().vector_orbit_representatives(square), and for the "
        f"Lorentzian component character use L.positive_cone_subgroup(); the "
        f"marked family {marked_vectors} would only be needed by the traversal "
        "this absence names"
    )


__all__ = ["lorentzian_reduction_complex"]
