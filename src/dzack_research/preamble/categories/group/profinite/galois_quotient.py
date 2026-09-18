r"""Finite coordinates and restriction maps of an absolute Galois group."""

from sage.categories.finite_fields import FiniteFields as SageFiniteFields
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.integer_ring import ZZ
from sage.structure.element import Element
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    ExactFieldMorphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring, _own_ring
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category import _object_of


def _relative_degree(base_field, extension_field):
    r"""Return ``[L:K] = [L:F] / [K:F]`` over the common prime field ``F``.

    Engine adapter: Sage's number fields, the rational field and finite
    fields all answer ``absolute_degree()``, the degree over the prime field.
    """
    base = _engine_ring(base_field)
    extension = _engine_ring(extension_field)
    assert base.characteristic() == extension.characteristic(), (
        "a finite extension has the same characteristic as its base"
    )
    base_degree = ZZ(base.absolute_degree())
    extension_degree = ZZ(extension.absolute_degree())
    assert extension_degree % base_degree == 0, (
        "the stated field cannot be finite over the base field"
    )
    return extension_degree // base_degree


class FiniteGaloisExtension(SageObject):
    r"""A finite separable field (L/K\subset\bar K) with both exact embeddings."""

    def __init__(
        self,
        base_field,
        field,
        base_embedding: ExactFieldMorphism,
        closure,
        closure_embedding: ExactFieldMorphism,
    ) -> None:
        self._base_field = _own_ring(base_field)
        self._field = _own_ring(field)
        self._closure = _own_ring(closure)
        assert base_embedding.parent() is self._base_field.exact_morphisms_to(self._field), (
            "the base inclusion K -> L is an exact field morphism from the base field to the field"
        )
        assert closure_embedding.parent() is self._field.exact_morphisms_to(self._closure), (
            "the realization L -> Kbar is an exact field morphism from the field to the closure"
        )
        self._base_embedding = base_embedding
        self._closure_embedding = closure_embedding
        compatible_embeddings = finite_ordered_set(
            tuple(
                candidate
                for candidate in self._field.exact_embeddings(self._closure)
                if all(
                    candidate(self._base_embedding(generator))
                    == self._closure_embedding(self._base_embedding(generator))
                    for generator in self._base_field.field_generators()
                )
            )
        )
        assert compatible_embeddings.cardinality() == cardinal(self.degree()), (
            "a represented finite extension is separable over its base field: it has [L:K] K-embeddings into Kbar"
        )

    def base_field(self):
        return self._base_field

    def field(self):
        return self._field

    def algebraic_closure(self):
        return self._closure

    def base_embedding(self) -> ExactFieldMorphism:
        return self._base_embedding

    def embedding(self) -> ExactFieldMorphism:
        return self._closure_embedding

    def degree(self):
        return _relative_degree(self.base_field(), self.field())

    @cached_method
    def automorphisms_over_base_field(self):
        r"""The exact ``K``-automorphisms of ``L``: the self-embeddings of ``L`` fixing ``K``."""
        base_generators = self.base_field().field_generators()
        return finite_ordered_set(
            tuple(
                candidate
                for candidate in self.field().exact_embeddings(self.field())
                if all(
                    candidate(self.base_embedding()(generator))
                    == self.base_embedding()(generator)
                    for generator in base_generators
                )
            )
        )

    def automorphisms(self):
        r"""The elements of ``Gal(L/K)``, as exact field maps; ``L/K`` is Galois."""
        assert self.is_galois(), (
            f"{self.field()} is not represented as a finite Galois extension of {self.base_field()}"
        )
        return self.automorphisms_over_base_field()

    def is_galois(self) -> bool:
        r"""Whether ``L/K`` is Galois: ``|Aut_K(L)| = [L:K]`` (Stacks, Lemma 9.21.2)."""
        return self.automorphisms_over_base_field().cardinality() == cardinal(self.degree())

    def __eq__(self, other) -> bool:
        r"""Equal when the defining data ``K -> L -> Kbar`` agree.

        The fields and the closure are compared by identity and the two exact
        embeddings by their values on field generators.
        """
        return (
            isinstance(other, FiniteGaloisExtension)
            and other.base_field() is self.base_field()
            and other.field() is self.field()
            and other.algebraic_closure() is self.algebraic_closure()
            and other.base_embedding() == self.base_embedding()
            and other.embedding() == self.embedding()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(
            (
                id(self._base_field),
                id(self._field),
                id(self._closure),
                self._base_embedding,
                self._closure_embedding,
            )
        )

    def _repr_(self) -> str:
        return f"Finite separable extension {self.field()} / {self.base_field()} in {self.algebraic_closure()}"


def _morphism_signature(morphism: ExactFieldMorphism) -> tuple:
    return tuple(
        morphism(generator) for generator in morphism.domain().field_generators()
    )


class FiniteGaloisAutomorphism(Element):
    r"""An exact ``K``-automorphism of a represented finite extension ``L/K``.

    The element implementation of the finite field-automorphism engine:
    an element is its position in the group's enumeration of the
    ``K``-automorphisms of ``L``.
    """

    def __init__(self, parent, index: int) -> None:
        Element.__init__(self, parent)
        self._index = int(index)

    def action(self) -> ExactFieldMorphism:
        return self.parent().automorphisms()[self._index]

    as_morphism = action

    def __call__(self, element):
        return self.action()(element)

    def _mul_(self, other):
        r"""``self ∘ other``; Sage's arithmetic calls this with one parent."""
        return self.parent().compose(self, other)

    def __invert__(self):
        return self.inverse()

    def inverse(self):
        return self.parent().inverse(self)

    def multiplicative_order(self):
        identity = self.parent().one()
        value = identity
        for order in range(1, int(self.parent().order()) + 1):
            value = value * self
            if value == identity:
                return ZZ(order)
        raise ArithmeticError(
            "the represented finite group element has no finite order"
        )

    def __pow__(self, exponent):
        exponent = ZZ(exponent)
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = self.parent().one()
        factor = self
        while exponent:
            if exponent & 1:
                result = result * factor
            factor = factor * factor
            exponent >>= 1
        return result

    def _richcmp_(self, other, op):
        r"""Compare by position in the enumeration; Sage calls this with one parent."""
        return richcmp(self._index, other._index, op)

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._index))

    def _repr_(self) -> str:
        return repr(self.action())


class _FiniteFieldAutomorphismEngine:
    r"""The exact finite group Aut_K(L), realized at OwnedGroups().Finite().

    The extension determines the self-embeddings fixing K, their composition
    and inverses.  It is a realization of a finite group, not another
    category of engine outputs.  Normality is required only by the quotient
    entry Gal(L/K), not by Aut_K(L).
    """

    def __init__(self, extension, **rest) -> None:
        self._extension = extension
        super().__init__(**rest)

    def extension_data(self) -> FiniteGaloisExtension:
        return self._extension

    def top_field(self):
        return self._extension.field()

    def base_field(self):
        return self._extension.base_field()

    def automorphisms(self):
        return self._extension.automorphisms_over_base_field()

    @cached_method
    def _signature_positions(self):
        r"""The position of each automorphism, keyed by its values on the generators of ``L``."""
        return {
            _morphism_signature(automorphism): position
            for position, automorphism in enumerate(self.automorphisms())
        }

    def _element_constructor_(self, datum):
        if isinstance(datum, FiniteGaloisAutomorphism):
            if datum.parent() is self:
                return datum
            datum = datum.action()
        if isinstance(datum, ExactFieldMorphism):
            if datum.domain() is not self.top_field() or datum.codomain() is not self.top_field():
                raise ValueError("an automorphism has this top field as both endpoints")
            position = self._signature_positions().get(_morphism_signature(datum))
            if position is None:
                raise ValueError("the map is not an automorphism in this group")
            return self.element_class(self, position)
        index = int(ZZ(datum))
        if not 0 <= index < int(self.order()):
            raise ValueError("the automorphism index is outside this finite group")
        return self.element_class(self, index)

    def __iter__(self):
        return (self.element_class(self, index) for index in range(int(self.order())))

    def one(self):
        identity_signature = tuple(self.top_field().field_generators())
        assert identity_signature in self._signature_positions(), (
            "the enumerated automorphisms contain the identity"
        )
        return self.element_class(self, self._signature_positions()[identity_signature])

    def order(self):
        return ZZ(int(self.automorphisms().cardinality()))

    def cardinality(self):
        return cardinal(self.order())

    def compose(self, left, right):
        images = tuple(
            left(right(generator)) for generator in self.top_field().field_generators()
        )
        assert images in self._signature_positions(), (
            "the finite automorphism list is closed under composition"
        )
        return self.element_class(self, self._signature_positions()[images])

    def inverse(self, element):
        identity = self.one()
        return next(
            candidate
            for candidate in self
            if element * candidate == identity and candidate * element == identity
        )

    def decomposition_group(self, prime_above):
        r"""Return the decomposition subgroup at ``prime_above``."""
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            _finite_decomposition_group,
        )

        return _finite_decomposition_group(self, prime_above)

    def inertia_group(self, prime_above):
        r"""Return the inertia subgroup at ``prime_above``."""
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            _finite_inertia_group,
        )

        return _finite_inertia_group(self, prime_above)

    def frobenius_class(self, base_prime, prime_above):
        r"""Return the unramified Frobenius conjugacy class at ``prime_above``."""
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            _finite_frobenius_class,
        )

        return _finite_frobenius_class(self, base_prime, prime_above)

    def group_generators(self):
        r"""A generating set: the Frobenius power of order ``[L:K]`` over a finite field, else the nonidentity elements."""
        identity = self.one()
        nonidentity = tuple(element for element in self if element != identity)
        if _engine_ring(self.top_field()) not in SageFiniteFields():
            return finite_ordered_set(nonidentity)
        generators = tuple(
            element
            for element in nonidentity
            if element.multiplicative_order() == self.order()
        )
        assert self.order() == 1 or generators, (
            "the Galois group of a finite extension of finite fields is cyclic"
        )
        return finite_ordered_set(generators[:1])

    def is_abelian(self) -> bool:
        return all(left * right == right * left for left in self for right in self)

    def _repr_(self) -> str:
        if self._extension.is_galois():
            return f"Gal({self.top_field()} / {self.base_field()})"
        return f"Aut_{self.base_field()}({self.top_field()})"
    def __call__(self, datum):
        return self._element_constructor_(datum)

    def __contains__(self, datum):
        return isinstance(datum, FiniteGaloisAutomorphism) and datum.parent() is self


@cached_function
def FiniteExtensionAutomorphismGroup(extension):
    r"""Aut_K(L) for the exact extension diagram, using the finite-group entry."""
    return _object_of(
        OwnedGroups().Finite(),
        _engine=(OwnedGroups(), _FiniteFieldAutomorphismEngine, FiniteGaloisAutomorphism),
        extension=extension,
    )


def FiniteGaloisQuotient(extension):
    r"""Gal(L/K): Aut_K(L) when the finite separable extension is normal."""
    assert extension.is_galois(), f"{extension} is not Galois, so it has no Galois group quotient of G_K"
    return FiniteExtensionAutomorphismGroup(extension)




class GaloisRestrictionMap(Morphism):
    r"""The continuous quotient map (G_K\to\operatorname{Gal}(L/K))."""

    def __init__(self, domain, codomain) -> None:
        extension = domain.extension_data(codomain.extension_data())
        Morphism.__init__(self, domain.continuous_morphisms_to(codomain))
        self._extension = extension

    def extension(self) -> FiniteGaloisExtension:
        return self._extension

    def _call_(self, element):
        r"""``sigma |-> sigma|_L``: a realized finite coordinate, else the automorphism of ``L`` agreeing with ``sigma`` on its generators."""
        element = self.domain()(element)
        coordinate = element.restriction_coordinate(self.extension())
        if coordinate is not None:
            return self.codomain()(coordinate)
        embedding = self.extension().embedding()
        generators = self.extension().field().field_generators()
        images = tuple(element(embedding(generator)) for generator in generators)
        restriction = next(
            (
                candidate
                for candidate in self.codomain()
                if all(
                    image == embedding(candidate(generator))
                    for generator, image in zip(generators, images, strict=True)
                )
            ),
            None,
        )
        assert restriction is not None, (
            "the represented automorphism preserves this Galois stage"
        )
        return restriction

    def kernel(self):
        return self.domain().open_subgroup(self.extension())

    def is_surjective(self) -> bool:
        return True

    def is_continuous(self) -> bool:
        return True

    def _repr_(self) -> str:
        return f"Restriction {self.domain()} -> {self.codomain()}"


class LiftCoset(SageObject):
    r"""The coset of all global extensions of one finite-level automorphism."""

    def __init__(self, restriction_map: GaloisRestrictionMap, element) -> None:
        self._restriction_map = restriction_map
        self._element = restriction_map.codomain()(element)

    def supergroup(self):
        return self._restriction_map.domain()

    def ambient(self):
        r"""Return the ambient absolute Galois group containing this coset."""
        return self.supergroup()

    def finite_automorphism(self):
        return self._element

    def extension(self) -> FiniteGaloisExtension:
        return self._restriction_map.extension()

    def kernel(self):
        return self._restriction_map.kernel()

    def __contains__(self, candidate) -> bool:
        return candidate in self.supergroup() and self._restriction_map(candidate) == self._element

    def representative(self, candidate=None):
        r"""Return a supplied representative, or the canonical finite-field one.

        Over a general field the fiber is a coset but has no distinguished
        element.  Selecting one here would silently reintroduce a global
        extension-choice policy.
        """
        if candidate is not None:
            if candidate not in self:
                raise ValueError("the supplied automorphism is not in this lift coset")
            return candidate
        if self.supergroup()._is_finite_field():
            return self.supergroup().lift(self._element)
        raise ValueError(
            "this extension coset has no canonically selected representative"
        )

    def _repr_(self) -> str:
        return f"Lift coset of {self._element} in {self.supergroup()}"


__all__ = [
    "FiniteExtensionAutomorphismGroup",
    "FiniteGaloisAutomorphism",
    "FiniteGaloisExtension",
    "FiniteGaloisQuotient",
    "GaloisRestrictionMap",
    "LiftCoset",
]
