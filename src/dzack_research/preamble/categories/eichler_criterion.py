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


def covering_discriminant_classes(lattice, square):
    r"""Return the discriminant classes covering the primitive vectors of ``square``.

    For a primitive ``v`` write ``d = div(v)``, so ``v/d`` lies in ``L^#`` and
    ``x = [v/d]`` lies in ``A_L``.  The order of ``x`` is exactly ``d``: a
    smaller order ``e`` would put ``(e/d) v`` in ``L`` and contradict
    primitivity.  The discriminant quadratic form then reads
    ``q_{A_L}(x) = q(v)/d^2`` in ``K/2R``.  Both statements are unconditional,
    so the classes satisfying

    ``q_{A_L}(x) = square / ord(x)^2``

    cover the primitive vectors of that square: every such vector has its
    divided class among them, with its divisibility the order of that class.
    This is the finite covering list, and it is computed by one pass over the
    finite discriminant group with no search in ``L``.

    Under Eichler's criterion the list is sharper still: the stable orthogonal
    group is then transitive on the primitive vectors sharing a square and a
    divided class, so each class in the list carries at most one stable orbit.
    Which classes are actually attained is a separate question this list does
    not answer, which is why it covers rather than enumerates.
    """
    from dzack_research.preamble.categories.sets.finite_ordered_sets import (
        finite_ordered_set,
    )

    discriminant = lattice.discriminant_group()
    values = discriminant.quadratic_value_module()
    field = lattice.base_ring().fraction_field()
    target = field(square)
    return finite_ordered_set(
        tuple(
            element
            for element in discriminant.elements()
            if discriminant.q(element)
            == values(target / field(element.additive_order()) ** 2)
        )
    )


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
    "covering_discriminant_classes",
    "eichler_criterion_applies",
    "hyperbolic_plane_summand_count",
    "splits_two_hyperbolic_planes",
]
