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

from collections.abc import Iterator
from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom, all_axioms
from sage.categories.sets_cat import Sets as SageSets
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.semirings.non_negative_integer_semiring import NN

from dzack_research.preamble.lexicon.interop import SageParent, SageUniqueRepresentation



if TYPE_CHECKING:
    # Sage's abstract_method ships untyped; for type-checking use
    # abc.abstractmethod (typed, and permits the empty abstract bodies
    # below). Runtime uses Sage's.
    from abc import abstractmethod as abstract_method

    from dzack_research.preamble.categories.sets.cardinals import Cardinal
else:
    from sage.misc.abstract_method import abstract_method

_SET_AXIOMS = ("Countable", "Uncountable", "TotallyOrdered")


def register_set_axioms() -> None:
    r"""Register exactly ``Countable``, ``Uncountable``, and
    ``TotallyOrdered`` in Sage's global
    axiom registry. Idempotent: after the first registration, repeated calls
    leave the registry unchanged."""
    for axiom_name in _SET_AXIOMS:
        if axiom_name not in all_axioms:
            all_axioms.add(axiom_name)
    assert all(axiom_name in all_axioms for axiom_name in _SET_AXIOMS)


register_set_axioms()


class CountabilitySubcategoryMethods:
    r"""The ``Countable``/``Uncountable`` axiom requests with their
    disjointness guards. Shared by the owned ``Sets()`` root and by every
    owned structured root whose objects carry set axioms (magmas, additive
    magmas, and their descendants)."""

    # Runtime Sage mixes this class into every subcategory, so ``self``
    # is a Category there; the casts state that fact for the checker.
    def Countable(self) -> Category:
        r"""Objects whose underlying set has a chosen computable,
        exhaustive, duplicate-free enumeration."""
        category = self
        assert "Uncountable" not in category.axioms(), "Countable and Uncountable are disjoint"
        return category._with_axiom("Countable")

    def Uncountable(self) -> Category:
        r"""Objects whose underlying set is beyond every enumeration, by
        trusted declaration. (The reverse contradiction, ``Uncountable``
        then ``Finite``, is refused by Sage's native finite/infinite
        incompatibility because ``Uncountable`` implies ``Infinite``.)"""
        category = self
        assert "Countable" not in category.axioms(), "Countable and Uncountable are disjoint"
        return category._with_axiom("Uncountable")

    def TotallyOrdered(self) -> Category:
        r"""Objects whose underlying set is equipped with a total order."""
        category = self
        return category._with_axiom("TotallyOrdered")


class Sets(Category):
    r"""The owned category of sets: declaration owner of the generic
    meanings of cardinality, finiteness, infinitude, countability,
    uncountability, enumeration, indexing, and reverse lookup."""

    def super_categories(self) -> list[Category]:
        return [SageSets()]

    if TYPE_CHECKING:
        # Typed axiom navigation: at runtime Sage synthesizes these from
        # SubcategoryMethods; the axiom tree is closed under its own axioms.
        # The class-attribute wiring at the bottom of this module is Sage's
        # class-resolution shortcut and is runtime-only.
        def Countable(self) -> Sets: ...
        def Uncountable(self) -> Sets: ...
        def TotallyOrdered(self) -> Sets: ...
        def Finite(self) -> Sets: ...
        def Infinite(self) -> Sets: ...
        def Facade(self) -> Sets: ...
        # Sage synthesizes the construction category from the Sage Sets
        # SubcategoryMethods (covariant-construction machinery), for every
        # subcategory of Sets; not an axiom, so it does not return Sets.
        def CartesianProducts(self) -> Category: ...

    SubcategoryMethods = CountabilitySubcategoryMethods

    class ParentMethods:
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


class FiniteSets(CategoryWithAxiom):
    r"""Finite sets: Sage's standard axiom, plus the owned refinement that
    finiteness implies the countable enumeration contract."""

    _base_category_class_and_axiom = (Sets, "Finite")

    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().Countable()]

    def __contains__(self, parent: object) -> bool:
        r"""Return whether ``parent`` is a finite set.

        Sage's default answers from category placement alone, so an object
        that has *computed* its finiteness — and says so through
        ``is_finite`` — is reported infinite merely because nothing refined
        it afterwards. Finiteness is a property of the object, and this
        category is the place that asks for it, so a caller writing the
        membership question gets the object's own answer rather than a
        record of how it was constructed.
        """
        from sage.structure.parent import Parent

        if super().__contains__(parent):
            return True
        return isinstance(parent, Parent) and bool(parent.is_finite())

    class ParentMethods:
        def cardinality(self) -> Cardinal:
            r"""The exact count, by materializing the chosen enumeration —
            finite sets own the termination-dependent implementation,
            constructed from the witness suite.

            A construction that determines its own count states it directly
            (the fundamental finite sets, cartesian products, disjoint
            unions).  This is the one-time evaluation witness for a finite
            set whose construction does not: the enumeration runs once and
            the cardinal it yields is the set's stored count from then on."""
            stored = self.__dict__.get("_owned_cardinality")
            if stored is not None:
                return stored

            from sage.rings.integer_ring import ZZ

            from dzack_research.preamble.categories.sets.cardinals import Cardinal

            stored = Cardinal(ZZ(sum(1 for _ in self)))
            self._owned_cardinality = stored
            return stored


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

    def extra_super_categories(self) -> list[Category]:
        from sage.categories.enumerated_sets import EnumeratedSets

        return [EnumeratedSets()]

    class ParentMethods:
        # Operations of a CHOSEN enumeration, available where one exists;
        # never obligations of countability.  ponytail: they read the
        # enumeration through iteration rather than through the slice object
        # that properly holds it -- see the module note on Slice(f).
        def __getitem__(self, n: int) -> object:
            r"""The ``n``-th element of the chosen enumeration, ``n >= 0``."""
            assert n >= 0, f"enumeration indices are nonnegative; found {n}"
            for position, element in enumerate(self):
                if position == n:
                    return element
            assert False, f"index {n} exceeds the enumeration of {self}"

        def index(self, element: object) -> int:
            r"""Reverse lookup in the chosen enumeration: terminates for
            members and satisfies ``X[X.index(x)] == x``. No termination
            promise for a nonmember of an infinite parent."""
            for position, candidate in enumerate(self):
                if candidate == element:
                    return position
            assert False, f"{element} is not in the enumeration of {self}"

        def enumeration_injection(self) -> object:
            r"""The monomorphism into the SET of nonnegative integers
            realized by the chosen enumeration, ``x -> index(x)``, as an
            element of the actual homset — the constructed effective
            witness of countability. (The codomain is the underlying set of
            the naturals: the injection is a set map, so it forgets the
            semiring structure of its codomain.)"""
            from sage.categories.homset import Hom  # type: ignore[attr-defined]
            from sage.categories.morphism import SetMorphism

            from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

            target = UnderlyingSet(NonNegativeIntegers())
            homset = Hom(self, target, SageSets())
            # target[n] IS the natural number n (identity enumeration),
            # already normalized into the host parent.
            return SetMorphism(homset, lambda element: target[self.index(element)])

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

    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().Infinite()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return False

        def is_uncountable(self) -> bool:
            return True

        def cardinality(self) -> Cardinal:
            r"""The continuum, ``2^aleph_0``: exact for every uncountable
            object constructible in this graph (see ``objects/cardinals``)."""
            from dzack_research.preamble.categories.sets.cardinals import continuum

            return continuum


class TotallyOrderedSets(CategoryWithAxiom):
    r"""Totally ordered sets."""

    _base_category_class_and_axiom = (Sets, "TotallyOrdered")


_SET_AXIOM_NAMES = ("Finite", "Infinite", "Countable", "Uncountable", "TotallyOrdered")


def placement_of(parent: SageParent) -> Sets:
    r"""The owned ``Sets()`` placement a parent's declared axioms carry.

    Countability, finiteness and order are answers this parent already
    declares; reading them off is how an object enters the owned sets able
    to answer what ``Sets`` declares abstract.  Contradictory declarations
    are refused by the owned axiom guards at translation time.

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
    if "Uncountable" in axioms:
        placement = placement.Uncountable()
    elif "Infinite" in axioms:
        placement = placement.Infinite()
    if "TotallyOrdered" in axioms:
        placement = placement.TotallyOrdered()
    return placement


class NonNegativeIntegers(SageUniqueRepresentation, SageParent):
    r"""The nonnegative integers as an owned countable set: the identity
    enumeration ``0, 1, 2, ...`` over Sage's ``NN``.

    Placed in the owned sets and nowhere higher.  This exists as the codomain
    of :meth:`enumeration_injection`, which is a map of *sets*: it forgets the
    semiring structure of the naturals, so declaring that structure here would
    claim something the one caller discards.
    """

    def __init__(self) -> None:
        SageParent.__init__(self, facade=NN, category=Sets().Countable().Infinite().Facade())

    def _repr_(self) -> str:
        return "Set of nonnegative integers"

    def __iter__(self) -> Iterator[Integer]:
        return iter(NN)

    def index(self, element: Integer | int) -> Integer:
        member = ZZ(element)
        assert member >= 0, f"{element} is not a nonnegative integer"
        return member


if not TYPE_CHECKING:
    # Sage's class-resolution shortcut: the axiom category class must be
    # reachable as `<BaseCategory>.<Axiom>` for `_base_category_class_and_axiom`
    # to resolve. Runtime-only wiring; the typed surface of these names is the
    # axiom-navigation method declarations on the category class above.
    Sets.Finite = FiniteSets
    Sets.Infinite = InfiniteSets
    Sets.Countable = CountableSets
    Sets.Uncountable = UncountableSets
    Sets.TotallyOrdered = TotallyOrderedSets
    CountableSets.Infinite = CountablyInfiniteSets
