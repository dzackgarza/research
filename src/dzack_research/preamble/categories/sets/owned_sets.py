r"""The owned ``Sets()`` root and its five axioms.

The owned root sits over Sage's ``Sets()`` and reuses Sage's standard
``Finite`` and ``Infinite`` axioms; project-owned ``Countable``,
``Uncountable``, and ``TotallyOrdered`` enter Sage's global ``all_axioms``
registry through the exact idempotent adapter below — the only Sage mutation
this module performs.

The axiom lattice is mathematical fact: ``Finite`` refines ``Countable``
(every finite set receives the enumeration contract), ``Uncountable``
refines ``Infinite``, ``Countable`` and ``Uncountable`` are disjoint, and
totally ordered sets are a trusted placement that says nothing about
cardinality. Countably-infinite is the join ``Sets().Countable().Infinite()``,
never a new named root. Membership is opt-in-with-trust: ``Countable`` forces
the executable witness suite (exhaustive duplicate-free iteration, integer
indexing, reverse lookup) through Sage ``abstract_method`` obligations;
``Uncountable`` is trusted placement carrying uniform consequences and no
enumeration obligation. Generic infinite-set consequences (``is_finite``,
``cardinality() == +Infinity``) are inherited from Sage's ``Infinite`` axiom
through the join and are never reimplemented here.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator, Mapping
from typing import cast, Generic, TYPE_CHECKING, TypeVar

from sage.categories.category import Category as SageCategory
from sage.categories.category_with_axiom import all_axioms
from sage.categories.homset import Homset as SageHomset
from sage.misc.cachefunc import cached_method
from sage.categories.morphism import Morphism as SageMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.rings.integer import Integer
from sage.rings.semirings.non_negative_integer_semiring import NN
from sage.structure.element import Element as SageElement
from sage.structure.richcmp import richcmp

from dzack_research.preamble.lexicon.interop import SageParent
from dzack_research.preamble.owned_category import OwnedParent
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
    IsoCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.functor_images import (
    _FunctorImageParameters,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    CoproductsOfCategory,
    ProductsOfCategory,
)
from dzack_research.preamble.owned_category_bases import (
    Category,
    CategoryWithParameters,
    CategoryWithAxiom,
)

if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData

    # Sage's abstract_method ships untyped; for type-checking use
    # abc.abstractmethod (typed, and permits the empty abstract bodies
    # below). Runtime uses Sage's.
    from abc import abstractmethod as abstract_method
    from sage.structure.parent import ElementConstructorInput

    from dzack_research.preamble.categories.abstract_categories.functors import (
        DiscreteCategory,
    )
    from dzack_research.preamble.categories.sets.cardinals import Cardinal
    from dzack_research.preamble.categories.sets.sets import (
        CartesianProductFunctor,
        DisjointUnionFunctor,
    )

    from collections.abc import Hashable, Iterable
    from sage.combinat.posets.posets import FinitePoset
    from sage.repl.rich_output.display_manager import DisplayManager
    from sage.repl.rich_output.output_basic import OutputBase

    # A finite poset's elements are arbitrary hashable objects; this alias
    # names that genuine generality once, instead of scattering ``Any``.
    type PosetElement = Hashable
    type SetElementInput = ElementConstructorInput
    type SetMap = Callable[[SetElementInput], SetElementInput]
    type SetMapDefinition = SetMap | Mapping[SetElementInput, SetElementInput]

    class _ParentWithIsFinite(SageParent[_E], Generic[_E]):
        def is_finite(self) -> bool: ...
else:
    from sage.misc.abstract_method import abstract_method

_E = TypeVar("_E")

_SET_AXIOMS = ("Countable", "Uncountable", "PartiallyOrdered", "TotallyOrdered")


def register_set_axioms() -> None:
    r"""Register exactly ``Countable``, ``Uncountable``, ``PartiallyOrdered``, and
    ``TotallyOrdered`` in Sage's global
    axiom registry. Idempotent: after the first registration, repeated calls
    leave the registry unchanged."""
    for axiom_name in _SET_AXIOMS:
        if axiom_name not in all_axioms:
            all_axioms.add(axiom_name)
    assert all(axiom_name in all_axioms for axiom_name in _SET_AXIOMS)


register_set_axioms()


class SetSubcategoryMethods:
    r"""Set axioms and Set-valued functorial constructions."""

    # Runtime Sage mixes this class into every subcategory, so ``self``
    # is a SageCategory there; the casts state that fact for the checker.
    def Countable(self) -> SageCategory:
        r"""Objects whose underlying set has a chosen computable,
        exhaustive, duplicate-free enumeration."""
        category = cast(SageCategory, self)
        assert "Uncountable" not in category.axioms(), "Countable and Uncountable are disjoint"
        return category._with_axiom("Countable")

    def Uncountable(self) -> SageCategory:
        r"""Objects whose underlying set is beyond every enumeration, by
        trusted declaration. (The reverse contradiction, ``Uncountable``
        then ``Finite``, is refused by Sage's native finite/infinite
        incompatibility because ``Uncountable`` implies ``Infinite``.)"""
        category = cast(SageCategory, self)
        assert "Countable" not in category.axioms(), "Countable and Uncountable are disjoint"
        return category._with_axiom("Uncountable")

    def PartiallyOrdered(self) -> SageCategory:
        r"""Objects whose underlying set is equipped with a partial order."""
        category = cast(SageCategory, self)
        return category._with_axiom("PartiallyOrdered")

    def TotallyOrdered(self) -> SageCategory:
        r"""Objects whose underlying set is equipped with a total order."""
        category = cast(SageCategory, self)
        return category._with_axiom("TotallyOrdered")

    @cached_method
    def ProductFunctor(
        self,
        index_category: "DiscreteCategory",
    ) -> "CartesianProductFunctor":
        from dzack_research.preamble.categories.sets.sets import (
            CartesianProductFunctor,
        )

        return CartesianProductFunctor(Sets(), index_category)

    def Products(self, index_category: "DiscreteCategory") -> SageCategory:
        return self.ProductFunctor(index_category).Image()

    @cached_method
    def CoproductFunctor(
        self,
        index_category: "DiscreteCategory",
    ) -> "DisjointUnionFunctor":
        from dzack_research.preamble.categories.sets.sets import (
            DisjointUnionFunctor,
        )

        return DisjointUnionFunctor(Sets(), index_category)

    def Coproducts(self, index_category: "DiscreteCategory") -> SageCategory:
        return self.CoproductFunctor(index_category).Image()


class Sets(Category):
    r"""The owned category of sets: declaration owner of the generic
    meanings of cardinality, finiteness, infinitude, countability,
    uncountability, enumeration, indexing, and reverse lookup.

    It is also the **root of the owned construction chain**.  Its
    ``ObjectType`` is the parent implementation class of everything built
    through the chain: it declares Sage's ``Parent`` as a base and makes the
    one non-cooperative ``Parent.__init__`` call, so a level above it supplies
    only the datum it introduces and reaches this one by ``super()``.
    :mod:`dzack_research.preamble.owned_category` records the mechanism, and
    why Sage's ``Sets()`` below is load-bearing rather than decoration.
    """

    def super_categories(self) -> list[SageCategory]:
        return [SageSets()]

    if TYPE_CHECKING:
        # Typed axiom navigation: at runtime Sage synthesizes these from
        # SubcategoryMethods; the axiom tree is closed under its own axioms.
        # The class-attribute wiring at the bottom of this module is Sage's
        # class-resolution shortcut and is runtime-only.
        def Countable(self) -> Sets: ...
        def Uncountable(self) -> Sets: ...
        def PartiallyOrdered(self) -> Sets: ...
        def TotallyOrdered(self) -> Sets: ...
        def Finite(self) -> Sets: ...
        def Infinite(self) -> Sets: ...
        def Facade(self) -> Sets: ...
    SubcategoryMethods = SetSubcategoryMethods

    class _Products(_FunctorImageParameters, CategoryWithParameters):
        r"""Cartesian products as the Set-specific image of a product functor."""

        def super_categories(self) -> list[SageCategory]:
            return [ProductsOfCategory(self.functor())]

        def _repr_(self) -> str:
            return f"Category of cartesian products constructed by {self.functor()}"

        class ObjectType:

            @cached_method
            def factor_cardinalities(
                self,
            ) -> "Callable[[SetElementInput], Cardinal]":
                return lambda index: self.diagram()(index).cardinality()

            def cartesian_factors(self) -> tuple[SageParent, ...]:
                r"""The finite factor family under Sage's enumeration protocol."""
                assert self.index_category().objects() in Sets().Finite()
                return tuple(self.factors())

            def _sets_keys(self) -> range:
                r"""The positions used by Sage's finite-product enumerator."""
                return range(len(self.cartesian_factors()))

            @cached_method
            def cardinality(self) -> Cardinal:
                r"""Return ``prod(#X_i)`` for the cartesian factors ``X_i``."""
                from dzack_research.preamble.categories.sets.cardinals import (
                    Cardinalities,
                )

                return Cardinalities().indexed_product(
                    self.index_category().objects(),
                    self.factor_cardinalities(),
                )

            def _cartesian_product_of_elements(
                self, elements: Iterable[SageElement]
            ) -> SageElement:
                r"""The point \((x_i)\) assembled from its components, under
                the name Sage's product machinery reads.

                Sage states the enumeration of a product of sets in terms of
                this name and of :meth:`cartesian_factors`, so supplying it is
                what makes that enumeration the enumeration of this product:
                lexicographic when every factor after the first is finite, and
                Cantor's antidiagonal otherwise, which is fair across infinite
                factors.  The empty product yields the one empty family, and a
                product with an empty factor yields nothing.
                """
                indices = tuple(self.index_category().objects())
                return self(dict(zip(indices, elements)))

            __iter__ = SageSets.CartesianProducts.ParentMethods.__iter__

            def projection(self, index: "SetElementInput") -> "Sets.ArrowType":
                r"""The ``index``-th product projection \(\pi_i:\prod_j X_j\to X_i\)."""
                factor = self.diagram()(index)

                def project(point: "SetElementInput") -> "SetElementInput":
                    match point:
                        case SageElement() if point.parent() is self:
                            return point[index]
                        case _:
                            return self(point)[index]

                return Sets().Hom(self, factor)(project)

            def cartesian_projection(self, index: int) -> "Sets.ArrowType":
                r"""The projection, under the name Sage's product machinery reads."""
                indices = tuple(self.index_category().objects())
                return self.projection(indices[index])

            def universal_morphism(self, cone: SageElement) -> "Sets.ArrowType":
                constant_diagram = cone.domain()
                assert constant_diagram.domain() is self.index_category()
                return Sets().Hom(constant_diagram.constant_value(), self)(
                    lambda element: self(
                        lambda index: cone.component(index)(element)
                    )
                )

            def cardinality_comparison(self) -> SageMorphism:
                from dzack_research.preamble.categories.sets.cardinals import (
                    Cardinalities,
                )

                cardinals = Cardinalities()
                source = self.cardinality()
                target = cardinals.indexed_product(
                    self.index_category().objects(),
                    self.factor_cardinalities(),
                )
                assert source == target
                return cardinals.hom(source, target).identity()

            def __contains__(self, element: ElementConstructorInput) -> bool:
                r"""Whether ``element`` is a point of \(\prod_i X_i\).

                A point built by this product is one of its own elements.  A
                callable declares an indexed section.  An explicit mapping is
                admitted only for a finite index set and is checked at every
                index.
                """
                match element:
                    case SageElement() if element.parent() is self:
                        return True
                    case Mapping() if self.index_category().objects() in Sets().Finite():
                        indices = self.index_category().objects()
                        return all(key in indices for key in element) and all(
                            index in element
                            and element[index] in self.diagram()(index)
                            for index in indices
                        )
                    case Callable():
                        return True
                    case _:
                        return False

            def _element_constructor_(
                self, definition: "SetMapDefinition"
            ) -> SageElement:
                r"""Return the indexed family \((x_i)\) in this product."""
                assert definition in self
                return self.ElementType(definition=definition, parent=self)

            def _repr_(self) -> str:
                return f"Product of {self.diagram()}"

        class ElementMethods:
            r"""A point of \(\prod_i X_i\): the family \((x_i)\) and nothing more.

            No arithmetic.  A product of *sets* has no addition to offer, and
            putting one here would be a second notion of what a module or
            lattice element is, competing with the one the levels above
            declare.  Components, comparison and indexing are all a point of a
            product is.
            """

            def __init__(
                self,
                parent: SageParent,
                definition: "SetMapDefinition",
            ) -> None:
                self._definition = definition
                super().__init__(parent=parent)

            def components(self) -> "SetMapDefinition":
                return self._definition

            def cartesian_projection(self, index: int) -> SageElement:
                r"""The ``index``-th component, under the name Sage's machinery reads."""
                indices = tuple(self.parent().index_category().objects())
                return self[indices[index]]

            def __getitem__(self, index: "SetElementInput") -> SageElement:
                parent = self.parent()
                assert index in parent.index_category()
                match self._definition:
                    case Mapping():
                        value = self._definition[index]
                    case Callable():
                        value = self._definition(index)
                    case _:
                        raise AssertionError("invalid product-element representation")
                return parent.diagram()(index)(value)

            def __iter__(self) -> Iterator[SageElement]:
                indices = self.parent().index_category().objects()
                assert indices in Sets().Finite()
                return iter(tuple(self[index] for index in indices))

            def _repr_(self) -> str:
                indices = self.parent().index_category().objects()
                if indices in Sets().Finite():
                    return "(%s)" % ", ".join(
                        repr(self[index]) for index in indices
                    )
                return f"Element of {self.parent()}"

    class _Coproducts(_FunctorImageParameters, CategoryWithParameters):
        r"""Disjoint unions as the Set-specific image of a coproduct functor."""

        def super_categories(self) -> list[SageCategory]:
            return [CoproductsOfCategory(self.functor())]

        def _repr_(self) -> str:
            return f"Category of disjoint unions constructed by {self.functor()}"

        class ObjectType:
            @cached_method
            def cofactor_cardinalities(
                self,
            ) -> "Callable[[SetElementInput], Cardinal]":
                return lambda index: self.diagram()(index).cardinality()

            @cached_method
            def cardinality(self) -> Cardinal:
                from dzack_research.preamble.categories.sets.cardinals import (
                    Cardinalities,
                )

                return Cardinalities().indexed_sum(
                    self.index_category().objects(),
                    self.cofactor_cardinalities(),
                )

            def __iter__(self) -> Iterator[SageElement]:
                from sage.sets.disjoint_union_enumerated_sets import (
                    DisjointUnionEnumeratedSets,
                )
                from sage.sets.family import Family

                index_set = self.index_category().objects()
                family = Family(index_set, self.diagram())
                for tagged_element in DisjointUnionEnumeratedSets(
                    family,
                    keepkey=True,
                ):
                    yield self(tagged_element)

            def __contains__(self, tagged_element: "SetElementInput") -> bool:
                match tagged_element:
                    case SageElement() if tagged_element.parent() is self:
                        return True
                    case tuple() if len(tagged_element) == 2:
                        index, element = tagged_element
                        return (
                            index in self.index_category()
                            and element in self.diagram()(index)
                        )
                    case _:
                        return False

            def _element_constructor_(
                self,
                tagged_element: tuple["SetElementInput", "SetElementInput"],
            ) -> SageElement:
                assert tagged_element in self
                index, element = tagged_element
                return self.ElementType(
                    parent=self,
                    index=index,
                    value=self.diagram()(index)(element),
                )

            def injection(self, index: "SetElementInput") -> "Sets.ArrowType":
                assert index in self.index_category()
                cofactor = self.diagram()(index)
                return Sets().Hom(cofactor, self)(
                    lambda element: self((index, element))
                )

            def universal_morphism(self, cocone: SageElement) -> "Sets.ArrowType":
                constant_diagram = cocone.codomain()
                assert constant_diagram.domain() is self.index_category()

                def copair(tagged_element: "SetElementInput") -> "SetElementInput":
                    element = self(tagged_element)
                    return cocone.component(element.index())(element.value())

                return Sets().Hom(self, constant_diagram.constant_value())(
                    copair
                )

            def cardinality_comparison(self) -> SageMorphism:
                from dzack_research.preamble.categories.sets.cardinals import (
                    Cardinalities,
                )

                cardinals = Cardinalities()
                source = self.cardinality()
                target = cardinals.indexed_sum(
                    self.index_category().objects(),
                    self.cofactor_cardinalities(),
                )
                assert source == target
                return cardinals.hom(source, target).identity()

            def _repr_(self) -> str:
                return f"Coproduct of {self.diagram()}"

        class ElementMethods:
            def __init__(
                self,
                parent: SageParent,
                index: "SetElementInput",
                value: "SetElementInput",
            ) -> None:
                self._index = index
                self._value = value
                super().__init__(parent=parent)

            def index(self) -> "SetElementInput":
                return self._index

            def value(self) -> "SetElementInput":
                return self._value

            def _repr_(self) -> str:
                return f"({self._index}, {self._value})"

    class _HomCategory(HomCategoryConstruction):
        r"""Set-valued arrows, represented by functions.

        The object built by this category is still a hom category.  Its
        objects are functions.  The associated exponential is the set of
        those objects and is constructed separately.
        """

        class ParentMethods:
            def __call__(
                self,
                definition: "SetMapDefinition | Sets.ArrowType",
            ) -> "Sets.ArrowType":
                match definition:
                    case SageElement() if definition in self:
                        return definition
                    case Mapping() | Callable():
                        return self.ObjectType(
                            hom_category=self,
                            definition=definition,
                        )
                    case _:
                        raise TypeError(
                            "a set arrow requires a callable or an explicit mapping"
                        )

            def identity(self) -> "Sets.ArrowType":
                assert self.domain() is self.codomain(), (
                    "an identity belongs to an endomorphism category"
                )
                return self(lambda element: element)

            def compose(
                self,
                second: "Sets.ArrowType",
                first: "Sets.ArrowType",
            ) -> "Sets.ArrowType":
                assert first.codomain() is second.domain(), (
                    "set arrows compose only when their middle object agrees"
                )
                assert self.domain() is first.domain()
                assert self.codomain() is second.codomain()
                return self(lambda element: second(first(element)))

            def object_set(self) -> SageParent:
                r"""Return the exponential whose members are this category's objects."""
                from dzack_research.preamble.categories.sets.sets import (
                    ExponentialOfSets,
                )

                return ExponentialOfSets(self.codomain(), self.domain())

            def cardinality(self) -> Cardinal:
                r"""Return the number of functions from the domain to the codomain."""
                from dzack_research.preamble.categories.sets.cardinals import (
                    Cardinalities,
                )

                return Cardinalities().power(
                    self.codomain().cardinality(),
                    self.domain().cardinality(),
                )

        class ElementMethods:
            r"""A function between two sets.

            A callable declares a total function.  Each application checks
            its input and output.  An explicit mapping defines a function
            only when its finite domain is exactly the mapping's key set.
            """

            def __init__(
                self,
                hom_category: SageCategory,
                definition: "SetMapDefinition",
            ) -> None:
                match definition:
                    case Mapping():
                        assert hom_category.domain() in Sets().Finite(), (
                            "an explicit mapping requires a finite domain"
                        )
                        assert all(
                            key in hom_category.domain() for key in definition
                        ), "every mapping key must belong to the domain"
                        assert all(
                            element in definition for element in hom_category.domain()
                        ), "an explicit mapping must define every domain element"
                        assert all(
                            value in hom_category.codomain()
                            for value in definition.values()
                        ), "every mapping value must belong to the codomain"
                        self._definition = dict(definition)
                    case Callable():
                        self._definition = definition
                    case _:
                        raise TypeError(
                            "a set arrow requires a callable or an explicit mapping"
                        )
                super().__init__(hom_category=hom_category)

            def __call__(self, element: "SetElementInput") -> "SetElementInput":
                assert element in self.domain(), (
                    f"{element!r} is not in the domain of {self}"
                )
                match self._definition:
                    case Mapping():
                        image = self._definition[element]
                    case Callable():
                        image = self._definition(element)
                    case _:
                        raise AssertionError("invalid set-arrow representation")
                assert image in self.codomain(), (
                    f"{self} sends {element!r} outside its codomain"
                )
                return image

    class _IsoCategory(IsoCategoryConstruction):
        r"""Isomorphisms of sets with declared inverse functions."""

        class ParentMethods:
            def __call__(
                self,
                definition: "SetMapDefinition | Sets.IsoArrowType",
                inverse_definition: "SetMapDefinition | None" = None,
            ) -> "Sets.IsoArrowType":
                match definition:
                    case SageElement() if definition in self:
                        return definition
                    case Mapping() | Callable():
                        assert inverse_definition is not None, (
                            "a set isomorphism requires its inverse function"
                        )
                        forward = self.base_category().Hom(
                            self.domain(), self.codomain()
                        )(definition)
                        backward = self.base_category().Hom(
                            self.codomain(), self.domain()
                        )(inverse_definition)
                        return super().__call__(
                            forward,
                            backward,
                        )
                    case _:
                        raise TypeError(
                            "a set isomorphism requires a callable or an explicit mapping"
                        )

        class ElementMethods:
            def __call__(self, element: "SetElementInput") -> "SetElementInput":
                return self.forward()(element)

    class ElementMethods(SageElement):
        r"""An element of an owned set: the element implementation class.

        The element half of what ``ObjectType`` is for parents.  It carries
        ``Element`` so that everything built through the chain has a parent,
        and it carries nothing else: what an element of a bare *set* is, is a
        member of that set.  Structure is added by the levels above, which is
        where the arithmetic lives.
        """

        def __init__(self, parent: SageParent) -> None:
            SageElement.__init__(self, parent)

    class ParentMethods(OwnedParent, SageParent):
        def __init__(
            self, cardinality: Cardinal | Integer | None = None, **rest: ConstructionData
        ) -> None:
            r"""The bottom of every owned construction.

            The only non-cooperative ``Parent.__init__`` call in the chain:
            every level above reaches it through ``super().__init__(**rest)``
            after consuming its own datum, so constructing anything owned has
            already constructed the set it is built on.

            ``cardinality`` is this level's datum, and it is optional because
            a set may be constructed knowing its size or not.  A level that
            knows how big the set it is building is -- \(\mathbb{F}_p\) knows
            \(p\) -- passes it up here rather than answering the question
            itself; a level that does not, such as a product, derives the
            answer from its own datum instead.  Nothing counts an enumeration
            to rediscover a number the construction was given.
            """
            if cardinality is not None:
                from dzack_research.preamble.categories.sets.cardinals import cardinal

                self._cardinality = cardinal(cardinality)
            SageParent.__init__(self, **rest)

        def cardinality(self) -> Cardinal:
            r"""Return \(|X|\), as the construction stated it.

            A set that was not built with a size does not have one to give,
            and says so by having no answer here rather than by counting.
            """
            return self._cardinality

        def is_finite(self) -> bool:
            return self.cardinality().is_finite()

        def is_infinite(self) -> bool:
            return self.cardinality().is_infinite()

        def is_countable(self) -> bool:
            r"""Whether $|X| \le \aleph_0$.

            Read off the cardinal, which is total on sets, rather than
            declared by placement: countability is a fact about the size, so
            any set that can say how big it is answers this, and no chosen
            enumeration is required to do it.  The axiom subcategories
            override with their exact answer.
            """
            return bool(self.cardinality().is_countable())

        def is_uncountable(self) -> bool:
            r"""Whether $|X| > \aleph_0$."""
            return bool(self.cardinality().is_uncountable())

        def Hom(
            self,
            target: SageParent,
            category: SageCategory | None = None,
        ) -> SageCategory:
            r"""Return the hom category by delegation to the owning category."""
            source_category = self.category() if category is None else category
            assert self in source_category and target in source_category
            return source_category.Hom(self, target)

        def End(self) -> SageCategory:
            r"""Return the endomorphism category by delegation to the category."""
            return self.category().End(self)

        def Aut(self) -> SageCategory:
            r"""Return the automorphism category by delegation to the category."""
            return self.category().Aut(self)

        def exponential(self, exponent: SageParent) -> SageParent:
            r"""Return the set \(Y^X\) of functions \(X\to Y\)."""
            from dzack_research.preamble.categories.sets.sets import (
                ExponentialOfSets,
            )

            return ExponentialOfSets(self, exponent)

        def __pow__(self, exponent: SageParent) -> SageParent:
            return self.exponential(exponent)

        def _Hom_(
            self,
            codomain: SageParent,
            category: SageCategory | None = None,
        ) -> SageCategory:
            r"""Route Sage's ``Hom`` entry point to the owned Hom category."""
            return self.Hom(codomain, category=category)


class FinitelySupportedFunctionSets(Category):
    r"""Sets of finitely supported functions from a set into a pointed set.

    For a set \(S\) and a pointed set \((X,x_0)\), this construction has
    elements

    \[
        X^{(S)}=\{a:S\to X:\{s\in S:a(s)\ne x_0\}\text{ is finite}\}.
    \]

    If \(S\) is finite, this is the full function set \(X^S\), which is
    equinumerous with a finite cartesian product of copies of \(X\).  Its
    elements remain functions.  The construction therefore supplies the
    cardinality and the resulting set placement without putting its objects
    in the category of cartesian-product sets.
    """

    def super_categories(self) -> list[SageCategory]:
        return [Sets()]

    @classmethod
    def _repr_object_names(cls) -> str:
        return "sets of finitely supported functions"

    class ParentMethods:
        def __init__(
            self,
            index_set: SageParent,
            value_set: SageParent,
            basepoint: SageElement,
            **rest: ConstructionData,
        ) -> None:
            assert basepoint in value_set, (
                f"the basepoint {basepoint!r} is an element of {value_set}"
            )
            self._index_set = index_set
            self._value_set = value_set
            self._basepoint = basepoint
            # The cardinality belongs to the finitely supported-function set
            # constructed here, before any algebraic enrichment is added.
            cardinality = self._finitely_supported_cardinality()
            if cardinality.is_finite():
                placement = Sets().Finite()
            elif cardinality.is_countable():
                placement = Sets().Countable()
            else:
                placement = Sets().Uncountable()
            category = rest.get("category")
            assert category is not None, "owned constructions require a category"
            rest["category"] = SageCategory.join((category, placement))
            super().__init__(
                cardinality=cardinality,
                **rest,
            )

            from dzack_research.preamble.refine import refine

            refine(self, placement)

        def index_set(self) -> SageParent:
            return self._index_set

        def value_set(self) -> SageParent:
            return self._value_set

        def basepoint(self) -> SageElement:
            return self._basepoint

        def _finitely_supported_cardinality(self) -> Cardinal:
            r"""Return the cardinality determined by this set construction."""
            from dzack_research.preamble.categories.sets.cardinals import (
                Cardinal,
                Cardinalities,
                cardinal,
            )
            from sage.rings.infinity import Infinity

            value_count = self.value_set().cardinality()
            if not isinstance(value_count, Cardinal) and value_count == Infinity:
                assert "Countable" in placement_of(self.value_set()).axioms(), (
                    f"{self.value_set()} reports only +Infinity and does not "
                    "declare countability, so its cardinality is not determined"
                )
            value_cardinality = cardinal(value_count)
            if value_cardinality == 1:
                return cardinal(1)

            index_count = self.index_set().cardinality()
            if not isinstance(index_count, Cardinal) and index_count == Infinity:
                assert "Countable" in placement_of(self.index_set()).axioms(), (
                    f"{self.index_set()} reports only +Infinity and does not "
                    "declare countability, so its cardinality is not determined"
                )
            index_cardinality = cardinal(index_count)
            if index_cardinality == 0:
                return cardinal(1)
            if index_cardinality.is_finite():
                return Cardinalities().power(
                    value_cardinality, index_cardinality
                )
            return Cardinalities().supremum(
                value_cardinality, index_cardinality
            )

        def cardinality(self) -> Cardinal:
            r"""Return \(\lvert X^{(S)}\rvert\).

            A finite \(S\) gives \(\lvert X\rvert^{\lvert S\rvert}\).  For
            infinite \(S\) and nontrivial \(X\), finite support gives
            \(\max(\lvert X\rvert,\lvert S\rvert)\), not the cardinality of
            the full product \(X^S\).
            """
            return self._finitely_supported_cardinality()

class FiniteSets(CategoryWithAxiom):
    r"""Finite sets: Sage's standard axiom, plus the owned refinement that
    finiteness implies the countable enumeration contract."""

    _base_category_class_and_axiom = (Sets, "Finite")

    def extra_super_categories(self) -> list[SageCategory]:
        return [cast(Sets, self.base_category()).Countable()]

    def __contains__(self, parent: ElementConstructorInput) -> bool:
        r"""Return whether ``parent`` is a finite set.

        Sage's default answers from category placement alone, so an object
        that has *computed* its finiteness — and says so through
        ``is_finite`` — is reported infinite merely because nothing refined
        it afterwards. Placement in this category is itself a legitimate
        proof of finiteness, so the membership question first accepts the
        placement answer, then falls through to the object's own computed
        answer. A caller writing the membership question therefore gets the
        stronger of the two, never only a record of how the object was
        constructed.
        """
        if super().__contains__(parent):
            return True

        return False

    class ParentMethods:
        if TYPE_CHECKING:
            def __iter__(self) -> Iterator[SageElement]: ...

        @cached_method
        def symmetric_group(self) -> SageParent:
            r"""Return :math:`\operatorname{Sym}(X)`: the automorphism group
            of this set *in* ``Set``.

            Named for which automorphism group it is.  In ``Set`` every
            bijection is an automorphism, so this is the full symmetric
            group on the members.  For a *totally ordered* finite set the
            automorphism group in its own category is trivial — an
            order-preserving bijection of a finite total order fixes every
            element — and :math:`\operatorname{Sym}(X)` instead acts simply
            transitively on the set of total orderings of :math:`X` (the
            torsor of orderings); a bare ``Aut`` on an ordered parent would
            conflate the two, which is the recorded error of the source
            corpus this method was migrated from (PLAN-corpora-audit-registry,
            ``FiniteOrderedSet.py`` error row).  Sage's ``SymmetricGroup``
            on the members is the engine.

            The permutation-matrix representation is not stored here: it is
            the free-module functor applied on morphisms
            (``FreeModuleFunctorClass._apply_functor_to_morphism`` in
            ``categories/functors/free_forgetful_adjunction.sage``), which
            sends :math:`\operatorname{Sym}(X)` into
            :math:`\operatorname{Aut}(F(X))` as the permutation matrices of
            the chosen enumeration.
            """
            from sage.groups.perm_gps.permgroup_named import SymmetricGroup

            automorphisms = SymmetricGroup(domain=tuple(self))
            return cast(SageParent, automorphisms)

        # No ``cardinality`` here.  A count is an operation this category may
        # state for every finite set, and the *object* supplies it: a group
        # knows its order, a prime field is of size p, a free module of rank n
        # over R has |R|^n elements.  Counting by materializing an enumeration
        # answers only for a set given by nothing else, and Sage already owns
        # that case (``FiniteEnumeratedSets``), so a count written here would
        # not add the answer -- it would take precedence over every object
        # that can state its own, which is the whole membership of this
        # category.

class InfiniteSets(CategoryWithAxiom):
    r"""Infinite sets: Sage's standard axiom supplies the uniform
    consequences (``is_finite() == False``, ``cardinality() == +Infinity``)
    through the join; nothing is reimplemented here."""

    _base_category_class_and_axiom = (Sets, "Infinite")


class CountableSets(CategoryWithAxiom):
    r"""Countable sets: the property that an injection into $\mathbb N$
    exists.

    Countability does not name an enumeration.  A set is countable when
    *some* injection into $\mathbb N$ exists, and a chosen one is extra
    data: the pair $(X, f\colon X\hookrightarrow U(\mathbb N))$ is an object
    of the slice over $U(\mathbb N)$, not a set carrying an adjective.  So
    this node declares the property and demands no enumeration; Sage's
    ``EnumeratedSets`` — parents that do come with a chosen one — is
    admitted as adapter machinery, which is what lets Sage's solved
    construction machinery (fair Cartesian-product iteration, disjoint
    unions) consume these natively, and is what supplies ``iter(X)`` where
    an enumeration was in fact chosen.
    """

    _base_category_class_and_axiom = (Sets, "Countable")

    class ParentMethods:
        if TYPE_CHECKING:
            def __iter__(self) -> Iterator[SageElement]: ...

        def _chosen_enumeration(self) -> Iterator[SageElement]:
            r"""The chosen enumeration of this set, as an iterator.

            Reading it is what :meth:`__getitem__` and :meth:`position` do, and
            the reason they cannot simply write ``iter(self)``: Python treats
            a type that defines ``__getitem__`` and no ``__iter__`` as a
            sequence, and iterates it *by calling* ``__getitem__``.  On such a
            parent ``iter(self)`` is this category's own accessor, so reading
            the enumeration through it would be reading itself.  A set with no
            ``__iter__`` has chosen no enumeration, and these operations --
            which are operations of a chosen one, never obligations of
            countability -- say so instead of descending.
            """
            from sage.categories.enumerated_sets import EnumeratedSets

            assert self in EnumeratedSets(), (
                f"{self} has chosen no enumeration: its parent is not in Sage's "
                "EnumeratedSets category, so "
                f"there is no order in which to index its elements. Countability "
                f"is the existence of an injection into the naturals and names no "
                f"enumeration; supply one to look up by position."
            )
            return iter(self)

        # Operations of a CHOSEN enumeration, available where one exists;
        # never obligations of countability.  ponytail: they read the
        # enumeration through iteration rather than through the slice object
        # that properly holds it -- see the module note on Slice(f).
        def __getitem__(self, n: int) -> SageElement:
            r"""The ``n``-th element of the chosen enumeration, ``n >= 0``."""
            assert n >= 0, f"enumeration indices are nonnegative; found {n}"
            for position, element in enumerate(self._chosen_enumeration()):
                if position == n:
                    return element
            assert False, f"index {n} exceeds the enumeration of {self}"

        def position(self, element: SageElement) -> int:
            r"""Reverse lookup in the chosen enumeration: terminates for
            members and satisfies ``X[X.position(x)] == x``. No termination
            promise for a nonmember of an infinite parent."""
            for position, candidate in enumerate(self._chosen_enumeration()):
                if candidate == element:
                    return position
            assert False, f"{element} is not in the enumeration of {self}"

        def enumeration_injection(self) -> "Sets.ArrowType":
            r"""The monomorphism into the SET of nonnegative integers
            realized by the chosen enumeration, ``x -> position(x)``, as an
            element of the actual homset — the constructed effective
            witness of countability. (The codomain is the underlying set of
            the naturals: the injection is a set map, so it forgets the
            semiring structure of its codomain.)"""
            # Quoted: ``cast`` evaluates its first argument, and Sage's
            # ``Parent`` is a Cython class that cannot be subscripted.
            domain = cast("SageParent[SageElement]", self)
            naturals = cast("SageParent[Integer]", NN)
            # naturals[n] IS the natural number n (identity enumeration),
            # already normalized into the host parent.
            return Sets().Hom(domain, naturals)(
                lambda element: naturals[self.position(element)]
            )

        def is_countable(self) -> bool:
            return True

        def is_uncountable(self) -> bool:
            return False


class CountablyInfiniteSets(CategoryWithAxiom):
    r"""Countably infinite sets — the join ``Sets().Countable().Infinite()``,
    never a new named root. Owns the exact cardinal: ``aleph_0``."""

    _base_category_class_and_axiom = (CountableSets, "Infinite")

    class ParentMethods:
        def cardinality(self) -> Cardinal:
            r"""``aleph_0``, exactly — not Sage's countable-blind
            ``+Infinity`` (to which it compares equal)."""
            from dzack_research.preamble.categories.sets.cardinals import aleph0

            return aleph0


class UncountableSets(CategoryWithAxiom):
    r"""Uncountable sets: trusted placement, uniform consequences, and in
    particular infinite."""

    _base_category_class_and_axiom = (Sets, "Uncountable")

    def extra_super_categories(self) -> list[SageCategory]:
        return [self.base_category().Infinite()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return False

        def is_uncountable(self) -> bool:
            return True


class PosetMorphism(SageMorphism):
    r"""Morphism of partially ordered sets (order-preserving map)."""

    def __init__(
        self,
        parent: PosetHomset,
        function: Callable[[PosetElement], PosetElement],
    ) -> None:
        SageMorphism.__init__(self, parent)
        self._function = function

    def __call__(self, x: PosetElement) -> PosetElement:
        return self._function(x)

    def is_order_preserving(self) -> bool:
        r"""Return True if x <= y implies f(x) <= f(y)."""
        dom = self.domain()
        codom = self.codomain()
        for x, y in dom.cover_relations():
            if not codom.is_lequal(self(x), self(y)):
                return False
        return True

    def is_order_reflecting(self) -> bool:
        r"""Return True if f(x) <= f(y) implies x <= y."""
        dom = self.domain()
        codom = self.codomain()
        for x in dom:
            for y in dom:
                if codom.is_lequal(self(x), self(y)) and not dom.is_lequal(x, y):
                    return False
        return True

    def is_order_embedding(self) -> bool:
        r"""Return True if x <= y iff f(x) <= f(y)."""
        return self.is_order_preserving() and self.is_order_reflecting()

    def is_injective(self) -> bool:
        r"""Return True if f is one-to-one."""
        images = [self(x) for x in self.domain()]
        return len(images) == len(set(images))

    def is_surjective(self) -> bool:
        r"""Return True if f maps onto the codomain."""
        images = set(self(x) for x in self.domain())
        return images == set(self.codomain())

    def is_bijective(self) -> bool:
        return self.is_injective() and self.is_surjective()

    def is_order_isomorphism(self) -> bool:
        r"""Return True if f is a bijective order embedding."""
        return self.is_order_embedding() and self.is_bijective()

    def inverse(self) -> "PosetMorphism":
        r"""Return the inverse poset isomorphism."""
        assert self.is_order_isomorphism(), (
            "inverse only exists for order isomorphisms"
        )
        inv_map = {self(x): x for x in self.domain()}
        return PosetHomset(self.codomain(), self.domain())(lambda y: inv_map[y])

    def __mul__(self, other: "PosetMorphism") -> "PosetMorphism":
        assert self.domain() == other.codomain(), (
            "domains and codomains do not match for composition"
        )
        return PosetHomset(other.domain(), self.codomain())(lambda x: self(other(x)))

    def _repr_(self) -> str:
        return f"Poset morphism from {self.domain()} to {self.codomain()}"


class PosetHomset(SageHomset):
    r"""Set of morphisms between partially ordered sets."""

    Element = PosetMorphism

    def _element_constructor_(
        self, f: Callable[[PosetElement], PosetElement]
    ) -> PosetMorphism:
        mor = PosetMorphism(self, f)
        assert mor.is_order_preserving(), (
            f"function {f} does not preserve the partial order "
            "(not a poset homomorphism)"
        )
        return mor


class PosetTikz:
    r"""TikZ Hasse diagram representation."""

    def __init__(
        self,
        poset: FinitePoset,
        label_map: Callable[[PosetElement], str] | None = None,
        scale: float = 1.0,
        width: int = 580,
        height: int = 440,
        theme: str = "dark",
    ) -> None:
        self._poset = poset
        self._label_map = label_map
        self._scale = scale
        self._width = width
        self._height = height
        self._theme = theme
        self._coords = self._compute_layout()

    def _compute_layout(self) -> dict[PosetElement, tuple[float, float]]:
        heights: dict[PosetElement, int] = {}
        for v in self._poset.linear_extension():
            low = self._poset.lower_covers(v)
            if not low:
                heights[v] = 0
            else:
                heights[v] = max(heights[u] for u in low) + 1

        max_h = max(heights.values()) if heights else 0
        levels: dict[int, list[PosetElement]] = {h: [] for h in range(max_h + 1)}
        for v, h in heights.items():
            levels[h].append(v)

        coords: dict[PosetElement, tuple[float, float]] = {}
        for h in range(max_h + 1):
            elems = list(levels[h])
            if h > 0:
                def avg_pred_x(v: PosetElement) -> float:
                    preds = self._poset.lower_covers(v)
                    if preds and any(u in coords for u in preds):
                        return sum(coords[u][0] for u in preds if u in coords) / len(preds)
                    return 0.0
                elems.sort(key=lambda v: (avg_pred_x(v), str(v)))

            m = len(elems)
            for i, v in enumerate(elems):
                x = (i - (m - 1) / 2.0) * 2.0
                y = float(h * 2.0)
                coords[v] = (x, y)

        return coords

    def tikz_code(self) -> str:
        node_id_map = {v: f"node_{i}" for i, v in enumerate(self._poset)}
        lines = [
            r"\begin{tikzpicture}[",
            f"  scale={self._scale:.2f},",
            r"  every node/.style={circle, draw=black!80, fill=blue!10, inner sep=2pt, minimum size=18pt, font=\small},",
            r"  edge/.style={draw=black!70, thick, ->, >=stealth}",
            r"]",
        ]
        for v, (x, y) in self._coords.items():
            lbl = str(self._label_map(v) if self._label_map else v)
            nid = node_id_map[v]
            lines.append(f"  \\node ({nid}) at ({x:.2f}, {y:.2f}) {{{lbl}}};")
        for u, v in self._poset.cover_relations():
            nid_u = node_id_map[u]
            nid_v = node_id_map[v]
            lines.append(f"  \\draw[edge] ({nid_u}) -> ({nid_v});")
        lines.append(r"\end{tikzpicture}")
        return "\n".join(lines)

    def _repr_(self) -> str:
        return self.tikz_code()

    def _latex_(self) -> str:
        return self.tikz_code()

    def _repr_latex_(self) -> str:
        return f"$$\n{self.tikz_code()}\n$$"

    def _repr_html_(self) -> str:
        import math
        import uuid
        uid = f"hasse_{uuid.uuid4().hex[:8]}"

        if not self._coords:
            return f'<div id="{uid}">Empty Poset</div>'

        margin = 50
        xs = [float(pt[0]) for pt in self._coords.values()]
        ys = [float(pt[1]) for pt in self._coords.values()]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        span_x = (max_x - min_x) if max_x > min_x else 1.0
        span_y = (max_y - min_y) if max_y > min_y else 1.0

        px_coords = {}
        for v, (x, y) in self._coords.items():
            px_x = margin + (float(x) - min_x) / span_x * (self._width - 2 * margin)
            px_y = (self._height - margin) - (float(y) - min_y) / span_y * (self._height - 2 * margin)
            px_coords[v] = (px_x, px_y)

        node_radius = 16
        initial_theme = self._theme if self._theme in ("dark", "light") else "dark"
        btn_label = "🌙 Dark" if initial_theme == "dark" else "☀️ Light"

        lines = [
            f'<div id="{uid}" class="hasse-container" data-theme="{initial_theme}" style="display: inline-block; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif; border-radius: 12px; overflow: hidden; margin: 12px 0; box-shadow: 0 4px 20px rgba(0,0,0,0.15); transition: background-color 0.25s, border-color 0.25s;">',
            "  <style>",
            f"    #{uid}[data-theme=\"dark\"] {{",
            "      background: #0f172a;",
            "      border: 1px solid #1e293b;",
            "      color: #f8fafc;",
            "    }",
            f"    #{uid}[data-theme=\"light\"] {{",
            "      background: #ffffff;",
            "      border: 1px solid #e2e8f0;",
            "      color: #0f172a;",
            "    }",
            f"    #{uid} .hasse-header {{",
            "      display: flex;",
            "      justify-content: space-between;",
            "      align-items: center;",
            "      padding: 8px 14px;",
            "      font-size: 12px;",
            "      font-weight: 600;",
            "      border-bottom: 1px solid rgba(128,128,128,0.15);",
            "    }",
            f"    #{uid} .theme-btn {{",
            "      background: rgba(128,128,128,0.15);",
            "      border: none;",
            "      border-radius: 6px;",
            "      padding: 4px 8px;",
            "      font-size: 11px;",
            "      font-weight: 500;",
            "      cursor: pointer;",
            "      color: inherit;",
            "      display: flex;",
            "      align-items: center;",
            "      gap: 4px;",
            "      transition: background 0.15s;",
            "    }",
            f"    #{uid} .theme-btn:hover {{",
            "      background: rgba(128,128,128,0.28);",
            "    }",
            f"    #{uid}[data-theme=\"dark\"] .hasse-edge {{",
            "      stroke: #475569;",
            "      stroke-width: 2;",
            f"      marker-end: url(#{uid}_arrow_dark);",
            "    }",
            f"    #{uid}[data-theme=\"light\"] .hasse-edge {{",
            "      stroke: #94a3b8;",
            "      stroke-width: 2;",
            f"      marker-end: url(#{uid}_arrow_light);",
            "    }",
            f"    #{uid}[data-theme=\"dark\"] .hasse-node {{",
            "      fill: #1e293b;",
            "      stroke: #38bdf8;",
            "      stroke-width: 2;",
            "      transition: all 0.2s;",
            "    }",
            f"    #{uid}[data-theme=\"dark\"] .hasse-node:hover {{",
            "      fill: #0284c7;",
            "      stroke: #7dd3fc;",
            "      stroke-width: 3;",
            "    }",
            f"    #{uid}[data-theme=\"light\"] .hasse-node {{",
            "      fill: #f8fafc;",
            "      stroke: #2563eb;",
            "      stroke-width: 2;",
            "      transition: all 0.2s;",
            "    }",
            f"    #{uid}[data-theme=\"light\"] .hasse-node:hover {{",
            "      fill: #dbeafe;",
            "      stroke: #1d4ed8;",
            "      stroke-width: 3;",
            "    }",
            f"    #{uid}[data-theme=\"dark\"] .hasse-text {{",
            "      fill: #f8fafc;",
            "      font-size: 11px;",
            "      font-weight: 600;",
            "      text-anchor: middle;",
            "      dominant-baseline: central;",
            "      pointer-events: none;",
            "    }",
            f"    #{uid}[data-theme=\"light\"] .hasse-text {{",
            "      fill: #0f172a;",
            "      font-size: 11px;",
            "      font-weight: 600;",
            "      text-anchor: middle;",
            "      dominant-baseline: central;",
            "      pointer-events: none;",
            "    }",
            "  </style>",
            '  <div class="hasse-header">',
            f'    <span>Hasse Diagram ({len(self._coords)} elements)</span>',
            f'    <button class="theme-btn" onclick="(function(){{ var el = document.getElementById(\'{uid}\'); var cur = el.getAttribute(\'data-theme\'); var next = cur === \'dark\' ? \'light\' : \'dark\'; el.setAttribute(\'data-theme\', next); document.getElementById(\'{uid}_btn_text\').innerText = next === \'dark\' ? \'🌙 Dark\' : \'☀️ Light\'; }})()"><span id="{uid}_btn_text">{btn_label}</span></button>',
            "  </div>",
            f'  <svg width="{self._width}" height="{self._height}" viewBox="0 0 {self._width} {self._height}" xmlns="http://www.w3.org/2000/svg">',
            "    <defs>",
            f'      <marker id="{uid}_arrow_dark" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
            '        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8" />',
            "      </marker>",
            f'      <marker id="{uid}_arrow_light" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
            '        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb" />',
            "      </marker>",
            "    </defs>",
        ]

        for u, v in self._poset.cover_relations():
            x1, y1 = px_coords[u]
            x2, y2 = px_coords[v]
            dx = x2 - x1
            dy = y2 - y1
            dist = math.hypot(dx, dy)
            if dist > 34:
                ux = dx / dist
                uy = dy / dist
                sx = x1 + ux * (node_radius + 1)
                sy = y1 + uy * (node_radius + 1)
                ex = x2 - ux * (node_radius + 5)
                ey = y2 - uy * (node_radius + 5)
            else:
                sx, sy, ex, ey = x1, y1, x2, y2
            lines.append(f'    <line class="hasse-edge" x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" />')

        for v, (x, y) in px_coords.items():
            lbl = str(self._label_map(v) if self._label_map else v)
            if len(lbl) > 12:
                lbl = lbl[:10] + ".."
            lines.append(f'    <circle class="hasse-node" cx="{x:.1f}" cy="{y:.1f}" r="{node_radius}" />')
            lines.append(f'    <text class="hasse-text" x="{x:.1f}" y="{y:.1f}">{lbl}</text>')

        lines.append("  </svg>\n</div>")
        return "\n".join(lines)


def _poset_repr_html(poset: FinitePoset) -> str:
    return PosetTikz(poset)._repr_html_()


def _poset_latex(poset: FinitePoset) -> str:
    return PosetTikz(poset).tikz_code()


def _poset_repr_latex(poset: FinitePoset) -> str:
    return rf"\(\displaystyle {_poset_latex(poset)}\)"


def _poset_rich_repr(
    poset: FinitePoset, dm: DisplayManager
) -> OutputBase | None:
    if hasattr(dm, "types") and hasattr(dm, "supported_output"):
        if dm.types.OutputHtml in dm.supported_output():
            html_content = _poset_repr_html(poset)
            return dm.types.OutputHtml(html_content)
        elif dm.types.OutputLatex in dm.supported_output():
            return dm.types.OutputLatex(_poset_latex(poset))
        elif dm.types.OutputPlainText in dm.supported_output():
            return dm.types.OutputPlainText(repr(poset))
    return None


def _poset_repr_mimebundle(
    poset: FinitePoset,
    include: Iterable[str] | None = None,
    exclude: Iterable[str] | None = None,
) -> dict[str, str]:
    return {
        "text/html": _poset_repr_html(poset),
        "text/latex": _poset_repr_latex(poset),
        "text/plain": repr(poset),
    }


class PartiallyOrderedSets(CategoryWithAxiom):
    r"""Partially ordered sets."""

    _base_category_class_and_axiom = (Sets, "PartiallyOrdered")

    class ParentMethods:
        def hasse_layout(self) -> dict[PosetElement, tuple[float, float]]:
            r"""Compute ranked (x, y) coordinates for the Hasse diagram without dot2tex."""
            pt = PosetTikz(self)
            return pt._coords

        def hasse_tikz(
            self,
            label_map: Callable[[PosetElement], str] | None = None,
            scale: float = 1.0,
        ) -> PosetTikz:
            r"""Return a PosetTikz representation of the Hasse diagram."""
            return PosetTikz(self, label_map=label_map, scale=scale)

        def tikz(
            self,
            label_map: Callable[[PosetElement], str] | None = None,
            scale: float = 1.0,
        ) -> PosetTikz:
            r"""Alias for :meth:`hasse_tikz`."""
            return self.hasse_tikz(label_map=label_map, scale=scale)

        def _repr_html_(self) -> str:
            r"""Render clean inline SVG in Jupyter notebook without dot2tex warnings."""
            return _poset_repr_html(self)

        def _latex_(self) -> str:
            return _poset_latex(self)

        def _repr_latex_(self) -> str:
            return _poset_repr_latex(self)

        def _rich_repr_(self, dm: DisplayManager) -> OutputBase | None:
            return _poset_rich_repr(self, dm)

        def _repr_mimebundle_(
            self,
            include: Iterable[str] | None = None,
            exclude: Iterable[str] | None = None,
        ) -> dict[str, str]:
            return _poset_repr_mimebundle(self, include=include, exclude=exclude)


def install_poset_display() -> None:
    r"""Route Sage's ``FinitePoset`` into ``PartiallyOrderedSets``.

    The category owns the Hasse-diagram display methods
    (``PartiallyOrderedSets.ObjectType`` above); this hook refines every
    finite poset Sage constructs into that category after ``__init__`` -- the
    sanctioned refinement route, never a monkey-patch onto Sage's class, and
    a failure here is loud.

    Called from the install sequence, like every other ``install_*`` hook, and
    never at import.  It constructs a category (``Sets().PartiallyOrdered()``),
    and constructing an owned category needs ``Cat()``; firing that from module
    scope re-enters the import of ``cat`` and fails with a partially
    initialized module.
    """
    from sage.combinat.posets.posets import FinitePoset

    from dzack_research.preamble.refine import hook_post_init

    hook_post_init(FinitePoset, Sets().PartiallyOrdered())


class TotallyOrderedSets(CategoryWithAxiom):
    r"""Totally ordered sets."""

    _base_category_class_and_axiom = (Sets, "TotallyOrdered")

    def extra_super_categories(self) -> list[SageCategory]:
        return [self.base_category().PartiallyOrdered()]


_SET_AXIOM_NAMES = (
    "Finite",
    "Infinite",
    "Countable",
    "Uncountable",
    "PartiallyOrdered",
    "TotallyOrdered",
)


def placement_of(parent: SageParent[_E]) -> Sets:
    r"""The owned ``Sets()`` placement a parent's declared axioms carry.

    Countability, finiteness and order are answers this parent already
    declares; reading them off is how an object enters the owned sets able
    to answer what ``Sets`` declares abstract.  When no cardinality axiom is
    declared, the category-owned cardinality determines finite, countable,
    or uncountable placement.  Contradictory declarations are refused by the
    owned axiom guards at translation time.  Sage's raw ``+Infinity`` does not
    identify an infinite cardinal and therefore supplies no derived placement.

    Sage's ``Enumerated`` witnesses countability without being it: it
    asserts a *chosen* enumeration, and exhibiting one injection into
    $\mathbb N$ proves the property.  Only the property is recorded here;
    the chosen enumeration is the structure map of a slice object over
    $U(\mathbb N)$ and does not travel in a ``Sets`` placement.
    """
    declared = frozenset(parent.category().axioms())
    axioms = declared & frozenset(_SET_AXIOM_NAMES)
    placement = Sets()
    if "Finite" in axioms:
        placement = placement.Finite()
    elif "Countable" in axioms or "Enumerated" in declared:
        placement = placement.Countable()
    elif not {"Finite", "Countable", "Uncountable"} & axioms:
        from sage.rings.infinity import Infinity

        from dzack_research.preamble.categories.sets.cardinals import cardinal

        try:
            declared_cardinality = parent.cardinality()
        except AttributeError:
            declared_cardinality = None
        if declared_cardinality is not None and declared_cardinality != Infinity:
            cardinality = cardinal(declared_cardinality)
            if cardinality.is_finite():
                placement = placement.Finite()
            elif cardinality.is_countable():
                placement = placement.Countable()
            else:
                placement = placement.Uncountable()
    if "Uncountable" in axioms:
        placement = placement.Uncountable()
    elif "Infinite" in axioms:
        placement = placement.Infinite()
    if "TotallyOrdered" in axioms:
        placement = placement.TotallyOrdered()
    elif "PartiallyOrdered" in axioms:
        placement = placement.PartiallyOrdered()
    else:
        from sage.categories.posets import Posets as SagePosets
        if parent.category().is_subcategory(SagePosets()):
            placement = placement.PartiallyOrdered()
    return placement


if not TYPE_CHECKING:
    # Sage's class-resolution shortcut: the axiom category class must be
    # reachable as `<BaseCategory>.<Axiom>` for `_base_category_class_and_axiom`
    # to resolve. Runtime-only wiring; the typed surface of these names is the
    # axiom-navigation method declarations on the category class above.
    Sets.Finite = FiniteSets
    Sets.Infinite = InfiniteSets
    Sets.Countable = CountableSets
    Sets.Uncountable = UncountableSets
    Sets.PartiallyOrdered = PartiallyOrderedSets
    Sets.TotallyOrdered = TotallyOrderedSets
    CountableSets.Infinite = CountablyInfiniteSets
