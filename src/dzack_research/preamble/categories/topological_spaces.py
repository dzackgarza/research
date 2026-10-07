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

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
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
            f"cannot check the topology axioms for a topology on {point_set}: they are "
            f"checked only for a finite enumerated set of points, and {point_set} is in "
            f"{point_set.category()}"
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
            raise ValueError(
                f"the subsets {opens} of {self.point_set()} are not a topology: a topology "
                f"must contain the empty set and the whole space"
            )
        for left in opens:
            for right in opens:
                if self._intersection(left, right) not in opens:
                    raise ValueError(
                        f"the subsets {opens} of {self.point_set()} are not a topology: the "
                        f"intersection of the open sets {left} and {right} is not open"
                    )
                if self._union(left, right) not in opens:
                    raise ValueError(
                        f"the subsets {opens} of {self.point_set()} are not a topology: the "
                        f"union of the open sets {left} and {right} is not open"
                    )

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

    def _element_constructor_(self, point):
        return self.unstructured_set()(point)

    def __iter__(self):
        return iter(self.unstructured_set())

    def _cardinality_decision(self):
        return self.unstructured_set().cardinality()


class ContinuousMap:
    r"""A continuous map, retaining its underlying set morphism."""

    def __init__(self, parent, set_morphism) -> None:
        if (
            set_morphism.domain() is not parent.domain()
            or set_morphism.codomain() is not parent.codomain()
        ):
            raise ValueError(
                f"{set_morphism} cannot underlie a continuous map {parent.domain()} -> "
                f"{parent.codomain()}: it is a map {set_morphism.domain()} -> "
                f"{set_morphism.codomain()}"
            )
        self._set_morphism = set_morphism
        super().__init__(parent, set_morphism)

    def underlying_set_morphism(self):
        return self._set_morphism

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        mor = TopologicalSpaces().Mor(other.domain(), self.codomain())
        return mor._from_continuous_set_map(
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


class TopologicalSpaceMor(CategoricalMor):
    r"""``Mor_Top(X, Y)``: the subset of ``Mor_Set(UX, UY)`` of the continuous maps.

    The forgetful functor ``U: Top -> Set`` is faithful, so a continuous map
    ``X -> Y`` is a set map ``UX -> UY`` with a property: the preimage of each
    open set of ``Y`` is open in ``X``.  The supercategory of this Mor is
    ``Mor_Set(X, Y)`` (``CategoricalMor.super_categories``), and a set map of
    the underlying sets lies in it exactly when it is continuous (``CON-17``).

    The underlying set ``UX`` has two parents: ``X`` itself, an object of
    ``Sets()``, and the point set ``X.underlying_set()`` that its topology was
    placed on.  ``X`` is a facade over that point set, so the two parents have
    the same points, and a set map out of either is a map of ``UX``.
    """

    ElementMethods = ContinuousMap

    def _presents_underlying_set(self, space, candidate) -> bool:
        r"""Whether the set ``candidate`` is ``U(space)``, by one of its two parents."""
        return candidate is space or candidate is space.underlying_set()

    def _is_map_of_underlying_sets(self, arrow) -> bool:
        r"""Whether ``arrow`` is a set map ``UX -> UY`` for the endpoints of this Mor."""
        domain = arrow.domain()
        codomain = arrow.codomain()
        return (
            self._presents_underlying_set(self.domain(), domain)
            and self._presents_underlying_set(self.codomain(), codomain)
            and arrow in Sets().Mor(domain, codomain)
        )

    def _preimages_of_opens_are_open(self, set_map) -> bool:
        r"""Continuity of ``set_map: UX -> UY``, decided from its definition.

        For each open set ``V`` of ``Y``, the preimage ``f^{-1}(V)`` is formed
        as a subset of ``X``, and ``X`` is asked whether it is open.
        """
        target_opens = self.codomain().open_subsets()
        assert target_opens in FiniteSets() and target_opens in EnumeratedSets(), (
            f"cannot decide whether {set_map} is continuous: continuity is decided "
            f"here only when the topology of the codomain {self.codomain()} has a finite "
            f"enumerated set of open sets, and its open sets are in {target_opens.category()}"
        )
        source_power = self.domain().power_set()
        return all(
            self.domain().is_open_subset(
                source_power.from_predicate(
                    lambda point, selected=open_subset: set_map(point) in selected
                )
            )
            is True
            for open_subset in target_opens
        )

    def accepts(self, arrow) -> bool:
        r"""Membership: a continuous map ``X -> Y``, or a continuous set map ``UX -> UY``."""
        if self._already_parented_arrow(arrow):
            return True
        return self._is_map_of_underlying_sets(arrow) and self._preimages_of_opens_are_open(arrow)

    def _element_constructor_(self, datum):
        r"""A continuous map, given by a set map ``UX -> UY`` or by a function on points.

        The datum is read as a set map in ``Mor_Set(X, Y)`` and admitted by
        continuity, the condition that cuts this subset out of it.
        """
        if element_parent(datum) is self:
            return datum
        maps = Sets().Mor(self.domain(), self.codomain())
        match datum:
            case Morphism() if (
                element_parent(datum) is not maps and self._is_map_of_underlying_sets(datum)
            ):
                set_morphism = maps(lambda point: datum(point))
            case _:
                set_morphism = maps(datum)
        if not self._preimages_of_opens_are_open(set_morphism):
            raise ValueError(
                f"{set_morphism} is not continuous from {self.domain()} to {self.codomain()}: "
                f"the preimage of an open set of {self.codomain()} is not open in {self.domain()}"
            )
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
            raise ValueError(
                f"there is no identity map from {self.domain()} to {self.codomain()}: an "
                f"identity needs its domain and codomain to be the same topological space"
            )
        return self._from_continuous_set_map(
            Sets().Mor(self.domain(), self.domain()).identity()
        )

    def _repr_(self):
        return f"Mor_Top({self.domain()}, {self.codomain()})"


class TopologicalSpaceMorCategoryConstruction(MorCategoryConstruction):
    r"""The Mor family of topological spaces."""

    def fixed_category_class(self):
        return TopologicalSpaceMor


class TopologicalSpaces(OwnedCategory):
    r"""Sets equipped with a topology, with continuous maps as morphisms."""

    _MorCategory = TopologicalSpaceMorCategoryConstruction

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

        def Mor(self, codomain, category=None):
            r"""Return the continuous maps into ``codomain``.

            Naming a coarser category is the explicit request to forget the
            topology, as in ``X.Mor(Y, category=Sets())``.
            """
            spaces = TopologicalSpaces()
            if category is None or category.is_subcategory(spaces):
                return spaces.Mor(self, codomain)
            return super().Mor(codomain, category=category)

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

        def integral_singular_cohomology(self, degree):
            r"""``H^degree(X; ZZ)``, the singular cohomology of this space with integer coefficients.

            A realization that computes the group supplies this method; the
            spaces without such a realization stop here.
            """
            assert False, (
                f"the integral singular cohomology H^{degree}({self}; ZZ) is computed only for the "
                "complex realizations of projective spaces, smooth complete toric varieties and "
                "smooth projective complete intersections over QQ"
            )

        def betti_number(self, degree):
            r"""``b_k(X) = rank H^k(X; ZZ)``, the ``k``-th Betti number.

            Hatcher, *Algebraic Topology* [Hat02], §2.2 (before Thm. 2.44),
            defines ``b_k`` as the rank of ``H_k(X; ZZ)``.  When ``H_k`` and
            ``H_{k-1}`` are finitely generated, Cor. 3.3 (universal
            coefficients) gives ``H^k = H_k / T_k + T_{k-1}`` with ``T`` the
            torsion, so ``H^k`` and ``H_k`` have the same rank.
            """
            return self.integral_singular_cohomology(degree).module_rank()

        def euler_characteristic(self):
            r"""``chi(X) = sum_k (-1)^k b_k(X)``.

            Hatcher [Hat02], Thm. 2.44: for a finite CW complex ``X``,
            ``chi(X) = sum_n (-1)^n rank H_n(X)``.  The sum runs over the
            degrees up to the dimension of a finite CW complex homotopy
            equivalent to ``X``, which the realization states in
            :meth:`_finite_cw_dimension`.  The sum is the contraction of the
            Betti vector ``(b_0, ..., b_d)`` with the covector
            ``((-1)^0, ..., (-1)^d)``.
            """
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
            from dzack_research.preamble.tensors import tensor
            from sage.rings.integer_ring import ZZ as SageZZ

            integers = _own_ring(SageZZ)
            degrees = range(int(self._finite_cw_dimension()) + 1)
            betti_vector = tensor.vector(
                integers, [integers(int(self.betti_number(degree))) for degree in degrees]
            )
            alternating_signs = tensor.covector(
                integers, [integers((-1) ** degree) for degree in degrees]
            )
            return alternating_signs.contract(betti_vector)

        def _finite_cw_dimension(self):
            r"""A bound ``d`` with ``X`` homotopy equivalent to a finite CW complex of dimension ``<= d``.

            Protected contract of :class:`TopologicalSpaces`.  The owner is
            this category; a realization engine that knows a finite CW
            structure up to homotopy overrides it and returns a Python
            ``int``.  The only caller is :meth:`euler_characteristic`, which
            needs the degrees where ``H^k`` can be nonzero.  A space without
            such a statement stops here.
            """
            assert False, (
                f"{self} is not known to have the homotopy type of a finite CW complex, so its "
                "Euler characteristic is not defined by Hatcher, Thm. 2.44"
            )


__all__ = [
    "ContinuousMap",
    "TopologicalSpaceMor",
    "TopologicalSpaces",
]
