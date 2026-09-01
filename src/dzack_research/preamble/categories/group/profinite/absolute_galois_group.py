r"""The realized parent (G_K=\operatorname{Aut}_K(\bar K))."""

from typing import cast

from sage.categories.finite_fields import FiniteFields
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CosliceCategory,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_group_element import (
    AbsoluteGaloisGroupElement,
    FrobeniusElement,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    absolute_galois_group_category,
)
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    ExactFieldMorphism,
    exact_embeddings,
    exact_field_homset,
    exact_field_morphism,
    field_generators,
    first_exact_embedding,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    FiniteGaloisAutomorphism,
    FiniteGaloisExtension,
    FiniteGaloisQuotient,
    GaloisRestrictionMap,
    LiftCoset,
)
from dzack_research.preamble.categories.rings.rings import (
    OwnedFields,
    engine_ring,
    own_ring,
)
from dzack_research.preamble.refine import refine


def _as_exact_embedding(domain, codomain, embedding) -> ExactFieldMorphism:
    domain = own_ring(domain)
    codomain = own_ring(codomain)
    if isinstance(embedding, ExactFieldMorphism):
        if embedding.domain() is not domain or embedding.codomain() is not codomain:
            raise ValueError("the supplied exact embedding has the wrong endpoints")
        return embedding
    if not isinstance(embedding, Map):
        raise TypeError("an embedding must be an exact Sage field morphism")
    return exact_field_morphism(domain, codomain, embedding)


class AbsoluteGaloisSliceAutomorphism(Morphism):
    r"""The commuting square in (K/\mathbf{Fields}) defined by an element of (G_K)."""

    def __init__(self, parent, element) -> None:
        Morphism.__init__(self, parent)
        if not element.fixes_base_field():
            raise ValueError("the closure automorphism does not commute with K -> Kbar")
        self._left = exact_field_homset(
            element.parent().base_field(),
            element.parent().base_field(),
        ).identity()
        self._right = element

    def left(self):
        return self._left

    def right(self):
        return self._right

    def components(self):
        return self._left, self._right

    def __mul__(self, other):
        if not isinstance(other, AbsoluteGaloisSliceAutomorphism):
            return NotImplemented
        if other._right.parent() is not self._right.parent():
            return NotImplemented
        return self._right.parent().slice_automorphism(self._right * other._right)

    def inverse(self):
        return self._right.parent().slice_automorphism(self._right.inverse())

    def __invert__(self):
        return self.inverse()

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, AbsoluteGaloisSliceAutomorphism)
            and other._right.parent() is self._right.parent()
            and other._right == self._right
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self._right.parent()), self._right))

    def _repr_(self) -> str:
        return f"Slice automorphism induced by {self._right}"


class AbsoluteGaloisGroup(Homset):
    r"""The automorphism group of one exact extension object (K\to\bar K).

    The extension is an object of the coslice category (K/\mathbf{Fields}),
    equivalently an object of the slice of affine schemes over
    (\operatorname{Spec}K).  Elements are precisely closure automorphisms
    commuting with that structure map.
    """

    Element = AbsoluteGaloisGroupElement

    def __init__(self, field, *, closure=None, embedding=None) -> None:
        self._field = own_ring(field)
        computation_field = engine_ring(self._field)
        if closure is None:
            closure = computation_field.algebraic_closure()
        self._closure = own_ring(closure)
        if embedding is None:
            embedding = first_exact_embedding(self._field, self._closure)
        self._embedding = _as_exact_embedding(self._field, self._closure, embedding)
        self._extension_cache: dict[object, FiniteGaloisExtension] = {}
        self._quotient_cache: dict[int, FiniteGaloisQuotient] = {}
        self._one_element = None
        category = absolute_galois_group_category(self._field)
        Homset.__init__(
            self,
            self._closure,
            self._closure,
            category=category,
            check=False,
        )
        refine(self, category)
        self._slice_category = CosliceCategory(OwnedFields(), self._field)
        self._extension_object = self._slice_category(self._embedding)

    def base_field(self):
        return self._field

    def algebraic_closure(self):
        return self._closure

    def base_embedding(self) -> ExactFieldMorphism:
        return self._embedding

    geometric_point = base_embedding

    def slice_category(self):
        return self._slice_category

    def extension_object(self):
        return self._extension_object

    slice_object = extension_object

    def slice_automorphism(self, element):
        r"""Regard ``element`` as the commuting automorphism square of (K\to\bar K)."""
        element = element if element in self else self(element)
        extension = self.extension_object()
        return AbsoluteGaloisSliceAutomorphism(
            self.slice_category().hom(extension, extension),
            element,
        )

    def is_profinite(self) -> bool:
        return True

    def is_finite(self):
        return False if self._is_finite_field() else Unknown

    def order(self):
        return Infinity if self._is_finite_field() else Unknown

    cardinality = order

    def is_abelian(self):
        return True if self._is_finite_field() else Unknown

    def is_finitely_generated(self):
        return False if self._is_finite_field() else Unknown

    def _is_finite_field(self) -> bool:
        return engine_ring(self._field) in FiniteFields()

    def base_field_order(self):
        if not self._is_finite_field():
            raise TypeError("q is defined here only for a finite base field")
        return ZZ(engine_ring(self._field).cardinality())

    def _element_constructor_(self, datum=None, **options):
        if isinstance(datum, AbsoluteGaloisGroupElement):
            if datum.parent() is self:
                return datum
            raise ValueError(
                "the automorphism belongs to a different realized absolute Galois group"
            )
        if isinstance(datum, ExactFieldMorphism):
            if (
                datum.domain() is not self._closure
                or datum.codomain() is not self._closure
            ):
                raise ValueError(
                    "a global automorphism must be an endomorphism of the chosen closure"
                )
            element = self.element_class(self, exact_action=datum)
        else:
            raise TypeError("an element requires an exact closure automorphism")
        if not element.fixes_base_field():
            raise ValueError(
                "the closure automorphism does not fix the embedded base field"
            )
        return element

    def __contains__(self, element) -> bool:
        if isinstance(element, AbsoluteGaloisGroupElement):
            return element.parent() is self
        if isinstance(element, ExactFieldMorphism):
            try:
                realized = cast(AbsoluteGaloisGroupElement, self(element))
                return realized.fixes_base_field()
            except (TypeError, ValueError):
                return False
        return False

    def __eq__(self, other) -> bool:
        return self is other

    def __hash__(self) -> int:
        return id(self)

    def one(self):
        if self._one_element is None:
            if self._is_finite_field():
                self._one_element = FrobeniusElement(self, ZZ.zero())
            else:
                identity = exact_field_homset(self._closure, self._closure).identity()
                self._one_element = self.element_class(self, exact_action=identity)
        return self._one_element

    def an_element(self):
        return self.frobenius() if self._is_finite_field() else self.one()

    def frobenius(self, prime=None):
        r"""Return (x\mapsto x^q) for finite fields, or a local class at ``prime``."""
        if self._is_finite_field() and prime is None:
            return FrobeniusElement(self, ZZ.one())
        if prime is None:
            raise TypeError(
                "a non-finite field has Frobenius only at a specified prime"
            )
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            FrobeniusConjugacyClass,
        )

        return FrobeniusConjugacyClass(self, prime)

    def topological_group_generators(self):
        if not self._is_finite_field():
            raise NotImplementedError(
                "no topological generating family is selected for this field"
            )
        return (self.frobenius(),)

    def _finite_frobenius_image(self, element, exponent):
        if not self._is_finite_field():
            raise TypeError("q-Frobenius acts only for a finite base field")
        exponent = ZZ(exponent)
        if exponent == 0:
            return element
        q = self.base_field_order()
        if exponent > 0:
            return element ** (q**exponent)
        degree_over_prime = ZZ(element.minpoly().degree())
        base_degree = ZZ(engine_ring(self._field).degree())
        orbit_order = degree_over_prime // degree_over_prime.gcd(base_degree)
        positive_exponent = exponent % orbit_order
        return element ** (q**positive_exponent)

    def _compose_elements(self, left, right):
        if (
            left.frobenius_exponent() is not None
            and right.frobenius_exponent() is not None
        ):
            return FrobeniusElement(
                self, left.frobenius_exponent() + right.frobenius_exponent()
            )
        if left == self.one():
            return right
        if right == self.one():
            return left
        left_action = left.exact_action()
        right_action = right.exact_action()
        if left_action is not None and right_action is not None:
            return self(left_action * right_action)
        raise NotImplementedError(
            "composition requires globally exact realization data"
        )

    def _inverse_element(self, element):
        if element.frobenius_exponent() is not None:
            return FrobeniusElement(self, -element.frobenius_exponent())
        if element == self.one():
            return self.one()
        exact = element.exact_action()
        if exact is not None:
            inverse_backend = exact.engine_morphism().inverse()
            inverse = exact_field_homset(self._closure, self._closure)(inverse_backend)
            return self(inverse)
        raise NotImplementedError(
            "the inverse requires globally exact realization data"
        )

    def _compatible_base_embedding(self, extension_field, closure_embedding):
        if extension_field is self._field:
            return exact_field_homset(self._field, self._field).identity()
        compatible = []
        for candidate in exact_embeddings(self._field, extension_field):
            if all(
                closure_embedding(candidate(generator)) == self._embedding(generator)
                for generator in field_generators(self._field)
            ):
                compatible.append(candidate)
        if len(compatible) != 1:
            raise ValueError(
                "the represented extension must contain the chosen copy of the base field"
            )
        return compatible[0]

    def extension_data(self, extension, *, embedding=None, base_embedding=None):
        if isinstance(extension, FiniteGaloisExtension):
            if (
                extension.base_field() is not self._field
                or extension.algebraic_closure() is not self._closure
                or extension.embedding() * extension.base_embedding() != self._embedding
            ):
                raise ValueError(
                    "the finite extension belongs to a different realization"
                )
            return extension
        extension_field = own_ring(extension)
        if (
            extension_field is self._field
            and embedding is None
            and base_embedding is None
        ):
            closure_candidates = (self._embedding,)
            base_candidates = (exact_field_homset(self._field, self._field).identity(),)
        else:
            closure_candidates = (
                exact_embeddings(extension_field, self._closure)
                if embedding is None
                else (_as_exact_embedding(extension_field, self._closure, embedding),)
            )
            base_candidates = (
                exact_embeddings(self._field, extension_field)
                if base_embedding is None
                else (
                    _as_exact_embedding(self._field, extension_field, base_embedding),
                )
            )
        compatible_pairs = [
            (candidate_base, candidate_closure)
            for candidate_closure in closure_candidates
            for candidate_base in base_candidates
            if candidate_closure * candidate_base == self._embedding
        ]
        if not compatible_pairs:
            raise ValueError("K -> L -> Kbar does not equal the chosen base embedding")
        base_embedding, closure_embedding = compatible_pairs[0]
        return FiniteGaloisExtension(
            self._field,
            extension_field,
            base_embedding,
            self._closure,
            closure_embedding,
        )

    def finite_extension(self, degree):
        r"""Return the canonical degree-``degree`` stage for a finite base field."""
        if not self._is_finite_field():
            raise TypeError(
                "degree-indexed canonical stages are specific to finite fields"
            )
        degree = ZZ(degree)
        if degree <= 0:
            raise ValueError("an extension degree must be positive")
        cached = self._extension_cache.get(degree)
        if cached is not None:
            return cached
        total_degree = ZZ(engine_ring(self._field).degree()) * degree
        field_engine, embedding_engine = engine_ring(self._closure).subfield(
            total_degree
        )
        extension_field = own_ring(field_engine)
        closure_embedding = exact_field_morphism(
            extension_field, self._closure, embedding_engine
        )
        stage = self.extension_data(extension_field, embedding=closure_embedding)
        self._extension_cache[degree] = stage
        return stage

    def finite_quotient(self, extension):
        stage = self.extension_data(extension)
        key = id(stage)
        quotient = self._quotient_cache.get(key)
        if quotient is None:
            quotient = FiniteGaloisQuotient(stage)
            self._quotient_cache[key] = quotient
        return quotient

    def restriction_map(self, extension):
        return GaloisRestrictionMap(self, self.finite_quotient(extension))

    def lift(self, finite_automorphism):
        if not isinstance(finite_automorphism, FiniteGaloisAutomorphism):
            raise TypeError("a lift starts from an exact finite Galois automorphism")
        quotient = finite_automorphism.parent()
        stage = self.extension_data(quotient.extension_data())
        if self._is_finite_field():
            generator = field_generators(stage.field())[0]
            q = self.base_field_order()
            for exponent in range(int(stage.degree())):
                if finite_automorphism(generator) == generator ** (q**exponent):
                    return FrobeniusElement(self, exponent)
            raise ValueError(
                "the finite automorphism is not a relative q-Frobenius power"
            )
        raise ValueError(
            "a finite automorphism determines an extension coset, not a canonical "
            "absolute automorphism; use lifts()"
        )

    def lifts(self, finite_automorphism):
        if not isinstance(finite_automorphism, FiniteGaloisAutomorphism):
            raise TypeError("extensions start from an exact finite Galois automorphism")
        quotient = finite_automorphism.parent()
        self.extension_data(quotient.extension_data())
        return LiftCoset(GaloisRestrictionMap(self, quotient), finite_automorphism)

    def open_subgroup(self, extension, embedding=None):
        from dzack_research.preamble.categories.group.profinite.absolute_galois_group_subgroup import (
            OpenAbsoluteGaloisSubgroup,
        )

        stage = self.extension_data(extension, embedding=embedding)
        return OpenAbsoluteGaloisSubgroup(self, stage)

    def open_subgroup_class(self, extension):
        from dzack_research.preamble.categories.group.profinite.absolute_galois_group_subgroup import (
            OpenGaloisSubgroupConjugacyClass,
        )

        return OpenGaloisSubgroupConjugacyClass(self, extension)

    def decomposition_group(self, prime, *, prolongation):
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            AbsoluteDecompositionGroup,
        )

        return AbsoluteDecompositionGroup(self, prime, prolongation)

    def decomposition_group_class(self, prime):
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            DecompositionGroupConjugacyClass,
        )

        return DecompositionGroupConjugacyClass(self, prime)

    def inertia_group(self, prime, *, prolongation):
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            AbsoluteInertiaGroup,
        )

        return AbsoluteInertiaGroup(self, prime, prolongation)

    def inertia_group_class(self, prime):
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            InertiaGroupConjugacyClass,
        )

        return InertiaGroupConjugacyClass(self, prime)

    def frobenius_class(self, prime):
        from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
            FrobeniusConjugacyClass,
        )

        return FrobeniusConjugacyClass(self, prime)

    def cyclotomic_character(self, n):
        from dzack_research.preamble.categories.group.profinite.galois_characters import (
            CyclotomicCharacter,
        )

        return CyclotomicCharacter(self, n)

    def quadratic_character(self, a):
        from dzack_research.preamble.categories.group.profinite.galois_characters import (
            QuadraticCharacter,
        )

        return QuadraticCharacter(self, a)

    def _repr_(self) -> str:
        return f"Aut({self._closure} / {self._field})"


absolute_galois_group = AbsoluteGaloisGroup


__all__ = [
    "AbsoluteGaloisGroup",
    "AbsoluteGaloisSliceAutomorphism",
    "absolute_galois_group",
]
