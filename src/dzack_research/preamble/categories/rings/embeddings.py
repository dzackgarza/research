r"""Exact embeddings of number fields and number-field orders."""

from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings as SageRings
from sage.categories.map import Map
from sage.misc.cachefunc import cached_function
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.rings import engine_ring


class NumberFieldEmbedding(Morphism):
    r"""An exact field embedding between owned number fields."""

    def __init__(self, parent, engine_morphism) -> None:
        Morphism.__init__(self, parent)
        if not isinstance(engine_morphism, Map):
            raise TypeError("a number-field embedding is represented by an exact ring morphism")
        if engine_ring(engine_morphism.domain()) is not engine_ring(self.domain()):
            raise ValueError("the engine embedding has the wrong domain")
        if engine_ring(engine_morphism.codomain()) is not engine_ring(self.codomain()):
            raise ValueError("the engine embedding has the wrong codomain")
        self._engine_morphism = engine_morphism

    def engine_morphism(self):
        return self._engine_morphism

    def __call__(self, element):
        r"""Apply the exact embedding to an element of the owned facade field.

        Owned number fields are facade parents: their elements retain the
        native Sage number field as concrete parent.  Going through Sage's
        generic ``Map.__call__`` would therefore ask for an irrelevant
        conversion map from the engine field to its owned facade before the
        actual field embedding runs.  The mathematical map is already the
        exact engine embedding, so cross that boundary directly.
        """
        return self._call_(element)

    def _call_(self, element):
        source = engine_ring(self.domain())
        target = engine_ring(self.codomain())
        return target(self._engine_morphism(source(element)))

    def is_injective(self) -> bool:
        return True

    def __mul__(self, other):
        if not isinstance(other, NumberFieldEmbedding) or other.codomain() is not self.domain():
            return NotImplemented
        target = self.codomain()
        source = other.domain()
        if engine_ring(source) is SageQQ:
            return number_field_homset(source, target)(
                engine_ring(source).hom(engine_ring(target))
            )
        primitive = source.primitive_element()
        return number_field_homset(source, target)(self(other(primitive)))


class NumberFieldHomset(Homset):
    Element = NumberFieldEmbedding

    def __init__(self, domain, codomain) -> None:
        Homset.__init__(self, domain, codomain, category=SageRings())

    def _element_constructor_(self, datum):
        if isinstance(datum, NumberFieldEmbedding):
            if datum.parent() is self:
                return datum
            datum = datum.engine_morphism()
        if isinstance(datum, Map):
            return self.element_class(self, datum)

        engine_domain = engine_ring(self.domain())
        engine_codomain = engine_ring(self.codomain())
        if engine_domain is SageQQ:
            return self.element_class(self, engine_domain.hom(engine_codomain))
        image = datum(self.domain().primitive_element()) if callable(datum) else datum
        return self.element_class(
            self,
            engine_domain.hom([engine_codomain(image)], engine_codomain),
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        engine = engine_ring(self.domain())
        if engine is SageQQ:
            return self(engine.hom(engine))
        return self(self.domain().primitive_element())

    def embeddings(self):
        return tuple(
            self(engine_embedding)
            for engine_embedding in engine_ring(self.domain()).embeddings(
                engine_ring(self.codomain())
            )
        )

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"


@cached_function
def number_field_homset(domain, codomain) -> NumberFieldHomset:
    return NumberFieldHomset(domain, codomain)


class OrderEmbedding(Morphism):
    r"""A unital embedding of orders, represented by its fraction-field extension."""

    def __init__(self, parent, field_embedding: NumberFieldEmbedding) -> None:
        Morphism.__init__(self, parent)
        source_field = self.domain().fraction_field()
        target_field = self.codomain().fraction_field()
        if engine_ring(field_embedding.domain()) is not engine_ring(source_field):
            raise ValueError("the field embedding does not extend this source order")
        if engine_ring(field_embedding.codomain()) is not engine_ring(target_field):
            raise ValueError("the field embedding does not land in this target order's field")
        for basis_element in self.domain().integral_basis():
            image = field_embedding.engine_morphism()(
                engine_ring(source_field)(basis_element)
            )
            if image not in self.codomain():
                raise ValueError("the field embedding does not carry the source order into the target order")
        self._field_embedding = field_embedding

    def field_embedding(self) -> NumberFieldEmbedding:
        return self._field_embedding

    def __call__(self, element):
        r"""Apply the order embedding without facade-parent coercion discovery."""
        return self._call_(element)

    def _call_(self, element):
        source_field = engine_ring(self.domain().fraction_field())
        image = self.field_embedding().engine_morphism()(source_field(element))
        return engine_ring(self.codomain())(image)

    def is_injective(self) -> bool:
        return True

    def __mul__(self, other):
        if not isinstance(other, OrderEmbedding) or other.codomain() is not self.domain():
            return NotImplemented
        return order_homset(other.domain(), self.codomain())(
            self.field_embedding() * other.field_embedding()
        )


class OrderHomset(Homset):
    Element = OrderEmbedding

    def __init__(self, domain, codomain) -> None:
        Homset.__init__(self, domain, codomain, category=SageRings())

    def _element_constructor_(self, field_embedding):
        source_field = self.domain().fraction_field()
        target_field = self.codomain().fraction_field()
        if not isinstance(field_embedding, NumberFieldEmbedding):
            field_embedding = number_field_homset(source_field, target_field)(field_embedding)
        elif (
            field_embedding.domain() is not source_field
            or field_embedding.codomain() is not target_field
        ):
            field_embedding = number_field_homset(source_field, target_field)(
                field_embedding.engine_morphism()
            )
        return self.element_class(self, field_embedding)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        field = self.domain().fraction_field()
        return self(number_field_homset(field, field).identity())

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"


@cached_function
def order_homset(domain, codomain) -> OrderHomset:
    return OrderHomset(domain, codomain)


__all__ = [
    "NumberFieldEmbedding",
    "NumberFieldHomset",
    "OrderEmbedding",
    "OrderHomset",
    "number_field_homset",
    "order_homset",
]
