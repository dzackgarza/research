r"""Finite coordinates and restriction maps of an absolute Galois group."""

from typing import cast

from sage.categories.groups import Groups as SageGroups
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.rings.integer_ring import ZZ
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.groups import OwnedFiniteGroups
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    ExactFieldMorphism,
    exact_embeddings,
    field_generators,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring, _own_ring


def _relative_degree(base_field, extension_field):
    base = _engine_ring(base_field)
    extension = _engine_ring(extension_field)
    if base.characteristic() != extension.characteristic():
        raise ValueError(
            "a finite extension must have the same characteristic as its base"
        )

    try:
        defining_base = extension.base_field()
    except AttributeError:
        defining_base = None
    if defining_base is base:
        for method_name in ("relative_degree", "degree"):
            method = getattr(extension, method_name, None)
            if method is None:
                continue
            try:
                return ZZ(method())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                continue

    def absolute_degree(field):
        for method_name in ("absolute_degree", "degree"):
            method = getattr(field, method_name, None)
            if method is None:
                continue
            try:
                return ZZ(method())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                continue
        raise TypeError(f"the absolute degree of {field} is unavailable")

    base_degree = absolute_degree(base)
    extension_degree = absolute_degree(extension)
    if extension_degree % base_degree:
        raise ValueError("the stated field cannot be finite over the base field")
    return extension_degree // base_degree


class FiniteGaloisExtension(SageObject):
    r"""A finite Galois field (L/K\subset\bar K) with both exact embeddings."""

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
        if not isinstance(base_embedding, ExactFieldMorphism):
            raise TypeError("the base inclusion K -> L must be an exact field morphism")
        if not isinstance(closure_embedding, ExactFieldMorphism):
            raise TypeError("the realization L -> Kbar must be an exact field morphism")
        if (
            base_embedding.domain() is not self._base_field
            or base_embedding.codomain() is not self._field
        ):
            raise ValueError("the base inclusion has the wrong endpoints")
        if (
            closure_embedding.domain() is not self._field
            or closure_embedding.codomain() is not self._closure
        ):
            raise ValueError("the closure inclusion has the wrong endpoints")
        self._base_embedding = base_embedding
        self._closure_embedding = closure_embedding
        compatible_embeddings = [
            candidate
            for candidate in exact_embeddings(self._field, self._closure)
            if all(
                candidate(self._base_embedding(generator))
                == self._closure_embedding(self._base_embedding(generator))
                for generator in field_generators(self._base_field)
            )
        ]
        if len(compatible_embeddings) != self.degree():
            raise ValueError(
                "a represented finite extension must be separable over its base field"
            )
        self._automorphisms: tuple[ExactFieldMorphism, ...] | None = None

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

    def automorphisms(self) -> tuple[ExactFieldMorphism, ...]:
        if self._automorphisms is None:
            automorphisms = []
            base_generators = field_generators(self.base_field())
            for candidate in exact_embeddings(self.field(), self.field()):
                if all(
                    candidate(self.base_embedding()(generator))
                    == self.base_embedding()(generator)
                    for generator in base_generators
                ):
                    automorphisms.append(candidate)
            if len(automorphisms) != self.degree():
                raise ValueError(
                    f"{self.field()} is not represented as a finite Galois extension "
                    f"of {self.base_field()}"
                )
            self._automorphisms = tuple(automorphisms)
        return self._automorphisms

    def is_galois(self) -> bool:
        try:
            self.automorphisms()
        except ValueError:
            return False
        return True

    def _repr_(self) -> str:
        return f"Finite Galois extension {self.field()} / {self.base_field()} in {self.algebraic_closure()}"


def _morphism_signature(morphism: ExactFieldMorphism) -> tuple:
    return tuple(
        morphism(generator) for generator in field_generators(morphism.domain())
    )


class FiniteGaloisAutomorphism(Element):
    r"""An exact (K)-automorphism of a represented finite extension (L/K)."""

    def __init__(self, parent, index: int) -> None:
        Element.__init__(self, parent)
        self._index = int(index)

    def action(self) -> ExactFieldMorphism:
        parent = cast("FiniteGaloisQuotient", self.parent())
        return parent.automorphisms()[self._index]

    as_morphism = action

    def __call__(self, element):
        return self.action()(element)

    def __mul__(self, other):
        if (
            not isinstance(other, FiniteGaloisAutomorphism)
            or other.parent() is not self.parent()
        ):
            return NotImplemented
        return self.parent().compose(self, other)

    def __invert__(self):
        return self.inverse()

    def inverse(self):
        return self.parent().inverse(self)

    def multiplicative_order(self):
        value = self.parent().one()
        for order in range(1, int(self.parent().order()) + 1):
            value = value * self
            if value == self.parent().one():
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

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FiniteGaloisAutomorphism)
            and other.parent() is self.parent()
            and other._index == self._index
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._index))

    def _repr_(self) -> str:
        return repr(self.action())


class FiniteGaloisQuotient(Parent):
    r"""The finite quotient (\operatorname{Gal}(L/K)) as exact field maps."""

    Element = FiniteGaloisAutomorphism

    def __init__(self, extension: FiniteGaloisExtension) -> None:
        if not isinstance(extension, FiniteGaloisExtension):
            raise TypeError(
                "a finite Galois quotient requires represented extension data"
            )
        self._extension = extension
        self._automorphisms = extension.automorphisms()
        self._signatures = {
            _morphism_signature(automorphism): index
            for index, automorphism in enumerate(self._automorphisms)
        }
        identity_signature = tuple(field_generators(extension.field()))
        try:
            self._identity_index = self._signatures[identity_signature]
        except KeyError as error:
            raise ValueError(
                "the enumerated automorphisms omit the identity"
            ) from error
        Parent.__init__(self, category=OwnedFiniteGroups())

    def extension_data(self) -> FiniteGaloisExtension:
        return self._extension

    def top_field(self):
        return self._extension.field()

    def base_field(self):
        return self._extension.base_field()

    def automorphisms(self) -> tuple[ExactFieldMorphism, ...]:
        return self._automorphisms

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def _element_constructor_(self, datum):
        if isinstance(datum, FiniteGaloisAutomorphism):
            if datum.parent() is self:
                return datum
            datum = datum.action()
        if isinstance(datum, ExactFieldMorphism):
            try:
                return self.element_class(
                    self, self._signatures[_morphism_signature(datum)]
                )
            except KeyError as error:
                raise ValueError(
                    "the map is not an automorphism in this quotient"
                ) from error
        index = int(datum)
        if index < 0 or index >= len(self._automorphisms):
            raise ValueError("the automorphism index is outside this finite quotient")
        return self.element_class(self, index)

    def __iter__(self):
        return iter(
            tuple(
                self.element_class(self, index)
                for index in range(len(self._automorphisms))
            )
        )

    def one(self):
        return self.element_class(self, self._identity_index)

    def order(self):
        return ZZ(len(self._automorphisms))

    cardinality = order

    def compose(self, left, right):
        images = tuple(
            left(right(generator)) for generator in field_generators(self.top_field())
        )
        try:
            return self.element_class(self, self._signatures[images])
        except KeyError as error:
            raise ArithmeticError(
                "the finite automorphism list is not closed under composition"
            ) from error

    def inverse(self, element):
        for candidate in self:
            if element * candidate == self.one() and candidate * element == self.one():
                return candidate
        raise ArithmeticError("the represented finite automorphism has no inverse")

    def group_generators(self):
        from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

        nonidentity = tuple(element for element in self if element != self.one())
        if self._is_relative_finite_field():
            generators = tuple(
                element
                for element in nonidentity
                if element.multiplicative_order() == self.order()
            )
            if self.order() > 1 and not generators:
                raise ArithmeticError(
                    "the relative finite-field Galois group is not procyclic"
                )
            return finite_ordered_set(generators[:1])
        return finite_ordered_set(nonidentity)

    def _is_relative_finite_field(self) -> bool:
        from sage.categories.finite_fields import FiniteFields

        return _engine_ring(self.top_field()) in FiniteFields()

    def is_abelian(self) -> bool:
        return all(left * right == right * left for left in self for right in self)

    def _repr_(self) -> str:
        return f"Gal({self.top_field()} / {self.base_field()})"


class ContinuousGroupHomset(Homset):
    def __init__(self, domain, codomain) -> None:
        Homset.__init__(self, domain, codomain, category=SageGroups())


def continuous_group_homset(domain, codomain):
    return ContinuousGroupHomset(domain, codomain)


class GaloisRestrictionMap(Morphism):
    r"""The continuous quotient map (G_K\to\operatorname{Gal}(L/K))."""

    def __init__(self, domain, codomain: FiniteGaloisQuotient) -> None:
        extension = domain.extension_data(codomain.extension_data())
        Morphism.__init__(self, continuous_group_homset(domain, codomain))
        self._extension = extension

    def extension(self) -> FiniteGaloisExtension:
        return self._extension

    def _call_(self, element):
        coordinate = getattr(element, "restriction_coordinate", lambda _stage: None)(
            self.extension()
        )
        if coordinate is not None:
            return self.codomain()(coordinate)
        embedding = self.extension().embedding()
        generators = field_generators(self.extension().field())
        images = tuple(element(embedding(generator)) for generator in generators)
        for candidate in self.codomain():
            if all(
                image == embedding(candidate(generator))
                for generator, image in zip(generators, images, strict=True)
            ):
                return candidate
        raise ValueError(
            "the represented automorphism does not preserve this finite stage"
        )

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

    def ambient(self):
        return self._restriction_map.domain()

    def finite_automorphism(self):
        return self._element

    def extension(self) -> FiniteGaloisExtension:
        return self._restriction_map.extension()

    def kernel(self):
        return self._restriction_map.kernel()

    def __contains__(self, candidate) -> bool:
        try:
            return self._restriction_map(candidate) == self._element
        except (TypeError, ValueError, NotImplementedError):
            return False

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
        if self.ambient()._is_finite_field():
            return self.ambient().lift(self._element)
        raise ValueError(
            "this extension coset has no canonically selected representative"
        )

    def _repr_(self) -> str:
        return f"Lift coset of {self._element} in {self.ambient()}"


def restrict_along(
    automorphism: ExactFieldMorphism, embedding: ExactFieldMorphism
) -> ExactFieldMorphism:
    r"""Solve (j\tau=\sigma j) for the exact restriction ``tau``."""
    candidates = exact_embeddings(embedding.domain(), embedding.domain())
    generators = field_generators(embedding.domain())
    restrictions = [
        candidate
        for candidate in candidates
        if all(
            embedding(candidate(generator)) == automorphism(embedding(generator))
            for generator in generators
        )
    ]
    if len(restrictions) != 1:
        raise ValueError(
            "the automorphism does not have a unique restriction along this embedding"
        )
    return restrictions[0]


def extensions_along(automorphism, embedding, candidates):
    r"""Return exactly the candidate automorphisms satisfying (\sigma j=j\tau)."""
    generators = field_generators(embedding.domain())
    matches = [
        candidate
        for candidate in candidates
        if all(
            candidate(embedding(generator)) == embedding(automorphism(generator))
            for generator in generators
        )
    ]
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
    return finite_ordered_set(matches)


__all__ = [
    "ContinuousGroupHomset",
    "FiniteGaloisAutomorphism",
    "FiniteGaloisExtension",
    "FiniteGaloisQuotient",
    "GaloisRestrictionMap",
    "LiftCoset",
    "continuous_group_homset",
    "extensions_along",
    "restrict_along",
]
