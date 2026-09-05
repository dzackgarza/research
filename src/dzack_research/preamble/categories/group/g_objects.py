r"""Objects of a category with a chosen action of a group.

For a group ``G`` and a category ``C``, a ``G``-action on an object ``X`` of
``C`` is a functor ``BG -> C`` selecting ``X``; equivalently a group morphism
``G -> Aut_C(X)`` (lean-categories FOUNDATIONS, Definition 34.1).  A morphism
of ``G``-objects is a morphism of ``C`` commuting with the two actions, so
``Mor_G(X, Y)`` is the fixed locus of ``G`` acting on ``Mor_C(X, Y)`` by
conjugation.  The forgetful functor to ``C`` is evaluation at the one object
of ``BG``.

``GSets(G)`` is ``GObjects(G, Sets())``, and ``Modules(R[G])`` refines
``GObjects(G, Modules(R))``.  A specialization constructs its objects through
``C``'s own constructor and supplies the action as the one datum of this
level: a function from group elements to data that ``Mor_C(X, X)`` accepts.
"""

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFinitePresentation,
    _owned_group,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def _verify_relators(action, group, endomorphisms) -> None:
    r"""Check that the generator images satisfy the group's chosen relators.

    An action is a left action: ``rho(s_1 s_2) = rho(s_1) rho(s_2)``, the
    product of the matrices acting on an ordered basis.  A function on the
    generators extends to a group morphism exactly when every defining
    relator, composed in that order, is the identity.  This decides that the
    generator images define an action; the datum's values on the other group
    elements are the caller's assertion and are not enumerated.
    """
    if group not in GroupsWithChosenFinitePresentation():
        return
    # Private serialization: Tietze letters index the chosen generators in
    # their recorded order, and a negative letter names an inverse.
    generators = tuple(group.group_generators())
    identity = endomorphisms.identity()
    for relator in group.defining_relations():
        composite = identity
        for letter in relator.Tietze():
            generator = generators[abs(int(letter)) - 1]
            composite = composite * action(generator if int(letter) > 0 else ~generator)
        assert composite == identity, (
            f"the generator images do not satisfy the relator {relator}, "
            f"so they define no left action of {group}"
        )


class EquivariantMorphism(Morphism):
    r"""A morphism of ``C`` between two ``G``-objects that commutes with the actions."""

    def __init__(self, parent, arrow) -> None:
        Morphism.__init__(self, parent)
        self._arrow = arrow

    def underlying_arrow(self):
        r"""Return the same morphism read in the underlying category."""
        return self._arrow

    def _call_(self, element):
        return self._arrow(element)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        homset = self.parent().hom_family().Of(other.domain(), self.codomain())
        return homset._from_equivariant_arrow(
            self.underlying_arrow() * other.underlying_arrow()
        )

    def __eq__(self, other) -> bool:
        r"""Equal when the underlying morphisms of ``C`` are; ``other`` may be either."""
        match other:
            case EquivariantMorphism():
                other = other.underlying_arrow()
        return self.underlying_arrow() == other

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), id(self)))

    def _repr_(self) -> str:
        return f"Equivariant {self.underlying_arrow()}"


class GObjectHomset(CategoricalHomset):
    r"""The represented ``Mor_G(X, Y)``: the equivariant morphisms of ``C``.

    Equivariance is decided on the chosen generators of the acting group,
    since the morphisms commuting with a group element form a subgroup.
    """

    Element = EquivariantMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        assert domain.acting_group() is codomain.acting_group(), (
            "equivariant morphisms require one acting group"
        )
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def underlying_homset(self):
        r"""Return ``Mor_C(X, Y)``, in which the equivariant morphisms lie."""
        return self.domain().underlying_category().Mor(self.domain(), self.codomain())

    def is_equivariant(self, arrow):
        r"""Decide ``f rho_X(s) = rho_Y(s) f`` on the chosen generators ``s``."""
        group = self.domain().acting_group()
        if group.is_finitely_generated() is not True:
            return Unknown
        arrow = self.underlying_homset()(arrow)
        return all(
            arrow * self.domain().action_of(generator)
            == self.codomain().action_of(generator) * arrow
            for generator in group.group_generators()
        )

    def _from_equivariant_arrow(self, arrow):
        r"""Wrap an arrow whose equivariance follows from its construction."""
        return self.element_class(self, arrow)

    def _element_constructor_(self, datum):
        arrow = self.underlying_homset()(datum)
        if self.is_equivariant(arrow) is not True:
            raise ValueError(
                f"{arrow} does not commute with the {self.domain().acting_group()}-actions"
            )
        return self._from_equivariant_arrow(arrow)

    def identity(self):
        assert self.domain() is self.codomain(), "identity belongs to an endomorphism Hom-set"
        return self._from_equivariant_arrow(self.underlying_homset().identity())

    def _repr_(self) -> str:
        return f"Mor_{self.domain().acting_group()}({self.domain()}, {self.codomain()})"


class GObjectHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GObjectHomset


class GObjects(CategoryPacketMethods, OwnedCategory):
    r"""The category of objects of ``C`` with a chosen ``G``-action."""

    @staticmethod
    def __classcall__(cls, group, category):
        return Category.__classcall__(cls, _owned_group(group), category)

    def __init__(self, group, category) -> None:
        self._group = group
        self._category = category
        OwnedCategory.__init__(self)

    def acting_group(self):
        return self._group

    def underlying_category(self):
        r"""Return ``C``, the codomain of the forgetful functor."""
        return self._category

    def super_categories(self):
        return [self.underlying_category()]

    def _repr_object_names(self):
        return f"{self.acting_group()}-objects in {self.underlying_category()._repr_object_names()}"

    _HomCategory = GObjectHomCategoryConstruction

    def an_object(self):
        r"""The trivial action on an object of the underlying category."""
        from dzack_research.preamble.categories.group.g_sets import trivial_g_set
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        category = self.underlying_category()
        sample = category.an_object()
        if category is Sets():
            return trivial_g_set(sample, self.acting_group())
        assert category.is_subcategory(Modules(category.base_ring())), (
            f"no owned constructor equips an object of {category} with a group action"
        )
        return Modules(category.base_ring()).trivial_action(self.acting_group())(sample)

    class ParentMethods:
        def __init__(self, acting_group, action, underlying_category, **rest) -> None:
            self._preamble_acting_group = acting_group
            self._preamble_action_datum = action
            self._preamble_underlying_category = underlying_category
            super().__init__(**rest)

        def acting_group(self):
            return self._preamble_acting_group

        def underlying_category(self):
            r"""Return the category in which this object is acted on."""
            return self._preamble_underlying_category

        @cached_method
        def action(self):
            r"""Return the chosen action as the set morphism ``G -> Mor_C(X, X)``.

            Its values are automorphisms of ``X`` in ``C``, and the action is
            a left action: ``rho(s_1 s_2) = rho(s_1) rho(s_2)``.  The generator
            images are checked against the group's chosen relators once, here.
            """
            endomorphisms = self.underlying_category().Mor(self, self)
            datum = self._preamble_action_datum
            action = Sets().Mor(self.acting_group(), endomorphisms)(
                lambda group_element: endomorphisms(datum(group_element))
            )
            _verify_relators(action, self.acting_group(), endomorphisms)
            return action

        @cached_method
        def action_of(self, group_element):
            r"""Return the automorphism of ``X`` in ``C`` induced by ``group_element``."""
            assert group_element in self.acting_group(), (
                f"{group_element} is not an element of {self.acting_group()}"
            )
            return self.action()(group_element)

        def act(self, group_element, element):
            r"""Return ``group_element . element``."""
            assert element in self, f"{element} is not an element of {self}"
            return self.action_of(group_element)(element)

        def is_invariant(self, element):
            r"""Decide ``g . element = element`` for all ``g``, on the chosen generators."""
            group = self.acting_group()
            if group.is_finitely_generated() is not True:
                return Unknown
            return all(
                self.act(generator, element) == element
                for generator in group.group_generators()
            )


__all__ = [
    "EquivariantMorphism",
    "GObjectHomset",
    "GObjects",
]
