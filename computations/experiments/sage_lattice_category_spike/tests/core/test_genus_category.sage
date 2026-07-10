r"""Phase A contract (Genus category epic #55, work unit #56): a genus is a
category-backed parent living in the ``Genera`` category; parity is the ``Even``
axiom acquired as OUTPUT of the discriminant form, never a boolean input; and the
parent IS the finite set of its isometry classes, so its cardinality is the class
number.

RED until the ``Genera`` category is built and ``SyntheticGenus`` is wired as its
``ParentMethods``. The literature pins in ``tests/literature/test_lit_genus.sage``
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
