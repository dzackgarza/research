r"""Phase A contract (Genus category epic #55, work unit #56): a genus is a
category-backed parent living in the ``Genera`` category; parity is the ``Even``
axiom acquired as OUTPUT of the discriminant form, never a boolean input; and the
parent IS the finite set of its isometry classes, so its cardinality is the class
number and it enumerates one representative lattice per class.

Every test here asserts what a genus can accomplish (membership, cardinality,
enumeration). The finite-set route is a public foundation contract: an owned
``Sets`` root supplies the finite enumerated vocabulary, while Sage supplies its
generic implementation. The literature pins in ``tests/literature/test_lit_genus.sage``
(Nikulin 1.10.1 reconstruction, Conway-Sloane Ch.15 local symbols, Gauss-Milgram)
must stay green through the change.
"""

from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc
from sage.all import ZZ


def test_even_lattice_genus_lives_in_the_even_genera_category():
    r"""A2 is an even lattice, so its genus is an object of ``Genera(ZZ)`` and
    acquires the ``Even`` axiom as OUTPUT (parity is a property of the genus,
    not a constructor argument)."""
    genus = lc.Lattice("A2").genus()
    assert genus in lc.Genera(ZZ), "a genus must be an object of the Genera category"
    assert genus in lc.Genera(ZZ).Even(), "an even lattice's genus must acquire the Even axiom"


def test_genus_cardinality_is_its_class_number():
    r"""A genus IS the finite set of its isometry classes; as a parent its
    cardinality equals the class number."""
    genus = lc.Lattice("A2").genus()
    assert genus.cardinality() == genus.class_number(), (
        "genus.cardinality() must equal the class number (the parent is the finite "
        "set of isometry classes)"
    )


def test_iterating_a_genus_enumerates_one_lattice_per_class():
    r"""The finite-set iteration inherited through the owned ``Sets`` route:
    iterating a genus yields exactly its representative lattices, one per isometry
    class, matching its cardinality."""
    genus = lc.Lattice("A2").genus()
    classes = list(genus)
    assert len(classes) == genus.cardinality(), (
        "iterating a genus must yield exactly cardinality()-many lattices "
        "(one representative per isometry class)"
    )
    assert all(lattice in lc.Lattices(ZZ) for lattice in classes), (
        "each element enumerated from a genus must be a lattice"
    )


def test_genus_uses_the_owned_finite_enumerated_sets_route():
    r"""A genus is a finite enumerated object of the spike-owned Sets root.

    This is the project-owned boundary: the concrete genus must retain both the
    finite cardinality and iteration interface and the category route that later
    finite-set parents share.
    """
    from sage_lattice_category_spike import Lattice, Sets

    genus = Lattice("A2").genus()
    assert genus in Sets().Finite().Enumerated(), (
        "a genus must route through the owned finite enumerated Sets category"
    )


def test_genera_is_usable_from_the_package_root():
    r"""The package root is the documented public surface. Exercise the re-export by
    USING it: a genus built through the root-imported constructor must land in the
    root-imported ``Genera`` category -- a dropped root export fails this test."""
    from sage_lattice_category_spike import Genera, Lattice

    assert Lattice("A2").genus() in Genera(ZZ), (
        "Genera and Lattice must be usable from the package root: a genus built via "
        "the root import must be an object of the root-imported Genera category"
    )
