r"""Cardinal and ordinal arithmetic in the owned set-theoretic number hierarchy."""

from __future__ import annotations

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.semirings import Semirings
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.infinity import Infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.abstract_categories.objects import Objects


@dataclass(frozen=True)
class _FiniteCardinal:
    value: int


@dataclass(frozen=True)
class _AlephCardinal:
    index: "Ordinal"


@dataclass(frozen=True)
class _PowerCardinal:
    base: "Cardinal"
    exponent: "Cardinal"


@dataclass(frozen=True)
class _SupremumCardinal:
    terms: tuple["Cardinal", ...]


@dataclass(frozen=True)
class _IndexedSumCardinal:
    index_set: Parent
    summands: Callable


@dataclass(frozen=True)
class _IndexedProductCardinal:
    index_set: Parent
    factors: Callable


class CardinalComparison(Enum):
    LESS = -1
    EQUAL = 0
    GREATER = 1
    LESS_OR_EQUAL = 2
    GREATER_OR_EQUAL = 3
    INCOMPARABLE = 4


class CardinalityMorphism(Morphism):
    def __init__(self, parent) -> None:
        Morphism.__init__(self, parent)

    def is_identity(self) -> bool:
        return self.domain() is self.codomain()

    def __mul__(self, other):
        if not isinstance(other, CardinalityMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        return Cardinalities().Mor(other.domain(), self.codomain()).unique_morphism()

    def _repr_(self) -> str:
        return f"{self.domain()} <= {self.codomain()}"


class CardinalityHomset(CategoricalHomset):
    Element = CardinalityMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def cardinality(self):
        return cardinal(1 if Cardinalities().le(self.domain(), self.codomain()) else 0)

    @cached_method
    def unique_morphism(self):
        if not Cardinalities().le(self.domain(), self.codomain()):
            raise ValueError(f"there is no cardinality morphism {self.domain()} -> {self.codomain()}")
        return self.element_class(self)

    def _element_constructor_(self, morphism=None):
        if morphism is not None and morphism.parent() is not self:
            raise ValueError(f"{morphism} is not in {self}")
        return self.unique_morphism()

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism homset")
        return self.unique_morphism()


class CardinalityHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return CardinalityHomset


class Cardinalities(Category):
    r"""The thin category associated to the represented cardinal order."""

    _HomCategory = CardinalityHomCategoryConstruction

    def super_categories(self):
        return [Objects()]

    def _repr_(self) -> str:
        return "Category of cardinalities"

    def Mor(self, domain, codomain) -> CardinalityHomset:
        return CardinalityHomCategoryConstruction(self).Of(
            cardinal(domain), cardinal(codomain)
        )

    class ParentMethods:
        def Mor(self, codomain, category=None):
            if category is not None and category is not Cardinalities():
                raise TypeError("a cardinal morphism lies in Cardinalities")
            return Cardinalities().Mor(self, codomain)

    def zero(self):
        return cardinal(0)

    def one(self):
        return cardinal(1)

    def sum(self, *summands):
        result = self.zero()
        for summand in map(cardinal, summands):
            if result.is_finite() and summand.is_finite():
                result = cardinal(result._finite_int() + summand._finite_int())
            elif result.is_finite():
                result = summand
            elif summand.is_infinite():
                result = self.supremum(result, summand)
        return result

    def product(self, *factors):
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

    def indexed_sum(self, index_set: Parent, summands: Callable):
        size = cardinal(index_set.cardinality())
        if size.is_finite():
            return self.sum(*(summands(index) for index in index_set))
        return _cardinal_with_expression(_IndexedSumCardinal(index_set, summands))

    def indexed_product(self, index_set: Parent, factors: Callable):
        size = cardinal(index_set.cardinality())
        if size.is_finite():
            return self.product(*(factors(index) for index in index_set))
        return _cardinal_with_expression(_IndexedProductCardinal(index_set, factors))

    def power(self, base, exponent):
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
        exponent_expression = cardinal_exponent.expression()
        if isinstance(exponent_expression, _SupremumCardinal):
            return self.supremum(
                *(self.power(cardinal_base, term) for term in exponent_expression.terms)
            )
        base_expression = cardinal_base.expression()
        if isinstance(base_expression, _SupremumCardinal):
            return self.supremum(
                *(self.power(term, cardinal_exponent) for term in base_expression.terms)
            )
        if isinstance(base_expression, _PowerCardinal):
            return self.power(
                base_expression.base,
                self.product(base_expression.exponent, cardinal_exponent),
            )
        return _cardinal_with_expression(_PowerCardinal(cardinal_base, cardinal_exponent))

    def supremum(self, *cardinal_numbers):
        terms: list[Cardinal] = []
        for cardinal_number in map(cardinal, cardinal_numbers):
            expression = cardinal_number.expression()
            if isinstance(expression, _SupremumCardinal):
                terms.extend(expression.terms)
            else:
                terms.append(cardinal_number)
        if not terms:
            raise ValueError("a finite supremum needs at least one cardinal")
        maximal_terms: list[Cardinal] = []
        for candidate in sorted(set(terms), key=Cardinal.sort_key):
            if any(self.le(candidate, term) for term in maximal_terms):
                continue
            maximal_terms = [term for term in maximal_terms if not self.le(term, candidate)]
            maximal_terms.append(candidate)
        maximal_terms.sort(key=Cardinal.sort_key)
        if len(maximal_terms) == 1:
            return maximal_terms[0]
        return _cardinal_with_expression(_SupremumCardinal(tuple(maximal_terms)))

    def le(self, source, target) -> bool:
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
        if isinstance(left_expression, (_IndexedSumCardinal, _IndexedProductCardinal)) or isinstance(
            right_expression, (_IndexedSumCardinal, _IndexedProductCardinal)
        ):
            return False
        if left.is_finite():
            if right.is_finite():
                return left._finite_int() <= right._finite_int()
            return True
        if right.is_finite():
            return False
        if left.is_aleph() and right.is_aleph():
            return left.aleph_index() <= right.aleph_index()
        if left.is_countably_infinite():
            return True
        if left.is_aleph() and left.aleph_index() == 1 and right.is_uncountable():
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
                    left_expression.exponent, right_expression.exponent
                )
        return False

    def lt(self, source, target) -> bool:
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
        if isinstance(left_expression, (_IndexedSumCardinal, _IndexedProductCardinal)) or isinstance(
            right_expression, (_IndexedSumCardinal, _IndexedProductCardinal)
        ):
            return False
        if left.is_finite():
            if right.is_finite():
                return left._finite_int() < right._finite_int()
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

    def ge(self, source, target) -> bool:
        return self.le(target, source)

    def gt(self, source, target) -> bool:
        return self.lt(target, source)

    def compare(self, source, target) -> CardinalComparison:
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

    def are_incomparable(self, source, target) -> bool:
        return not self.le(source, target) and not self.le(target, source)


class Cardinal(Parent):
    r"""A cardinal number as an object of the thin cardinal-order category."""

    def __init__(self, expression) -> None:
        self._expression = expression
        Parent.__init__(self, category=Cardinalities())

    def expression(self):
        return self._expression

    def cardinality(self):
        return self

    def sort_key(self) -> tuple[int, str]:
        expression = self.expression()
        if isinstance(expression, _FiniteCardinal):
            return (0, str(expression.value))
        if isinstance(expression, _AlephCardinal):
            return (1, str(expression.index))
        if isinstance(expression, _PowerCardinal):
            return (2, repr(self))
        if isinstance(expression, _SupremumCardinal):
            return (3, repr(self))
        return (4, repr(self))

    def _repr_(self) -> str:
        expression = self.expression()
        if isinstance(expression, _FiniteCardinal):
            return repr(expression.value)
        if isinstance(expression, _AlephCardinal):
            return f"ℵ_{expression.index}"
        if isinstance(expression, _PowerCardinal):
            return f"({expression.base})^({expression.exponent})"
        if isinstance(expression, _SupremumCardinal):
            return "sup(" + ", ".join(map(str, expression.terms)) + ")"
        if isinstance(expression, _IndexedSumCardinal):
            return f"sum_{{i in {expression.index_set}}} kappa_i"
        return f"prod_{{i in {expression.index_set}}} kappa_i"

    def __hash__(self) -> int:
        if self.is_finite():
            return hash(self._finite_int())
        if self.is_countably_infinite():
            return hash(Infinity)
        return hash(self.expression())

    def __eq__(self, other) -> bool:
        try:
            return self.expression() == cardinal(other).expression()
        except (TypeError, ValueError):
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
        if isinstance(expression, (_IndexedSumCardinal, _IndexedProductCardinal)):
            raise NotImplementedError(
                "finiteness of an arbitrary indexed cardinal family is not decidable"
            )
        return isinstance(expression, _FiniteCardinal)

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
        expression = self.expression()
        if isinstance(expression, (_IndexedSumCardinal, _IndexedProductCardinal)):
            raise NotImplementedError(
                "countability of an arbitrary indexed cardinal family is not decidable"
            )
        if self.is_finite() or self.is_countably_infinite():
            return False
        if isinstance(expression, _SupremumCardinal):
            return any(term.is_uncountable() for term in expression.terms)
        return True

    def is_countably_infinite(self) -> bool:
        expression = self.expression()
        return isinstance(expression, _AlephCardinal) and expression.index == 0

    def is_uncountably_infinite(self) -> bool:
        return self.is_infinite() and self.is_uncountable()

    def aleph_index(self):
        expression = self.expression()
        if not isinstance(expression, _AlephCardinal):
            raise ValueError(f"{self} is not an aleph cardinal")
        return expression.index

    def initial_ordinal(self):
        return omega(self.aleph_index())

    def _finite_int(self) -> int:
        expression = self.expression()
        if not isinstance(expression, _FiniteCardinal):
            raise ValueError(f"{self} is not a finite cardinal")
        return expression.value

    def finite_value(self):
        r"""Return the ordinary nonnegative integer representing this finite cardinal."""
        expression = self.expression()
        if not isinstance(expression, _FiniteCardinal):
            raise ValueError(f"{self} is not a finite cardinal")
        return expression.value

    def __int__(self) -> int:
        if not self.is_finite():
            raise TypeError(f"cannot convert infinite cardinal {self} to integer")
        return self._finite_int()

    def __index__(self) -> int:
        return int(self)

    def _integer_(self, ring=None):
        if not self.is_finite():
            raise TypeError(f"cannot convert infinite cardinal {self} to an integer")
        from sage.rings.integer_ring import ZZ as SageZZ

        return SageZZ(self._finite_int())

    def _rational_(self):
        if not self.is_finite():
            raise TypeError(f"cannot convert infinite cardinal {self} to a rational")
        from sage.rings.rational_field import QQ as SageQQ

        return SageQQ(self._finite_int())


@dataclass(frozen=True)
class _FiniteOrdinal:
    value: Integer


@dataclass(frozen=True)
class _InitialOrdinal:
    index: "Ordinal"


@dataclass(frozen=True)
class _NaturalSum:
    terms: tuple["Ordinal", ...]


@dataclass(frozen=True)
class _NaturalProduct:
    factors: tuple["Ordinal", ...]


@dataclass(frozen=True)
class _OrdinalSum:
    left: "Ordinal"
    right: "Ordinal"


@dataclass(frozen=True)
class _OrdinalProduct:
    left: "Ordinal"
    right: "Ordinal"


@dataclass(frozen=True)
class _OrdinalPower:
    base: "Ordinal"
    exponent: "Ordinal"


class OrdinalSemiringMorphism(Morphism):
    r"""A declared homomorphism between represented ordinal semirings."""

    def __init__(self, parent, function) -> None:
        Morphism.__init__(self, parent)
        if not callable(function):
            raise TypeError("an ordinal-semiring morphism requires an exact map")
        self._function = function
        self._preamble_is_identity = False

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        if not isinstance(other, OrdinalSemiringMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        if self.is_identity():
            return other
        if other.is_identity():
            return self
        return OrdinalSemirings().Mor(other.domain(), self.codomain())(
            lambda element: self(other(element))
        )

    def is_identity(self) -> bool:
        return self._preamble_is_identity


class OrdinalSemiringHomset(CategoricalHomset):
    Element = OrdinalSemiringMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def _element_constructor_(self, function):
        if isinstance(function, OrdinalSemiringMorphism):
            if function.domain() is not self.domain() or function.codomain() is not self.codomain():
                raise ValueError("the ordinal-semiring morphism has the wrong endpoints")
            if function.parent() is self:
                return function
            function = lambda element, morphism=function: morphism(element)
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        identity = self(lambda element: element)
        identity._preamble_is_identity = True
        return identity


class OrdinalSemiringHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return OrdinalSemiringHomset


class OrdinalSemirings(Category):
    r"""The category containing the ordinal semiring under natural operations."""

    _HomCategory = OrdinalSemiringHomCategoryConstruction

    def __init__(self) -> None:
        # Sage semiring classes provide Python arithmetic plumbing only; they
        # are not mathematical ancestors in the owned graph.
        self._super_categories_for_classes = [Semirings().Commutative()]
        super().__init__()

    def super_categories(self):
        return [Objects()]

    def Mor(self, domain, codomain) -> OrdinalSemiringHomset:
        if domain not in self or codomain not in self:
            raise TypeError("an ordinal-semiring morphism requires two ordinal semirings")
        return OrdinalSemiringHomCategoryConstruction(self).Of(domain, codomain)

    class ParentMethods:
        def Mor(self, codomain, category=None):
            if category is not None and category is not OrdinalSemirings():
                raise TypeError("an ordinal-semiring morphism lies in OrdinalSemirings")
            return OrdinalSemirings().Mor(self, codomain)


class Ordinal(Element):
    r"""An ordinal represented by a symbolic arithmetic expression."""

    def __init__(self, parent, expression) -> None:
        Element.__init__(self, parent)
        self._expression = expression

    def expression(self):
        return self._expression

    def __hash__(self) -> int:
        return hash(self.expression())

    def __eq__(self, other) -> bool:
        try:
            other_ordinal = self.parent()(other)
        except (TypeError, ValueError):
            return False
        return self.expression() == other_ordinal.expression()

    def __ne__(self, other) -> bool:
        return not self == other

    def __le__(self, other) -> bool:
        return self.parent().proves_le(self, other)

    def __lt__(self, other) -> bool:
        target = self.parent()(other)
        return self != target and self <= target

    def __ge__(self, other) -> bool:
        return self.parent().proves_le(other, self)

    def __gt__(self, other) -> bool:
        source = self.parent()(other)
        return self != source and self >= source

    def _add_(self, other):
        return self.parent().natural_sum(self, other)

    def _mul_(self, other):
        return self.parent().natural_product(self, other)

    def __radd__(self, other):
        return self.parent().natural_sum(other, self)

    def __rmul__(self, other):
        return self.parent().natural_product(other, self)

    def ordinal_sum(self, other):
        right = self.parent()(other)
        left_expression = self.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _FiniteOrdinal) and isinstance(
            right_expression, _FiniteOrdinal
        ):
            return self.parent()(left_expression.value + right_expression.value)
        if right == 0:
            return self
        if self == 0:
            return right
        return self.parent().from_expression(_OrdinalSum(self, right))

    def ordinal_product(self, other):
        right = self.parent()(other)
        left_expression = self.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _FiniteOrdinal) and isinstance(
            right_expression, _FiniteOrdinal
        ):
            return self.parent()(left_expression.value * right_expression.value)
        if self == 0 or right == 0:
            return self.parent().zero()
        if right == 1:
            return self
        if self == 1:
            return right
        return self.parent().from_expression(_OrdinalProduct(self, right))

    def ordinal_power(self, exponent):
        power = self.parent()(exponent)
        base_expression = self.expression()
        exponent_expression = power.expression()
        if isinstance(base_expression, _FiniteOrdinal) and isinstance(
            exponent_expression, _FiniteOrdinal
        ):
            return self.parent()(base_expression.value ** exponent_expression.value)
        if power == 0:
            return self.parent().one()
        if self == 0:
            return self.parent().zero()
        if self == 1:
            return self
        return self.parent().from_expression(_OrdinalPower(self, power))

    def is_initial(self) -> bool:
        return isinstance(self.expression(), _InitialOrdinal)

    def initial_index(self):
        expression = self.expression()
        if not isinstance(expression, _InitialOrdinal):
            raise ValueError(f"{self} is not an initial ordinal")
        return expression.index

    def cardinality(self):
        expression = self.expression()
        if isinstance(expression, _FiniteOrdinal):
            return cardinal(expression.value)
        if isinstance(expression, _InitialOrdinal):
            return aleph(expression.index)
        if isinstance(expression, (_NaturalSum, _OrdinalSum)):
            terms = (
                expression.terms
                if isinstance(expression, _NaturalSum)
                else (expression.left, expression.right)
            )
            return Cardinalities().sum(*(term.cardinality() for term in terms))
        if isinstance(expression, (_NaturalProduct, _OrdinalProduct)):
            factors = (
                expression.factors
                if isinstance(expression, _NaturalProduct)
                else (expression.left, expression.right)
            )
            return Cardinalities().product(*(factor.cardinality() for factor in factors))
        return Cardinalities().power(
            expression.base.cardinality(), expression.exponent.cardinality()
        )

    def _repr_(self) -> str:
        expression = self.expression()
        if isinstance(expression, _FiniteOrdinal):
            return repr(expression.value)
        if isinstance(expression, _InitialOrdinal):
            return f"ω_{expression.index}"
        if isinstance(expression, _NaturalSum):
            return " # ".join(map(repr, expression.terms))
        if isinstance(expression, _NaturalProduct):
            return " ⊗ ".join(map(repr, expression.factors))
        if isinstance(expression, _OrdinalSum):
            return f"({expression.left} +o {expression.right})"
        if isinstance(expression, _OrdinalProduct):
            return f"({expression.left} *o {expression.right})"
        return f"({expression.base} ^o {expression.exponent})"


class OrdinalSemiring(UniqueRepresentation, Parent):
    Element = Ordinal

    def __init__(self) -> None:
        Parent.__init__(self, category=OrdinalSemirings())

    def _repr_(self) -> str:
        return "Ordinal semiring"

    def from_expression(self, expression) -> Ordinal:
        return self.element_class(self, expression)

    def _element_constructor_(self, value):
        if isinstance(value, Ordinal):
            if value.parent() is self:
                return value
            raise TypeError("an ordinal belongs to the canonical ordinal semiring")
        integer = ZZ(value)
        if integer < 0:
            raise ValueError(f"an ordinal is nonnegative; found {integer}")
        return self.from_expression(_FiniteOrdinal(integer))

    def zero(self) -> Ordinal:
        return self(0)

    def one(self) -> Ordinal:
        return self(1)

    def initial(self, index) -> Ordinal:
        return self.from_expression(_InitialOrdinal(self(index)))

    def natural_sum(self, *summands) -> Ordinal:
        terms: list[Ordinal] = []
        finite_part = ZZ.zero()
        for summand in map(self, summands):
            expression = summand.expression()
            if isinstance(expression, _FiniteOrdinal):
                finite_part += expression.value
            elif isinstance(expression, _NaturalSum):
                terms.extend(expression.terms)
            else:
                terms.append(summand)
        if finite_part:
            terms.append(self(finite_part))
        if not terms:
            return self.zero()
        terms.sort(key=repr)
        if len(terms) == 1:
            return terms[0]
        return self.from_expression(_NaturalSum(tuple(terms)))

    def natural_product(self, *factors) -> Ordinal:
        ordinal_factors = tuple(map(self, factors))
        for index, factor in enumerate(ordinal_factors):
            expression = factor.expression()
            if isinstance(expression, _NaturalSum):
                preceding = ordinal_factors[:index]
                following = ordinal_factors[index + 1 :]
                return self.natural_sum(
                    *(
                        self.natural_product(*preceding, term, *following)
                        for term in expression.terms
                    )
                )
        normalized: list[Ordinal] = []
        finite_part = ZZ.one()
        for factor in ordinal_factors:
            expression = factor.expression()
            if isinstance(expression, _FiniteOrdinal):
                if expression.value == 0:
                    return self.zero()
                finite_part *= expression.value
            elif isinstance(expression, _NaturalProduct):
                normalized.extend(expression.factors)
            else:
                normalized.append(factor)
        if finite_part != 1 or not normalized:
            normalized.append(self(finite_part))
        normalized.sort(key=repr)
        if len(normalized) == 1:
            return normalized[0]
        return self.from_expression(_NaturalProduct(tuple(normalized)))

    def proves_le(self, left, right) -> bool:
        source = self(left)
        target = self(right)
        if source == target:
            return True
        source_expression = source.expression()
        target_expression = target.expression()
        if isinstance(source_expression, _FiniteOrdinal):
            if isinstance(target_expression, _FiniteOrdinal):
                return source_expression.value <= target_expression.value
            return True
        if isinstance(target_expression, _FiniteOrdinal):
            return False
        if isinstance(source_expression, _InitialOrdinal) and isinstance(
            target_expression, _InitialOrdinal
        ):
            return self.proves_le(source_expression.index, target_expression.index)
        return False


@cached_function
def Ordinals() -> OrdinalSemiring:
    return OrdinalSemiring()


def ordinal(value) -> Ordinal:
    return Ordinals()(value)


def omega(index) -> Ordinal:
    return Ordinals().initial(index)


omega0 = omega(0)


@cached_function
def _cardinal_with_expression(expression) -> Cardinal:
    return Cardinal(expression)


def cardinal(value) -> Cardinal:
    if isinstance(value, Cardinal):
        return value
    if value == Infinity:
        return aleph(0)
    if isinstance(value, int):
        integer = value
    else:
        try:
            integer = int(value)
        except (TypeError, ValueError, OverflowError) as error:
            raise TypeError("a finite cardinal is specified by an exact integer") from error
        if value != integer:
            raise TypeError("a finite cardinal is specified by an exact integer")
    if integer < 0:
        raise ValueError(f"a cardinal is nonnegative; found {integer}")
    return _cardinal_with_expression(_FiniteCardinal(integer))


def aleph(index) -> Cardinal:
    return _cardinal_with_expression(_AlephCardinal(ordinal(index)))


aleph0 = aleph(0)
continuum = cardinal(2) ** aleph0


__all__ = [
    "Cardinal",
    "CardinalComparison",
    "Cardinalities",
    "CardinalityHomset",
    "CardinalityMorphism",
    "Ordinal",
    "OrdinalSemiring",
    "OrdinalSemirings",
    "Ordinals",
    "aleph",
    "aleph0",
    "cardinal",
    "continuum",
    "omega",
    "omega0",
    "ordinal",
]
