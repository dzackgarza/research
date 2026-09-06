"""Owned Set categories, canonical index objects, and categorical constructions."""

from collections.abc import Callable, Iterable
from itertools import count

from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Homset
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.combinat.subset import Subsets as SageSubsets
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.integer import Integer as SageInteger
from sage.rings.integer_ring import ZZ
from sage.sets.condition_set import ConditionSet as SageConditionSet
from sage.sets.image_set import ImageSet as SageImageSet
from sage.sets.set import Set as SageSet
from sage.structure.element import Element, parent as element_parent
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.owned_category import OwnedParent, object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    _category_homset,
    CategoricalHomset,
    CategoricalIsomorphism,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
    aleph,
    aleph0,
    cardinal,
)
from dzack_research.preamble.categories.sets.indexed_families import indexed_family



class EnumeratedSets(OwnedCategory):
    r"""Sets equipped with a represented ranking/enumeration."""

    def an_object(self):
        r"""The ordinal 2, ranked by its own order."""
        return finite_ordinal_set(2)

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def ranking_map(self):
            r"""Return the isomorphism onto the ordinal counting this set.

            An enumeration is a bijection $X \xrightarrow{\ \sim\ }
            \operatorname{Ord}(|X|)$, so both directions a caller wants are
            this one arrow: it takes a point to its position, and its
            :meth:`inverse` takes a position back to the point there.
            """
            raise NotImplementedError("this enumerated set has no represented ranking map")

        def __getitem__(self, position):
            r"""Return the point at ``position``, the ranking map run backwards."""
            return self.ranking_map().inverse()(position)


class InfiniteEnumeratedSets(OwnedCategory):
    r"""Countably infinite enumerated sets."""

    def an_object(self):
        r"""The natural numbers, enumerated by identity."""
        return NN

    def super_categories(self):
        return [EnumeratedSets()]


class FiniteOrdinalSets(OwnedCategory):
    r"""The canonical finite ordinals \(\{0,\dots,n-1\}\), lazily."""

    def an_object(self):
        r"""\(\{0,1,2\}\)."""
        return finite_ordinal_set(3)

    def super_categories(self):
        # The join every finite ordinal was built in, declared once
        # by the category rather than computed for each object.
        return [EnumeratedSets(), TotallyOrderedSets(), FiniteEnumeratedSets()]

    class ParentMethods:
        def __init__(self, size, **rest) -> None:
            self._size = int(size)
            assert self._size >= 0, "a finite ordinal cardinality is nonnegative"
            super().__init__(facade=True, **rest)

        def cardinality(self):
            return cardinal(self._size)

        def __iter__(self):
            return (NN(index) for index in range(self._size))

        @cached_method
        def ranking_map(self):
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

            return ranking_isomorphism(self, position_of, point_at)

        def __contains__(self, element) -> bool:
            try:
                position = int(element)
            except (TypeError, ValueError):
                return False
            return 0 <= position < self._size

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
            if position < 0 or position >= self._size:
                raise ValueError(element)
            return NN(position)

        def le(self, left, right):
            ranking = self.ranking_map()
            return ranking(left) <= ranking(right)

        def __len__(self):
            return self._size

        def _repr_(self):
            if not self._size:
                return "{}"
            return f"{{0,...,{self._size - 1}}}"



@cached_function
def finite_ordinal_set(size):
    r"""The ordinal $\{0,\dots,n-1\}$.

    Interned by its size, because an ordinal is determined by how much it
    counts: two sets of the same cardinality must reach the *same* codomain
    or their enumerations do not compose.
    """
    return object_of(FiniteOrdinalSets(), size=int(size))


def counting_ordinal(source):
    r"""Return the ordinal that counts ``source``.

    That is $\{0,\dots,n-1\}$ when $|X| = n$ and $\omega$ when $X$ is
    countably infinite.  An uncountable set has no such ordinal here, and
    a set whose cardinality is undecided cannot name one either: both
    refuse rather than guess.
    """
    size = cardinal(source.cardinality())
    if size.is_finite():
        return finite_ordinal_set(size.finite_value())
    assert size.is_countably_infinite(), (
        f"{source} is not countable, so no ordinal represented here counts it"
    )
    return NN


def ranking_isomorphism(source, position_of, point_at):
    r"""Return the enumeration of ``source`` as one isomorphism onto its ordinal.

    An enumeration is a bijection $X \xrightarrow{\ \sim\ }
    \operatorname{Ord}(|X|)$; ranking and unranking are that arrow and its
    inverse, not two operations a convention has to keep agreeing.  The two
    directions are handed over together here and are mutually inverse by the
    construction that supplied them, so the pair is transported rather than
    re-derived point by point -- which for an infinite source is not a
    decidable question at all.

    It is an isomorphism of *sets* and of nothing further: a $G$-set's
    enumeration is not equivariant and a lattice's is not linear.  So it lives
    in the core of $\mathbf{Set}$, where the isomorphisms are the bijections.
    """
    ordinal = counting_ordinal(source)
    forward = Sets().Mor(source, ordinal)(lambda element: NN(position_of(element)))
    backward = Sets().Mor(ordinal, source)(lambda position: point_at(int(position)))
    return CategoricalIsomorphism(
        _set_core().Mor(source, ordinal), forward, backward, verify=False
    )


@cached_function
def _set_core():
    r"""The core of $\mathbf{Set}$, interned so every enumeration shares one home."""
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import Core

    return Core(Sets())


class _Delta:
    r"""The standard finite ordinals \(\Delta[n]=\{0,\ldots,n\}\), and \(\Delta[\aleph_0]=\mathbb N\)."""

    def __getitem__(self, dimension):
        if isinstance(dimension, (int, SageInteger)):
            return finite_ordinal_set(int(dimension) + 1)
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
        return aleph(index)

    def __repr__(self) -> str:
        return "ℵ"


class OwnedSetMorphism(SetMorphism):
    r"""A set map whose composition remains in the canonical owned Set Hom."""

    def __eq__(self, other) -> bool:
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
            raise NotImplementedError(
                "extensional equality of set maps is represented here for finite enumerated domains"
            )
        return all(self(element) == other(element) for element in domain)

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), id(self)))

    def is_identity(self) -> bool:
        return self._preamble_is_identity

    def _image_points(self):
        r"""The image, enumerated: decidable for a finite enumerated domain."""
        domain = self.domain()
        assert domain in FiniteSets() and domain in EnumeratedSets(), (
            "injectivity and surjectivity are decided here on a finite enumerated domain"
        )
        return {self(element) for element in domain}

    def is_injective(self) -> bool:
        r"""Decide ``f(x) = f(y) => x = y`` by counting the image."""
        return len(self._image_points()) == int(self.domain().cardinality())

    def is_surjective(self) -> bool:
        r"""Decide that every point of the codomain is a value."""
        codomain = self.codomain()
        assert codomain in FiniteSets() and codomain in EnumeratedSets(), (
            "surjectivity is decided here on a finite enumerated codomain"
        )
        image = self._image_points()
        return all(point in image for point in codomain)

    def __mul__(self, other):
        if not isinstance(other, SetMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        if self.is_identity():
            return other
        if isinstance(other, OwnedSetMorphism) and other.is_identity():
            return self
        return Sets().Mor(other.domain(), self.codomain())(
            lambda element: self(other(element))
        )


class SetMorCategory(CategoricalHomset):
    r"""The owned category $\mathrm{Mor}_{\mathbf{Set}}(X, Y)$.

    Its objects are the functions $X \to Y$.  A set is a category -- the
    discrete one -- so this is a category like every other `Mor`, and not a
    special set-valued case: `ARC-07` has `Mor` return a category at every
    level.  Sage's ``Homset``, reached through ``CategoricalHomset``, remains
    the runtime parent its ``SetMorphism`` elements require.
    """

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, mor_family, domain, codomain)

    def __call__(self, datum):
        if isinstance(datum, SetMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the set morphism has the wrong source or target")
            if datum.parent() is self:
                return datum
            datum = datum._call_
        if not callable(datum):
            raise TypeError("a set morphism is supplied by a callable")
        morphism = OwnedSetMorphism(self, datum)
        morphism._preamble_is_identity = False
        return morphism

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only for equal set endpoints")
        identity = OwnedSetMorphism(self, lambda element: element)
        identity._preamble_is_identity = True
        return identity

    def identity_at(self, obj):
        return Sets().Mor(obj, obj).identity()

    def _repr_(self):
        return f"Mor_Set({self.domain()}, {self.codomain()})"


class SetMorCategoryConstruction(HomCategoryConstruction):
    r"""The owned family $(X, Y) \mapsto \mathrm{Mor}_{\mathbf{Set}}(X, Y)$."""

    def fixed_category_class(self):
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

    def an_object(self):
        r"""The ordinal 2: two distinct elements, so a map out of it is not forced."""
        return finite_ordinal_set(2)

    def super_categories(self):
        return [Objects()]

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

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a set morphism requires two set objects")
        return _set_mor_category(domain, codomain)








    class SubcategoryMethods:
        def Finite(self):
            r"""Return this category with the axiom that its objects are finite."""
            return self._with_axiom("Finite")

        def Infinite(self):
            r"""Return this category with the axiom that its objects are infinite."""
            return self._with_axiom("Infinite")

        def product(self, family):
            r"""Return $\prod_{i \in I} X_i$ for an indexed family of objects.

            A product is taken over an index set, so the family carries both the
            index set and the factor at each index.  Asking the category is the
            public route (`STY-02`), and naming the index set rather than an arity
            is what `CON-14` requires; the binary `Product(A, B)` is sugar that
            chooses `Sets.Δ[1]` for the caller.

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
                _finite_factor_family,
            )

            family = _finite_factor_family(family, name="Product factors")
            index_set = family.index_set()
            if index_set.is_finite():
                return _cartesian_product_of_tuple(
                    tuple(family.value(index) for index in index_set)
                )
            return CartesianProductOfFamily(index_set, family.value)

        def _categorical_product(self, left, right):
            return CartesianProductOfSets(left, right)

        def coproduct(self, factors):
            r"""Return the coproduct of a finite family of objects of this category."""
            return self._fold_construction(
                self._categorical_coproduct, factors, name="Coproduct factors"
            )

        def _categorical_coproduct(self, left, right):
            return CoproductOfSets(left, right)

        def _categorical_product_morphism(self, left_morphism, right_morphism, source, target):
            return CartesianProductMorphism(
                source, target,
                lambda index: left_morphism if int(index) == 0 else right_morphism,
            )

        def _categorical_coproduct_morphism(self, left_morphism, right_morphism, source, target):
            return CoproductMorphism(
                source, target,
                lambda index: left_morphism if int(index) == 0 else right_morphism,
            )

        def Homsets(self):
            r"""A Hom object of any owned category is a set."""
            return Homsets()

        # Functors out of ``Set``, each spelled as a method of this, their
        # domain category, and named by the construction it performs.

        def free_module(self, base_ring):
            r"""``F_R : Set -> Mod_R``, the free ``R``-module functor.

            The free module on a set has that set for its module generating
            set, so a set map is carried to the linear map sending generator
            to generator.  Left adjoint of the underlying-set functor on
            ``R``-modules; the adjunction is ``free_module_adjunction``.
            """
            from dzack_research.preamble.categories.functors.free_forgetful import (
                free_module_functor,
            )

            return free_module_functor(base_ring)

        def free_module_adjunction(self, base_ring):
            r"""``F_R -| U`` between ``Set`` and ``Mod_R``.

            An adjunction is a method of its left adjoint's domain category,
            and ``F_R`` is the left adjoint.  Its unit at ``S`` sends a label
            to the module generator on that label, and its counit at ``M``
            evaluates a formal ``R``-combination of elements of ``M``.
            """
            from dzack_research.preamble.categories.functors.free_forgetful import (
                free_forgetful_adjunction,
            )

            return free_forgetful_adjunction(base_ring)

        def free_group(self):
            r"""``F : Set -> Grp``, the free-group functor.

            The free group on a set carries that set as its chosen free basis,
            so a set map is carried to the group morphism it determines on the
            free generators.  Left adjoint of the underlying-set functor on
            groups; the adjunction is ``free_group_adjunction``.
            """
            from dzack_research.preamble.categories.functors.free_groups import (
                free_group_functor,
            )

            return free_group_functor()

        def free_group_adjunction(self):
            r"""``F -| U`` between ``Set`` and ``Grp``.

            An adjunction is a method of its left adjoint's domain category,
            and ``F`` is the left adjoint.  Its unit at ``S`` sends a letter to
            the free generator on it, and its counit at ``G`` multiplies out a
            word in the elements of ``G``.
            """
            from dzack_research.preamble.categories.functors.free_groups import (
                free_group_underlying_set_adjunction,
            )

            return free_group_underlying_set_adjunction()

        def cardinality_functor(self):
            r"""``# : core(Set) -> Card``, the cardinality functor.

            Cardinality is an isomorphism invariant: a bijection of sets fixes
            it, and an arbitrary set map does not respect it at all, so this
            functor is defined on the core groupoid of ``Set`` and not on
            ``Set``.  The method is sited here because ``Set`` is the category
            whose core that is, and ``domain()`` reports ``core(Set)``.
            """
            from dzack_research.preamble.categories.functors.cardinality import (
                cardinality_functor,
            )

            return cardinality_functor()

        def power_set_functor(self):
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
                finite_power_set_functor,
            )

            return finite_power_set_functor()

    def coproduct(self, family):
        r"""Return $\coprod_{i \in I} X_i$ for an indexed family of sets.

        The coproduct over an index set, built directly, the way ``product``
        already builds the product.  Folding the binary coproduct over three
        sets gives $(X_0\sqcup X_1)\sqcup X_2$, which satisfies the same
        universal property but is a different object: its index set has two
        elements, one of which is itself a coproduct, so an injection is
        named by a path rather than by an index.  Both are coproducts and
        only one is the coproduct over $I$ (`CON-14`).

        On ``Sets`` rather than on ``Sets.SubcategoryMethods``, because this
        is the coproduct of *sets*.  A subcategory keeps the fold of its own
        binary coproduct until it builds its own over an index set, which is
        where a free product or a direct sum belongs.

        A bare sequence of factors is the family on the canonical labels, so
        the caller may hand over either.
        """
        from dzack_research.preamble.categories.abstract_categories.products import (
            _finite_factor_family,
        )

        family = _finite_factor_family(family, name="Coproduct factors")
        index_set = family.index_set()
        return _coproduct_of_tuple(
            tuple(family.value(index) for index in index_set)
        )

    def identity(self, set_object):
        return self.Mor(set_object, set_object).identity()

    def Countable(self):
        return CountableSets()

    def CountablyInfinite(self):
        return CountablyInfiniteSets()

    def Uncountable(self):
        return UncountableSets()

    def PartiallyOrdered(self):
        return PartiallyOrderedSets()

    def TotallyOrdered(self):
        return TotallyOrderedSets()

    class ParentMethods:
        def Mor(self, codomain, category=None):
            if category is None:
                return Sets().Mor(self, codomain)
            return _category_homset(category, self, codomain)

        def power_set(self):
            return PowerSet(self)

        def exponential(self, exponent):
            return ExponentialOfSets(self, exponent)

        def __mul__(self, other):
            r"""Return $X \times Y$.  A product of sets is a set."""
            return self.product_with(other)

        def product_with(self, other):
            r"""Return $X \times Y$, the product asked of the objects.

            `STY-02`: the construction is asked of the objects rather than of a
            global constructor.  The index set chosen here is `Sets.Δ[1]`; when
            the index set is part of the mathematics, name it and use
            `Sets().product(family)` (`CON-14`).
            """
            assert other in Sets(), "a product is taken between two owned sets"
            factors = (self, other)
            return Sets().product(
                indexed_family(Sets.Δ[1], lambda index: factors[int(index)])
            )

        def __pow__(self, exponent):
            r"""Return $X^n$, the product of the constant family over `Sets.Δ[n-1]`."""
            count = int(exponent)
            if count < 1:
                raise ValueError("a set power is indexed by a nonempty finite set")
            return Sets().product(indexed_family(Sets.Δ[count - 1], lambda index: self))

        def subsets_of_size(self, size):
            return SubsetsOfSize(self, size)

        def finite_subsets(self):
            return FiniteSubsets(self)

    class Finite(CategoryWithAxiom):
        r"""Sets whose cardinality is finite."""

        def an_object(self):
            r"""The ordinal 2."""
            return finite_ordinal_set(2)

        # Functors into finite G-sets, sited on their domain.

        def trivial_action(self, group):
            r"""``Triv_G : FinSet -> FinGSet_G``, every point fixed."""
            from dzack_research.preamble.categories.functors.g_sets import TrivialGSetFunctor

            return TrivialGSetFunctor(group)

        def free_action(self, group):
            r"""``G x - : FinSet -> FinGSet_G``, the free ``G``-set on a set."""
            from dzack_research.preamble.categories.functors.g_sets import FreeGSetFunctor

            return FreeGSetFunctor(group)

        def free_underlying_adjunction(self, group):
            r"""``G x - -| U``."""
            from dzack_research.preamble.categories.functors.g_sets import (
                free_g_set_underlying_adjunction,
            )

            return free_g_set_underlying_adjunction(group)

        def trivial_fixed_adjunction(self, group):
            r"""``Triv_G -| (-)^G``."""
            from dzack_research.preamble.categories.functors.g_sets import (
                g_set_trivial_fixed_adjunction,
            )

            return g_set_trivial_fixed_adjunction(group)

        def __contains__(self, candidate) -> bool:
            if candidate not in Sets():
                return False
            try:
                return cardinal(candidate.cardinality()).is_finite()
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                return False

    class Infinite(CategoryWithAxiom):
        r"""Sets whose cardinality is infinite."""

        def an_object(self):
            r"""The natural numbers."""
            return NN

        def __contains__(self, candidate) -> bool:
            # The cardinality of the underlying set decides this, as it does for
            # FiniteSets.  Sage's own Infinite() axiom answers for Sage's graph, in
            # which an owned set is not placed at all (`CAT-12`).
            if candidate not in Sets():
                return False
            try:
                return not cardinal(candidate.cardinality()).is_finite()
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                return False
def FiniteSets():
    r"""The category of finite sets."""
    return Sets().Finite()


def InfiniteSets():
    r"""The category of infinite sets."""
    return Sets().Infinite()




def Set(source):
    r"""Return ``source`` as an owned set whenever this constructor creates it."""
    if source in Sets() or source in SageSets():
        return source
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

    return finite_ordered_set(tuple(SageSet(source)))


def ConditionSet(universe, predicate):
    r"""Return the subset of ``universe`` cut out by ``predicate``."""
    return SageConditionSet(universe, predicate)


def ImageSet(map_, domain_subset, *, category=None, is_injective=None, inverse=None):
    r"""Return the represented image of ``domain_subset`` under ``map_``."""
    try:
        domain_cardinality = domain_subset.cardinality()
        if domain_cardinality.is_finite():
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

            return finite_ordered_set(tuple(map_(element) for element in domain_subset))
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        pass
    return SageImageSet(
        map_,
        domain_subset,
        category=category,
        is_injective=is_injective,
        inverse=inverse,
    )


class SetInjection(OwnedSetMorphism):
    r"""A set morphism supplied with the assertion that it is injective."""

    def is_injective(self) -> bool:
        return True


class SetSurjection(OwnedSetMorphism):
    r"""A set morphism supplied with the assertion that it is surjective."""

    def is_surjective(self) -> bool:
        return True


def set_injection(domain, codomain, function):
    return SetInjection(Sets().Mor(domain, codomain), function)


def set_surjection(domain, codomain, function):
    return SetSurjection(Sets().Mor(domain, codomain), function)


class SetInclusion(OwnedSetMorphism):
    r"""A represented subobject inclusion \(A\hookrightarrow X\)."""

    def __init__(
        self,
        domain,
        codomain,
        characteristic_morphism=None,
        finite_members=None,
    ) -> None:
        parent = Sets().Mor(domain, codomain)
        SetMorphism.__init__(self, parent, lambda member: codomain(member))
        self._characteristic_morphism = characteristic_morphism
        self._finite_members = finite_members

    def inclusion(self):
        return self

    def is_injective(self) -> bool:
        return True

    def factor_through(self, target_inclusion):
        r"""Return the canonical map of subset objects when this subset is contained."""
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError("subset factorization requires one common base set")
        if not self <= target_inclusion:
            raise ValueError("the first subset is not contained in the second")
        return SetMorphism(
            Sets().Mor(self.domain(), target_inclusion.domain()),
            lambda member: target_inclusion.domain()(self(member)),
        )

    def underlying_set(self):
        return self.domain()

    def characteristic_morphism(self):
        if self._characteristic_morphism is None:
            raise NotImplementedError(
                "this subobject has no represented decidable characteristic morphism"
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

    def cardinality(self):
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
        if base in FiniteEnumeratedSets():
            return all(member not in self or member in other for member in base)
        raise NotImplementedError(
            "this subset relation has no represented decision procedure"
        )

    def union(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: member in self or member in other
        )

    def intersection(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: member in self and member in other
        )

    def difference(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: member in self and member not in other
        )

    def symmetric_difference(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: (member in self) != (member in other)
        )

    def complement(self):
        return PowerSet(self.codomain()).from_predicate(lambda member: member not in self)

    def __or__(self, other):
        return self.union(other)

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other not in PowerSet(self.codomain()):
            return False
        if self._finite_members is not None and other._finite_members is not None:
            return len(self._finite_members) == len(other._finite_members) and all(
                member in other for member in self._finite_members
            )
        if self.codomain() in FiniteEnumeratedSets():
            return all((member in self) == (member in other) for member in self.codomain())
        return self._characteristic_morphism is other._characteristic_morphism

    def __ne__(self, other) -> bool:
        return not self == other

    def _repr_(self) -> str:
        return f"Subobject of {self.codomain()} defined by {self.domain()}"


class PowerSets(OwnedCategory):
    r"""The power object \(P(X)\), represented by subobjects of ``X``."""

    def an_object(self):
        r"""One object of this category."""
        return PowerSet(Sets.Δ[2])

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, base_set, **rest) -> None:
            assert base_set in Sets(), "a power set is formed from an owned set"
            self._base_set = base_set
            super().__init__(**rest)

        def base_set(self):
            return self._base_set

        def truth_values(self):
            return Sets.Δ[1]

        def characteristic_homset(self):
            return Sets().Mor(self.base_set(), self.truth_values())

        characteristic_hom_category = characteristic_homset

        def _subset_from_predicate(self, predicate: Callable):
            truth_values = self.truth_values()
            characteristic = SetMorphism(
                self.characteristic_homset(),
                lambda member: truth_values(ZZ.one() if predicate(member) else ZZ.zero()),
            )
            domain = ConditionSet(self.base_set(), predicate)
            return SetInclusion(domain, self.base_set(), characteristic)

        def from_predicate(self, predicate: Callable):
            return self._subset_from_predicate(predicate)

        def from_characteristic_morphism(self, characteristic_morphism):
            if characteristic_morphism.parent() is not self.characteristic_homset():
                raise ValueError("a characteristic morphism must lie in Hom(X, Δ[1])")
            truth = self.truth_values()(1)

            def predicate(member):
                return characteristic_morphism(member) == truth

            domain = ConditionSet(self.base_set(), predicate)
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
            characteristic = SetMorphism(
                self.characteristic_homset(),
                lambda member: truth_values(ZZ.one() if member in frozen else ZZ.zero()),
            )
            domain = ConditionSet(self.base_set(), lambda member: member in frozen)
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

        def top(self):
            return self(self.base_set())

        def bottom(self):
            return self(())

        def inverse_image_morphism(self, morphism):
            if morphism.codomain() is not self.base_set():
                raise ValueError("inverse image requires the morphism codomain to be the base set")
            target = PowerSet(morphism.domain())
            return SetMorphism(
                Sets().Mor(self, target),
                lambda subset: target.from_predicate(lambda member: morphism(member) in subset),
            )

        def direct_image_morphism(self, morphism):
            if morphism.domain() is not self.base_set():
                raise ValueError("direct image requires the morphism domain to be the base set")
            target = PowerSet(morphism.codomain())

            def direct_image(subset):
                size = subset.cardinality()
                if not size.is_finite():
                    image_domain = ImageSet(morphism, subset.domain())
                    return SetInclusion(image_domain, morphism.codomain())
                return target(tuple(morphism(member) for member in subset))

            return SetMorphism(Sets().Mor(self, target), direct_image)

        def __iter__(self):
            if self.base_set() not in FiniteEnumeratedSets():
                raise TypeError("only a finite power set has a chosen enumeration")
            return (self(subset) for subset in SageSubsets(self.base_set()))

        def cardinality(self):
            return cardinal(2) ** cardinal(self.base_set().cardinality())

        def cardinality_comparison(self):
            size = self.cardinality()
            return Cardinalities().Mor(size, size).identity()

        def _repr_(self) -> str:
            return f"Power set of {self.base_set()}"




@cached_function
def PowerSet(base_set):
    return object_of(PowerSets(), base_set=base_set)


def _function_set_of(codomain, exponent):
    r"""Build \(Y^X\) and place it.

    Over a finite exponent every function is finitely supported, and over an
    infinite one that is exactly what fails, so the refinement is read off the
    exponent.
    """
    from dzack_research.preamble.refine import refine

    exponential = object_of(FunctionSets(), codomain=codomain, exponent=exponent)
    if exponent in FiniteSets():
        refine(exponential, FinitelySupportedFunctionSets())
    return exponential


class FunctionSets(OwnedCategory):
    r"""Exponentials \(Y^X=\operatorname{Hom}_{Set}(X,Y)\)."""

    def an_object(self):
        r"""\(\Delta_2^{\Delta_1}\)."""
        return ExponentialOfSets(Sets.Δ[2], Sets.Δ[1])

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, codomain, exponent, **rest) -> None:
            assert codomain in Sets() and exponent in Sets(), (
                "an exponential requires two owned sets"
            )
            self._codomain = codomain
            self._exponent = exponent
            super().__init__(**rest)

        def base(self):
            return self._codomain

        def exponent(self):
            return self._exponent

        def _preamble_all_functions_finitely_supported(self) -> bool:
            return self.exponent() in FiniteSets()

        def homset(self):
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

        def cardinality(self):
            return cardinal(self.base().cardinality()) ** cardinal(self.exponent().cardinality())

        def _repr_(self) -> str:
            return f"{self.base()}^{self.exponent()}"



@cached_function
def ExponentialOfSets(codomain, exponent):
    return _function_set_of(codomain, exponent)


class FixedCardinalitySubsetSets(OwnedCategory):
    r"""The sets \([X]^k\) of subsets of one fixed finite cardinality."""

    def an_object(self):
        r"""One object of this category."""
        return SubsetsOfSize(Sets.Δ[2], 2)

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, source, subset_cardinality, **rest) -> None:
            self._source = source
            self._subset_cardinality = int(subset_cardinality)
            assert self._subset_cardinality >= 0, "a subset cardinality is nonnegative"
            super().__init__(**rest)

        def source(self):
            return self._source

        def subset_cardinality(self):
            return self._subset_cardinality

        def power_set(self):
            return PowerSet(self.source())

        def __call__(self, *args, **kwargs):
            r"""Construct through the owned set representation directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, members):
            subset = self.power_set()(members)
            if subset.cardinality() != cardinal(self.subset_cardinality()):
                raise ValueError(
                    f"a member of {self} has cardinality {self.subset_cardinality()}"
                )
            return subset

        def __contains__(self, candidate) -> bool:
            if candidate not in self.power_set():
                return False
            return self.power_set()(candidate).cardinality() == cardinal(
                self.subset_cardinality()
            )

        def __iter__(self):
            if self.source() not in FiniteEnumeratedSets():
                raise TypeError(
                    "the current enumeration of fixed-cardinality subsets requires a finite source"
                )
            return (
                self(tuple(subset))
                for subset in SageSubsets(self.source(), self.subset_cardinality())
            )

        def cardinality(self):
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
def SubsetsOfSize(source, subset_cardinality):
    return object_of(
        FixedCardinalitySubsetSets(),
        source=source,
        subset_cardinality=subset_cardinality,
    )


class FinitePowerSets(OwnedCategory):
    r"""Finite power objects \(P_{fin}(X)\), the finite subsets of \(X\)."""

    def an_object(self):
        r"""One object of this category."""
        return FiniteSubsets(Sets.Δ[2])

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, source, **rest) -> None:
            self._source = source
            super().__init__(**rest)

        def source(self):
            return self._source

        def power_set(self):
            return PowerSet(self.source())

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
                raise TypeError(
                    "the current enumeration of finite subsets requires a finite source"
                )
            return (self(tuple(subset)) for subset in SageSubsets(self.source()))

        def cardinality(self):
            source_size = cardinal(self.source().cardinality())
            if source_size.is_finite():
                return cardinal(2) ** source_size
            return source_size

        def _repr_(self) -> str:
            return f"Finite subsets of {self.source()}"



@cached_function
def FiniteSubsets(source):
    return object_of(FinitePowerSets(), source=source)


def _cartesian_product_of(index_set, family):
    r"""Build the product and place it.

    Finiteness is a fact about the index set and the factors; the product is
    built in the category it always belongs to and gains the enumerated
    placement it earns.
    """
    try:
        finite = cardinal(index_set.cardinality()).is_finite() and all(
            cardinal(family(index).cardinality()).is_finite() for index in index_set
        )
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        finite = False
    product_category = CartesianProductsOfSets()
    category = product_category
    if finite:
        category = Category.join(
            (product_category, EnumeratedSets(), FiniteEnumeratedSets())
        )
    return product_category.ObjectType(
        category=category, index_set=index_set, family=family
    )


class CartesianProductsOfSets(OwnedCategory):
    r"""Dependent products of families of sets."""

    class ElementMethods(Element):
        r"""What an element of a product of a family is."""

        def __init__(self, parent, components) -> None:
            Element.__init__(self, parent)
            self._components = components

        def component(self, index):
            normalized = self.parent().index_set()(index)
            value = self._components(normalized)
            return self.parent().factor(normalized)(value)

        def __getitem__(self, index):
            return self.component(index)

        def __iter__(self):
            return (
                self.component(index)
                for index in self.parent().index_set()
            )

        def _repr_(self) -> str:
            if not self.parent().has_finite_index_set():
                return f"Section of {self.parent()}"
            return "(" + ", ".join(
                repr(self.component(index)) for index in self.parent().index_set()
            ) + ")"

        def __eq__(self, other) -> bool:
            if self is other:
                return True
            if other.parent() is not self.parent():
                return False
            if not self.parent().has_finite_index_set():
                return False
            return all(
                self.component(index) == other.component(index)
                for index in self.parent().index_set()
            )

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self) -> int:
            if not self.parent().has_finite_index_set():
                return hash((id(self.parent()), id(self._components)))
            value_hash = 0
            for index in self.parent().index_set():
                value_hash = hash((value_hash, self.component(index)))
            return hash((id(self.parent()), value_hash))

    class ParentMethods:

        def __init__(self, index_set, family, **rest) -> None:
            assert index_set in Sets(), (
                "the index object of a product family must be an owned set"
            )
            self._index_set = index_set
            self._family = family
            super().__init__(**rest)

        def index_set(self):
            return self._index_set

        def family(self):
            return self._family

        def has_finite_index_set(self) -> bool:
            try:
                return cardinal(self.index_set().cardinality()).is_finite()
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                return False

        def factor(self, index):
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
            if not self.has_finite_index_set():
                raise TypeError(
                    "a product over an infinite index set is specified by a callable section"
                )
            values = iter(components)
            assignment = {}
            for index in self.index_set():
                try:
                    value = next(values)
                except StopIteration as error:
                    raise ValueError("a product element needs one component per factor") from error
                assignment[index] = self.factor(index)(value)
            try:
                next(values)
            except StopIteration:
                pass
            else:
                raise ValueError("a product element needs one component per factor")
            return self.element_class(self, assignment.__getitem__)

        @cached_method
        def ranking_map(self):
            r"""The mixed-radix enumeration of a finite product of finite factors.

            The represented enumeration is the mixed-radix one, which needs a
            finite index set and a finite enumerated factor at each index.  A
            product of countably many countable factors is still countable, so
            an isomorphism onto $\omega$ exists; this construction is not it,
            and the arrow is refused rather than returned with both directions
            raising when applied.
            """
            assert self.has_finite_index_set(), (
                "the mixed-radix enumeration is represented over a finite index set"
            )
            assert self.index_set() in EnumeratedSets(), (
                "the mixed-radix enumeration reads its index order off the index set"
            )
            index_count = int(cardinal(self.index_set().cardinality()).finite_value())
            index_at = self.index_set().ranking_map().inverse()
            for index in self.index_set():
                factor = self.factor(index)
                assert factor in EnumeratedSets(), (
                    f"the factor at {index} states no enumeration of its own"
                )
                assert cardinal(factor.cardinality()).is_finite(), (
                    f"the factor at {index} is infinite, so the product's "
                    "mixed-radix enumeration is not represented here"
                )
            total_size = int(cardinal(self.cardinality()).finite_value())

            def point_at(position):
                position = int(position)
                if position < 0 or position >= total_size:
                    raise IndexError(position)
                assignment = {}
                quotient = position
                for offset in range(index_count - 1, -1, -1):
                    index = index_at(offset)
                    factor = self.factor(index)
                    radix = int(cardinal(factor.cardinality()).finite_value())
                    quotient, digit = divmod(quotient, radix)
                    assignment[index] = factor.ranking_map().inverse()(digit)
                frozen = dict(assignment)
                return self(lambda index: frozen[index])

            def position_of(section):
                section = self(section)
                position = 0
                for index in self.index_set():
                    factor = self.factor(index)
                    radix = int(cardinal(factor.cardinality()).finite_value())
                    digit = int(factor.ranking_map()(section.component(index)))
                    position = position * radix + digit
                return position

            return ranking_isomorphism(self, position_of, point_at)

        def projection(self, index):
            normalized = self.index_set()(index)
            return SetMorphism(
                Sets().Mor(self, self.factor(normalized)),
                lambda element: element.component(normalized),
            )

        def from_maps(self, source, maps):
            r"""Return the unique map into the product with the stated components."""
            return SetMorphism(
                Sets().Mor(source, self),
                lambda element: self(lambda index: maps(index)(element)),
            )

        def cardinality(self):
            return Cardinalities().indexed_product(
                self.index_set(), lambda index: cardinal(self.factor(index).cardinality())
            )

        def __iter__(self):
            if not self.has_finite_index_set():
                raise TypeError("only a product over a finite index set is enumerated here")
            for index in self.index_set():
                try:
                    if not cardinal(self.factor(index).cardinality()).is_finite():
                        raise TypeError(
                            "product enumeration here requires every represented factor to be finite"
                        )
                except (AttributeError, NotImplementedError, ValueError) as error:
                    raise TypeError(
                        "product enumeration here requires every represented factor to be finite"
                    ) from error

            def sections(position, assignment):
                if position == int(cardinal(self.index_set().cardinality()).finite_value()):
                    frozen = dict(assignment)
                    yield self(lambda index: frozen[index])
                    return
                index = self.index_set().ranking_map().inverse()(position)
                for value in self.factor(index):
                    assignment[index] = value
                    yield from sections(position + 1, assignment)
                assignment.pop(index, None)

            return sections(0, {})

        def _repr_(self) -> str:
            return f"Product of the family over {self.index_set()}"

    def an_object(self):
        r"""The square of the ordinal 2."""
        return CartesianProductOfSets(finite_ordinal_set(2), finite_ordinal_set(2))

    def super_categories(self):
        return [Sets()]


class CoproductsOfSets(OwnedCategory):
    r"""Dependent coproducts (disjoint unions) of families of sets."""

    class ElementMethods(Element):
        r"""What an element of a coproduct of a family is."""

        def __init__(self, parent, index, value) -> None:
            Element.__init__(self, parent)
            normalized = parent.index_set()(index)
            self._index = normalized
            self._value = parent.cofactor(normalized)(value)

        def summand_index(self):
            return self._index

        def summand_element(self):
            return self._value

        def _repr_(self) -> str:
            return f"ι_{self.summand_index()}({self.summand_element()})"

        def __eq__(self, other) -> bool:
            return (
                other.parent() is self.parent()
                and other.parent() is self.parent()
                and other.summand_index() == self.summand_index()
                and other.summand_element() == self.summand_element()
            )

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self) -> int:
            return hash((id(self.parent()), self.summand_index(), self.summand_element()))

    class ParentMethods:

        def __init__(self, index_set, family, **rest) -> None:
            assert index_set in Sets(), (
                "the index object of a coproduct family must be an owned set"
            )
            self._index_set = index_set
            self._family = family
            super().__init__(**rest)

        def index_set(self):
            return self._index_set

        def family(self):
            return self._family

        def cofactor(self, index):
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

        def injection(self, index):
            normalized = self.index_set()(index)
            return SetMorphism(
                Sets().Mor(self.cofactor(normalized), self),
                lambda element: self(normalized, element),
            )

        def from_maps(self, target, maps):
            r"""Return the unique map out of the coproduct extending the stated maps."""
            return SetMorphism(
                Sets().Mor(self, target),
                lambda element: maps(element.summand_index())(element.summand_element()),
            )

        def cardinality(self):
            return Cardinalities().indexed_sum(
                self.index_set(), lambda index: cardinal(self.cofactor(index).cardinality())
            )

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

        @staticmethod
        def _factor_has_position(factor, position) -> bool:
            try:
                size = cardinal(factor.cardinality())
                if size.is_finite():
                    return position < int(size.finite_value())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass
            try:
                CoproductOfFamilyParent._factor_point_at(factor, position)
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
        def ranking_map(self):
            r"""The lazy enumeration by rank layer, diagonalized when infinite."""

            def point_at(position):
                position = int(position)
                if position < 0:
                    raise IndexError(position)
                finite_size = self._known_finite_size()
                if finite_size is not None and position >= finite_size:
                    raise IndexError(position)
                index_at = self.index_set().ranking_map().inverse()
                for reached, (index_position, factor_position) in enumerate(
                    self._enumeration_pairs()
                ):
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

            return ranking_isomorphism(self, position_of, point_at)

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

    def an_object(self):
        r"""The disjoint union of the ordinal 2 with itself."""
        return CoproductOfSets(finite_ordinal_set(2), finite_ordinal_set(2))

    def super_categories(self):
        return [Sets()]


DisjointUnionsOfSets = CoproductsOfSets






@cached_function
def CartesianProductOfFamily(index_set, family):
    return _cartesian_product_of(index_set, family)


@cached_function
def _cartesian_product_of_tuple(factors):
    index_set = Sets.Δ[len(factors) - 1]
    family = lambda index: factors[int(index)]
    return _cartesian_product_of(index_set, family)


def CartesianProductOfSets(*factors):
    return _cartesian_product_of_tuple(tuple(factors))


def cartesian_product_of(factors):
    return CartesianProductOfSets(*tuple(factors))


def CartesianProductMorphism(source, target, component_morphisms):
    r"""Return the componentwise map between two dependent products."""
    if source.index_set() != target.index_set():
        raise ValueError("componentwise product maps require one index set")
    return SetMorphism(
        Sets().Mor(source, target),
        lambda element: target(
            lambda index: component_morphisms(index)(element.component(index))
        ),
    )






@cached_function
def CoproductOfFamily(index_set, family):
    return object_of(CoproductsOfSets(), index_set=index_set, family=family)


@cached_function
def _coproduct_of_tuple(cofactors):
    index_set = Sets.Δ[len(cofactors) - 1]
    return object_of(CoproductsOfSets(), index_set=index_set, family=lambda index: cofactors[int(index)]
    )


def CoproductOfSets(*cofactors):
    return _coproduct_of_tuple(tuple(cofactors))


def CoproductMorphism(source, target, component_morphisms):
    r"""Return the componentwise map between two dependent coproducts."""
    if source.index_set() != target.index_set():
        raise ValueError("componentwise coproduct maps require one index set")
    return SetMorphism(
        Sets().Mor(source, target),
        lambda element: target(
            element.summand_index(),
            component_morphisms(element.summand_index())(element.summand_element()),
        ),
    )


ObjectSetsOfDiscreteCategories = SageSets
ExponentialsOfSets = FunctionSets


class NaturalNumberSets(OwnedCategory):
    r"""The owned set \(\mathbb{N}=\{0,1,2,\dots\}\)."""

    def an_object(self):
        r"""\(\mathbb{N}\)."""
        return NN

    def super_categories(self):
        from dzack_research.preamble.categories.group.magmas import AdditiveMonoids

        # Enumerated as well as countably infinite: the identity ranking
        # is the chosen enumeration.  Declared by the category rather
        # than joined for the one object.
        return [
            CountablyInfiniteSets(),
            TotallyOrderedSets(),
            InfiniteEnumeratedSets(),
            AdditiveMonoids(),
        ]

    class ElementMethods(Element):
        r"""What a natural number is."""

        def __init__(self, parent, value) -> None:
            Element.__init__(self, parent)
            # This constructor is an ingress boundary.  It accepts the owned
            # integer view without importing the higher ring theory back into Sets;
            # the ring exposes only this private runtime marker/engine pair.
            from sage.rings.integer_ring import ZZ as _SageZZ

            if isinstance(value, parent.category().ElementType):
                value = int(value)
            elif isinstance(value, SageObject):
                parent = element_parent(value)
                if not (
                    bool(getattr(parent, "_preamble_owned_ring_parent", False))
                    and getattr(parent, "_engine", None) is _SageZZ
                ):
                    raise TypeError(
                        "raw backend integers are not accepted by the owned natural numbers"
                    )
                value = int(value)
            value = int(value)
            if value < 0:
                raise ValueError("a natural number is nonnegative")
            self._value = value

        def __int__(self):
            return self._value

        __index__ = __int__

        def __hash__(self):
            # Equality is decided on the number, not on the parent that
            # presented it, so the hash is the number's.
            return hash(self._value)

        def __eq__(self, other):
            # The argument is genuinely arbitrary here, so the question is
            # membership rather than what class it is.
            if other not in self.parent():
                return False
            return self.parent()(other)._value == self._value

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
        def ranking_map(self):
            r"""The identity: $\mathbb N$ is the ordinal $\omega$ that counts it."""
            return ranking_isomorphism(self, lambda value: int(self(value)), self)

        def cardinality(self):
            return aleph0

        def zero(self):
            return self(0)

        def _repr_(self):
            return "Natural numbers"

class Homsets(OwnedCategory):
    r"""Hom objects \(\operatorname{Hom}(X,Y)\), which are sets."""

    def an_object(self):
        r"""The endomorphisms of a set, which hold at least its identity."""
        witness = Sets().an_object()
        return Sets().Mor(witness, witness)

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def is_endomorphism_set(self) -> bool:
            return self.domain() is self.codomain()




class CountableSets(OwnedCategory):
    r"""Sets equipped with a countable enumeration."""

    def an_object(self):
        r"""The natural numbers."""
        return NN

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        try:
            return cardinal(candidate.cardinality()).is_countable()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False


class CountablyInfiniteSets(OwnedCategory):
    r"""Countably infinite sets."""

    def an_object(self):
        r"""The natural numbers."""
        return NN

    def super_categories(self):
        return [CountableSets(), InfiniteSets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        try:
            return cardinal(candidate.cardinality()).is_countably_infinite()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False


class UncountableSets(OwnedCategory):
    r"""Sets whose represented cardinal is provably uncountable."""

    def an_object(self):
        r"""The power set of the natural numbers, uncountable by Cantor's theorem."""
        return PowerSet(NN)

    def super_categories(self):
        return [InfiniteSets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        try:
            return cardinal(candidate.cardinality()).is_uncountable()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False


class PartiallyOrderedSets(OwnedCategory):
    r"""Sets equipped with a partial order."""

    def an_object(self):
        r"""The natural numbers under their usual order."""
        return NN

    def super_categories(self):
        return [Sets()]


class TotallyOrderedSets(OwnedCategory):
    r"""Sets equipped with a total order."""

    def an_object(self):
        r"""The natural numbers, totally ordered."""
        return NN

    def super_categories(self):
        return [PartiallyOrderedSets()]






NN = object_of(NaturalNumberSets())


class FinitelySupportedFunctionSets(OwnedCategory):
    r"""Function sets whose elements have finite support."""

    _certifying_predicate = "_preamble_all_functions_finitely_supported"

    def an_object(self):
        r"""Functions from the ordinal 2 to itself, all of finite support."""
        return ExponentialOfSets(finite_ordinal_set(2), finite_ordinal_set(2))

    def super_categories(self):
        return [Sets()]



def placement_of(parent):
    r"""Return the strongest represented owned Set cardinality category for ``parent``."""
    if parent in FiniteSets():
        return FiniteSets()
    if parent in CountablyInfiniteSets():
        return CountablyInfiniteSets()
    if parent in UncountableSets():
        return UncountableSets()
    if parent in InfiniteSets():
        return InfiniteSets()
    if parent in CountableSets():
        return CountableSets()
    return Sets()


def register_set_axioms() -> None:
    r"""Compatibility entry point: the live owned categories need no Sage-global mutation."""
    return None


class SetSubcategoryMethods:
    r"""Compatibility name for the owned Set category-navigation surface."""


__all__ = [
    "CartesianProductMorphism",
    "CartesianProductOfFamily",
    "CartesianProductOfSets",
    "CartesianProductsOfSets",
    "ConditionSet",
    "CountableSets",
    "CountablyInfiniteSets",
    "CoproductMorphism",
    "CoproductOfFamily",
    "CoproductOfSets",
    "CoproductsOfSets",
    "DisjointUnionsOfSets",
    "EnumeratedSets",
    "ExponentialOfSets",
    "FiniteOrdinalSets",
    "FinitePowerSets",
    "FiniteSets",
    "FiniteSubsets",
    "FinitelySupportedFunctionSets",
    "FixedCardinalitySubsetSets",
    "FunctionSets",
    "ImageSet",
    "InfiniteEnumeratedSets",
    "InfiniteSets",
    "NaturalNumberSets",
    "NN",
    "ObjectSetsOfDiscreteCategories",
    "PartiallyOrderedSets",
    "PowerSet",
    "PowerSets",
    "PowerSets",
    "Set",
    "SetInclusion",
    "SetInjection",
    "SetSubcategoryMethods",
    "SetSurjection",
    "Sets",
    "SubsetsOfSize",
    "TotallyOrderedSets",
    "UncountableSets",
    "cartesian_product_of",
    "counting_ordinal",
    "placement_of",
    "finite_ordinal_set",
    "ranking_isomorphism",
    "register_set_axioms",
    "set_injection",
    "set_surjection",
]
