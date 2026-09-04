r"""Exact field maps used by realized absolute Galois groups.

The owned scalar parents are facades over Sage computation fields.  A native
Sage field map therefore has engine fields as its endpoints, while the public
map must have the corresponding owned fields as endpoints.  The classes here
cross precisely that boundary without replacing an embedding by a numerical
approximation or by descriptive metadata.
"""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
from typing import Any, cast

from sage.categories.fields import Fields as SageFields
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function
from sage.rings.infinity import Infinity
from sage.rings.qqbar import AlgebraicField_common

from dzack_research.preamble.categories.rings.ring_foundation import _engine_element, _engine_ring, _own_ring


def field_generators(field) -> tuple:
    r"""Return exact elements which determine a unital map out of ``field``."""
    engine = _engine_ring(field)
    if isinstance(engine, AlgebraicField_common):
        raise TypeError(f"{engine} has no finite field-generating family")
    try:
        if engine.ngens() == Infinity:
            raise TypeError(f"{engine} has no finite field-generating family")
    except (AttributeError, NotImplementedError):
        pass
    try:
        if engine.is_algebraically_closed() and not engine.is_finite():
            raise TypeError(f"{engine} has no finite field-generating family")
    except (AttributeError, NotImplementedError):
        pass
    generators = tuple(engine.gens())
    if not generators:
        return (field.one(),)
    return tuple(
        field._from_engine_element(engine(generator))
        for generator in generators
    )


class ExactFieldMorphism(Morphism):
    r"""A field morphism with owned endpoints and an exact Sage map backend."""

    def __init__(self, parent, engine_morphism: Map) -> None:
        if not isinstance(engine_morphism, Map):
            raise TypeError("an exact field morphism requires a Sage map backend")
        try:
            homset_category = cast(Any, engine_morphism.parent()).homset_category()
        except AttributeError as error:
            raise TypeError(
                "an exact field morphism requires a genuine field-homomorphism backend"
            ) from error
        if not homset_category.is_subcategory(SageFields()):
            raise TypeError(
                "an exact field morphism requires a genuine field-homomorphism backend"
            )
        if _engine_ring(engine_morphism.domain()) is not _engine_ring(parent.domain()):
            raise ValueError("the exact backend has the wrong domain")
        if _engine_ring(engine_morphism.codomain()) is not _engine_ring(
            parent.codomain()
        ):
            raise ValueError("the exact backend has the wrong codomain")
        Morphism.__init__(self, parent)
        self._engine_morphism = engine_morphism

    def _engine_morphism_crossing(self) -> Map:
        r"""Return the private exact Sage field-map realization."""
        return self._engine_morphism

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        source = _engine_ring(self.domain())
        target = _engine_ring(self.codomain())
        backend_element = _engine_element(self.domain(), self.domain()(element))
        image = target(self._engine_morphism(source(backend_element)))
        return self.codomain()._from_engine_element(image)

    def is_injective(self) -> bool:
        return True

    def agrees_on_field(self, other) -> bool:
        if (
            self.domain() is not other.domain()
            or self.codomain() is not other.codomain()
        ):
            return False
        if self._engine_morphism_crossing() is other._engine_morphism_crossing():
            return True
        try:
            if self._engine_morphism_crossing() == other._engine_morphism_crossing():
                return True
        except (NotImplementedError, TypeError, ValueError):
            pass
        try:
            generators = field_generators(self.domain())
        except TypeError:
            return False
        return all(self(generator) == other(generator) for generator in generators)

    def __eq__(self, other) -> bool:
        return isinstance(other, ExactFieldMorphism) and self.agrees_on_field(other)

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        try:
            signature = tuple(
                self(generator) for generator in field_generators(self.domain())
            )
        except TypeError:
            # Exact backend equality is available even when the source has no
            # finite determining family.  A constant backend signature keeps
            # the hash compatible with that extensional equality.
            signature = ("backend",)
        return hash(
            (
                type(self),
                id(self.domain()),
                id(self.codomain()),
                signature,
            )
        )

    def __mul__(self, other):
        if (
            not isinstance(other, ExactFieldMorphism)
            or other.codomain() is not self.domain()
        ):
            return NotImplemented
        backend = self._engine_morphism_crossing() * other._engine_morphism_crossing()
        return exact_field_homset(other.domain(), self.codomain())(backend)

    def _repr_(self) -> str:
        return repr(self._engine_morphism_crossing())


class ExactFieldHomset(OwnedHomset):
    Element = ExactFieldMorphism

    def __init__(self, domain, codomain) -> None:
        Homset.__init__(self, domain, codomain, category=SageFields())

    def _element_constructor_(self, datum):
        if isinstance(datum, ExactFieldMorphism):
            if datum.parent() is self:
                return datum
            datum = datum._engine_morphism_crossing()
        return self.element_class(self, datum)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        engine = _engine_ring(self.domain())
        return self(engine.hom(engine))

    def _repr_(self) -> str:
        return f"Exact field morphisms from {self.domain()} to {self.codomain()}"


@cached_function
def exact_field_homset(domain, codomain) -> ExactFieldHomset:
    return ExactFieldHomset(domain, codomain)


def _exact_field_morphism_from_engine(domain, codomain, backend) -> ExactFieldMorphism:
    r"""Wrap an exact Sage field map with the stated owned endpoints."""
    domain = _own_ring(domain)
    codomain = _own_ring(codomain)
    return exact_field_homset(domain, codomain)(backend)


def exact_embeddings(domain, codomain) -> tuple[ExactFieldMorphism, ...]:
    r"""Return all exact embeddings of ``domain`` into ``codomain``."""
    domain = _own_ring(domain)
    codomain = _own_ring(codomain)
    source = _engine_ring(domain)
    target = _engine_ring(codomain)
    backends = tuple(source.embeddings(target))
    if not backends:
        try:
            backends = (source.mor(target),)
        except (TypeError, ValueError):
            backends = ()
    return tuple(
        _exact_field_morphism_from_engine(domain, codomain, backend) for backend in backends
    )


def first_exact_embedding(domain, codomain) -> ExactFieldMorphism:
    r"""Choose the first exact Sage embedding in its deterministic ordering."""
    embeddings = exact_embeddings(domain, codomain)
    if not embeddings:
        raise ValueError(f"no exact embedding of {domain} into {codomain} is available")
    return embeddings[0]


__all__ = [
    "ExactFieldHomset",
    "ExactFieldMorphism",
    "exact_embeddings",
    "exact_field_homset",
    "field_generators",
    "first_exact_embedding",
]
