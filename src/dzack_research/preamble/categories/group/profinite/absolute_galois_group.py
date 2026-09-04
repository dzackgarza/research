r"""The realized parent (G_K=\operatorname{Aut}_K(\bar K))."""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
from typing import cast

from sage.categories.finite_fields import FiniteFields
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CosliceCategory,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    OpenAbsoluteGaloisSubgroups,
    absolute_galois_group_category,
)
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    ExactFieldMorphism,
    exact_embeddings,
    exact_field_homset,
    _exact_field_morphism_from_engine,
    field_generators,
    first_exact_embedding,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    FiniteGaloisAutomorphism,
    FiniteGaloisExtension,
    FiniteGaloisQuotient,
    GaloisRestrictionMap,
    LiftCoset,
    continuous_group_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.refine import refine


class AbsoluteGaloisGroupElement(Morphism):
    r"""A coherent, progressively realized automorphism of the chosen closure.

    A global exact map may be supplied directly.  A lift from a finite
    quotient instead starts with one exact finite coordinate; additional
    coordinates can be installed only after their compatibility is checked.
    """

    def __init__(
        self,
        parent,
        *,
        exact_action: ExactFieldMorphism | None = None,
        coordinates=(),
        frobenius_exponent=None,
    ) -> None:
        Morphism.__init__(self, parent)
        self._exact_action = exact_action
        self._coordinates = list(coordinates)
        self._frobenius_exponent = (
            None if frobenius_exponent is None else ZZ(frobenius_exponent)
        )
        if self._exact_action is None and self._frobenius_exponent is None:
            raise TypeError(
                "an absolute Galois element requires a globally exact action"
            )

    def as_morphism(self):
        return self

    def exact_action(self):
        return self._exact_action

    def realized_stages(self) -> tuple:
        return tuple(stage for stage, _coordinate in self._coordinates)

    def restriction_coordinate(self, stage):
        for known_stage, coordinate in self._coordinates:
            if known_stage is stage:
                return coordinate
            if (
                known_stage.field() is stage.field()
                and known_stage.embedding() == stage.embedding()
            ):
                return coordinate
        return None

    def extend_coordinate(self, restriction_map, coordinate) -> None:
        r"""Install a higher finite coordinate after checking compatibility."""
        stage = restriction_map.extension()
        coordinate = restriction_map.codomain()(coordinate)
        for old_stage, old_coordinate in self._coordinates:
            if old_stage is stage:
                if old_coordinate != coordinate:
                    raise ValueError(
                        "the new coordinate contradicts the realized coordinate"
                    )
                return
        if restriction_map(self) != coordinate:
            raise ValueError("the new coordinate contradicts the global automorphism")
        self._coordinates.append((stage, coordinate))

    def frobenius_exponent(self):
        return self._frobenius_exponent

    def is_globally_evaluable(self) -> bool:
        return self._frobenius_exponent is not None or self._exact_action is not None

    def __call__(self, element):
        r"""Evaluate without forcing a finite-stage element through the closure facade."""
        return self._call_(element)

    def _call_(self, element):
        if self._frobenius_exponent is not None:
            return self.parent()._finite_frobenius_image(
                element, self._frobenius_exponent
            )
        if self._exact_action is not None:
            return self._exact_action(element)
        raise NotImplementedError("this automorphism has no global exact action")

    def fixes_base_field(self) -> bool:
        parent = cast("AbsoluteGaloisGroup", self.parent())
        embedding = parent.base_embedding()
        try:
            return all(
                self(embedding(generator)) == embedding(generator)
                for generator in field_generators(parent.base_field())
            )
        except NotImplementedError:
            return False

    def restrict(self, stage):
        return self.parent().restriction_map(stage)(self)

    def __mul__(self, other):
        if isinstance(other, AbsoluteGaloisGroupElement):
            if other.parent() is not self.parent():
                return NotImplemented
            return self.parent()._compose_elements(self, other)
        return Morphism.__mul__(self, other)

    def __invert__(self):
        return self.inverse()

    def inverse(self):
        return self.parent()._inverse_element(self)

    def __pow__(self, exponent):
        exponent = ZZ(exponent)
        if self._frobenius_exponent is not None:
            return FrobeniusElement(self.parent(), exponent * self._frobenius_exponent)
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

    def conjugacy_class(self):
        return ElementConjugacyClass(self.parent(), self)

    def __eq__(self, other) -> bool:
        if (
            not isinstance(other, AbsoluteGaloisGroupElement)
            or other.parent() is not self.parent()
        ):
            return False
        if (
            self._frobenius_exponent is not None
            or other._frobenius_exponent is not None
        ):
            return self._frobenius_exponent == other._frobenius_exponent
        if self._exact_action is not None and other._exact_action is not None:
            return self._exact_action == other._exact_action
        return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        datum: tuple[object, ...]
        if self._frobenius_exponent is not None:
            datum = ("frobenius", self._frobenius_exponent)
        elif self._exact_action is not None:
            datum = ("exact", self._exact_action)
        else:
            datum = ("unrealized",)
        return hash((id(self.parent()), datum))

    def _repr_(self) -> str:
        if self._frobenius_exponent is not None:
            parent = cast("AbsoluteGaloisGroup", self.parent())
            q = parent.base_field_order()
            return f"q-Frobenius^{self._frobenius_exponent} (q={q})"
        if self._exact_action is not None:
            return f"Element of {self.parent()} represented by {self._exact_action}"
        fields = ", ".join(str(stage.field()) for stage, _ in self._coordinates)
        return f"Element of {self.parent()} realized on {fields}"


class FrobeniusElement(AbsoluteGaloisGroupElement):
    r"""An integral power of the canonical (q)-Frobenius."""

    def __init__(self, parent, exponent=1) -> None:
        super().__init__(parent, frobenius_exponent=ZZ(exponent))


class ElementConjugacyClass(SageObject):
    r"""The conjugacy class of a represented global automorphism."""

    def __init__(self, ambient, representative) -> None:
        self._ambient = ambient
        self._representative = representative

    def ambient(self):
        return self._ambient

    def representative(self):
        return self._representative

    def __contains__(self, element) -> bool:
        if self._ambient.is_abelian() is not True:
            raise NotImplementedError(
                "conjugacy membership is not decided for this absolute Galois group"
            )
        if element not in self._ambient:
            return False
        return element == self._representative

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, ElementConjugacyClass):
            return False
        if other._ambient is not self._ambient:
            return False
        if self._ambient.is_abelian() is not True:
            raise NotImplementedError(
                "conjugacy-class equality is not decided for this absolute Galois group"
            )
        return other._representative == self._representative

    def __hash__(self) -> int:
        if self._ambient.is_abelian() is not True:
            raise TypeError(
                "undecided absolute-Galois conjugacy classes are not hashable"
            )
        return hash((id(self._ambient), self._representative))

    def _repr_(self) -> str:
        return f"Conjugacy class of {self._representative} in {self._ambient}"

def _as_exact_embedding(domain, codomain, embedding) -> ExactFieldMorphism:
    domain = _own_ring(domain)
    codomain = _own_ring(codomain)
    if isinstance(embedding, ExactFieldMorphism):
        if embedding.domain() is not domain or embedding.codomain() is not codomain:
            raise ValueError("the supplied exact embedding has the wrong endpoints")
        return embedding
    if not isinstance(embedding, Map):
        raise TypeError("an embedding must be an exact Sage field morphism")
    return _exact_field_morphism_from_engine(domain, codomain, embedding)


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


class AbsoluteGaloisGroup(OwnedHomset):
    r"""The automorphism group of one exact extension object (K\to\bar K).

    The extension is an object of the coslice category (K/\mathbf{Fields}),
    equivalently an object of the slice of affine schemes over
    (\operatorname{Spec}K).  Elements are precisely closure automorphisms
    commuting with that structure map.
    """

    Element = AbsoluteGaloisGroupElement

    def __init__(self, field, *, closure=None, embedding=None) -> None:
        self._field = _own_ring(field)
        computation_field = _engine_ring(self._field)
        if closure is None:
            closure = computation_field.algebraic_closure()
        self._closure = _own_ring(closure)
        if embedding is None:
            embedding = first_exact_embedding(self._field, self._closure)
        self._embedding = _as_exact_embedding(self._field, self._closure, embedding)
        self._extension_cache: dict[object, FiniteGaloisExtension] = {}
        self._quotient_cache: dict[int, FiniteGaloisQuotient] = {}
        self._one_element = None
        category = absolute_galois_group_category(self._field)
        from sage.categories.sets_cat import Sets as SageSets
        Homset.__init__(
            self,
            self._closure,
            self._closure,
            category=SageSets(),
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
            self.slice_category().mor(extension, extension),
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
        return _engine_ring(self._field) in FiniteFields()

    def base_field_order(self):
        if not self._is_finite_field():
            raise TypeError("q is defined here only for a finite base field")
        return ZZ(_engine_ring(self._field).cardinality())

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
        degree_over_prime = ZZ(int(element.minpoly().degree()))
        base_degree = ZZ(_engine_ring(self._field).degree())
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
            inverse_backend = exact._engine_morphism_crossing().inverse()
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
        extension_field = _own_ring(extension)
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
        total_degree = ZZ(_engine_ring(self._field).degree()) * degree
        field_engine, embedding_engine = _engine_ring(self._closure).subfield(
            total_degree
        )
        extension_field = _own_ring(field_engine)
        closure_embedding = _exact_field_morphism_from_engine(
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
        stage = self.extension_data(extension, embedding=embedding)
        return OpenAbsoluteGaloisSubgroup(self, stage)

    def open_subgroup_class(self, extension):
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


class OpenSubgroupInclusion(Morphism):
    r"""The literal inclusion of a realized open subgroup into its ambient group."""

    def __init__(self, subgroup) -> None:
        Morphism.__init__(
            self,
            continuous_group_homset(subgroup, subgroup.ambient()),
        )

    def _call_(self, element):
        subgroup = self.domain()
        element = subgroup(element)
        ambient = self.codomain()
        exponent = element.frobenius_exponent()
        if exponent is not None and ambient._is_finite_field():
            return FrobeniusElement(ambient, subgroup.index() * exponent)
        exact = element.exact_action()
        if exact is not None:
            return ambient(exact)
        raise NotImplementedError("the subgroup element has no global exact action")

    def is_injective(self) -> bool:
        return True

    def is_continuous(self) -> bool:
        return True


class OpenAbsoluteGaloisSubgroup(AbsoluteGaloisGroup):
    r"""The actual subgroup fixing one embedded finite extension (E/K)."""

    def __init__(self, ambient, extension: FiniteGaloisExtension) -> None:
        if not isinstance(extension, FiniteGaloisExtension):
            raise TypeError(
                "an open subgroup requires represented finite-extension data"
            )
        extension = ambient.extension_data(extension)
        self._ambient = ambient
        self._fixed_extension = extension
        super().__init__(
            extension.field(),
            closure=ambient.algebraic_closure(),
            embedding=extension.embedding(),
        )
        refine(self, OpenAbsoluteGaloisSubgroups())
        self._inclusion = OpenSubgroupInclusion(self)

    def ambient(self):
        return self._ambient

    def fixed_field(self):
        return self._fixed_extension.field()

    def fixed_extension(self) -> FiniteGaloisExtension:
        return self._fixed_extension

    def embedding(self):
        return self._fixed_extension.embedding()

    def index(self):
        return self._fixed_extension.degree()

    def inclusion(self) -> OpenSubgroupInclusion:
        return self._inclusion

    def is_normal(self) -> bool:
        return self._fixed_extension.is_galois()

    def __contains__(self, element) -> bool:
        if isinstance(element, AbsoluteGaloisGroupElement) and element.parent() is self:
            return True
        if element not in self._ambient:
            return False
        embedding = self.embedding()
        try:
            return all(
                element(embedding(generator)) == embedding(generator)
                for generator in field_generators(self.fixed_field())
            )
        except NotImplementedError:
            return False

    def _element_constructor_(self, datum=None, **options):
        if (
            isinstance(datum, AbsoluteGaloisGroupElement)
            and datum.parent() is self._ambient
        ):
            if datum not in self:
                raise ValueError(
                    "the ambient automorphism does not fix this subgroup's field"
                )
            exponent = datum.frobenius_exponent()
            if exponent is not None and self._ambient._is_finite_field():
                if exponent % self.index():
                    raise ValueError(
                        "the Frobenius power is outside this open subgroup"
                    )
                return FrobeniusElement(self, exponent // self.index())
            exact = datum.exact_action()
            if exact is not None:
                return super()._element_constructor_(exact)
            raise NotImplementedError("the ambient element has no global exact action")
        return super()._element_constructor_(datum, **options)

    def conjugacy_class(self):
        return OpenGaloisSubgroupConjugacyClass(self._ambient, self.fixed_field())

    def core(self):
        if self.is_normal():
            return self
        field = _engine_ring(self.fixed_field())
        base = _engine_ring(self._ambient.base_field())
        defining_base = getattr(field, "base_field", lambda: None)()
        if defining_base is base:
            polynomial = field.relative_polynomial()
        elif base.absolute_degree() == 1:
            polynomial = field.defining_polynomial().change_ring(base)
        else:
            raise NotImplementedError(
                "the relative defining polynomial over the ambient base field is unavailable"
            )

        normal_field, base_backend = polynomial.splitting_field(
            "normal_closure", map=True
        )
        normal_field = _own_ring(normal_field)
        base_embedding = _exact_field_morphism_from_engine(
            self._ambient.base_field(), normal_field, base_backend
        )
        compatible_closure_embeddings = []
        for fixed_to_normal in exact_embeddings(self.fixed_field(), normal_field):
            if not all(
                fixed_to_normal(self._fixed_extension.base_embedding()(generator))
                == base_embedding(generator)
                for generator in field_generators(self._ambient.base_field())
            ):
                continue
            for normal_to_closure in exact_embeddings(
                normal_field, self._ambient.algebraic_closure()
            ):
                if all(
                    normal_to_closure(fixed_to_normal(generator))
                    == self.embedding()(generator)
                    for generator in field_generators(self.fixed_field())
                ):
                    compatible_closure_embeddings.append(normal_to_closure)
        if not compatible_closure_embeddings:
            raise ValueError(
                "the normal closure could not be placed compatibly inside the chosen algebraic closure"
            )
        stage = self._ambient.extension_data(
            normal_field,
            embedding=compatible_closure_embeddings[0],
            base_embedding=base_embedding,
        )
        return self._ambient.open_subgroup(stage)

    def __le__(self, other) -> bool:
        if (
            not isinstance(other, OpenAbsoluteGaloisSubgroup)
            or other.ambient() is not self.ambient()
        ):
            return False
        for embedding in exact_embeddings(other.fixed_field(), self.fixed_field()):
            if all(
                self.embedding()(embedding(generator)) == other.embedding()(generator)
                for generator in field_generators(other.fixed_field())
            ):
                return True
        return False

    def intersection(self, other):
        if (
            not isinstance(other, OpenAbsoluteGaloisSubgroup)
            or other.ambient() is not self.ambient()
        ):
            raise ValueError(
                "open-subgroup intersection requires one ambient Galois group"
            )
        if _engine_ring(self.fixed_field()) in FiniteFields():
            degree = ZZ(self.index()).lcm(ZZ(other.index()))
            return self.ambient().open_subgroup(self.ambient().finite_extension(degree))
        raise NotImplementedError(
            "the compositum must be supplied with its exact closure embedding"
        )

    def _repr_(self) -> str:
        return f"Gal({self.algebraic_closure()} / {self.fixed_field()}) inside {self._ambient}"


class OpenGaloisSubgroupConjugacyClass(SageObject):
    r"""The conjugacy class obtained by forgetting (E\hookrightarrow\bar K)."""

    def __init__(self, ambient, extension_field) -> None:
        self._ambient = ambient
        if isinstance(extension_field, FiniteGaloisExtension):
            if extension_field.base_field() is not ambient.base_field():
                raise ValueError("the extension has the wrong ambient base field")
            self._extension_field = extension_field.field()
            self._base_embedding = extension_field.base_embedding()
        else:
            self._extension_field = _own_ring(extension_field)
            base_embeddings = exact_embeddings(
                ambient.base_field(), self._extension_field
            )
            if len(base_embeddings) != 1:
                raise ValueError(
                    "the K-structure must be supplied as finite extension data"
                )
            self._base_embedding = base_embeddings[0]

    def ambient(self):
        return self._ambient

    def fixed_field(self):
        return self._extension_field

    def base_embedding(self):
        return self._base_embedding

    def index(self):
        from dzack_research.preamble.categories.group.profinite.galois_quotient import (
            _relative_degree,
        )

        return _relative_degree(self._ambient.base_field(), self._extension_field)

    def representative(self, embedding=None):
        if embedding is None:
            candidates = [
                candidate
                for candidate in exact_embeddings(
                    self._extension_field,
                    self._ambient.algebraic_closure(),
                )
                if all(
                    candidate(self._base_embedding(generator))
                    == self._ambient.base_embedding()(generator)
                    for generator in field_generators(self._ambient.base_field())
                )
            ]
            if not candidates:
                raise ValueError(
                    "the K-extension has no compatible embedding in the chosen closure"
                )
            embedding = candidates[0]
        stage = self._ambient.extension_data(
            self._extension_field,
            embedding=embedding,
            base_embedding=self._base_embedding,
        )
        return self._ambient.open_subgroup(stage)

    def __eq__(self, other) -> bool:
        if not isinstance(other, OpenGaloisSubgroupConjugacyClass):
            return False
        if other._ambient is not self._ambient or other.index() != self.index():
            return False
        return any(
            all(
                isomorphism(self._base_embedding(generator))
                == other._base_embedding(generator)
                for generator in field_generators(self._ambient.base_field())
            )
            for isomorphism in exact_embeddings(
                self._extension_field, other._extension_field
            )
        )

    def __hash__(self) -> int:
        return hash((id(self._ambient), self.index()))

    def _repr_(self) -> str:
        return (
            f"Conjugacy class of index-{self.index()} open subgroups of "
            f"{self._ambient} corresponding to {self._extension_field}"
        )


def open_absolute_galois_subgroup(ambient, extension, embedding=None):
    return ambient.open_subgroup(extension, embedding=embedding)

absolute_galois_group = AbsoluteGaloisGroup


__all__ = [
    "AbsoluteGaloisGroup",
    "AbsoluteGaloisGroupElement",
    "AbsoluteGaloisSliceAutomorphism",
    "ElementConjugacyClass",
    "FrobeniusElement",
    "OpenAbsoluteGaloisSubgroup",
    "OpenGaloisSubgroupConjugacyClass",
    "OpenSubgroupInclusion",
    "absolute_galois_group",
    "open_absolute_galois_subgroup",
]
