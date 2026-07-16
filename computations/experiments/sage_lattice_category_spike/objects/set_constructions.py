r"""Set constructions: finite Cartesian products and disjoint unions.

Thin owned parents that own exactly what Sage's native constructions lack:
placement in the owned axiom lattice by the refinement rules of
``decisions/sets-owns-cardinality-through-standard-constructions`` (which
are conditional — empty-factor precedence, nonemptiness side conditions —
so they are computed per instance rather than declared as blanket
functorial closure), and exact cardinal arithmetic through the owned
``Cardinal`` type. Everything already solved by Sage is delegated: fair
antidiagonal product iteration comes from ``cartesian_product`` and fair
keyed interleaving from ``DisjointUnionEnumeratedSets``, both consuming
owned countable sets natively since the ``Countable`` axiom refines
``EnumeratedSets``. (sympy also owns a symbolic ``DisjointUnion``, but it
lives in sympy's set world and cannot hold Sage parents' elements; probed
2026-07-16.)

Both parents are facades in Sage's sense, with the same plain elements the
delegated machinery uses: a point of a product is a tuple of factor
elements; a point of a disjoint union is a ``(tag, element)`` pair.
Projections, injections, and componentwise map action are elements of the
actual homsets.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any, cast

from sage.categories.category import Category
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.rings.integer_ring import ZZ
from sage.structure.element_wrapper import ElementWrapper

from ..lexicon import SageParent, SageUniqueRepresentation
from .cardinals import Cardinal, cardinal
from .sets import Sets


def _declared_axioms(factor: SageParent) -> frozenset[str]:
    return frozenset(factor.category().axioms())


def _is_finite_placed(factor: SageParent) -> bool:
    return "Finite" in _declared_axioms(factor)


def _is_countable_placed(factor: SageParent) -> bool:
    declared = _declared_axioms(factor)
    return "Countable" in declared or "Finite" in declared


def _is_infinite_placed(factor: SageParent) -> bool:
    declared = _declared_axioms(factor)
    return "Infinite" in declared or "Uncountable" in declared


def _is_uncountable_placed(factor: SageParent) -> bool:
    return "Uncountable" in _declared_axioms(factor)


def _exact_cardinality(factor: SageParent) -> Cardinal:
    # The dynamic access is a documented seam (cardinality is injected by
    # the axiom categories' ParentMethods, not defined on the Parent base
    # class); the value is immediately normalized into the owned cardinal
    # arithmetic, so no untyped value escapes.
    return cardinal(cast(Any, factor).cardinality())


def _is_known_empty(factor: SageParent) -> bool:
    r"""Whether the factor is empty, decided from its declared placement.

    Infinite and uncountable sets are nonempty; a finite set answers by
    exact cardinality; a countable set answers by a terminating first
    -element probe. Anything else must declare its placement first."""
    if _is_infinite_placed(factor):
        return False
    if _is_finite_placed(factor):
        return _exact_cardinality(factor) == 0
    assert _is_countable_placed(factor), f"emptiness of {factor} is undetermined: declare its placement in the owned set axioms"
    for _ in cast(Iterable[object], factor):
        return False
    return True


def _placement(factors: tuple[SageParent, ...]) -> Category:
    r"""The owned axiom placement shared by products and finite disjoint
    unions of the given constituents (for a finite constituent family the
    refinement rules coincide): finite when all are finite, countable when
    all are countable, infinite when any is infinite, uncountable when any
    is uncountable. Empty-constituent precedence for products is handled by
    the caller before this is consulted."""
    category: Sets = Sets()
    if all(_is_finite_placed(factor) for factor in factors):
        return category.Finite()
    if all(_is_countable_placed(factor) for factor in factors):
        category = category.Countable()
    if any(_is_uncountable_placed(factor) for factor in factors):
        category = category.Uncountable()
    elif any(_is_infinite_placed(factor) for factor in factors):
        category = category.Infinite()
    return category


class CartesianProduct(SageUniqueRepresentation, SageParent):
    r"""The finite Cartesian product of owned sets.

    The empty product is the finite singleton; a product with an empty
    factor is the finite empty set regardless of the other factors; a
    product of finite factors multiplies exact cardinalities; countability,
    infinitude, and uncountability propagate by the refinement rules. A
    point wraps a tuple of factor elements (Sage's ``ElementWrapper``, so
    points carry a real parent through the morphism machinery); iteration
    delegates to Sage's fair antidiagonal enumeration."""

    Element = ElementWrapper

    def __init__(self, *factors: SageParent) -> None:
        self._factors = factors
        self._has_empty_factor = any(_is_known_empty(factor) for factor in factors)
        placement = Sets().Finite() if self._has_empty_factor or not factors else _placement(factors)
        # Integration, not invention: the parent is a member of Sage's
        # standard CartesianProducts() construction category.
        SageParent.__init__(self, category=Category.join([placement, Sets().CartesianProducts()]))

    def _repr_(self) -> str:
        if not self._factors:
            return "Cartesian product of no sets (the singleton)"
        return "Cartesian product of " + " x ".join(repr(factor) for factor in self._factors)

    def factors(self) -> tuple[SageParent, ...]:
        return self._factors

    def _element_constructor_(self, components: Iterable[object]) -> ElementWrapper:
        entries = tuple(components)
        assert len(entries) == len(self._factors), f"a point of this product has {len(self._factors)} components; found {len(entries)}"
        converted = tuple(factor(entry) for factor, entry in zip(self._factors, entries))
        for factor, entry in zip(self._factors, converted):
            assert entry in factor, f"{entry} is not an element of {factor}"
        return self.element_class(self, converted)

    def __contains__(self, point: object) -> bool:
        if isinstance(point, ElementWrapper):
            return bool(point.parent() is self)
        if not isinstance(point, tuple) or len(point) != len(self._factors):
            return False
        return all(entry in factor for factor, entry in zip(self._factors, point))

    def cardinality(self) -> Cardinal:
        r"""Exact cardinal product of the factor cardinalities (the
        empty-factor case is the cardinal identity ``0 * kappa == 0``)."""
        if self._has_empty_factor:
            return cardinal(ZZ(0))
        result = cardinal(ZZ(1))
        for factor in self._factors:
            result = result * _exact_cardinality(factor)
        return result

    def __iter__(self) -> Iterator[ElementWrapper]:
        from sage.categories.cartesian_product import cartesian_product

        if not self._factors:
            yield self(())
            return
        if self._has_empty_factor:
            return
        for point in cartesian_product(list(self._factors)):
            yield self(tuple(point))

    def projection(self, i: int) -> SetMorphism:
        r"""The ``i``-th projection, as an element of the actual homset."""
        factor = self._factors[i]
        homset = Hom(self, factor, SageSets())
        return SetMorphism(homset, lambda point: point.value[i])

    # Sage's CartesianProducts() spellings of the same data:
    def cartesian_factors(self) -> tuple[SageParent, ...]:
        return self._factors

    def cartesian_projection(self, i: int) -> SetMorphism:
        return self.projection(i)


def cartesian_product_morphism(*maps: SetMorphism) -> SetMorphism:
    r"""The Cartesian product of set maps, acting componentwise: the map
    ``prod X_i -> prod Y_i`` induced by ``f_i: X_i -> Y_i``."""
    domain = CartesianProduct(*[component.domain() for component in maps])
    codomain = CartesianProduct(*[component.codomain() for component in maps])
    homset = Hom(domain, codomain, SageSets())
    return SetMorphism(homset, lambda point: codomain(tuple(component(entry) for component, entry in zip(maps, point.value))))


class DisjointUnion(SageUniqueRepresentation, SageParent):
    r"""The tagged disjoint union (coproduct) of finitely many owned sets.

    A point wraps a ``(tag, element)`` pair — the same pairs Sage's
    ``DisjointUnionEnumeratedSets`` yields — so equal elements of distinct
    summands stay distinct, and points carry a real parent through the
    morphism machinery. Cardinality is the exact cardinal sum; the empty
    coproduct is the finite empty set; countability, infinitude, and
    uncountability propagate by the refinement rules. Iteration delegates
    to Sage's fair keyed interleaving."""

    Element = ElementWrapper

    def __init__(self, *summands: SageParent) -> None:
        self._summands = summands
        category = Sets().Finite() if not summands else _placement(summands)
        SageParent.__init__(self, category=category)

    def _repr_(self) -> str:
        if not self._summands:
            return "Disjoint union of no sets (the empty set)"
        return "Disjoint union of " + " + ".join(repr(summand) for summand in self._summands)

    def summands(self) -> tuple[SageParent, ...]:
        return self._summands

    def _element_constructor_(self, tagged: object) -> ElementWrapper:
        assert isinstance(tagged, tuple) and len(tagged) == 2, f"a point of a disjoint union is a (tag, element) pair; found {tagged!r}"
        tag, value = tagged
        position = int(tag)
        assert 0 <= position < len(self._summands), f"tag {position} has no summand among {len(self._summands)}"
        summand = self._summands[position]
        converted = summand(value)
        assert converted in summand, f"{converted} is not an element of summand {position}"
        return self.element_class(self, (position, converted))

    def __contains__(self, point: object) -> bool:
        if isinstance(point, ElementWrapper):
            return bool(point.parent() is self)
        if not isinstance(point, tuple) or len(point) != 2:
            return False
        tag, value = point
        return isinstance(tag, int) and 0 <= tag < len(self._summands) and value in self._summands[tag]

    def cardinality(self) -> Cardinal:
        r"""Exact cardinal sum of the summand cardinalities."""
        result = cardinal(ZZ(0))
        for summand in self._summands:
            result = result + _exact_cardinality(summand)
        return result

    def __iter__(self) -> Iterator[ElementWrapper]:
        from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets
        from sage.sets.family import Family

        if not self._summands:
            return
        interleaved = DisjointUnionEnumeratedSets(Family(list(self._summands)), keepkey=True)
        for tag, value in interleaved:
            yield self((int(tag), value))

    def injection(self, i: int) -> SetMorphism:
        r"""The ``i``-th coproduct injection, as an element of the actual
        homset."""
        summand = self._summands[i]
        homset = Hom(summand, self, SageSets())
        return SetMorphism(homset, lambda value: self((i, value)))
