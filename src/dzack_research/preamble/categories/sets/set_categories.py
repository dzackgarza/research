"""Owned Set categories, canonical index objects, and categorical constructions."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from itertools import count
from typing import Any, Self, SupportsInt, TypeVar

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.combinat.subset import Subsets as SageSubsets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown, UnknownClass
from sage.rings.integer import Integer as SageInteger
from sage.sets.condition_set import ConditionSet as SageConditionSet
from sage.sets.set import Set as SageSet
from sage.structure.element import Element
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoricalIsomorphism,
    EpiCategoryConstruction,
    HomCategoryConstruction,
    MonoCategoryConstruction,
    _category_hom,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
    CardinalityMorphism,
    cardinal,
)
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom

IndexT = TypeVar("IndexT")
SourcePointT = TypeVar("SourcePointT")
TargetPointT = TypeVar("TargetPointT")

for _axiom in ("Countable", "Uncountable"):
    if _axiom not in all_axioms:
        all_axioms.add(_axiom)


class _OwnedImageSet(Parent):
    r"""A represented image retaining its source map and available inverse data."""

    def __init__(
        self,
        source,
        map_,
        *,
        is_injective=False,
        inverse=None,
        category=None,
    ) -> None:
        self._source = source
        self._map = map_
        self._inverse = inverse
        self._is_injective = bool(is_injective)
        categories = [Sets()]
        if source in FiniteSets():
            categories.append(FiniteSets())
        if category is not None:
            categories.append(category)
        Parent.__init__(self, facade=True, category=Category.join(tuple(categories)))

    def source_set(self):
        return self._source

    def image_map(self):
        return self._map

    def inverse_on_image(self):
        assert self._inverse is not None, (
            "inverse_on_image requires a selected inverse for this image construction"
        )
        return self._inverse

    def is_injective_image(self) -> bool:
        return self._is_injective

    def cardinality(self):
        if self.is_injective_image():
            return cardinal(self.source_set().cardinality())
        assert self.source_set() in FiniteSets(), (
            "cardinality of a noninjective image requires a finite source or additional represented image data"
        )
        return cardinal(len(tuple(self)))

    def _finite_values(self):
        values = []
        for source in self.source_set():
            value = self.image_map()(source)
            if not any(value == known for known in values):
                values.append(value)
        return tuple(values)

    def __iter__(self):
        if self.source_set() in FiniteSets():
            return iter(self._finite_values())
        assert self.is_injective_image() and self.source_set() in EnumeratedSets(), (
            "enumerating an infinite image requires an injective represented map from an enumerated source"
        )
        return (self.image_map()(source) for source in self.source_set())

    def __contains__(self, element) -> bool:
        if self._inverse is not None:
            try:
                source = self._inverse(element)
                source = self.source_set()(source)
            except (TypeError, ValueError):
                return False
            return self.image_map()(source) == element
        assert self.source_set() in FiniteSets(), (
            "membership in an infinite image requires a selected inverse-on-image decision procedure"
        )
        return any(element == value for value in self._finite_values())

    def _element_constructor_(self, element):
        if element not in self:
            raise ValueError(f"{element!r} is not in {self}")
        return element

    def _repr_(self) -> str:
        if self.source_set() in FiniteSets():
            return "{" + ", ".join(repr(value) for value in self._finite_values()) + "}"
        return f"Image of {self.source_set()} under {self.image_map()}"


class EnumeratedSets(OwnedCategory):
    r"""Sets equipped with a represented ranking/enumeration."""

    def an_object(self) -> Parent:
        r"""The ordinal 2, ranked by its own order."""
        return finite_ordinal_set(2)

    def super_categories(self):
        return [Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""Return the isomorphism onto the ordinal counting this set.

            An enumeration is a bijection $X \xrightarrow{\ \sim\ }
            \operatorname{Ord}(|X|)$, so both directions a caller wants are
            this one arrow: it takes a point to its position, and its
            :meth:`inverse` takes a position back to the point there.
            """

        def __getitem__(self, position):
            r"""Return the point at ``position``, the ranking map run backwards."""
            return self.ranking_map().inverse()(position)

        def _ranking_isomorphism(self, position_of, point_at):
            r"""Build the represented enumeration from its mutually inverse directions."""
            ordinal = self.counting_ordinal()
            forward = Sets().Mor(self, ordinal)(
                lambda element: NN(position_of(element))
            )
            backward = Sets().Mor(ordinal, self)(
                lambda position: point_at(int(position))
            )
            return CategoricalIsomorphism(
                _set_core().Mor(self, ordinal),
                forward,
                backward,
                verify=False,
            )

        def fixed_size_selections(self, selection_size, *, repetition):
            r"""Return the ordered selections of the stated size from this ranked set."""
            from dzack_research.preamble.categories.sets.fixed_size_selections import (
                _fixed_size_selections,
            )

            return _fixed_size_selections(
                self,
                selection_size,
                repetition=repetition,
            )

        def ordered_subsets_of_size(self, size):
            r"""Return increasing ``size``-element selections without repetition."""
            return self.fixed_size_selections(size, repetition=False)

        def multisets_of_size(self, size):
            r"""Return increasing ``size``-element selections with repetition."""
            return self.fixed_size_selections(size, repetition=True)


class FiniteOrdinalSets(OwnedCategory):
    r"""The canonical finite ordinals \(\{0,\dots,n-1\}\), lazily."""

    def an_object(self) -> Parent:
        r"""\(\{0,1,2\}\)."""
        return finite_ordinal_set(3)

    def super_categories(self):
        # The join every finite ordinal was built in, declared once
        # by the category rather than computed for each object.
        return [EnumeratedSets(), TotallyOrderedSets(), FiniteSets()]

    def _call_(self, size):
        r"""Construct the canonical finite ordinal of cardinality ``size``."""
        return _object_of(self, size=size)

    class ParentMethods:
        def __init__(self, size: int, **rest) -> None:
            self._size = int(size)
            assert self._size >= 0 and size == self._size, "a finite ordinal cardinality is a nonnegative integer"
            super().__init__(facade=True, **rest)

        def cardinality(self) -> Parent:
            return cardinal(self._size)

        def __iter__(self):
            return (NN(index) for index in range(self._size))

        def __getitem__(self, position):
            r"""Return the point at ``position`` without enumerating preceding points."""
            position = int(position)
            if position < 0 or position >= self._size:
                raise IndexError(position)
            return NN(position)

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""The identity: an ordinal already *is* the ordinal counting it."""

            def point_at(position):
                position = int(position)
                if position < 0 or position >= self._size:
                    raise IndexError(position)
                return NN(position)

            def position_of(element):
                try:
                    position = int(element)
                except (TypeError, ValueError) as error:
                    raise ValueError(element) from error
                if position < 0 or position >= self._size:
                    raise ValueError(element)
                return position

            return self._ranking_isomorphism(position_of, point_at)

        def __contains__(self, element) -> bool:
            try:
                position = int(element)
            except (TypeError, ValueError):
                return False
            return element == position and 0 <= position < self._size

        is_parent_of = __contains__

        def __call__(self, element):
            r"""Normalize a natural number to the point of this ordinal it names.

            This is the element constructor, the one boundary that admits
            foreign data, so it reads the position directly.  It cannot ask
            the ranking map: applying an arrow coerces its argument into the
            domain, and the domain is this parent.
            """
            try:
                position = int(element)
            except (TypeError, ValueError) as error:
                raise ValueError(element) from error
            if element != position or position < 0 or position >= self._size:
                raise ValueError(element)
            return NN(position)

        def le(self, left: SupportsInt, right: SupportsInt) -> bool:
            ranking = self.ranking_map()
            return ranking(left) <= ranking(right)

        def __len__(self):
            return self._size

        def _repr_(self):
            if not self._size:
                return "{}"
            return f"{{0,...,{self._size - 1}}}"


@cached_function
def finite_ordinal_set(size: int) -> Parent:
    r"""The ordinal $\{0,\dots,n-1\}$.

    Interned by its size, because an ordinal is determined by how much it
    counts: two sets of the same cardinality must reach the *same* codomain
    or their enumerations do not compose.
    """
    return FiniteOrdinalSets()(size)


@cached_function
def _set_core():
    r"""The core of $\mathbf{Set}$, interned so every enumeration shares one home."""
    return Sets().Core()


class _Delta:
    r"""The standard finite ordinals \(\Delta[n]=\{0,\ldots,n\}\), and \(\Delta[\aleph_0]=\mathbb N\)."""

    def __getitem__(self, dimension):
        if isinstance(dimension, (int, SageInteger)):
            return finite_ordinal_set(int(dimension) + 1)
        from dzack_research.preamble.categories.sets.cardinals import aleph0

        size = cardinal(dimension)
        if size == aleph0:
            return NN
        if not size.is_finite():
            raise ValueError("the represented simplex index is finite or countably infinite")
        return finite_ordinal_set(int(size.finite_value()) + 1)

    def __repr__(self) -> str:
        return "Δ"


class _Aleph:
    def __getitem__(self, index):
        from dzack_research.preamble.categories.sets.cardinals import aleph

        return aleph(index)

    def __repr__(self) -> str:
        return "ℵ"


class OwnedSetMorphism(SetMorphism):
    r"""A set map whose composition remains in the canonical owned Set Hom.

    Unverified construction specimens, including a subset inclusion and maps
    of Python labels rather than Sage elements::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: labels = finite_ordered_set(("a", "b"))
        sage: swap = Sets().Mor(labels, labels)(lambda x: {"a": "b", "b": "a"}[x])
        sage: inclusion = labels.power_set()(("a",))
        sage: inclusion("a"), (swap * inclusion)("a")
        ('a', 'b')
        sage: (swap * swap).is_identity()
        True
        sage: hash(swap * swap) == hash(Sets().Mor(labels, labels).identity())
        True
    """

    def __init__(
        self,
        parent: SetMorCategory,
        function: Callable[[SourcePointT], TargetPointT],
    ) -> None:
        SetMorphism.__init__(self, parent, function)
        self._owned_function = function
        self._preamble_is_identity = False

    def __call__(self, element: SourcePointT, *args, **kwargs) -> TargetPointT:
        r"""Send a point of the source to its point of the target.

        Sage's ``SetMorphism`` is typed to return an ``Element``, so a map
        whose target has points that are not Sage elements -- a set of
        labels, an index set of generator names -- cannot be applied at all
        through it.  A map of sets carries no such restriction: it takes a
        point of the source to a point of the target, whatever those are.
        The function is kept here so applying the map never crosses that
        typing, and foreign data is read where every owned set reads it, by
        the source's own ingress.
        """
        point = self.domain()(element)
        return self.codomain()(self._owned_function(point, *args, **kwargs))

    def __eq__(self, other: Any) -> bool | UnknownClass:
        r"""Two set maps agree when they agree at every point.

        That is decidable when the source is a finite enumerated set, and not
        otherwise.
        """
        if not isinstance(other, SetMorphism):
            return False
        if self is other:
            return True
        if self.parent() is not other.parent():
            return False
        domain = self.domain()
        if domain not in FiniteSets() or domain not in EnumeratedSets():
            return Unknown
        answer = True
        for element in domain:
            equal = self(element) == other(element)
            if equal is False:
                return False
            if equal is not True:
                answer = Unknown
        return answer

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        # Equality is extensional within one Hom.  An identity-based hash of
        # the function would give equal maps different hashes; hashing only
        # the parent also works when points of either endpoint are unhashable.
        return hash(id(self.parent()))

    def is_identity(self) -> bool | UnknownClass:
        r"""Decide identity on a finite enumeration; retain unknown otherwise."""
        if self.domain() is not self.codomain():
            return False
        if self._preamble_is_identity:
            return True
        return self == self.parent().identity()

    def _image_points(self) -> Parent:
        r"""The image, enumerated: decidable for a finite enumerated domain."""
        from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

        domain = self.domain()
        assert domain in FiniteSets() and domain in EnumeratedSets(), "injectivity and surjectivity are decided here on a finite enumerated domain"
        return finite_ordered_set(tuple(self(element) for element in domain))

    def is_injective(self) -> bool:
        r"""Decide ``f(x) = f(y) => x = y`` by counting the image."""
        return len(self._image_points()) == int(self.domain().cardinality())

    def is_surjective(self) -> bool:
        r"""Decide that every point of the codomain is a value."""
        codomain = self.codomain()
        assert codomain in FiniteSets() and codomain in EnumeratedSets(), "surjectivity is decided here on a finite enumerated codomain"
        image = self._image_points()
        return all(point in image for point in codomain)

    def inverse(self):
        r"""Return the inverse of a bijection between finite enumerated sets."""
        domain = self.domain()
        codomain = self.codomain()
        match (
            domain in FiniteSets() and domain in EnumeratedSets(),
            codomain in FiniteSets() and codomain in EnumeratedSets(),
        ):
            case (True, True):
                pass
            case _:
                assert (
                    domain in FiniteSets()
                    and domain in EnumeratedSets()
                    and codomain in FiniteSets()
                    and codomain in EnumeratedSets()
                ), "the represented inverse search requires finite enumerated endpoints"
        match (self.is_injective(), self.is_surjective()):
            case (True, True):
                pass
            case _:
                raise ValueError("only a bijective set morphism has an inverse")

        def preimage(target):
            try:
                return next(source for source in domain if self(source) == target)
            except StopIteration as error:
                raise ArithmeticError("a declared bijection omitted a codomain point") from error

        return Sets().Mor(codomain, domain)(preimage)

    def as_isomorphism(self):
        r"""Return this finite bijection as the corresponding arrow of ``core(Set)``."""
        return Sets().Core().Mor(self.domain(), self.codomain())(self, self.inverse())

    def __mul__(self, other):
        if not isinstance(other, Morphism) or other.codomain() is not self.domain():
            return NotImplemented
        homset = Sets().Mor(other.domain(), self.codomain())
        if self.is_identity() is True and other.parent() is homset:
            return other
        if isinstance(other, OwnedSetMorphism) and other.is_identity() is True:
            return self
        return homset(lambda element: self(other(element)))


class SetMorCategory(CategoricalHomset):
    r"""The owned category $\mathrm{Mor}_{\mathbf{Set}}(X, Y)$.

    Its objects are the functions $X \to Y$.  A set is a category -- the
    discrete one -- so this is a category like every other `Mor`, and not a
    special set-valued case: `ARC-07` has `Mor` return a category at every
    level.  Sage's ``Homset``, reached through ``CategoricalHomset``, remains
    the runtime parent its ``SetMorphism`` elements require.
    """

    def __init__(
        self,
        mor_family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(self, mor_family, domain, codomain)

    def __call__(self, datum):
        if isinstance(datum, Morphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the set morphism has the wrong source or target")
            if datum.parent() is self:
                return datum
        if not callable(datum):
            raise TypeError("a set morphism is supplied by a callable")
        morphism = OwnedSetMorphism(self, datum)
        return morphism

    @cached_method
    def identity(self) -> OwnedSetMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only for equal set endpoints")
        identity = OwnedSetMorphism(self, lambda element: element)
        identity._preamble_is_identity = True
        return identity

    def identity_at(self, obj: Parent) -> OwnedSetMorphism:
        return Sets().Mor(obj, obj).identity()

    def _repr_(self):
        return f"Mor_Set({self.domain()}, {self.codomain()})"


class SetMorCategoryConstruction(HomCategoryConstruction):
    r"""The owned family $(X, Y) \mapsto \mathrm{Mor}_{\mathbf{Set}}(X, Y)$."""

    def fixed_category_class(self) -> type[SetMorCategory]:
        return SetMorCategory


def _set_mor_category(domain, codomain):
    r"""Return the canonical $\mathrm{Mor}_{\mathbf{Set}}(X, Y)$.

    The family interns by endpoint identity, so this replaces the local cache
    the set level kept while it was the one category building its Mor object
    by hand.
    """
    return SetMorCategoryConstruction(Sets()).Of(domain, codomain)


class Sets(OwnedCategory):
    r"""The owned category of sets.

    All Sage set objects are admitted.  The category owns the mathematical
    constructions the preamble adds; Sage remains the implementation of
    ordinary set maps.

    Sage remains an implementation substrate for concrete parent and coercion
    behavior, but the mathematical supercategory edge is entirely owned.
    """

    _HomCategory = SetMorCategoryConstruction

    Δ = _Delta()
    ℵ = _Aleph()
    א = ℵ

    def an_object(self) -> Parent:
        r"""The ordinal 2: two distinct elements, so a map out of it is not forced."""
        return finite_ordinal_set(2)

    def super_categories(self):
        return [Objects()]

    def _call_(self, source):
        r"""Construct ``source`` as a represented set when syntactic ingress is needed."""
        if source in self or source in SageSets():
            return source
        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            finite_ordered_set,
        )

        return finite_ordered_set(tuple(SageSet(source)))

    def condition_set(self, universe, predicate):
        r"""Return the represented subset of ``universe`` cut out by ``predicate``."""
        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            finite_ordered_set,
        )

        if universe in FiniteSets():
            elements = getattr(universe, "elements", None)
            if callable(elements):
                return finite_ordered_set(
                    tuple(element for element in elements() if predicate(element))
                )
            if universe in EnumeratedSets():
                return finite_ordered_set(
                    tuple(element for element in universe if predicate(element))
                )
        return SageConditionSet(universe, predicate)

    def image_set(
        self,
        map_,
        domain_subset,
        *,
        category=None,
        is_injective=None,
        inverse=None,
    ):
        r"""Return the owned image construction of ``domain_subset`` under ``map_``."""
        if is_injective is True and inverse is not None and domain_subset in EnumeratedSets():
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                OrderedEnumeratedSets,
                FiniteOrderedSets,
            )

            def contains(element):
                try:
                    source = inverse(element)
                    source = domain_subset(source)
                except (TypeError, ValueError):
                    return False
                return map_(source) == element

            match domain_subset in FiniteSets():
                case True:
                    return FiniteOrderedSets().from_indexed(
                        domain_subset,
                        map_,
                        index_of=inverse,
                        contains=contains,
                        image_source=domain_subset,
                        image_map=map_,
                        image_inverse=inverse,
                    )
                case False:
                    return OrderedEnumeratedSets()(
                        domain_subset,
                        map_,
                        index_of=inverse,
                        contains=contains,
                        image_source=domain_subset,
                        image_map=map_,
                        image_inverse=inverse,
                    )

        return _OwnedImageSet(
            domain_subset,
            map_,
            is_injective=is_injective is True,
            inverse=inverse,
            category=category,
        )

    def __contains__(self, candidate) -> bool:
        try:
            if candidate.category().is_subcategory(self):
                return True
        except AttributeError:
            pass
        try:
            return candidate in SageSets()
        except (TypeError, ValueError):
            return False

    def Mor(self, domain: Parent, codomain: Parent) -> SetMorCategory:
        if domain not in self or codomain not in self:
            raise TypeError("a set morphism requires two set objects")
        return _set_mor_category(domain, codomain)

    class SubcategoryMethods:
        def Finite(self) -> Category:
            r"""Return this category with the axiom that its objects are finite."""
            return self._with_axiom("Finite")

        def Infinite(self) -> Category:
            r"""Return this category with the axiom that its objects are infinite."""
            return self._with_axiom("Infinite")

        def Countable(self) -> Category:
            r"""Return this category with the axiom that its objects are countable."""
            return self._with_axiom("Countable")

        def Uncountable(self) -> Category:
            r"""Return this category with the axiom that its objects are uncountable."""
            return self._with_axiom("Uncountable")

        def product(
            self,
            family: IndexedFamily | Iterable[Parent],
        ) -> Parent:
            r"""Return $\prod_{i \in I} X_i$ for an indexed family of objects.

            A product is taken over an index set, so the family carries both the
            index set and the factor at each index.  Asking the category is the
            public route (`STY-02`), and naming the index set rather than an arity
            is what `CON-14` requires. A two-factor call may pass a two-element
            family, whose canonical labels are then `Sets.Δ[1]`.

            Two constructions of the same product are the same object.  Without
            that, an element of one never equals an element of the other and the
            product is unusable as a codomain -- a caller could not compare what an
            operation returned against a value it built.  A family's value map is a
            callable and cannot key a cache, so a finite index set is resolved to
            its factors, which can.

            A bare sequence of factors is the family on the canonical labels, so
            the caller may hand over either.
            """
            from dzack_research.preamble.categories.abstract_categories.products import (
                _factor_family,
            )

            family = _factor_family(family, name="Product factors")
            index_set = family.index_set()
            if index_set in FiniteSets() and index_set in EnumeratedSets():
                return self._categorical_product_construction(family).object()
            return _cartesian_product_of_family(index_set, family)

        def _categorical_product(self, left, right):
            return self._categorical_product_construction((left, right)).object()

        def _categorical_product_construction(self, factors):
            from dzack_research.preamble.categories.abstract_categories.products import (
                SelectedLimitConstruction,
                _discrete_diagram,
                _finite_factor_family,
            )

            family = _finite_factor_family(factors, name="Product factors")
            if any(factor not in self for factor in family):
                raise TypeError("a set product requires set-valued factors")
            product = _cartesian_product_of_finite_family(family)
            diagram = _discrete_diagram(family, self)
            universal_cone = (diagram).ProductCones().cone(
                product,
                lambda index: product.projection(index.value()),
            )

            def factorizer(cone):
                return product.from_maps(
                    cone.apex(),
                    lambda label: cone.structure_morphism(diagram.domain()(label)),
                )

            return SelectedLimitConstruction(diagram, universal_cone, factorizer)

        def _categorical_equalizer(self, left_morphism, right_morphism):
            r"""Return the represented subset on which two set maps agree."""
            return self._categorical_equalizer_construction(
                left_morphism, right_morphism
            ).object()

        def _categorical_equalizer_construction(
            self, left_morphism, right_morphism
        ):
            r"""Return the selected equalizer cone for two parallel set maps."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                SelectedLimitConstruction,
                _parallel_pair_diagram,
            )

            if (
                left_morphism.domain() is not right_morphism.domain()
                or left_morphism.codomain() is not right_morphism.codomain()
            ):
                raise ValueError("a set equalizer requires parallel maps")
            source = left_morphism.domain()
            target = left_morphism.codomain()
            if source not in self or target not in self:
                raise TypeError("a set equalizer requires set-valued endpoints")

            equalizer = self.condition_set(
                source,
                lambda element: left_morphism(element) == right_morphism(element),
            )
            inclusion = self.Mor(equalizer, source)(lambda element: source(element))
            diagram = _parallel_pair_diagram(left_morphism, right_morphism, self)
            shape = diagram.domain()
            universal_cone = diagram.Cones().cone(
                equalizer,
                lambda index: (
                    inclusion
                    if index is shape.source()
                    else left_morphism * inclusion
                ),
            )

            def factorizer(cone):
                source_leg = cone.structure_morphism(shape.source())
                return self.Mor(cone.apex(), equalizer)(
                    lambda element: equalizer(source_leg(element))
                )

            return SelectedLimitConstruction(diagram, universal_cone, factorizer)

        def coproduct(
            self,
            family: IndexedFamily | Iterable[Parent],
        ) -> Parent:
            r"""Return $\coprod_{i \in I} X_i$ for an indexed family of objects.

            The dual of :meth:`product`, and built the same way.  Folding the
            binary coproduct over three sets gives $(X_0\sqcup X_1)\sqcup
            X_2$, which satisfies the same universal property but is a
            different object: its index set has two elements, one of which is
            itself a coproduct, so an injection is named by a path rather than
            by an index.  Both are coproducts and only one is the coproduct
            over $I$ (`CON-14`).

            Two constructions of the same coproduct are the same object, for
            the reason :meth:`product` gives -- an element of one would
            otherwise never equal an element of the other.

            A bare sequence of factors is the family on the canonical labels,
            so the caller may hand over either.
            """
            from dzack_research.preamble.categories.abstract_categories.products import (
                _factor_family,
            )

            family = _factor_family(family, name="Coproduct factors")
            index_set = family.index_set()
            if index_set in FiniteSets() and index_set in EnumeratedSets():
                return self._categorical_coproduct_construction(family).object()
            return _coproduct_of_family(index_set, family)

        def _categorical_coproduct(self, left, right):
            return self._categorical_coproduct_construction((left, right)).object()

        def _categorical_coproduct_construction(self, factors):
            from dzack_research.preamble.categories.abstract_categories.products import (
                SelectedColimitConstruction,
                _discrete_diagram,
                _finite_factor_family,
            )

            family = _finite_factor_family(factors, name="Coproduct factors")
            if any(factor not in self for factor in family):
                raise TypeError("a set coproduct requires set-valued factors")
            coproduct = _coproduct_of_finite_family(family)
            diagram = _discrete_diagram(family, self)
            universal_cocone = (diagram).CoproductCocones().cocone(
                coproduct,
                lambda index: coproduct.injection(index.value()),
            )

            def factorizer(cocone):
                return coproduct.from_maps(
                    cocone.apex(),
                    lambda label: cocone.costructure_morphism(diagram.domain()(label)),
                )

            return SelectedColimitConstruction(diagram, universal_cocone, factorizer)

        def _categorical_coequalizer(self, left_morphism, right_morphism):
            return self._categorical_coequalizer_construction(
                left_morphism, right_morphism
            ).object()

        def _categorical_coequalizer_construction(
            self, left_morphism, right_morphism
        ):
            from dzack_research.preamble.categories.abstract_categories.products import (
                SelectedColimitConstruction,
                _parallel_pair_diagram,
            )

            if (
                left_morphism.domain() is not right_morphism.domain()
                or left_morphism.codomain() is not right_morphism.codomain()
            ):
                raise ValueError("a coequalizer requires parallel set maps")
            source = left_morphism.domain()
            target = left_morphism.codomain()
            if source not in self or target not in self:
                raise TypeError("a set coequalizer requires set-valued endpoints")
            assert (
                cardinal(source.cardinality()).is_finite()
                and cardinal(target.cardinality()).is_finite()
            ), "the represented set coequalizer requires finite sets"

            source_points = tuple(source)
            target_points = tuple(target)
            parents = list(range(len(target_points)))

            def position(value):
                for index, point in enumerate(target_points):
                    if point == value:
                        return index
                raise ValueError("a parallel map left the represented target set")

            def root(index):
                while parents[index] != index:
                    parents[index] = parents[parents[index]]
                    index = parents[index]
                return index

            def union(left_index, right_index):
                left_root = root(left_index)
                right_root = root(right_index)
                if left_root != right_root:
                    parents[right_root] = left_root

            for point in source_points:
                union(
                    position(left_morphism(point)),
                    position(right_morphism(point)),
                )

            representatives = []
            class_position = {}
            for target_index in range(len(target_points)):
                representative = root(target_index)
                if representative not in class_position:
                    class_position[representative] = len(representatives)
                    representatives.append(target_index)

            quotient = Sets.Δ[len(representatives) - 1]
            projection = Sets().Mor(target, quotient)(
                lambda point: quotient(class_position[root(position(point))])
            )
            diagram = _parallel_pair_diagram(
                left_morphism, right_morphism, self
            )
            shape = diagram.domain()
            universal_cocone = (diagram).Cocones().cocone(
                quotient,
                lambda index: (
                    projection * left_morphism
                    if index is shape.source()
                    else projection
                ),
            )

            def factorizer(cocone):
                target_map = cocone.costructure_morphism(shape.target())
                return Sets().Mor(quotient, cocone.apex())(
                    lambda label: target_map(
                        target_points[representatives[int(label)]]
                    )
                )

            return SelectedColimitConstruction(
                diagram, universal_cocone, factorizer
            )

        def _categorical_product_morphism(self, left_morphism, right_morphism, source, target):
            return _cartesian_product_morphism(
                source,
                target,
                lambda index: left_morphism if int(index) == 0 else right_morphism,
            )

        def _categorical_coproduct_morphism(self, left_morphism, right_morphism, source, target):
            return _coproduct_morphism(
                source,
                target,
                lambda index: left_morphism if int(index) == 0 else right_morphism,
            )

        def Homsets(self) -> Category:
            r"""A Hom object of any owned category is a set."""
            return Homsets()

        # Functors out of ``Set``, each spelled as a method of this, their
        # domain category, and named by the construction it performs.

        def free_module(self, base_ring: Parent) -> Functor:
            r"""``F_R : Set -> Mod_R``, the free ``R``-module functor.

            The free module on a set has that set for its module generating
            set, so a set map is carried to the linear map sending generator
            to generator.  Left adjoint of the underlying-set functor on
            ``R``-modules; the adjunction is ``free_module_adjunction``.
            """
            from dzack_research.preamble.categories.functors.free_forgetful import (
                _free_module_functor,
            )

            return _free_module_functor(base_ring)

        def free_module_adjunction(self, base_ring: Parent) -> Adjunction:
            r"""``F_R -| U`` between ``Set`` and ``Mod_R``.

            An adjunction is a method of its left adjoint's domain category,
            and ``F_R`` is the left adjoint.  Its unit at ``S`` sends a label
            to the module generator on that label, and its counit at ``M``
            evaluates a formal ``R``-combination of elements of ``M``.
            """
            from dzack_research.preamble.categories.functors.free_forgetful import (
                _free_forgetful_adjunction,
            )

            return _free_forgetful_adjunction(base_ring)

        def free_group(self) -> Functor:
            r"""``F : Set -> Grp``, the free-group functor.

            The free group on a set carries that set as its chosen free basis,
            so a set map is carried to the group morphism it determines on the
            free generators.  Left adjoint of the underlying-set functor on
            groups; the adjunction is ``free_group_adjunction``.
            """
            from dzack_research.preamble.categories.functors.free_groups import (
                _free_group_functor,
            )

            return _free_group_functor()

        def free_group_adjunction(self) -> Adjunction:
            r"""``F -| U`` between ``Set`` and ``Grp``.

            An adjunction is a method of its left adjoint's domain category,
            and ``F`` is the left adjoint.  Its unit at ``S`` sends a letter to
            the free generator on it, and its counit at ``G`` multiplies out a
            word in the elements of ``G``.
            """
            from dzack_research.preamble.categories.functors.free_groups import (
                _free_group_underlying_set_adjunction,
            )

            return _free_group_underlying_set_adjunction()

        def cardinality_functor(self) -> Functor:
            r"""``# : core(Set) -> Card``, the cardinality functor.

            Cardinality is an isomorphism invariant: a bijection of sets fixes
            it, and an arbitrary set map does not respect it at all, so this
            functor is defined on the core groupoid of ``Set`` and not on
            ``Set``.  The method is sited here because ``Set`` is the category
            whose core that is, and ``domain()`` reports ``core(Set)``.
            """
            from dzack_research.preamble.categories.functors.cardinality import (
                _cardinality_functor,
            )

            return _cardinality_functor()

        def power_set_functor(self) -> Functor:
            r"""``P_fin : Set -> Set``, the finite subsets under direct image.

            Defined on every set and not only the finite ones: the finite
            subsets of an infinite set are again a set, and a set map carries
            a finite subset to its direct image, which is finite.  Every
            subset of a finite set is finite, so reached from ``FiniteSets()``
            this is the full power set.  Inverse image does not preserve
            finiteness, so the contravariant power set is a separate functor
            on the opposite category.
            """
            from dzack_research.preamble.categories.functors.set_constructions import (
                _finite_power_set_functor,
            )

            return _finite_power_set_functor()

        def inverse_image_power_set_functor(self) -> Functor:
            r"""Return the contravariant power-set functor under inverse image."""
            from dzack_research.preamble.categories.functors.set_constructions import (
                _inverse_image_power_set_functor,
            )

            return _inverse_image_power_set_functor()

        def exponential_functor(self) -> Functor:
            r"""Return the Set exponential bifunctor ``(X,Y) |-> Y^X``."""
            from dzack_research.preamble.categories.functors.set_constructions import (
                _exponential_functor,
            )

            return _exponential_functor()

        def fixed_cardinality_subset_functor(self, subset_cardinality) -> Functor:
            r"""Return the functor of subsets of cardinality ``subset_cardinality``."""
            from dzack_research.preamble.categories.functors.set_constructions import (
                _fixed_cardinality_subset_functor,
            )

            return _fixed_cardinality_subset_functor(subset_cardinality)

    def identity(self, set_object: Parent) -> OwnedSetMorphism:
        return self.Mor(set_object, set_object).identity()

    def PartiallyOrdered(self) -> Category:
        return PartiallyOrderedSets()

    def TotallyOrdered(self) -> Category:
        return TotallyOrderedSets()

    class ParentMethods:
        def counting_ordinal(self):
            r"""Return the represented ordinal that counts this set when it is countable."""
            size = cardinal(self.cardinality())
            if size.is_finite():
                return finite_ordinal_set(size.finite_value())
            assert size.is_countably_infinite(), (
                f"{self} is not countable, so no ordinal represented here counts it"
            )
            return NN

        def Mor(
            self,
            codomain: Parent,
            category: Category | None = None,
        ) -> Category:
            if category is None:
                return Sets().Mor(self, codomain)
            return _category_hom(category, self, codomain)

        def condition_set(self, predicate) -> Parent:
            r"""Return the represented subset of ``self`` cut out by ``predicate``."""
            return Sets().condition_set(self, predicate)

        def image_set(
            self,
            map_,
            *,
            category=None,
            is_injective=None,
            inverse=None,
        ) -> Parent:
            r"""Return the represented image of ``self`` under ``map_``."""
            return Sets().image_set(
                map_,
                self,
                category=category,
                is_injective=is_injective,
                inverse=inverse,
            )

        def power_set(self) -> Parent:
            return _power_set(self)

        def exponential(self, exponent: Parent) -> Parent:
            return _exponential_of_sets(self, exponent)

        def __mul__(self, other):
            r"""Return $X \times Y$.  A product of sets is a set."""
            return self.product_with(other)

        def product_with(self, other: Parent) -> Parent:
            r"""Return $X \times Y$, the product asked of the objects.

            `STY-02`: the construction is asked of the objects rather than of a
            global constructor.  The index set chosen here is `Sets.Δ[1]`; when
            the index set is part of the mathematics, name it and use
            `Sets().product(family)` (`CON-14`).
            """
            assert other in Sets(), "a product is taken between two owned sets"
            factors = (self, other)
            return Sets().product(indexed_family(Sets.Δ[1], lambda index: factors[int(index)]))

        def coproduct_with(self, other: Parent) -> Parent:
            r"""Return $X \sqcup Y$, the coproduct asked of the objects."""
            assert other in Sets(), "a coproduct is taken between two owned sets"
            cofactors = (self, other)
            return Sets().coproduct(
                indexed_family(
                    Sets.Δ[1],
                    lambda index: cofactors[int(index)],
                )
            )

        def __pow__(self, exponent):
            r"""Return $X^n$, the product of the constant family over `Sets.Δ[n-1]`."""
            count = int(exponent)
            if count < 0 or exponent != count:
                raise ValueError("a finite set power requires a nonnegative exponent")
            return Sets().product(indexed_family(Sets.Δ[count - 1], lambda index: self))

        def subsets_of_size(self, size: int) -> Parent:
            return _subsets_of_size(self, size)

        def finite_subsets(self) -> Parent:
            return _finite_subsets(self)

    class Finite(CategoryWithAxiom):
        r"""Sets whose cardinality is finite."""

        def an_object(self) -> Parent:
            r"""The ordinal 2."""
            return finite_ordinal_set(2)

        def extra_super_categories(self) -> list[Category]:
            r"""A finite set is countable."""
            return [Sets().Countable()]

        # Functors into finite G-sets, sited on their domain.

        def trivial_action(self, group: Parent) -> Functor:
            r"""``Triv_G : FinSet -> FinGSet_G``, every point fixed."""
            from dzack_research.preamble.categories.functors.g_sets import TrivialGSetFunctor

            return TrivialGSetFunctor(group)

        def free_action(self, group: Parent) -> Functor:
            r"""``G x - : FinSet -> FinGSet_G``, the free ``G``-set on a set."""
            from dzack_research.preamble.categories.functors.g_sets import FreeGSetFunctor

            return FreeGSetFunctor(group)

        def free_underlying_adjunction(self, group: Parent) -> Adjunction:
            r"""``G x - -| U``."""
            from dzack_research.preamble.categories.functors.g_sets import (
                _free_g_set_underlying_adjunction,
            )

            return _free_g_set_underlying_adjunction(group)

        def trivial_fixed_adjunction(self, group: Parent) -> Adjunction:
            r"""``Triv_G -| (-)^G``."""
            from dzack_research.preamble.categories.functors.g_sets import (
                _g_set_trivial_fixed_adjunction,
            )

            return _g_set_trivial_fixed_adjunction(group)

    class Infinite(CategoryWithAxiom):
        r"""Sets whose cardinality is infinite."""

        def an_object(self) -> Parent:
            r"""The natural numbers."""
            return NN

    class Countable(CategoryWithAxiom):
        r"""Sets whose cardinality is at most \(\aleph_0\)."""

        def an_object(self) -> Parent:
            r"""The natural numbers."""
            return NN

        class Infinite(CategoryWithAxiom):
            r"""Sets whose cardinality is \(\aleph_0\)."""

            def an_object(self) -> Parent:
                r"""The natural numbers."""
                return NN

    class Uncountable(CategoryWithAxiom):
        r"""Sets whose cardinality exceeds \(\aleph_0\)."""

        def an_object(self) -> Parent:
            r"""The power set of the natural numbers."""
            return NN.power_set()

        def extra_super_categories(self) -> list[Category]:
            r"""An uncountable set is infinite."""
            return [Sets().Infinite()]


def FiniteSets() -> Category:
    r"""The category of finite sets."""
    return Sets().Finite()


def InfiniteSets() -> Category:
    r"""The category of infinite sets."""
    return Sets().Infinite()


def CountableSets() -> Category:
    r"""The category of countable sets."""
    return Sets().Countable()


def CountablyInfiniteSets() -> Category:
    r"""The category of countably infinite sets."""
    return Sets().Countable().Infinite()


def UncountableSets() -> Category:
    r"""The category of uncountable sets."""
    return Sets().Uncountable()


def Set[SourcePointT](source: Parent | Iterable[SourcePointT]) -> Parent:
    r"""Notebook notation for construction through :class:`Sets`."""
    return Sets()(source)



class SetInjection(OwnedSetMorphism):
    r"""A set morphism supplied with the assertion that it is injective."""

    def is_injective(self) -> bool:
        return True

    def __mul__(self, other):
        if isinstance(other, SetInjection) and other.codomain() is self.domain():
            return Sets().Mono(other.domain(), self.codomain())(
                lambda element: self(other(element))
            )
        return super().__mul__(other)


class SetSurjection(OwnedSetMorphism):
    r"""A set morphism supplied with the assertion that it is surjective."""

    def is_surjective(self) -> bool:
        return True

    def __mul__(self, other):
        if isinstance(other, SetSurjection) and other.codomain() is self.domain():
            return Sets().Epi(other.domain(), self.codomain())(
                lambda element: self(other(element))
            )
        return super().__mul__(other)


class SetInjectionHomset(SetMorCategory):
    r"""The declared injections between two sets."""

    def __call__(self, datum):
        if isinstance(datum, Morphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the set injection has the wrong source or target")
            if datum.parent() is self:
                return datum
            try:
                injective = datum.is_injective()
            except (AttributeError, NotImplementedError):
                injective = False
            if injective is not True:
                raise ValueError("a set monomorphism requires an injective map")
            return SetInjection(self, lambda element: datum(element))
        if not callable(datum):
            raise TypeError("a set injection is supplied by a callable")
        return SetInjection(self, datum)

    def arrow_set(self):
        return Sets().Mor(self.domain(), self.codomain())

    underlying_homset = arrow_set

    def accepts(self, arrow):
        if not (
            isinstance(arrow, Morphism)
            and arrow.domain() is self.domain()
            and arrow.codomain() is self.codomain()
        ):
            return False
        try:
            return arrow.is_injective() is True
        except (AttributeError, NotImplementedError):
            return False

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only for equal set endpoints")
        identity = SetInjection(self, lambda element: element)
        identity._preamble_is_identity = True
        return identity

    def super_categories(self):
        packet = self.base_category().category_packet()
        source = self.domain_object()
        target = self.codomain_object()
        inherited = [
            superpacket.Monos().Of(source, target)
            for superpacket in packet.super_packets()
            if source in superpacket.C() and target in superpacket.C()
        ]
        return [packet.Homs().Of(source, target), *inherited]

    def _repr_(self):
        return f"Mono_Set({self.domain()}, {self.codomain()})"


class SetSurjectionHomset(SetMorCategory):
    r"""The declared surjections between two sets."""

    def __call__(self, datum):
        if isinstance(datum, Morphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the set surjection has the wrong source or target")
            if datum.parent() is self:
                return datum
            try:
                surjective = datum.is_surjective()
            except (AttributeError, NotImplementedError):
                surjective = False
            if surjective is not True:
                raise ValueError("a set epimorphism requires a surjective map")
            return SetSurjection(self, lambda element: datum(element))
        if not callable(datum):
            raise TypeError("a set surjection is supplied by a callable")
        return SetSurjection(self, datum)

    def arrow_set(self):
        return Sets().Mor(self.domain(), self.codomain())

    underlying_homset = arrow_set

    def accepts(self, arrow):
        if not (
            isinstance(arrow, Morphism)
            and arrow.domain() is self.domain()
            and arrow.codomain() is self.codomain()
        ):
            return False
        try:
            return arrow.is_surjective() is True
        except (AttributeError, NotImplementedError):
            return False

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only for equal set endpoints")
        identity = SetSurjection(self, lambda element: element)
        identity._preamble_is_identity = True
        return identity

    def super_categories(self):
        packet = self.base_category().category_packet()
        source = self.domain_object()
        target = self.codomain_object()
        inherited = [
            superpacket.Epis().Of(source, target)
            for superpacket in packet.super_packets()
            if source in superpacket.C() and target in superpacket.C()
        ]
        return [packet.Homs().Of(source, target), *inherited]

    def _repr_(self):
        return f"Epi_Set({self.domain()}, {self.codomain()})"


class SetMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The declared monomorphisms of sets."""

    def fixed_category_class(self):
        return SetInjectionHomset


class SetEpiCategoryConstruction(EpiCategoryConstruction):
    r"""The declared epimorphisms of sets."""

    def fixed_category_class(self):
        return SetSurjectionHomset


Sets._MonoCategory = SetMonoCategoryConstruction
Sets._EpiCategory = SetEpiCategoryConstruction


class SetInclusion(OwnedSetMorphism):
    r"""A represented subobject inclusion \(A\hookrightarrow X\)."""

    def __init__(
        self,
        domain: Parent,
        codomain: Parent,
        characteristic_morphism: SetMorphism | None = None,
        finite_members: Iterable[SourcePointT] | None = None,
    ) -> None:
        parent = Sets().Mor(domain, codomain)
        super().__init__(parent, lambda member: codomain(member))
        self._characteristic_morphism = characteristic_morphism
        self._finite_members = finite_members

    def inclusion(self) -> Self:
        return self

    def __call__(self, member, *args, **kwargs):
        r"""Apply the inclusion using the ambient set's owned ingress."""
        ambient_member = self.codomain()(member)
        match ambient_member in self:
            case True:
                return ambient_member
            case _:
                raise ValueError(f"{member!r} is not in this represented subset")

    def is_injective(self) -> bool:
        return True

    def factor_through(self, target_inclusion: SetInclusion) -> SetMorphism:
        r"""Return the canonical map of subset objects when this subset is contained."""
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError("subset factorization requires one common base set")
        if not self <= target_inclusion:
            raise ValueError("the first subset is not contained in the second")
        return Sets().Mor(self.domain(), target_inclusion.domain())(lambda member: target_inclusion.domain()(self(member)))

    def underlying_set(self) -> Parent:
        return self.domain()

    def characteristic_morphism(self) -> SetMorphism:
        assert self._characteristic_morphism is not None, (
            "characteristic_morphism requires a represented decidable subset predicate"
        )
        return self._characteristic_morphism

    def __contains__(self, member) -> bool:
        try:
            member = self.codomain()(member)
        except (TypeError, ValueError):
            return False
        if self._finite_members is not None:
            return member in self._finite_members
        characteristic = self.characteristic_morphism()
        return characteristic(member) == characteristic.codomain()(1)

    def __iter__(self):
        if self._finite_members is not None:
            return iter(self._finite_members)
        return iter(self.domain())

    def cardinality(self) -> Parent:
        if self._finite_members is not None:
            return cardinal(len(self._finite_members))
        return cardinal(self.domain().cardinality())

    def __len__(self) -> int:
        size = self.cardinality()
        if not size.is_finite():
            raise TypeError("length is defined only for finite subsets")
        return int(size)

    def _check_common_base(self, other) -> None:
        if self.codomain() is not other.codomain():
            raise ValueError("subset operations require one common base set")

    def __le__(self, other) -> bool:
        self._check_common_base(other)
        if self._finite_members is not None:
            return all(member in other for member in self._finite_members)
        base = self.codomain()
        assert base in FiniteEnumeratedSets(), (
            "subset comparison requires a finite enumerated base or an explicitly finite source subset"
        )
        return all(member not in self or member in other for member in base)

    def union(self, other: SetInclusion) -> SetInclusion:
        self._check_common_base(other)
        return self.codomain().power_set().from_predicate(lambda member: member in self or member in other)

    def intersection(self, other: SetInclusion) -> SetInclusion:
        self._check_common_base(other)
        return self.codomain().power_set().from_predicate(lambda member: member in self and member in other)

    def difference(self, other: SetInclusion) -> SetInclusion:
        self._check_common_base(other)
        return self.codomain().power_set().from_predicate(lambda member: member in self and member not in other)

    def symmetric_difference(self, other: SetInclusion) -> SetInclusion:
        self._check_common_base(other)
        return self.codomain().power_set().from_predicate(lambda member: (member in self) != (member in other))

    def complement(self) -> SetInclusion:
        return self.codomain().power_set().from_predicate(lambda member: member not in self)

    def __or__(self, other):
        return self.union(other)

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other not in self.codomain().power_set():
            return False
        if self._finite_members is not None and other._finite_members is not None:
            return len(self._finite_members) == len(other._finite_members) and all(member in other for member in self._finite_members)
        if self.codomain() in FiniteEnumeratedSets():
            return all((member in self) == (member in other) for member in self.codomain())
        return self._characteristic_morphism is other._characteristic_morphism

    def __ne__(self, other) -> bool:
        return not self == other

    def _repr_(self) -> str:
        return f"Subobject of {self.codomain()} defined by {self.domain()}"


class PowerSets(OwnedCategory):
    r"""The power object \(P(X)\), represented by subobjects of ``X``."""

    def an_object(self) -> Parent:
        r"""One object of this category."""
        return Sets.Δ[2].power_set()

    def super_categories(self):
        return [Sets()]

    def __call__(self, base_set):
        r"""Construct ``P(base_set)`` even when ``base_set`` is itself a power set."""
        return self._call_(base_set)

    def _call_(self, base_set):
        r"""Construct the power object of ``base_set``."""
        return _object_of(self, base_set=base_set)

    class ParentMethods:
        def __init__(self, base_set: Parent, **rest) -> None:
            assert base_set in Sets(), "a power set is formed from an owned set"
            self._base_set = base_set
            super().__init__(**rest)

        def base_set(self) -> Parent:
            return self._base_set

        def truth_values(self) -> Parent:
            return Sets.Δ[1]

        def characteristic_homset(self) -> SetMorCategory:
            return Sets().Mor(self.base_set(), self.truth_values())

        characteristic_hom_category = characteristic_homset

        def _subset_from_predicate(self, predicate: Callable):
            truth_values = self.truth_values()
            characteristic = self.characteristic_homset()(lambda member: truth_values(int(bool(predicate(member)))))
            domain = self.base_set().condition_set(predicate)
            return SetInclusion(domain, self.base_set(), characteristic)

        def from_predicate(
            self,
            predicate: Callable[[SourcePointT], bool],
        ) -> SetInclusion:
            return self._subset_from_predicate(predicate)

        def from_characteristic_morphism(
            self,
            characteristic_morphism: SetMorphism,
        ) -> SetInclusion:
            if characteristic_morphism.parent() is not self.characteristic_homset():
                raise ValueError("a characteristic morphism must lie in Hom(X, Δ[1])")
            truth = self.truth_values()(1)

            def predicate(member):
                return characteristic_morphism(member) == truth

            domain = self.base_set().condition_set(predicate)
            return SetInclusion(domain, self.base_set(), characteristic_morphism)

        def _from_finite_members(self, members):
            normalized = []
            for member in members:
                try:
                    member = self.base_set()(member)
                except (TypeError, ValueError) as error:
                    raise ValueError(f"{member!r} is not in {self.base_set()}") from error
                if member not in normalized:
                    normalized.append(member)
            frozen = tuple(normalized)
            truth_values = self.truth_values()
            characteristic = self.characteristic_homset()(lambda member: truth_values(int(member in frozen)))
            domain = self.base_set().condition_set(lambda member: member in frozen)
            return SetInclusion(domain, self.base_set(), characteristic, frozen)

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, candidate):
            if isinstance(candidate, SetInclusion):
                if candidate.codomain() is not self.base_set():
                    raise ValueError("the subobject has a different base set")
                return candidate
            if candidate is self.base_set():
                return self.from_predicate(lambda _member: True)
            if candidate in Sets() and candidate in FiniteEnumeratedSets():
                return self._from_finite_members(candidate)
            if isinstance(candidate, Iterable):
                return self._from_finite_members(candidate)
            raise TypeError(f"{candidate!r} does not present a subset of {self.base_set()}")

        def __contains__(self, candidate) -> bool:
            if isinstance(candidate, SetInclusion):
                return candidate.codomain() is self.base_set()
            if candidate is self.base_set():
                return True
            if candidate in Sets() and candidate in FiniteEnumeratedSets():
                return all(member in self.base_set() for member in candidate)
            if isinstance(candidate, Iterable):
                return all(member in self.base_set() for member in candidate)
            return False

        def top(self) -> SetInclusion:
            return self(self.base_set())

        def bottom(self) -> SetInclusion:
            return self(())

        def inverse_image_morphism(self, morphism: SetMorphism) -> SetMorphism:
            if morphism.codomain() is not self.base_set():
                raise ValueError("inverse image requires the morphism codomain to be the base set")
            target = morphism.domain().power_set()
            return Sets().Mor(self, target)(lambda subset: target.from_predicate(lambda member: morphism(member) in subset))

        def direct_image_morphism(self, morphism: SetMorphism) -> SetMorphism:
            if morphism.domain() is not self.base_set():
                raise ValueError("direct image requires the morphism domain to be the base set")
            target = morphism.codomain().power_set()

            def direct_image(subset):
                size = subset.cardinality()
                if not size.is_finite():
                    image_domain = subset.domain().image_set(morphism)
                    return SetInclusion(image_domain, morphism.codomain())
                return target(tuple(morphism(member) for member in subset))

            return Sets().Mor(self, target)(direct_image)

        def __iter__(self):
            if self.base_set() not in FiniteEnumeratedSets():
                raise TypeError("only a finite power set has a chosen enumeration")
            return (self(subset) for subset in SageSubsets(self.base_set()))

        def cardinality(self) -> Parent:
            return cardinal(2) ** cardinal(self.base_set().cardinality())

        def cardinality_comparison(self) -> CardinalityMorphism:
            size = self.cardinality()
            return Cardinalities().Mor(size, size).identity()

        def _repr_(self) -> str:
            return f"Power set of {self.base_set()}"


@cached_function
def _power_set(base_set: Parent) -> Parent:
    return PowerSets()(base_set)


def _function_set_of(codomain, exponent):
    r"""Build \(Y^X\) and place it.

    Over a finite exponent every function is finitely supported, and over an
    infinite one that is exactly what fails, so the refinement is read off the
    exponent.
    """
    from dzack_research.preamble.refine import refine

    exponential = _object_of(FunctionSets(), codomain=codomain, exponent=exponent)
    if exponent in FiniteSets():
        refine(exponential, FinitelySupportedFunctionSets())
    return exponential


class FunctionSets(OwnedCategory):
    r"""Exponentials \(Y^X=\operatorname{Hom}_{Set}(X,Y)\)."""

    def an_object(self) -> Parent:
        r"""\(\Delta_2^{\Delta_1}\)."""
        return Sets.Δ[2].exponential(Sets.Δ[1])

    def super_categories(self):
        return [Sets()]

    def _call_(self, codomain, exponent):
        r"""Construct the exponential ``codomain^exponent``."""
        return _function_set_of(codomain, exponent)

    class ParentMethods:
        def __init__(self, codomain: Parent, exponent: Parent, **rest) -> None:
            assert codomain in Sets() and exponent in Sets(), "an exponential requires two owned sets"
            self._codomain = codomain
            self._exponent = exponent
            super().__init__(**rest)

        def base(self) -> Parent:
            return self._codomain

        def exponent(self) -> Parent:
            return self._exponent

        def _preamble_all_functions_finitely_supported(self) -> bool:
            return self.exponent() in FiniteSets()

        def homset(self) -> SetMorCategory:
            return Sets().Mor(self.exponent(), self.base())

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, definition):
            homset = self.homset()
            if definition in homset:
                return definition
            return homset(definition)

        def __contains__(self, function) -> bool:
            return function in self.homset()

        def cardinality(self) -> Parent:
            return cardinal(self.base().cardinality()) ** cardinal(self.exponent().cardinality())

        def _repr_(self) -> str:
            return f"{self.base()}^{self.exponent()}"


@cached_function
def _exponential_of_sets(codomain: Parent, exponent: Parent) -> Parent:
    return FunctionSets()(codomain, exponent)


class FixedCardinalitySubsetSets(OwnedCategory):
    r"""The sets \([X]^k\) of subsets of one fixed finite cardinality."""

    def an_object(self) -> Parent:
        r"""One object of this category."""
        return Sets.Δ[2].subsets_of_size(2)

    def super_categories(self):
        return [Sets()]

    def _call_(self, source, subset_cardinality):
        r"""Construct the set of subsets of ``source`` of the stated cardinality."""
        return _object_of(
            self,
            source=source,
            subset_cardinality=subset_cardinality,
        )

    class ParentMethods:
        def __init__(self, source: Parent, subset_cardinality: int, **rest) -> None:
            self._source = source
            self._subset_cardinality = int(subset_cardinality)
            assert self._subset_cardinality >= 0, "a subset cardinality is nonnegative"
            super().__init__(**rest)

        def source(self) -> Parent:
            return self._source

        def subset_cardinality(self) -> int:
            return self._subset_cardinality

        def power_set(self) -> Parent:
            return self.source().power_set()

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, members):
            subset = self.power_set()(members)
            if subset.cardinality() != cardinal(self.subset_cardinality()):
                raise ValueError(f"a member of {self} has cardinality {self.subset_cardinality()}")
            return subset

        def __contains__(self, candidate) -> bool:
            if candidate not in self.power_set():
                return False
            return self.power_set()(candidate).cardinality() == cardinal(self.subset_cardinality())

        def __iter__(self):
            if self.source() not in FiniteEnumeratedSets():
                raise TypeError("the current enumeration of fixed-cardinality subsets requires a finite source")
            return (self(tuple(subset)) for subset in SageSubsets(self.source(), self.subset_cardinality()))

        def cardinality(self) -> Parent:
            from math import comb

            source_size = cardinal(self.source().cardinality())
            if self.subset_cardinality() == 0:
                return cardinal(1)
            if source_size.is_finite():
                return cardinal(comb(int(source_size), self.subset_cardinality()))
            return source_size

        def _repr_(self) -> str:
            return f"Subsets of {self.source()} of cardinality {self.subset_cardinality()}"


@cached_function
def _subsets_of_size(source: Parent, subset_cardinality: int) -> Parent:
    return FixedCardinalitySubsetSets()(source, subset_cardinality)


class FinitePowerSets(OwnedCategory):
    r"""Finite power objects \(P_{fin}(X)\), the finite subsets of \(X\)."""

    def an_object(self) -> Parent:
        r"""One object of this category."""
        return Sets.Δ[2].finite_subsets()

    def super_categories(self):
        return [Sets()]

    def _call_(self, source):
        r"""Construct the finite-subset object of ``source``."""
        return _object_of(self, source=source)

    class ParentMethods:
        def __init__(self, source: Parent, **rest) -> None:
            self._source = source
            super().__init__(**rest)

        def source(self) -> Parent:
            return self._source

        def power_set(self) -> Parent:
            return self.source().power_set()

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, members):
            subset = self.power_set()(members)
            if not subset.cardinality().is_finite():
                raise ValueError("a member of the finite powerset must be finite")
            return subset

        def __contains__(self, candidate) -> bool:
            if candidate not in self.power_set():
                return False
            return self.power_set()(candidate).cardinality().is_finite()

        def __iter__(self):
            if self.source() not in FiniteEnumeratedSets():
                raise TypeError("the current enumeration of finite subsets requires a finite source")
            return (self(tuple(subset)) for subset in SageSubsets(self.source()))

        def cardinality(self) -> Parent:
            source_size = cardinal(self.source().cardinality())
            if source_size.is_finite():
                return cardinal(2) ** source_size
            return source_size

        def _repr_(self) -> str:
            return f"Finite subsets of {self.source()}"


@cached_function
def _finite_subsets(source: Parent) -> Parent:
    return FinitePowerSets()(source)


@cached_function(key=lambda index_set, family: (id(index_set), id(family)))
def _cartesian_product_of[IndexT](index_set: Parent, family: Callable[[IndexT], Parent]) -> Parent:
    r"""Build the product and place it.

    Finiteness is a fact about the index set and the factors; the product is
    built in the category it always belongs to and gains the enumerated
    placement it earns.
    """
    if not isinstance(family, IndexedFamily):
        family = indexed_family(index_set, family)
    if family.index_set() is not index_set:
        raise ValueError("the product family has a different index set")
    product_category = CartesianProductsOfSets()
    placements = [product_category]
    if index_set in FiniteSets() and index_set in EnumeratedSets():
        from dzack_research.preamble.categories.group.magmas import AdditiveMonoids

        if all(family(index) in AdditiveMonoids() for index in index_set):
            placements.append(CartesianProductsOfAdditiveMonoids())
        factor_cardinalities = tuple(
            cardinal(family(index).cardinality()) for index in index_set
        )
        product_cardinality = Cardinalities().product(*factor_cardinalities)
        if product_cardinality.is_finite():
            if all(
                family(index) in FiniteSets() and family(index) in EnumeratedSets()
                for index in index_set
            ):
                category = Category.join(
                    [FiniteEnumeratedCartesianProductsOfSets(), *placements]
                )
                return product_category.ObjectType(
                    category=category,
                    index_set=index_set,
                    family=family,
                )
            placements.append(FiniteSets())
        elif product_cardinality.is_countably_infinite():
            placements.append(Sets().Countable().Infinite())
    category = Category.join(placements)
    return product_category.ObjectType(category=category, index_set=index_set, family=family)


class CartesianProductsOfSets(OwnedCategory):
    r"""Dependent products of families of sets."""

    class ElementMethods(Element):
        r"""What an element of a product of a family is."""

        def __init__(
            self,
            parent: Parent,
            components: Callable[[IndexT], SourcePointT],
            *,
            positional_components: tuple[SourcePointT, ...] | None = None,
        ) -> None:
            Element.__init__(self, parent)
            self._components = components
            self._positional_components = positional_components

        def component(self, index: IndexT) -> SourcePointT:
            normalized = self.parent().index_set()(index)
            if self._positional_components is not None:
                position = int(self.parent().index_set().ranking_map()(normalized))
                return self._positional_components[position]
            value = self._components(normalized)
            return self.parent().factor(normalized)(value)

        def __getitem__(self, index):
            return self.component(index)

        def __iter__(self):
            return (self.component(index) for index in self.parent().index_set())

        def _repr_(self) -> str:
            if not self.parent().has_finite_index_set():
                return f"Section of {self.parent()}"
            return "(" + ", ".join(repr(self.component(index)) for index in self.parent().index_set()) + ")"

        def __eq__(self, other) -> bool | UnknownClass:
            if self is other:
                return True
            if not isinstance(other, Element) or other.parent() is not self.parent():
                return False
            if not self.parent().has_finite_index_set():
                return True if self._components is other._components else Unknown
            answer = True
            finite_enumerated = self.parent() in FiniteEnumeratedCartesianProductsOfSets()
            for index in self.parent().index_set():
                left = self.component(index)
                right = other.component(index)
                if left is right:
                    continue
                equal = left == right
                if equal is False:
                    return False
                if equal is True:
                    continue
                if finite_enumerated:
                    factor_ranking = self.parent().factor(index).ranking_map()
                    if factor_ranking(left) != factor_ranking(right):
                        return False
                    continue
                answer = Unknown
            return answer

        def __ne__(self, other) -> bool | UnknownClass:
            equal = self == other
            return Unknown if equal is Unknown else not equal

        def __hash__(self) -> int:
            if not self.parent().has_finite_index_set():
                return hash(id(self.parent()))
            components = tuple(
                self.component(index) for index in self.parent().index_set()
            )
            return hash((id(self.parent()), components))

    def _call_(self, index_set, family):
        r"""Construct the dependent product of the stated family of sets."""
        return _cartesian_product_of(index_set, family)

    class ParentMethods:
        def __init__(
            self,
            index_set: Parent,
            family: Callable[[IndexT], Parent],
            **rest,
        ) -> None:
            assert index_set in Sets(), "the index object of a product family must be an owned set"
            self._index_set = index_set
            if isinstance(family, IndexedFamily):
                if family.index_set() is not index_set:
                    raise ValueError("the family and its construction have different index sets")
                self._family = family
            else:
                self._family = indexed_family(index_set, family)
            super().__init__(**rest)

        def index_set(self) -> Parent:
            return self._index_set

        def family(self) -> IndexedFamily[IndexT, Parent]:
            return self._family

        def has_finite_index_set(self) -> bool:
            return self.index_set() in FiniteSets()

        def factor(self, index: IndexT) -> Parent:
            normalized = self.index_set()(index)
            factor = self.family()(normalized)
            if factor not in Sets():
                raise TypeError("every factor of a set product must be an owned set")
            return factor

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, components):
            if isinstance(components, self.category().ElementType):
                if components.parent() is self:
                    return components
                raise ValueError("the section belongs to a different product")
            if callable(components):
                return self.element_class(self, components)
            if not self.has_finite_index_set() or self.index_set() not in EnumeratedSets():
                raise TypeError("a positional product element requires a finite enumerated index set; otherwise supply a callable section")
            values = iter(components)
            assignment = {}
            for position, index in enumerate(self.index_set()):
                try:
                    value = next(values)
                except StopIteration as error:
                    raise ValueError("a product element needs one component per factor") from error
                assignment[position] = self.factor(index)(value)
            try:
                next(values)
            except StopIteration:
                pass
            else:
                raise ValueError("a product element needs one component per factor")
            ranking = self.index_set().ranking_map()
            positional = tuple(assignment[position] for position in range(len(assignment)))
            return self.element_class(
                self,
                lambda index: positional[int(ranking(index))],
                positional_components=positional,
            )

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            return _cartesian_product_ranking_map(self)

        def projection(self, index: IndexT) -> SetMorphism:
            normalized = self.index_set()(index)
            return Sets().Mor(self, self.factor(normalized))(lambda element: element.component(normalized))

        def from_maps(
            self,
            source: Parent,
            maps: Callable[[IndexT], SetMorphism],
        ) -> SetMorphism:
            r"""Return the unique map into the product with the stated components."""
            return Sets().Mor(source, self)(lambda element: self(lambda index: maps(index)(element)))

        def cardinality(self) -> Parent:
            return Cardinalities().indexed_product(self.index_set(), lambda index: cardinal(self.factor(index).cardinality()))

        def __iter__(self):
            if not self.has_finite_index_set():
                raise TypeError(
                    "an infinite-index product is specified by a callable section and has no represented enumeration here"
                )

            ranking = self.index_set().ranking_map()
            index_count = int(cardinal(self.index_set().cardinality()).finite_value())
            factors = tuple(
                self.factor(ranking.inverse()(position))
                for position in range(index_count)
            )
            factor_cardinalities = tuple(
                cardinal(factor.cardinality()) for factor in factors
            )

            if all(size.is_finite() for size in factor_cardinalities):
                def sections(position, assignment):
                    if position == index_count:
                        positional = tuple(assignment[offset] for offset in range(index_count))
                        yield self.element_class(
                            self,
                            lambda index, positional=positional: positional[int(ranking(index))],
                            positional_components=positional,
                        )
                        return
                    for value in factors[position]:
                        assignment[position] = value
                        yield from sections(position + 1, assignment)
                    assignment.pop(position, None)

                return sections(0, {})

            if not all(
                factor in EnumeratedSets() and size.is_countable()
                for factor, size in zip(factors, factor_cardinalities, strict=True)
            ):
                raise TypeError(
                    "a finite-index product is enumerable here only when every factor is finite or countably enumerated"
                )

            bounds = tuple(
                int(size.finite_value()) if size.is_finite() else None
                for size in factor_cardinalities
            )

            def weak_compositions(total, parts):
                if parts == 0:
                    if total == 0:
                        yield ()
                    return
                if parts == 1:
                    yield (total,)
                    return
                for first in range(total + 1):
                    for rest in weak_compositions(total - first, parts - 1):
                        yield (first, *rest)

            def countable_sections():
                for total in count():
                    for positions in weak_compositions(total, index_count):
                        if any(
                            bound is not None and position >= bound
                            for position, bound in zip(positions, bounds, strict=True)
                        ):
                            continue
                        values = tuple(
                            factor.ranking_map().inverse()(position)
                            for factor, position in zip(factors, positions, strict=True)
                        )
                        yield self(
                            lambda index, values=values: values[int(ranking(index))]
                        )

            return countable_sections()

        def _repr_(self) -> str:
            return f"Product of the family over {self.index_set()}"

    def an_object(self) -> Parent:
        r"""The square of the ordinal 2."""
        return Sets().product((finite_ordinal_set(2), finite_ordinal_set(2)))

    def super_categories(self):
        return [Sets()]


class CartesianProductsOfAdditiveMonoids(OwnedCategory):
    r"""Cartesian products with the componentwise additive-monoid structure."""

    def super_categories(self):
        from dzack_research.preamble.categories.group.magmas import AdditiveMonoids

        return [CartesianProductsOfSets(), AdditiveMonoids()]

    class ElementMethods:
        def __add__(self, other):
            other = self.parent()(other)
            return self.parent()(
                lambda index: self.component(index) + other.component(index)
            )

        __radd__ = __add__

    class ParentMethods:
        def zero(self):
            return self(lambda index: self.factor(index).zero())


def _cartesian_product_ranking_map(product) -> CategoricalIsomorphism:
    r"""Return the mixed-radix enumeration of a finite enumerated product.

    This is the enumeration datum that justifies placing the product in
    :class:`EnumeratedSets`.  Keeping it outside either category's method MRO
    lets the specialized placement expose the concrete map without duplicating
    the product algorithm.
    """
    assert product.has_finite_index_set(), (
        "the mixed-radix enumeration is represented over a finite index set"
    )
    assert product.index_set() in EnumeratedSets(), (
        "the mixed-radix enumeration reads its index order off the index set"
    )
    index_count = int(cardinal(product.index_set().cardinality()).finite_value())
    index_ranking = product.index_set().ranking_map()
    index_at = index_ranking.inverse()
    for index in product.index_set():
        factor = product.factor(index)
        assert factor in EnumeratedSets(), (
            f"the factor at {index} states no enumeration of its own"
        )
        assert cardinal(factor.cardinality()).is_finite(), (
            f"the factor at {index} is infinite, so the product's mixed-radix enumeration is not represented here"
        )
    total_size = int(cardinal(product.cardinality()).finite_value())

    def point_at(position):
        position = int(position)
        if position < 0 or position >= total_size:
            raise IndexError(position)
        assignment = {}
        quotient = position
        for offset in range(index_count - 1, -1, -1):
            index = index_at(offset)
            factor = product.factor(index)
            radix = int(cardinal(factor.cardinality()).finite_value())
            quotient, digit = divmod(quotient, radix)
            assignment[offset] = factor.ranking_map().inverse()(digit)
        return product(tuple(assignment[offset] for offset in range(index_count)))

    def position_of(section):
        section = product(section)
        position = 0
        for index in product.index_set():
            factor = product.factor(index)
            radix = int(cardinal(factor.cardinality()).finite_value())
            digit = int(factor.ranking_map()(section.component(index)))
            position = position * radix + digit
        return position

    return product._ranking_isomorphism(position_of, point_at)


class FiniteEnumeratedCartesianProductsOfSets(OwnedCategory):
    r"""Finite dependent products carrying their mixed-radix enumeration."""

    def super_categories(self):
        return [
            CartesianProductsOfSets(),
            EnumeratedSets(),
            FiniteSets(),
        ]

    class ParentMethods:
        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            return _cartesian_product_ranking_map(self)


class CoproductsOfSets(OwnedCategory):
    r"""Dependent coproducts (disjoint unions) of families of sets."""

    class ElementMethods(Element):
        r"""What an element of a coproduct of a family is."""

        def __init__(
            self,
            parent: Parent,
            index: IndexT,
            value: SourcePointT,
        ) -> None:
            Element.__init__(self, parent)
            normalized = parent.index_set()(index)
            self._index = normalized
            self._value = parent.cofactor(normalized)(value)

        def summand_index(self) -> IndexT:
            return self._index

        def summand_element(self) -> SourcePointT:
            return self._value

        def _repr_(self) -> str:
            return f"ι_{self.summand_index()}({self.summand_element()})"

        def __eq__(self, other) -> bool:
            return (
                isinstance(other, Element)
                and other.parent() is self.parent()
                and other.summand_index() == self.summand_index()
                and other.summand_element() == self.summand_element()
            )

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self) -> int:
            return hash((id(self.parent()), self.summand_index(), self.summand_element()))

    def _call_(self, index_set, family):
        r"""Construct the dependent coproduct of the stated family of sets."""
        return _coproduct_of_indexed_family(index_set, family)

    class ParentMethods:
        def __init__(
            self,
            index_set: Parent,
            family: Callable[[IndexT], Parent],
            **rest,
        ) -> None:
            assert index_set in Sets(), "the index object of a coproduct family must be an owned set"
            self._index_set = index_set
            if isinstance(family, IndexedFamily):
                if family.index_set() is not index_set:
                    raise ValueError("the family and its construction have different index sets")
                self._family = family
            else:
                self._family = indexed_family(index_set, family)
            super().__init__(**rest)

        def index_set(self) -> Parent:
            return self._index_set

        def family(self) -> IndexedFamily[IndexT, Parent]:
            return self._family

        def cofactor(self, index: IndexT) -> Parent:
            normalized = self.index_set()(index)
            cofactor = self.family()(normalized)
            if cofactor not in Sets():
                raise TypeError("every cofactor of a set coproduct must be an owned set")
            return cofactor

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, datum, value=None):
            if isinstance(datum, self.category().ElementType):
                if datum.parent() is self:
                    return datum
                raise ValueError("the element belongs to a different coproduct")
            if value is None:
                index, value = datum
            else:
                index = datum
            return self.element_class(self, index, value)

        def injection(self, index: IndexT) -> SetMorphism:
            normalized = self.index_set()(index)
            return Sets().Mor(self.cofactor(normalized), self)(lambda element: self(normalized, element))

        def from_maps(
            self,
            target: Parent,
            maps: Callable[[IndexT], SetMorphism],
        ) -> SetMorphism:
            r"""Return the unique map out of the coproduct extending the stated maps."""
            return Sets().Mor(self, target)(lambda element: maps(element.summand_index())(element.summand_element()))

        def cardinality(self) -> Parent:
            return Cardinalities().indexed_sum(self.index_set(), lambda index: cardinal(self.cofactor(index).cardinality()))

        def _finite_index_count(self):
            try:
                size = cardinal(self.index_set().cardinality())
                if size.is_finite():
                    return int(size.finite_value())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass
            return None

        @staticmethod
        def _factor_point_at(factor, position):
            from itertools import islice

            if factor in EnumeratedSets():
                return factor.ranking_map().inverse()(position)
            try:
                return next(islice(iter(factor), position, position + 1))
            except StopIteration as error:
                raise IndexError(position) from error

        @staticmethod
        def _factor_position_of(factor, value):
            if factor in EnumeratedSets():
                return int(factor.ranking_map()(value))
            for position, candidate in enumerate(factor):
                if candidate == value:
                    return position
            raise ValueError(value)

        def _factor_has_position(self, factor, position) -> bool:
            try:
                size = cardinal(factor.cardinality())
                if size.is_finite():
                    return position < int(size.finite_value())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass
            try:
                self._factor_point_at(factor, position)
            except (IndexError, ValueError):
                return False
            return True

        def _known_finite_size(self):
            try:
                size = self.cardinality()
                if size.is_finite():
                    return int(size.finite_value())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass
            return None

        def _enumeration_pairs(self):
            r"""Yield ``(index_position, factor_position)`` in a total rank order."""
            finite_index_count = self._finite_index_count()
            if finite_index_count is not None:
                layer = 0
                while True:
                    emitted = False
                    index_at = self.index_set().ranking_map().inverse()
                    for index_position in range(finite_index_count):
                        index = index_at(index_position)
                        factor = self.cofactor(index)
                        if self._factor_has_position(factor, layer):
                            emitted = True
                            yield index_position, layer
                    if not emitted and self._known_finite_size() is not None:
                        return
                    layer += 1
                return

            # Countably indexed coproduct: diagonalize N x N.  Missing positions in
            # finite/empty summands are skipped; no index family is materialized.
            index_at = self.index_set().ranking_map().inverse()
            diagonal = 0
            while True:
                for index_position in range(diagonal + 1):
                    factor_position = diagonal - index_position
                    try:
                        index = index_at(index_position)
                    except (IndexError, ValueError):
                        continue
                    factor = self.cofactor(index)
                    if self._factor_has_position(factor, factor_position):
                        yield index_position, factor_position
                diagonal += 1

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""The lazy enumeration by rank layer, diagonalized when infinite."""

            def point_at(position):
                position = int(position)
                if position < 0:
                    raise IndexError(position)
                finite_size = self._known_finite_size()
                if finite_size is not None and position >= finite_size:
                    raise IndexError(position)
                index_at = self.index_set().ranking_map().inverse()
                for reached, (index_position, factor_position) in enumerate(self._enumeration_pairs()):
                    if reached != position:
                        continue
                    index = index_at(index_position)
                    return self(
                        index,
                        self._factor_point_at(self.cofactor(index), factor_position),
                    )
                raise IndexError(position)

            def position_of(element):
                element = self(element)
                summand = element.summand_index()
                target = (
                    int(self.index_set().ranking_map()(summand)),
                    self._factor_position_of(self.cofactor(summand), element.summand_element()),
                )
                for position, pair in enumerate(self._enumeration_pairs()):
                    if pair == target:
                        return position
                raise ValueError(element)

            return self._ranking_isomorphism(position_of, point_at)

        def __contains__(self, element) -> bool:
            return element.parent() is self

        is_parent_of = __contains__

        def __iter__(self):
            finite_size = self._known_finite_size()
            positions = range(finite_size) if finite_size is not None else count()
            point_at = self.ranking_map().inverse()
            return (point_at(position) for position in positions)

        def _repr_(self) -> str:
            return f"Coproduct of the family over {self.index_set()}"

    def an_object(self) -> Parent:
        r"""The disjoint union of the ordinal 2 with itself."""
        return Sets().coproduct((finite_ordinal_set(2), finite_ordinal_set(2)))

    def super_categories(self):
        return [Sets()]


DisjointUnionsOfSets = CoproductsOfSets


def _finite_family_key(family: IndexedFamily) -> tuple[int, tuple[int, ...]]:
    r"""Intern a finite construction by its exact index set and factor objects.

    Resolving a finite family is legitimate here; its labels are retained by
    the family rather than replaced by positions.  The resulting parent keeps
    the family and its factors alive, so identity keys cannot be recycled.
    """
    return id(family.index_set()), tuple(id(value) for value in family)


@cached_function(key=_finite_family_key)
def _cartesian_product_of_finite_family(family: IndexedFamily) -> Parent:
    return CartesianProductsOfSets()(family.index_set(), family)


def _cartesian_product_of_family[IndexT](
    index_set: Parent,
    family: Callable[[IndexT], Parent],
) -> Parent:
    r"""Construct a product retaining its chosen labels and factor parents.

    Unverified specimens for nonordinal labels and canonical finite products::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: labels = finite_ordered_set(("red", "blue"))
        sage: points = finite_ordered_set(("a", "b"))
        sage: family = indexed_family(labels, lambda label: points)
        sage: product = Sets().product(family)
        sage: product.index_set() is labels
        True
        sage: product is Sets().product(indexed_family(labels, lambda label: points))
        True
        sage: section = product(lambda label: "a" if label == "red" else "b")
        sage: product.projection("red")(section), product.projection("blue")(section)
        ('a', 'b')
        sage: coproduct = Sets().coproduct(family)
        sage: point = coproduct.injection("blue")("a")
        sage: point.summand_index(), point.summand_element()
        ('blue', 'a')
        sage: coproduct.index_set() is labels
        True

    Unverified specimens for unhashable labels and empty products::

        sage: labels = finite_ordered_set(([0], [1]))
        sage: product = Sets().product(indexed_family(labels, lambda label: points))
        sage: section = product(("a", "b"))
        sage: product.projection([0])(section), product.projection([1])(section)
        ('a', 'b')
        sage: product.ranking_map().inverse()(product.ranking_map()(section)) == section
        True
        sage: len(tuple(product))
        4
        sage: unit = points ** 0
        sage: unit.cardinality() == cardinal(1)
        True
        sage: unit(()) == unit.ranking_map().inverse()(0)
        True
    """
    if isinstance(family, IndexedFamily) and family.index_set() is not index_set:
        raise ValueError("the product family has a different index set")
    if index_set in FiniteSets() and index_set in EnumeratedSets():
        return _cartesian_product_of_finite_family(indexed_family(index_set, family))
    return CartesianProductsOfSets()(index_set, family)



def _cartesian_product_morphism[IndexT](
    source: Parent,
    target: Parent,
    component_morphisms: Callable[[IndexT], SetMorphism],
) -> SetMorphism:
    r"""Return the componentwise map between two dependent products."""
    if source.index_set() is not target.index_set():
        raise ValueError("componentwise product maps require one index set")
    return Sets().Mor(source, target)(lambda element: target(lambda index: component_morphisms(index)(element.component(index))))


@cached_function(key=_finite_family_key)
def _coproduct_of_finite_family(family: IndexedFamily) -> Parent:
    return CoproductsOfSets()(family.index_set(), family)


@cached_function(key=lambda index_set, family: (id(index_set), id(family)))
def _coproduct_of_indexed_family[IndexT](index_set: Parent, family: Callable[[IndexT], Parent]) -> Parent:
    return _object_of(CoproductsOfSets(), index_set=index_set, family=family)


def _coproduct_of_family[IndexT](
    index_set: Parent,
    family: Callable[[IndexT], Parent],
) -> Parent:
    if isinstance(family, IndexedFamily) and family.index_set() is not index_set:
        raise ValueError("the coproduct family has a different index set")
    if index_set in FiniteSets() and index_set in EnumeratedSets():
        return _coproduct_of_finite_family(indexed_family(index_set, family))
    return CoproductsOfSets()(index_set, family)



def _coproduct_morphism[IndexT](
    source: Parent,
    target: Parent,
    component_morphisms: Callable[[IndexT], SetMorphism],
) -> SetMorphism:
    r"""Return the componentwise map between two dependent coproducts."""
    if source.index_set() is not target.index_set():
        raise ValueError("componentwise coproduct maps require one index set")
    return Sets().Mor(source, target)(
        lambda element: target(
            element.summand_index(),
            component_morphisms(element.summand_index())(element.summand_element()),
        )
    )


ObjectSetsOfDiscreteCategories = SageSets
ExponentialsOfSets = FunctionSets


class NaturalNumberSets(OwnedCategory):
    r"""The owned set \(\mathbb{N}=\{0,1,2,\dots\}\)."""

    def an_object(self) -> Parent:
        r"""\(\mathbb{N}\)."""
        return NN

    def super_categories(self):
        from dzack_research.preamble.categories.group.magmas import AdditiveMonoids

        # The identity ranking is the chosen enumeration.  Declared by the
        # category rather than joined for the one object.
        return [
            EnumeratedSets(),
            Sets().Infinite(),
            TotallyOrderedSets(),
            AdditiveMonoids(),
        ]

    class ElementMethods(Element):
        r"""What a natural number is."""

        def __init__(self, parent: Parent, value: SupportsInt) -> None:
            Element.__init__(self, parent)
            # This constructor is an ingress boundary.  It accepts the owned
            # integer view without importing the higher ring theory back into Sets;
            # the ring exposes only this private runtime marker/engine pair.
            from sage.rings.integer_ring import ZZ as _SageZZ

            if isinstance(value, parent.category().ElementType):
                value = int(value)
            elif isinstance(value, SageObject):
                parent = element_parent(value)
                if not (bool(getattr(parent, "_preamble_owned_ring_parent", False)) and getattr(parent, "_engine", None) is _SageZZ):
                    raise TypeError("raw backend integers are not accepted by the owned natural numbers")
                value = int(value)
            value = int(value)
            if value < 0:
                raise ValueError("a natural number is nonnegative")
            self._value = value

        def __int__(self) -> int:
            return self._value

        __index__ = __int__

        def __hash__(self):
            # Equality is decided on the number, not on the parent that
            # presented it, so the hash is the number's.
            return hash(self._value)

        def __eq__(self, other: Any) -> bool:
            # Normalize once.  Asking membership first constructs the same
            # natural number and can recurse through equality during ranking.
            try:
                normalized = self.parent()(other)
            except (TypeError, ValueError):
                return False
            return normalized._value == self._value

        def __ne__(self, other):
            return not self == other

        def __lt__(self, other):
            other = self.parent()(other)
            return self._value < other._value

        def __le__(self, other):
            other = self.parent()(other)
            return self._value <= other._value

        def __add__(self, other):
            other = self.parent()(other)
            return self.parent()(self._value + int(other))

        __radd__ = __add__

        def __sub__(self, other):
            other = self.parent()(other)
            return self.parent()(self._value - int(other))

        def __rsub__(self, other):
            return self.parent()(int(other) - self._value)

        def __mod__(self, other):
            divisor = int(self.parent()(other))
            match divisor:
                case 0:
                    raise ZeroDivisionError("natural-number remainder by zero")
                case _:
                    return self.parent()(self._value % divisor)

        def _repr_(self):
            return str(self._value)

    class ParentMethods:
        def __init__(self, **rest) -> None:
            super().__init__(**rest)

        def _element_constructor_(self, value):
            if isinstance(value, self.category().ElementType) and value.parent() is self:
                return value
            return self.element_class(self, value)

        def __call__(self, value):
            r"""Construct an owned natural number without Sage coercion discovery."""
            return self._element_constructor_(value)

        def __contains__(self, value) -> bool:
            r"""Decide whether ``value`` names a natural number.

            The argument is genuinely arbitrary here, so the question is
            whether this set has a point for it, and that is what the element
            constructor decides.  A nonnegative owned integer names one, since
            $\mathbb N\subset\mathbb Z$, and so does the literal a
            mathematician writes at a prompt.
            """
            try:
                self._element_constructor_(value)
            except (TypeError, ValueError):
                return False
            return True

        def __iter__(self):
            index = 0
            while True:
                yield self(index)
                index += 1

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""The identity: $\mathbb N$ is the ordinal $\omega$ that counts it."""
            return self._ranking_isomorphism(lambda value: int(self(value)), self)

        def cardinality(self) -> Parent:
            from dzack_research.preamble.categories.sets.cardinals import aleph0

            return aleph0

        def zero(self) -> Element:
            return self(0)

        def _repr_(self):
            return "NN = {0, 1, 2, ...}"

        def _latex_(self):
            return r"\mathbb{N}=\{0,1,2,\ldots\}"


class Homsets(OwnedCategory):
    r"""Hom objects \(\operatorname{Hom}(X,Y)\), which are sets."""

    def an_object(self) -> SetMorCategory:
        r"""The endomorphisms of a set, which hold at least its identity."""
        witness = Sets().an_object()
        return Sets().Mor(witness, witness)

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def is_endomorphism_set(self) -> bool:
            return self.domain() is self.codomain()


class PartiallyOrderedSets(OwnedCategory):
    r"""Sets equipped with a partial order."""

    def an_object(self) -> Parent:
        r"""The natural numbers under their usual order."""
        return NN

    def super_categories(self):
        return [Sets()]


class TotallyOrderedSets(OwnedCategory):
    r"""Sets equipped with a total order."""

    def an_object(self) -> Parent:
        r"""The natural numbers, totally ordered."""
        return NN

    def super_categories(self):
        return [PartiallyOrderedSets()]


NN = _object_of(NaturalNumberSets())


class FinitelySupportedFunctionSets(OwnedCategory):
    r"""Function sets whose elements have finite support."""

    _certifying_predicate = "_preamble_all_functions_finitely_supported"

    def an_object(self) -> Parent:
        r"""Functions from the ordinal 2 to itself, all of finite support."""
        return finite_ordinal_set(2).exponential(finite_ordinal_set(2))

    def super_categories(self):
        return [Sets()]


def register_set_axioms() -> None:
    r"""Compatibility entry point: the live owned categories need no Sage-global mutation."""
    return None


class SetSubcategoryMethods:
    r"""Compatibility name for the owned Set category-navigation surface."""


__all__ = [
    "CartesianProductsOfSets",
    "CountableSets",
    "CountablyInfiniteSets",
    "CoproductsOfSets",
    "DisjointUnionsOfSets",
    "EnumeratedSets",
    "FiniteOrdinalSets",
    "FinitePowerSets",
    "FiniteSets",
    "FinitelySupportedFunctionSets",
    "FixedCardinalitySubsetSets",
    "FunctionSets",
    "InfiniteSets",
    "NaturalNumberSets",
    "NN",
    "ObjectSetsOfDiscreteCategories",
    "PartiallyOrderedSets",
    "PowerSets",
    "PowerSets",
    "Set",
    "SetInclusion",
    "SetInjection",
    "SetSubcategoryMethods",
    "SetSurjection",
    "Sets",
    "TotallyOrderedSets",
    "UncountableSets",
    "finite_ordinal_set",
    "register_set_axioms",
]
