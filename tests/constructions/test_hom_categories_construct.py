r"""Every object has Hom, End and Aut, and a mathematician knows several of their sizes.

One kind of object per row: a finite set, a finite group, a ring, a field, a
free module, a vector space, a lattice, a polynomial algebra, an affine line.
The same three questions are asked of each.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403

OBJECTS = {
    # name: (constructor, |Aut| or None if infinite, |End| or None if infinite)
    "a finite set": (lambda: Sets.Δ[2], 6, 27),
    "a finite group": (lambda: Groups.S(3), 6, 10),
    "the integers": (lambda: ZZ, 1, 1),
    "the rationals": (lambda: QQ, 1, 1),
    "a finite field": (lambda: GF(4), 2, 2),
    "a free module": (lambda: FreeModule(ZZ, 2), None, None),
    "a vector space over GF(2)": (lambda: FreeModule(GF(2), 2), 6, 16),
    "a lattice": (lambda: Lattices(ZZ)("A2"), 12, None),
    "a polynomial algebra": (lambda: PolynomialRing(QQ, "x"), None, None),
    "an affine line": (lambda: AffineSpace(1, QQ), None, None),
}


@pytest.mark.parametrize("name", sorted(OBJECTS))
def test_every_object_has_an_endomorphism_category_with_an_identity(name) -> None:
    obj = OBJECTS[name][0]()
    endomorphisms = obj.Mor(obj)
    identity = endomorphisms.identity()

    assert endomorphisms in Cat()
    assert obj.Mor(obj) is endomorphisms
    assert identity in endomorphisms
    assert identity * identity == identity
    assert identity.domain() is obj
    assert identity.codomain() is obj
    assert obj.End() is endomorphisms


@pytest.mark.parametrize("name", sorted(OBJECTS))
def test_every_object_has_an_automorphism_group(name) -> None:
    build, automorphism_order, endomorphism_count = OBJECTS[name]
    obj = build()
    automorphisms = obj.Aut()
    assert automorphisms in Groups()
    assert automorphisms.one() == obj.Mor(obj).identity()
    if automorphism_order is None:
        assert not automorphisms.is_finite()
    else:
        assert automorphisms.order() == automorphism_order
    if endomorphism_count is not None:
        assert obj.End().cardinality() == endomorphism_count


def test_homs_between_objects_of_different_kinds_are_refused() -> None:
    with pytest.raises(TypeError):
        ZZ.Mor(Sets.Δ[2])
    with pytest.raises(TypeError):
        Groups.S(3).Mor(FreeModule(ZZ, 2))
    with pytest.raises(TypeError):
        FreeModule(ZZ, 2).Mor(FreeModule(QQ, 2))


def test_homs_taken_in_a_common_supercategory() -> None:
    r"""A ring is a set, so set maps between rings exist even where ring maps do not."""
    assert Sets().Mor(QQ, ZZ).cardinality() == continuum
    assert Sets().Mor(GF(4), GF(5)).cardinality() == 5**4
    assert QQ.Mor(ZZ).cardinality() == 0
    assert Sets().Mor(Sets.Δ[2], QQ).cardinality() == aleph0
    assert Groups.S(3).Mor(Groups.C(2)).cardinality() == 2
    assert Sets().Mor(Groups.S(3), Groups.C(2)).cardinality() == 64


def test_hom_modules_are_modules_and_hom_sets_are_sets() -> None:
    plane = FreeModule(ZZ, 2)
    line = FreeModule(ZZ, 1)
    homs = plane.Hom(line)
    assert homs in Modules(ZZ)
    assert homs.module_rank() == 2
    assert plane.Mor(line) in Cat()
    assert homs.as_morphism(homs.zero()) == plane.Mor(line).zero()
    assert Modules(ZZ).Mor(plane, line) is plane.Mor(line)
    assert Modules(ZZ).Iso(plane, plane) in Cat()
    assert Modules(ZZ).Iso(plane, line).cardinality() == 0
    assert Modules(GF(2)).Iso(FreeModule(GF(2), 2), FreeModule(GF(2), 2)).cardinality() == 6
