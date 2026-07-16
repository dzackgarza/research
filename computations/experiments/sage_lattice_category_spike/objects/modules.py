r"""The module spine: ``Modules(R)`` through the owned free and projective
nodes.

``Modules(R)`` chains into the additive root, so every generic set
behavior is already rolled up through the underlying-set route — this
module adds NO set forwarding of its own. Over a field the constructor
dispatches to ``VectorSpaces(K)``, mirroring Sage's own dispatch.

Freeness and finite projectivity are mathematical properties, strictly
weaker than a chosen basis. The owned nodes carry the opt-in-with-trust
predicate overrides (decision:
``predicate-subcategories-are-opt-in-with-trust``): joining
``FreeModules(R)`` IS the declaration ``is_free``, from which
``is_torsionfree`` follows and ``is_torsion`` is refused. Coordinates
exist only through a separately chosen basis: a set isomorphism
``U(M) <-> U(R) x ... x U(R)`` realized as a pair of set maps whose
inverse returns elements of the module — never a re-parenting of the
module onto its coordinate description.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, cast

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.fields import Fields as SageFields
from sage.categories.homset import Hom
from sage.categories.modules import Modules as SageModules
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.matrix.constructor import matrix

from ..lexicon import BaseRing, SageParent
from .functors import CatObject
from .magmas import AdditiveGroups

if TYPE_CHECKING:
    from .set_constructions import CartesianProduct


def _undispatched_modules(base_ring: BaseRing) -> Category:
    r"""The plain ``Modules(R)`` node, bypassing field dispatch — used by
    the nodes that sit above it in the owned spine."""
    return cast(Category, Category_over_base_ring.__classcall__(Modules, base_ring))


def _coordinate_target(base_ring: BaseRing, rank: int) -> CartesianProduct:
    r"""``U(R) x ... x U(R)``: the coordinate description's home, built from
    the fundamental set underlying the base ring."""
    from sage.rings.integer_ring import ZZ
    from sage.rings.rational_field import QQ

    from .fundamental_sets import Integers, Rationals
    from .set_constructions import CartesianProduct

    assert base_ring is ZZ or base_ring is QQ, f"coordinate targets are wired for the fundamental scalars; found {base_ring} (extend the fundamental sets first)"
    # underlying_set is injected by the forwarding roots at runtime.
    scalar_set = cast(Any, Integers() if base_ring is ZZ else Rationals()).underlying_set()
    return CartesianProduct(*([scalar_set] * rank))


class Modules(CatObject, Category_over_base_ring):
    r"""The owned category of modules over ``R``: an additively commutative
    group with ``R``-scalar action, dispatching to ``VectorSpaces(K)``
    over a field."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: BaseRing) -> Category:
        if base_ring in SageFields():
            return cast(Category, VectorSpaces(base_ring))
        return cast(Category, Category_over_base_ring.__classcall__(cls, base_ring))

    def super_categories(self) -> list[Category]:
        return [SageModules(self.base_ring()), AdditiveGroups().AdditiveCommutative()]

    if TYPE_CHECKING:

        def Countable(self) -> Category: ...
        def Uncountable(self) -> Category: ...


class VectorSpaces(CatObject, Category_over_base_ring):
    r"""The owned category of vector spaces over a field ``K``: the
    field-dispatch image of ``Modules(K)``."""

    def super_categories(self) -> list[Category]:
        from sage.categories.vector_spaces import VectorSpaces as SageVectorSpaces

        return [SageVectorSpaces(self.base_ring()), _undispatched_modules(self.base_ring())]


class FreeModules(CatObject, Category_over_base_ring):
    r"""Free ``R``-modules: joining this node IS the opt-in declaration of
    freeness, with its predicate consequences."""

    def super_categories(self) -> list[Category]:
        # Plain construction: over a field this correctly dispatches, since
        # a free module over a field IS a vector space.
        return [cast(Category, Modules(self.base_ring()))]

    class ParentMethods:
        def is_free(self) -> bool:
            return True

        def is_torsionfree(self) -> bool:
            r"""A free module over a domain is torsion-free — the predicate
            follows from the freeness declaration."""
            return self.is_free()

        def is_torsion(self) -> bool:
            return False

        def coordinates(self, basis: Sequence[Any]) -> SetMorphism:
            r"""The coordinate set map ``U(M) -> U(R) x ... x U(R)`` for a
            CHOSEN basis: strictly stronger data than freeness, supplied
            per call and never stored as classification. Non-coordinates
            (a vector outside the basis span over ``R``) fail loudly at
            the target's own membership boundary."""
            parent = cast(SageParent, self)
            base_ring = parent.category().base_ring()
            basis_matrix = matrix(base_ring, [list(b) for b in basis])
            target = _coordinate_target(base_ring, len(basis))
            domain = cast(Any, self).underlying_set()
            return SetMorphism(Hom(domain, target, SageSets()), lambda element: target(tuple(basis_matrix.solve_left(element))))

        def from_coordinates(self, basis: Sequence[Any]) -> SetMorphism:
            r"""The registered inverse of ``coordinates(basis)``: coordinate
            tuples come back as elements of the module, never as bare
            tuples — enumeration through the isomorphism returns module
            elements."""
            parent = cast(SageParent, self)
            base_ring = parent.category().base_ring()
            target = _coordinate_target(base_ring, len(basis))
            codomain = cast(Any, self).underlying_set()
            return SetMorphism(Hom(target, codomain, SageSets()), lambda point: sum(scalar * b for scalar, b in zip(point.value, basis)))


class FiniteProjectiveModules(CatObject, Category_over_base_ring):
    r"""Finite projective ``R``-modules: the standard supercategory
    required by lattices. Finite projectivity supplies NO coordinate
    isomorphism — a projective module without a chosen trivialization has
    only its ordinary underlying-set route."""

    def super_categories(self) -> list[Category]:
        return [cast(Category, Modules(self.base_ring()))]

    class ParentMethods:
        def is_projective(self) -> bool:
            return True

        def is_finitely_generated(self) -> bool:
            return True


class FiniteFreeModules(CatObject, Category_over_base_ring):
    r"""Finite free ``R``-modules: free of finite rank, hence in
    particular finite projective."""

    def super_categories(self) -> list[Category]:
        return [FreeModules(self.base_ring()), FiniteProjectiveModules(self.base_ring())]

    if TYPE_CHECKING:

        def Countable(self) -> Category: ...
        def Uncountable(self) -> Category: ...
