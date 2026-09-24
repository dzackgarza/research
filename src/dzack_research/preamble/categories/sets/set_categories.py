"""Owned Set categories, canonical index objects, and categorical constructions."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from itertools import count
from math import comb
from operator import index as integer_index
from typing import Any, Self, SupportsIndex, TypeVar

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.combinat.subset import Subsets as SageSubsets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown, UnknownClass
from sage.rings.integer_ring import ZZ as SageZZ
from sage.sets.disjoint_set import DisjointSet as SageDisjointSet
from sage.sets.set import Set as SageSet
from sage.structure.element import Element
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent

import dzack_research.preamble.categories.sets.cardinals as cardinals
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalIsomorphism,
    CategoricalMor,
    EpiCategoryConstruction,
    MonoCategoryConstruction,
    MorCategoryConstruction,
    _category_mor,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
)
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom

IndexT = TypeVar("IndexT")
SourcePointT = TypeVar("SourcePointT")
TargetPointT = TypeVar("TargetPointT")

for _axiom in ("Countable", "Uncountable"):
    if _axiom not in all_axioms:
        all_axioms.add(_axiom)


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

        def le(self, left, right) -> bool:
            r"""The order the enumeration transports from its ordinal: ``x <= y`` when ``x`` is ranked no later."""
            ranking = self.ranking_map()
            return ranking(left) <= ranking(right)

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
        # A finite ordinal is a finite totally ordered set, enumerated by
        # itself; it is the base case of the enumeration datum.
        from dzack_research.preamble.categories.sets.finite_ordered_sets import FiniteOrderedSets

        return [FiniteOrderedSets()]

    def _call_(self, size):
        r"""Construct the canonical finite ordinal of cardinality ``size``."""
        return _object_of(self, size=size)

    class ParentMethods:
        _derived_construction_parameters = frozenset({"index_set", "element_at", "index_of"})

        def __init__(self, size: int, **rest) -> None:
            self._size = int(size)
            assert self._size >= 0 and size == self._size, (
                f"the finite ordinal [n] = {{0, ..., n-1}} needs n a nonnegative integer, but n = {size!r}"
            )
            # The ordinal is its own index set, and its enumeration is the
            # identity: the point at position k is k.
            super().__init__(
                index_set=self,
                element_at=lambda position: NN(int(position)),
                index_of=lambda point: int(point) if point in self else None,
                contains=self.__contains__,
                **rest,
            )

        def order_type(self) -> cardinals.Ordinal:
            r"""The ordinal ``n`` this well-ordered set is isomorphic to: itself.

            The finite ordinal ``{0, ..., n-1}`` is the von Neumann ordinal
            ``n``, so its order type is the datum it was built from.  The
            cardinality of the set is the cardinality of that ordinal, which
            is how ``Sets`` answers it.
            """
            return cardinals.ordinal(self._size)

        def __iter__(self):
            return (NN(index) for index in range(self._size))

        def __getitem__(self, position):
            r"""Return the point at ``position`` without enumerating preceding points."""
            position = int(position)
            if position < 0 or position >= self._size:
                raise IndexError(
                    f"position {position} is out of range for {self}, which has {self._size} points"
                )
            return NN(position)

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""The identity: an ordinal already *is* the ordinal counting it."""

            def point_at(position):
                position = int(position)
                if position < 0 or position >= self._size:
                    raise IndexError(
                        f"position {position} is out of range for {self}, which has {self._size} points"
                    )
                return NN(position)

            def position_of(element):
                return int(self(element))

            return self._ranking_isomorphism(position_of, point_at)

        def __contains__(self, element) -> bool:
            r"""Whether ``element`` names a position ``0 <= k < n``.

            A position is a natural number -- the Python literal, an owned
            natural or a nonnegative owned integer, as ``NN`` admits them --
            or a Sage integer, which a preparsed session writes for a literal.
            """
            match element:
                case _ if element in NN:
                    return int(NN(element)) < self._size
                case _ if element in SageZZ:
                    return 0 <= int(SageZZ(element)) < self._size
                case _:
                    return False

        is_parent_of = __contains__

        def __call__(self, element):
            r"""Normalize a natural number to the point of this ordinal it names.

            This is the element constructor, the one boundary that admits
            foreign data, so it reads the position directly.  It cannot ask
            the ranking map: applying an arrow coerces its argument into the
            domain, and the domain is this parent.
            """
            if element not in self:
                raise ValueError(f"{element!r} is not an element of {self}")
            return NN(int(element))

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
        r"""\(\Delta[n]\) for an integer \(n\geq -1\), or \(\Delta[\aleph_0]=\mathbb N\).

        \(\Delta[-1]\) is the empty ordinal, the index set of an empty family.
        A finite cardinal \(n\) names \(\Delta[n]\) as an integer does.
        """
        match dimension:
            case _ if dimension in cardinals.Cardinalities():
                if dimension == cardinals.aleph0:
                    return NN
                assert dimension.is_finite(), (
                    f"the simplex Delta[n] is defined here for n finite or countably infinite, but n = {dimension}"
                )
                return finite_ordinal_set(dimension.finite_value() + 1)
            case _:
                assert dimension == int(dimension) and int(dimension) >= -1, (
                    f"the simplex Delta[n] needs n an integer >= -1 or a cardinal, but n = {dimension!r}"
                )
                return finite_ordinal_set(int(dimension) + 1)

    def __repr__(self) -> str:
        return "Δ"


class _Aleph:
    def __getitem__(self, index):
        return cardinals.aleph(index)

    def __repr__(self) -> str:
        return "ℵ"


class OwnedSetMorphism(SetMorphism):
    r"""A set map whose composition remains in the canonical owned Set Mor.

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
        # Equality is extensional within one Mor.  An identity-based hash of
        # the function would give equal maps different hashes; hashing only
        # the parent also works when points of either endpoint are unhashable.
        return hash(id(self.parent()))

    def is_identity(self) -> bool | UnknownClass:
        r"""Decide identity on a finite enumeration; retain unknown otherwise.

        The identity of a Mor object is the one arrow its ``identity()`` interns,
        so that arrow answers by identity of objects; any other arrow answers
        extensionally, which is the same three-valued equality as ``==``.
        """
        if self.domain() is not self.codomain():
            return False
        identity = self.parent().identity()
        if self is identity:
            return True
        return self == identity

    def image(self) -> Parent:
        r"""The represented image ``f(X)``, constructed at the set owner.

        Construction needs the map, not an algorithm enumerating its image.
        Finite images are enumerated by the image engine; for an infinite
        source it states the frontier when membership or cardinality is asked.
        """
        return Sets().image_set(self, self.domain())

    def is_injective(self) -> bool | UnknownClass:
        r"""Decide ``f(x) = f(y) => x = y`` by counting the image.

        Decided on a finite enumerated domain; ``Unknown`` otherwise, which
        is the hypothesis the answer needs and does not have.
        """
        domain = self.domain()
        if domain not in FiniteSets() or domain not in EnumeratedSets():
            return Unknown
        return self.image().cardinality() == domain.cardinality()

    def is_surjective(self) -> bool | UnknownClass:
        r"""Decide that every point of the codomain is a value.

        Decided on finite enumerated endpoints; ``Unknown`` otherwise.
        """
        domain = self.domain()
        codomain = self.codomain()
        if domain not in FiniteSets() or domain not in EnumeratedSets():
            return Unknown
        if codomain not in FiniteSets() or codomain not in EnumeratedSets():
            return Unknown
        image = self.image()
        return all(point in image for point in codomain)

    def inverse(self):
        r"""Return the inverse of a bijection between finite enumerated sets."""
        domain = self.domain()
        codomain = self.codomain()
        assert self.is_injective() is True and self.is_surjective() is True, (
            f"{self} has no inverse: it is not known to be a bijection {domain} -> {codomain} "
            "(injectivity and surjectivity are decided only between finite enumerated sets)"
        )
        absent = object()

        def preimage(target):
            source = next((source for source in domain if self(source) == target), absent)
            assert source is not absent, (
                f"{self} was decided to be a bijection {domain} -> {codomain}, but no point of {domain} "
                f"maps to {target}"
            )
            return source

        return Sets().Mor(codomain, domain)(preimage)

    def as_isomorphism(self):
        r"""Return this finite bijection as the corresponding arrow of ``core(Set)``."""
        return Sets().Core().Mor(self.domain(), self.codomain())(self, self.inverse())

    def __mul__(self, other):
        r"""Compose ``self ∘ other``.

        The right operand is arbitrary, which is Python's binary-operator
        protocol: like ``__eq__``, this decides about anything and answers
        ``NotImplemented`` for what is not a composable arrow.
        """
        if not isinstance(other, Morphism) or other.codomain() is not self.domain():
            return NotImplemented
        mor = Sets().Mor(other.domain(), self.codomain())
        if self.domain() is self.codomain() and self is self.parent().identity() and other.parent() is mor:
            return other
        if other.domain() is other.codomain() and other is other.parent().identity():
            return self
        return mor(lambda element: self(other(element)))


class SetMorCategory(CategoricalMor):
    r"""The owned category $\mathrm{Mor}_{\mathbf{Set}}(X, Y)$.

    Its objects are the functions $X \to Y$.  A set is a category -- the
    discrete one -- so this is a category like every other `Mor`, and not a
    special set-valued case: `ARC-07` has `Mor` return a category at every
    level.  Sage's ``Mor``, reached through ``CategoricalMor``, remains
    the runtime parent its ``SetMorphism`` elements require.
    """

    def __init__(
        self,
        mor_family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    def _element_constructor_(self, datum):
        r"""Admit an arrow: a set map between these endpoints, or a callable.

        The element constructor is the one boundary that reads foreign data,
        so it is where the datum's shape is inspected.
        """
        if isinstance(datum, Morphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError(
                    f"cannot view {datum} as a map {self.domain()} -> {self.codomain()}: it is a map "
                    f"{datum.domain()} -> {datum.codomain()}"
                )
            if datum.parent() is self:
                return datum
        if not callable(datum):
            raise TypeError(
                f"a map of sets {self.domain()} -> {self.codomain()} needs a function on points, but "
                f"{datum!r} is not callable"
            )
        return OwnedSetMorphism(self, datum)

    @cached_method
    def identity(self) -> OwnedSetMorphism:
        r"""The identity arrow, interned: ``is_identity`` reads it by identity."""
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity map exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        return OwnedSetMorphism(self, lambda element: element)

    def identity_at(self, obj: Parent) -> OwnedSetMorphism:
        return Sets().Mor(obj, obj).identity()

    def _repr_(self):
        return f"Mor_Set({self.domain()}, {self.codomain()})"


class SetMorCategoryConstruction(MorCategoryConstruction):
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

    _MorCategory = SetMorCategoryConstruction

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
        if source in self:
            return source
        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            finite_ordered_set,
        )

        if source in SageSets():
            if source not in SageSets().Finite():
                raise TypeError(
                    f"cannot use the Sage set {source} as a set of this session: it is infinite, and only finite "
                    "Sage sets convert directly"
                )
            return finite_ordered_set(tuple(source))
        return finite_ordered_set(tuple(SageSet(source)))

    def condition_set(self, universe, predicate):
        r"""Return the subset \(\{x\in X : P(x)\}\) of ``universe`` cut out by ``predicate``, with its inclusion.

        A subset of a finite enumerated set is the finite ordered set of its
        points in the order of \(X\), realized by the ordered filter engine;
        any other subset is realized by the condition-set engine, a set that
        is finite when \(X\) is.
        """
        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            _FilteredOrderedSet,
        )

        match universe:
            case _ if universe in FiniteSets() and universe in EnumeratedSets():
                return _FilteredOrderedSet(universe, predicate)
            case _:
                return _ConditionSet(universe, predicate)

    def image_set(self, map_, domain_subset, *, inverse=None):
        r"""Return the image \(f(A)\) of ``domain_subset`` under ``map_``.

        An inverse \(g\) on the image, \(g(f(a)) = a\), witnesses that \(f\) is
        injective on \(A\).  With it and an enumerated \(A\), the image is the
        ordered enumerated set indexed by \(A\) through \(f\), with \(g\) the
        inverse of that enumeration, built by ``OrderedEnumeratedSets`` or,
        for finite \(A\), ``FiniteOrderedSets``.  Any other image, including
        the image of a map that is not injective, is realized by the image
        engine.
        """
        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            _EnumeratedImageSet,
        )

        match domain_subset:
            case _ if inverse is not None and domain_subset in EnumeratedSets():
                return _EnumeratedImageSet(domain_subset, map_, inverse)
            case _:
                return _ImageSet(domain_subset, map_, image_inverse=inverse)

    def Mor(self, domain: Parent, codomain: Parent) -> SetMorCategory:
        if domain not in self or codomain not in self:
            raise TypeError(
                f"a map of sets needs a set as domain and codomain, but got {domain} and {codomain}"
            )
        return _set_mor_category(domain, codomain)

    def Subobjects(self, base_object: Parent) -> Category:
        r"""Return the monomorphism subcategory of the slice over ``base_object``.

        Stated on ``Set`` itself, where a subobject is its inclusion; a
        category of structured sets keeps the general subobject category.
        """
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            SetSubobjectCategory,
        )

        return SetSubobjectCategory(self, base_object)

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
            return CartesianProductsOfSets()(family)

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
                raise TypeError(
                    f"a product of sets needs every factor to be a set, but the factors are {family}"
                )
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
                raise ValueError(
                    f"an equalizer needs parallel maps f, g: X -> Y, but {left_morphism} is "
                    f"{left_morphism.domain()} -> {left_morphism.codomain()} and {right_morphism} is "
                    f"{right_morphism.domain()} -> {right_morphism.codomain()}"
                )
            source = left_morphism.domain()
            target = left_morphism.codomain()
            if source not in self or target not in self:
                raise TypeError(
                    f"an equalizer in the category of sets needs maps between sets, but {source} or {target} is not a set"
                )

            equalizer = self.condition_set(
                source,
                lambda element: left_morphism(element) == right_morphism(element),
            )
            inclusion = equalizer.inclusion()
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
            return CoproductsOfSets()(family)

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
                raise TypeError(
                    f"a coproduct of sets needs every factor to be a set, but the factors are {family}"
                )
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
                raise ValueError(
                    f"a coequalizer needs parallel maps f, g: X -> Y, but {left_morphism} is "
                    f"{left_morphism.domain()} -> {left_morphism.codomain()} and {right_morphism} is "
                    f"{right_morphism.domain()} -> {right_morphism.codomain()}"
                )
            source = left_morphism.domain()
            target = left_morphism.codomain()
            if source not in self or target not in self:
                raise TypeError(
                    f"a coequalizer in the category of sets needs maps between sets, but {source} or {target} is not a set"
                )
            assert (
                cardinals.cardinal(source.cardinality()).is_finite()
                and cardinals.cardinal(target.cardinality()).is_finite()
            ), (
                f"the coequalizer of {left_morphism} and {right_morphism} is computed here only between "
                f"finite sets, but {source} or {target} is not known to be finite"
            )

            # The coequalizer of finite sets is the quotient of the target by
            # the equivalence relation generated by ``f(x) ~ g(x)``.  Sage's
            # ``DisjointSet`` (sage/sets/disjoint_set.pyx) is the engine that
            # closes the relation; it works on the target's ranking positions
            # and nothing of it reaches the result (`OWN-06`).
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_set,
            )

            enumerated_target = finite_ordered_set(tuple(target))
            target_points = tuple(enumerated_target)
            target_ranking = enumerated_target.ranking_map()

            def position(value):
                return int(target_ranking(value))

            classes = SageDisjointSet(len(target_points))
            for point in source:
                classes.union(position(left_morphism(point)), position(right_morphism(point)))

            representatives = tuple(sorted(classes.root_to_elements_dict()))
            class_position = {
                representative: label for label, representative in enumerate(representatives)
            }

            quotient = Sets.Δ[len(representatives) - 1]
            projection = Sets().Mor(target, quotient)(
                lambda point: quotient(class_position[classes.find(position(point))])
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

        def Mors(self) -> Category:
            r"""A Mor object of any owned category is a set."""
            return Mors()

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
        def cardinality(self) -> cardinals.Cardinalities.ObjectType:
            r"""The cardinality ``|X|``, an object of ``Card``.

            Cardinality is total on sets (`CAT-01`), and this is its one
            owner: no set construction restates it.  It is an isomorphism
            invariant, so it is read off what the construction of ``X``
            determines, by placement:

            - the finite ordinal ``n`` has the cardinality of its order
              type ``n``;
            - a set with a chosen enumeration from an index set is in
              bijection with that index set;
            - ``|P(X)| = 2^|X|``, since ``P(X)`` is in bijection with the
              characteristic maps ``X -> 2``;
            - ``|Y^X| = |Y|^|X|``, the definition of cardinal exponentiation;
            - the ``k``-element subsets of ``X`` number ``binomial(|X|, k)``
              for finite ``X``, one for ``k = 0``, and ``|X|`` for infinite
              ``X`` and ``k >= 1``;
            - the finite subsets of ``X`` number ``2^|X|`` for finite ``X``
              and ``|X|`` for infinite ``X``;
            - ``|prod_i X_i| = prod_i |X_i|`` and ``|coprod_i X_i| =
              sum_i |X_i|``, the definitions of cardinal product and sum;
            - any other finite set is counted through its points, and any
              other countably infinite set has cardinality ``aleph_0``.

            An engine realizing sets whose construction determines a
            cardinality these cases do not reach -- the image of an injective
            map, the ``k``-selections from a set -- states that theorem with
            its own ``cardinality``.  A represented set outside all of these
            has a cardinality that no exact computation here reaches, and the
            assertion says so.
            """
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                OrderedEnumeratedSets,
            )

            match self:
                case _ if self in FiniteOrdinalSets():
                    return self.order_type().cardinality()
                case _ if self in OrderedEnumeratedSets():
                    return cardinals.cardinal(self.index_set().cardinality())
                case _ if self in PowerSets():
                    return cardinals.cardinal(2) ** cardinals.cardinal(self.base_set().cardinality())
                case _ if self in FunctionSets():
                    return cardinals.cardinal(self.base().cardinality()) ** cardinals.cardinal(
                        self.exponent().cardinality()
                    )
                case _ if self in FixedCardinalitySubsetSets() and self.subset_cardinality() == 0:
                    return cardinals.cardinal(1)
                case _ if self in FixedCardinalitySubsetSets() and cardinals.cardinal(self.source().cardinality()).is_finite():
                    return cardinals.cardinal(
                        comb(
                            cardinals.cardinal(self.source().cardinality()).finite_value(),
                            self.subset_cardinality(),
                        )
                    )
                case _ if self in FixedCardinalitySubsetSets():
                    return cardinals.cardinal(self.source().cardinality())
                case _ if self in FinitePowerSets() and cardinals.cardinal(self.source().cardinality()).is_finite():
                    return cardinals.cardinal(2) ** cardinals.cardinal(self.source().cardinality())
                case _ if self in FinitePowerSets():
                    return cardinals.cardinal(self.source().cardinality())
                case _ if self in CartesianProductsOfSets():
                    return cardinals.Cardinalities().indexed_product(
                        self.index_set(),
                        lambda index: cardinals.cardinal(self.factor(index).cardinality()),
                    )
                case _ if self in CoproductsOfSets():
                    return cardinals.Cardinalities().indexed_sum(
                        self.index_set(),
                        lambda index: cardinals.cardinal(self.cofactor(index).cardinality()),
                    )
                case _ if self in Sets().Finite():
                    return cardinals.cardinal(sum(1 for _point in self))
                case _:
                    assert self in Sets().Countable() and self in Sets().Infinite(), (
                        f"cannot compute the cardinality of {self}: it is not known to be finite or countably "
                        f"infinite, and no formula for it applies (it is in {self.category()})"
                    )
                    return cardinals.aleph0

        def finite_words(self):
            r"""All finite words in this alphabet, including the empty word."""
            return _finite_words(self, commutative=False)

        def finite_multisets(self):
            r"""All finite multisets in this alphabet, including the empty multiset."""
            return _finite_words(self, commutative=True)

        def counting_ordinal(self):
            r"""Return the represented ordinal that counts this set when it is countable."""
            size = cardinals.cardinal(self.cardinality())
            if size.is_finite():
                return finite_ordinal_set(size.finite_value())
            assert size.is_countably_infinite(), (
                f"{self} has cardinality {size}, which is not countable, so no ordinal here counts it"
            )
            return NN

        def Mor(
            self,
            codomain: Parent,
            category: Category | None = None,
        ) -> Category:
            if category is None:
                return Sets().Mor(self, codomain)
            return _category_mor(category, self, codomain)

        def condition_set(self, predicate) -> Parent:
            r"""Return the represented subset of ``self`` cut out by ``predicate``."""
            return Sets().condition_set(self, predicate)

        def image_set(self, map_, *, inverse=None) -> Parent:
            r"""Return the image of ``self`` under ``map_``, with ``inverse`` on the image when one is selected."""
            return Sets().image_set(map_, self, inverse=inverse)

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
            assert other in Sets(), (
                f"the product {self} x Y needs Y a set, but {other} is not in the category of sets"
            )
            factors = (self, other)
            return Sets().product(indexed_family(Sets.Δ[1], lambda index: factors[int(index)]))

        def coproduct_with(self, other: Parent) -> Parent:
            r"""Return $X \sqcup Y$, the coproduct asked of the objects."""
            assert other in Sets(), (
                f"the coproduct {self} + Y needs Y a set, but {other} is not in the category of sets"
            )
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
                raise ValueError(
                    f"the power X^n of {self} needs n a nonnegative integer, but n = {exponent!r}"
                )
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
            from dzack_research.preamble.categories.functors.g_sets import (
                TrivialGSetFunctor,
            )

            return TrivialGSetFunctor(group)

        def free_action(self, group: Parent) -> Functor:
            r"""``G x - : FinSet -> FinGSet_G``, the free ``G``-set on a set."""
            from dzack_research.preamble.categories.functors.g_sets import (
                FreeGSetFunctor,
            )

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
    r"""A set morphism whose injectivity is decided or construction-derived."""

    def _injectivity_derivation(self):
        return None

    def __init__(self, parent, function) -> None:
        OwnedSetMorphism.__init__(self, parent, function)
        decision = self._injectivity_derivation()
        if decision is None:
            decision = parent.arrow_set()(function).is_injective()
        if decision is False:
            raise ValueError(
                f"{function} is not injective as a map {parent.domain()} -> {parent.codomain()}"
            )
        if decision is not True:
            raise ValueError(
                f"cannot decide whether {function} is injective as a map {parent.domain()} -> {parent.codomain()}"
            )

    def is_injective(self) -> bool:
        return True

    def __mul__(self, other):
        r"""Compose; a composite of monomorphisms is placed as a monomorphism."""
        composite = super().__mul__(other)
        if composite is NotImplemented:
            return composite
        monomorphisms = Sets().Mono(other.domain(), self.codomain())
        if Sets().Mono(other.domain(), other.codomain()).accepts(other):
            return _CompositeSetInjection(monomorphisms, self, other)
        return composite


class _IdentitySetInjection(SetInjection):
    def __init__(self, parent) -> None:
        super().__init__(parent, lambda element: element)

    def _injectivity_derivation(self):
        return True


class _CompositeSetInjection(SetInjection):
    def __init__(self, parent, left, right) -> None:
        self._left = left
        self._right = right
        super().__init__(parent, lambda element: left(right(element)))

    def _injectivity_derivation(self):
        return True


class SetSurjection(OwnedSetMorphism):
    r"""A set morphism whose surjectivity is decided or construction-derived."""

    def _surjectivity_derivation(self):
        return None

    def __init__(self, parent, function) -> None:
        OwnedSetMorphism.__init__(self, parent, function)
        decision = self._surjectivity_derivation()
        if decision is None:
            decision = parent.arrow_set()(function).is_surjective()
        if decision is False:
            raise ValueError(
                f"{function} is not surjective as a map {parent.domain()} -> {parent.codomain()}"
            )
        if decision is not True:
            raise ValueError(
                f"cannot decide whether {function} is surjective as a map {parent.domain()} -> {parent.codomain()}"
            )

    def is_surjective(self) -> bool:
        return True

    def __mul__(self, other):
        r"""Compose; a composite of epimorphisms is placed as an epimorphism."""
        composite = super().__mul__(other)
        if composite is NotImplemented:
            return composite
        epimorphisms = Sets().Epi(other.domain(), self.codomain())
        if Sets().Epi(other.domain(), other.codomain()).accepts(other):
            return _CompositeSetSurjection(epimorphisms, self, other)
        return composite


class _IdentitySetSurjection(SetSurjection):
    def __init__(self, parent) -> None:
        super().__init__(parent, lambda element: element)

    def _surjectivity_derivation(self):
        return True


class _CompositeSetSurjection(SetSurjection):
    def __init__(self, parent, left, right) -> None:
        self._left = left
        self._right = right
        super().__init__(parent, lambda element: left(right(element)))

    def _surjectivity_derivation(self):
        return True


class SetInjectionMor(SetMorCategory):
    r"""The declared injections between two sets."""

    def _element_constructor_(self, datum):
        r"""Admit an injective set map, or a callable declared injective."""
        if isinstance(datum, Morphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError(
                    f"cannot view {datum} as an injection {self.domain()} -> {self.codomain()}: it is a map "
                    f"{datum.domain()} -> {datum.codomain()}"
                )
            if datum.parent() is self:
                return datum
            if self.arrow_set()(datum).is_injective() is not True:
                raise ValueError(
                    f"{datum} is not known to be injective, so it is not an injection {self.domain()} -> {self.codomain()}"
                )
            return SetInjection(self, datum)
        if not callable(datum):
            raise TypeError(
                f"an injection {self.domain()} -> {self.codomain()} needs a function on points, but "
                f"{datum!r} is not callable"
            )
        return SetInjection(self, datum)

    def arrow_set(self):
        return Sets().Mor(self.domain(), self.codomain())

    underlying_mor = arrow_set

    def accepts(self, arrow):
        r"""Membership: an arrow of the Mor object decided injective."""
        return arrow in self.arrow_set() and self.arrow_set()(arrow).is_injective() is True

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity map exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        return _IdentitySetInjection(self)

    def super_categories(self):
        r"""An injection ``X -> Y`` is a map ``X -> Y``: ``Mono_Set(X, Y)`` is a full subcategory of ``Mor_Set(X, Y)``.

        That is the only inclusion the objects state.  A monomorphism of a
        subcategory need not be a monomorphism of a category containing it,
        so no monomorphism family of a supercategory of ``Set`` is declared.
        """
        return [Sets().Mor(self.domain_object(), self.codomain_object())]

    def _repr_(self):
        return f"Mono_Set({self.domain()}, {self.codomain()})"


class SetSurjectionMor(SetMorCategory):
    r"""The declared surjections between two sets."""

    def _element_constructor_(self, datum):
        r"""Admit a surjective set map, or a callable declared surjective."""
        if isinstance(datum, Morphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError(
                    f"cannot view {datum} as a surjection {self.domain()} -> {self.codomain()}: it is a map "
                    f"{datum.domain()} -> {datum.codomain()}"
                )
            if datum.parent() is self:
                return datum
            if self.arrow_set()(datum).is_surjective() is not True:
                raise ValueError(
                    f"{datum} is not known to be surjective, so it is not a surjection {self.domain()} -> {self.codomain()}"
                )
            return SetSurjection(self, datum)
        if not callable(datum):
            raise TypeError(
                f"a surjection {self.domain()} -> {self.codomain()} needs a function on points, but "
                f"{datum!r} is not callable"
            )
        return SetSurjection(self, datum)

    def arrow_set(self):
        return Sets().Mor(self.domain(), self.codomain())

    underlying_mor = arrow_set

    def accepts(self, arrow):
        r"""Membership: an arrow of the Mor object decided surjective."""
        return arrow in self.arrow_set() and self.arrow_set()(arrow).is_surjective() is True

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity map exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        return _IdentitySetSurjection(self)

    def super_categories(self):
        r"""A surjection ``X -> Y`` is a map ``X -> Y``: ``Epi_Set(X, Y)`` is a full subcategory of ``Mor_Set(X, Y)``.

        That is the only inclusion the objects state.  An epimorphism of a
        subcategory need not be an epimorphism of a category containing it,
        so no epimorphism family of a supercategory of ``Set`` is declared.
        """
        return [Sets().Mor(self.domain_object(), self.codomain_object())]

    def _repr_(self):
        return f"Epi_Set({self.domain()}, {self.codomain()})"


class SetMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The declared monomorphisms of sets."""

    def fixed_category_class(self):
        return SetInjectionMor

    def accepts(self, arrow):
        r"""A monomorphism of sets is exactly an injective set map."""
        if arrow.domain() not in Sets() or arrow.codomain() not in Sets():
            return False
        return self.Of(arrow.domain(), arrow.codomain()).accepts(arrow)


class SetEpiCategoryConstruction(EpiCategoryConstruction):
    r"""The declared epimorphisms of sets."""

    def fixed_category_class(self):
        return SetSurjectionMor

    def accepts(self, arrow):
        r"""An epimorphism of sets is exactly a surjective set map."""
        if arrow.domain() not in Sets() or arrow.codomain() not in Sets():
            return False
        return self.Of(arrow.domain(), arrow.codomain()).accepts(arrow)


Sets._MonoCategory = SetMonoCategoryConstruction
Sets._EpiCategory = SetEpiCategoryConstruction


class SetInclusion(OwnedSetMorphism):
    r"""A represented subobject inclusion \(A\hookrightarrow X\).

    A subobject of \(X\) is the pair \((A, i\colon A\hookrightarrow X)\): the
    set \(A\) is the domain, \(X\) the codomain, and every question about
    the subset -- membership, enumeration, cardinality -- is asked of the
    set \(A\).  The characteristic morphism \(\chi_A\colon X\to\Delta[1]\)
    is derived from membership in \(A\); nothing is stored beside the two
    endpoints.
    """

    def __init__(self, domain: Parent, codomain: Parent) -> None:
        parent = Sets().Mor(domain, codomain)
        super().__init__(parent, lambda member: codomain(member))

    def inclusion(self) -> Self:
        return self

    def __call__(self, member, *args, **kwargs):
        r"""Apply the inclusion using the codomain's owned ingress."""
        point = self.codomain()(member)
        match point in self:
            case True:
                return point
            case _:
                raise ValueError(
                    f"{member!r} is not in the subset {self.domain()} of {self.codomain()}"
                )

    def is_injective(self) -> bool:
        return True

    def factor_through(self, target_inclusion: SetInclusion) -> SetMorphism:
        r"""Return the canonical map of subset objects when this subset is contained."""
        factor = self.factor_through_or_none(target_inclusion)
        if factor is None:
            raise ValueError(
                f"the subset {self.domain()} of {self.codomain()} is not contained in the subset "
                f"{target_inclusion.domain()}"
            )
        return factor

    def factor_through_or_none(self, target_inclusion: SetInclusion):
        r"""Return the canonical subset factor, or None when containment fails."""
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError(
                f"cannot compare the subsets {self.domain()} and {target_inclusion.domain()}: they are subsets "
                f"of different sets {self.codomain()} and {target_inclusion.codomain()}"
            )
        if not self <= target_inclusion:
            return None
        return Sets().Mor(self.domain(), target_inclusion.domain())(lambda member: target_inclusion.domain()(self(member)))

    def underlying_set(self) -> Parent:
        r"""The set \(A\), which is the domain of the inclusion."""
        return self.domain()

    def characteristic_morphism(self) -> SetMorphism:
        r"""The characteristic map \(\chi_A\colon X\to\Delta[1]\), read off membership."""
        truth_values = Sets.Δ[1]
        return Sets().Mor(self.codomain(), truth_values)(
            lambda member: truth_values(int(member in self))
        )

    def __contains__(self, member) -> bool:
        r"""Whether ``member`` names a point of \(X\) lying in \(A\)."""
        return member in self.codomain() and self.codomain()(member) in self.domain()

    def __iter__(self):
        return iter(self.domain())

    def cardinality(self) -> cardinals.Cardinalities.ObjectType:
        r"""The cardinality of the subset \(A\subseteq X\) this inclusion presents as an element of \(P(X)\).

        An element of the power set is a subset, a set with a cardinality;
        here it is presented by its inclusion, whose domain is \(A\).
        """
        return cardinals.cardinal(self.domain().cardinality())

    def _check_common_base(self, other) -> None:
        if self.codomain() is not other.codomain():
            raise ValueError(
                f"cannot combine the subsets {self.domain()} and {other.domain()}: they are subsets of different "
                f"sets {self.codomain()} and {other.codomain()}"
            )

    def __le__(self, other) -> bool:
        self._check_common_base(other)
        domain = self.domain()
        if domain in FiniteSets() and domain in EnumeratedSets():
            return all(member in other for member in domain)
        base = self.codomain()
        assert base in FiniteSets() and base in EnumeratedSets(), (
            f"cannot decide whether {domain} is contained in {other.domain()}: containment is decided here "
            f"only when {domain} or {base} is finite and enumerated"
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

    def __eq__(self, other) -> bool | UnknownClass:
        r"""Two subsets of \(X\) are equal when they have the same members.

        Decided when the base is finite enumerated, or when both subsets are
        finite enumerated; ``Unknown`` otherwise.
        """
        if self is other:
            return True
        if other not in self.codomain().power_set():
            return False
        other = self.codomain().power_set()(other)
        base = self.codomain()
        if base in FiniteSets() and base in EnumeratedSets():
            return all((member in self) == (member in other) for member in base)
        left, right = self.domain(), other.domain()
        if all(side in FiniteSets() and side in EnumeratedSets() for side in (left, right)):
            return left.cardinality() == right.cardinality() and all(member in other for member in left)
        return Unknown

    def __ne__(self, other) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

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
            assert base_set in Sets(), (
                f"the power set P(X) needs X a set, but {base_set} is not in the category of sets"
            )
            self._base_set = base_set
            super().__init__(**rest)

        def base_set(self) -> Parent:
            return self._base_set

        def truth_values(self) -> Parent:
            return Sets.Δ[1]

        def characteristic_mor(self) -> SetMorCategory:
            return Sets().Mor(self.base_set(), self.truth_values())

        def from_predicate(
            self,
            predicate: Callable[[SourcePointT], bool],
        ):
            r"""The subset \(\{x\in X : P(x)\}\) with its inclusion."""
            inclusion = self.base_set().condition_set(predicate).inclusion()
            return Sets().Subobjects(self.base_set())(inclusion)

        def from_characteristic_morphism(
            self,
            characteristic_morphism: SetMorphism,
        ):
            r"""The subset classified by \(\chi\colon X\to\Delta[1]\): where \(\chi=1\)."""
            if characteristic_morphism.parent() is not self.characteristic_mor():
                raise ValueError(
                    f"{characteristic_morphism} is not a characteristic map X -> Delta[1] of a subset of "
                    f"{self.base_set()}: it lies in {characteristic_morphism.parent()}"
                )
            truth = self.truth_values()(1)
            return self.from_predicate(lambda member: characteristic_morphism(member) == truth)

        def _from_finite_members(self, members):
            r"""The finite subset on the stated members, as a finite ordered set with its inclusion."""
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_set,
            )

            base = self.base_set()
            normalized = []
            for member in members:
                if member not in base:
                    raise ValueError(
                        f"{member!r} is not an element of {base}, so it cannot be a member of a subset of {base}"
                    )
                point = base(member)
                if point not in normalized:
                    normalized.append(point)
            inclusion = SetInclusion(finite_ordered_set(tuple(normalized)), base)
            return Sets().Subobjects(base)(inclusion)

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, candidate):
            r"""Admit a subset: an inclusion into \(X\), \(X\) itself, or finitely many members."""
            subobjects = Sets().Subobjects(self.base_set())
            if candidate in subobjects:
                return candidate
            if isinstance(candidate, SetInclusion):
                if candidate.codomain() is not self.base_set():
                    raise ValueError(
                        f"{candidate} is a subset of {candidate.codomain()}, not of {self.base_set()}"
                    )
                return subobjects(candidate)
            if candidate is self.base_set():
                return self.from_predicate(lambda _member: True)
            if candidate in Sets():
                assert candidate in FiniteSets() and candidate in EnumeratedSets(), (
                    f"cannot read {candidate} as a subset of {self.base_set()}: a set is read as a subset here only "
                    "through its elements, which needs it finite and enumerated"
                )
                return self._from_finite_members(candidate)
            if isinstance(candidate, Iterable):
                return self._from_finite_members(candidate)
            raise TypeError(f"{candidate!r} does not present a subset of {self.base_set()}")

        def __contains__(self, candidate) -> bool:
            r"""Whether ``candidate`` is a subset of \(X\): \(A\in P(X)\) exactly when \(A\subseteq X\).

            A subset is \(X\) itself, a set all of whose points lie in \(X\)
            (decided here for a finite enumerated set), or a subobject
            \(A\hookrightarrow X\), which is an arrow of ``Set`` rather than a
            set; reading that presentation off the arbitrary ``candidate`` is
            this method's whole job.  Finitely many points are data for the
            element constructor, not a subset: ``P(X)((x, y))`` builds one.
            """
            base = self.base_set()
            if candidate in Sets().Subobjects(base):
                return True
            match candidate:
                case _ if candidate is base:
                    return True
                case _ if candidate in Sets():
                    return (
                        candidate in FiniteSets()
                        and candidate in EnumeratedSets()
                        and all(point in base for point in candidate)
                    )
                case _ if isinstance(candidate, SetInclusion):
                    return candidate.codomain() is base
                case _:
                    return False

        def top(self):
            return self(self.base_set())

        def bottom(self):
            return self(())

        def inverse_image_morphism(self, morphism: SetMorphism) -> SetMorphism:
            if morphism.codomain() is not self.base_set():
                raise ValueError(
                    f"the inverse image f^-1 on P({self.base_set()}) needs f to end at {self.base_set()}, but "
                    f"{morphism} ends at {morphism.codomain()}"
                )
            target = morphism.domain().power_set()
            return Sets().Mor(self, target)(lambda subset: target.from_predicate(lambda member: morphism(member) in subset))

        def direct_image_morphism(self, morphism: SetMorphism) -> SetMorphism:
            r"""Direct image \(A\mapsto f(A)\) on subsets, as a set map \(P(X)\to P(Y)\)."""
            if morphism.domain() is not self.base_set():
                raise ValueError(
                    f"the direct image f_* on P({self.base_set()}) needs f to start at {self.base_set()}, but "
                    f"{morphism} starts at {morphism.domain()}"
                )
            target = morphism.codomain().power_set()

            def direct_image(subset):
                inclusion = SetInclusion(subset.underlying_set().image_set(morphism), morphism.codomain())
                return Sets().Subobjects(morphism.codomain())(inclusion)

            return Sets().Mor(self, target)(direct_image)

        def __iter__(self):
            r"""Enumerate the subsets of a finite enumerated base.

            Sage's ``Subsets`` (sage/combinat/subset.py) is the engine that
            enumerates them; each subset it yields is read back through this
            power set's element constructor (`OWN-06`).
            """
            base = self.base_set()
            assert base in FiniteSets() and base in EnumeratedSets(), (
                f"cannot list the subsets of {base}: the power set is enumerated here only for a finite "
                "enumerated set"
            )
            return (self(subset) for subset in SageSubsets(base))

        def cardinality_comparison(self) -> cardinals.CardinalityMorphism:
            size = self.cardinality()
            return cardinals.Cardinalities().Mor(size, size).identity()

        def _repr_(self) -> str:
            return f"Power set of {self.base_set()}"


@cached_function
def _power_set(base_set: Parent) -> Parent:
    return PowerSets()(base_set)


def _function_set_of(codomain, exponent):
    r"""Build \(Y^X\) in the category its exponent decides.

    Over a finite exponent every function is finitely supported, whatever
    base point of \(Y\) support is measured against, and over an infinite one
    that is exactly what fails.  That is a fact of the datum, so the object
    is built in the finer category rather than refined into it afterwards.
    """
    match exponent:
        case _ if exponent in FiniteSets():
            return _object_of(FinitelySupportedFunctionSets(), codomain=codomain, exponent=exponent)
        case _:
            return _object_of(FunctionSets(), codomain=codomain, exponent=exponent)


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
            assert codomain in Sets() and exponent in Sets(), (
                f"the exponential Y^X needs X and Y sets, but got X = {exponent} and Y = {codomain}"
            )
            self._codomain = codomain
            self._exponent = exponent
            super().__init__(**rest)

        def base(self) -> Parent:
            return self._codomain

        def exponent(self) -> Parent:
            return self._exponent

        def mor(self) -> SetMorCategory:
            return Sets().Mor(self.exponent(), self.base())

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, definition):
            mor = self.mor()
            if definition in mor:
                return definition
            return mor(definition)

        def __contains__(self, function) -> bool:
            return function in self.mor()

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
            assert self._subset_cardinality >= 0, (
                f"the set of k-element subsets of {source} needs k >= 0, but k = {subset_cardinality}"
            )
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
            if subset.domain().cardinality() != cardinals.cardinal(self.subset_cardinality()):
                raise ValueError(
                    f"{subset.domain()} is not in {self}: it has cardinality {subset.domain().cardinality()}, "
                    f"not {self.subset_cardinality()}"
                )
            return subset

        def __contains__(self, candidate) -> bool:
            if candidate not in self.power_set():
                return False
            return self.power_set()(candidate).domain().cardinality() == cardinals.cardinal(self.subset_cardinality())

        def __iter__(self):
            r"""Enumerate the ``k``-subsets of a finite enumerated source.

            Sage's ``Subsets`` (sage/combinat/subset.py) is the engine that
            enumerates them; each is read back through this object's element
            constructor (`OWN-06`).
            """
            source = self.source()
            assert source in FiniteSets() and source in EnumeratedSets(), (
                f"cannot list the {self.subset_cardinality()}-element subsets of {source}: they are enumerated "
                "here only for a finite enumerated set"
            )
            return (self(tuple(subset)) for subset in SageSubsets(source, self.subset_cardinality()))

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
            if not subset.domain().cardinality().is_finite():
                raise ValueError(f"{subset.domain()} is not in {self}: it is not finite")
            return subset

        def __contains__(self, candidate) -> bool:
            if candidate not in self.power_set():
                return False
            return self.power_set()(candidate).domain().cardinality().is_finite()

        def __iter__(self):
            r"""Enumerate the subsets of a finite enumerated source, through Sage's ``Subsets`` (`OWN-06`)."""
            source = self.source()
            assert source in FiniteSets() and source in EnumeratedSets(), (
                f"cannot list the finite subsets of {source}: they are enumerated here only for a finite "
                "enumerated set"
            )
            return (self(tuple(subset)) for subset in SageSubsets(source))

        def _repr_(self) -> str:
            return f"Finite subsets of {self.source()}"


@cached_function
def _finite_subsets(source: Parent) -> Parent:
    return FinitePowerSets()(source)


class _ConditionSet(Sets().ObjectType):
    r"""The subset \(\{x\in X : P(x)\}\) of a set \(X\) cut out by a predicate \(P\).

    An engine realizing objects of ``Sets()``: the datum is the set \(X\) and
    the predicate \(P\) on its points, and the object is the set of points
    satisfying \(P\), whose inclusion into \(X\) is the subobject it is.  A
    subset of a finite set is finite, which places it.  ``Sets().condition_set``
    is the construction route; a subset of a finite enumerated set is built
    there by the ordered filter engine instead.
    """

    def __init__(self, universe: Parent, predicate: Callable[[SourcePointT], bool]) -> None:
        assert universe in Sets(), (
            f"a subset cut out by a predicate needs a set to cut it from, but {universe} is not in the "
            "category of sets"
        )
        self._universe = universe
        self._predicate = predicate
        match universe:
            case _ if universe in FiniteSets():
                placement = FiniteSets()
            case _:
                placement = Sets()
        super().__init__(category=placement, facade=True)

    def universe(self) -> Parent:
        r"""The set \(X\) this subset is cut out of."""
        return self._universe

    def predicate(self) -> Callable[[SourcePointT], bool]:
        r"""The predicate \(P\) cutting this subset out of \(X\)."""
        return self._predicate

    @cached_method
    def inclusion(self) -> SetInclusion:
        r"""The inclusion \(\{x\in X : P(x)\}\hookrightarrow X\)."""
        return SetInclusion(self, self.universe())

    def __contains__(self, element) -> bool:
        r"""Whether ``element`` is a point of \(X\) satisfying \(P\)."""
        universe = self.universe()
        return element in universe and bool(self.predicate()(universe(element)))

    is_parent_of = __contains__

    def _element_constructor_(self, element):
        if element not in self:
            raise ValueError(f"{element!r} is not in {self}")
        return self.universe()(element)

    def __iter__(self):
        universe = self.universe()
        assert universe in FiniteSets() or universe in EnumeratedSets(), (
            f"cannot list the elements of {self}: the set {universe} it is cut out of is neither finite "
            "nor enumerated"
        )
        return (point for point in universe if self.predicate()(point))

    def _repr_(self) -> str:
        return f"Subset of {self.universe()} cut out by {self.predicate()}"


class _ImageSet(Sets().ObjectType):
    r"""The image \(f(A)\) of a set \(A\) under a map \(f\).

    An engine realizing objects of ``Sets()``: the datum is the set \(A\), the
    map \(f\) on it, and optionally an inverse \(g\) on the image with
    \(g(f(a)) = a\), which witnesses that \(f\) is injective on \(A\).  A point
    of the image is a value \(f(a)\).  The image of a finite set is finite,
    which places it.  ``Sets().image_set`` is the construction route; an image
    with an inverse over an enumerated \(A\) is built there as an ordered
    enumerated set instead.
    """

    def __init__(
        self,
        source: Parent,
        image_map: Callable[[SourcePointT], TargetPointT],
        *,
        image_inverse: Callable[[TargetPointT], SourcePointT] | None = None,
    ) -> None:
        assert source in Sets(), (
            f"the image of a map needs a set as domain, but {source} is not in the category of sets"
        )
        self._source = source
        self._image_map = image_map
        self._image_inverse = image_inverse
        match source:
            case _ if source in FiniteSets():
                placement = FiniteSets()
            case _:
                placement = Sets()
        super().__init__(category=placement, facade=True)

    def source_set(self) -> Parent:
        r"""The set \(A\) of which this set is the image \(f(A)\)."""
        return self._source

    def image_map(self) -> Callable[[SourcePointT], TargetPointT]:
        r"""The map \(f\) of which this set is the image \(f(A)\)."""
        return self._image_map

    def inverse_on_image(self) -> Callable[[TargetPointT], SourcePointT]:
        r"""The selected inverse \(g\) of \(f\) on the image."""
        assert self._image_inverse is not None, (
            f"{self} has no inverse map on the image: none was given when the image was constructed"
        )
        return self._image_inverse

    def is_injective_image(self) -> bool | UnknownClass:
        r"""Whether \(f\) is injective on \(A\).

        ``True`` when an inverse on the image was selected; decided by
        counting the distinct values over a finite source; ``Unknown``
        otherwise.
        """
        match self.source_set():
            case _ if self._image_inverse is not None:
                return True
            case source if source in FiniteSets():
                return cardinals.cardinal(sum(1 for _value in self._distinct_values())) == cardinals.cardinal(
                    source.cardinality()
                )
            case _:
                return Unknown

    def cardinality(self) -> cardinals.Cardinalities.ObjectType:
        r"""The cardinality of \(f(A)\).

        An inverse on the image makes \(f\) a bijection \(A\to f(A)\), so
        \(|f(A)| = |A|\); without one, the image of a finite set is a finite
        set, counted through its points by the set level.
        """
        match self.source_set():
            case source if self._image_inverse is not None:
                return cardinals.cardinal(source.cardinality())
            case source:
                assert source in FiniteSets(), (
                    f"cannot compute the cardinality of the image {self}: its source {source} is not known to be "
                    "finite and no inverse on the image was given"
                )
                return super().cardinality()

    @cached_method
    def _distinct_values(self):
        r"""The values of \(f\) over a finite source, each once, in the order of the source."""
        return tuple(dict.fromkeys(self.image_map()(point) for point in self.source_set()))

    @cached_method
    def _finite_image(self):
        r"""Sage's enumerated set on the values: membership by hashing, not by search."""
        return SageSet(self._distinct_values())

    def __iter__(self):
        assert self.source_set() in FiniteSets(), (
            f"cannot list the elements of the image {self}: its source {self.source_set()} is not known "
            "to be finite; for an infinite image use Sets().image_set with an inverse on the image"
        )
        return iter(self._distinct_values())

    def __contains__(self, element) -> bool:
        r"""Whether ``element`` is a value \(f(a)\) for a point \(a\) of the source."""
        source = self.source_set()
        match source:
            case _ if source in FiniteSets():
                return element in self._finite_image()
            case _ if self._image_inverse is not None:
                preimage = self._image_inverse(element)
                return preimage in source and self.image_map()(source(preimage)) == element
            case _:
                assert self._image_inverse is not None, (
                    f"cannot decide whether {element!r} lies in the image {self}: the source is infinite and no "
                    "inverse on the image was given"
                )

    is_parent_of = __contains__

    def _element_constructor_(self, element):
        if element not in self:
            raise ValueError(f"{element!r} is not in {self}")
        return element

    def _repr_(self) -> str:
        match self.source_set():
            case source if source in FiniteSets():
                return "{" + ", ".join(repr(value) for value in self) + "}"
            case source:
                return f"Image of {source} under {self.image_map()}"


@cached_function(key=lambda family: id(family))
def _cartesian_product_of(family: IndexedFamily) -> Parent:
    r"""Build the product of the family of sets ``family`` in the category its factors decide.

    Finiteness is a fact about the index set and the factors; the product is
    built in the category it always belongs to, joined with the enumerated,
    finite or countable placement its factors establish.
    """
    index_set = family.index_set()
    placements = [CartesianProductsOfSets()]
    if index_set in FiniteSets() and index_set in EnumeratedSets():
        from dzack_research.preamble.categories.group.magmas import AdditiveMonoids

        if all(family(index) in AdditiveMonoids() for index in index_set):
            placements.append(CartesianProductsOfAdditiveMonoids())
        factor_cardinalities = tuple(
            cardinals.cardinal(family(index).cardinality()) for index in index_set
        )
        product_cardinality = cardinals.Cardinalities().product(*factor_cardinalities)
        if product_cardinality.is_finite():
            if all(
                family(index) in FiniteSets() and family(index) in EnumeratedSets()
                for index in index_set
            ):
                placements.insert(0, FiniteEnumeratedCartesianProductsOfSets())
            else:
                placements.append(FiniteSets())
        elif product_cardinality.is_countably_infinite():
            placements.append(Sets().Countable().Infinite())
    return _object_of(Category.join(placements), family=family)


class CartesianProductsOfSets(OwnedCategory):
    r"""Dependent products of families of sets.

    The defining datum is the family \((X_i)_{i\in I}\), which carries its
    index set; the object is \(\prod_{i\in I}X_i\), a point of which is a
    section \(i\mapsto x_i\in X_i\).

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
            # A point of a product has fixed components; each is read into its
            # factor once and kept, not re-validated on every hash or comparison.
            self._resolved_components = {}

        def component(self, index: IndexT) -> SourcePointT:
            normalized = self.parent().index_set()(index)
            resolved = self._resolved_components.get(normalized)
            if resolved is not None:
                return resolved
            if self._positional_components is not None:
                position = int(self.parent().index_set().ranking_map()(normalized))
                resolved = self._positional_components[position]
            else:
                resolved = self.parent().factor(normalized)(self._components(normalized))
            self._resolved_components[normalized] = resolved
            return resolved

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

    def _call_(self, family: IndexedFamily) -> Parent:
        r"""Construct the dependent product of the family of sets ``family``."""
        return _cartesian_product_of(family)

    class ParentMethods:
        def __init__(self, family: IndexedFamily, **rest) -> None:
            assert family.index_set() in Sets(), (
                f"a product of sets needs the index of the family to be a set, but {family.index_set()} is not "
                "in the category of sets"
            )
            self._family = family
            super().__init__(**rest)

        def index_set(self) -> Parent:
            return self.family().index_set()

        def family(self) -> IndexedFamily[IndexT, Parent]:
            return self._family

        def has_finite_index_set(self) -> bool:
            return self.index_set() in FiniteSets()

        def factor(self, index: IndexT) -> Parent:
            normalized = self.index_set()(index)
            factor = self.family()(normalized)
            assert factor in Sets(), (
                f"the factor at index {normalized} of {self} is {factor}, which is not a set"
            )
            return factor

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, components):
            r"""Admit a section: one of this product, a callable, or positional components."""
            if isinstance(components, self.category().ElementType):
                if components.parent() is self:
                    return components
                raise ValueError(
                    f"{components} is an element of {components.parent()}, not of the product {self}"
                )
            if callable(components):
                return self.element_class(self, components)
            if not self.has_finite_index_set() or self.index_set() not in EnumeratedSets():
                raise TypeError(
                    f"cannot read {components!r} as an element of {self} component by component: the index set "
                    f"{self.index_set()} is not finite and enumerated; give a function from indices to components"
                )
            values = tuple(components)
            indices = tuple(self.index_set())
            if len(values) != len(indices):
                raise ValueError(
                    f"an element of {self} needs one component for each of the {len(indices)} indices, but "
                    f"{len(values)} were given"
                )
            positional = tuple(
                self.factor(index)(value) for index, value in zip(indices, values, strict=True)
            )
            ranking = self.index_set().ranking_map()
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

        def __iter__(self):
            assert self.has_finite_index_set(), (
                f"cannot list the elements of {self}: its index set {self.index_set()} is infinite"
            )

            ranking = self.index_set().ranking_map()
            index_count = int(cardinals.cardinal(self.index_set().cardinality()).finite_value())
            factors = tuple(
                self.factor(ranking.inverse()(position))
                for position in range(index_count)
            )
            factor_cardinalities = tuple(
                cardinals.cardinal(factor.cardinality()) for factor in factors
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

            assert all(
                factor in EnumeratedSets() and size.is_countable()
                for factor, size in zip(factors, factor_cardinalities, strict=True)
            ), (
                f"cannot list the elements of {self}: the product is enumerated here only when every factor "
                "is enumerated and countable"
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
        f"the mixed-radix enumeration of {product} needs a finite index set, but "
        f"{product.index_set()} is not known to be finite"
    )
    assert product.index_set() in EnumeratedSets(), (
        f"the mixed-radix enumeration of {product} needs an enumerated index set, but "
        f"{product.index_set()} is not enumerated"
    )
    index_count = int(cardinals.cardinal(product.index_set().cardinality()).finite_value())
    index_ranking = product.index_set().ranking_map()
    index_at = index_ranking.inverse()
    for index in product.index_set():
        factor = product.factor(index)
        assert factor in EnumeratedSets(), (
            f"the mixed-radix enumeration of {product} needs every factor enumerated, but the factor "
            f"{factor} at {index} is not"
        )
        assert cardinals.cardinal(factor.cardinality()).is_finite(), (
            f"the mixed-radix enumeration of {product} needs every factor finite, but the factor "
            f"{factor} at {index} is infinite"
        )
    total_size = int(cardinals.cardinal(product.cardinality()).finite_value())

    def point_at(position):
        position = int(position)
        if position < 0 or position >= total_size:
            raise IndexError(
                f"position {position} is out of range for {product}, which has {total_size} elements"
            )
        assignment = {}
        quotient = position
        for offset in range(index_count - 1, -1, -1):
            index = index_at(offset)
            factor = product.factor(index)
            radix = int(cardinals.cardinal(factor.cardinality()).finite_value())
            quotient, digit = divmod(quotient, radix)
            assignment[offset] = factor.ranking_map().inverse()(digit)
        return product(tuple(assignment[offset] for offset in range(index_count)))

    def position_of(section):
        section = product(section)
        position = 0
        for index in product.index_set():
            factor = product.factor(index)
            radix = int(cardinals.cardinal(factor.cardinality()).finite_value())
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

    def _call_(self, family: IndexedFamily) -> Parent:
        r"""Construct the dependent coproduct of the family of sets ``family``."""
        return _coproduct_of_indexed_family(family)

    class ParentMethods:
        def __init__(self, family: IndexedFamily, **rest) -> None:
            assert family.index_set() in Sets(), (
                f"a coproduct of sets needs the index of the family to be a set, but {family.index_set()} is "
                "not in the category of sets"
            )
            self._family = family
            super().__init__(**rest)

        def index_set(self) -> Parent:
            return self.family().index_set()

        def family(self) -> IndexedFamily[IndexT, Parent]:
            return self._family

        def cofactor(self, index: IndexT) -> Parent:
            normalized = self.index_set()(index)
            cofactor = self.family()(normalized)
            assert cofactor in Sets(), (
                f"the cofactor at index {normalized} of {self} is {cofactor}, which is not a set"
            )
            return cofactor

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, datum, value=None):
            if isinstance(datum, self.category().ElementType):
                if datum.parent() is self:
                    return datum
                raise ValueError(
                    f"{datum} is an element of {datum.parent()}, not of the coproduct {self}"
                )
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

        def __contains__(self, element) -> bool:
            return element_parent(element) is self

        is_parent_of = __contains__

        def _repr_(self) -> str:
            return f"Coproduct of the family over {self.index_set()}"

    def an_object(self) -> Parent:
        r"""The disjoint union of the ordinal 2 with itself."""
        return Sets().coproduct((finite_ordinal_set(2), finite_ordinal_set(2)))

    def super_categories(self):
        return [Sets()]


class EnumeratedCoproductsOfSets(OwnedCategory):
    r"""Coproducts of finitely many enumerated sets over an enumerated index, ranked by layer.

    The \(k\)-th layer holds the \(k\)-th point of every summand that has one,
    in the order of the index set; a countably indexed family is
    diagonalized instead.  A coproduct of arbitrary sets has no such
    enumeration and stays in :class:`CoproductsOfSets`.
    """

    def super_categories(self):
        return [CoproductsOfSets(), EnumeratedSets()]

    class ParentMethods:
        def _finite_index_count(self):
            r"""The number of summands as an ``int`` when the index set is finite, else ``None``."""
            size = cardinals.cardinal(self.index_set().cardinality())
            return int(size.finite_value()) if size.is_finite() else None

        @staticmethod
        def _factor_point_at(factor, position):
            from itertools import islice

            if factor in EnumeratedSets():
                return factor.ranking_map().inverse()(position)
            absent = object()
            point = next(islice(iter(factor), position, position + 1), absent)
            if point is absent:
                raise IndexError(f"position {position} is out of range for {factor}")
            return point

        @staticmethod
        def _factor_position_of(factor, value):
            if factor in EnumeratedSets():
                return int(factor.ranking_map()(value))
            for position, candidate in enumerate(factor):
                if candidate == value:
                    return position
            raise ValueError(f"{value!r} is not an element of {factor}")

        def _factor_has_position(self, factor, position) -> bool:
            r"""Whether the summand ``factor`` has a point at rank ``position``."""
            size = cardinals.cardinal(factor.cardinality())
            if size.is_finite():
                return position < int(size.finite_value())
            return True

        def _known_finite_size(self):
            r"""This coproduct's size as an ``int`` when finite, else ``None``."""
            size = cardinals.cardinal(self.cardinality())
            return int(size.finite_value()) if size.is_finite() else None

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
                    factor = self.cofactor(index_at(index_position))
                    if self._factor_has_position(factor, factor_position):
                        yield index_position, factor_position
                diagonal += 1

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""The lazy enumeration by rank layer, diagonalized when infinite."""

            def point_at(position):
                position = int(position)
                if position < 0:
                    raise IndexError(
                        f"position {position} is out of range for {self}: positions are nonnegative"
                    )
                finite_size = self._known_finite_size()
                if finite_size is not None and position >= finite_size:
                    raise IndexError(
                        f"position {position} is out of range for {self}, which has {finite_size} elements"
                    )
                index_at = self.index_set().ranking_map().inverse()
                for reached, (index_position, factor_position) in enumerate(self._enumeration_pairs()):
                    if reached != position:
                        continue
                    index = index_at(index_position)
                    return self(
                        index,
                        self._factor_point_at(self.cofactor(index), factor_position),
                    )
                raise IndexError(f"position {position} is out of range for {self}")

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
                raise ValueError(f"{element!r} is not an element of {self}")

            return self._ranking_isomorphism(position_of, point_at)

        def __iter__(self):
            finite_size = self._known_finite_size()
            positions = range(finite_size) if finite_size is not None else count()
            point_at = self.ranking_map().inverse()
            return (point_at(position) for position in positions)



DisjointUnionsOfSets = CoproductsOfSets


class _FiniteWordSet:
    r"""The length-graded word enumeration at the coproduct owner.

    The summands are already constructed Cartesian powers, or fixed-size
    multisets.  Their union is a singleton for the empty alphabet.  For a
    nonempty countable alphabet it is countably infinite: each degree is
    countable, and repetition of one letter injects N into the union.
    This determines the cardinality without sampling an infinite family.
    """

    _derived_construction_parameters = frozenset({"family"})

    def __init__(self, alphabet, commutative, **rest) -> None:
        self._alphabet = alphabet
        match commutative:
            case True:
                degree_set = alphabet.multisets_of_size
            case False:
                def degree_set(degree):
                    positions = finite_ordinal_set(int(degree))
                    return Sets().product(indexed_family(positions, lambda _: alphabet))
        super().__init__(family=indexed_family(NN, degree_set), **rest)

    def cardinality(self):
        match self._alphabet.cardinality() == 0:
            case True:
                return cardinals.cardinal(1)
            case False:
                return cardinals.aleph0


@cached_function
def _finite_words(alphabet, *, commutative):
    r"""Construct the countable coproduct of the alphabet's finite powers."""
    assert alphabet in EnumeratedSets(), (
        f"the words over {alphabet} are enumerated here only for an enumerated alphabet"
    )
    match alphabet.cardinality() == 0:
        case True:
            size_category = FiniteSets()
        case False:
            size_category = CountablyInfiniteSets()
    return _object_of(
        Category.join((EnumeratedCoproductsOfSets(), size_category)),
        _engine=(CoproductsOfSets(), _FiniteWordSet, None),
        alphabet=alphabet, commutative=commutative,
    )


def _finite_family_key(family: IndexedFamily) -> tuple[int, tuple[int, ...]]:
    r"""Intern a finite construction by its exact index set and factor objects.

    Resolving a finite family is legitimate here; its labels are retained by
    the family rather than replaced by positions.  The resulting parent keeps
    the family and its factors alive, so identity keys cannot be recycled.
    """
    return id(family.index_set()), tuple(id(value) for value in family)


@cached_function(key=_finite_family_key)
def _cartesian_product_of_finite_family(family: IndexedFamily) -> Parent:
    return CartesianProductsOfSets()(family)


def _cartesian_product_morphism[IndexT](
    source: Parent,
    target: Parent,
    component_morphisms: Callable[[IndexT], SetMorphism],
) -> SetMorphism:
    r"""Return the componentwise map between two dependent products."""
    if source.index_set() is not target.index_set():
        raise ValueError(
            f"a componentwise map of products needs one index set, but {source} is indexed by "
            f"{source.index_set()} and {target} by {target.index_set()}"
        )
    return Sets().Mor(source, target)(lambda element: target(lambda index: component_morphisms(index)(element.component(index))))


@cached_function(key=_finite_family_key)
def _coproduct_of_finite_family(family: IndexedFamily) -> Parent:
    return CoproductsOfSets()(family)


@cached_function(key=lambda family: id(family))
def _coproduct_of_indexed_family(family: IndexedFamily) -> Parent:
    r"""Build the coproduct of the family of sets ``family`` in the category its summands decide.

    A disjoint union of finitely many enumerated sets over an enumerated index
    set is enumerated by rank layer (``EnumeratedCoproductsOfSets``); it is
    finite when every summand is, and countably infinite otherwise.  Any
    other coproduct is placed as a set, with no enumeration claimed.
    """
    index_set = family.index_set()
    placements = [CoproductsOfSets()]
    if (
        index_set in FiniteSets()
        and index_set in EnumeratedSets()
        and all(family(index) in EnumeratedSets() for index in index_set)
    ):
        placements.append(EnumeratedCoproductsOfSets())
        if all(family(index) in FiniteSets() for index in index_set):
            placements.append(FiniteSets())
        else:
            placements.append(CountablyInfiniteSets())
    return _object_of(Category.join(placements), family=family)


def _coproduct_morphism[IndexT](
    source: Parent,
    target: Parent,
    component_morphisms: Callable[[IndexT], SetMorphism],
) -> SetMorphism:
    r"""Return the componentwise map between two dependent coproducts."""
    if source.index_set() is not target.index_set():
        raise ValueError(
            f"a componentwise map of coproducts needs one index set, but {source} is indexed by "
            f"{source.index_set()} and {target} by {target.index_set()}"
        )
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

        def __init__(self, parent: Parent, value: int) -> None:
            Element.__init__(self, parent)
            # The datum is a Python integer; admission of foreign data is
            # the parent's element constructor's, which is the one boundary
            # that reads it.
            assert value >= 0, f"{value} is not a natural number: it is negative"
            self._value = value

        def __int__(self) -> int:
            return self._value

        __index__ = __int__

        def __hash__(self):
            # Equality is decided on the number, not on the parent that
            # presented it, so the hash is the number's.
            return hash(self._value)

        def __eq__(self, other: Any) -> bool:
            if other not in self.parent():
                return False
            return int(self.parent()(other)) == self._value

        def __ne__(self, other):
            return not self == other

        def __lt__(self, other):
            other = self.parent()(other)
            return self._value < other._value

        def __le__(self, other):
            other = self.parent()(other)
            return self._value <= other._value

        def __gt__(self, other):
            other = self.parent()(other)
            return self._value > other._value

        def __ge__(self, other):
            other = self.parent()(other)
            return self._value >= other._value

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
                    raise ZeroDivisionError(f"cannot compute {self} mod 0 in the natural numbers")
                case _:
                    return self.parent()(self._value % divisor)

        def _repr_(self):
            return str(self._value)

    class ParentMethods:
        def __init__(self, **rest) -> None:
            super().__init__(**rest)

        def _element_constructor_(self, value):
            r"""The natural number ``value`` names; its admission is :meth:`__contains__`."""
            match value:
                case _ if element_parent(value) is self:
                    return value
                case _ if value in self:
                    return self.element_class(self, int(value))
                case _:
                    raise ValueError(f"{value!r} is not a natural number")

        def __call__(self, value):
            r"""Construct an owned natural number without Sage coercion discovery."""
            return self._element_constructor_(value)

        def __contains__(self, value) -> bool:
            r"""Decide whether ``value`` names a natural number.

            The argument is genuinely arbitrary here, so the question is
            whether this set has a point for it: a natural number of this
            set, the Python integer literal a mathematician writes at a
            prompt, or a nonnegative owned integer, since
            \(\mathbb N\subset\mathbb Z\).  A raw engine integer is not an
            owned value and names nothing here.
            """
            match value:
                case _ if element_parent(value) is self:
                    return True
                case _ if isinstance(value, int):
                    return value >= 0
                case _ if isinstance(value, Element) and element_parent(value) in Objects() and isinstance(value, SupportsIndex):
                    return integer_index(value) >= 0
                case _:
                    return False

        def __iter__(self):
            index = 0
            while True:
                yield self(index)
                index += 1

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""The identity: $\mathbb N$ is the ordinal $\omega$ that counts it."""
            return self._ranking_isomorphism(lambda value: int(self(value)), self)

        def zero(self) -> Element:
            return self(0)

        def _repr_(self):
            return "NN = {0, 1, 2, ...}"

        def _latex_(self):
            return r"\mathbb{N}=\{0,1,2,\ldots\}"


class Mors(OwnedCategory):
    r"""Mor objects \(\operatorname{Hom}(X,Y)\), which are sets."""

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
    r"""Exponentials \(Y^X\) over a finite exponent \(X\).

    Every function out of a finite set has finite support, whichever base
    point of \(Y\) support is measured against, so these are the function
    sets on which finite support is a theorem rather than a hypothesis.  A
    finitely supported function set is a function set: that is its one
    immediate supercategory.
    """

    def an_object(self) -> Parent:
        r"""Functions from the ordinal 2 to itself, all of finite support."""
        return finite_ordinal_set(2).exponential(finite_ordinal_set(2))

    def super_categories(self):
        return [FunctionSets()]


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
