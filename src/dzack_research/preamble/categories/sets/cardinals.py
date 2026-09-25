r"""Cardinal and ordinal arithmetic in the owned set-theoretic number hierarchy.

A cardinal is an object of :class:`Cardinalities` whose defining datum is a
term of cardinal arithmetic, and an ordinal is an object of :class:`Ordinals`
whose defining datum is a term of ordinal arithmetic.  Each term form
answers the structural questions about itself -- whether it is finite, how it
is displayed, which law of exponentiation or comparison applies to it -- so
an operation asks the datum and never inspects which form it has.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import SupportsInt, TypeVar

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.rings.infinity import AnInfinity, Infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
)
from dzack_research.preamble.owned_category import _object_of

IndexT = TypeVar("IndexT")


def _is_session_integer(value) -> bool:
    r"""Whether ``value`` is an exact integer: a Python ``int`` or an element of the owned ``ZZ``.

    The session's integer literals are owned integers, which Sage's ``ZZ``
    neither contains nor converts, so the owned ring is asked about them.  A
    Python ``int`` is answered first, without the owned ring, because this
    module names finite cardinals while the owned integers are still being
    built.
    """
    if value in ZZ:
        return True
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    return value in _own_ring(ZZ)


class _CardinalExpression(ABC):
    r"""A term of cardinal arithmetic, the defining datum of a cardinal.

    The forms are a finite cardinal ``n``, an aleph ``aleph_alpha``, a power
    ``kappa^lambda`` with infinite exponent, a finite supremum of terms that
    are not otherwise compared, and an indexed sum or product over an infinite
    index set.  The last two are not normal forms: they are not evaluated to
    any of the others, so neither their finiteness nor their order is decided
    here.

    The defaults below are the answers of the forms that do not override
    them.
    """

    @abstractmethod
    def display(self) -> str:
        r"""The notation of this term."""
        ...

    @abstractmethod
    def sort_key(self) -> tuple[int, str]:
        r"""The key ordering terms by form, then by notation."""
        ...

    def is_normal_form(self) -> bool:
        r"""Whether this term has a known finite-or-infinite classification."""
        return True

    def is_finite(self) -> bool:
        return False

    def is_aleph(self) -> bool:
        return False

    def is_countably_infinite(self) -> bool:
        return False

    def is_continuum(self) -> bool:
        return False

    def supremum_terms(self, cardinal_number: Cardinal) -> tuple[Cardinal, ...]:
        r"""The terms whose supremum ``cardinal_number`` is: itself alone."""
        return (cardinal_number,)

    def power_with_this_exponent(
        self,
        base: Cardinal,
        exponent: Cardinal,
    ) -> Cardinal:
        r"""``base^exponent`` for this term as the infinite exponent: the base decides."""
        return base.expression().power_with_this_base(base, exponent)

    def power_with_this_base(
        self,
        base: Cardinal,
        exponent: Cardinal,
    ) -> Cardinal:
        r"""``base^exponent`` for this term as the base: no law reduces it."""
        return _cardinal_with_expression(_PowerCardinal(base, exponent))

    def bounds_above(self, cardinal_number: Cardinal) -> bool:
        r"""Whether a law of this term's form shows ``cardinal_number <= self``: none does."""
        return False

    def strictly_bounds_above(self, cardinal_number: Cardinal) -> bool:
        r"""Whether a law of this term's form shows ``cardinal_number < self``: none does."""
        return False

    def is_componentwise_below(self, power: _PowerCardinal) -> bool:
        r"""Whether this term is a power below ``power`` in base and exponent: it is not a power."""
        return False


@dataclass(frozen=True)
class _FiniteCardinal(_CardinalExpression):
    value: int

    def display(self) -> str:
        return repr(self.value)

    def sort_key(self) -> tuple[int, str]:
        return (0, str(self.value))

    def is_finite(self) -> bool:
        return True


@dataclass(frozen=True)
class _AlephCardinal(_CardinalExpression):
    index: Ordinal

    def display(self) -> str:
        return f"ℵ_{self.index}"

    def sort_key(self) -> tuple[int, str]:
        return (1, str(self.index))

    def is_aleph(self) -> bool:
        return True

    def is_countably_infinite(self) -> bool:
        return self.index == 0


@dataclass(frozen=True)
class _PowerCardinal(_CardinalExpression):
    r"""``base^exponent`` with an infinite exponent and a base of at least two."""

    base: Cardinal
    exponent: Cardinal

    def display(self) -> str:
        return f"({self.base})^({self.exponent})"

    def sort_key(self) -> tuple[int, str]:
        return (2, self.display())

    def is_continuum(self) -> bool:
        return self.base == 2 and self.exponent.is_countably_infinite()

    def power_with_this_base(
        self,
        base: Cardinal,
        exponent: Cardinal,
    ) -> Cardinal:
        r"""``(kappa^lambda)^mu = kappa^(lambda mu)``."""
        cardinalities = Cardinalities()
        return cardinalities.power(
            self.base,
            cardinalities.product(self.exponent, exponent),
        )

    def bounds_above(self, cardinal_number: Cardinal) -> bool:
        r"""Decide ``cardinal_number <= kappa^lambda`` by the laws of exponentiation.

        ``nu <= kappa`` gives ``nu <= kappa^lambda`` since ``lambda >= 1``;
        ``2 <= kappa`` and ``nu <= lambda`` give ``nu < 2^lambda <= kappa^lambda``;
        a power ``rho^sigma`` with ``rho <= kappa`` and ``sigma <= lambda`` is
        below ``kappa^lambda`` by monotonicity.
        """
        cardinalities = Cardinalities()
        if cardinalities.le(cardinal_number, self.base):
            return True
        if cardinalities.le(2, self.base) and cardinalities.le(cardinal_number, self.exponent):
            return True
        return cardinal_number.expression().is_componentwise_below(self)

    def strictly_bounds_above(self, cardinal_number: Cardinal) -> bool:
        r"""Decide ``cardinal_number < kappa^lambda`` by Cantor's theorem: ``nu <= lambda < 2^lambda <= kappa^lambda``."""
        cardinalities = Cardinalities()
        return cardinalities.le(2, self.base) and cardinalities.le(cardinal_number, self.exponent)

    def is_componentwise_below(self, power: _PowerCardinal) -> bool:
        cardinalities = Cardinalities()
        return cardinalities.le(self.base, power.base) and cardinalities.le(self.exponent, power.exponent)


@dataclass(frozen=True)
class _SupremumCardinal(_CardinalExpression):
    r"""The supremum of finitely many pairwise undecided terms, none a supremum."""

    terms: tuple[Cardinal, ...]

    def display(self) -> str:
        return "sup(" + ", ".join(map(str, self.terms)) + ")"

    def sort_key(self) -> tuple[int, str]:
        return (3, self.display())

    def supremum_terms(self, cardinal_number: Cardinal) -> tuple[Cardinal, ...]:
        return self.terms

    def power_with_this_exponent(
        self,
        base: Cardinal,
        exponent: Cardinal,
    ) -> Cardinal:
        r"""``kappa^(max_i lambda_i) = max_i kappa^(lambda_i)`` for finitely many ``lambda_i``."""
        cardinalities = Cardinalities()
        return cardinalities.supremum(*(cardinalities.power(base, term) for term in self.terms))

    def power_with_this_base(
        self,
        base: Cardinal,
        exponent: Cardinal,
    ) -> Cardinal:
        r"""``(max_i kappa_i)^lambda = max_i kappa_i^lambda`` for finitely many ``kappa_i``."""
        cardinalities = Cardinalities()
        return cardinalities.supremum(*(cardinalities.power(term, exponent) for term in self.terms))


@dataclass(frozen=True)
class _IndexedSumCardinal(_CardinalExpression):
    r"""``sum_{i in I} kappa_i`` over an infinite index set, not evaluated."""

    index_set: Parent
    summands: Callable

    def display(self) -> str:
        return f"sum_{{i in {self.index_set}}} kappa_i"

    def sort_key(self) -> tuple[int, str]:
        return (4, self.display())

    def is_normal_form(self) -> bool:
        return False


@dataclass(frozen=True)
class _IndexedProductCardinal(_CardinalExpression):
    r"""``prod_{i in I} kappa_i`` over an infinite index set, not evaluated."""

    index_set: Parent
    factors: Callable

    def display(self) -> str:
        return f"prod_{{i in {self.index_set}}} kappa_i"

    def sort_key(self) -> tuple[int, str]:
        return (4, self.display())

    def is_normal_form(self) -> bool:
        return False


class CardinalComparison(Enum):
    LESS = -1
    EQUAL = 0
    GREATER = 1
    LESS_OR_EQUAL = 2
    GREATER_OR_EQUAL = 3
    INCOMPARABLE = 4


class CardinalityMorphism(Morphism):
    def __init__(self, parent: CardinalityMor) -> None:
        Morphism.__init__(self, parent)

    def is_identity(self) -> bool:
        return self.domain() is self.codomain()

    def __mul__(self, other):
        r"""Compose ``self ∘ other``.

        The right operand is arbitrary, which is Python's binary-operator
        protocol: like ``__eq__``, this decides about anything and answers
        ``NotImplemented`` for what is not a composable order arrow.
        """
        other_parent = element_parent(other)
        match other_parent:
            case CategoricalMor() if (
                other_parent.mor_category().is_subcategory(Cardinalities())
                and other.codomain() is self.domain()
            ):
                pass
            case _:
                return NotImplemented
        return Cardinalities().Mor(other.domain(), self.codomain()).unique_morphism()

    def _repr_(self) -> str:
        return f"{self.domain()} <= {self.codomain()}"


class CardinalityMor(CategoricalMor):
    Element = CardinalityMorphism

    def __init__(
        self,
        mor_family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    def is_empty(self):
        r"""The cardinal-order Mor is empty exactly when its source exceeds its target.

        The comparison owner proves some inequalities and leaves others
        undecided.  Failure to prove an inequality is not its negation.
        """
        cardinals = Cardinalities()
        match (cardinals.le(self.domain(), self.codomain()), cardinals.lt(self.codomain(), self.domain())):
            case (True, _):
                return False
            case (_, True):
                return True
            case _:
                return Unknown

    def cardinality(self) -> Cardinal:
        r"""Zero or one when the cardinal comparison decides the Mor's emptiness."""
        empty = self.is_empty()
        assert empty is not Unknown, (
            f"cannot compute the cardinality of {self}: it is undecided whether {self.domain()} <= "
            f"{self.codomain()}, so it is undecided whether this set of morphisms is empty"
        )
        return cardinal(0 if empty else 1)

    @cached_method
    def unique_morphism(self) -> CardinalityMorphism:
        empty = self.is_empty()
        if empty is True:
            raise ValueError(
                f"there is no morphism {self.domain()} -> {self.codomain()} of cardinals: "
                f"{self.domain()} is not <= {self.codomain()}"
            )
        assert empty is False, (
            f"cannot give the morphism {self.domain()} -> {self.codomain()} of cardinals: it is "
            f"undecided whether {self.domain()} <= {self.codomain()}"
        )
        return self.element_class(self)

    def _element_constructor_(self, morphism=None):
        if morphism is not None and morphism.parent() is not self:
            raise ValueError(f"{morphism} is not in {self}")
        return self.unique_morphism()

    def identity(self) -> CardinalityMorphism:
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        return self.unique_morphism()


class CardinalityMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self) -> type[CardinalityMor]:
        return CardinalityMor


class Cardinalities(OwnedCategory):
    r"""The thin category associated to the represented cardinal order."""

    def an_object(self) -> Cardinal:
        r"""The cardinal three."""
        return cardinal(3)

    _MorCategory = CardinalityMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    def _repr_(self) -> str:
        return "Card: cardinalities with a unique morphism kappa -> lambda exactly when kappa <= lambda"

    def _call_(self, value: SupportsInt | AnInfinity) -> Cardinal:
        r"""Construct the cardinal a literal names.

        The literal ingress of this category's one construction, reached
        through ``Cardinalities()(value)`` once ``value`` is not already a
        cardinal: Sage's ``Infinity`` names ``aleph_0``, and an exact
        nonnegative integer names the finite cardinal.  Anything else is
        refused by the construction, not caught.
        """
        if value is Infinity:
            return aleph(0)
        integer = int(value)
        if value != integer:
            raise TypeError(
                f"a finite cardinal is given by an integer, but {value!r} is not an integer"
            )
        if integer < 0:
            raise ValueError(f"a cardinal is nonnegative, but {integer} is negative")
        return _cardinal_with_expression(_FiniteCardinal(integer))

    def Mor(
        self,
        domain: Cardinal | SupportsInt | AnInfinity,
        codomain: Cardinal | SupportsInt | AnInfinity,
    ) -> CardinalityMor:
        return CardinalityMorCategoryConstruction(self).Of(cardinal(domain), cardinal(codomain))

    class ParentMethods:
        def __init__(self, expression: _CardinalExpression, **rest) -> None:
            self._expression = expression
            super().__init__(**rest)

        def expression(self) -> _CardinalExpression:
            return self._expression

        def cardinality(self) -> Cardinal:
            r"""``|kappa| = kappa``.

            Under the von Neumann assignment a cardinal is the initial ordinal
            of its size, a set whose cardinality is that cardinal.
            """
            return self

        def sort_key(self) -> tuple[int, str]:
            return self.expression().sort_key()

        def _repr_(self) -> str:
            return self.expression().display()

        def __hash__(self) -> int:
            if self.is_finite():
                return hash(self._finite_int())
            if self.is_countably_infinite():
                return hash(Infinity)
            return hash(self.expression())

        def __eq__(self, other) -> bool:
            r"""Equality of the defining terms, with a literal read as the cardinal it names."""
            match other:
                case _ if other in Cardinalities():
                    return self.expression() == other.expression()
                case _ if other is Infinity:
                    return self.expression() == Cardinalities()(other).expression()
                case _ if _is_session_integer(other) and int(other) >= 0:
                    return self.expression() == Cardinalities()(other).expression()
                case _:
                    return False

        def __ne__(self, other) -> bool:
            return not self == other

        def __lt__(self, other) -> bool:
            return Cardinalities().lt(self, other)

        def __le__(self, other) -> bool:
            return Cardinalities().le(self, other)

        def __gt__(self, other) -> bool:
            return Cardinalities().gt(self, other)

        def __ge__(self, other) -> bool:
            return Cardinalities().ge(self, other)

        def __add__(self, other):
            return Cardinalities().sum(self, other)

        __radd__ = __add__

        def __mul__(self, other):
            return Cardinalities().product(self, other)

        __rmul__ = __mul__

        def __pow__(self, exponent):
            return Cardinalities().power(self, exponent)

        def __rpow__(self, base):
            return Cardinalities().power(base, self)

        def is_finite(self) -> bool:
            expression = self.expression()
            assert expression.is_normal_form(), (
                f"cannot decide whether the cardinal {self} is finite: it is not a finite sum, product, or "
                "supremum of known cardinals"
            )
            return expression.is_finite()

        def is_infinite(self) -> bool:
            return not self.is_finite()

        def is_aleph(self) -> bool:
            return self.expression().is_aleph()

        def is_continuum(self) -> bool:
            return self.expression().is_continuum()

        def is_countable(self) -> bool:
            return self.is_finite() or self.is_countably_infinite()

        def is_uncountable(self) -> bool:
            r"""Whether ``kappa > aleph_0``.

            A countable cardinal is not; an aleph beyond ``aleph_0`` and a
            power ``kappa^lambda`` with infinite exponent are; a supremum is
            when one of its terms is.
            """
            expression = self.expression()
            assert expression.is_normal_form(), (
                f"cannot decide whether the cardinal {self} is uncountable: it is not a finite sum, product, "
                "or supremum of known cardinals"
            )
            if self.is_countable():
                return False
            return any(not term.is_countable() for term in expression.supremum_terms(self))

        def is_countably_infinite(self) -> bool:
            return self.expression().is_countably_infinite()

        def is_uncountably_infinite(self) -> bool:
            return self.is_infinite() and self.is_uncountable()

        def aleph_index(self) -> Ordinal:
            assert self.is_aleph(), f"{self} is not an aleph cardinal, so it has no aleph index"
            return self.expression().index

        def initial_ordinal(self) -> Ordinal:
            return omega(self.aleph_index())

        def _finite_int(self) -> int:
            assert self.is_finite(), f"{self} is not a finite cardinal"
            return self.expression().value

        def finite_value(self) -> int:
            r"""Return the ordinary nonnegative integer representing this finite cardinal."""
            return self._finite_int()

        def __int__(self) -> int:
            if not self.is_finite():
                raise TypeError(f"cannot convert infinite cardinal {self} to integer")
            return self._finite_int()

        def __index__(self) -> int:
            return int(self)

        def _integer_(self, ring=None):
            if not self.is_finite():
                raise TypeError(f"cannot convert infinite cardinal {self} to an integer")
            return ZZ(self._finite_int())

        def _rational_(self):
            if not self.is_finite():
                raise TypeError(f"cannot convert infinite cardinal {self} to a rational")
            from sage.rings.rational_field import QQ as SageQQ

            return SageQQ(self._finite_int())

        def Mor(
            self,
            codomain: Cardinal | SupportsInt | AnInfinity,
            category: Category | None = None,
        ) -> CardinalityMor:
            if category is not None and category is not Cardinalities():
                raise TypeError(
                    f"a morphism of cardinals lies in the category of cardinals, not in {category}"
                )
            return Cardinalities().Mor(self, codomain)

    def zero(self) -> Cardinal:
        return cardinal(0)

    def one(self) -> Cardinal:
        return cardinal(1)

    def sum(
        self,
        *summands: Cardinal | SupportsInt | AnInfinity,
    ) -> Cardinal:
        result = self.zero()
        for summand in map(cardinal, summands):
            if result.is_finite() and summand.is_finite():
                result = cardinal(result._finite_int() + summand._finite_int())
            elif result.is_finite():
                result = summand
            elif summand.is_infinite():
                result = self.supremum(result, summand)
        return result

    def product(
        self,
        *factors: Cardinal | SupportsInt | AnInfinity,
    ) -> Cardinal:
        result = self.one()
        for factor in map(cardinal, factors):
            if result == 0 or factor == 0:
                return cardinal(0)
            if result.is_finite() and factor.is_finite():
                result = cardinal(result._finite_int() * factor._finite_int())
            elif result.is_finite():
                result = factor
            elif factor.is_infinite():
                result = self.supremum(result, factor)
        return result

    def indexed_sum(
        self,
        index_set: Parent,
        summands: Callable[[IndexT], Cardinal | SupportsInt | AnInfinity],
    ) -> Cardinal:
        size = cardinal(index_set.cardinality())
        if size.is_finite():
            return self.sum(*(summands(index) for index in index_set))
        return _cardinal_with_expression(_IndexedSumCardinal(index_set, summands))

    def indexed_product(
        self,
        index_set: Parent,
        factors: Callable[[IndexT], Cardinal | SupportsInt | AnInfinity],
    ) -> Cardinal:
        size = cardinal(index_set.cardinality())
        if size.is_finite():
            return self.product(*(factors(index) for index in index_set))
        return _cardinal_with_expression(_IndexedProductCardinal(index_set, factors))

    def power(
        self,
        base: Cardinal | SupportsInt | AnInfinity,
        exponent: Cardinal | SupportsInt | AnInfinity,
    ) -> Cardinal:
        r"""``kappa^lambda``.

        With a finite exponent the power is computed or equals the infinite
        base.  With an infinite exponent ``lambda``, a base ``kappa`` with
        ``2 <= kappa <= lambda`` gives ``kappa^lambda = 2^lambda``, and the
        remaining reductions belong to the forms of the exponent and the base:
        a supremum distributes, and a power multiplies exponents.
        """
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
                return cardinal(cardinal_base._finite_int() ** cardinal_exponent._finite_int())
            return cardinal_base
        if cardinal_base.is_finite() or self.le(cardinal_base, cardinal_exponent):
            cardinal_base = cardinal(2)
        return cardinal_exponent.expression().power_with_this_exponent(cardinal_base, cardinal_exponent)

    def sum_morphism(
        self,
        *morphisms: CardinalityMorphism,
    ) -> CardinalityMorphism:
        r"""Apply cardinal addition to a finite family of comparison morphisms."""
        source = self.sum(*(morphism.domain() for morphism in morphisms))
        target = self.sum(*(morphism.codomain() for morphism in morphisms))
        return self.Mor(source, target).unique_morphism()

    def product_morphism(
        self,
        *morphisms: CardinalityMorphism,
    ) -> CardinalityMorphism:
        r"""Apply cardinal multiplication to a finite family of comparison morphisms."""
        source = self.product(*(morphism.domain() for morphism in morphisms))
        target = self.product(*(morphism.codomain() for morphism in morphisms))
        return self.Mor(source, target).unique_morphism()

    def power_morphism(
        self,
        base_morphism: CardinalityMorphism,
        exponent_morphism: CardinalityMorphism,
    ) -> CardinalityMorphism:
        r"""Apply exponentiation to comparisons when the source base is nonzero."""
        if not self.le(1, base_morphism.domain()):
            raise ValueError(
                f"exponentiation is monotone in the exponent only for a nonzero base, but the base "
                f"{base_morphism.domain()} may be zero"
            )
        source = self.power(
            base_morphism.domain(),
            exponent_morphism.domain(),
        )
        target = self.power(
            base_morphism.codomain(),
            exponent_morphism.codomain(),
        )
        return self.Mor(source, target).unique_morphism()

    def supremum(
        self,
        *cardinal_numbers: Cardinal | SupportsInt | AnInfinity,
    ) -> Cardinal:
        r"""The supremum of finitely many cardinals: the maximal terms, or their undecided supremum."""
        terms: list[Cardinal] = [
            term
            for cardinal_number in map(cardinal, cardinal_numbers)
            for term in cardinal_number.expression().supremum_terms(cardinal_number)
        ]
        assert terms, (
            "the supremum of finitely many cardinals needs at least one cardinal, but none was given"
        )
        maximal_terms: list[Cardinal] = []
        for candidate in sorted(set(terms), key=lambda term: term.sort_key()):
            if any(self.le(candidate, term) for term in maximal_terms):
                continue
            maximal_terms = [term for term in maximal_terms if not self.le(term, candidate)]
            maximal_terms.append(candidate)
        maximal_terms.sort(key=lambda term: term.sort_key())
        if len(maximal_terms) == 1:
            return maximal_terms[0]
        return _cardinal_with_expression(_SupremumCardinal(tuple(maximal_terms)))

    def le(
        self,
        source: Cardinal | SupportsInt | AnInfinity,
        target: Cardinal | SupportsInt | AnInfinity,
    ) -> bool:
        r"""Prove ``source <= target`` by the represented laws; ``False`` means no proof was found.

        A supremum is below ``target`` when each of its terms is, and
        ``source`` is below a supremum when it is below one of its terms.
        """
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return True
        return all(
            any(
                self._le_terms(left_term, right_term)
                for right_term in right.expression().supremum_terms(right)
            )
            for left_term in left.expression().supremum_terms(left)
        )

    def _le_terms(self, left: Cardinal, right: Cardinal) -> bool:
        r"""Decide ``left <= right`` for two cardinals, neither a supremum."""
        if left == right:
            return True
        if not (left.expression().is_normal_form() and right.expression().is_normal_form()):
            return False
        if left.is_finite():
            return not right.is_finite() or left._finite_int() <= right._finite_int()
        if right.is_finite():
            return False
        if left.is_aleph() and right.is_aleph():
            return left.aleph_index() <= right.aleph_index()
        if left.is_countably_infinite():
            return True
        if left.is_aleph() and left.aleph_index() == 1 and right.is_uncountable():
            return True
        return right.expression().bounds_above(left)

    def lt(
        self,
        source: Cardinal | SupportsInt | AnInfinity,
        target: Cardinal | SupportsInt | AnInfinity,
    ) -> bool:
        r"""Prove ``source < target`` by the represented laws; ``False`` means no proof was found."""
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return False
        return all(
            any(
                self._lt_terms(left_term, right_term)
                for right_term in right.expression().supremum_terms(right)
            )
            for left_term in left.expression().supremum_terms(left)
        )

    def _lt_terms(self, left: Cardinal, right: Cardinal) -> bool:
        r"""Decide ``left < right`` for two cardinals, neither a supremum."""
        if left == right:
            return False
        if not (left.expression().is_normal_form() and right.expression().is_normal_form()):
            return False
        if left.is_finite():
            return not right.is_finite() or left._finite_int() < right._finite_int()
        if right.is_finite():
            return False
        if left.is_aleph() and right.is_aleph():
            return left.aleph_index() < right.aleph_index()
        if left.is_countably_infinite() and right.is_uncountable():
            return True
        return right.expression().strictly_bounds_above(left)

    def ge(
        self,
        source: Cardinal | SupportsInt | AnInfinity,
        target: Cardinal | SupportsInt | AnInfinity,
    ) -> bool:
        return self.le(target, source)

    def gt(
        self,
        source: Cardinal | SupportsInt | AnInfinity,
        target: Cardinal | SupportsInt | AnInfinity,
    ) -> bool:
        return self.lt(target, source)

    def compare(
        self,
        source: Cardinal | SupportsInt | AnInfinity,
        target: Cardinal | SupportsInt | AnInfinity,
    ) -> CardinalComparison:
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
        source: Cardinal | SupportsInt | AnInfinity,
        target: Cardinal | SupportsInt | AnInfinity,
    ) -> bool:
        return not self.le(source, target) and not self.le(target, source)


Cardinal = Cardinalities().ObjectType


class _OrdinalExpression(ABC):
    r"""A term of ordinal arithmetic, the defining datum of an ordinal.

    The forms are a finite ordinal, an initial ordinal ``omega_alpha``, the
    natural (Hessenberg) sum and product of several terms, and the ordinal sum,
    product and power of two.  The defaults below are the answers of the forms
    that do not override them.
    """

    @abstractmethod
    def display(self) -> str:
        r"""The notation of this term."""
        ...

    @abstractmethod
    def denoted_cardinality(self) -> Cardinal:
        r"""``|alpha|`` for the ordinal this term denotes."""
        ...

    def is_finite(self) -> bool:
        return False

    def is_initial(self) -> bool:
        return False

    def natural_sum_terms(self, ordinal_number: Ordinal) -> tuple[Ordinal, ...]:
        r"""The terms whose natural sum ``ordinal_number`` is: itself alone."""
        return (ordinal_number,)

    def natural_product_factors(self, ordinal_number: Ordinal) -> tuple[Ordinal, ...]:
        r"""The factors whose natural product ``ordinal_number`` is: itself alone."""
        return (ordinal_number,)



@dataclass(frozen=True)
class _FiniteOrdinal(_OrdinalExpression):
    value: Integer

    def display(self) -> str:
        return repr(self.value)

    def denoted_cardinality(self) -> Cardinal:
        return cardinal(self.value)

    def is_finite(self) -> bool:
        return True


@dataclass(frozen=True)
class _InitialOrdinal(_OrdinalExpression):
    index: Ordinal

    def display(self) -> str:
        return f"ω_{self.index}"

    def denoted_cardinality(self) -> Cardinal:
        r"""``|omega_alpha| = aleph_alpha``."""
        return aleph(self.index)

    def is_initial(self) -> bool:
        return True


@dataclass(frozen=True)
class _NaturalSum(_OrdinalExpression):
    terms: tuple[Ordinal, ...]

    def display(self) -> str:
        return " # ".join(map(repr, self.terms))

    def denoted_cardinality(self) -> Cardinal:
        return Cardinalities().sum(*(term.cardinality() for term in self.terms))

    def natural_sum_terms(self, ordinal_number: Ordinal) -> tuple[Ordinal, ...]:
        return self.terms



@dataclass(frozen=True)
class _NaturalProduct(_OrdinalExpression):
    factors: tuple[Ordinal, ...]

    def display(self) -> str:
        return " ⊗ ".join(map(repr, self.factors))

    def denoted_cardinality(self) -> Cardinal:
        return Cardinalities().product(*(factor.cardinality() for factor in self.factors))

    def natural_product_factors(self, ordinal_number: Ordinal) -> tuple[Ordinal, ...]:
        return self.factors


@dataclass(frozen=True)
class _OrdinalSum(_OrdinalExpression):
    left: Ordinal
    right: Ordinal

    def display(self) -> str:
        return f"({self.left} +o {self.right})"

    def denoted_cardinality(self) -> Cardinal:
        r"""``|alpha + beta| = |alpha| + |beta|``."""
        return Cardinalities().sum(self.left.cardinality(), self.right.cardinality())


@dataclass(frozen=True)
class _OrdinalProduct(_OrdinalExpression):
    left: Ordinal
    right: Ordinal

    def display(self) -> str:
        return f"({self.left} *o {self.right})"

    def denoted_cardinality(self) -> Cardinal:
        r"""``|alpha beta| = |alpha| |beta|``."""
        return Cardinalities().product(self.left.cardinality(), self.right.cardinality())


@dataclass(frozen=True)
class _OrdinalPower(_OrdinalExpression):
    r"""``base^exponent`` with ``base >= 2``, ``exponent >= 1``, one of them infinite."""

    base: Ordinal
    exponent: Ordinal

    def display(self) -> str:
        return f"({self.base} ^o {self.exponent})"

    def denoted_cardinality(self) -> Cardinal:
        r"""``|alpha^beta| = max(|alpha|, |beta|)`` for ``alpha >= 2``, ``beta >= 1``, one infinite.

        Ordinal exponentiation is continuous in the exponent, so
        ``alpha^beta = sup_{gamma < beta} alpha^gamma`` at a limit ``beta``,
        and induction on ``beta`` bounds ``|alpha^beta|`` by
        ``max(|alpha|, |beta|)``; ``alpha^beta >= alpha`` and
        ``alpha^beta >= beta`` give the other inequality.  It is not the
        cardinal power: ``2^omega = omega`` is countable.
        """
        return Cardinalities().supremum(self.base.cardinality(), self.exponent.cardinality())


class OrdinalMorphism(Morphism):
    r"""The unique comparison arrow ``alpha -> beta`` when ``alpha <= beta``."""

    def __init__(self, parent: OrdinalMor) -> None:
        Morphism.__init__(self, parent)

    def is_identity(self) -> bool:
        return self.domain() is self.codomain()

    def __mul__(self, other):
        r"""Compose two ordinal comparisons."""
        other_parent = element_parent(other)
        match other_parent:
            case CategoricalMor() if (
                other_parent.mor_category().is_subcategory(Ordinals())
                and other.codomain() is self.domain()
            ):
                pass
            case _:
                return NotImplemented
        return Ordinals().Mor(other.domain(), self.codomain()).unique_morphism()

    def _repr_(self) -> str:
        return f"{self.domain()} <= {self.codomain()}"


class OrdinalMor(CategoricalMor):
    r"""The zero-or-one-element Mor object of the ordinal order."""

    Element = OrdinalMorphism

    def __init__(
        self,
        mor_family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    def is_empty(self):
        comparison = Ordinals().le(self.domain(), self.codomain())
        if comparison is True:
            return False
        reverse = Ordinals().le(self.codomain(), self.domain())
        if reverse is True:
            return True
        return Unknown

    def cardinality(self) -> Cardinal:
        empty = self.is_empty()
        assert empty is not Unknown, (
            f"cannot compute the cardinality of {self}: it is undecided whether {self.domain()} <= "
            f"{self.codomain()}, so it is undecided whether this set of morphisms is empty"
        )
        return cardinal(0 if empty else 1)

    @cached_method
    def unique_morphism(self) -> OrdinalMorphism:
        empty = self.is_empty()
        if empty is True:
            raise ValueError(
                f"there is no morphism {self.domain()} -> {self.codomain()} of ordinals: "
                f"{self.domain()} is not <= {self.codomain()}"
            )
        assert empty is False, (
            f"cannot give the morphism {self.domain()} -> {self.codomain()} of ordinals: it is "
            f"undecided whether {self.domain()} <= {self.codomain()}"
        )
        return self.element_class(self)

    def _element_constructor_(self, morphism=None):
        if morphism is not None and morphism.parent() is not self:
            raise ValueError(f"{morphism} is not in {self}")
        return self.unique_morphism()

    def identity(self) -> OrdinalMorphism:
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        return self.unique_morphism()


class OrdinalMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self) -> type[OrdinalMor]:
        return OrdinalMor


class Ordinals(OwnedCategory):
    r"""The thin category ``Ord`` of represented ordinals under ``<=``.

    Ordinals are objects, not elements of a distinguished semiring object.
    Natural (Hessenberg) sum and product are the commutative-semiring
    operations on these objects.  Ordinary ordinal sum, product and power
    remain object operations because they are not that commutative semiring
    structure.
    """

    _MorCategory = OrdinalMorCategoryConstruction

    def an_object(self) -> Ordinal:
        return self(3)

    def super_categories(self):
        return [Objects()]

    def _repr_(self) -> str:
        return "Ord: ordinals with a unique morphism alpha -> beta exactly when alpha <= beta"

    def _call_(self, value: Ordinal | Cardinal | SupportsInt) -> Ordinal:
        if value in self:
            return value
        match value:
            case _ if value in Cardinalities():
                if not value.is_finite():
                    raise ValueError(
                        f"the cardinal {value} is not itself an ordinal in this literal ingress: only finite "
                        "cardinals identify canonically with their finite initial ordinals"
                    )
                integer = value.finite_value()
            case _ if _is_session_integer(value):
                integer = int(value)
            case _:
                raise ValueError(
                    f"{value!r} does not name an ordinal here: use an ordinal, a finite cardinal, or an exact "
                    "nonnegative integer"
                )
        if integer < 0:
            raise ValueError(f"an ordinal is nonnegative, but {integer} is negative")
        return _ordinal_with_expression(_FiniteOrdinal(ZZ(integer)))

    def from_expression(self, expression: _OrdinalExpression) -> Ordinal:
        return _ordinal_with_expression(expression)

    def Mor(
        self,
        domain: Ordinal | Cardinal | SupportsInt,
        codomain: Ordinal | Cardinal | SupportsInt,
    ) -> OrdinalMor:
        return OrdinalMorCategoryConstruction(self).Of(self(domain), self(codomain))

    class ParentMethods:
        def __init__(self, expression: _OrdinalExpression, **rest) -> None:
            self._expression = expression
            super().__init__(**rest)

        def expression(self) -> _OrdinalExpression:
            return self._expression

        def _repr_(self) -> str:
            return self.expression().display()

        def __hash__(self) -> int:
            if self.expression().is_finite():
                return hash(int(self.expression().value))
            return hash(self.expression())

        def __eq__(self, other) -> bool:
            r"""Equality of the defining terms, with finite literals read as their ordinals."""
            match other:
                case _ if other in Ordinals():
                    return self.expression() == other.expression()
                case _ if other in Cardinalities() and other.is_finite():
                    return self.expression() == Ordinals()(other).expression()
                case _ if _is_session_integer(other) and int(other) >= 0:
                    return self.expression() == Ordinals()(other).expression()
                case _:
                    return False

        def __ne__(self, other) -> bool:
            return not self == other

        def __le__(self, other):
            return Ordinals().le(self, other)

        def __lt__(self, other):
            return Ordinals().lt(self, other)

        def __ge__(self, other):
            return Ordinals().ge(self, other)

        def __gt__(self, other):
            return Ordinals().gt(self, other)

        def __add__(self, other):
            return Ordinals().natural_sum(self, other)

        def __radd__(self, other):
            return Ordinals().natural_sum(other, self)

        def __mul__(self, other):
            return Ordinals().natural_product(self, other)

        def __rmul__(self, other):
            return Ordinals().natural_product(other, self)

        def ordinal_sum(self, other: Ordinal | SupportsInt) -> Ordinal:
            right = Ordinals()(other)
            if self.expression().is_finite() and right.expression().is_finite():
                return Ordinals()(self.expression().value + right.expression().value)
            if right == 0:
                return self
            if self == 0:
                return right
            return Ordinals().from_expression(_OrdinalSum(self, right))

        def ordinal_product(self, other: Ordinal | SupportsInt) -> Ordinal:
            right = Ordinals()(other)
            if self.expression().is_finite() and right.expression().is_finite():
                return Ordinals()(self.expression().value * right.expression().value)
            if self == 0 or right == 0:
                return Ordinals().zero()
            if right == 1:
                return self
            if self == 1:
                return right
            return Ordinals().from_expression(_OrdinalProduct(self, right))

        def ordinal_power(self, exponent: Ordinal | SupportsInt) -> Ordinal:
            power = Ordinals()(exponent)
            if self.expression().is_finite() and power.expression().is_finite():
                return Ordinals()(self.expression().value ** power.expression().value)
            if power == 0:
                return Ordinals().one()
            if self == 0:
                return Ordinals().zero()
            if self == 1:
                return self
            return Ordinals().from_expression(_OrdinalPower(self, power))

        def is_initial(self) -> bool:
            return self.expression().is_initial()

        def initial_index(self) -> Ordinal:
            assert self.is_initial(), f"{self} is not an initial ordinal, so it has no initial index"
            return self.expression().index

        def cardinality(self) -> Cardinal:
            r"""``|alpha|``, the cardinality of the von Neumann ordinal ``alpha``."""
            return self.expression().denoted_cardinality()

        def Mor(
            self,
            codomain: Ordinal | Cardinal | SupportsInt,
            category: Category | None = None,
        ) -> OrdinalMor:
            if category is not None and category is not Ordinals():
                raise TypeError(
                    f"a morphism of ordinals lies in the category of ordinals, not in {category}"
                )
            return Ordinals().Mor(self, codomain)

    def zero(self) -> Ordinal:
        return self(0)

    def one(self) -> Ordinal:
        return self(1)

    def initial(self, index: Ordinal | SupportsInt) -> Ordinal:
        return self.from_expression(_InitialOrdinal(self(index)))

    def natural_sum(self, *summands) -> Ordinal:
        terms: list[Ordinal] = []
        finite_part = ZZ.zero()
        for summand in map(self, summands):
            expression = summand.expression()
            if expression.is_finite():
                finite_part += expression.value
            else:
                terms.extend(expression.natural_sum_terms(summand))
        if finite_part:
            terms.append(self(finite_part))
        if not terms:
            return self.zero()
        terms.sort(key=repr)
        if len(terms) == 1:
            return terms[0]
        return self.from_expression(_NaturalSum(tuple(terms)))

    def natural_product(self, *factors) -> Ordinal:
        r"""Distribute over a natural sum, otherwise multiply the factors directly."""
        normalized = tuple(map(self, factors))
        for position, factor in enumerate(normalized):
            terms = factor.expression().natural_sum_terms(factor)
            match terms:
                case (term,) if term is factor:
                    continue
                case _:
                    return self.natural_sum(*(
                        self.natural_product(*normalized[:position], term, *normalized[position + 1:])
                        for term in terms
                    ))
        return self._natural_product_without_sums(normalized)

    def _natural_product_without_sums(self, factors: tuple[Ordinal, ...]) -> Ordinal:
        normalized: list[Ordinal] = []
        finite_part = ZZ.one()
        for factor in factors:
            expression = factor.expression()
            if expression.is_finite():
                if expression.value == 0:
                    return self.zero()
                finite_part *= expression.value
            else:
                normalized.extend(expression.natural_product_factors(factor))
        if finite_part != 1 or not normalized:
            normalized.append(self(finite_part))
        normalized.sort(key=repr)
        if len(normalized) == 1:
            return normalized[0]
        return self.from_expression(_NaturalProduct(tuple(normalized)))

    def natural_sum_morphism(self, *morphisms: OrdinalMorphism) -> OrdinalMorphism:
        source = self.natural_sum(*(morphism.domain() for morphism in morphisms))
        target = self.natural_sum(*(morphism.codomain() for morphism in morphisms))
        return self.Mor(source, target).unique_morphism()

    def natural_product_morphism(self, *morphisms: OrdinalMorphism) -> OrdinalMorphism:
        source = self.natural_product(*(morphism.domain() for morphism in morphisms))
        target = self.natural_product(*(morphism.codomain() for morphism in morphisms))
        return self.Mor(source, target).unique_morphism()

    def le(
        self,
        left: Ordinal | Cardinal | SupportsInt,
        right: Ordinal | Cardinal | SupportsInt,
    ):
        source = self(left)
        target = self(right)
        if source == target:
            return True
        if source.expression().is_finite():
            if target.expression().is_finite():
                return source.expression().value <= target.expression().value
            return True
        if target.expression().is_finite():
            return False
        if source.is_initial() and target.is_initial():
            return self.le(source.initial_index(), target.initial_index())
        return Unknown

    def lt(
        self,
        left: Ordinal | Cardinal | SupportsInt,
        right: Ordinal | Cardinal | SupportsInt,
    ):
        source = self(left)
        target = self(right)
        if source == target:
            return False
        return self.le(source, target)

    def ge(self, left, right):
        return self.le(right, left)

    def gt(self, left, right):
        return self.lt(right, left)

    def proves_le(
        self,
        left: Ordinal | Cardinal | SupportsInt,
        right: Ordinal | Cardinal | SupportsInt,
    ) -> bool:
        return self.le(left, right) is True


Ordinal = Ordinals().ObjectType
Ord = Ordinals()


@cached_function
def _ordinal_with_expression(expression: _OrdinalExpression) -> Ordinal:
    return _object_of(Ordinals(), expression=expression)


def ordinal(value: Ordinal | SupportsInt) -> Ordinal:
    return Ordinals()(value)


def omega(index: Ordinal | SupportsInt) -> Ordinal:
    return Ordinals().initial(index)


omega0 = omega(0)


@cached_function
def _cardinal_with_expression(expression: _CardinalExpression) -> Cardinal:
    return _object_of(Cardinalities(), expression=expression)


def cardinal(
    value: Cardinal | SupportsInt | AnInfinity,
) -> Cardinal:
    r"""Notation for ``Cardinalities()(value)``: ``value`` itself when it is a cardinal."""
    return Cardinalities()(value)


def aleph(index: Ordinal | SupportsInt) -> Cardinal:
    return _cardinal_with_expression(_AlephCardinal(ordinal(index)))


aleph0 = aleph(0)
continuum = cardinal(2) ** aleph0


__all__ = [
    "CardinalComparison",
    "Cardinalities",
    "CardinalityMor",
    "CardinalityMorphism",
    "Ord",
    "OrdinalMor",
    "OrdinalMorphism",
    "Ordinals",
    "aleph",
    "aleph0",
    "cardinal",
    "continuum",
    "omega",
    "omega0",
    "ordinal",
]
