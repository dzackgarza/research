r"""The absolute Galois group parent with chosen realization.

\(G_K=\operatorname{Gal}(\bar K/K)\) is a profinite group, the inverse
limit of the finite Galois groups \(\operatorname{Gal}(L/K)\).  This
parent models the *based* object
\[
G_{K,\bar K,\iota}:=\operatorname{Aut}_{\iota(K)}(\bar K),
\qquad
\iota:K\hookrightarrow\bar K,
\]
exactly analogous to defining \(\pi_1(X,\bar x)\) after choosing a
geometric basepoint.  Changing \(\bar x\) changes the concrete group by
an isomorphism well-defined only up to inner automorphism.

The concrete realization is the default.  The parent chooses
\(\bar K\) and \(\iota\) at construction time — using Sage's existing
``K.algebraic_closure()`` and a deterministic choice policy — and
records them as inspectable state.  Conjugacy classes and
choice-independent invariants are first-class *projections* of the
concrete objects, not the only interface.
"""

from collections.abc import Iterator
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput

from sage.rings.integer_ring import ZZ as SageZZ
from dzack_research.preamble.lexicon import Element

if TYPE_CHECKING:
    from sage.rings.number_field.galois_group import GaloisGroup_v2, GaloisGroupElement
    from sage.sets.family import Family
    from dzack_research.preamble.categories.group.profinite.galois_choice_policy import (
        GaloisChoicePolicy,
    )
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.rings.integer import Integer
    from sage.categories.rings import Ring
    from dzack_research.preamble.lexicon import RingElement
from dzack_research.preamble.categories.group.profinite.absolute_galois_group_element import AbsoluteGaloisGroupElement
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category_singleton
from sage.categories.fields import Fields as SageFields
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism
from sage.rings.infinity import Infinity
from sage.structure.parent import Parent


class FrobeniusElement(Morphism):
    r"""The Frobenius automorphism \(x\mapsto x^{q}\) of a finite field.

    A group element of \(G_K\) *is* a field automorphism fixing \(K\);
    the map on elements is the morphism itself.  Concrete for finite
    fields and their powers.
    """

    def __init__(self, parent: "Parent", field_order: "Integer") -> None:
        field = parent.base_field()
        Morphism.__init__(self, Hom(field, field, SageFields()))
        self._field_order = field_order

    def _call_(self, element: "Element") -> "Element":
        r"""Return \(x^{q}\)."""
        image: "Element" = element**self._field_order
        return image

    def _repr_(self) -> str:
        return f"Arithmetic Frobenius (x |-> x^{self._field_order})"

    def __hash__(self) -> int:
        return hash((type(self), self._field_order))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._field_order == other._field_order
            and self.domain() == other.domain()
        )


class RealizedAbsoluteGaloisGroups(Category_singleton):
    r"""The absolute Galois group \(G_K=\operatorname{Gal}(\bar K/K)\) with
    its realization chosen.

    :class:`AbsoluteGaloisGroups` states the interface.  This level adds the
    chosen realization: an algebraic closure \(\bar K\), an embedding
    \(\iota:K\hookrightarrow\bar K\), and a :class:`GaloisChoicePolicy`.
    Those are the data it introduces, and they are inspectable through
    :meth:`algebraic_closure`, :meth:`base_embedding` and
    :meth:`choice_data`.  The realization is not canonical in the
    mathematical sense, but it is reproducible: the same construction yields
    the same choices.

    The computational content is supplied through finite quotients and
    field-specific structure, not through generic elements.  The identity is
    canonical; ``an_element()`` returns it.  ``gens()`` raises
    :exc:`NotImplementedError` for a generic field, and the finite-field
    subcategory below answers it.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "realized absolute Galois groups"

    def super_categories(self) -> list:
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import AbsoluteGaloisGroups

        return [AbsoluteGaloisGroups()]

    class ParentMethods:
        if TYPE_CHECKING:
            # Supplied by ``AbsoluteGaloisGroups().ParentMethods``: the
            # finite coordinates are declared one level up.
            def finite_quotient(self, L: "Ring") -> "GaloisGroup_v2": ...

        def __init__(
            self,
            field: "Ring",
            closure: "Ring | None" = None,
            embedding: "Morphism | None" = None,
            choice_policy: "GaloisChoicePolicy | None" = None,
            **rest: "ConstructionData",
        ) -> None:
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.group.profinite.galois_choice_policy import default_choice_policy
            from dzack_research.preamble.categories.rings.rings import engine_ring

            self._field = field
            computation_field = engine_ring(field)

            # Choose the algebraic closure
            if closure is None:
                closure = computation_field.algebraic_closure()
            self._closure = closure

            # Choose the base embedding iota: K -> bar K
            if choice_policy is None:
                choice_policy = default_choice_policy()
            self._choice_policy = choice_policy

            if embedding is None:
                embedding = choice_policy.choose_embedding(computation_field, closure)
            self._embedding = embedding

            super().__init__(**rest)

        def base_field(self) -> "Ring":
            r"""Return \(K\), the field this is the absolute Galois group of."""
            return self._field

        def algebraic_closure(self) -> "Ring":
            r"""Return \(\bar K\), the chosen algebraic closure of \(K\)."""
            return self._closure

        def base_embedding(self) -> "Morphism":
            r"""Return \(\iota:K\hookrightarrow\bar K\), the chosen base embedding."""
            return self._embedding

        def choice_policy(self) -> "GaloisChoicePolicy":
            r"""Return the :class:`GaloisChoicePolicy` governing realization choices."""
            return self._choice_policy

        def choice_data(self) -> dict:
            r"""Return a dict of all realization choices: closure, embedding, policy."""
            return {
                "closure": self._closure,
                "embedding": self._embedding,
                "choice_policy": self._choice_policy,
            }

        def has_canonical_realization(self) -> bool:
            r"""Return whether the realization is mathematically canonical.

            Deliberately a stronger property than "Sage has chosen a preferred
            realization."  For a finite field the Frobenius is canonical; for
            most other fields the realization is chosen, not canonical.
            """
            return False

        def geometric_point(self) -> "Morphism":
            r"""Return the geometric point \(\iota:K\hookrightarrow\bar K\).

            Under the étale fundamental group identification
            \(\pi_1(\operatorname{Spec}K,\iota)\cong G_K\), the base
            embedding *is* the geometric point.
            """
            return self._embedding

        def one(self) -> Morphism:
            r"""Return the identity automorphism, the group's identity element."""
            return FrobeniusElement(self, SageZZ.one())

        def an_element(self) -> Morphism:
            r"""Return the identity; no canonical nontrivial element exists generically."""
            return self.one()

        def __contains__(self, element: "MembershipInput") -> bool:
            r"""Return whether ``element`` is a field automorphism of the base field."""
            if not isinstance(element, Morphism):
                return False
            if element.domain() != self._field or element.codomain() != self._field:
                return False
            return True

        def _finite_galois_extensions(self) -> "Iterator[Ring | None]":
            r"""Yield finite Galois extensions \(L/K\subset\bar K\), lazily.

            For a number field, enumerate by degree.  For a finite field,
            enumerate by extension degree.  This is the supply for
            :meth:`topological_generating_family`.
            """
            degree = 1
            while True:
                yield self.algebraic_closure().subfield_degree(degree)
                degree += 1

        def _normal_closure_containing(
            self, stage: "Ring", alpha: "RingElement"
        ) -> "Ring":
            r"""Return a finite normal extension \(M/K\) with \(\mathrm{stage}(\alpha)\subset M\subset\bar K\).

            Internal helper for :class:`AbsoluteGaloisGroupElement._call_`.

            Refuses.  The extension mechanics the caller needs are in place
            (:func:`extensions_along` solves \(\sigma\circ j=j\circ\tau\) for
            \(\sigma\)); what is missing is the closure itself, which has to
            place \(M\) *inside the chosen* \(\bar K\) so that successive
            forcings compose.  Choosing that placement is the open part
            (dzackgarza/research#356).
            """
            raise NotImplementedError(
                f"the normal closure of {stage} and {alpha} inside "
                f"{self._closure} is not yet placed for "
                f"{type(self._field).__name__} (dzackgarza/research#356)"
            )

        def __hash__(self) -> int:
            return hash((type(self), self._field))

        def __eq__(self, other: "MembershipInput") -> bool:
            return type(other) is type(self) and self._field == other._field

        def _repr_(self) -> str:
            return f"Absolute Galois group of {self._field}"


class AbsoluteGaloisGroupsOfFiniteFields(Category_singleton):
    r"""The absolute Galois group of a finite field \(K=\mathbb{F}_q\).

    \(G_K\cong\hat{\mathbb{Z}}\), with canonical topological generator
    \(\operatorname{Frob}_q:x\mapsto x^q\).  Frobenius is an actual
    element here, not a conjugacy class: the absolute Galois group of a
    finite field is procyclic and the Frobenius is canonical.

    Deliberately uses ``topological_generators()`` (not ``gens()``):
    \(G_{\mathbb{F}_q}\cong\hat{\mathbb{Z}}\) is topologically generated
    by Frobenius but not abstractly cyclic.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "absolute Galois groups of finite fields"

    def super_categories(self) -> list:
        return [RealizedAbsoluteGaloisGroups()]

    class ParentMethods:
        def frobenius(self) -> FrobeniusElement:
            r"""Return the arithmetic Frobenius \(x\mapsto x^q\), the canonical topological generator."""
            return FrobeniusElement(self, SageZZ(self.base_field().order()))

        def topological_group_generators(self) -> "Iterator[FrobeniusElement]":
            r"""Yield the canonical topological generator \(\operatorname{Frob}_q\)."""
            yield self.frobenius()

        def is_abelian(self) -> bool:
            r"""Return ``True``; \(G_{\mathbb{F}_q}\cong\hat{\mathbb{Z}}\) is procyclic."""
            return True

        def has_canonical_realization(self) -> bool:
            r"""Return ``True``; the Frobenius generator is canonical for \(\mathbb{F}_q\)."""
            return True


class LiftCoset:
    r"""The open coset \(g\cdot G_L\) of all lifts of a finite-quotient element.

    Canonical once \(L\subset\bar K\) is fixed; the coset is the set of
    all automorphisms of \(\bar K\) restricting to a given \(\sigma\) on
    \(L\).  ``lift`` on \(G_K\) picks a representative;
    this object is the invariant.
    """

    def __init__(
        self,
        ambient: "Parent",
        sigma: "Morphism",
        extension: "Ring | None",
    ) -> None:
        self._ambient = ambient
        self._sigma = sigma
        self._extension = extension

    def ambient(self) -> "Parent":
        return self._ambient

    def representative(self) -> AbsoluteGaloisGroupElement:
        return self._ambient.lift(self._sigma)

    def extension(self) -> "Ring | None":
        return self._extension

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._sigma))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._sigma == other._sigma
        )

    def _repr_(self) -> str:
        return f"Lift coset of {self._sigma} in {self._ambient}"


def absolute_galois_group_category(field: "Ring") -> Category_singleton:
    r"""Return the category \(G_K\) is built in, which the field decides.

    A finite field has a canonical Frobenius, so its absolute Galois group
    answers for a generating set; every other field reaches only the general
    realized node.
    """
    from sage.rings.finite_rings.finite_field_base import FiniteField

    if isinstance(field, FiniteField):
        return AbsoluteGaloisGroupsOfFiniteFields()
    return RealizedAbsoluteGaloisGroups()


def absolute_galois_group(
    field: "Ring", **kwargs: "Ring | Morphism | GaloisChoicePolicy | None"
) -> Parent:
    r"""Return \(G_K=\operatorname{Gal}(\bar K/K)\) with chosen realization."""
    return object_of(
        absolute_galois_group_category(field),
        field=field,
        cardinality=Infinity,
        **kwargs,
    )
