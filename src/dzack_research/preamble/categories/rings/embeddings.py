r"""Exact embeddings of number fields and number-field orders."""

from sage.categories.map import Map
from sage.misc.cachefunc import cached_function
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
)
from dzack_research.preamble.categories.rings.field_morphisms import ExactFieldMorphism
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedOrders,
    RingMorphism,
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


class NumberFieldEmbedding(ExactFieldMorphism):
    r"""An exact field embedding between owned number fields."""

    def __init__(self, parent, engine_morphism) -> None:
        domain = parent.domain()
        codomain = parent.codomain()
        if not isinstance(engine_morphism, Map):
            raise TypeError(
                f"cannot form the embedding {domain} -> {codomain} from {engine_morphism!r}: "
                f"an embedding of number fields must be a ring morphism, but this is a {type(engine_morphism).__name__}"
            )
        if _engine_ring(engine_morphism.domain()) is not _engine_ring(domain):
            raise ValueError(
                f"cannot form an embedding {domain} -> {codomain} from {engine_morphism}: "
                f"its domain is {engine_morphism.domain()}, not {domain}"
            )
        if _engine_ring(engine_morphism.codomain()) is not _engine_ring(codomain):
            raise ValueError(
                f"cannot form an embedding {domain} -> {codomain} from {engine_morphism}: "
                f"its codomain is {engine_morphism.codomain()}, not {codomain}"
            )
        ExactFieldMorphism.__init__(self, parent, engine_morphism)

    def _primitive_image_key(self):
        engine_domain = _engine_ring(self.domain())
        if engine_domain is SageQQ:
            return ()
        return self._engine_morphism(engine_domain.gen())

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, NumberFieldEmbedding)
            and other.domain() is self.domain()
            and other.codomain() is self.codomain()
            and other._primitive_image_key() == self._primitive_image_key()
        )
        return equal if op == op_EQ else not equal

    def __hash__(self):
        return hash(
            (
                id(self.domain()),
                id(self.codomain()),
                self._primitive_image_key(),
            )
        )

    def is_injective(self) -> bool:
        return True

    def __mul__(self, other):
        from dzack_research.preamble.categories.rings.ring_foundation import (
            _is_ring_map_into,
            _ring_composite,
        )

        if not _is_ring_map_into(other, self.domain()):
            return NotImplemented
        if not isinstance(other, NumberFieldEmbedding):
            return _ring_composite(self, other)
        target = self.codomain()
        source = other.domain()
        if _engine_ring(source) is SageQQ:
            return source.Mor(target)(
                _engine_ring(source).hom(_engine_ring(target))
            )
        primitive = source.primitive_element()
        return source.Mor(target)(self(other(primitive)))


class NumberFieldMor(CategoricalMor):
    Element = NumberFieldEmbedding

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    def _element_constructor_(self, datum):
        if isinstance(datum, NumberFieldEmbedding):
            if datum.parent() is self:
                return datum
            source = self.domain()
            datum = lambda element, embedding=datum: self.codomain()(
                embedding(embedding.domain()(source(element)))
            )
        if isinstance(datum, Map):
            return self.element_class(self, datum)

        engine_domain = _engine_ring(self.domain())
        engine_codomain = _engine_ring(self.codomain())
        if engine_domain is SageQQ:
            return self.element_class(self, engine_domain.hom(engine_codomain))
        image = datum(self.domain().primitive_element()) if callable(datum) else datum
        owned_image = self.codomain()(image)
        backend_image = _engine_element(self.codomain(), owned_image)
        return self.element_class(
            self,
            engine_domain.hom([backend_image], engine_codomain),
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        engine = _engine_ring(self.domain())
        if engine is SageQQ:
            return self(engine.hom(engine))
        return self(self.domain().primitive_element())

    def embeddings(self):
        # The engine hands back its own ordered listing.  That is syntactic
        # ingress, parsed once into the owned finite ordered set of arrows.
        return finite_ordered_set(
            tuple(
                self(engine_embedding)
                for engine_embedding in _engine_ring(self.domain()).embeddings(
                    _engine_ring(self.codomain())
                )
            )
        )

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"


class OrderEmbedding(RingMorphism):
    r"""A unital embedding of orders, represented by its fraction-field extension."""

    def __init__(self, parent, field_embedding: NumberFieldEmbedding) -> None:
        domain = parent.domain()
        codomain = parent.codomain()
        source_field = domain.fraction_field()
        target_field = codomain.fraction_field()
        if _engine_ring(field_embedding.domain()) is not _engine_ring(source_field):
            raise ValueError(
                f"cannot restrict {field_embedding} to the order {domain}: "
                f"its domain is {field_embedding.domain()}, not the fraction field {source_field} of that order"
            )
        if _engine_ring(field_embedding.codomain()) is not _engine_ring(target_field):
            raise ValueError(
                f"cannot restrict {field_embedding} to a morphism into the order {codomain}: "
                f"its codomain is {field_embedding.codomain()}, not the fraction field {target_field} of that order"
            )
        for basis_element in domain.integral_basis():
            source_owned = source_field(basis_element)
            image = field_embedding(source_owned)
            if image not in codomain:
                raise ValueError(
                    f"{field_embedding} does not restrict to a morphism of orders {domain} -> {codomain}: "
                    f"it sends the basis element {basis_element} to {image}, which is not in {codomain}"
                )
        self._field_embedding = field_embedding
        RingMorphism.__init__(self, parent, self._evaluate_field_embedding)

    def field_embedding(self) -> NumberFieldEmbedding:
        return self._field_embedding

    def _evaluate_field_embedding(self, element):
        source_field = self.domain().fraction_field()
        source_owned = source_field(self.domain()(element))
        image = self.field_embedding()(source_owned)
        return self.codomain()(image)

    def is_injective(self) -> bool:
        return True

    def __mul__(self, other):
        if not isinstance(other, OrderEmbedding) or other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            self.field_embedding() * other.field_embedding()
        )


class OrderMor(CategoricalMor):
    Element = OrderEmbedding

    def __init__(self, domain, codomain) -> None:
        CategoricalMor.__init__(
            self, OwnedOrders().MorCategory(), domain, codomain
        )

    def _element_constructor_(self, field_embedding):
        source_field = self.domain().fraction_field()
        target_field = self.codomain().fraction_field()
        if not isinstance(field_embedding, NumberFieldEmbedding):
            field_embedding = source_field.Mor(target_field)(field_embedding)
        elif (
            field_embedding.domain() is not source_field
            or field_embedding.codomain() is not target_field
        ):
            field_embedding = source_field.Mor(target_field)(
                lambda element, embedding=field_embedding: target_field(
                    embedding(embedding.domain()(element))
                )
            )
        return self.element_class(self, field_embedding)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(X, X), but this is Mor({self.domain()}, {self.codomain()})"
            )
        field = self.domain().fraction_field()
        return self(field.Mor(field).identity())

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"


__all__ = [
    "NumberFieldEmbedding",
    "NumberFieldMor",
    "OrderEmbedding",
    "OrderMor",
]
