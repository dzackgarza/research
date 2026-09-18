r"""The realized parent (G_K=\operatorname{Aut}_K(\bar K))."""

from typing import cast

from sage.categories.finite_fields import FiniteFields
from sage.categories.morphism import Morphism
from sage.categories.number_fields import NumberFields
from sage.misc.classcall_metaclass import typecall
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import Element
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    _RestrictedHomCategoryOf,
    RestrictedHomCategoryParent,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    OpenAbsoluteGaloisSubgroups,
    _absolute_galois_group_category,
)
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    ExactFieldMorphism,
    _exact_field_morphism_from_engine,
)
from dzack_research.preamble.categories.group.profinite.galois_characters import (
    CyclotomicCharacter,
    QuadraticCharacter,
)
from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
    AbsoluteDecompositionGroup,
    AbsoluteInertiaGroup,
    DecompositionGroupConjugacyClass,
    FrobeniusConjugacyClass,
    InertiaGroupConjugacyClass,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    FiniteExtensionAutomorphismGroup,
    FiniteGaloisExtension,
    FiniteGaloisQuotient,
    GaloisRestrictionMap,
    LiftCoset,
    _relative_degree,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    OwnedRings,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


class AbsoluteGaloisGroupElement(Element):
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
        Element.__init__(self, parent)
        self._exact_action = exact_action
        self._coordinates = list(coordinates)
        self._frobenius_exponent = (
            None if frobenius_exponent is None else ZZ(frobenius_exponent)
        )
        if self._exact_action is None and self._frobenius_exponent is None:
            raise TypeError(
                "an absolute Galois element requires a globally exact action"
            )

    @cached_method
    def as_morphism(self):
        field_endomorphisms = self.parent().arrow_set()
        if self._exact_action is not None:
            return field_endomorphisms(self._exact_action._engine_morphism_crossing())
        return field_endomorphisms.elementwise(lambda element: self(element))

    underlying_field_morphism = as_morphism

    def domain(self):
        return self.parent().algebraic_closure()

    def codomain(self):
        return self.parent().algebraic_closure()

    def exact_action(self):
        return self._exact_action

    def realized_stages(self):
        return finite_ordered_set(
            tuple(stage for stage, _coordinate in self._coordinates)
        )

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
        r"""Evaluate: a Frobenius power by its exponent, otherwise the exact action; construction supplies one of the two."""
        if self._frobenius_exponent is not None:
            return self.parent()._finite_frobenius_image(
                element, self._frobenius_exponent
            )
        return self._exact_action(element)

    def fixes_base_field(self) -> bool:
        parent = cast("AbsoluteGaloisGroup", self.parent())
        embedding = parent.base_embedding()
        return all(
            self(embedding(generator)) == embedding(generator)
            for generator in parent.base_field().field_generators()
        )

    def restrict(self, stage):
        return self.parent().restriction_map(stage)(self)

    def _mul_(self, other):
        r"""``self ∘ other``; Sage's arithmetic calls this with one parent."""
        return self.parent()._compose_elements(self, other)

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


class _AbsoluteElementConjugacyClassEngine:
    r"""Private realization of a represented absolute-Galois conjugacy orbit."""

    def __init__(self, representative, **rest) -> None:
        self._representative = representative
        super().__init__(**rest)

    def supergroup(self):
        return self.codomain()

    def ambient(self):
        r"""Return the ambient absolute Galois group ``G_K``."""
        return self.supergroup()

    def representative(self):
        return self._representative

    def _repr_(self) -> str:
        return f"Conjugacy class of {self._representative} in {self.supergroup()}"


def ElementConjugacyClass(supergroup, representative):
    r"""The represented conjugacy orbit of ``representative`` as a subset of ``G_K``.

    In the currently decidable absolute-Galois regime the group is abelian, so
    the orbit is the singleton ``{representative}``.  Outside that regime the
    predicate retains the existing assertion frontier rather than identifying
    conjugacy with equality.
    """
    representative = supergroup(representative)

    def is_conjugate(element):
        assert supergroup.is_abelian() is True, (
            "conjugacy membership is represented here when the absolute Galois group is abelian"
        )
        return supergroup(element) == representative

    inclusion = supergroup.condition_set(is_conjugate).inclusion()
    return Sets().Subobjects(supergroup).object(
        inclusion,
        _engine=_AbsoluteElementConjugacyClassEngine,
        construction_data={"representative": representative},
    )


def _as_exact_embedding(domain, codomain, embedding) -> ExactFieldMorphism:
    r"""Read ``embedding`` as an element of the exact field Hom from ``domain`` to ``codomain``.

    That Hom's element constructor admits its own elements and exact Sage
    field maps between the corresponding engine fields, and refuses anything
    else, including a map with other endpoints.
    """
    return _own_ring(domain).exact_morphisms_to(_own_ring(codomain))(embedding)


class AbsoluteGaloisSliceAutomorphism(Morphism):
    r"""The commuting square in (K/\mathbf{Fields}) defined by an element of (G_K)."""

    def __init__(self, parent, element) -> None:
        Morphism.__init__(self, parent)
        if not element.fixes_base_field():
            raise ValueError("the closure automorphism does not commute with K -> Kbar")
        self._element = element
        base = element.parent().base_field()
        self._left = OwnedFields().category_packet().Homs().Of(base, base).identity()
        self._right = element.as_morphism()

    def left(self):
        return self._left

    def right(self):
        return self._right

    def components(self):
        return self._left, self._right

    def __mul__(self, other):
        if not isinstance(other, AbsoluteGaloisSliceAutomorphism):
            return NotImplemented
        if other._element.parent() is not self._element.parent():
            return NotImplemented
        group = self._element.parent()
        return group.slice_automorphism(self._element * other._element)

    def inverse(self):
        return self._element.parent().slice_automorphism(self._element.inverse())

    def __invert__(self):
        return self.inverse()

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, AbsoluteGaloisSliceAutomorphism)
            and other._element.parent() is self._element.parent()
            and other._element == self._element
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self._element.parent()), self._element))

    def _repr_(self) -> str:
        return f"Slice automorphism induced by {self._element}"


class AbsoluteGaloisCategoryConstruction(_RestrictedHomCategoryOf):
    r"""Closure endomorphisms fixing one chosen embedded base field."""

    _declaration_name = "_AbsoluteGaloisCategory"

    @staticmethod
    def __classcall__(cls, base_category, base_field, base_embedding):
        return typecall(cls, base_category, base_field, base_embedding)

    def __init__(self, base_category, base_field, base_embedding) -> None:
        self._base_field = base_field
        self._base_embedding = base_embedding
        super().__init__(base_category)

    def fixed_category_class(self):
        return AbsoluteGaloisGroup

    def accepts(self, arrow) -> bool:
        r"""Whether the closure endomorphism ``arrow`` fixes the embedded base field, read on its generators."""
        return all(
            arrow(self._base_embedding(generator))
            == self._base_embedding(generator)
            for generator in self._base_field.field_generators()
        )


@cached_function(key=lambda field: id(field))
def _canonical_absolute_galois_group(field):
    return typecall(AbsoluteGaloisGroup, field)


class AbsoluteGaloisGroup(RestrictedHomCategoryParent):
    r"""The automorphism group of one exact extension object (K\to\bar K).

    The extension is an object of the coslice category (K/\mathbf{Fields}),
    equivalently an object of the slice of affine schemes over
    (\operatorname{Spec}K).  Elements are precisely closure automorphisms
    commuting with that structure map.
    """

    Element = AbsoluteGaloisGroupElement

    @staticmethod
    def __classcall__(cls, field, closure=None, embedding=None, extra_categories=()):
        r"""``G_K`` for the canonical closure and embedding is one object per field; stated choices construct anew."""
        field = _own_ring(field)
        if closure is None and embedding is None and not extra_categories:
            return _canonical_absolute_galois_group(field)
        return typecall(
            cls,
            field,
            closure=closure,
            embedding=embedding,
            extra_categories=tuple(extra_categories),
        )

    def __init__(
        self,
        field,
        *,
        closure=None,
        embedding=None,
        extra_categories=(),
    ) -> None:
        self._field = _own_ring(field)
        computation_field = _engine_ring(self._field)
        if closure is None:
            closure = computation_field.algebraic_closure()
        self._closure = _own_ring(closure)
        if embedding is None:
            embedding = self._field.first_exact_embedding(self._closure)
        self._embedding = _as_exact_embedding(self._field, self._closure, embedding)
        category = Cat().meet(
            (_absolute_galois_group_category(self._field), *tuple(extra_categories))
        )
        # The elements are field automorphisms of the closure, so this is the
        # subcategory of Aut_Fields(closure) fixing the structure map from K.
        super().__init__(
            AbsoluteGaloisCategoryConstruction(
                OwnedFields(),
                self._field,
                self._embedding,
            ),
            self._closure,
            self._closure,
            category=category,
        )
        self._slice_category = OwnedFields().CosliceUnder(self._field)
        self._extension_object = self._slice_category(self._embedding)

    def base_field(self):
        return self._field

    def algebraic_closure(self):
        return self._closure

    def base_embedding(self) -> ExactFieldMorphism:
        return self._embedding

    geometric_point = base_embedding

    def choice_data(self):
        r"""Return the explicit realization data retained by this parent.

        The live realization records the chosen algebraic closure and base
        embedding.  Later finite-stage embeddings and prolongations are
        supplied as explicit mathematical data at their constructors rather
        than being selected by a hidden global choice policy.
        """
        return {
            "closure": self.algebraic_closure(),
            "embedding": self.base_embedding(),
        }

    def has_canonical_realization(self) -> bool:
        r"""Return whether this realized absolute Galois group is canonical.

        For a finite field the selected profinite group is canonically
        procyclic, with the arithmetic Frobenius as its distinguished
        topological generator.  For a general field the concrete closure and
        base embedding are chosen realization data rather than canonical
        mathematical objects.
        """
        return self._is_finite_field()

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
            self.slice_category().Mor(extension, extension),
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
        r"""Return whether this absolute Galois group is algebraically finitely generated.

        Finite-field absolute Galois groups are procyclic but not algebraically
        generated by Frobenius.  If ``K`` is a number field, then for every
        ``r`` there are multiquadratic finite Galois extensions of ``K`` with
        Galois group ``(C_2)^r``.  Hence ``G_K`` has finite quotients whose
        minimal number of generators is arbitrarily large, so no finite
        algebraic generating set of ``G_K`` can exist.  Outside these two
        represented regimes this parent does not decide the question.
        """
        if self._is_finite_field():
            return False
        computation_field = _engine_ring(self._field)
        if computation_field is SageQQ or computation_field in NumberFields():
            return False
        return Unknown

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
            element = AbsoluteGaloisGroupElement(self, exact_action=datum)
        else:
            raise TypeError("an element requires an exact closure automorphism")
        if not element.fixes_base_field():
            raise ValueError(
                "the closure automorphism does not fix the embedded base field"
            )
        return element

    def __contains__(self, element) -> bool:
        return RestrictedHomCategoryParent.__contains__(self, element)

    def __eq__(self, other) -> bool:
        return self is other

    def __hash__(self) -> int:
        return id(self)

    @cached_method
    def one(self):
        r"""The identity: the zeroth Frobenius power over a finite field, else the identity of the closure."""
        if self._is_finite_field():
            return FrobeniusElement(self, ZZ.zero())
        identity = self._closure.exact_morphisms_to(self._closure).identity()
        return AbsoluteGaloisGroupElement(self, exact_action=identity)

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

        return FrobeniusConjugacyClass(self, prime)

    def topological_group_generators(self):
        assert self._is_finite_field(), (
            "a selected topological generating family is represented here for finite-field absolute Galois groups"
        )
        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            finite_ordered_set,
        )

        return finite_ordered_set((self.frobenius(),))

    def topological_generating_family(self):
        r"""Return the selected topological generating family when represented."""
        return self.topological_group_generators()

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
        assert left_action is not None and right_action is not None, (
            "composing a Frobenius power with an automorphism given by an exact map "
            "requires the Frobenius power as an exact map of the closure, which is not represented"
        )
        return self(left_action * right_action)

    def _inverse_element(self, element):
        r"""``sigma^-1``: the negated Frobenius exponent, else the inverse of the exact action."""
        if element.frobenius_exponent() is not None:
            return FrobeniusElement(self, -element.frobenius_exponent())
        if element == self.one():
            return self.one()
        inverse_backend = element.exact_action()._engine_morphism_crossing().inverse()
        return self(self._closure.exact_morphisms_to(self._closure)(inverse_backend))

    def extension_data(self, extension, *, embedding=None, base_embedding=None):
        r"""The stage ``K -> L -> Kbar`` named by a stage of this realization or by an owned field ``L``.

        For a field the embeddings are the stated ones, or the first pair of
        exact embeddings whose composite is the chosen ``K -> Kbar``.
        """
        if extension not in OwnedRings():
            if (
                extension.base_field() is not self._field
                or extension.algebraic_closure() is not self._closure
                or extension.embedding() * extension.base_embedding() != self._embedding
            ):
                raise ValueError(
                    "the finite extension belongs to a different realization"
                )
            return extension
        extension_field = extension
        if (
            extension_field is self._field
            and embedding is None
            and base_embedding is None
        ):
            closure_candidates = (self._embedding,)
            base_candidates = (self._field.exact_morphisms_to(self._field).identity(),)
        else:
            closure_candidates = (
                extension_field.exact_embeddings(self._closure)
                if embedding is None
                else (_as_exact_embedding(extension_field, self._closure, embedding),)
            )
            base_candidates = (
                self._field.exact_embeddings(extension_field)
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

    @cached_method(key=lambda group, degree: ZZ(degree))
    def finite_extension(self, degree):
        r"""Return the canonical degree-``degree`` stage for a finite base field.

        Over ``F_q`` the unique extension of degree ``d`` inside the chosen
        closure is its subfield of order ``q^d``, so the degree is the whole
        defining datum and one degree names one stage.

        The cache key uses the same exact integer conversion as construction;
        truncating with ``int`` would admit a nonintegral degree on a cache hit.
        """
        assert self._is_finite_field(), (
            "degree-indexed canonical stages are specific to finite fields"
        )
        degree = ZZ(degree)
        assert degree > 0, "an extension degree must be positive"
        total_degree = ZZ(_engine_ring(self._field).degree()) * degree
        field_engine, embedding_engine = _engine_ring(self._closure).subfield(
            total_degree
        )
        extension_field = _own_ring(field_engine)
        closure_embedding = _exact_field_morphism_from_engine(
            extension_field, self._closure, embedding_engine
        )
        return self.extension_data(extension_field, embedding=closure_embedding)

    def finite_quotient(self, extension):
        r"""Return ``Gal(L/K)`` for the finite stage ``L`` named by ``extension``.

        ``extension`` is a stage or a field; both name the stage
        :meth:`extension_data` selects, and the quotient is keyed on that
        stage's defining data, so equal data give one quotient.
        """
        return self._finite_quotient_of_stage(self.extension_data(extension))

    @cached_method
    def _finite_quotient_of_stage(self, stage):
        return FiniteGaloisQuotient(stage)

    def restriction_map(self, extension):
        return GaloisRestrictionMap(self, self.finite_quotient(extension))

    def lift(self, finite_automorphism):
        quotient = finite_automorphism.parent()
        stage = self.extension_data(quotient.extension_data())
        finite_automorphism = FiniteGaloisQuotient(stage)(finite_automorphism)
        if self._is_finite_field():
            generator = stage.field().field_generators()[0]
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
        quotient = finite_automorphism.parent()
        stage = self.extension_data(quotient.extension_data())
        quotient = FiniteGaloisQuotient(stage)
        return LiftCoset(GaloisRestrictionMap(self, quotient), quotient(finite_automorphism))

    def open_subgroup(self, extension, embedding=None):
        stage = self.extension_data(extension, embedding=embedding)
        return OpenAbsoluteGaloisSubgroup(self, stage)

    def open_subgroup_class(self, extension):
        return OpenGaloisSubgroupConjugacyClass(self, extension)

    def decomposition_group(self, prime, *, prolongation):

        return AbsoluteDecompositionGroup(self, prime, prolongation)

    def decomposition_group_class(self, prime):

        return DecompositionGroupConjugacyClass(self, prime)

    def inertia_group(self, prime, *, prolongation):

        return AbsoluteInertiaGroup(self, prime, prolongation)

    def inertia_group_class(self, prime):

        return InertiaGroupConjugacyClass(self, prime)

    def frobenius_class(self, prime):

        return FrobeniusConjugacyClass(self, prime)

    def cyclotomic_character(self, n):

        return CyclotomicCharacter(self, n)

    def quadratic_character(self, a):

        return QuadraticCharacter(self, a)

    def _repr_(self) -> str:
        return f"Aut({self._closure} / {self._field})"


class OpenSubgroupInclusion(Morphism):
    r"""The literal inclusion of a realized open subgroup into its supergroup group."""

    def __init__(self, subgroup) -> None:
        Morphism.__init__(
            self,
            subgroup.continuous_morphisms_to(subgroup.supergroup()),
        )

    def _call_(self, element):
        subgroup = self.domain()
        element = subgroup(element)
        supergroup = self.codomain()
        exponent = element.frobenius_exponent()
        if exponent is not None:
            # A Frobenius power exists only over a finite field, where the
            # q^[E:K]-Frobenius of G_E is the [E:K]-th power of G_K's.
            return FrobeniusElement(supergroup, subgroup.index() * exponent)
        return supergroup(element.exact_action())

    def is_injective(self) -> bool:
        return True

    def is_continuous(self) -> bool:
        return True


class OpenAbsoluteGaloisSubgroup(AbsoluteGaloisGroup):
    r"""The actual subgroup fixing one embedded finite extension (E/K)."""

    @staticmethod
    def __classcall__(cls, supergroup, extension):
        return typecall(cls, supergroup, extension)

    def __init__(self, supergroup, extension: FiniteGaloisExtension) -> None:
        extension = supergroup.extension_data(extension)
        self._supergroup = supergroup
        self._fixed_extension = extension
        super().__init__(
            extension.field(),
            closure=supergroup.algebraic_closure(),
            embedding=extension.embedding(),
            extra_categories=(OpenAbsoluteGaloisSubgroups(),),
        )
        self._inclusion = OpenSubgroupInclusion(self)

    def supergroup(self):
        return self._supergroup

    def ambient(self):
        r"""Return the ambient absolute Galois group ``G_K``."""
        return self.supergroup()

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
        if element not in self._supergroup:
            return False
        embedding = self.embedding()
        return all(
            element(embedding(generator)) == embedding(generator)
            for generator in self.fixed_field().field_generators()
        )

    def _element_constructor_(self, datum=None, **options):
        if (
            isinstance(datum, AbsoluteGaloisGroupElement)
            and datum.parent() is self._supergroup
        ):
            if datum not in self:
                raise ValueError(
                    "the supergroup automorphism does not fix this subgroup's field"
                )
            exponent = datum.frobenius_exponent()
            if exponent is not None and self._supergroup._is_finite_field():
                if exponent % self.index():
                    raise ValueError(
                        "the Frobenius power is outside this open subgroup"
                    )
                return FrobeniusElement(self, exponent // self.index())
            return super()._element_constructor_(datum.exact_action())
        return super()._element_constructor_(datum, **options)

    def conjugacy_class(self):
        return OpenGaloisSubgroupConjugacyClass(self._supergroup, self.fixed_field())

    def core(self):
        if self.is_normal():
            return self
        # A non-normal open subgroup occurs only over a number field, whose
        # Sage engine names the field it is defined over by base_field().
        field = _engine_ring(self.fixed_field())
        base = _engine_ring(self._supergroup.base_field())
        defining_base = field.base_field()
        assert defining_base is base or base.absolute_degree() == 1, (
            "the represented open-subgroup core requires a relative defining polynomial over "
            "the supergroup base field, or an absolute degree-one base"
        )
        if defining_base is base:
            polynomial = field.relative_polynomial()
        else:
            polynomial = field.defining_polynomial().change_ring(base)

        normal_field, base_backend = polynomial.splitting_field(
            "normal_closure", map=True
        )
        normal_field = _own_ring(normal_field)
        base_embedding = _exact_field_morphism_from_engine(
            self._supergroup.base_field(), normal_field, base_backend
        )
        # The embeddings N -> Kbar of the normal closure extending the chosen
        # E -> Kbar through some K-embedding E -> N.
        compatible_closure_embeddings = tuple(
            normal_to_closure
            for fixed_to_normal in self.fixed_field().exact_embeddings(normal_field)
            if all(
                fixed_to_normal(self._fixed_extension.base_embedding()(generator))
                == base_embedding(generator)
                for generator in self._supergroup.base_field().field_generators()
            )
            for normal_to_closure in normal_field.exact_embeddings(
                self._supergroup.algebraic_closure()
            )
            if all(
                normal_to_closure(fixed_to_normal(generator))
                == self.embedding()(generator)
                for generator in self.fixed_field().field_generators()
            )
        )
        if not compatible_closure_embeddings:
            raise ValueError(
                "the normal closure could not be placed compatibly inside the chosen algebraic closure"
            )
        stage = self._supergroup.extension_data(
            normal_field,
            embedding=compatible_closure_embeddings[0],
            base_embedding=base_embedding,
        )
        return self._supergroup.open_subgroup(stage)

    def normalizer_quotient(self):
        r"""Return ``N_{G_K}(G_E)/G_E = Aut_K(E)`` as exact field maps.

        The infinite normalizer itself is not materialized.  The quotient is
        the finite group of exact ``K``-automorphisms of the fixed extension,
        which is canonically isomorphic to the normalizer quotient under the
        Galois correspondence.
        """
        return FiniteExtensionAutomorphismGroup(self.fixed_extension())

    def __le__(self, other) -> bool:
        if other not in OpenAbsoluteGaloisSubgroups() or other.supergroup() is not self.supergroup():
            return False
        for embedding in other.fixed_field().exact_embeddings(self.fixed_field()):
            if all(
                self.embedding()(embedding(generator)) == other.embedding()(generator)
                for generator in other.fixed_field().field_generators()
            ):
                return True
        return False

    def intersection(self, other):
        if other not in OpenAbsoluteGaloisSubgroups() or other.supergroup() is not self.supergroup():
            raise ValueError(
                "open-subgroup intersection requires one supergroup Galois group"
            )
        assert _engine_ring(self.fixed_field()) in FiniteFields(), (
            "the represented open-subgroup intersection computes the compositum canonically "
            "for finite fields; other bases require explicit compositum closure data"
        )
        degree = ZZ(self.index()).lcm(ZZ(other.index()))
        return self.supergroup().open_subgroup(self.supergroup().finite_extension(degree))

    def _repr_(self) -> str:
        return f"Gal({self.algebraic_closure()} / {self.fixed_field()}) inside {self._supergroup}"


class OpenGaloisSubgroupConjugacyClass(SageObject):
    r"""The conjugacy class obtained by forgetting (E\hookrightarrow\bar K)."""

    def __init__(self, supergroup, extension_field) -> None:
        self._supergroup = supergroup
        if extension_field not in OwnedRings():
            if extension_field.base_field() is not supergroup.base_field():
                raise ValueError("the extension has the wrong supergroup base field")
            self._extension_field = extension_field.field()
            self._base_embedding = extension_field.base_embedding()
        else:
            self._extension_field = extension_field
            base_embeddings = supergroup.base_field().exact_embeddings(
                self._extension_field
            )
            if len(base_embeddings) != 1:
                raise ValueError(
                    "the K-structure must be supplied as finite extension data"
                )
            self._base_embedding = base_embeddings[0]

    def supergroup(self):
        return self._supergroup

    def ambient(self):
        r"""Return the ambient absolute Galois group ``G_K``.

        ``supergroup`` is the generic subgroup vocabulary; ``ambient`` is the
        arithmetic name retained by the open-subgroup construction data.
        """
        return self.supergroup()

    def fixed_field(self):
        return self._extension_field

    def base_embedding(self):
        return self._base_embedding

    def index(self):

        return _relative_degree(self._supergroup.base_field(), self._extension_field)

    def representative(self, embedding=None):
        if embedding is None:
            candidates = [
                candidate
                for candidate in self._extension_field.exact_embeddings(
                    self._supergroup.algebraic_closure()
                )
                if all(
                    candidate(self._base_embedding(generator))
                    == self._supergroup.base_embedding()(generator)
                    for generator in self._supergroup.base_field().field_generators()
                )
            ]
            if not candidates:
                raise ValueError(
                    "the K-extension has no compatible embedding in the chosen closure"
                )
            embedding = candidates[0]
        stage = self._supergroup.extension_data(
            self._extension_field,
            embedding=embedding,
            base_embedding=self._base_embedding,
        )
        return self._supergroup.open_subgroup(stage)

    def __eq__(self, other) -> bool:
        if not isinstance(other, OpenGaloisSubgroupConjugacyClass):
            return False
        if other._supergroup is not self._supergroup or other.index() != self.index():
            return False
        return any(
            all(
                isomorphism(self._base_embedding(generator))
                == other._base_embedding(generator)
                for generator in self._supergroup.base_field().field_generators()
            )
            for isomorphism in self._extension_field.exact_embeddings(
                other._extension_field
            )
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self.index()))

    def _repr_(self) -> str:
        return (
            f"Conjugacy class of index-{self.index()} open subgroups of "
            f"{self._supergroup} corresponding to {self._extension_field}"
        )



__all__ = [
    "AbsoluteGaloisGroup",
    "AbsoluteGaloisGroupElement",
    "AbsoluteGaloisSliceAutomorphism",
    "ElementConjugacyClass",
    "FrobeniusElement",
    "OpenAbsoluteGaloisSubgroup",
    "OpenGaloisSubgroupConjugacyClass",
    "OpenSubgroupInclusion",
]
