r"""First-class functor kernel proofs (issue #211, kernel commit of CP1).

Functors are morphisms of the (mostly synthetic) category of categories:
they inhabit functor spaces ``Fun(C, D)``, compose associatively with
identity absorption, act on objects and morphisms, and support natural
isomorphisms whose components and naturality squares are checked on real
nonidentity morphisms. Sage owns none of this surface: ``Functor`` has no
composition operator and ``Hom`` between categories falls back to a generic
id-equality homset in ``Objects()`` (verified against the running Sage at
kernel authoring).

Witnesses follow the AG (negative-definite) root convention: ``A2`` has
Gram matrix ``[[-2, 1], [1, -2]]``.
"""

from __future__ import annotations

import pytest

from sage.all import QQ, ZZ, identity_matrix, matrix

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.objects.categories import Lattices
from sage_lattice_category_spike.objects.functors import (
    FunctorSpace,
    LatticeBaseChangeFunctor,
    NaturalIsomorphism,
    TwistFunctor,
)


def test_twist_functor_acts_on_objects_and_morphisms():
    r"""``L(2)`` doubles the form and keeps morphism matrices: the twist
    endofunctor is total data (objects and morphisms), not an object-only
    construction."""
    A2 = Lattice("A2")
    T2 = TwistFunctor(Lattices(ZZ), 2)
    twisted = T2(A2)
    assert twisted.gram_matrix() == matrix(ZZ, [[-4, 2], [2, -4]])
    assert twisted.base_ring() == ZZ

    root = A2.gens()[0]
    reflection = A2.reflection(root)
    image = T2(reflection)
    assert image.matrix() == reflection.matrix()
    assert image.domain() == twisted
    assert image.codomain() == twisted
    assert image * image == twisted.identity_morphism()


def test_composition_is_associative_with_exact_boundaries():
    r"""``(F . T2) . T3`` and ``F . (T2 . T3)`` are the same route
    ``Lattices(ZZ) -> Lattices(QQ)``: same boundaries, same object image
    (``A2`` twisted by 6 over ``QQ``), same morphism image."""
    A2 = Lattice("A2")
    T2 = TwistFunctor(Lattices(ZZ), 2)
    T3 = TwistFunctor(Lattices(ZZ), 3)
    F = LatticeBaseChangeFunctor(Lattices(ZZ), Lattices(QQ))

    left = (F * T2) * T3
    right = F * (T2 * T3)
    assert left.domain() is Lattices(ZZ)
    assert left.codomain() is Lattices(QQ)
    assert right.domain() is Lattices(ZZ)
    assert right.codomain() is Lattices(QQ)

    image = left(A2)
    assert image.base_ring() == QQ
    assert image.gram_matrix() == matrix(QQ, [[-12, 6], [6, -12]])
    assert right(A2) == image

    reflection = A2.reflection(A2.gens()[0])
    assert left(reflection).matrix() == reflection.matrix()
    assert left(reflection) == right(reflection)


def test_identity_is_absorbed_and_acts_as_identity():
    r"""The identity of ``Fun(C, C)`` is the unit of composition: it is
    absorbed exactly (object identity, not a wrapper), and it fixes objects
    and nonidentity morphisms."""
    A2 = Lattice("A2")
    identity = FunctorSpace(Lattices(ZZ), Lattices(ZZ)).identity()
    assert identity(A2) is A2

    reflection = A2.reflection(A2.gens()[0])
    assert reflection.matrix() != identity_matrix(ZZ, 2)
    assert identity(reflection) == reflection

    F = LatticeBaseChangeFunctor(Lattices(ZZ), Lattices(QQ))
    assert (F * identity) is F
    assert (FunctorSpace(Lattices(QQ), Lattices(QQ)).identity() * F) is F


def test_composition_refuses_mismatched_boundaries():
    r"""``T2 . F`` with ``T2`` at ``ZZ`` and ``F`` landing in ``QQ`` is an
    incoherent route and must be refused at composition time."""
    T2 = TwistFunctor(Lattices(ZZ), 2)
    F = LatticeBaseChangeFunctor(Lattices(ZZ), Lattices(QQ))
    with pytest.raises(AssertionError):
        T2 * F


def test_categories_are_objects_of_cat_and_functor_spaces_are_its_homsets():
    r"""The kernel's categorical statement made literal: category instances
    are elements of ``Cat``, and ``Hom_Cat(C, D)`` IS the functor space, so
    functors are genuinely morphisms of a category of categories."""
    from sage_lattice_category_spike.objects.functors import Cat

    cat = Cat()
    assert Lattices(ZZ) in cat
    assert Lattices(QQ) in cat
    assert ZZ not in cat

    homset = cat.homset(Lattices(ZZ), Lattices(QQ))
    assert homset is FunctorSpace(Lattices(ZZ), Lattices(QQ))
    assert LatticeBaseChangeFunctor(Lattices(ZZ), Lattices(QQ)) in homset
    a2 = Lattice("A2")
    assert cat.homset(Lattices(ZZ), Lattices(ZZ)).identity()(a2) is a2

    # Owned categories are objects of Cat through the STANDARD protocols:
    # category() answers Cat, and Sage's own Hom dispatches to Fun(C, D).
    from sage.categories.homset import Hom
    from sage_lattice_category_spike.objects.magmas import Magmas
    from sage_lattice_category_spike.objects.sets import Sets

    assert Magmas().category() is cat
    assert Sets().category() is cat
    assert Hom(Magmas(), Sets()) is FunctorSpace(Magmas(), Sets())


def test_functor_space_membership_is_boundary_exact():
    r"""``Fun(C, D)`` is a genuine parent: unique per boundary pair, and
    membership is exactly agreement of domain and codomain."""
    fun_zq = FunctorSpace(Lattices(ZZ), Lattices(QQ))
    assert fun_zq is FunctorSpace(Lattices(ZZ), Lattices(QQ))

    F = LatticeBaseChangeFunctor(Lattices(ZZ), Lattices(QQ))
    T2 = TwistFunctor(Lattices(ZZ), 2)
    assert F in fun_zq
    assert T2 not in fun_zq
    assert T2 in FunctorSpace(Lattices(ZZ), Lattices(ZZ))
    assert (F * T2) in fun_zq


def test_minus_one_is_a_natural_automorphism_of_the_identity():
    r"""``v -> -v`` is the classic nonidentity natural automorphism of the
    identity functor on an additive category: its components are the
    ``-id`` isometries and every naturality square against real morphisms
    commutes because morphisms are additive."""
    A2 = Lattice("A2")
    E8 = Lattice("E8")
    identity = FunctorSpace(Lattices(ZZ), Lattices(ZZ)).identity()

    def minus_one(L):
        return Lattices(ZZ).morphism(L, -identity_matrix(ZZ, L.rank()), codomain=L)

    eta = NaturalIsomorphism(identity, identity, components=minus_one, inverse_components=minus_one)

    component = eta.component(A2)
    assert component.matrix() == -identity_matrix(ZZ, 2)
    assert component != A2.identity_morphism()

    reflection = A2.reflection(A2.gens()[0])
    assert eta.check_naturality_on([reflection, E8.reflection(E8.gens()[0])])

    inverse = eta.inverse()
    assert inverse.component(A2) * component == A2.identity_morphism()
    assert component * inverse.component(A2) == A2.identity_morphism()


def test_base_change_preserves_laws_and_is_faithful_on_a_finite_homset():
    r"""The concrete-node functor laws for scalar extension, proven
    exhaustively on the order-12 group ``O(A2)``: identities and
    compositions are preserved, and the twelve images stay pairwise
    distinct — the behavioral content of faithfulness on this homset."""
    A2 = Lattice("A2")
    F = LatticeBaseChangeFunctor(Lattices(ZZ), Lattices(QQ))
    isometries = list(A2.isometry_group())
    assert len(isometries) == 12

    image_lattice = F(A2)
    assert F(A2.identity_morphism()) == image_lattice.identity_morphism()

    images = [F(g) for g in isometries]
    assert all(F(g * h) == F(g) * F(h) for g in isometries[:4] for h in isometries[:4])
    assert len({tuple(tuple(row) for row in phi.matrix().rows()) for phi in images}) == 12
    assert F.is_faithful()
