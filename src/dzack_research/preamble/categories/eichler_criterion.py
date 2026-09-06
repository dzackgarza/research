r"""Eichler's criterion: the orbit invariants of a primitive vector.

Let ``L`` be an even lattice splitting two hyperbolic planes, ``L = U + U +
K``.  Eichler's criterion says that the stable orthogonal group ``ker(rho_L)``
acts transitively on the primitive vectors of a given square and a given
class in the discriminant group, so the orbit of a primitive ``v`` is
determined by

``q(v)``,   ``div(v) = gcd b(v, L)``,   ``[v / div(v)] in A_L``.

The reference is Eichler, *Quadratische Formen und orthogonale Gruppen*,
Springer 1952, section 10.

All three invariants are already owned: ``v.q()``, ``v.div()`` and
``v.divided_discriminant_class()``.  What this module adds is the hypothesis
under which they are a complete invariant, and the decision the theorem then
licenses.  That decision replaces a search: it answers an orbit question about
an infinite group by comparing three finite pieces of data, with no
enumeration and no bound.

The hypothesis is checked on the lattice's *represented* decomposition, not by
searching for an abstract isometry to ``U + U + K``.  A lattice built as a sum
of named summands answers it; a lattice given only by a Gram matrix does not,
and that is a statement about the presentation rather than about the lattice.
"""


def hyperbolic_plane_summand_count(lattice):
    r"""Return how many indecomposable summands of ``lattice`` are hyperbolic planes."""
    from dzack_research.preamble.categories.lattices import Lattices

    plane = Lattices(lattice.base_ring())("U")
    return sum(
        1 for summand in lattice.indecomposable_summands() if summand.is_isometric(plane)
    )


def splits_two_hyperbolic_planes(lattice) -> bool:
    r"""Return whether the represented decomposition has two hyperbolic-plane summands.

    This is the hypothesis of Eichler's criterion, read off the decomposition
    the lattice was built with.  A lattice presented only by a Gram matrix has
    no represented decomposition and answers ``False`` even when it is
    abstractly isometric to one that splits ``U + U``.
    """
    if not lattice.is_decomposable():
        return False
    return hyperbolic_plane_summand_count(lattice) >= 2


def eichler_criterion_applies(lattice) -> bool:
    r"""Return whether Eichler's criterion classifies primitive-vector orbits here."""
    return bool(lattice.is_even()) and splits_two_hyperbolic_planes(lattice)


def are_in_one_stable_orbit(left, right) -> bool:
    r"""Decide whether two primitive vectors share a ``ker(rho_L)`` orbit.

    The decision is Eichler's: under the criterion's hypothesis the square,
    the divisibility and the divided discriminant class are a complete
    invariant of the orbit.  Both vectors are required to be primitive,
    because the criterion is a statement about primitive vectors.
    """
    lattice = left.parent()
    assert right.parent() is lattice, (
        "an orbit comparison is between two vectors of one lattice"
    )
    assert eichler_criterion_applies(lattice), (
        "Eichler's criterion classifies primitive-vector orbits for an even "
        "lattice splitting two hyperbolic planes; this lattice does not "
        "present such a decomposition, and the orbit question is then a "
        "computation for the exact indefinite backend rather than a "
        "comparison of invariants"
    )
    for vector in (left, right):
        assert lattice.subobject_on((vector,)).is_primitive(), (
            "Eichler's criterion compares primitive vectors"
        )
    return (
        left.q() == right.q()
        and left.div() == right.div()
        and left.divided_discriminant_class() == right.divided_discriminant_class()
    )


__all__ = [
    "are_in_one_stable_orbit",
    "eichler_criterion_applies",
    "hyperbolic_plane_summand_count",
    "splits_two_hyperbolic_planes",
]
