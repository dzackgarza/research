r"""Diagrams, cones, cocones, and selected finite product constructions."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.unknown import Unknown, UnknownClass
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.element import parent
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.cat import Cat, _FunctorCategory
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    _category_hom,
    _category_homset,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects as OwnedObjects
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor, NaturalTransformation
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import FiniteSets, Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import Category as OwnedCategoryBase


class _DiagramCategory(_FunctorCategory):
    r"""The functor category ``[J,C]`` of diagrams of one shape."""

    @staticmethod
    @cached_function(key=lambda cls, index_category, target_category: (cls, id(index_category), id(target_category)))
    def __classcall__(cls, index_category: Category, target_category: Category):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(index_category, target_category)
        return typecall(cls, index_category, target_category)

    def __init__(self, index_category: Category, target_category: Category) -> None:
        super().__init__(Cat(), index_category, target_category)

    def index_category(self) -> Category:
        return self.domain_category()

    def target_category(self) -> Category:
        return self.codomain_category()

    def super_categories(self):
        return [Cat().Mor(self.index_category(), self.target_category())]


class DirectedSystem(_DiagramCategory):
    r"""A diagram category whose index category represents a directed order."""


class InverseSystem(_DiagramCategory):
    r"""The diagram category ``[J^op,C]`` for inverse systems indexed by ``J``."""

    def __init__(self, index_category: Category, target_category: Category) -> None:
        self._base_index_category = index_category
        super().__init__(index_category.opposite(), target_category)

    def base_index_category(self) -> Category:
        r"""Return ``J`` when this inverse system category is ``[J^op,C]``."""
        return self._base_index_category


class PosetMorphism(Morphism):
    r"""The unique arrow ``p -> q`` of a thin poset category when ``p <= q``."""

    def __init__(self, parent) -> None:
        Morphism.__init__(self, parent)

    def __mul__(self, other):
        match other:
            case PosetMorphism() if other.codomain() is self.domain():
                return self.parent().poset_category().Mor(other.domain(), self.codomain()).unique()
            case _:
                return NotImplemented

    def __eq__(self, other) -> bool:
        return parent(other) is self.parent()

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(id(self.parent()))


class PosetHomset(CategoricalHomset):
    Element = PosetMorphism

    def poset_category(self):
        return self.base_category()

    def cardinality(self):
        category = self.poset_category()
        return cardinal(
            1
            if category.le(self.domain().value(), self.codomain().value())
            else 0
        )

    @cached_method
    def unique(self):
        if self.cardinality() != cardinal(1):
            raise ValueError("there is no arrow between these incomparable poset objects")
        return PosetMorphism(self)

    def _element_constructor_(self, value=None):
        if value is not None and value is not self.unique():
            raise ValueError("a poset Hom-set has at most one arrow")
        return self.unique()

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity requires one object")
        return self.unique()


class PosetHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = PosetHomset


class PosetCategory(OwnedCategory):
    r"""The thin category attached to an owned partially ordered set ``P``.

    Objects are the points of ``P`` and there is one arrow ``p -> q`` exactly
    when ``p <= q``.  The object family is lazy, so an infinite poset remains
    an infinite represented indexing category rather than an eagerly traversed
    sequence.  ``le`` may be supplied when the owned set carries its order only
    by construction rather than by element comparison.
    """

    _HomCategory = PosetHomCategoryConstruction

    class ParentMethods:
        def __init__(self, value, **rest) -> None:
            self._value = value
            super().__init__(**rest)

        def value(self):
            return self._value

        def _repr_(self) -> str:
            return repr(self.value())

    def __init__(self, ordered_set, le=None) -> None:
        if ordered_set not in Sets():
            raise TypeError("a poset category requires an owned set of indices")
        self._ordered_set = ordered_set
        self._le = le
        self._objects = indexed_family(
            ordered_set,
            lambda value: _object_of(self, value=value),
            name=f"Objects of the poset category on {ordered_set}",
        )
        super().__init__()

    def _make_named_class_key(self, name):
        return self._ordered_set, self._le

    def super_categories(self):
        return [OwnedObjects()]

    def object_set(self):
        return self._ordered_set

    def objects(self):
        return self._objects

    def __call__(self, value):
        return self._objects(self._ordered_set(value))

    def le(self, left, right) -> bool:
        left = self._ordered_set(left)
        right = self._ordered_set(right)
        if self._le is not None:
            return bool(self._le(left, right))
        return bool(left <= right)

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a poset Hom requires objects of this category")
        return self.HomCategory().Of(domain, codomain)

    def identity(self, obj):
        return self.Mor(obj, obj).identity()

    @cached_method
    def arrows(self):
        assert self.object_set() in FiniteSets(), (
            "arrow enumeration for a poset category requires a finite represented object set; "
            "an infinite poset is represented by its order relation instead"
        )
        return finite_ordered_set(
            tuple(
                self.Mor(self(left), self(right)).unique()
                for left in self.object_set()
                for right in self.object_set()
                if self.le(left, right)
            )
        )


class FiniteOrdinalMorphism(Morphism):
    r"""The unique arrow ``i -> j`` in a finite ordinal category when ``i <= j``."""

    def __init__(self, parent) -> None:
        Morphism.__init__(self, parent)

    def __mul__(self, other):
        match other:
            case FiniteOrdinalMorphism() if other.codomain() is self.domain():
                return self.parent().ordinal_category().Mor(other.domain(), self.codomain()).unique()
            case _:
                return NotImplemented

    def __eq__(self, other) -> bool:
        return parent(other) is self.parent()

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(id(self.parent()))


class FiniteOrdinalHomset(CategoricalHomset):
    Element = FiniteOrdinalMorphism

    def ordinal_category(self):
        return self.base_category()

    def cardinality(self):
        return cardinal(1 if self.domain().position() <= self.codomain().position() else 0)

    @cached_method
    def unique(self):
        if self.cardinality() != cardinal(1):
            raise ValueError("there is no arrow in the decreasing direction of a finite ordinal")
        return FiniteOrdinalMorphism(self)

    def _element_constructor_(self, value=None):
        if value is not None and value is not self.unique():
            raise ValueError("a finite-ordinal Hom-set has at most one arrow")
        return self.unique()

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity requires one object")
        return self.unique()


class FiniteOrdinalHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = FiniteOrdinalHomset


class FiniteOrdinalCategory(OwnedCategory):
    r"""The category attached to the finite total order ``0 < ... < n-1``."""

    _HomCategory = FiniteOrdinalHomCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, size: (cls, int(size)))
    def __classcall__(cls, size):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(size)
        return typecall(cls, size)

    class ParentMethods:
        def __init__(self, position, **rest) -> None:
            self._position = int(position)
            super().__init__(**rest)

        def position(self) -> int:
            return self._position

        def _repr_(self) -> str:
            return str(self.position())

    def __init__(self, size) -> None:
        size = int(size)
        if size < 0:
            raise ValueError("a finite ordinal category has nonnegative size")
        self._object_set = Sets.Δ[size - 1]
        self._objects = indexed_family(
            self._object_set,
            lambda position: _object_of(self, position=int(position)),
            name="Objects of a finite ordinal category",
        )
        super().__init__()

    def super_categories(self):
        return [OwnedObjects()]

    def object_set(self):
        return self._object_set

    def objects(self):
        return self._objects

    def __call__(self, position):
        return self._objects(self._object_set(position))

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a finite-ordinal Hom requires objects of this category")
        return self.HomCategory().Of(domain, codomain)

    def identity(self, obj):
        return self.Mor(obj, obj).identity()

    @cached_method
    def arrows(self):
        return finite_ordered_set(
            tuple(
                self.Mor(self(i), self(j)).unique()
                for i in self.object_set()
                for j in self.object_set()
                if int(i) <= int(j)
            )
        )


class FiniteSequenceDiagram(Functor):
    r"""A finite composable sequence, with all composites derived from its transitions."""

    def __init__(self, objects, transitions, target_category: Category) -> None:
        self._objects = tuple(objects)
        self._transitions = tuple(transitions)
        if len(self._transitions) != max(0, len(self._objects) - 1):
            raise ValueError("a finite sequence has one transition between consecutive objects")
        if any(obj not in target_category for obj in self._objects):
            raise TypeError("every finite-sequence object must lie in the target category")
        for position, transition in enumerate(self._transitions):
            if (
                transition.domain() is not self._objects[position]
                or transition.codomain() is not self._objects[position + 1]
            ):
                raise ValueError("a finite-sequence transition has the wrong consecutive endpoints")
        self._shape = FiniteOrdinalCategory(len(self._objects))
        super().__init__(self._shape, target_category)

    def objects(self):
        return indexed_family(
            self.domain().object_set(),
            lambda position: self._objects[int(position)],
            name="Objects of a finite sequence diagram",
        )

    def transitions(self):
        labels = Sets.Δ[len(self._transitions) - 1]
        return indexed_family(
            labels,
            lambda position: self._transitions[int(position)],
            name="Transitions of a finite sequence diagram",
        )

    def _apply_object(self, obj):
        return self._objects[obj.position()]

    def _apply_morphism(self, morphism):
        source = morphism.domain().position()
        target = morphism.codomain().position()
        if source == target:
            image = self._objects[source]
            return _category_homset(self.codomain(), image, image).identity()
        composite = self._transitions[source]
        for position in range(source + 1, target):
            composite = self._transitions[position] * composite
        return composite


class ParallelPairMorphism(Morphism):
    r"""One arrow of the walking parallel-pair category ``0 ⇉ 1``."""

    def __init__(self, parent, name: str) -> None:
        Morphism.__init__(self, parent)
        self._name = name

    def name(self) -> str:
        return self._name

    def is_identity(self) -> bool:
        return self.domain() is self.codomain()

    def __mul__(self, other):
        match other:
            case ParallelPairMorphism() if other.codomain() is self.domain():
                pass
            case _:
                return NotImplemented
        if self.is_identity():
            return other
        if other.is_identity():
            return self
        raise ValueError("the walking parallel pair has no composite of two nonidentity arrows")

    def __eq__(self, other) -> bool:
        return parent(other) is self.parent() and other.name() == self.name()

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), self.name()))


class ParallelPairHomset(CategoricalHomset):
    Element = ParallelPairMorphism

    def __init__(self, family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, family, domain, codomain)

    def parallel_pair_category(self):
        return self.base_category()

    def cardinality(self):
        category = self.parallel_pair_category()
        if self.domain() is self.codomain():
            return cardinal(1)
        if self.domain() is category.source() and self.codomain() is category.target():
            return cardinal(2)
        return cardinal(0)

    def _element_constructor_(self, name=None):
        category = self.parallel_pair_category()
        if self.domain() is self.codomain():
            if name not in (None, "identity"):
                raise ValueError("an endomorphism of the walking parallel pair is its identity")
            return ParallelPairMorphism(self, "identity")
        if self.domain() is category.source() and self.codomain() is category.target():
            if name not in ("left", "right"):
                raise ValueError("the two parallel arrows are named 'left' and 'right'")
            return ParallelPairMorphism(self, name)
        raise ValueError("the walking parallel pair has no arrow from 1 to 0")

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity requires one object")
        return self()


class ParallelPairHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = ParallelPairHomset


class ParallelPairCategory(OwnedCategory):
    r"""The walking parallel pair ``0 ⇉ 1``."""

    _HomCategory = ParallelPairHomCategoryConstruction

    class ParentMethods:
        def __init__(self, position, **rest) -> None:
            self._position = int(position)
            super().__init__(**rest)

        def position(self) -> int:
            return self._position

        def _repr_(self) -> str:
            return str(self.position())

    def __init__(self) -> None:
        self._positions = finite_ordered_set((0, 1))
        self._objects = indexed_family(
            self._positions,
            lambda position: _object_of(self, position=position),
            name="Objects of the walking parallel pair",
        )
        super().__init__()

    def super_categories(self):
        return [OwnedObjects()]

    def object_set(self):
        return self._positions

    def objects(self):
        return self._objects

    def source(self):
        return self._objects[0]

    def target(self):
        return self._objects[1]

    def __call__(self, position):
        return self._objects[int(position)]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a walking-parallel-pair Hom requires its owned objects")
        return self.HomCategory().Of(domain, codomain)

    @cached_method
    def left(self):
        return self.Mor(self.source(), self.target())("left")

    @cached_method
    def right(self):
        return self.Mor(self.source(), self.target())("right")

    def identity(self, obj):
        return self.Mor(obj, obj).identity()


class ParallelPairDiagram(Functor):
    r"""A diagram ``A ⇉ B`` retaining its two parallel arrows."""

    def __init__(self, left: Morphism, right: Morphism, target_category: Category) -> None:
        if left.domain() is not right.domain() or left.codomain() is not right.codomain():
            raise ValueError("a parallel-pair diagram requires parallel arrows")
        self._left = left
        self._right = right
        self._shape = ParallelPairCategory()
        super().__init__(self._shape, target_category)

    def left(self):
        return self._left

    def right(self):
        return self._right

    def source_object(self):
        return self.left().domain()

    def target_object(self):
        return self.left().codomain()

    def _apply_object(self, obj):
        if obj is self.domain().source():
            return self.source_object()
        if obj is self.domain().target():
            return self.target_object()
        raise ValueError("the object is not in the walking parallel pair")

    def _apply_morphism(self, morphism):
        if morphism.is_identity():
            image = self(morphism.domain())
            return _category_homset(self.codomain(), image, image).identity()
        if morphism.name() == "left":
            return self.left()
        if morphism.name() == "right":
            return self.right()
        raise ValueError("unknown arrow of the walking parallel pair")


@cached_function
def _parallel_pair_diagram(left: Morphism, right: Morphism, target_category: Category) -> ParallelPairDiagram:
    r"""Return the selected diagram object for one represented parallel pair.

    Equalizers and coequalizers of the same two arrows have the same source
    diagram ``A ⇉ B``.  Retaining one diagram object lets a natural
    transformation of that diagram induce both universal maps without
    manufacturing a second, merely isomorphic indexing presentation.
    """
    return ParallelPairDiagram(left, right, target_category)


class RestrictedDiagram(Functor):
    r"""The precomposition ``D ∘ u`` retaining ``D`` and the indexing functor ``u``."""

    def __init__(self, diagram: Functor, indexing_functor: Functor) -> None:
        if indexing_functor.codomain() is not diagram.domain():
            raise ValueError("a diagram restriction precomposes by a functor into the index category")
        self._diagram = diagram
        self._indexing_functor = indexing_functor
        super().__init__(indexing_functor.domain(), diagram.codomain())

    def original_diagram(self):
        return self._diagram

    def indexing_functor(self):
        return self._indexing_functor

    def _apply_object(self, obj):
        return self.original_diagram()(self.indexing_functor()(obj))

    def _apply_morphism(self, morphism):
        return self.original_diagram()(self.indexing_functor()(morphism))

class SelectedLimitConstruction(SageObject):
    r"""A selected universal cone over one represented diagram."""

    def __init__(self, diagram, universal_cone, factorizer) -> None:
        if universal_cone.diagram() is not diagram:
            raise ValueError("a selected limit retains a cone over its own diagram")
        self._diagram = diagram
        self._universal_cone = universal_cone
        self._factorizer = factorizer

    def diagram(self):
        return self._diagram

    def cone(self):
        return self._universal_cone

    def object(self):
        return self.cone().apex()

    apex = object

    def structure_morphism(self, index):
        return self.cone().structure_morphism(index)

    def factor(self, cone):
        if cone.diagram() is not self.diagram():
            raise ValueError("the cone to factor must lie over this construction's diagram")
        apex_map = self._factorizer(cone)
        return (self.diagram()).Cones().Mor(cone, self.cone())(apex_map)

    def induced_map(self, transformation, target_construction):
        r"""Return the map on selected limits induced by ``D -> E``."""
        if transformation.source() is not self.diagram():
            raise ValueError("the natural transformation must start at this limit's diagram")
        if transformation.target() is not target_construction.diagram():
            raise ValueError("the natural transformation must end at the target limit's diagram")
        target_diagram = target_construction.diagram()
        induced_cone = (target_diagram).Cones().cone(
            self.object(),
            lambda index: (
                transformation.component(index) * self.structure_morphism(index)
            ),
        )
        return target_construction.factor(induced_cone).apex_map()


class SelectedColimitConstruction(SageObject):
    r"""A selected universal cocone under one represented diagram."""

    def __init__(self, diagram, universal_cocone, factorizer) -> None:
        if universal_cocone.diagram() is not diagram:
            raise ValueError("a selected colimit retains a cocone under its own diagram")
        self._diagram = diagram
        self._universal_cocone = universal_cocone
        self._factorizer = factorizer

    def diagram(self):
        return self._diagram

    def cocone(self):
        return self._universal_cocone

    def object(self):
        return self.cocone().apex()

    apex = object

    def costructure_morphism(self, index):
        return self.cocone().costructure_morphism(index)

    def factor(self, cocone):
        if cocone.diagram() is not self.diagram():
            raise ValueError("the cocone to factor must lie under this construction's diagram")
        apex_map = self._factorizer(cocone)
        return (self.diagram()).Cocones().Mor(self.cocone(), cocone)(apex_map)

    def induced_map(self, transformation, target_construction):
        r"""Return the map on selected colimits induced by ``D -> E``."""
        if transformation.source() is not self.diagram():
            raise ValueError("the natural transformation must start at this colimit's diagram")
        if transformation.target() is not target_construction.diagram():
            raise ValueError("the natural transformation must end at the target colimit's diagram")
        source_diagram = self.diagram()
        induced_cocone = (source_diagram).Cocones().cocone(
            target_construction.object(),
            lambda index: (
                target_construction.costructure_morphism(index)
                * transformation.component(index)
            ),
        )
        return self.factor(induced_cocone).apex_map()




def _commutes_with_diagram(source, target, apex_map, cocone=False) -> bool:
    for index in source.diagram().domain().objects():
        if cocone:
            left = apex_map * source.costructure_morphism(index)
            right = target.costructure_morphism(index)
        else:
            left = target.structure_morphism(index) * apex_map
            right = source.structure_morphism(index)
        if (left == right) is not True:
            return False
    return True


class ConeMorphism(Morphism):
    r"""A morphism of cones, determined by its apex map."""

    def __init__(self, parent: ConeHomset, apex_map: Morphism, *, verify: bool = True) -> None:
        Morphism.__init__(self, parent)
        if apex_map.domain() is not self.domain().apex():
            raise ValueError("the cone map has the wrong domain apex")
        if apex_map.codomain() is not self.codomain().apex():
            raise ValueError("the cone map has the wrong codomain apex")
        if apex_map not in _category_hom(
            parent.cone_category().target_category(), self.domain().apex(), self.codomain().apex()
        ):
            raise ValueError("the apex map is not a morphism of the diagram's target category")
        if verify and not _commutes_with_diagram(self.domain(), self.codomain(), apex_map):
            raise ValueError("the apex map does not commute with the cone legs")
        self._apex_map = apex_map

    def apex_map(self) -> Morphism:
        return self._apex_map

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        if parent(other) is not self.parent():
            return False
        return self.apex_map() == other.apex_map()

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        match other:
            case ConeMorphism() if other.codomain() is self.domain():
                pass
            case _:
                return NotImplemented
        # Each leg satisfies r_i g = q_i and q_i f = p_i, hence r_i(gf)=p_i.
        parent = self.parent().cone_category().Mor(other.domain(), self.codomain())
        return ConeMorphism(
            parent, self.apex_map() * other.apex_map(), verify=False
        )


class CoconeMorphism(Morphism):
    r"""A morphism of cocones, determined by its apex map."""

    def __init__(self, parent: CoconeHomset, apex_map: Morphism, *, verify: bool = True) -> None:
        Morphism.__init__(self, parent)
        if apex_map.domain() is not self.domain().apex():
            raise ValueError("the cocone map has the wrong domain apex")
        if apex_map.codomain() is not self.codomain().apex():
            raise ValueError("the cocone map has the wrong codomain apex")
        if apex_map not in _category_hom(
            parent.cocone_category().target_category(), self.domain().apex(), self.codomain().apex()
        ):
            raise ValueError("the apex map is not a morphism of the diagram's target category")
        if verify and not _commutes_with_diagram(
            self.domain(), self.codomain(), apex_map, cocone=True
        ):
            raise ValueError("the apex map does not commute with the cocone legs")
        self._apex_map = apex_map

    def apex_map(self) -> Morphism:
        return self._apex_map

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        if parent(other) is not self.parent():
            return False
        return self.apex_map() == other.apex_map()

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        match other:
            case CoconeMorphism() if other.codomain() is self.domain():
                pass
            case _:
                return NotImplemented
        # Dually, g q_i = r_i and f p_i = q_i imply (gf)p_i = r_i.
        parent = self.parent().cocone_category().Mor(other.domain(), self.codomain())
        return CoconeMorphism(
            parent, self.apex_map() * other.apex_map(), verify=False
        )


class ConeHomset(CategoricalHomset):
    Element = ConeMorphism

    def __init__(
        self,
        family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, domain, codomain
        )

    def cone_category(self) -> _ConeCategory:
        return self.base_category()

    def _element_constructor_(self, apex_map):
        match apex_map:
            case ConeMorphism():
                if apex_map.parent() is self:
                    return apex_map
                if apex_map.domain() is not self.domain() or apex_map.codomain() is not self.codomain():
                    raise ValueError("the cone morphism has the wrong endpoints")
                apex_map = apex_map.apex_map()
        return ConeMorphism(self, apex_map)

    def identity(self) -> ConeMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity requires one cone")
        apex = self.domain().apex()
        return ConeMorphism(
            self,
            _category_homset(self.cone_category().target_category(), apex, apex).identity(),
            verify=False,
        )


class CoconeHomset(CategoricalHomset):
    Element = CoconeMorphism

    def __init__(
        self,
        family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, domain, codomain
        )

    def cocone_category(self) -> _CoconeCategory:
        return self.base_category()

    def _element_constructor_(self, apex_map):
        match apex_map:
            case CoconeMorphism():
                if apex_map.parent() is self:
                    return apex_map
                if apex_map.domain() is not self.domain() or apex_map.codomain() is not self.codomain():
                    raise ValueError("the cocone morphism has the wrong endpoints")
                apex_map = apex_map.apex_map()
        return CoconeMorphism(self, apex_map)

    def identity(self) -> CoconeMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity requires one cocone")
        apex = self.domain().apex()
        return CoconeMorphism(
            self,
            _category_homset(self.cocone_category().target_category(), apex, apex).identity(),
            verify=False,
        )


class ConeHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = ConeHomset


class CoconeHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = CoconeHomset


class _ConeCategory(OwnedCategory):
    r"""The category of cones over one represented diagram.

    Unverified specimens test nonidentity maps of cones and cocones, including
    the identity on an object with nontrivial legs::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: labels = finite_ordered_set(("j",))
        sage: index = DiscreteCategory(labels)
        sage: points = finite_ordered_set(("a", "b"))
        sage: one = finite_ordered_set(("*",))
        sage: diagram = Cat().Mor(index, Sets()).constant_functor(one)
        sage: category = diagram.Cones()
        sage: leg = Sets().Mor(points, one)(lambda point: "*")
        sage: cone = category.cone(points, lambda obj: leg)
        sage: hom = category.Mor(cone, cone)
        sage: hom is category.HomCategory().Of(cone, cone)
        True
        sage: swap = Sets().Mor(points, points)(lambda point: "b" if point == "a" else "a")
        sage: hom(swap) * hom(swap) == hom.identity()
        True
        sage: cocones = diagram.Cocones()
        sage: leg = Sets().Mor(one, points)(lambda point: "a")
        sage: cocone = cocones.cocone(points, lambda obj: leg)
        sage: hom = cocones.Mor(cocone, cocone)
        sage: hom is cocones.HomCategory().Of(cocone, cocone)
        True
        sage: collapse = hom(Sets().Mor(points, points)(lambda point: "a"))
        sage: hom.identity() * collapse == collapse
        True
        sage: collapse * collapse == collapse
        True

    Unverified specimen: even an empty cone diagram does not make a
    non-morphism into a permitted apex map::

        sage: injections = Sets().WideSubcategory(Sets().MonomorphismArrowCategory())
        sage: empty_shape = DiscreteCategory(finite_ordered_set(()))
        sage: diagram = Cat().Mor(empty_shape, injections).constant_functor(points)
        sage: category = diagram.Cones()
        sage: cone = category.cone(points, lambda obj: injections.identity(points))
        sage: hom = category.Mor(cone, cone)
        sage: hom(swap).apex_map() is swap
        True
        sage: hom(Sets().Mor(points, points)(lambda point: "a"))
        Traceback (most recent call last):
        ...
        ValueError: the apex map is not a morphism of the diagram's target category
    """

    _HomCategory = ConeHomCategoryConstruction

    class ParentMethods:
        def __init__(
            self,
            apex: Parent,
            transformation: NaturalTransformation,
            **rest,
        ) -> None:
            self._apex = apex
            self._transformation = transformation
            super().__init__(**rest)

        def cone_category(self) -> _ConeCategory:
            return self.category()

        def diagram(self) -> Functor:
            return self.cone_category().diagram()

        def apex(self) -> Parent:
            return self._apex

        def transformation(self) -> NaturalTransformation:
            return self._transformation

        def structure_morphism(self, index: Parent) -> Morphism:
            return self.transformation().component(index)

        def structure_morphisms(self) -> IndexedFamily:
            domain = self.diagram().domain()
            return indexed_family(
                domain.object_set(),
                lambda label: self.structure_morphism(domain(label)),
                name=f"Structure morphisms of {self}",
            )

        def _repr_(self) -> str:
            return f"Cone with apex {self.apex()} over {self.diagram()}"

    def __init__(self, diagram: Functor) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self) -> Functor:
        return self._diagram

    def target_category(self) -> Category:
        return self.diagram().codomain()

    def super_categories(self):
        return [OwnedObjects()]

    def cone(
        self,
        apex: Parent,
        components: Callable[[Parent], Morphism],
    ) -> Parent:

        constant = Cat().Mor(
            self.diagram().domain(), self.target_category()
        ).constant_functor(apex)
        transformation = NaturalTransformation(constant, self.diagram(), components)
        return _object_of(self, apex=apex, transformation=transformation)

    def Mor(self, domain: Parent, codomain: Parent) -> ConeHomset:
        if domain not in self or codomain not in self:
            raise TypeError("a cone Hom requires two cones over the same diagram")
        return self.HomCategory().Of(domain, codomain)



class _CoconeCategory(OwnedCategory):
    r"""The category of cocones under one represented diagram."""

    _HomCategory = CoconeHomCategoryConstruction

    class ParentMethods:
        def __init__(
            self,
            apex: Parent,
            transformation: NaturalTransformation,
            **rest,
        ) -> None:
            self._apex = apex
            self._transformation = transformation
            super().__init__(**rest)

        def cocone_category(self) -> _CoconeCategory:
            return self.category()

        def diagram(self) -> Functor:
            return self.cocone_category().diagram()

        def apex(self) -> Parent:
            return self._apex

        def transformation(self) -> NaturalTransformation:
            return self._transformation

        def costructure_morphism(self, index: Parent) -> Morphism:
            return self.transformation().component(index)

        def costructure_morphisms(self) -> IndexedFamily:
            domain = self.diagram().domain()
            return indexed_family(
                domain.object_set(),
                lambda label: self.costructure_morphism(domain(label)),
                name=f"Costructure morphisms of {self}",
            )

        def _repr_(self) -> str:
            return f"Cocone with apex {self.apex()} under {self.diagram()}"

    def __init__(self, diagram: Functor) -> None:
        self._diagram = diagram
        super().__init__()

    def _make_named_class_key(self, name):
        return self._diagram

    def diagram(self) -> Functor:
        return self._diagram

    def target_category(self) -> Category:
        return self.diagram().codomain()

    def super_categories(self):
        return [OwnedObjects()]

    def cocone(
        self,
        apex: Parent,
        components: Callable[[Parent], Morphism],
    ) -> Parent:

        constant = Cat().Mor(
            self.diagram().domain(), self.target_category()
        ).constant_functor(apex)
        transformation = NaturalTransformation(self.diagram(), constant, components)
        return _object_of(self, apex=apex, transformation=transformation)

    def Mor(self, domain: Parent, codomain: Parent) -> CoconeHomset:
        if domain not in self or codomain not in self:
            raise TypeError("a cocone Hom requires two cocones under the same diagram")
        return self.HomCategory().Of(domain, codomain)



class _SpanCategory(_ConeCategory):
    r"""Spans in one category, over the shape ``. <- . -> .``.

    That shape needs no new vocabulary.  A span :math:`A\leftarrow C\to B` is
    an apex with one arrow to each of two objects, which is exactly a cone
    over the discrete diagram on those two, so the cone category already owns
    it and this is that category read as spans.

    A span is an object here rather than a pair of arguments, so it has an
    apex, two legs, a diagram, and its own colimit.  The colimit is computed
    in the category the span lives in, which is where a pushout belongs and
    which is what lets a category with a construction of its own supply it.
    """

    def super_categories(self):
        return [_ConeCategory(self.diagram())]

    class ParentMethods:
        def target_category(self) -> Category:
            r"""The category the span lives in."""
            return self.cone_category().target_category()

        def left_leg(self) -> Morphism:
            return self.structure_morphism(self.diagram().domain()(0))

        def right_leg(self) -> Morphism:
            return self.structure_morphism(self.diagram().domain()(1))

        def pushout(self) -> Parent:
            r"""Return the pushout of this span, the colimit of its diagram."""
            return self.target_category().pushout(self.left_leg(), self.right_leg())

        def _repr_(self) -> str:
            return f"Span {self.left_leg().codomain()} <- {self.apex()} -> {self.right_leg().codomain()}"


class _ProductConeCategory(_ConeCategory):
    r"""Selected product cones over one finite discrete diagram."""

    def super_categories(self):
        return [_ConeCategory(self.diagram())]


class _CoproductCoconeCategory(_CoconeCategory):
    r"""Selected coproduct cocones under one finite discrete diagram."""

    def super_categories(self):
        return [_CoconeCategory(self.diagram())]


class _LimitsOfCategory(OwnedCategoryBase):
    def __init__(self, index_category: Category, target_category: Category) -> None:
        self._index_category = index_category
        self._target_category = target_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._index_category, self._target_category

    def index_category(self):
        return self._index_category

    def target_category(self):
        return self._target_category

    def super_categories(self):
        return [OwnedObjects()]

    def _finite_shape_data(self, diagram):
        if diagram.domain() is not self.index_category():
            raise ValueError("a selected limit diagram has the wrong indexing category")
        if diagram.codomain() is not self.target_category():
            raise ValueError("a selected limit diagram has the wrong target category")
        shape = self.index_category()
        object_set_function = getattr(shape, "object_set", None)
        objects_function = getattr(shape, "objects", None)
        arrows_function = getattr(shape, "arrows", None)
        assert callable(object_set_function) and callable(objects_function), (
            "the theorem-backed realization requires an indexing category with represented object data"
        )
        assert callable(arrows_function), (
            "the theorem-backed realization requires an indexing category with a represented arrow set"
        )
        object_set = object_set_function()
        objects = objects_function()
        assert cardinal(object_set.cardinality()).is_finite(), (
            "the current product/equalizer realization enumerates a finite represented shape"
        )
        arrows = arrows_function()
        assert cardinal(arrows.cardinality()).is_finite(), (
            "the current product/equalizer realization enumerates a finite represented arrow set"
        )
        return object_set, objects, arrows

    @staticmethod
    def _extremal_shape_object(objects, arrows, *, terminal: bool):
        r"""Return an initial/terminal object with its unique arrows, if represented.

        A diagram indexed by a category with a terminal object has colimit the
        value at that object; dually an initial object computes the limit.
        Detecting this before a product/equalizer or coproduct/coequalizer
        reduction matters when the target subcategory has the required
        extremal colimit but does not have arbitrary coequalizers.
        """
        shape_objects = tuple(objects)
        shape_arrows = tuple(arrows)
        for candidate in shape_objects:
            selected = {}
            for obj in shape_objects:
                source, target = (obj, candidate) if terminal else (candidate, obj)
                matches = tuple(
                    arrow
                    for arrow in shape_arrows
                    if arrow.domain() is source and arrow.codomain() is target
                )
                if len(matches) != 1:
                    break
                selected[obj] = matches[0]
            else:
                return candidate, selected
        return None

    @cached_method(key=lambda self, diagram: id(diagram))
    def construction(self, diagram):
        r"""Return the selected limit, using products and an equalizer on finite represented shapes."""
        object_set, objects, arrows = self._finite_shape_data(diagram)
        extremal = self._extremal_shape_object(objects, arrows, terminal=False)
        if extremal is not None:
            initial, arrows_from_initial = extremal
            apex = diagram(initial)
            universal_cone = (diagram).Cones().cone(
                apex,
                lambda index: diagram(arrows_from_initial[index]),
            )

            def factorizer(cone):
                return cone.structure_morphism(initial)

            return SelectedLimitConstruction(diagram, universal_cone, factorizer)

        target = self.target_category()
        object_factors = indexed_family(
            object_set,
            lambda label: diagram(objects.value(label)),
            name="Object factors of a finite limit",
        )
        product_objects = target.product_construction(object_factors)
        arrow_factors = indexed_family(
            arrows,
            lambda arrow: diagram(arrow.codomain()),
            name="Arrow-target factors of a finite limit",
        )
        product_arrows = target.product_construction(arrow_factors)

        def object_label(obj):
            for label in object_set:
                if objects.value(label) is obj:
                    return label
            raise ValueError("an arrow endpoint is not one of the indexing category's objects")

        p_shape = product_objects.diagram().domain()
        product_arrows.diagram().domain()

        def compatibility_map(use_diagram_arrow):
            cone = (product_arrows.diagram()).Cones().cone(
                product_objects.object(),
                lambda q_index: (
                    diagram(q_index.value())
                    * product_objects.structure_morphism(
                        p_shape(object_label(q_index.value().domain()))
                    )
                    if use_diagram_arrow
                    else product_objects.structure_morphism(
                        p_shape(object_label(q_index.value().codomain()))
                    )
                ),
            )
            return product_arrows.factor(cone).apex_map()

        target_projection = compatibility_map(False)
        arrow_projection = compatibility_map(True)
        equalizer = target.equalizer_construction(target_projection, arrow_projection)
        equalizer_shape = equalizer.diagram().domain()
        into_product = equalizer.structure_morphism(equalizer_shape.source())
        universal_cone = (diagram).Cones().cone(
            equalizer.object(),
            lambda index: (
                product_objects.structure_morphism(p_shape(object_label(index)))
                * into_product
            ),
        )

        def factorizer(cone):
            product_cone = (product_objects.diagram()).Cones().cone(
                cone.apex(),
                lambda index: cone.structure_morphism(objects.value(index.value())),
            )
            into_product_from_apex = product_objects.factor(product_cone).apex_map()
            equalizer_cone = (equalizer.diagram()).Cones().cone(
                cone.apex(),
                lambda index: (
                    into_product_from_apex
                    if index is equalizer_shape.source()
                    else target_projection * into_product_from_apex
                ),
            )
            return equalizer.factor(equalizer_cone).apex_map()

        return SelectedLimitConstruction(diagram, universal_cone, factorizer)

    def object(self, diagram):
        return self.construction(diagram).object()

    @cached_method
    def defining_functor(self):
        r"""Return the functor ``[J,C] -> C`` selected by these limits."""
        from dzack_research.preamble.categories.abstract_categories.functors import (
            _limit_functor,
        )

        return _limit_functor(self.target_category(), self.index_category())


class _ColimitsOfCategory(_LimitsOfCategory):
    @cached_method(key=lambda self, diagram: id(diagram))
    def construction(self, diagram):
        r"""Return the selected colimit, using coproducts and a coequalizer on finite shapes."""
        object_set, objects, arrows = self._finite_shape_data(diagram)
        extremal = self._extremal_shape_object(objects, arrows, terminal=True)
        if extremal is not None:
            terminal, arrows_to_terminal = extremal
            apex = diagram(terminal)
            universal_cocone = (diagram).Cocones().cocone(
                apex,
                lambda index: diagram(arrows_to_terminal[index]),
            )

            def factorizer(cocone):
                return cocone.costructure_morphism(terminal)

            return SelectedColimitConstruction(diagram, universal_cocone, factorizer)

        target = self.target_category()
        object_cofactors = indexed_family(
            object_set,
            lambda label: diagram(objects.value(label)),
            name="Object cofactors of a finite colimit",
        )
        coproduct_objects = target.coproduct_construction(object_cofactors)
        arrow_cofactors = indexed_family(
            arrows,
            lambda arrow: diagram(arrow.domain()),
            name="Arrow-source cofactors of a finite colimit",
        )
        coproduct_arrows = target.coproduct_construction(arrow_cofactors)

        def object_label(obj):
            for label in object_set:
                if objects.value(label) is obj:
                    return label
            raise ValueError("an arrow endpoint is not one of the indexing category's objects")

        coproduct_arrows.diagram().domain()
        b_shape = coproduct_objects.diagram().domain()

        def compatibility_map(use_diagram_arrow):
            cocone = (coproduct_arrows.diagram()).Cocones().cocone(
                coproduct_objects.object(),
                lambda a_index: (
                    coproduct_objects.costructure_morphism(
                        b_shape(object_label(a_index.value().codomain()))
                    )
                    * diagram(a_index.value())
                    if use_diagram_arrow
                    else coproduct_objects.costructure_morphism(
                        b_shape(object_label(a_index.value().domain()))
                    )
                ),
            )
            return coproduct_arrows.factor(cocone).apex_map()

        source_injection = compatibility_map(False)
        arrow_injection = compatibility_map(True)
        coequalizer = target.coequalizer_construction(source_injection, arrow_injection)
        coequalizer_shape = coequalizer.diagram().domain()
        from_coproduct = coequalizer.costructure_morphism(coequalizer_shape.target())
        universal_cocone = (diagram).Cocones().cocone(
            coequalizer.object(),
            lambda index: (
                from_coproduct
                * coproduct_objects.costructure_morphism(
                    b_shape(object_label(index))
                )
            ),
        )

        def factorizer(cocone):
            object_cocone = (coproduct_objects.diagram()).Cocones().cocone(
                cocone.apex(),
                lambda index: cocone.costructure_morphism(objects.value(index.value())),
            )
            from_objects = coproduct_objects.factor(object_cocone).apex_map()
            coequalizer_cocone = (coequalizer.diagram()).Cocones().cocone(
                cocone.apex(),
                lambda index: (
                    from_objects * source_injection
                    if index is coequalizer_shape.source()
                    else from_objects
                ),
            )
            return coequalizer.factor(coequalizer_cocone).apex_map()

        return SelectedColimitConstruction(diagram, universal_cocone, factorizer)

    @cached_method
    def defining_functor(self):
        r"""Return the functor ``[J,C] -> C`` selected by these colimits."""
        from dzack_research.preamble.categories.abstract_categories.functors import (
            _colimit_functor,
        )

        return _colimit_functor(self.target_category(), self.index_category())


class _ProductsOfCategory(_LimitsOfCategory):
    pass


class _CoproductsOfCategory(_ColimitsOfCategory):
    pass


def _factor_family(factors, *, name="Selected factors"):
    r"""Return the indexed family a construction is taken over.

    A construction is taken over an index set, so its datum is the family and
    never an arity.  A bare sequence is syntactic ingress: it denotes the
    family on the canonical labels ``Sets.Δ[n-1]``, and this is the one
    boundary at which that normalization happens.
    """
    match factors:
        case IndexedFamily():
            return factors
    values = tuple(factors)
    labels = Sets.Δ[len(values) - 1]
    return indexed_family(
        labels,
        lambda label: values[int(labels.ranking_map()(label))],
        name=name,
    )


def _finite_factor_family(factors, *, name="Selected factors"):
    r"""Return the family, where the construction is represented over finite index sets."""
    family = _factor_family(factors, name=name)
    if not family.cardinality().is_finite():
        raise TypeError("the current product/coproduct construction requires finitely many factors")
    return family


def _two_factors_of(factors, *, name="Selected factors"):
    r"""Return the two factors, where the construction is represented binary.

    A backend that takes exactly two objects cannot answer over a larger
    index set.  Folding it would return an object satisfying the same
    universal property, but a different one: its projections and injections
    are composites through a nest, so there is no arrow to or from the factor
    at a given index.  A site with such a backend names that hypothesis here
    rather than folding.
    """
    family = _factor_family(factors, name=name)
    assert family.cardinality() == cardinal(2), (
        f"{name.lower()} over an index set other than a two-element one is "
        "defined, but the represented construction takes exactly two factors"
    )
    labels = tuple(family.index_set())
    return family[labels[0]], family[labels[1]]


class BiproductCategory(OwnedCategoryBase):
    r"""Objects equipped with the selected finite biproduct structure."""

    def __init__(self, factors: IndexedFamily | Iterable[Parent]) -> None:
        self._factors = _finite_factor_family(factors, name="Biproduct factors")
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def factors(self) -> IndexedFamily:
        return self._factors

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether ``candidate`` is a biproduct of exactly these factors.

        Nothing is built in this category; the objects that have a selected
        biproduct decomposition record it on themselves (lattices do), so the
        recorded factors are read and compared.
        """
        match getattr(candidate, "biproduct_factors", None):
            case None:
                return False
            case recorded:
                return recorded() == self.factors()


DirectSumCategory = BiproductCategory


class TensorProductCategory(OwnedCategoryBase):
    r"""Objects equipped with a chosen tensor-product universal bilinear map."""

    def __init__(self, factors: IndexedFamily | Iterable[Parent]) -> None:
        self._factors = _finite_factor_family(factors, name="Tensor factors")
        super().__init__()

    def _make_named_class_key(self, name):
        return self._factors

    def tensor_factors(self) -> IndexedFamily:
        return self._factors

    def super_categories(self):
        return [OwnedObjects()]

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether ``candidate`` is a tensor product of exactly these factors, as it records them."""
        match getattr(candidate, "tensor_factors", None):
            case None:
                return False
            case recorded:
                return recorded() == self.tensor_factors()


def _discrete_diagram(factors, target_category=None):
    family = _finite_factor_family(factors)
    if family.cardinality() == cardinal(0):
        if target_category is None:
            raise ValueError(
                "an empty diagram has no object from which to infer its target category"
            )
        target = target_category
    else:
        target = (
            Cat().join(tuple(obj.category() for obj in family))
            if target_category is None
            else target_category
        )

    index = DiscreteCategory(family.index_set())
    return Cat().Mor(index, target).discrete_diagram(family)


__all__ = [
    "BiproductCategory",
    "CoconeMorphism",
    "ConeMorphism",
    "DirectSumCategory",
    "DirectedSystem",
    "FiniteOrdinalCategory",
    "FiniteSequenceDiagram",
    "InverseSystem",
    "ParallelPairCategory",
    "ParallelPairDiagram",
    "PosetCategory",
    "RestrictedDiagram",
    "SelectedColimitConstruction",
    "SelectedLimitConstruction",
    "TensorProductCategory",
]
