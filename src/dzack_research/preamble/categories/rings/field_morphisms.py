r"""Exact morphisms of owned fields with private Sage-map backends.

The owned scalar parents are facades over Sage computation fields.  A native
Sage field map therefore has engine fields as its endpoints, while the public
map must have the corresponding owned fields as endpoints.  The classes here
cross precisely that boundary without replacing an embedding by a numerical
approximation or by descriptive metadata.
"""

from sage.categories.fields import Fields as SageFields
from sage.categories.finite_fields import FiniteFields as SageFiniteFields
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.rings.rational_field import QQ as SageQQ
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField_generic
from sage.rings.infinity import Infinity
from sage.rings.qqbar import AlgebraicField_common

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import OwnedFields, _engine_element, _engine_ring, _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def _uses_generator_comparison(field) -> bool:
    r"""Whether this adapter reads a finite determining family from the engine.

    Number fields and finite fields supply algebraic generators.  A native
    ngens() on an analytic or completed field need not count generators as
    an abstract field, so it is not used to decide this question.  Other
    realizations use the exact map backend's comparison instead.
    """
    engine = _engine_ring(field)
    return engine is SageQQ or engine in SageFiniteFields() or engine in SageNumberFields()


def _native_field_generators(engine):
    r"""Generators over the prime field, including each relative tower level."""
    match engine:
        case _ if engine is SageQQ:
            return (engine.one(),)
        case _ if engine in SageFiniteFields():
            return tuple(engine.gens())
        case _:
            return tuple(engine.gens()) + tuple(
                engine(generator)
                for generator in _native_field_generators(engine.base_field())
            )


def _field_generators(field):
    r"""A finite determining family for a represented finite or number field."""
    assert _uses_generator_comparison(field), (
        f"cannot list field generators of {field}: generators are computed only for finite fields "
        f"and number fields, and {field} is neither"
    )
    return finite_ordered_set(tuple(
        _owned_engine_element(field, generator)
        for generator in _native_field_generators(_engine_ring(field))
    ))


class ExactFieldMorphism(Morphism):
    r"""A field morphism with owned endpoints and an exact Sage field map retained privately.

    The private map is admitted by the exact field Mor's element constructor,
    which checks it is a field homomorphism between the engine fields of the
    endpoints.
    """

    def __init__(self, parent, engine_morphism: Map) -> None:
        Morphism.__init__(self, parent)
        self._engine_morphism = engine_morphism

    def _engine_morphism_crossing(self) -> Map:
        r"""Return the private exact Sage field-map realization.

        This is the implementation endpoint of
        :func:\`_engine_exact_field_morphism\`; ordinary mathematical
        consumers use this morphism itself.
        """
        return self._engine_morphism

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        source = _engine_ring(self.domain())
        target = _engine_ring(self.codomain())
        backend_element = _engine_element(self.domain(), self.domain()(element))
        image = target(self._engine_morphism(source(backend_element)))
        return _owned_engine_element(self.codomain(), image)

    def is_injective(self) -> bool:
        return True

    def inverse(self):
        r"""Return the inverse exact field morphism of this field automorphism."""
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no inverse as a field automorphism: its domain {self.domain()} "
                f"differs from its codomain {self.codomain()}"
            )
        backend = self._engine_morphism_crossing().inverse()
        return self.domain().exact_morphisms_to(self.domain())(backend)

    def agrees_on_field(self, other) -> bool:
        r"""Whether two exact maps with the same endpoints agree.

        On a finite or number field the full tower generating family
        determines the map; other realizations use exact equality of their represented maps.
        """
        if (
            self.domain() is not other.domain()
            or self.codomain() is not other.codomain()
        ):
            return False
        if self._engine_morphism_crossing() is other._engine_morphism_crossing():
            return True
        if _uses_generator_comparison(self.domain()):
            return all(
                self(generator) == other(generator)
                for generator in self.domain().field_generators()
            )
        return bool(self._engine_morphism_crossing() == other._engine_morphism_crossing())

    def __eq__(self, other) -> bool:
        return isinstance(other, ExactFieldMorphism) and self.agrees_on_field(other)

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        r"""The values on the source's generators; a constant on an algebraic closure, compatible with backend equality."""
        signature = (
            tuple(self(generator) for generator in self.domain().field_generators())
            if _uses_generator_comparison(self.domain())
            else ("backend",)
        )
        return hash(
            (
                type(self),
                id(self.domain()),
                id(self.codomain()),
                signature,
            )
        )

    def _composition(self, right):
        r"""``self ∘ right`` for an exact field map ``right``, composed on the backends.

        Sage's ``Map.__mul__`` has checked that ``right`` is a map into this
        map's domain.
        """
        source = right.domain()
        if source not in OwnedFields() or right.parent() is not source.exact_morphisms_to(self.domain()):
            return NotImplemented
        backend = self._engine_morphism_crossing() * right._engine_morphism_crossing()
        return source.exact_morphisms_to(self.codomain())(backend)

    def restrict_along(self, embedding):
        r"""Solve ``j tau = self j`` for the exact restriction ``tau``."""
        candidates = embedding.domain().exact_embeddings(embedding.domain())
        generators = embedding.domain().field_generators()
        restrictions = [
            candidate
            for candidate in candidates
            if all(
                embedding(candidate(generator)) == self(embedding(generator))
                for generator in generators
            )
        ]
        if len(restrictions) != 1:
            raise ValueError(
                f"the automorphism {self} does not restrict along {embedding} to a unique automorphism "
                f"of {embedding.domain()}: {len(restrictions)} automorphisms are compatible with it"
            )
        return restrictions[0]

    def extensions_along(self, embedding, candidates):
        r"""Return the candidate extensions ``sigma`` satisfying ``sigma j = j self``."""
        generators = embedding.domain().field_generators()
        matches = [
            candidate
            for candidate in candidates
            if all(
                candidate(embedding(generator)) == embedding(self(generator))
                for generator in generators
            )
        ]
        return finite_ordered_set(matches)

    def _repr_(self) -> str:
        if not _uses_generator_comparison(self.domain()):
            return f"Exact field morphism {self.domain()} -> {self.codomain()}"
        images = ", ".join(
            f"{generator} -> {self(generator)}"
            for generator in self.domain().field_generators()
        )
        return f"Exact field morphism {self.domain()} -> {self.codomain()} ({images})"


class _ExactFieldMor(CategoricalMor):
    Element = ExactFieldMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalMor.__init__(
            self, mor_family, domain, codomain
        )

    def _element_constructor_(self, datum):
        r"""Admit an exact field map between these endpoints, or a Sage field homomorphism between their engine fields."""
        if isinstance(datum, ExactFieldMorphism):
            if datum.parent() is self:
                return datum
            datum = datum._engine_morphism_crossing()
        if not isinstance(datum, Map):
            raise TypeError(
                f"cannot form a field morphism {self.domain()} -> {self.codomain()} from {datum!r}: "
                f"it is a {type(datum).__name__}, not a map"
            )
        if not datum.parent().mor_category().is_subcategory(SageFields()):
            raise TypeError(
                f"cannot form a field morphism {self.domain()} -> {self.codomain()} from {datum}: "
                f"it is a morphism in {datum.parent().mor_category()}, not a homomorphism of fields"
            )
        if _engine_ring(datum.domain()) is not _engine_ring(self.domain()):
            raise ValueError(
                f"cannot form a field morphism {self.domain()} -> {self.codomain()} from {datum}: "
                f"its domain is {datum.domain()}, not {self.domain()}"
            )
        if _engine_ring(datum.codomain()) is not _engine_ring(self.codomain()):
            raise ValueError(
                f"cannot form a field morphism {self.domain()} -> {self.codomain()} from {datum}: "
                f"its codomain is {datum.codomain()}, not {self.codomain()}"
            )
        return self.element_class(self, datum)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        engine = _engine_ring(self.domain())
        return self(engine.mor(engine))

    def _repr_(self) -> str:
        return f"Exact field morphisms from {self.domain()} to {self.codomain()}"

def _exact_field_morphism_from_engine(domain, codomain, backend) -> ExactFieldMorphism:
    r"""Wrap an exact Sage field map with the stated owned endpoints."""
    domain = _own_ring(domain)
    codomain = _own_ring(codomain)
    return domain.exact_morphisms_to(codomain)(backend)


def _exact_embeddings(domain, codomain):
    r"""Return all exact embeddings of ``domain`` into ``codomain``, as Sage's ``embeddings`` enumerates them."""
    domain = _own_ring(domain)
    codomain = _own_ring(codomain)
    backends = tuple(_engine_ring(domain).embeddings(_engine_ring(codomain)))
    return finite_ordered_set(
        tuple(
            _exact_field_morphism_from_engine(domain, codomain, backend)
            for backend in backends
        )
    )


__all__ = [
    "ExactFieldMorphism",
]
