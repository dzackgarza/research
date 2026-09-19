r"""Owned topological spaces and continuous maps.

A topological space is a set together with a topology; a morphism is a
continuous set map.  The general public constructor implemented here is the
exact finite case, where the topology axioms and continuity are decidable by
enumeration.  Infinite geometric realizations (manifolds and scheme
underlying spaces) supply private topology data to this same owner and may
assert at the computational frontier when arbitrary openness is not
represented.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.structure.element import parent as element_parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    _precomposable,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    FiniteSets,
    Sets,
)
from dzack_research.preamble.owned_category import _object_of


def _members_of_subset(base_set, candidate):
    r"""The members of ``candidate <= base_set`` in the order of ``base_set``."""

    subset = base_set.power_set()(candidate)
    return tuple(point for point in base_set if point in subset)


class _FiniteTopologyData(SageObject):
    r"""The exact topology on a finite enumerated set, retained by its opens."""

    def __init__(self, point_set, open_subsets) -> None:
        assert point_set in FiniteSets() and point_set in EnumeratedSets(), (
            "the explicit topology constructor currently verifies a finite enumerated point set"
        )
        opens = []
        for candidate in open_subsets:
            members = _members_of_subset(point_set, candidate)
            if members not in opens:
                opens.append(members)
        self._point_set = point_set
        self._open_member_families = tuple(opens)
        self._verify_topology_axioms()

    def point_set(self):
        return self._point_set

    def _union(self, left, right):
        return tuple(
            point
            for point in self.point_set()
            if point in left or point in right
        )

    def _intersection(self, left, right):
        return tuple(
            point
            for point in self.point_set()
            if point in left and point in right
        )

    def _verify_topology_axioms(self) -> None:
        opens = self._open_member_families
        empty = ()
        whole = tuple(self.point_set())
        if empty not in opens or whole not in opens:
            raise ValueError("a topology contains the empty set and the whole space")
        for left in opens:
            for right in opens:
                if self._intersection(left, right) not in opens:
                    raise ValueError("the selected opens are not closed under finite intersections")
                if self._union(left, right) not in opens:
                    raise ValueError("the selected opens are not closed under unions")

    def open_subsets(self, space):
        power = space.power_set()
        return finite_ordered_set(
            tuple(power(members) for members in self._open_member_families)
        )

    def is_open_subset(self, space, candidate) -> bool:
        members = _members_of_subset(space, candidate)
        return members in self._open_member_families


class _FiniteTopologicalSpaceEngine:
    r"""A finite topological space realized on an already owned finite set."""

    def __init__(self, point_set, topology_data, **rest) -> None:
        self._unstructured_set = point_set
        super().__init__(topology_data=topology_data, facade=True, **rest)

    def unstructured_set(self):
        r"""The set on which this selected topology was placed."""
        return self._unstructured_set

    underlying_set = unstructured_set

    def __contains__(self, point) -> bool:
        return point in self.unstructured_set()

    is_parent_of = __contains__

    def _element_constructor_(self, point):
        return self.unstructured_set()(point)

    def __iter__(self):
        return iter(self.unstructured_set())

    def cardinality(self):
        return self.unstructured_set().cardinality()


class ContinuousMap(Morphism):
    r"""A continuous map, retaining its underlying set morphism."""

    def __init__(self, parent, set_morphism) -> None:
        Morphism.__init__(self, parent)
        if (
            set_morphism.domain() is not self.domain()
            or set_morphism.codomain() is not self.codomain()
        ):
            raise ValueError("a continuous map has the wrong underlying set-map endpoints")
        self._set_morphism = set_morphism

    def underlying_set_morphism(self):
        return self._set_morphism

    def __call__(self, point):
        return self.underlying_set_morphism()(point)

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        hom = TopologicalSpaces().Mor(other.domain(), self.codomain())
        return hom._from_continuous_set_map(
            self.underlying_set_morphism()
            * other.underlying_set_morphism()
        )

    def __eq__(self, other) -> bool:
        return (
            element_parent(other) is self.parent()
            and other.underlying_set_morphism() == self.underlying_set_morphism()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None


class TopologicalSpaceHomset(CategoricalHomset):
    r"""Continuous maps between two represented topological spaces."""

    Element = ContinuousMap

    def _verify_continuity(self, set_morphism) -> None:
        target_opens = self.codomain().open_subsets()
        assert target_opens in FiniteSets() and target_opens in EnumeratedSets(), (
            "continuity of an arbitrary represented map is currently decided when the target topology has finitely enumerable opens"
        )
        source_power = self.domain().power_set()
        for open_subset in target_opens:
            inverse_image = source_power.from_predicate(
                lambda point, selected=open_subset: set_morphism(point) in selected
            )
            if self.domain().is_open_subset(inverse_image) is not True:
                raise ValueError("the supplied set map is not continuous")

    def _element_constructor_(self, datum):
        if element_parent(datum) is self:
            return datum
        set_morphism = Sets().Mor(self.domain(), self.codomain())(datum)
        self._verify_continuity(set_morphism)
        return self.element_class(self, set_morphism)

    def _from_continuous_set_map(self, set_morphism):
        r"""Construct a map whose continuity follows from a categorical theorem.

        Used only by identity and composition: no arbitrary caller datum enters
        through this route.
        """
        return self.element_class(self, set_morphism)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on one topological space")
        return self._from_continuous_set_map(
            Sets().Mor(self.domain(), self.domain()).identity()
        )


class TopologicalSpaceHomCategoryConstruction(HomCategoryConstruction):
    r"""The Hom family of topological spaces."""

    def fixed_category_class(self):
        return TopologicalSpaceHomset


class TopologicalSpaces(OwnedCategory):
    r"""Sets equipped with a topology, with continuous maps as morphisms."""

    _HomCategory = TopologicalSpaceHomCategoryConstruction

    def super_categories(self):
        return [Sets()]

    def an_object(self):
        r"""The Sierpiński two-point space."""
        points = Sets.Δ[1]
        return self(points, ((), (points(1),), points))

    def _call_(self, point_set, open_subsets):
        r"""Construct an exact finite topology on ``point_set``."""
        point_set = Sets()(point_set)
        topology_data = _FiniteTopologyData(point_set, open_subsets)
        return _object_of(
            self,
            _engine=(self, _FiniteTopologicalSpaceEngine, None),
            point_set=point_set,
            topology_data=topology_data,
        )

    @classmethod
    def _repr_object_names(cls):
        return "topological spaces"

    class ParentMethods:
        def __init__(self, topology_data, **rest) -> None:
            self._represented_topology_data = topology_data
            super().__init__(**rest)

        def _topology_data(self):
            return self._represented_topology_data

        def open_subsets(self):
            r"""The set of open subsets defining this topology."""
            return self._topology_data().open_subsets(self)

        topology = open_subsets

        def is_open_subset(self, subset) -> bool:
            r"""Whether ``subset`` is open in this topology."""
            return self._topology_data().is_open_subset(self, subset)

        def continuous_map(self, codomain, map_):
            return self.Mor(codomain)(map_)


__all__ = [
    "ContinuousMap",
    "TopologicalSpaceHomset",
    "TopologicalSpaces",
]
