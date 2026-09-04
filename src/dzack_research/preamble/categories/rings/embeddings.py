r"""Exact embeddings of number fields and number-field orders."""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings as SageRings
from sage.categories.sets_cat import Sets as SageSets
from sage.categories.map import Map
from sage.misc.cachefunc import cached_function
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.rings.number_fields import OwnedNumberFields
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedOrders,
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


class NumberFieldEmbedding(Morphism):
    r"""An exact field embedding between owned number fields."""

    def __init__(self, parent, engine_morphism) -> None:
        Morphism.__init__(self, parent)
        if not isinstance(engine_morphism, Map):
            raise TypeError("a number-field embedding is represented by an exact ring morphism")
        if _engine_ring(engine_morphism.domain()) is not _engine_ring(self.domain()):
            raise ValueError("the engine embedding has the wrong domain")
        if _engine_ring(engine_morphism.codomain()) is not _engine_ring(self.codomain()):
            raise ValueError("the engine embedding has the wrong codomain")
        self._engine_morphism = engine_morphism

    def _engine_morphism_crossing(self):
        r"""Return the private exact Sage embedding."""
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
        source = _engine_ring(self.domain())
        target = _engine_ring(self.codomain())
        backend_source = _engine_element(self.domain(), self.domain()(element))
        image = self._engine_morphism(backend_source)
        return self.codomain()._from_engine_element(target(image))

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
        if not isinstance(other, NumberFieldEmbedding) or other.codomain() is not self.domain():
            return NotImplemented
        target = self.codomain()
        source = other.domain()
        if _engine_ring(source) is SageQQ:
            return number_field_homset(source, target)(
                _engine_ring(source).hom(_engine_ring(target))
            )
        primitive = source.primitive_element()
        return number_field_homset(source, target)(self(other(primitive)))


class NumberFieldHomset(CategoricalHomset):
    Element = NumberFieldEmbedding

    def __init__(self, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(OwnedNumberFields()), domain, codomain
        )

    def _element_constructor_(self, datum):
        if isinstance(datum, NumberFieldEmbedding):
            if datum.parent() is self:
                return datum
            datum = datum._engine_morphism_crossing()
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
            raise ValueError("identity is defined on an endomorphism homset")
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


@cached_function
def number_field_homset(domain, codomain) -> NumberFieldHomset:
    return NumberFieldHomset(domain, codomain)


class OrderEmbedding(Morphism):
    r"""A unital embedding of orders, represented by its fraction-field extension."""

    def __init__(self, parent, field_embedding: NumberFieldEmbedding) -> None:
        Morphism.__init__(self, parent)
        source_field = self.domain().fraction_field()
        target_field = self.codomain().fraction_field()
        if _engine_ring(field_embedding.domain()) is not _engine_ring(source_field):
            raise ValueError("the field embedding does not extend this source order")
        if _engine_ring(field_embedding.codomain()) is not _engine_ring(target_field):
            raise ValueError("the field embedding does not land in this target order's field")
        target_engine = _engine_ring(self.codomain())
        for basis_element in self.domain().integral_basis():
            source_owned = source_field(basis_element)
            image = field_embedding._engine_morphism_crossing()(
                _engine_element(source_field, source_owned)
            )
            try:
                target_engine(image)
            except (TypeError, ValueError) as error:
                raise ValueError(
                    "the field embedding does not carry the source order into the target order"
                ) from error
        self._field_embedding = field_embedding

    def field_embedding(self) -> NumberFieldEmbedding:
        return self._field_embedding

    def __call__(self, element):
        r"""Apply the order embedding without facade-parent coercion discovery."""
        return self._call_(element)

    def _call_(self, element):
        source_field = self.domain().fraction_field()
        source_owned = source_field(self.domain()(element))
        image = self.field_embedding()._engine_morphism_crossing()(
            _engine_element(source_field, source_owned)
        )
        return self.codomain()._from_engine_element(
            _engine_ring(self.codomain())(image)
        )

    def is_injective(self) -> bool:
        return True

    def __mul__(self, other):
        if not isinstance(other, OrderEmbedding) or other.codomain() is not self.domain():
            return NotImplemented
        return order_homset(other.domain(), self.codomain())(
            self.field_embedding() * other.field_embedding()
        )


class OrderHomset(CategoricalHomset):
    Element = OrderEmbedding

    def __init__(self, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(OwnedOrders()), domain, codomain
        )

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
                field_embedding._engine_morphism_crossing()
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
