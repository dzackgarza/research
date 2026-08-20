r"""Cardinal numbers, their arithmetic, and their thin category.

``Cardinalities`` is the category associated to the cardinal order.  Its
objects are cardinals.  ``Hom(kappa, lambda)`` is a singleton when
``kappa <= lambda`` and is empty otherwise.

A cardinal is an initial ordinal, thus a set, and the owned ``Sets()`` is
this category's super category.  The subcategory is not full: a cardinal
object keeps its own thin hom-sets.  What it gains is the set surface, which
it already answered -- ``is_finite``, ``is_countable`` and ``is_uncountable``
are the questions about the set of that size -- and now answers as a member
of the owned sets.

The objects are closed under cardinal addition, multiplication, and
exponentiation.  A finite supremum records the maximum of infinite cardinals
when the represented order does not compare the inputs.  This keeps
expressions such as ``aleph(2) + continuum`` defined without adding a
continuum-hypothesis assumption.  The arithmetic follows the definitions and
normalization theorems in Mathlib's ``SetTheory/Cardinal/Defs.lean``,
``Arithmetic.lean``, and ``Continuum.lean``.
"""

from __future__ import annotations


from collections.abc import Iterator
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.category import Category as SageCategory
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.infinity import Infinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

if TYPE_CHECKING:
    from dzack_research.preamble.categories.sets.ordinals import Ordinal, OrdinalInput
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.rings.rational import Rational
    from sage.rings.ring import Ring


type CardinalScalar = Integer | int | PlusInfinity


@dataclass(frozen=True)
class _FiniteCardinal:
    value: Integer


@dataclass(frozen=True)
class _AlephCardinal:
    index: Ordinal


@dataclass(frozen=True)
class _PowerCardinal:
    base: Cardinal
    exponent: Cardinal


@dataclass(frozen=True)
class _SupremumCardinal:
    terms: tuple[Cardinal, ...]


type _CardinalExpression = (
    _FiniteCardinal | _AlephCardinal | _PowerCardinal | _SupremumCardinal
)
type CardinalInput = CardinalScalar | _CardinalExpression


class CardinalComparison(Enum):
    r"""The comparison in the poset of provable cardinal relations."""

    LESS = -1
    EQUAL = 0
    GREATER = 1
    LESS_OR_EQUAL = 2
    GREATER_OR_EQUAL = 3
    INCOMPARABLE = 4


class Cardinalities(Category):
    r"""The thin category associated to the represented cardinal order."""

    def super_categories(self) -> list[SageCategory]:
        return [Sets()]

    def _repr_(self) -> str:
        return "Category of cardinalities"

    def zero(self) -> Cardinal:
        r"""Return the additive identity."""
        return cardinal(0)

    def one(self) -> Cardinal:
        r"""Return the multiplicative identity."""
        return cardinal(1)

    def sum(
        self,
        *summands: Cardinal | CardinalScalar,
    ) -> Cardinal:
        r"""Return the cardinal sum of ``summands``."""
        result = self.zero()
        for summand in map(cardinal, summands):
            if result.is_finite() and summand.is_finite():
                result = cardinal(
                    result.finite_value() + summand.finite_value()
                )
            elif result.is_finite():
                result = summand
            elif summand.is_infinite():
                result = self.supremum(result, summand)
        return result

    def product(
        self,
        *factors: Cardinal | CardinalScalar,
    ) -> Cardinal:
        r"""Return the cardinal product of ``factors``."""
        result = self.one()
        for factor in map(cardinal, factors):
            if result == 0 or factor == 0:
                return cardinal(0)
            if result.is_finite() and factor.is_finite():
                result = cardinal(
                    result.finite_value() * factor.finite_value()
                )
            elif result.is_finite():
                result = factor
            elif factor.is_infinite():
                result = self.supremum(result, factor)
        return result

    def power(
        self,
        base: Cardinal | CardinalScalar,
        exponent: Cardinal | CardinalScalar,
    ) -> Cardinal:
        r"""Return cardinal exponentiation ``base ^ exponent``."""
        cardinal_base = cardinal(base)
        cardinal_exponent = cardinal(exponent)

        if cardinal_exponent == 0:
            return cardinal(1)
        if cardinal_base == 0:
            return cardinal(0)
        if cardinal_base == 1:
            return cardinal(1)

        if cardinal_exponent.is_finite():
            if cardinal_base.is_finite():
                return cardinal(
                    cardinal_base.finite_value()
                    ** cardinal_exponent.finite_value()
                )
            return cardinal_base

        # Normalization: the exponent is infinite here, and for any base with
        # 2 <= base <= exponent, base ^ exponent = 2 ^ exponent (Mathlib
        # ``Cardinal.power_eq_two_power``).  A finite base was not 0 or 1
        # above, so it qualifies; an infinite base qualifies exactly when the
        # represented order compares it below the exponent.
        if cardinal_base.is_finite() or Cardinalities().le(
            cardinal_base, cardinal_exponent
        ):
            cardinal_base = cardinal(2)

        exponent_expression = cardinal_exponent.expression()
        if isinstance(exponent_expression, _SupremumCardinal):
            return self.supremum(
                *(
                    self.power(cardinal_base, term)
                    for term in exponent_expression.terms
                )
            )

        expression = cardinal_base.expression()
        if isinstance(expression, _SupremumCardinal):
            return self.supremum(
                *(
                    self.power(term, cardinal_exponent)
                    for term in expression.terms
                )
            )
        if isinstance(expression, _PowerCardinal):
            return self.power(
                expression.base,
                self.product(expression.exponent, cardinal_exponent),
            )
        return _cardinal_with_expression(
            _PowerCardinal(cardinal_base, cardinal_exponent)
        )

    def sum_morphism(
        self,
        *morphisms: CardinalityMorphism,
    ) -> CardinalityMorphism:
        r"""Apply cardinal addition to a finite family of morphisms."""
        source = self.sum(*(morphism.domain() for morphism in morphisms))
        target = self.sum(*(morphism.codomain() for morphism in morphisms))
        return self.hom(source, target).unique_morphism()

    def product_morphism(
        self,
        *morphisms: CardinalityMorphism,
    ) -> CardinalityMorphism:
        r"""Apply cardinal multiplication to a finite family of morphisms."""
        source = self.product(*(morphism.domain() for morphism in morphisms))
        target = self.product(*(morphism.codomain() for morphism in morphisms))
        return self.hom(source, target).unique_morphism()

    def power_morphism(
        self,
        base_morphism: CardinalityMorphism,
        exponent_morphism: CardinalityMorphism,
    ) -> CardinalityMorphism:
        r"""Apply cardinal exponentiation when the source base is nonzero."""
        assert self.le(1, base_morphism.domain()), (
            "exponentiation is monotone in the exponent for nonzero bases"
        )
        source = self.power(
            base_morphism.domain(),
            exponent_morphism.domain(),
        )
        target = self.power(
            base_morphism.codomain(),
            exponent_morphism.codomain(),
        )
        return self.hom(source, target).unique_morphism()

    def supremum(
        self,
        *cardinal_numbers: Cardinal | CardinalScalar,
    ) -> Cardinal:
        r"""Return the finite supremum of ``cardinal_numbers``."""
        terms: list[Cardinal] = []
        for cardinal_number in map(cardinal, cardinal_numbers):
            expression = cardinal_number.expression()
            if isinstance(expression, _SupremumCardinal):
                terms.extend(expression.terms)
            else:
                terms.append(cardinal_number)

        assert terms, "a finite supremum needs at least one cardinal"
        maximal_terms: list[Cardinal] = []
        for candidate in sorted(set(terms), key=Cardinal.sort_key):
            if any(self.le(candidate, term) for term in maximal_terms):
                continue
            maximal_terms = [
                term for term in maximal_terms if not self.le(term, candidate)
            ]
            maximal_terms.append(candidate)

        maximal_terms.sort(key=Cardinal.sort_key)
        if len(maximal_terms) == 1:
            return maximal_terms[0]
        return _cardinal_with_expression(_SupremumCardinal(tuple(maximal_terms)))

    def le(
        self,
        source: Cardinal | CardinalScalar,
        target: Cardinal | CardinalScalar,
    ) -> bool:
        r"""Return whether the represented theory proves ``source <= target``."""
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return True

        left_expression = left.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _SupremumCardinal):
            return all(self.le(term, right) for term in left_expression.terms)
        if isinstance(right_expression, _SupremumCardinal):
            return any(self.le(left, term) for term in right_expression.terms)

        if left.is_finite():
            if right.is_finite():
                return left.finite_value() <= right.finite_value()
            return True
        if right.is_finite():
            return False

        if left.is_aleph() and right.is_aleph():
            return left.aleph_index() <= right.aleph_index()
        if left.is_countably_infinite():
            return True
        if (
            left.is_aleph()
            and left.aleph_index() == 1
            and right.is_uncountable()
        ):
            return True

        if isinstance(right_expression, _PowerCardinal):
            if self.le(left, right_expression.base):
                return True
            if self.le(cardinal(2), right_expression.base) and self.le(
                left, right_expression.exponent
            ):
                return True
            if isinstance(left_expression, _PowerCardinal):
                return self.le(left_expression.base, right_expression.base) and self.le(
                    left_expression.exponent,
                    right_expression.exponent,
                )
        return False

    def lt(
        self,
        source: Cardinal | CardinalScalar,
        target: Cardinal | CardinalScalar,
    ) -> bool:
        r"""Return whether the represented theory proves ``source < target``."""
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return False

        left_expression = left.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _SupremumCardinal):
            return all(self.lt(term, right) for term in left_expression.terms)
        if isinstance(right_expression, _SupremumCardinal):
            return any(self.lt(left, term) for term in right_expression.terms)
        if left.is_finite():
            if right.is_finite():
                return left.finite_value() < right.finite_value()
            return True
        if right.is_finite():
            return False
        if left.is_aleph() and right.is_aleph():
            return left.aleph_index() < right.aleph_index()
        if left.is_countably_infinite() and right.is_uncountable():
            return True
        if isinstance(right_expression, _PowerCardinal):
            return self.le(cardinal(2), right_expression.base) and self.le(
                left, right_expression.exponent
            )
        return False

    def ge(
        self,
        source: Cardinal | CardinalScalar,
        target: Cardinal | CardinalScalar,
    ) -> bool:
        return self.le(target, source)

    def gt(
        self,
        source: Cardinal | CardinalScalar,
        target: Cardinal | CardinalScalar,
    ) -> bool:
        return self.lt(target, source)

    def compare(
        self,
        source: Cardinal | CardinalScalar,
        target: Cardinal | CardinalScalar,
    ) -> CardinalComparison:
        r"""Compare two objects using only provable cardinal inequalities."""
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return CardinalComparison.EQUAL
        if self.lt(left, right):
            return CardinalComparison.LESS
        if self.lt(right, left):
            return CardinalComparison.GREATER
        if self.le(left, right):
            return CardinalComparison.LESS_OR_EQUAL
        if self.le(right, left):
            return CardinalComparison.GREATER_OR_EQUAL
        return CardinalComparison.INCOMPARABLE

    def are_incomparable(
        self,
        source: Cardinal | CardinalScalar,
        target: Cardinal | CardinalScalar,
    ) -> bool:
        return not self.le(source, target) and not self.le(target, source)

    def hom(
        self,
        source: Cardinal,
        target: Cardinal,
    ) -> CardinalityHomset:
        homset = Hom(source, target, self)
        assert isinstance(homset, CardinalityHomset)
        return homset


    class ParentMethods:
        r"""A cardinal: an object of :class:`Cardinalities`, and the set of
        that size.

        The expression is the one datum this level introduces.  Every answer
        below reads it.
        """

        def __init__(
            self, expression: _CardinalExpression, **rest: ConstructionData
        ) -> None:
            self._expression = expression
            super().__init__(**rest)

        def cardinality(self) -> Cardinal:
            r"""Return $|\kappa|$, which is $\kappa$.

            A cardinal is an initial ordinal, and the size of that set is the
            cardinal itself.  The set level asks the construction for a size,
            and this level is the one place where the answer is the object.
            """
            return self

        def expression(self) -> _CardinalExpression:
            return self._expression

        def sort_key(self) -> tuple[int, str]:
            expression = self.expression()
            if isinstance(expression, _FiniteCardinal):
                return (0, str(expression.value))
            if isinstance(expression, _AlephCardinal):
                return (1, str(expression.index))
            if isinstance(expression, _PowerCardinal):
                return (2, repr(self))
            return (3, repr(self))

        def _repr_(self) -> str:
            expression = self.expression()
            if isinstance(expression, _FiniteCardinal):
                return repr(expression.value)
            if isinstance(expression, _AlephCardinal):
                return f"\N{HEBREW LETTER ALEF}_{expression.index}"
            if isinstance(expression, _PowerCardinal):
                return f"({expression.base})^({expression.exponent})"
            return "sup(" + ", ".join(map(str, expression.terms)) + ")"

        def __hash__(self) -> int:
            if self.is_finite():
                return hash(self.finite_value())
            if self.is_countably_infinite():
                return hash(Infinity)
            return hash(self.expression())

        def __eq__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> bool:
            return self.expression() == cardinal(other).expression()

        def __ne__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> bool:
            return not self.__eq__(other)

        def __lt__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> bool:
            return Cardinalities().lt(self, other)

        def __le__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> bool:
            return Cardinalities().le(self, other)

        def __gt__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> bool:
            return Cardinalities().gt(self, other)

        def __ge__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> bool:
            return Cardinalities().ge(self, other)

        def __add__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> Cardinal:
            return Cardinalities().sum(self, other)

        def __radd__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> Cardinal:
            return self.__add__(other)

        def __mul__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> Cardinal:
            return Cardinalities().product(self, other)

        def __rmul__(
            self,
            other: Cardinal | CardinalScalar,
        ) -> Cardinal:
            return self.__mul__(other)

        def __pow__(
            self,
            exponent: Cardinal | CardinalScalar,
        ) -> Cardinal:
            return Cardinalities().power(self, exponent)

        def __rpow__(
            self,
            base: Cardinal | CardinalScalar,
        ) -> Cardinal:
            return Cardinalities().power(base, self)

        def is_finite(self) -> bool:
            return isinstance(self.expression(), _FiniteCardinal)

        def is_infinite(self) -> bool:
            return not self.is_finite()

        def is_aleph(self) -> bool:
            return isinstance(self.expression(), _AlephCardinal)

        def is_continuum(self) -> bool:
            expression = self.expression()
            return bool(
                isinstance(expression, _PowerCardinal)
                and expression.base == 2
                and expression.exponent.is_countably_infinite()
            )

        def is_countable(self) -> bool:
            return self.is_finite() or self.is_countably_infinite()

        def is_uncountable(self) -> bool:
            if self.is_finite() or self.is_countably_infinite():
                return False
            expression = self.expression()
            if isinstance(expression, _SupremumCardinal):
                return any(term.is_uncountable() for term in expression.terms)
            return True

        def is_countably_infinite(self) -> bool:
            expression = self.expression()
            return bool(
                isinstance(expression, _AlephCardinal)
                and expression.index == 0
            )

        def is_uncountably_infinite(self) -> bool:
            return self.is_infinite() and self.is_uncountable()

        def aleph_index(self) -> Ordinal:
            expression = self.expression()
            assert isinstance(expression, _AlephCardinal), (
                f"{self} is not an aleph cardinal"
            )
            return expression.index

        def initial_ordinal(self) -> Ordinal:
            r"""Return the initial ordinal represented by this aleph cardinal."""
            from dzack_research.preamble.categories.sets.ordinals import omega

            return omega(self.aleph_index())

        def finite_value(self) -> Integer:
            expression = self.expression()
            assert isinstance(expression, _FiniteCardinal), (
                f"{self} is not a finite cardinal"
            )
            return expression.value

        def __int__(self) -> int:
            if not self.is_finite():
                raise TypeError(f"cannot convert infinite cardinal {self} to integer")
            return int(self.finite_value())

        def __index__(self) -> int:
            if not self.is_finite():
                raise TypeError(
                    f"cannot convert infinite cardinal {self} to integer index"
                )
            return int(self.finite_value())

        def _integer_(self, ring: Ring | None = None) -> Integer:
            if not self.is_finite():
                raise TypeError(
                    f"cannot convert infinite cardinal {self} to Sage Integer"
                )
            return self.finite_value()

        def _rational_(self) -> Rational:
            if not self.is_finite():
                raise TypeError(
                    f"cannot convert infinite cardinal {self} to Sage Rational"
                )
            return QQ(self.finite_value())

        def _Hom_(
            self,
            codomain: Cardinal,
            category: Category | None = None,
        ) -> CardinalityHomset:
            assert isinstance(codomain, Cardinal), (
                "a cardinality morphism has cardinal objects at both ends"
            )
            assert category is None or category == Cardinalities(), (
                "the requested hom-set is not in Cardinalities"
            )
            return CardinalityHomset(self, codomain)


Cardinal = Cardinalities.ParentMethods
r"""The class of a cardinal object.

The category is the class, so the implementation class of
:class:`Cardinalities` is what an ``isinstance`` question and a type
annotation both name.  A cardinal is built by :func:`cardinal` or
:func:`aleph`.
"""


# A homset is a parent whose elements are its morphisms.  The runtime class
# is a Cython extension type and cannot be subscripted at class-creation
# time, so the binding goes through an alias, per the note in
# ``typings/sage/structure/parent.pyi``.
if TYPE_CHECKING:
    CardinalityHomsetBase = Homset[Cardinal, Cardinal]
else:
    CardinalityHomsetBase = Homset


class CardinalityHomset(CardinalityHomsetBase):
    r"""The empty or singleton hom-set between two cardinal objects."""

    def __init__(self, source: Cardinal, target: Cardinal) -> None:
        Homset.__init__(self, source, target, category=Cardinalities())

    def _repr_(self) -> str:
        return f"Hom({self.domain()}, {self.codomain()}) in Cardinalities"

    def __bool__(self) -> bool:
        return Cardinalities().le(self.domain(), self.codomain())

    def __len__(self) -> int:
        return 1 if self else 0

    def cardinality(self) -> Integer:
        return ZZ(len(self))

    def is_finite(self) -> bool:
        return True

    def __iter__(self) -> Iterator[CardinalityMorphism]:
        if self:
            yield self.unique_morphism()

    def __contains__(self, candidate: Morphism) -> bool:
        return (
            isinstance(candidate, CardinalityMorphism)
            and candidate.parent() is self
        )

    @cached_method
    def unique_morphism(self) -> CardinalityMorphism:
        assert self, (
            f"there is no cardinality morphism {self.domain()} -> {self.codomain()}"
        )
        return CardinalityMorphism(self)

    def _an_element_(self) -> CardinalityMorphism:
        return self.unique_morphism()

    def _element_constructor_(
        self,
        morphism: CardinalityMorphism | None = None,
    ) -> CardinalityMorphism:
        assert morphism is None or morphism in self, (
            f"{morphism} is not in {self}"
        )
        return self.unique_morphism()

    def identity(self) -> CardinalityMorphism:
        assert self.is_endomorphism_set(), (
            "identity is defined only for an endomorphism set"
        )
        return self.unique_morphism()


class CardinalityMorphism(Morphism):
    r"""The unique morphism witnessing one represented cardinal inequality."""

    def __init__(self, parent: CardinalityHomset) -> None:
        Morphism.__init__(self, parent)

    def _repr_(self) -> str:
        return f"{self.domain()} <= {self.codomain()}"

    def _composition_(
        self,
        right: Morphism,
        homset: Homset[Cardinal, Cardinal],
    ) -> CardinalityMorphism:
        assert isinstance(right, CardinalityMorphism)
        assert isinstance(homset, CardinalityHomset)
        return homset.unique_morphism()


@cached_function
def _cardinal_with_expression(expression: _CardinalExpression) -> Cardinal:
    r"""Return the one object of ``Cardinalities`` with this expression.

    Equal expressions give one object.  The expressions are frozen data
    classes, so equality is by value and the cache is keyed by the
    mathematics rather than by who asked first.
    """
    cardinal_number: Cardinal = object_of(Cardinalities(), expression=expression)
    return cardinal_number


def cardinal(value: Cardinal | CardinalScalar) -> Cardinal:
    r"""Return a cardinal object.

    Cardinal arithmetic is closed over counts: the value must be a
    ``Cardinal``, an integer, or ``Infinity`` (read as ``aleph_0``).  There
    is no scalar action of a larger ring on the cardinals — a rational
    times a cardinal does not typecheck mathematically.  Formulas that mix
    a finite-or-infinite count into scalar arithmetic (the determinant law
    ``|det L| = |det O| * [O : L]^2``) live in the extended scalars
    ``ZZ ∪ {oo}`` and consume the extended-scalar spelling (``index()``),
    never a cardinal.
    """
    if isinstance(value, Cardinal):
        return value
    assert value == Infinity or value in ZZ, (
        f"a cardinal is a count (a Cardinal, an integer, or oo); found the "
        f"non-count scalar {value!r} — extended-scalar formulas consume the "
        f"extended-scalar spelling (index()) instead"
    )
    if not isinstance(value, (Integer, int)) and value == Infinity:
        return aleph(0)
    finite_value = ZZ(value)
    assert finite_value >= 0, (
        f"a cardinal is a nonnegative integer; found {finite_value}"
    )
    return _cardinal_with_expression(_FiniteCardinal(finite_value))


def aleph(index: OrdinalInput) -> Cardinal:
    r"""Return the ``index``-th infinite initial cardinal."""
    from dzack_research.preamble.categories.sets.ordinals import ordinal

    return _cardinal_with_expression(_AlephCardinal(ordinal(index)))


aleph0 = aleph(0)
r"""The first infinite cardinal."""

continuum = cardinal(2) ** aleph0
r"""The cardinal ``2^aleph_0``."""
