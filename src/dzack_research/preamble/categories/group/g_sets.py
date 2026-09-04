r"""Finite represented ``G``-sets, their actions, and equivariant Hom-sets.

A ``G``-set is a set with a group morphism ``G -> Sym(X)``; the categories
below are stated over the owned sets and the owned acting group.  The finite
point-set presentation is used only to compute equivariance, fixed points,
orbits, and the standard finite free/cofree constructions.
"""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Homset
from sage.categories.morphism import SetMorphism
from sage.groups.perm_gps.permgroup_named import SymmetricGroup
from sage.misc.abstract_method import abstract_method
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.set_categories import (
    FiniteSets,
    Sets,
)
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)


class GSets(Category):
    @staticmethod
    def __classcall__(cls, group):
        from dzack_research.preamble.categories.group.groups import _owned_group

        return Category.__classcall__(cls, _owned_group(group))

    def __init__(self, group):
        self._group = group
        super().__init__()

    def _make_named_class_key(self, name):
        return self._group

    def group(self):
        return self._group

    acting_group = group

    def super_categories(self):
        return [Sets()]

    def _repr_object_names(self):
        return f"{self._group}-sets"

    class ParentMethods:
        @abstract_method
        def action(self):
            r"""Return the chosen action morphism ``G -> Sym(X)``."""
            ...

        def acting_group(self):
            return self.action().domain()

        def act(self, group_element, point):
            if group_element not in self.acting_group():
                raise TypeError(f"{group_element} is not in {self.acting_group()}")
            if point not in self:
                raise TypeError(f"{point} is not a point of {self}")
            permutation_group = self.action().codomain()
            permutation = self.action()(group_element)
            backend_permutation = permutation_group._to_engine(permutation)
            return self(backend_permutation(point))

        def _Hom_(self, codomain, category=None):
            if codomain not in GSets(self.acting_group()):
                raise TypeError("an equivariant map requires the same acting group")
            return g_set_homset(self, codomain)


class FiniteGSets(Category):
    r"""The represented finite objects of ``GSets(G)``."""

    @staticmethod
    def __classcall__(cls, group):
        from dzack_research.preamble.categories.group.groups import _owned_group

        return Category.__classcall__(cls, _owned_group(group))

    def __init__(self, group):
        self._group = group
        super().__init__()

    def _make_named_class_key(self, name):
        return self._group

    def group(self):
        return self._group

    acting_group = group

    def super_categories(self):
        return [GSets(self._group), FiniteSets()]

    def _repr_object_names(self):
        return f"finite {self._group}-sets"

    class ParentMethods:
        def point_set(self):
            r"""Return the finite set used to present the points of this ``G``-set."""
            return self._preamble_g_set_points


class FiniteGSet(Parent):
    r"""A finite set equipped with a group morphism into its permutation group."""

    def __init__(self, point_set, action) -> None:
        group = action.domain()
        if point_set not in FiniteEnumeratedSets():
            raise TypeError("the represented G-set constructor requires a finite enumerated point set")
        if group.is_finitely_generated() is not True:
            raise NotImplementedError(
                "the represented equivariant Hom-set requires a chosen finite group generating set"
            )
        self._preamble_g_set_points = point_set
        self._preamble_g_set_action = action
        permutations = action.codomain()
        for group_generator in group.group_generators():
            backend_permutation = permutations._to_engine(action(group_generator))
            for point in point_set:
                if backend_permutation(point) not in point_set:
                    raise ValueError("the action morphism does not preserve the stated point set")
        Parent.__init__(self, facade=point_set, category=FiniteGSets(group))

    def __iter__(self):
        return iter(self.point_set())

    def action(self):
        return self._preamble_g_set_action

    def __contains__(self, point) -> bool:
        return point in self.point_set()

    is_parent_of = __contains__

    def __call__(self, point):
        if not isinstance(point, Element):
            return self._element_constructor_(point)
        try:
            return Parent.__call__(self, point)
        except TypeError:
            return self._element_constructor_(point)

    def _element_constructor_(self, point):
        if point not in self.point_set():
            raise ValueError(f"{point!r} is not a point of {self}")
        return self.point_set()(point)

    def cardinality(self):
        return self.point_set().cardinality()

    def _repr_(self):
        return f"{self.point_set()} with {self.acting_group()}-action"


class GSetMorphism(SetMorphism):
    r"""A set map checked to commute with the represented group actions."""

    def __init__(self, parent, function) -> None:
        SetMorphism.__init__(self, parent, function)
        group = self.domain().acting_group()
        if group.is_finitely_generated() is not True:
            raise NotImplementedError(
                "checking equivariance requires a chosen finite group generating set"
            )
        for group_generator in group.group_generators():
            for point in self.domain():
                if self(self.domain().act(group_generator, point)) != self.codomain().act(
                    group_generator, self(point)
                ):
                    raise ValueError("the stated set map is not G-equivariant")

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return g_set_homset(other.domain(), self.codomain())(
            lambda point: self(other(point))
        )


class GSetHomset(OwnedHomset):
    r"""The actual equivariant Hom-set between represented finite ``G``-sets."""

    Element = GSetMorphism

    def __init__(self, domain, codomain) -> None:
        if domain.acting_group() != codomain.acting_group():
            raise ValueError("equivariant maps require a common acting group")
        Homset.__init__(self, domain, codomain, category=GSets(domain.acting_group()))

    def _element_constructor_(self, function):
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism Hom-set")
        return self(lambda point: point)

    def _repr_(self):
        return f"Hom_{self.domain().acting_group()}({self.domain()}, {self.codomain()})"


def g_set_homset(domain, codomain) -> GSetHomset:
    return GSetHomset(domain, codomain)


def _permutation_from_point_map(permutation_group, point_set, mapping):
    images = [mapping(point) for point in point_set]
    for point in point_set:
        if sum(image == point for image in images) != 1:
            raise ValueError("a group action must send each group element to a permutation")

    remaining = list(point_set)
    cycles = []
    while remaining:
        start = remaining[0]
        cycle = [start]
        remaining.remove(start)
        current = mapping(start)
        while current != start:
            cycle.append(current)
            remaining.remove(current)
            current = mapping(current)
        if len(cycle) > 1:
            cycles.append(tuple(cycle))
    return permutation_group(cycles)


def _finite_g_set_from_action(group, point_set, action):
    r"""Construct a represented finite ``G``-set from a binary action.

    ``action(g, x)`` is converted once into the defining group morphism
    ``G -> Sym(X)``; the returned object stores that morphism rather than the
    temporary binary callback.
    """
    from dzack_research.preamble.categories.group.groups import group_homset
    from dzack_research.preamble.categories.group.groups import _own_group, _owned_group

    if isinstance(point_set, (tuple, list)):
        point_set = finite_ordered_set(point_set)
    if point_set not in FiniteEnumeratedSets():
        raise TypeError("the represented G-set constructor requires a finite enumerated point set")
    group = _owned_group(group)
    if group.is_finitely_generated() is not True:
        raise NotImplementedError(
            "constructing a represented action morphism requires a chosen finite group generating set"
        )
    # Private finite backend serialization: Sage's SymmetricGroup constructor
    # requires a sliceable concrete domain, while the mathematical point set
    # remains the owned ordered set above.
    backend_points = list(point_set)
    permutations = _own_group(SymmetricGroup(backend_points))
    action_morphism = group_homset(group, permutations)(
        {
            group_generator: _permutation_from_point_map(
                permutations,
                point_set,
                lambda point, group_generator=group_generator: action(group_generator, point),
            )
            for group_generator in group.group_generators()
        }
    )
    return FiniteGSet(point_set, action_morphism)


def finite_g_set(point_set, group, action):
    r"""Return the finite owned ``G``-set defined by ``action(g,x)``."""
    return _finite_g_set_from_action(group, point_set, action)


def trivial_g_set(point_set, group):
    r"""Equip a finite set with the trivial ``group``-action."""
    return finite_g_set(point_set, group, lambda _group_element, point: point)


class OrbitClass(Element):
    r"""One orbit in the quotient set ``X/G``."""

    def __init__(self, parent, index) -> None:
        Element.__init__(self, parent)
        self._index = index

    def representative(self):
        return self.parent().orbit_points(self).unrank(0)

    def points(self):
        return self.parent().orbit_points(self)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, OrbitClass)
            and other.parent() is self.parent()
            and other._index == self._index
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self):
        return hash((id(self.parent()), self._index))

    def _repr_(self):
        return "Orbit(" + ", ".join(repr(point) for point in self.points()) + ")"


class OrbitSet(Parent):
    r"""The finite orbit quotient ``X/G`` of a represented finite ``G``-set."""

    Element = OrbitClass

    def __init__(self, g_set) -> None:
        from collections import deque

        self._g_set = g_set
        group = g_set.acting_group()
        if group.is_finitely_generated() is not True:
            raise NotImplementedError(
                "constructing finite orbits requires a chosen finite group generating set"
            )

        point_set = finite_ordered_set(g_set)
        point_count = int(point_set.cardinality())
        unseen = {position for position in range(point_count)}
        orbit_families = {}
        orbit_count = 0
        while unseen:
            seed_rank = min(unseen)
            unseen.remove(seed_rank)
            orbit_ranks = {seed_rank}
            frontier = deque((seed_rank,))
            while frontier:
                point_rank = frontier.popleft()
                point = point_set.unrank(point_rank)
                for group_generator in group.group_generators():
                    image_rank = int(
                        point_set.rank(g_set.act(group_generator, point))
                    )
                    if image_rank in orbit_ranks:
                        continue
                    orbit_ranks.add(image_rank)
                    unseen.discard(image_rank)
                    frontier.append(image_rank)

            rank_by_position = {
                position: rank
                for position, rank in enumerate(sorted(orbit_ranks))
            }
            orbit_families[orbit_count] = finite_ordered_image(
                Sets.Δ[len(rank_by_position) - 1],
                lambda position, rank_by_position=rank_by_position: point_set.unrank(
                    rank_by_position[int(position)]
                ),
                name=f"Orbit {orbit_count}",
            )
            orbit_count += 1

        self._orbit_indices = Sets.Δ[orbit_count - 1]
        self._orbit_points = finite_indexed_family(
            self._orbit_indices,
            lambda index: orbit_families[int(index)],
            name="Orbit point families",
        )
        Parent.__init__(self, category=FiniteEnumeratedSets())
        self._orbit_classes = finite_ordered_image(
            self._orbit_indices,
            lambda index: self.element_class(self, index),
            name="Orbit classes",
        )

    def g_set(self):
        return self._g_set

    def __iter__(self):
        return iter(self._orbit_classes)

    def __contains__(self, orbit) -> bool:
        return isinstance(orbit, OrbitClass) and orbit.parent() is self

    def cardinality(self):
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)(self._orbit_classes.cardinality())

    def unrank(self, position):
        return self._orbit_classes.unrank(position)

    def rank(self, orbit):
        if orbit not in self:
            raise ValueError(orbit)
        return int(orbit._index)

    position = rank
    index = rank

    def orbit_points(self, orbit):
        if orbit not in self:
            raise TypeError("the orbit class belongs to a different quotient")
        return self._orbit_points[orbit._index]

    def orbit_of(self, point):
        if point not in self.g_set():
            raise TypeError(f"{point} is not a point of {self.g_set()}")
        for orbit in self:
            if point in self.orbit_points(orbit):
                return orbit
        raise AssertionError("every point of a finite G-set belongs to an orbit")

    def _repr_(self):
        return f"Orbit set of {self.g_set()}"


def fixed_point_set(g_set):
    r"""Return the finite fixed-point set ``X^G``."""
    group = g_set.acting_group()
    if group.is_finitely_generated() is not True:
        raise NotImplementedError(
            "constructing fixed points requires a chosen finite group generating set"
        )
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_filter

    return finite_ordered_filter(
        finite_ordered_set(g_set),
        lambda point: all(
            g_set.act(group_generator, point) == point
            for group_generator in group.group_generators()
        ),
    )


class Torsors(Category):
    def __init__(self, group):
        self._group = group
        super().__init__()

    def _make_named_class_key(self, name):
        return self._group

    def group(self):
        return self._group

    acting_group = group

    def super_categories(self):
        return [GSets(self._group)]

    def _repr_object_names(self):
        return f"torsors under {self._group}"

    class ParentMethods:
        @abstract_method
        def an_element(self):
            r"""Return the chosen point trivializing this torsor."""
            ...

        def transporter(self, source, target):
            r"""Return the unique group element carrying ``source`` to ``target`` when computable."""
            return Unknown


__all__ = [
    "FiniteGSet",
    "FiniteGSets",
    "GSets",
    "GSetHomset",
    "GSetMorphism",
    "OrbitClass",
    "OrbitSet",
    "Torsors",
    "finite_g_set",
    "fixed_point_set",
    "g_set_homset",
    "trivial_g_set",
]
