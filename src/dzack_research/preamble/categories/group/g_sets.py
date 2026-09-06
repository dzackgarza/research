r"""Finite represented ``G``-sets, their orbits, fixed points, and torsors.

A ``G``-set is an object of ``Sets()`` with a chosen ``G``-action, so
``GSets(G)`` is ``GObjects(G, Sets())``.  The finite represented objects
additionally record the action as a group morphism ``G -> Sym(X)``, which is
the engine used to compute equivariance, fixed points, orbits, and the
standard finite free/cofree constructions.
"""

from collections import deque

from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.groups.perm_gps.permgroup_named import SymmetricGroup
from sage.misc.abstract_method import abstract_method
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import Element

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.group.g_objects import GObjectHomset, GObjects
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _engine_group,
    _integer_engine_point,
    _own_group,
    _owned_group,
    _owned_point,
    group_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_filter,
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    FiniteSets,
    Sets,
)
from dzack_research.preamble.owned_category import object_of


def GSets(group):
    r"""Return the category of ``group``-sets: objects of ``Sets()`` with a chosen action."""
    return GObjects(group, Sets())


class GSetHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GSetHomset


class FiniteGSets(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""The represented finite objects of ``GSets(G)``."""

    def parameter_category(self):
        r"""A finite ``G``-set is indexed by the acting group ``G``."""
        return OwnedGroups()

    def an_object(self):
        r"""The three-point set with the trivial action of the group."""
        from dzack_research.preamble.categories.sets.set_categories import (
            finite_ordinal_set,
        )

        return trivial_g_set(finite_ordinal_set(3), self.group())

    @staticmethod
    def __classcall__(cls, group):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(group))

    def __init__(self, group):
        OwnedParameterizedCategory.__init__(self, group)

    def _make_named_class_key(self, name):
        return self.group()

    def group(self):
        return self.parameter()

    acting_group = group

    def super_categories(self):
        return [GSets(self.group()), FiniteSets(), EnumeratedSets()]

    def _repr_object_names(self):
        return f"finite {self.group()}-sets"

    def _call_(self, point_set, action):
        r"""The finite ``G``-set on ``point_set`` with the action ``action(g, x)``."""
        return finite_g_set(point_set, self.group(), action)

    # Functors out of finite G-sets, sited on their domain.

    def orbits_functor(self):
        r"""``X |-> X/G : FinGSet_G -> FinSet``."""
        from dzack_research.preamble.categories.functors.g_sets import GSetOrbitsFunctor

        return GSetOrbitsFunctor(self.group())

    def fixed_points_functor(self):
        r"""``X |-> X^G : FinGSet_G -> FinSet``."""
        from dzack_research.preamble.categories.functors.g_sets import GSetFixedPointsFunctor

        return GSetFixedPointsFunctor(self.group())

    def orbits_trivial_adjunction(self):
        r"""``(-)/G -| Triv_G``."""
        from dzack_research.preamble.categories.functors.g_sets import (
            g_set_orbits_trivial_adjunction,
        )

        return g_set_orbits_trivial_adjunction(self.group())

    def underlying_cofree_adjunction(self):
        r"""``U -| Map(G, -)``: the underlying set is left adjoint to the cofree ``G``-set."""
        from dzack_research.preamble.categories.functors.g_sets import (
            underlying_cofree_g_set_adjunction,
        )

        return underlying_cofree_g_set_adjunction(self.group())

    _HomCategory = GSetHomCategoryConstruction

    class ParentMethods:
        def __init__(self, point_set, permutation_representation, **rest) -> None:
            assert point_set in FiniteSets(), "a represented G-set is on a finite point set"
            group = permutation_representation.domain()
            assert group.is_finitely_generated() is True, (
                "the represented equivariant Hom-set requires a chosen finite group "
                "generating set"
            )
            self._preamble_g_set_points = point_set
            self._preamble_permutation_representation = permutation_representation
            permutations = permutation_representation.codomain()
            engine = _engine_group(permutations)

            def permute(group_element, point):
                backend_permutation = permutations._to_engine(
                    permutation_representation(group_element)
                )
                return _owned_point(engine, backend_permutation(_integer_engine_point(point)))

            for group_generator in group.group_generators():
                for point in point_set:
                    assert permute(group_generator, point) in point_set, (
                        "the action morphism does not preserve the stated point set"
                    )

            def point_map(group_element):
                return lambda point: self(permute(group_element, point))

            super().__init__(
                acting_group=group,
                action=point_map,
                underlying_category=Sets(),
                facade=point_set,
                **rest,
            )

        def permutation_representation(self):
            r"""Return the chosen action as the group morphism ``G -> Sym(X)``."""
            return self._preamble_permutation_representation

        def point_set(self):
            r"""Return the finite set used to present the points of this ``G``-set."""
            return self._preamble_g_set_points

        def __iter__(self):
            return iter(self.point_set())

        def __contains__(self, point) -> bool:
            return point in self.point_set()

        is_parent_of = __contains__

        def __call__(self, point):
            return self._element_constructor_(point)

        def _element_constructor_(self, point):
            assert point in self.point_set(), f"{point!r} is not a point of {self}"
            return self.point_set()(point)

        def cardinality(self):
            return cardinal(self.point_set().cardinality())

        def orbits(self):
            r"""The orbit set ``X / G``."""
            return FiniteGSets(self.acting_group()).orbits_functor()(self)

        def fixed_points(self):
            r"""The fixed-point set ``X^G``."""
            return FiniteGSets(self.acting_group()).fixed_points_functor()(self)

        def rank(self, point):
            return self.point_set().rank(point)

        def unrank(self, position):
            return self.point_set().unrank(position)

        def _repr_(self):
            return f"{self.point_set()} with {self.acting_group()}-action"


class GSetMorphism(SetMorphism):
    r"""A set map checked to commute with the represented group actions."""

    def __init__(self, parent, function) -> None:
        SetMorphism.__init__(self, parent, function)
        if parent.is_equivariant(self) is not True:
            raise ValueError("the stated set map is not G-equivariant")

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return g_set_homset(other.domain(), self.codomain())(
            lambda point: self(other(point))
        )

    def _as_set_map(self):
        r"""The same function read in ``Sets``, between the finite point sets."""
        return Sets().Mor(self.domain().point_set(), self.codomain().point_set())(
            lambda point: self(point)
        )

    def is_injective(self) -> bool:
        return self._as_set_map().is_injective()

    def is_surjective(self) -> bool:
        return self._as_set_map().is_surjective()


class GSetHomset(GObjectHomset):
    r"""The equivariant Mor category between represented finite ``G``-sets."""

    Element = GSetMorphism

    def _element_constructor_(self, function):
        return self.element_class(self, function)

    def identity(self):
        assert self.domain() is self.codomain(), "identity is defined on an endomorphism Hom-set"
        return self(lambda point: point)


class OrbitSets(OwnedCategory):
    r"""The finite orbit quotients \(X/G\) of a finite \(G\)-set."""

    def an_object(self):
        r"""The orbits of a trivial action on three points."""
        from dzack_research.preamble.categories.functors.g_sets import (
            g_set_orbits_trivial_adjunction,
        )
        from dzack_research.preamble.categories.group.groups import Groups

        group = Groups.S(3)
        return g_set_orbits_trivial_adjunction(group).left_adjoint()(
            trivial_g_set(Sets.Δ[2], group)
        )

    def super_categories(self):
        return [FiniteSets()]

    class ElementMethods(Element):
        r"""What an orbit is."""

        def __init__(self, parent, index) -> None:
            Element.__init__(self, parent)
            self._index = index

        def representative(self):
            return self.parent().orbit_points(self).unrank(0)

        def points(self):
            return self.parent().orbit_points(self)

        def __eq__(self, other) -> bool:
            return other in self.parent() and other._index == self._index

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self):
            return hash((id(self.parent()), self._index))

        def _repr_(self):
            return "Orbit(" + ", ".join(repr(point) for point in self.points()) + ")"

    class ParentMethods:
        def __init__(self, g_set, **rest) -> None:
            self._g_set = g_set
            group = g_set.acting_group()
            assert group.is_finitely_generated() is True, (
                "constructing finite orbits requires a chosen finite group "
                "generating set"
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
            super().__init__(**rest)
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
            try:
                return orbit.parent() is self
            except AttributeError:
                return False

        def _element_constructor_(self, orbit):
            assert orbit in self, f"{orbit} is not an orbit of {self}"
            return orbit

        def cardinality(self):
            return self._orbit_classes.cardinality()

        def unrank(self, position):
            return self._orbit_classes.unrank(position)

        def rank(self, orbit):
            assert orbit in self, f"{orbit} is not an orbit of {self}"
            return int(orbit._index)

        position = rank
        index = rank

        def orbit_points(self, orbit):
            assert orbit in self, "the orbit class belongs to a different quotient"
            return self._orbit_points[orbit._index]

        def orbit_of(self, point):
            assert point in self.g_set(), f"{point} is not a point of {self.g_set()}"
            for orbit in self:
                if point in self.orbit_points(orbit):
                    return orbit
            raise AssertionError("every point of a finite G-set belongs to an orbit")

        def _repr_(self):
            return f"Orbit set of {self.g_set()}"


def g_set_homset(domain, codomain) -> GSetHomset:
    return FiniteGSets(domain.acting_group()).Mor(domain, codomain)


def _permutation_from_point_map(permutation_group, point_set, mapping):
    images = [mapping(point) for point in point_set]
    for point in point_set:
        assert sum(image == point for image in images) == 1, (
            "a group action must send each group element to a permutation"
        )

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
            # The engine permutes the engine's points; owned integers cross here.
            cycles.append(tuple(_integer_engine_point(point) for point in cycle))
    return permutation_group(cycles)


def _finite_g_set_from_action(group, point_set, action):
    r"""Construct a represented finite ``G``-set from a binary action.

    ``action(g, x)`` is read once, on the chosen group generators, into the
    defining group morphism ``G -> Sym(X)``; the returned object stores that
    morphism rather than the temporary binary callback.
    """

    if isinstance(point_set, (tuple, list)):
        # Integer literals are integers: points written as Python ints are
        # owned integers, the same points a permutation group's elements return.
        integers = _own_ring(SageZZ)
        point_set = finite_ordered_set(
            tuple(integers(point) if isinstance(point, int) else point for point in point_set)
        )
    assert point_set in FiniteSets(), (
        "the represented G-set constructor requires a finite point set"
    )
    group = _owned_group(group)
    assert group.is_finitely_generated() is True, (
        "constructing a represented action morphism requires a chosen finite group generating set"
    )
    # Private finite backend serialization: Sage's SymmetricGroup constructor
    # requires a sliceable concrete domain of engine points, while the
    # mathematical point set remains the owned set above.
    backend_points = [_integer_engine_point(point) for point in point_set]
    permutations = _own_group(SymmetricGroup(backend_points))
    permutation_representation = group_homset(group, permutations)(
        {
            group_generator: _permutation_from_point_map(
                permutations,
                point_set,
                lambda point, group_generator=group_generator: action(group_generator, point),
            )
            for group_generator in group.group_generators()
        }
    )
    return object_of(
        FiniteGSets(permutation_representation.domain()),
        point_set=point_set,
        permutation_representation=permutation_representation,
    )


def finite_g_set(point_set, group, action):
    r"""Return the finite owned ``G``-set defined by ``action(g,x)``."""
    return _finite_g_set_from_action(group, point_set, action)


def trivial_g_set(point_set, group):
    r"""Equip a finite set with the trivial ``group``-action."""
    return finite_g_set(point_set, group, lambda _group_element, point: point)


def fixed_point_set(g_set):
    r"""Return the finite fixed-point set ``X^G``."""
    group = g_set.acting_group()
    assert group.is_finitely_generated() is True, (
        "constructing fixed points requires a chosen finite group generating set"
    )
    return finite_ordered_filter(finite_ordered_set(g_set), g_set.is_invariant)


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

        def transporter(self, source, target):
            r"""Return the unique group element carrying ``source`` to ``target`` when computable."""
            return Unknown


__all__ = [
    "FiniteGSets",
    "GSetHomset",
    "GSetMorphism",
    "GSets",
    "OrbitSets",
    "Torsors",
    "finite_g_set",
    "fixed_point_set",
    "g_set_homset",
    "trivial_g_set",
]
