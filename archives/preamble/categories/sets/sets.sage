r"""Owned sets used by the preamble.

The owned ``Sets()`` root and its axioms live in ``owned_sets.py``.  This
module keeps the preamble inside that category while reusing Sage's concrete
set parents, and it declares the set constructions built on a set: the power
object, the subsets of one fixed cardinality, and the finite subsets.  It
also supplies the canonical finite ordinals and the construction that
transports the order of a finite enumeration.  An arbitrary parent is not
declared ordered merely because it can be iterated.
"""

from __future__ import annotations

from sage.rings.semirings.non_negative_integer_semiring import NN
from dzack_research.preamble.refine import refine

from collections.abc import Callable, Hashable, Iterable, Iterator, Sequence
from typing import TYPE_CHECKING, TypeVar

from sage.categories.category import Category as SageCategory
from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.rings.integer import Integer as SageInteger
from sage.rings.integer_ring import ZZ as SageZZ
from sage.sets.condition_set import ConditionSet as SageConditionSet
from sage.sets.image_set import ImageSet as SageImageSet
from sage.sets.integer_range import IntegerRange
from sage.sets.set import Set as SageSet
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.sets.cardinals import Cardinal
from dzack_research.preamble.categories.sets.owned_sets import (
    Sets,
    placement_of,
)
from dzack_research.preamble.categories.abstract_categories.functors import (
    CoproductFunctor,
    DiscreteCategories,
    DiscreteCategory,
    DiscreteDiagram,
    Functor,
    NaturalTransformation,
    ProductFunctor,
)
from dzack_research.preamble.categories.abstract_categories.functor_images import (
    _FunctorImageParameters,
    ImageOfFunctor,
)
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category, CategoryWithParameters

if TYPE_CHECKING:
    # Type-only: the preamble loads into one shared namespace and nothing
    # named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.structure.parent import ElementConstructorInput
    from sage.categories.morphism import Morphism
    from sage.categories.poor_man_map import PoorManMap
    from dzack_research.preamble.categories.sets.cardinals import (
        Cardinal,
        CardinalityMorphism,
    )
    from dzack_research.preamble.categories.sets.owned_sets import SetMapDefinition


def Set(source: Parent | Iterable[Element]) -> "lexicon.Set":
    r"""Return ``source`` as an object of the owned category of sets."""
    if source in Sets():
        return source
    match source:
        case Parent():
            result = SageSet(source)
        case Iterable():
            result = SageSet(source)
        case _:
            assert False, (
                f"a set is constructed from a parent or iterable, got {source!r}"
            )
    if result in Sets():
        return result
    return refine(result, placement_of(result))


def ConditionSet(
    universe: "lexicon.Set",
    *predicates: "Element",
    names: "OrderedSet | None" = None,
) -> "lexicon.Set":
    r"""Construct a predicate-defined object of the owned category of sets."""
    result = SageConditionSet(universe, *predicates, names=names)
    return refine(result, placement_of(result))


def ImageSet(
    map_: "Morphism | PoorManMap",
    domain_subset: "lexicon.Set",
    *,
    category: "SageCategory | None" = None,
    is_injective: bool | None = None,
    inverse: "Morphism | None" = None,
) -> "lexicon.Set":
    r"""Construct an image object in the owned category of sets."""
    result = SageImageSet(
        map_,
        domain_subset,
        category=category,
        is_injective=is_injective,
        inverse=inverse,
    )
    return refine(result, placement_of(result))


def _cartesian_product_placement(factors: tuple[Parent, ...]) -> Sets:
    r"""Return the cardinality placement of a finite cartesian product."""
    if not factors or any(factor.cardinality() == 0 for factor in factors):
        return Sets().Finite()
    axiom_families = [frozenset(placement_of(factor).axioms()) for factor in factors]
    if all("Finite" in axioms for axioms in axiom_families):
        return Sets().Finite()
    if all(
        "Finite" in axioms or "Countable" in axioms
        for axioms in axiom_families
    ):
        return Sets().Countable()
    if any("Uncountable" in axioms for axioms in axiom_families):
        return Sets().Uncountable()
    if any("Infinite" in axioms for axioms in axiom_families):
        return Sets().Infinite()
    return Sets()


def _coproduct_placement(cofactors: tuple[Parent, ...]) -> Sets:
    r"""Return the cardinality placement of a finite disjoint union."""
    axiom_families = [
        frozenset(placement_of(cofactor).axioms())
        for cofactor in cofactors
    ]
    if all("Finite" in axioms for axioms in axiom_families):
        return Sets().Finite()
    if all(
        "Finite" in axioms or "Countable" in axioms
        for axioms in axiom_families
    ):
        return Sets().Countable()
    if any("Uncountable" in axioms for axioms in axiom_families):
        return Sets().Uncountable()
    if any("Infinite" in axioms for axioms in axiom_families):
        return Sets().Infinite()
    return Sets()


def _placement_for_cardinality(size: Cardinal) -> Sets:
    r"""Return the strongest Set placement decided by one cardinal."""
    if size.is_finite():
        return Sets().Finite()
    if size.is_countable():
        return Sets().Countable().Infinite()
    if size.is_uncountable():
        return Sets().Uncountable()
    if size.is_infinite():
        return Sets().Infinite()
    return Sets()


class ObjectSetFunctor(Functor):
    r"""The object-set functor from discrete categories to sets."""

    def __init__(self) -> None:
        Functor.__init__(self, DiscreteCategories(), Sets())

    def _image_category(self) -> SageCategory:
        return ObjectSetsOfDiscreteCategories(self)

    @cached_method
    def _apply_functor(self, category: SageCategory) -> Parent:
        return object_of(self.Image(), preimage=category)

    def _apply_functor_to_morphism(self, functor: Element) -> "Sets.ArrowType":
        source = self(functor.domain())
        target = self(functor.codomain())
        return Sets().Hom(source, target)(lambda obj: functor(obj))


class CartesianProductFunctor(ProductFunctor):
    r"""The product functor on Set-valued diagrams of one discrete shape."""

    def _image_category(self) -> SageCategory:
        return Sets._Products(self)

    @cached_method
    def _apply_functor(self, diagram: Functor) -> Parent:
        assert diagram.domain() is self.index_category()
        indices = diagram.domain().objects()
        placement = Sets()
        if indices in Sets().Finite():
            placement = _cartesian_product_placement(
                tuple(diagram(index) for index in indices)
            )
        image = self.Image()
        return object_of(
            SageCategory.join((image, placement)),
            preimage=diagram,
        )


class DisjointUnionFunctor(CoproductFunctor):
    r"""The coproduct functor on Set-valued diagrams of one discrete shape."""

    def _image_category(self) -> SageCategory:
        return Sets._Coproducts(self)

    @cached_method
    def _apply_functor(self, diagram: Functor) -> Parent:
        assert diagram.domain() is self.index_category()
        indices = diagram.domain().objects()
        placement = Sets()
        if indices in Sets().Finite():
            placement = _coproduct_placement(
                tuple(diagram(index) for index in indices)
            )
        image = self.Image()
        return object_of(
            SageCategory.join((image, placement)),
            preimage=diagram,
        )


class ExponentialFunctor(Functor):
    r"""The internal-hom bifunctor :math:`\mathbf{Set}^{op}\times\mathbf{Set}\to\mathbf{Set}`."""

    def __init__(self) -> None:
        domain = Sets().OppositeCategory().ProductCategory(Sets())
        Functor.__init__(self, domain, Sets())

    def _image_category(self) -> SageCategory:
        return ExponentialsOfSets(self)

    @cached_method
    def _apply_functor(self, pair: Element) -> Parent:
        from dzack_research.preamble.categories.sets.cardinals import Cardinalities

        size = Cardinalities().power(
            pair.second().cardinality(),
            pair.first().cardinality(),
        )
        return object_of(
            SageCategory.join((self.Image(), _placement_for_cardinality(size))),
            preimage=pair,
        )

    def _apply_functor_to_morphism(self, pair: Element) -> "Sets.ArrowType":
        source = self(pair.domain())
        target = self(pair.codomain())
        precompose = pair.first().underlying_arrow()
        postcompose = pair.second()
        return Sets().Hom(source, target)(
            lambda function: target(
                lambda element: postcompose(function(precompose(element)))
            )
        )


class InverseImagePowerSetFunctor(Functor):
    r"""The contravariant power-set functor, represented on ``Sets().OppositeCategory()``."""

    def __init__(self) -> None:
        Functor.__init__(self, Sets().OppositeCategory(), Sets())

    def _image_category(self) -> SageCategory:
        return PowerSets(self)

    @cached_method
    def _apply_functor(self, base_set: Parent) -> Parent:
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        size = cardinal(2) ** base_set.cardinality()
        return object_of(
            SageCategory.join((self.Image(), _placement_for_cardinality(size))),
            preimage=base_set,
        )

    def _apply_functor_to_morphism(self, morphism: Element) -> "Sets.ArrowType":
        source = self(morphism.domain())
        return source.inverse_image_morphism(morphism.underlying_arrow())


class FinitePowerSetFunctor(Functor):
    r"""The covariant finite-power-set functor under direct image."""

    def __init__(self) -> None:
        Functor.__init__(self, Sets(), Sets())

    def _image_category(self) -> SageCategory:
        return FinitePowerSets(self)

    def image_cardinality(self, source: Parent) -> Cardinal:
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        source_cardinality = cardinal(source.cardinality())
        if source_cardinality.is_finite():
            return cardinal(2) ** source_cardinality
        return source_cardinality

    @cached_method
    def _apply_functor(self, source: Parent) -> Parent:
        categories = [
            self.Image(),
            _placement_for_cardinality(self.image_cardinality(source)),
        ]
        if source in Sets().Countable():
            categories.append(SageEnumeratedSets())
        return object_of(
            SageCategory.join(categories),
            preimage=source,
        )

    def _apply_functor_to_morphism(
        self,
        morphism: "Sets.ArrowType",
    ) -> "Sets.ArrowType":
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return Sets().Hom(source, target)(
            lambda subset: target(tuple(morphism(member) for member in subset))
        )


class FixedCardinalitySubsetFunctor(Functor):
    r"""Direct image on subsets of one finite cardinality, along injections."""

    def __init__(self, subset_cardinality: SageInteger) -> None:
        self._subset_cardinality = SageInteger(subset_cardinality)
        assert self._subset_cardinality >= 0, "a subset cardinality is nonnegative"
        domain = Sets().WideSubcategory(Sets().MonomorphismArrowCategory())
        Functor.__init__(self, domain, Sets())

    def subset_cardinality(self) -> SageInteger:
        return self._subset_cardinality

    def _image_category(self) -> SageCategory:
        return FixedCardinalitySubsets(self)

    def image_cardinality(self, source: Parent) -> Cardinal:
        from sage.arith.misc import binomial

        from dzack_research.preamble.categories.sets.cardinals import cardinal

        source_cardinality = cardinal(source.cardinality())
        if self._subset_cardinality == 0:
            return cardinal(1)
        if source_cardinality.is_finite():
            return cardinal(
                binomial(SageZZ(source_cardinality), self._subset_cardinality)
            )
        return source_cardinality

    @cached_method
    def _apply_functor(self, source: Parent) -> Parent:
        categories = [
            self.Image(),
            _placement_for_cardinality(self.image_cardinality(source)),
        ]
        if source in Sets().Countable():
            categories.append(SageEnumeratedSets())
        return object_of(
            SageCategory.join(categories),
            preimage=source,
        )

    def _apply_functor_to_morphism(
        self,
        morphism: "Sets.MonoArrowType",
    ) -> "Sets.ArrowType":
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return Sets().Hom(source, target)(
            lambda subset: target(tuple(morphism(member) for member in subset))
        )


def CartesianProductOfFamily(
    index_set: Parent,
    factors: "Callable[[ElementConstructorInput], Parent]",
) -> Parent:
    r"""Return the product of a set-indexed family of sets."""
    index_category = DiscreteCategory(index_set)
    diagram = DiscreteDiagram(index_category, Sets(), factors)
    return Sets().ProductFunctor(index_category)(diagram)


def CartesianProductOfSets(factors: Iterable[Parent]) -> Parent:
    r"""Return the product of a finite sequence of sets."""
    family = tuple(factors)
    indices = Sets.Δ[len(family) - 1]
    return CartesianProductOfFamily(
        indices,
        lambda index: family[int(index)],
    )


def CartesianProductMorphismOfFamily(
    index_set: Parent,
    maps: "Callable[[ElementConstructorInput], Sets.ArrowType]",
) -> "Sets.ArrowType":
    r"""Apply the product functor to an indexed natural transformation."""
    index_category = DiscreteCategory(index_set)
    source = DiscreteDiagram(
        index_category,
        Sets(),
        lambda index: maps(index).domain(),
    )
    target = DiscreteDiagram(
        index_category,
        Sets(),
        lambda index: maps(index).codomain(),
    )
    transformation = NaturalTransformation(
        source,
        target,
        maps,
    )
    return Sets().ProductFunctor(index_category)(transformation)


def cartesian_product_morphism(*maps: "Sets.ArrowType") -> "Sets.ArrowType":
    r"""Return the componentwise morphism between finite products."""
    map_family = tuple(maps)
    indices = Sets.Δ[len(map_family) - 1]
    return CartesianProductMorphismOfFamily(
        indices,
        lambda index: map_family[int(index)],
    )


def CoproductOfFamily(
    index_set: Parent,
    cofactors: "Callable[[ElementConstructorInput], Parent]",
) -> Parent:
    r"""Return the coproduct of a set-indexed family of sets."""
    index_category = DiscreteCategory(index_set)
    diagram = DiscreteDiagram(index_category, Sets(), cofactors)
    return Sets().CoproductFunctor(index_category)(diagram)


def CoproductOfSets(cofactors: Iterable[Parent]) -> Parent:
    r"""Return the coproduct of a finite sequence of sets."""
    family = tuple(cofactors)
    indices = Sets.Δ[len(family) - 1]
    return CoproductOfFamily(
        indices,
        lambda index: family[int(index)],
    )


def CoproductMorphismOfFamily(
    index_set: Parent,
    maps: "Callable[[ElementConstructorInput], Sets.ArrowType]",
) -> "Sets.ArrowType":
    r"""Apply the coproduct functor to an indexed natural transformation."""
    index_category = DiscreteCategory(index_set)
    source = DiscreteDiagram(
        index_category,
        Sets(),
        lambda index: maps(index).domain(),
    )
    target = DiscreteDiagram(
        index_category,
        Sets(),
        lambda index: maps(index).codomain(),
    )
    transformation = NaturalTransformation(source, target, maps)
    return Sets().CoproductFunctor(index_category)(transformation)


def coproduct_morphism(*maps: "Sets.ArrowType") -> "Sets.ArrowType":
    r"""Return the componentwise morphism between finite coproducts."""
    map_family = tuple(maps)
    indices = Sets.Δ[len(map_family) - 1]
    return CoproductMorphismOfFamily(
        indices,
        lambda index: map_family[int(index)],
    )


class ObjectSetsOfDiscreteCategories(
    _FunctorImageParameters,
    CategoryWithParameters,
):
    r"""Object sets of discrete categories."""

    def super_categories(self) -> list[SageCategory]:
        return [ImageOfFunctor(self.functor())]

    def _repr_object_names(self) -> str:
        return "object sets of discrete categories"

    class ParentMethods:
        def discrete_category(self) -> SageCategory:
            return self.preimage()

        def __contains__(self, candidate: ElementConstructorInput) -> bool:
            return candidate in self.discrete_category()

        def _element_constructor_(
            self,
            candidate: ElementConstructorInput,
        ) -> ElementConstructorInput:
            assert candidate in self
            return candidate

        def _repr_(self) -> str:
            return f"Objects of {self.discrete_category()}"


@cached_function
def object_set_functor() -> ObjectSetFunctor:
    r"""Return the object-set functor on discrete categories."""
    return ObjectSetFunctor()


@cached_function
def ObjectSet(discrete_category: SageCategory) -> Parent:
    r"""Return the set of objects of ``discrete_category``."""
    assert discrete_category in DiscreteCategories()
    return object_set_functor()(discrete_category)


class ExponentialsOfSets(_FunctorImageParameters, CategoryWithParameters):
    r"""Function sets \(Y^X\), as the object sets of Set hom categories."""

    def super_categories(self) -> list[SageCategory]:
        return [ImageOfFunctor(self.functor())]

    def _repr_object_names(self) -> str:
        return "exponentials of sets"

    class ParentMethods:
        def base(self) -> Parent:
            return self.preimage().second()

        def exponent(self) -> Parent:
            return self.preimage().first()

        def hom_category(self) -> SageCategory:
            return Sets().Hom(self.exponent(), self.base())

        def __contains__(self, function: "Sets.ArrowType") -> bool:
            return function in self.hom_category()

        def _element_constructor_(
            self,
            definition: "SetMapDefinition | Sets.ArrowType",
        ) -> "Sets.ArrowType":
            return self.hom_category()(definition)

        def cardinality(self) -> Cardinal:
            from dzack_research.preamble.categories.sets.cardinals import (
                Cardinalities,
            )

            return Cardinalities().power(
                self.base().cardinality(),
                self.exponent().cardinality(),
            )

        def _repr_(self) -> str:
            return f"{self.base()}^{self.exponent()}"


@cached_function
def ExponentialOfSets(codomain: Parent, exponent: Parent) -> Parent:
    r"""Return \(Y^X\), the set of functions from ``exponent`` to ``codomain``."""
    assert codomain in Sets() and exponent in Sets()
    functor = Sets().ExponentialFunctor()
    pair = functor.domain()(exponent, codomain)
    return functor(pair)


def _has_canonical_set_inclusion(domain: Parent, codomain: Parent) -> bool:
    r"""Return whether the standard catalogue supplies ``domain -> codomain``.

    Sage defines ``NN`` as the nonnegative integers and ``ZZ`` as the integer
    ring.  The inclusion below is the set map induced by those canonical Sage
    parents; it is not inferred from enumeration.
    """
    from dzack_research.preamble.categories.rings.rings import engine_ring
    return domain is NN and engine_ring(codomain) is SageZZ


class SubsetsOfSet(CategoryWithParameters):
    r"""The canonical set-valued subobjects of one set.

    This category only fixes the codomain of a Set monomorphism.  The generic
    subobject structure comes from ``Sets().Subobjects(X)``.  Set-specific
    characteristic morphisms and Boolean operations belong to
    ``Sets.MonoArrowType``.
    """

    def __init__(self, base_set: "lexicon.Set") -> None:
        self._base_set = base_set
        super().__init__()

    def super_categories(self) -> list[SageCategory]:
        return [Sets().Subobjects(self._base_set)]

    def _make_named_class_key(self, name: str) -> SageCategory:
        return Sets()

    def _repr_object_names(self) -> str:
        return f"subsets of {self._base_set}"

    def __contains__(self, candidate: "ElementConstructorInput") -> bool:
        return (
            candidate in Sets().Subobjects(self._base_set)
            and candidate.parent() in Sets().MonoCategory()
        )


class PowerSets(_FunctorImageParameters, CategoryWithParameters):
    r"""The power object of a set.

    An object is \(P(X)\) for a set \(X\).  Its elements are subobjects of
    \(X\): each has an inclusion into \(X\) and the equivalent characteristic
    morphism into ``Delta[1]``.

    The construction is the image of the contravariant power-set functor.
    Thus the object retains only its preimage \(X\); its complete Set
    implementation comes from the functor codomain.
    """

    def super_categories(self) -> list[SageCategory]:
        return [ImageOfFunctor(self.functor())]

    def _repr_object_names(self) -> str:
        return "power sets"

    class ParentMethods:
        r"""\(P(X)\): the subobjects of the base set \(X\)."""

        def base_set(self) -> "lexicon.Set":
            return self.preimage()

        def characteristic_hom_category(self) -> SageCategory:
            r"""Return ``Hom(base_set, Delta[1])``."""
            return Sets().Hom(self.base_set(), Sets.Δ[1])

        def _from_subset(
            self,
            subset: "lexicon.Set",
            characteristic_morphism: "Sets.ArrowType",
            members: "frozenset[Element] | None" = None,
        ) -> "Sets.MonoArrowType":
            set_arrow = Sets().Hom(subset, self.base_set())(
                lambda member: self.base_set()(member)
            )
            inclusion = Sets().Mono(subset, self.base_set())(set_arrow)
            inclusion._power_set = self
            inclusion._characteristic_morphism = characteristic_morphism
            inclusion._members = members
            assert inclusion in SubsetsOfSet(self.base_set())
            return inclusion

        def _subset_from_predicate(
            self,
            predicate: "Callable[[Element], bool]",
        ) -> "Sets.MonoArrowType":
            subset = ConditionSet(self.base_set(), predicate)
            truth_values = Sets.Δ[1]
            characteristic_morphism = self.characteristic_hom_category()(
                lambda member: truth_values(SageInteger(predicate(member)))
            )
            return self._from_subset(subset, characteristic_morphism)

        def _subset_from_finite_members(
            self,
            members: "lexicon.Set",
        ) -> "Sets.MonoArrowType":
            subset = ConditionSet(self.base_set(), lambda member: member in members)
            truth_values = Sets.Δ[1]
            characteristic_morphism = self.characteristic_hom_category()(
                lambda member: truth_values(SageInteger(member in members))
            )
            return self._from_subset(
                subset,
                characteristic_morphism,
                frozenset(members),
            )

        def _element_constructor_(
            self,
            candidate: "Sets.MonoArrowType | Parent | Iterable[Element]",
        ) -> "Sets.MonoArrowType":
            if candidate in SubsetsOfSet(self.base_set()):
                return candidate
            match candidate:
                case Parent() if candidate is self.base_set():
                    characteristic = self.characteristic_hom_category()(
                        lambda member: Sets.Δ[1](1)
                    )
                    return self._from_subset(self.base_set(), characteristic)
                case Parent() if _has_canonical_set_inclusion(candidate, self.base_set()):
                    truth_values = Sets.Δ[1]
                    characteristic_morphism = self.characteristic_hom_category()(
                        lambda member: truth_values(
                            SageInteger(member in candidate)
                        )
                    )
                    return self._from_subset(candidate, characteristic_morphism)
                case Parent() if candidate in Sets().Finite():
                    assert all(member in self.base_set() for member in candidate), (
                        "every member of a subset must lie in its base set"
                    )
                    return self._subset_from_finite_members(candidate)
                case Iterable():
                    members = Set(candidate)
                    assert all(member in self.base_set() for member in members), (
                        "every member of a subset must lie in its base set"
                    )
                    return self._subset_from_finite_members(members)
                case _:
                    assert False, f"{candidate!r} does not present a subset of {self.base_set()}"

        def __contains__(
            self,
            candidate: "Sets.MonoArrowType | Parent | Iterable[Element]",
        ) -> bool:
            if candidate in SubsetsOfSet(self.base_set()):
                return True
            match candidate:
                case Parent() if candidate in Sets().Finite():
                    return all(member in self.base_set() for member in candidate)
                case Parent():
                    return candidate is self.base_set() or _has_canonical_set_inclusion(
                        candidate, self.base_set()
                    )
                case Iterable():
                    return all(member in self.base_set() for member in candidate)
                case _:
                    return False

        def from_predicate(
            self,
            predicate: "Callable[[Element], bool]",
        ) -> "Sets.MonoArrowType":
            r"""Return the subobject defined by ``predicate``."""
            return self._subset_from_predicate(predicate)

        def from_characteristic_morphism(
            self,
            characteristic_morphism: "Sets.ArrowType",
        ) -> "Sets.MonoArrowType":
            r"""Return the subset classified by ``base_set -> Delta[1]``."""
            assert characteristic_morphism in self.characteristic_hom_category(), (
                "a characteristic morphism must lie in Hom(base_set, Delta[1])"
            )
            subset = ConditionSet(
                self.base_set(),
                lambda member: characteristic_morphism(member) == Sets.Δ[1](1),
            )
            return self._from_subset(subset, characteristic_morphism)

        def top(self) -> "Sets.MonoArrowType":
            r"""Return the greatest subset, the base set itself."""
            return self(self.base_set())

        def bottom(self) -> "Sets.MonoArrowType":
            r"""Return the empty subset."""
            return self(())

        def inverse_image_morphism(
            self,
            morphism: "Sets.ArrowType",
        ) -> "Sets.ArrowType":
            r"""Return the inverse-image map ``P(codomain) -> P(domain)``."""
            assert morphism.codomain() is self.base_set(), (
                "inverse image requires the morphism codomain to equal the base set"
            )
            domain_power_set = PowerSet(morphism.domain())
            return Sets().Hom(self, domain_power_set)(
                lambda subset: domain_power_set.from_predicate(
                    lambda member: morphism(member) in subset
                )
            )

        def direct_image_morphism(
            self,
            morphism: "Sets.ArrowType",
        ) -> "Sets.ArrowType":
            r"""Return the direct-image map ``P(domain) -> P(codomain)``."""
            assert morphism.domain() is self.base_set(), (
                "direct image requires the morphism domain to equal the base set"
            )
            codomain_power_set = PowerSet(morphism.codomain())
            return Sets().Hom(self, codomain_power_set)(
                lambda subset: self._finite_direct_image(
                    subset,
                    morphism,
                    codomain_power_set,
                )
            )

        def _finite_direct_image(
            self,
            subset: "Sets.MonoArrowType",
            morphism: "Sets.ArrowType",
            codomain_power_set: Parent,
        ) -> "Sets.MonoArrowType":
            assert subset.underlying_set() in Sets().Finite(), (
                "direct-image membership requires a finite subset or an image decision procedure"
            )
            return codomain_power_set(tuple(morphism(member) for member in subset))

        def __iter__(self) -> "Iterator[Sets.MonoArrowType]":
            assert self.base_set() in Sets().Finite(), (
                "an uncountable power set has no enumeration"
            )
            from sage.combinat.subset import Subsets as SageSubsets

            for members in SageSubsets(self.base_set()):
                yield self(members)

        def cardinality(self) -> Cardinal:
            from dzack_research.preamble.categories.sets.cardinals import cardinal

            return cardinal(2) ** self.base_set().cardinality()

        def cardinality_comparison(self) -> "CardinalityMorphism":
            from dzack_research.preamble.categories.sets.cardinals import (
                Cardinalities,
            )

            cardinals = Cardinalities()
            source = self.cardinality()
            target = cardinals.power(2, self.base_set().cardinality())
            assert source == target
            return cardinals.Hom(source, target).identity()

        def _repr_(self) -> str:
            return f"Power set of {self.base_set()}"


class FixedCardinalitySubsets(_FunctorImageParameters, CategoryWithParameters):
    r"""The subsets of ``S`` with one fixed finite cardinality.

    Direct image preserves this cardinality along injections.  Thus these
    objects form the image of a functor from the wide subcategory of sets and
    injective maps.
    """

    def super_categories(self) -> list[SageCategory]:
        return [ImageOfFunctor(self.functor())]

    def _repr_object_names(self) -> str:
        return "sets of subsets of one fixed cardinality"

    class ParentMethods:
        r"""\([S]^k\): the subsets of ``S`` of cardinality ``k``."""

        def source(self) -> "lexicon.Set":
            return self.preimage()

        @cached_method
        def power_set(self) -> Parent:
            return PowerSet(self.source())

        def cardinality(self) -> Cardinal:
            r"""Return \(\bigl|\{A\subseteq S:|A|=k\}\bigr|\).

            For finite \(S\), this is \(\binom{|S|}{k}\).  For infinite \(S\)
            and positive finite \(k\), this is \(|S|\).  The empty subset is
            the only subset of cardinality zero.
            """
            return self.constructing_functor().image_cardinality(self.source())

        def subset_cardinality(self) -> SageInteger:
            cardinality: SageInteger = (
                self.constructing_functor().subset_cardinality()
            )
            return cardinality

        def _element_constructor_(
            self,
            members: Iterable[Element],
        ) -> "Sets.MonoArrowType":
            subset = self.power_set()(members)
            assert subset.cardinality() == self.subset_cardinality(), (
                f"a member has cardinality {self.subset_cardinality()}"
            )
            return subset

        def __call__(
            self,
            x: ElementConstructorInput = (),
            *arguments: ElementConstructorInput,
            **keywords: ElementConstructorInput,
        ) -> "Sets.MonoArrowType":
            return self._element_constructor_(x)

        def __contains__(self, candidate: ElementConstructorInput) -> bool:
            if candidate not in self.power_set():
                return False
            return (
                self.power_set()(candidate).cardinality()
                == self.subset_cardinality()
            )

        def __iter__(self) -> "Iterator[Sets.MonoArrowType]":
            from sage.combinat.subset import Subsets as SageSubsets

            assert self.source() in Sets().Countable(), (
                "enumeration of fixed-cardinality subsets requires a countable source"
            )
            if self.source() in Sets().Finite():
                for subset in SageSubsets(self.source(), self.subset_cardinality()):
                    yield self(tuple(subset))
                return
            if self.subset_cardinality() == 0:
                yield self(())
                return

            preceding: list[Element] = []
            for maximum in self.source():
                if len(preceding) >= self.subset_cardinality() - 1:
                    for initial in SageSubsets(
                        tuple(preceding),
                        self.subset_cardinality() - 1,
                    ):
                        yield self(tuple(initial) + (maximum,))
                preceding.append(maximum)

        def _repr_(self) -> str:
            return (
                f"Subsets of {self.source()} of cardinality "
                f"{self.subset_cardinality()}"
            )


class FinitePowerSets(_FunctorImageParameters, CategoryWithParameters):
    r"""The set of all finite subsets of a set.

    Countable sources also receive an enumeration.  Finite sources delegate
    that enumeration to Sage's mature ``sage.combinat.subset.Subsets``.

    This is the image of the covariant finite-power-set functor.  Direct image
    transports its elements along every Set arrow.
    """

    def super_categories(self) -> list[SageCategory]:
        return [ImageOfFunctor(self.functor())]

    def _repr_object_names(self) -> str:
        return "sets of finite subsets"

    class ParentMethods:
        r"""\(P_{\mathrm{fin}}(S)\): the finite subsets of ``S``."""

        def source(self) -> "lexicon.Set":
            return self.preimage()

        @cached_method
        def power_set(self) -> Parent:
            return PowerSet(self.source())

        def cardinality(self) -> Cardinal:
            r"""Return \(\bigl|\{A\subseteq S:A\text{ finite}\}\bigr|\).

            For finite \(S\), every subset is finite, so this is \(2^{|S|}\).
            For infinite \(S\), the finite subsets have cardinality \(|S|\).
            """
            return self.constructing_functor().image_cardinality(self.source())

        def _element_constructor_(
            self,
            members: Iterable[Element],
        ) -> "Sets.MonoArrowType":
            return self.power_set()(members)

        def __call__(
            self,
            x: ElementConstructorInput = (),
            *arguments: ElementConstructorInput,
            **keywords: ElementConstructorInput,
        ) -> "Sets.MonoArrowType":
            return self._element_constructor_(x)

        def __contains__(self, candidate: ElementConstructorInput) -> bool:
            return candidate in self.power_set() and self.power_set()(candidate).cardinality().is_finite()

        def index(self, subset: Iterable[Element]) -> int:
            r"""Return the position of ``subset`` in the chosen enumeration."""
            return self.position(self(subset))

        def __iter__(self) -> "Iterator[Sets.MonoArrowType]":
            from sage.combinat.subset import Subsets as SageSubsets

            assert self.source() in Sets().Countable(), (
                "enumeration of finite subsets requires a countable source"
            )
            if self.source() in Sets().Finite():
                for subset in SageSubsets(self.source()):
                    yield self(tuple(subset))
                return

            yield self(())
            preceding: list[Element] = []
            for maximum in self.source():
                for initial in SageSubsets(tuple(preceding)):
                    yield self(tuple(initial) + (maximum,))
                preceding.append(maximum)

        def _repr_(self) -> str:
            return f"Finite subsets of {self.source()}"


def _power_set_of(base_set: "lexicon.Set") -> Parent:
    r"""Apply the contravariant power-set functor to \(X\)."""
    return Sets().InverseImagePowerSetFunctor()(base_set)


@cached_function
def _cached_power_set(base_set: "lexicon.Set") -> Parent:
    return _power_set_of(base_set)


def PowerSet(base_set: "lexicon.Set") -> Parent:
    match base_set:
        case SageImageSet():
            return _power_set_of(base_set)
        case Hashable():
            return _cached_power_set(base_set)
        case _:
            return _power_set_of(base_set)


@cached_function
def SubsetsOfSize(
    source: "lexicon.Set",
    cardinality: "Integer",
) -> Parent:
    r"""Return \([S]^k\), the subsets of ``source`` of the given cardinality."""
    if source not in Sets():
        source = _as_set(source)
    subset_cardinality = SageInteger(cardinality)
    assert subset_cardinality >= 0, "a subset cardinality is nonnegative"
    return Sets().FixedCardinalitySubsetFunctor(subset_cardinality)(source)


@cached_function
def FiniteSubsets(source: "lexicon.Set") -> Parent:
    r"""Return \(P_{\mathrm{fin}}(S)\), the finite subsets of ``source``."""
    assert source in Sets()
    return Sets().FinitePowerSetFunctor()(source)


E = TypeVar("E", bound=Element)


def _as_set(source: lexicon.Set[E] | lexicon.OrderedSet[E]) -> "lexicon.Set[E]":
    return Set(source)


def finite_ordered_set(
    source: lexicon.Set[E] | lexicon.OrderedSet[E] | Sequence[E],
) -> "lexicon.OrderedSet[E]":
    r"""Transport the displayed finite enumeration to a total order.

    The input is a mathematical set: an unordered set of the owned vocabulary
    (a ``Sets()``-member parent or a finite collection) or a set with a
    distinguished linear order -- a generator tuple, in the lexicon's sense.

    Imposing a total order means supplying its data, not asking Sage to sort.
    An ordered enumeration is that data: the enumeration itself is the order,
    and it is handed to ``TotallyOrderedFiniteSet`` untouched -- never
    coerced through ``Set``, which would discard it.  A repeated member is
    one member, so an enumeration keeps each element at its first position:
    \(\{1,2,1\}=\{1,2\}\).  An unordered finite set is given the total order
    of its own iteration.  A totally ordered finite parent is returned
    unchanged.  The result implements the order through Sage's
    ``TotallyOrderedFiniteSet``; category placement is not standing in for
    the relation.
    """
    match source:
        case list() | tuple():
            return _ordered_set_on(tuple(dict.fromkeys(_owned_members(source))))
        case _:
            pass
    source = _as_set(source)
    assert source in Sets().Finite(), f"{source} is not a finite set"
    if source in Sets().TotallyOrdered():
        return source
    return _ordered_set_on(tuple(_owned_members(source)))


def _owned_members(
    members: "Iterable[Element | int]",
) -> tuple[Element, ...]:
    r"""Return the members as this preamble's objects.

    A Python ``int`` and a Sage ``Integer`` print alike, compare equal and
    hash together, so a set built from either answers to the same cache key --
    and the canonical set then holds whichever spelling reached it first.
    That made a set's members depend on construction order, and a morphism out
    of such a set returned a bare ``int`` where an ``Element`` was required.
    The repo bans that fork elsewhere for the same reason; this is where it
    would otherwise enter.
    """
    def owned(member: Element | int) -> Element:
        match member:
            case int():
                return SageZZ(member)
            case _:
                return member

    return tuple(owned(member) for member in members)


def ordered_set_owned_by[E: Element](
    elements: "Iterable[E]",
) -> "lexicon.OrderedSet[E]":
    r"""Return the ordered set on ``elements``, in their given order.

    Not a *fresh* set: ``TotallyOrderedFiniteSet`` is a unique
    representation, so equal members in the same order give one object no
    matter who asks.  This spelling exists because its callers hold elements
    rather than labels and do not want them run through the member
    normalization that ``finite_ordered_set`` applies to raw input.
    """
    return refine(
        TotallyOrderedFiniteSet(tuple(elements)),
        Sets().Finite().TotallyOrdered(),
    )


def _ordered_set_on(elements: tuple) -> "lexicon.OrderedSet":
    r"""Return *the* ordered set on this enumeration.

    One object per enumeration, which is what makes $F_R(S)=F_R(S')$ hold
    when $S=S'$.  The uniqueness is Sage's: ``TotallyOrderedFiniteSet``
    defers to ``FiniteEnumeratedSet``, which is a unique representation, so
    equal members in the same order already give one object.  Caching here
    on top of that bought nothing, and a mutation check said so.
    """
    return refine(
        TotallyOrderedFiniteSet(elements),
        Sets().Finite().TotallyOrdered(),
    )


class _Delta:
    r"""Finite and countable simplex indexing objects \(\Delta[n]\)."""

    def __getitem__(
        self, n: "Integer | int | Cardinal"
    ) -> "lexicon.OrderedSet[Integer]":
        match n:
            case int() | SageInteger():
                assert n >= -1, f"a simplex ordinal has dimension at least -1, got {n}"
                # IntegerRange, not range: the vertices of Δ[n] are the
                # integers 0..n, and Sage's IntegerRange yields Integer.
                # Python's range yields int, a different object that prints
                # the same, and the repo bans that fork.
                # Through the same constructor as every other ordered set:
                # $\Delta[0]$ and the ordered set on $(0)$ are one set, and
                # anything keyed by them -- a free module, above all -- is the
                # same object only when they are.
                return _ordered_set_on(
                    tuple(IntegerRange(SageZZ(n) + SageZZ.one()))
                )
            case _ if n == _ALEPH[0]:
                # The countable simplex is an owned ordered set like every
                # other Delta[n]; handing back a bare Sage NN would leave the
                # one infinite case outside the vocabulary the finite ones use.
                return refine(
                    NN,
                    Sets().Countable().Infinite().TotallyOrdered(),
                )
            case _:
                assert False, f"Δ expects an integer, got {n!r}"

    def __repr__(self) -> str:
        return "Δ"


_DELTA = _Delta()
Sets.Δ = _DELTA


class _Aleph:
    r"""The finite-index aleph cardinals."""

    def __getitem__(self, n: "Integer | int") -> "Cardinal":
        match n:
            case int() | SageInteger():
                from dzack_research.preamble.categories.sets.cardinals import aleph

                return aleph(n)
            case _:
                assert False, f"aleph expects an integer, got {n!r}"

    def __repr__(self) -> str:
        return "ℵ"


_ALEPH = _Aleph()
Sets.ℵ = _ALEPH
Sets.א = _ALEPH
