r"""The owned operation spines: Magmas → Semigroups → Monoids, and the
additive mirror.

Each node is an owned category over Sage's standard node of the same name,
chained by ``super_categories`` the way :class:`OwnedGroups` is seated —
plain categories, not axiom classes, so nothing here re-registers Sage's
``Associative``/``Unital``/``Inverse`` axioms.  The nodes are the filing
addresses of the operation layer: a method about "a set with an associative
operation" is declared on the owned ``Semigroups``, never re-stated on a
descendant.  They carry no parent methods yet; the addresses land ahead of
their content (user ruling 2026-08-19: category-tree scaffolding is the
filing structure for future work, and emptiness discards ceremony only,
never structure).

``OwnedGroups`` (in ``groups.sage``) is seated over the owned ``Monoids``
node, closing the multiplicative spine; the additive spine closes at
``AdditiveGroups``, consumed by the owned module category
(``modules/pure/modules.sage``), since a module is an additively
commutative group with a ring action.
"""

from sage.categories.additive_magmas import AdditiveMagmas as SageAdditiveMagmas
from sage.categories.additive_semigroups import AdditiveSemigroups as SageAdditiveSemigroups
from sage.categories.additive_monoids import AdditiveMonoids as SageAdditiveMonoids
from sage.categories.additive_groups import AdditiveGroups as SageAdditiveGroups
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.magmas import Magmas as SageMagmas
from sage.categories.monoids import Monoids as SageMonoids
from sage.categories.semigroups import Semigroups as SageSemigroups


class Magmas(Category):
    r"""The owned category of magmas: a set with a binary operation.

    The owned ``Sets()`` is named here because that is what the sentence
    says: a magma *is* a set, with an operation on it.  Seating the root on
    this node and on :class:`AdditiveMagmas` is what carries every owned
    group, ring, module and algebra to it through the spine they already
    declare, so no constructor has to place an object in ``Sets()`` by hand
    and no object can be in ``Sets().Finite()`` without being in ``Sets()``.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "magmas"

    def super_categories(self) -> list[Category]:
        # Local: the sets module is lower than this one and imports nothing
        # from the category tree, so the edge is one-way.
        from dzack_research.preamble.categories.sets.owned_sets import Sets as OwnedSets

        return [SageMagmas(), OwnedSets()]


class Semigroups(Category):
    r"""The owned category of semigroups: associative magmas."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "semigroups"

    def super_categories(self) -> list[Category]:
        return [SageSemigroups(), Magmas()]


class Monoids(Category):
    r"""The owned category of monoids: unital semigroups.

    ``OwnedGroups`` is seated directly over this node.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "monoids"

    def super_categories(self) -> list[Category]:
        return [SageMonoids(), Semigroups()]


class AdditiveMagmas(Category):
    r"""The owned category of additive magmas: a set with a ``+``.

    Names the owned ``Sets()`` for the same reason :class:`Magmas` does, and
    it is this node that carries modules there: a module is an additively
    commutative group with a ring action, so its additive spine passes
    through here.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "additive magmas"

    def super_categories(self) -> list[Category]:
        # Local: see Magmas.super_categories.
        from dzack_research.preamble.categories.sets.owned_sets import Sets as OwnedSets

        return [SageAdditiveMagmas(), OwnedSets()]


class AdditiveSemigroups(Category):
    r"""The owned category of additive semigroups: associative ``+``."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "additive semigroups"

    def super_categories(self) -> list[Category]:
        return [SageAdditiveSemigroups(), AdditiveMagmas()]


class AdditiveMonoids(Category):
    r"""The owned category of additive monoids: additively unital."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "additive monoids"

    def super_categories(self) -> list[Category]:
        return [SageAdditiveMonoids(), AdditiveSemigroups()]


class AdditiveGroups(Category):
    r"""The owned category of additive groups: additive inverses."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "additive groups"

    def super_categories(self) -> list[Category]:
        return [SageAdditiveGroups(), AdditiveMonoids()]
