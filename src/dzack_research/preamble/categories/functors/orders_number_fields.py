r"""The fraction-field / ring-of-integers adjunction.

For number-field orders and number fields with unital embeddings,

``Frac ⊣ O``:

``Hom_NF(Frac(O), K) ≅ Hom_Ord(O, O_K)``.

An order embedding extends uniquely to fraction fields; a field embedding
restricts to maximal orders because integrality is preserved.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.rings.embeddings import (
    NumberFieldEmbedding,
    OrderEmbedding,
    number_field_homset,
    order_homset,
)
from dzack_research.preamble.categories.rings.number_fields import OwnedNumberFields
from dzack_research.preamble.categories.rings.ring_foundation import OwnedOrders, _engine_ring


class FractionFieldFunctor(Functor):
    r"""``Frac : Orders -> NumberFields``."""

    def __init__(self) -> None:
        super().__init__(OwnedOrders(), OwnedNumberFields())

    def _apply_object(self, order):
        return order.fraction_field()

    def _apply_morphism(self, embedding: OrderEmbedding):
        source = self(embedding.domain())
        target = self(embedding.codomain())
        return number_field_homset(source, target)(
            embedding.field_embedding()._engine_morphism_crossing()
        )

    def _repr_(self):
        return "Fraction-field functor"


class RingOfIntegersFunctor(Functor):
    r"""``K -> O_K : NumberFields -> Orders``."""

    def __init__(self) -> None:
        super().__init__(OwnedNumberFields(), OwnedOrders())

    def _apply_object(self, field):
        return field.ring_of_integers()

    def _apply_morphism(self, embedding: NumberFieldEmbedding):
        source = self(embedding.domain())
        target = self(embedding.codomain())
        return order_homset(source, target)(embedding)

    def chosen_preimage(self, image):
        if image not in OwnedOrders():
            raise ValueError("the image is not an owned order")
        return image.fraction_field()

    def _repr_(self):
        return "Ring-of-integers functor"


class OrderNumberFieldAdjunction(Adjunction):
    r"""``Frac ⊣ O``."""

    def __init__(self) -> None:
        super().__init__(FractionFieldFunctor(), RingOfIntegersFunctor())

    def unit(self, order):
        field = self.left_adjoint()(order)
        maximal_order = self.right_adjoint()(field)
        return order_homset(order, maximal_order)(
            number_field_homset(field, field).identity()
        )

    def counit(self, field):
        source = self.left_adjoint()(self.right_adjoint()(field))
        if _engine_ring(source) is _engine_ring(field):
            if source is field:
                return number_field_homset(field, field).identity()
            if _engine_ring(source).degree() == 1:
                return number_field_homset(source, field)(
                    _engine_ring(source).hom(_engine_ring(field))
                )
            return number_field_homset(source, field)(field.primitive_element())
        embeddings = number_field_homset(source, field).embeddings()
        if len(embeddings) != 1:
            raise ValueError("the counit requires the canonical identification Frac(O_K) = K")
        return embeddings[0]


    def _repr_(self):
        return "Fraction-field/ring-of-integers adjunction"


@cached_function
def order_number_field_adjunction() -> OrderNumberFieldAdjunction:
    return OrderNumberFieldAdjunction()


__all__ = [
    "FractionFieldFunctor",
    "OrderNumberFieldAdjunction",
    "RingOfIntegersFunctor",
    "order_number_field_adjunction",
]
